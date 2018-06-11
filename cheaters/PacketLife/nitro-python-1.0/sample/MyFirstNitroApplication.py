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
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service

# This sample code demonstrates basic usage of the NITRO APIs
class MyFirstNitroApplication : 
	def __init__(self):
		_ip=""
		_username=""
		_password=""

	@staticmethod
	def main(cls, args_):
		if(len(args_) < 3):
			print("Usage: run.bat <ip> <username> <password>")
			return

		config = MyFirstNitroApplication()
		config.ip = args_[1]
		config.username = args_[2]
		config.password = args_[3] 
		
		try :
			
			#Create an instance of the nitro_service class to connect to the appliance
			ns_session = nitro_service(config.ip,"HTTP")
			
			ns_session.set_credential("nsroot", "nsroot")
			ns_session.timeout = 310
			#Log on to the appliance using your credentials
			ns_session.login()
			
			#Enable the load balancing feature.
			features_to_be_enabled = "lb"			
			ns_session.enable_features(features_to_be_enabled)
			
			#Create an instance of the virtual server class
			new_lbvserver_obj = lbvserver()
			
			#Create a new virtual server
			new_lbvserver_obj.name = "MyFirstLbVServer"
			new_lbvserver_obj.ipv46 = "10.102.29.88"
			new_lbvserver_obj.servicetype = "HTTP"
			new_lbvserver_obj.port = 80
			new_lbvserver_obj.lbmethod = "ROUNDROBIN"
			lbvserver.add(ns_session, new_lbvserver_obj)
					
			#Retrieve the details of the virtual server
			new_lbvserver_obj = lbvserver.get(ns_session,new_lbvserver_obj.name)
			print("Name : " +new_lbvserver_obj.name +"\n" +"Protocol : " +new_lbvserver_obj.servicetype)

			#Delete the virtual server
			lbvserver.delete(ns_session, new_lbvserver_obj.name)
			
			#Save the configurations
			ns_session.save_config()
			
			#Logout from the NetScaler appliance
			ns_session.logout()
			
		except nitro_exception as  e:
			print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e:         
			print("Exception::message="+str(e.args))
		return

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
			MyFirstNitroApplication().main(MyFirstNitroApplication(),sys.argv)
	except SystemExit:
		print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")

