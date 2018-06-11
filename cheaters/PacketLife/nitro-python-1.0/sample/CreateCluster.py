#!/usr/bin/env python

#
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http:#www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import sys
import time
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.cluster.cluster import cluster
from nssrc.com.citrix.netscaler.nitro.resource.config.cluster.clusterinstance import clusterinstance
from nssrc.com.citrix.netscaler.nitro.resource.config.cluster.clusternode import clusternode
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsip import nsip
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service

# Sample code to create a two-node NetScaler cluster.

class CreateCluster :

	@staticmethod
	def main(cls, args_):
		if(len(args_) < 3):
			print("Usage: run.bat <ip> <username> <password>")
			return

        try :          
			#UPDATE THESE VARIABLES AS NEEDED
			nsipAddress0 = "10.102.201.11"
			nsipAddress1 = "10.102.201.12"
			clipAddress = "10.102.201.17"
			protocol = "http"
			uName = "nsroot"
			password = "nsroot"
			timeout = 20    # The time to wait before connecting to the cluster IP address 

			#Connect to the first appliance that you want to add to the cluster
			nonClipSession0 = nitro_service(nsipAddress0, protocol)
			nonClipSession0.login(uName, password)
		
			#Create a cluster instance			
			newClusterInstance = clusterinstance()
			newClusterInstance.clid = 1
			clusterinstance.add(nonClipSession0, newClusterInstance)
			
			#Add the appliance to the cluster
			ClusterNode0 = clusternode()
			ClusterNode0.nodeid = 0
			ClusterNode0.ipaddress = nsipAddress0
			ClusterNode0.state = "ACTIVE"
			ClusterNode0.backplane = "0/1/1"
			clusternode.add(nonClipSession0, ClusterNode0)
			
			#Add the cluster IP address
			newNSIPAddress = nsip()
			newNSIPAddress.ipaddress = clipAddress
			newNSIPAddress.netmask = "255.255.255.255"
			newNSIPAddress.type = "CLIP"
			nsip.add(nonClipSession0, newNSIPAddress)
			
			#Enable the cluster instance
			clusterinstance.enable(nonClipSession0, newClusterInstance)

			#Save the configurations
			nonClipSession0.save_config()
			
			#Warm reboot the appliance
			nonClipSession0.reboot(True)
			
			#Wait for while for the cluster IP address to be available
			time.sleep(timeout)
			
			#The cluster is created and the first node is added to the cluster. 
			#This node becomes the initial configuration coordinator of the cluster.
			
			#Log on to the cluster IP address and add the other nodes to the cluster
			
			#Connect to the cluster IP address
			clipSession = nitro_service(clipAddress, protocol)
			clipSession.login(uName, password)
			
			#Add the node to the cluster
			ClusterNode1 = clusternode()
			ClusterNode1.nodeid = 1
			ClusterNode1.ipaddress = nsipAddress1
			ClusterNode1.state = "ACTIVE"
			ClusterNode1.backplane = "1/1/1"
			clusternode.add(clipSession, ClusterNode1)
			
			#Save the configurations
			clipSession.save_config()
			
			#The second node is added to the cluster. 
			#You must now log on to the node that you have just added and join it to the cluster
			
			#Connect to the node that you have just added to the cluster
			nonClipSession1 = nitro_service(nsipAddress1, protocol)
			nonClipSession1.login(uName, password)
			
			#Join the node to the cluster
			newCluster = cluster()
			newCluster.clip = clipAddress
			newCluster.password = password
			cluster.join(nonClipSession1, newCluster)
			
			#Save the configurations
			nonClipSession1.save_config()
			
			#Warm reboot the appliance
			nonClipSession1.reboot(True)
			
			#Wait for while for the node to reboot
			time.sleep(timeout)

			#Retrieving the cluster node details
			id = 0 # node id 
			node= clusternode.get(clipSession, id)
			print("Node ID: "+ node.nodeid + " | Admin state: " + node.state + " | Backplane interface: "+ node.backplane)
						
			#Retrieving the cluster instance details
			id1 = 0# instance id 
			instance = clusterinstance.get(clipSession, id1)
			print("Cluster instance ID: "+ instance.clid + " | Operational state: " +instance.operationalstate)	

        except nitro_exception as  e:
			print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:         
			print("Exception::message="+str(e.args))

#
# Main thread of execution
#

if __name__ == '__main__':
	try:
		if len(sys.argv) != 4:
			sys.exit()
		else:
			ipaddress=sys.argv[1]
			username=sys.argv[2]
			password=sys.argv[3]
			CreateCluster().main(CreateCluster(),sys.argv)
	except SystemExit:
		print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")
