#!/usr/bin/env python

#
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import sys
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.stat.basic.service_stats import service_stats
from nssrc.com.citrix.netscaler.nitro.resource.stat.basic.servicegroupmember_stats import servicegroupmember_stats
from nssrc.com.citrix.netscaler.nitro.resource.stat.lb.lbvserver_stats import lbvserver_stats
from nssrc.com.citrix.netscaler.nitro.resource.stat.network.Interface_stats import Interface_stats
from nssrc.com.citrix.netscaler.nitro.resource.stat.ns.ns_stats import ns_stats
from nssrc.com.citrix.netscaler.nitro.resource.stat.system.system_stats import system_stats
from nssrc.com.citrix.netscaler.nitro.resource.stat.vpn.vpn_stats import vpn_stats
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service


class stat_config :
	_ip=""
	_username=""
	_password=""

	@staticmethod
	def main(cls, args_):
		if(len(args_) < 3):
			print("Usage: run.bat <ip> <username> <password>")
			return

		config = stat_config()
		config.ip = args_[1]
		config.username = args_[2]
		config.password = args_[3] 
		try :
			client = nitro_service(config.ip,"http")
			client.set_credential(config.username,config.password)
			client.timeout = 500
			config.run_sample(client)
			client.logout()
		except nitro_exception as  e:
			print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e:         
			print("Exception::message="+str(e.args))
		return

	def statservicegrpmem(self, client) :
		try : 
			obj = servicegroupmember_stats()
			obj.servicegroupname = "svcgrp"
			obj.ip = "1.1.1.1"
			obj.port = 77
			obj1 = servicegroupmember_stats.get(client, obj)
			print("statservicegrpmem result::req="+obj1.servicegroupname+", curClintConnctions="+obj1.curclntconnections)
		except nitro_exception as e :
			print("Exception::statservicegrpmem::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::statservicegrpmem::message="+str(e.args))
		
	
	
	def statns(self, client) :
		try : 
			obj = ns_stats.get(client)
			for i in range(len(obj)) :
				print("statns result::req="+str(obj[i].httptotrxrequestbytes)+", res="+str(obj[i].httptotrxresponsebytes) +", tcpclient="+obj[i].tcpcurclientconn+ ", tcp_esta_client"+obj[i].tcpcurclientconnestablished)
		except nitro_exception as e :
			print("Exception::statns::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::statns::message="+str(e.args))
		
	
	
	def statlbvserver_byname(self, client) :
		try : 
			obj = lbvserver_stats.get(client, "lb_vip")
			print("statlbvserver_byname result::name="+obj.name+", servicetype="+obj.type +",totalpktsrecvd="+obj.totalpktsrecvd)
		except nitro_exception as e :
			print("Exception::statlbvserver_byname::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::statlbvserver_byname::message="+str(e.args))
		
	
	
	def statinterface(self, client) :
		try : 
			obj = Interface_stats.get(client, "1/1")
			print("statinterface result::id="+obj.id+", curlinkdwntime="+obj.curlinkdowntime)
		except nitro_exception as e :
			print("Exception::statinterface::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::statinterface::message="+str(e.args))
		
	
	
	def statservice_byname(self, client) :
		try : 
			obj = service_stats.get(client, "svc_1")
			print("statservice_byname result::name="+obj.name+", servicetype="+obj.servicetype +",requestbytes="+obj.totalrequestbytes)
		except nitro_exception as e :
			print("Exception::statservice_byname::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::statservice_byname::message="+str(e.args))

	def statlbvserver(self, client):
		try: 
			result = lbvserver_stats.get(client)
			print("statlbvserver result::length="+str(len(result)))
		except nitro_exception as e:
			print("Exception::statlbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e:
			print("Exception::statlbvserver::message="+str(e.args))
		
		
	def statvpn(self, client) :
		try : 
			result = vpn_stats.get(client)
			for i in range(len(result)) :
				print("statvpn result::totalcsconnsucc="+result[i].totalcsconnsucc)
		except nitro_exception as e :
			print("Exception::statvpn::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :		
			print("Exception::statvpn::message="+str(e.args))
		

	def statsystem(self, client) : 
		try : 
			obj = system_stats.get(client)
			for i in range(len(obj)) :
				print("statsystem result::cpuUsage="+obj[i].cpuusage+",Memsize(MB)="+obj[i].memsizemb+", memusage(MB)="+obj[i].memuseinmb)
		except nitro_exception as e :
			print("Exception::statsystem::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::statsystem::message="+str(e.args))
		

	def run_sample(self, client) :
		self.statlbvserver(client)
		self.statlbvserver_byname(client)
		self.statservice_byname(client)
		self.statvpn(client)
		self.statsystem(client)
		self.statinterface(client)
		self.statns(client)
		self.statservicegrpmem(client)
		
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
			stat_config().main(stat_config(),sys.argv)
	except SystemExit:
		print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")

