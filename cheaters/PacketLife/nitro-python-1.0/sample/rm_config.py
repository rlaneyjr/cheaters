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
from nssrc.com.citrix.netscaler.nitro.resource.base.base_response import base_response
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwconfidfield import appfwconfidfield
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwprofile import appfwprofile
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup import servicegroup
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.filter.filterprebodyinjection import filterprebodyinjection
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice import gslbservice
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbsite import gslbsite
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver import gslbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver_gslbservice_binding import gslbvserver_gslbservice_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor import lbmonitor
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor_service_binding import lbmonitor_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.network.channel import channel
from nssrc.com.citrix.netscaler.nitro.resource.config.network.route6 import route6
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpengineid import snmpengineid
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpgroup import snmpgroup
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpmanager import snmpmanager
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmptrap import snmptrap
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service


class rm_config :
	def __init__(self):
		_ip=""
		_username=""
		_password=""

	@staticmethod
	def main(cls, args_):
		if(len(args_) < 3):
			print("Usage: run.bat <ip> <username> <password>")
			return

		config = rm_config()
		config.ip = args_[1]
		config.username = args_[2]
		config.password = args_[3] 
		
		try:
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
		
	def unbind_lbvserver_service(self, client):
		try:
			obj = []
			obj = [ lbvserver_service_binding() for _ in range(2)]
			obj[0].name = "lb1"
			obj[0].servicename = "svc1"
			obj[1].name = "lb2"
			obj[1].servicename = "svc2"
			lbvserver_service_binding.delete(client, obj) 
			
			lbv = lbvserver_service_binding()
			lbv.name = "lb3"
			lbv.servicename = "svc3"
			lbvserver_service_binding.delete(client, lbv) 
			print("unbind_lbvserver_service:: done")		
		except nitro_exception as e:
			print("Exception::unbind_lbvserver_service::errocode - "+str(e.errorcode)+", message - "+e.message)			
		except Exception as e:	
			print("Exception::unbind_lbvserver_service:: "+str(e.args)) 

	
	def unbind_gslbvserver_gslbservice(self, client) :
		try :
			obj = gslbvserver_gslbservice_binding()
			obj.servicename = "newsvc0"
			obj.name = "newgvip1"
			gslbvserver_gslbservice_binding.delete(client, obj)			
			print("unbind_gslbvserver_gslbservice - Done")			 
		except nitro_exception as e :
			print("Exception::unbind_gslbvserver_gslbservice::errorcode="+str(e.errorcode)+" , Message ="+ e.message)
		except Exception as e : 
			print("Exception::unbind_gslbvserver_gslbservice::message="+str(e.args))			 
		
	
	
	def rm_gslb_vserver(self, client) :
		try :
			gslbvserver.delete(client,"newgvip1")				
			print("rm_gslb_vserver - Done")
		except nitro_exception as e :
			print("Exception::rm_gslb_vserver::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_gslb_vserver::message="+str(e.args))
		
			
	def rm_gslb_service(self, client) :
		try :
			gslbservice.delete(client,"newsvc0")				
			print("rm_gslb_service - Done")
		except nitro_exception as e :
			print("Exception::rm_gslb_service::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_gslb_service::message="+str(e.args))
		
	def rm_gslb_site(self, client) :
		try :
			gslbsite.delete(client,"bangalore1")				
			print("rm_gslb_site - Done")
		except nitro_exception as e :
			print("Exception::rm_gslb_site::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_gslb_site::message="+str(e.args))
		
	def rmcsvserver_bulk_1(self, client) :
		try : 
			str_ = ["cs1","cs2","cs3","cs4","cs5"]
			csvserver.delete(client, str_)
			print("rmcsvserver_bulk::rc= done")
		except nitro_exception as e :
			print("Exception::rmcsvserver_bulk::rc="+str(e.errorcode)+" , Message ="+ e.message)
		except Exception as e : 
			print("Exception::rmcsvserver_bulk::message="+str(e.args))
		
	
	def rmcsvserver_bulk(self, client) :
		try : 
			csvs = [csvserver() for _ in range(5)]
			for i in range(0, 5) :
				csvs[i].name = "csvserver"+str(i)
			csvserver.delete(client,csvs)
			print("rmcsvserver_bulk::rc= done")
		except nitro_exception as e :
			print("Exception::rmcsvserver_bulk::rc="+str(e.errorcode)+" , Message ="+ e.message)
		except Exception as e : 
			print("Exception::rmcsvserver_bulk::message="+str(e.args))
		
		
	def rmlbvserver_bulk(self, client):
		try: 
			lbvs = []
			lbvs = [ lbvserver() for _ in range(2) ]
			for i in range(2) :
				lbvs[i].name = "lb" + str(i+3)
			lbvserver.delete(client, lbvs)
			
			lbvs = ["lb5", "lb6"]
			lbvserver.delete(client, lbvs)			
			print("rmlbvserver_bulk::rc= done")
		except nitro_exception as e:
			print("Exception::rmlbvserver_bulk::rc="+str(e.errorcode)+" , Message ="+ e.message)
		except Exception as e:
			print("Exception::rmlbvserver_bulk::message="+str(e.args))
			
	def unset_bulk_service(self, client) :
		try : 
			arr= ["cmp","cacheable","usip","healthmonitor"]
			servicegroup1= [servicegroup() for _ in range(0, 5)]		 
			for i in range(0, 5) :
				servicegroup1[i].servicegroupname = "sg_"+str(i)
				servicegroup.unset(client, servicegroup1, arr)
				print("unset_bulk_service - DONE")
		except nitro_exception as e :
			print("Exception::unset_bulk_service::rc="+str(e.errorcode)+" ,Message ="+ e.message)
		except Exception as e : 
			print("Exception::unset_bulk_service::message="+str(e.args))
			
	
	def unbind_svcgrp_svgrpmem(self, client) :
		try : 
			obj = [servicegroup_servicegroupmember_binding() for _ in range(2)]
			obj[0].servicegroupname = "sg1"
			obj[0].ip = "1.1.1.7"
			obj[0].port = 77
			
			obj[1].servicegroupname = "sg2"
			obj[1].ip = "1.1.1.8"
			obj[1].port = 78		
			servicegroup_servicegroupmember_binding.delete(client, obj)
			print("unbind_svcgrp_svgrpmem - Done")
		except nitro_exception as e :
			print("Exception:: unbind_svcgrp_svgrpmem::rc="+str(e.errorcode)+" , Message ="+ e.message)
		except Exception as e : 
			print("Exception:: unbind_svcgrp_svgrpmem::message="+str(e.args))
		
	
	
	def unset_filterprebody(self, client) :
		try : 
			obj = filterprebodyinjection.get(client)
			args = ["prebody"]
			filterprebodyinjection.unset(client, obj, args)
			print("unset_filterprebody - Done")
		except nitro_exception as e :
			print("Exception:: unset_filterprebody::rc="+str(e.errorcode)+" , Message ="+ e.message)
		except Exception as e : 
			print("Exception:: unset_filterprebody::message="+str(e.args))
	
	
	def unset_channel(self, client) :
		try : 
			obj = channel.get(client, "LA/1")
			args = ["state", "speed"]
			channel.unset(client, obj, args)
			print("unset_channel - Done")
		except nitro_exception as e :
			print("Exception:: unset_channel::rc="+str(e.errorcode)+" , Message ="+ e.message)
		except Exception as e : 
			print("Exception:: unset_channel::message="+str(e.args))

			
	def unset_snmptrap(self, client) : 
		try :
			str_ = "10.102.1.2"
			obj = snmptrap()
			obj.trapclass = "generic"
			obj.trapdestination = str_
			args = ["destport"]
			snmptrap.unset(client, obj, args)
			print("unset_snmptrap - Done")
		except nitro_exception as e :
			print("Exception::unset_snmptrap::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::unset_snmptrap::message="+str(e.args))
		

	
	
	def rm_snmpmanager(self, client) :
		try :
			str_ = "10.102.31.19"
			snmpmanager.delete(client, str_)
			print("rm_snmpmanager - Done")
		except nitro_exception as e :
			print("Exception::rm_snmpmanager::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_snmpmanager::message="+str(e.args))
		
	
	
	def rm_snmptrap(self, client) :
		try :
			str_ = "10.102.1.3"
			obj = snmptrap()
			obj.trapclass = "generic"
			obj.trapdestination = str_
			snmptrap.delete(client, obj)
			print("rm_snmptrap - Done")
		except nitro_exception as e :
			print("Exception::rm_snmptrap::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_snmptrap::message="+str(e.args))
		
	
	
	def rm_route6(self, client) :
		try :
			obj = route6()
			obj.network = "::/0"
			obj.gateway = "1234::1"
			route6.delete(client, obj)
			print("rm_route6 - Done")
		except nitro_exception as e :
			print("Exception::rm_route6::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_route6::message="+str(e.args))
		
	
	
	def rmlbvserver_spaces(self, client) :
		try :
			lbvserver.delete(client, "x y")
			print("rmlbvserver_spaces - Done")
		except nitro_exception as e :
			print("Exception::rmlbvserver_spaces::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rmlbvserver_spaces::message="+str(e.args))
		
	
	
	def rm_channel(self, client) :
		try :
			obj = channel()
			obj.id = "LA/1"
			channel.delete(client, "LA/1")
			print("rm_channel - Done")
		except nitro_exception as e :
			print("Exception::rm_channel::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_channel::message="+str(e.args))
		
	
	
	def rm_snmpgroup(self, client) :
		try :
			obj = snmpgroup()
			obj.name = "snmp_grp"
			obj.securitylevel = "noAuthNoPriv"
			snmpgroup.delete(client, obj)
			print("rm_snmpgroup - Done")
		except nitro_exception as e :
			print("Exception::rm_snmpgroup::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_snmpgroup::message="+str(e.args))
		
	
	
	def rm_appfwprofile(self, client) :
		try :
			appfwprofile.delete(client, "pr1")
			print("rm_appfwprofile - Done")
		except nitro_exception as e :
			print("Exception::rm_appfwprofile::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_appfwprofile::message="+str(e.args))
		
	
	def rmlbvserver(self, client) :
		try :
			response =lbvserver.delete(client,"lb_vip_post")
			if (response.severity and response.severity == ("WARNING")):
				print("Warning : " + response.message)
			print("rmlbvserver - Done")
		except nitro_exception as e :
			print("Exception::rmlbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rmlbvserver::message="+str(e.args))
		
	
	def rmcspolicy(self, client) :
		try :
			cspolicy.delete(client,"cs_pol")
			print("rmcspolicy - Done")
		except nitro_exception as e :
			print("Exception::rmcspolicy::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rmcspolicy::message="+str(e.args))
		
	
	
	def rmlbmonitor(self, client) :
		try :
			mon = lbmonitor()
			mon.monitorname = "dns1"
			mon.type = "DNS"
			lbmonitor.delete(client, mon)
			print("rmlbmonitor - Done")
		except nitro_exception as e :
			print("Exception::rmlbmonitor::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rmlbmonitor::message="+str(e.args))
		
	
		
	def rmcsvserver(self, client) : 
		try :
			csvserver.delete(client, "cs_vip")
			print("rmcsvserver - Done")
		except nitro_exception as e :
			print("Exception::rmcsvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rmcsvserver::message="+str(e.args))
		
	

	def unset_cspolicy_domain(self, client) :
		try :
			obj = cspolicy.get(client, "cs_pol")
			args = ["domain"]
			cspolicy.unset(client, obj, args)
			print("unset_cspolicy_domain - Done")
		except nitro_exception as e :
			print("Exception::unset_cspolicy_domain::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::unset_cspolicy_domain::message="+str(e.args))
		
	
	
	def rm_appfw_confidField(self, client) : 
		try :
			obj = appfwconfidfield()
			obj.fieldname = "ap_con"
			obj.url = "/test1"
			appfwconfidfield.delete(client, obj)
			print("rm_appfw_confidField - Done")
		except nitro_exception as e :
			print("Exception::rm_appfw_confidField::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rm_appfw_confidField::message="+str(e.args))
		
	

	def unset_lbvserver(self, client) :
		try :
			lb1 = [lbvserver() for _ in range(2)]
			lb1[0].name = "lb2"
			lb1[1].name = "lb1"
			args = ["comment", "lbmethod"]
			lbvserver.unset(client, lb1, args)			
			print("unset_lbvserver - Done")
		except nitro_exception as e :
			print("Exception::unset_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::unset_lbvserver::message="+str(e.args))
		
	

	def unset_snmp_engineId (self, client) :
		try : 
			args = ["ownerNode"]
			my_engineid = snmpengineid.get(client)
			snmpengineid.unset(client, my_engineid, args)
			print("unset_snmp_engineId - Done")
		except nitro_exception as e :
			print("Exception::unset_snmp_engineId::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::unset_snmp_engineId::message="+str(e.args))
		
	
	def run_sample(self, client):
		self.unset_lbvserver(client)		
		self.rmlbvserver(client)
		self.rmlbmonitor(client)
		self.rm_appfw_confidField(client)
		self.unset_snmp_engineId(client)
		self.rmcsvserver(client)
		self.unset_cspolicy_domain(client)
		self.rmcspolicy(client)
		self.rm_appfwprofile(client)
		self.rm_snmpgroup(client)
		self.rm_channel(client)
		#rmlbvserver_spaces(client)
		self.rm_route6(client)
		self.rm_snmptrap(client)
		self.rm_snmpmanager(client)
		self.unset_snmptrap(client)
		self.unset_filterprebody(client)
		self.unset_channel(client)
		self.unbind_svcgrp_svgrpmem(client)
		self.unset_bulk_service(client)
		self.rmlbvserver_bulk(client)
		self.rmcsvserver_bulk(client)
		self.unbind_lbvserver_service(client)
		self.rmcsvserver_bulk_1(client)
		self.unbind_gslbvserver_gslbservice(client)
		self.rm_gslb_vserver(client)
		self.rm_gslb_service(client)
		self.rm_gslb_site(client)
		
		
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
			rm_config().main(rm_config(),sys.argv)
	except SystemExit:
		print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")
