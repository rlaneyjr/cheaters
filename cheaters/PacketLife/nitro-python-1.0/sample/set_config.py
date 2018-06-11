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



from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor import lbmonitor
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_rewritepolicy_binding import lbvserver_rewritepolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.network.rnat import rnat
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsacls import nsacls
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsconfig import nsconfig
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsmode import nsmode
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nspbrs import nspbrs
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpgroup import snmpgroup
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.cache.cacheobject import cacheobject
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcipher import sslcipher
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.ssldhparam import ssldhparam
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpkcs12 import sslpkcs12
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpkcs8 import sslpkcs8
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver import sslvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver_sslcertkey_binding import sslvserver_sslcertkey_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemgroup_systemuser_binding import systemgroup_systemuser_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.vpn.vpnvserver_vpnclientlessaccesspolicy_binding import vpnvserver_vpnclientlessaccesspolicy_binding
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.resource.config.aaa.aaaglobal_aaapreauthenticationpolicy_binding import aaaglobal_aaapreauthenticationpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.aaa.aaapreauthenticationaction import aaapreauthenticationaction
from nssrc.com.citrix.netscaler.nitro.resource.config.aaa.aaapreauthenticationpolicy import aaapreauthenticationpolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwconfidfield import appfwconfidfield
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwprofile import appfwprofile
from nssrc.com.citrix.netscaler.nitro.resource.config.authentication.authenticationvserver_auditnslogpolicy_binding import authenticationvserver_auditnslogpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.authentication.authenticationvserver_authenticationlocalpolicy_binding import authenticationvserver_authenticationlocalpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup import servicegroup
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver_cmppolicy_binding import csvserver_cmppolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.filter.filterpolicy import filterpolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice import gslbservice
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbsite import gslbsite
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver import gslbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver_domain_binding import gslbvserver_domain_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver_gslbservice_binding import gslbvserver_gslbservice_binding
from nssrc.com.citrix.netscaler.nitro.resource.base.base_response import base_response
from nssrc.com.citrix.netscaler.nitro.resource.base.base_responses import base_responses
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsfeature import nsfeature
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsmode import nsmode
from nssrc.com.citrix.netscaler.nitro.resource.config.rewrite.rewritepolicy import rewritepolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.rewrite.rewriteaction import rewriteaction
import sys 

class set_config :
    def __init__(self):
        _ip=""
        _username=""
        _password=""

    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return

        config = set_config()
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

    
    def flush_cacheobj(self, client) :
        try :
            obj = cacheobject()
            obj.locator = "84467440737096"
            cacheobject.flush(client, obj) 
            print("flush_cacheobj - Done")
        except nitro_exception as e :
            print("Exception::flush_cacheobj::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::flush_cacheobj::message="+str(e.args))
           
    

    #GSLB configs for Vserver, Service and Sites
    def add_gslb_vserver(self, client) :
        try :
            gslbvserver1 = gslbvserver()	
            gslbvserver1.name = "gvip1"
            gslbvserver1.servicetype = "http"
            gslbvserver.add(client, gslbvserver1)				
            print("add_gslb_vserver - Done")
        except nitro_exception as e :
            print("Exception::add_gslb_vserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_gslb_vserver::message="+str(e.args))
        
        
        
    def set_gslb_vserver_timeout(self, client) :
        try :
            gslbvserver1 = gslbvserver()	
            gslbvserver1.name = "gvip1"
            gslbvserver1.timeout = 10			
            gslbvserver.update(client, gslbvserver1)				
            print("set_gslb_vserver_timeout - Done")
        except nitro_exception as e :
            print("Exception::set_gslb_vserver_timeout::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::set_gslb_vserver_timeout::message="+str(e.args))
    
    def unset_gslb_vserver_timeout(self, client) :
        try :
            gslbvserver1 = gslbvserver()	
            gslbvserver1.name = "gvip1"
            arr = ["timeout"]
            gslbvserver.unset(client, gslbvserver1, arr)
            print("unset_gslb_vserver_timeout - Done")
        except nitro_exception as e :
            print("Exception::unset_gslb_vserver_timeout::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::unset_gslb_vserver_timeout::message="+str(e.args))
    
    def enable_gslb_vserver(self, client) :
        try :
            gslbvserver.enable(client, "gvip1")				
            print("enable_gslb_vserver - Done")
        except nitro_exception as e :
            print("Exception::enable_gslb_vserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::enable_gslb_vserver::message="+str(e.args))
        
    def disable_gslb_vserver(self, client) :
        try :
            gslbvserver.disable(client, "gvip1")
            print("disable_gslb_vserver - Done")
        except nitro_exception as e :
            print("Exception::disable_gslb_vserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::disable_gslb_vserver::message="+str(e.args))
    
    def rename_gslb_vserver(self, client) :
        try :
            newname="newgvip1"
            gslbvserver.rename(client, "gvip1", newname)
            print("rename_gslb_vserver - Done")
        except nitro_exception as e :
            print("Exception::rename_gslb_vserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::rename_gslb_vserverr::message="+str(e.args))
        
    def add_gslb_service(self, client) :
        try :
            port=80
            no=100
            gslbservice1 = gslbservice()
            gslbservice1.servicename = "svc0"
            gslbservice1.ip = "10.102.3.239"
            gslbservice1.maxclient = no
            gslbservice1.port = port
            gslbservice1.sitename = "bangalore1"
            gslbservice1.servicetype = "http"
            gslbservice.add(client, gslbservice1)				
            print("add_gslb_service - Done")
        except nitro_exception as e :
            print("Exception::add_gslb_service::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_gslb_service::message="+str(e.args))
        
    def add_service(self, client) :
        try :
            port=80
            service1 = service()
            service1.name = "svc10"
            service1.ip = "10.102.3.23"
            service1.port = port
            service1.servicetype = "http"
            service.add(client, service1)                
            print("add_service - Done")
        except nitro_exception as e :
            print("Exception::add_service::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_service::message="+str(e.args))
        
        
    def set_gslb_service_cip(self, client) :
        try :
            gslbservice1 = gslbservice()
            gslbservice1.servicename = "svc0"
            gslbservice1.cip = "enabled"
            gslbservice.update(client, gslbservice1)
            print("set_gslb_service_cip - Done")
        except nitro_exception as e :
            print("Exception::set_gslb_service_cip::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::set_gslb_service_cip::message="+str(e.args))
        
        
    
    def unset_gslb_service_cip(self, client) :
        try :
            gslbservice1 = gslbservice()
            gslbservice1.servicename = "svc0"
            arr=["cip"]
            gslbservice.unset(client, gslbservice1, arr)
            print("unset_gslb_service_cip - Done")
        except nitro_exception as e :
            print("Exception::unset_gslb_service_cip::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::unset_gslb_service_cip::message="+str(e.args))
        
    
    def rename_gslb_service(self, client) :
        try :
            newname="newsvc0"
            gslbservice.rename(client, "svc0", newname)
            print("rename_gslb_service - Done")
        except nitro_exception as e :
            print("Exception::rename_gslb_service::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::rename_gslb_service::message="+str(e.args))
    
    def add_gslb_site(self, client) :
        try :
            gslbsite1 = gslbsite()
            gslbsite1.sitename = "bangalore1"
            gslbsite1.sitetype = "local"
            gslbsite1.metricexchange = "enabled"
            gslbsite1.siteipaddress = "10.102.3.222"
            gslbsite.add(client, gslbsite1)
            print("add_gslb_site - Done")
        except nitro_exception as e :
            print("Exception::add_gslb_site::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_gslb_site::message="+str(e.args))
    
    def set_gslb_site_metricexchange(self, client) :			
        try :
            gslbsite1  = gslbsite()
            gslbsite1.sitename = "bangalore1"
            gslbsite1.metricexchange = "enabled"
            gslbsite.update(client,gslbsite1)	
            print("set_gslb_site_metricexchange - Done")
        except nitro_exception as e :
            print("Exception::set_gslb_site_metricexchange::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::set_gslb_site_metricexchange::message="+str(e.args))

    def unset_gslb_site_metricexchange(self, client) :
        try :
            arr = ["metricexchange"]
            gslbsite1 = gslbsite()
            gslbsite1.sitename = "bangalore1"
            gslbsite.unset(client, gslbsite1, arr)	
            print("unset_gslb_site_metricexchange - Done")
        except nitro_exception as e :
            print("Exception::unset_gslb_site_metricexchange::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::unset_gslb_site_metricexchange::message="+str(e.args))

    # GSLB vserver_service binding	
    def bind_gslbvserver_gslbservice(self, client) :
        try :
            obj = gslbvserver_gslbservice_binding()
            obj.name = "gvip1"
            obj.servicename = "svc0"
            gslbvserver_gslbservice_binding.add(client, obj)
            print("bind_gslbvserver_gslbservice - Done ")			 
        except nitro_exception as e : 
            print("Exception::bind_gslbvserver_gslbservice::errorcode="+str(e.errorcode)+" , Message ="+ e.message)
        except Exception as e: 
            print("Exception::bind_gslbvserver_gslbservice::message="+str(e.args))			 
        
    def nsconfig_diff(self, client) :
        try :
            obj = nsconfig()
            result = nsconfig.diff(client, obj)
            if result :
                print("nsconfig_diff - response = " + result.get_response())
            else :
                print("nsconfig_diff - Done")
        except nitro_exception as e :
            print("Exception::nsconfig_diff::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::nsconfig_diff::message="+str(e.args))
           
    
    def update_appfwprofile (self, client) : 
        try :
            myprofile = appfwprofile()		
            a=["xml"]
            myprofile.name = "pr1"
            myprofile.type = a
            client.warning = True
            appfwprofile.update(client, myprofile)
        except nitro_exception as e :
            print("Exception::update_appfwprofile::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::update_appfwprofile::message="+str(e.args))
    
    def bindsslvs_cert (self, client) : 
        try :
            lbvs = lbvserver()
            lbvs.name = "ssl_vs"
            lbvs.servicetype = lbvserver.Servicetype.SSL
            lbvs.ipv46 = "1.1.1.1"
            lbvs.port = 443
            lbvserver.add(client, lbvs)
            obj = [sslvserver_sslcertkey_binding() for _ in range(2)]
            obj[0].vservername = "ssl_vs"
            obj[0].certkeyname = "xx"
            obj[1].vservername = "ssl_vs"
            obj[1].certkeyname = "yy"
            sslvserver_sslcertkey_binding.add(client, obj)	
            print("bindsslvs_cert - Done")
        except nitro_exception as e :
            print("Exception::bindsslvs_cert::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::bindsslvs_cert::message="+str(e.args))
        
    
    def convert_sslpkcs8 (self, client) : 
        try :
            obj = sslpkcs8()
            obj.pkcs8file = "swetha1.pk8"
            obj.keyfile = "swetha-key2.pem"
            obj.keyform = sslpkcs8.Keyform.PEM
            obj.password = "asas"
            sslpkcs8.convert(client, obj)	
            print("convert_sslpkcs8 - Done")
        except nitro_exception as e :
            print("Exception::convert_sslpkcs8::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::convert_sslpkcs8::message="+str(e.args))
        
        
    def create_sslpkcs12 (self, client) : 
        try :
            obj = sslpkcs12()
            obj.outfile = "aaa.pk12"
            obj.export = True
            obj.certfile = "cacert.pem"
            obj.keyfile = "cakey.pem"
            obj.password = "abcd"
            sslpkcs12.convert(client, obj)	
            print("create_sslpkcs12 - Done")
        except nitro_exception as e :
            print("Exception::create_sslpkcs12::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::create_sslpkcs12::message="+str(e.args))
        
    
    
    def creat_ssldhparam (self, client) : 
        try :
            obj = ssldhparam()
            obj.dhfile = "fipskey1024"
            obj.bits = 787
            ssldhparam.create(client, obj)	
            print("creat_ssldhparam - Done")
        except nitro_exception as e :
            print("Exception::creat_ssldhparam::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::creat_ssldhparam::message="+str(e.args))
        
    
    
    def bind_authvs_nspol (self, client) : 
        try :
            obj = authenticationvserver_auditnslogpolicy_binding()
            obj.name = "auth_vs"
            obj.policy = "audit_pol"
            obj.priority = 77
            authenticationvserver_auditnslogpolicy_binding.add(client, obj)			
            print("bind_authvs_nspol - Done")
        except nitro_exception as e :
            print("Exception::bind_authvs_nspol::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::bind_authvs_nspol::message="+str(e.args))
        
    
    def apply_nspbrs (self, client) : 
        try :
            nspbrs.apply(client)
            print("apply_nspbrs - Done")
        except nitro_exception as e :
            print("Exception::apply_nspbrs::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::apply_nspbrs::message="+str(e.args))
        
    
    
    def clear_nspbrs(self, client) : 
        try :
            nspbrs.clear(client)
            print("clear_nspbrs - Done")
        except nitro_exception as e :
            print("Exception::clear_nspbrs::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::clear_nspbrs::message="+str(e.args))
        
    
    
    def bind_servicegroup_server (self, client) : 
        try :
            grp = servicegroup()
            grp.servicegroupname = "svcgrp1"
            grp.servicetype = servicegroup.Servicetype.HTTP
            servicegroup.add(client, grp)
            obj = servicegroup_servicegroupmember_binding()
            obj.servicegroupname = "svcgrp1"
            obj.ip = "1.1.2.79"
            obj.port = 77
            servicegroup_servicegroupmember_binding.add(client, obj)
            print("bind_servicegroup_server - Done")
        except nitro_exception as e :
            print("Exception::bind_servicegroup_server::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::bind_servicegroup_server::message="+str(e.args))
            
    
    def bind_csvs_cmppol(self, client) :
        try :
            obj = csvserver_cmppolicy_binding()
            obj.name = "cs1"
            obj.policyname = "pdf_cmp"
            csvserver_cmppolicy_binding.add(client, obj)
            print("bind_csvs_cmppol - Done")
        except nitro_exception as e :
            print("Exception::bind_csvs_cmppol::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::bind_csvs_cmppol::message="+str(e.args))
        
    

    def Update_certkey(self, client) :
        try : 
            certkey="cert1"
            sslcertkey1 = sslcertkey()
            sslcertkey1.certkey = certkey
            sslcertkey1.cert = "/nsconfig/ssl/geetika.cert"
            sslcertkey1.key = "/nsconfig/ssl/geetika.key"
            sslcertkey1.nodomaincheck = True
            sslcertkey.change(client,sslcertkey1)
            print("Update certkey - Done")
        except nitro_exception as e : 
            print("Exception::Update certkey::rc="+str(e.errorcode)+" , Message ="+ e.message)
        except Exception as e: 
            print("Exception::Update certkey::message="+str(e.args))
         
           
    
    def add_filter_pol(self, client) :
        try :
            obj = filterpolicy()
            obj.name = "f1"
            obj.rule = "method == get && url == /testsite/*"
            obj.reqaction = "DROP"
            filterpolicy.add(client, obj)
            print("add_filter_pol - Done")
        except nitro_exception as e :
            print("Exception::add_filter_pol::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_filter_pol::message="+str(e.args))
        
    def set_filter_policy(self, client) :
        try :
            obj = filterpolicy()
            obj.name = "f2"
            obj.rule = "method == post && url == /testsite/*"
            filterpolicy.update(client, obj)
            print("set_filter_policy - Done")
        except nitro_exception as e :
            print("Exception::set_filter_policy::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::set_filter_policy::message="+str(e.args))
        
    
    
    def clearconfig(self, client) :
        try :
            var = nsconfig()
            var.level = nsconfig.Level.full
            nsconfig.clear(client, var)
            print("clearconfig - Done")
        except nitro_exception as e :
            print("Exception::clearconfig::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::clearconfig::message="+str(e.args))
        
    

    def saveconfig(self, client) :
        try :
            obj = nsconfig()
            nsconfig.save(client,obj)
            print("saveconfig - Done")
        except nitro_exception as e :
            print("Exception::saveconfig::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::saveconfig::message="+str(e.args))
        
    def renumber_nsacls(self, client) :
        try :
            nsacls.renumber(client)
            print("renumber_nsacls - Done")
        except nitro_exception as e :
            print("Exception::renumber_nsacls::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::renumber_nsacls::message="+str(e.args))
        
    
    def bind_authvs_authlocalpolicy(self, client) :
        try :
            obj = authenticationvserver_authenticationlocalpolicy_binding()
            obj.name = "auth1"
            obj.policy = "auth-localpol"
            authenticationvserver_authenticationlocalpolicy_binding.add(client, obj)
            print("bind_authvs_authlocalpolicy - Done")
        except nitro_exception as e :
            print("Exception::bind_authvs_authlocalpolicy::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::bind_authvs_authlocalpolicy::message="+str(e.args))
        
    
    
    def add_lbvserver(self, client) :
        try :
            obj = lbvserver()			
            obj.name = "lb_vip"
            obj.servicetype = lbvserver.Servicetype.HTTP
            response = lbvserver.add(client, obj)
            print("add_lbvserver - Done")
            if response.severity and response.severity =="WARNING" :
                print("\tWarning : " + response.message)
        except nitro_exception as e :
            print("Exception::add_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_lbvserver::message="+str(e.args))
        
    
    def add_sslcipher(self, client) :
        try :
            obj1 = sslcipher()
            cipher = "TLS1-AES-256-CBC-SHA"
            obj1.ciphergroupname = "mygrp1"
            obj1.ciphgrpalias = cipher
            sslcipher.add(client, obj1)
            print("add_sslcipher by cipher - Done")
        except nitro_exception as e :
            print("Exception::add_sslcipher::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_sslcipher::message="+str(e.args))
        
    

    def add_appfwprofile(self, client) :
        try :
            obj = appfwprofile()
            obj.name = "pr1"
            type_ = [appfwprofile.Type.XML]
            obj.type = type_
            appfwprofile.add(client, obj)
            print("add_appfwprofile - Done")
        except nitro_exception as e :
            print("Exception::add_appfwprofile::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_appfwprofile::message="+str(e.args))
        
    
    
    def add_snmpgroup(self, client) :
        try :
            obj = snmpgroup()
            obj.name = "snmp_grp"
            obj.securitylevel = snmpgroup.Securitylevel.noAuthNoPriv
            obj.readviewname = "tmp"
            snmpgroup.add(client,obj)
            print("add_snmpgroup - Done")
        except nitro_exception as e :
            print("Exception::add_snmpgroup::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_snmpgroup::message="+str(e.args))
        
    
    def add_monitor(self, client) :
        try :
            obj = lbmonitor()
            obj.monitorname = "dns1"
            obj.type = lbmonitor.Type.DNS
            lbmonitor.add(client,obj)
            print("add_monitor - Done")
        except nitro_exception as e :
            print("Exception::add_monitor::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_monitor::message="+str(e.args))
        
    

    def add_lbvserver_post(self, client) :
        try :
            obj = lbvserver()
            obj.name = "lb_vip_post"
            obj.servicetype = lbvserver.Servicetype.HTTP
            lbvserver.add(client,obj) 
            print("add_lbvserver_post - Done")
        except nitro_exception as e :
            print("Exception::add_lbvserver_post::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_lbvserver_post::message="+str(e.args))
        
    
    
    def add_appfw_confidField(self, client) :
        try :
            obj = appfwconfidfield()
            obj.fieldname = "ap_con"
            obj.url = "/test1"
            appfwconfidfield.add(client,obj) 
            print("add_appfw_confidField - Done")
        except nitro_exception as e :
            print("Exception::add_appfw_confidField::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_appfw_confidField::message="+str(e.args))
        
    def add_csvserver(self, client) :
        try :
            obj = csvserver()
            obj.name = "cs_vip"
            obj.servicetype = csvserver.Servicetype.HTTP
            obj.ipv46 = "9.1.1.8"
            obj.port = 80
            csvserver.add(client, obj)
            print("add_csvserver - Done")
        except nitro_exception as e :
            print("Exception::add_csvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_csvserver::message="+str(e.args))
        
    
    
    def update_lbvserver(self, client) :
        try :
            obj = lbvserver()
            obj.name = "lb_vip"
            obj.comment = "Modified the comments. update resources works fine."
            obj.lbmethod = lbvserver.Lbmethod.LEASTBANDWIDTH
            lbvserver.update(client, obj)
            print("update_lbvserver - Done")
        except nitro_exception as e :
            print("Exception::update_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::update_lbvserver::message="+str(e.args))
        
    
    
    
    def bindlbvserver_rewritepol(self, client) :
        try :
            rwact = rewriteaction()
            rwact.name = "act1"
            rwact.type = rewriteaction.Type.delete_http_header
            rwact.target = "Host"
            rewriteaction.add(client, rwact)
            rwpol = rewritepolicy()
            rwpol.name = "pol123"
            rwpol.action = "act1"
            rwpol.rule = "TRUE"
            rewritepolicy.add(client, rwpol)
            bindrwpol = lbvserver_rewritepolicy_binding()
            bindrwpol.name = "lb_vip"
            bindrwpol.policyname = "pol123"
            bindrwpol.priority = 77
            bindrwpol.bindpoint = lbvserver_rewritepolicy_binding.Bindpoint.REQUEST
            lbvserver_rewritepolicy_binding.add(client, bindrwpol)
            print("bindlbvserver_rewritepol - Done")
        except nitro_exception as e :
            print("Exception::bindlbvserver_rewritepol::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::bindlbvserver_rewritepol::message="+str(e.args))
        
    

    def add_lbvs_bulk(self, client) : 
        try :
            lb = [lbvserver() for _ in range(2)]
            lb[0].name = "lb1"
            lb[0].servicetype = lbvserver.Servicetype.HTTP
            
            lb[1].name = "lb2"
            lb[1].servicetype = lbvserver.Servicetype.SSL
            
            lbvserver.add(client, lb)
            print("add_lbvs_bulk - Done")
            lbvserver.enable(client, lb)
            print("enable bulk resources - Done")
        except nitro_exception as e :
            print("Exception::add_lbvs_bulk::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_lbvs_bulk::message="+str(e.args))
        
    
    
    def bind_systemgroup_systemuser(self, client) :
        try : 
            systemgroup_systemuser_binding1 = systemgroup_systemuser_binding()
            systemgroup_systemuser_binding1.groupname = "g1"
            systemgroup_systemuser_binding1.username = "user1"
            result = systemgroup_systemuser_binding.add(client,systemgroup_systemuser_binding1)
            print("bind_systemgroup_systemuser::rc="+result.errorcode+ ", Message ="+result.message)
        except nitro_exception as e : 
            print("Exception::bind_systemgroup_systemuser::rc="+str(e.errorcode)+" , Message ="+ e.message)
        except Exception as e: 
            print("Exception::bind_systemgroup_systemuser::message="+str(e.args))
    
    
    def bind_vpnvserver_vpnclientlessacesspolicy(self, client) :
        try :
            vpnvserver_vpnclientlessaccesspolicy_binding1 = vpnvserver_vpnclientlessaccesspolicy_binding()
            vpnvserver_vpnclientlessaccesspolicy_binding1.policy = "clientlesspol1"
            vpnvserver_vpnclientlessaccesspolicy_binding1.priority = 1
            vpnvserver_vpnclientlessaccesspolicy_binding1.name = "vpnvserver1"
            result =vpnvserver_vpnclientlessaccesspolicy_binding.add(client,vpnvserver_vpnclientlessaccesspolicy_binding1)
            print("bind_vpnvserver_vpnclientlessacesspolicy::rc="+result.errorcode+ ", Message ="+result.message)
        except nitro_exception as e : 
            print("Exception::bind_vpnvserver_vpnclientlessacesspolicy::rc="+str(e.errorcode)+" , Message ="+ e.message)
        except Exception as e: 
            print("Exception::bind_vpnvserver_vpnclientlessacesspolicy::message="+str(e.args))
    
    
    
    def addlbvserver_bindings(self, client) :
        try :
            obj = lbvserver_service_binding()
            obj.name = "lb_vip"
            obj.servicename = "svc10"
            obj.weight = 77
            lbvserver_service_binding.add(client, obj)
            lbvserver_service_binding.delete(client, obj)
            print("addlbvserver_bindings - Done")
            svc = [ service() for _ in range(2)] 
            svc[0].name = "svc_1"
            svc[0].ip = "1.1.1.1"
            svc[0].port = 80
            svc[0].servicetype = service.Servicetype.HTTP

            svc[1].name = "svc_2"
            svc[1].ip = "1.1.1.1"
            svc[1].port = 81
            svc[1].servicetype = service.Servicetype.HTTP

            bindsvc = [lbvserver_service_binding() for _ in range(2)]
            bindsvc[0].name = "lb_vip"
            bindsvc[0].servicename = "svc_1"
            bindsvc[0].weight = 20

            bindsvc[1].name = "lb_vip"
            bindsvc[1].servicename = "svc_2"
            bindsvc[1].weight = 30

            service.add(client, svc)
            lbvserver_service_binding.add(client, bindsvc)			
            print("addlbvserver_bindings - Done")
        except nitro_exception as e :
            print("Exception::addlbvserver_bindings::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::addlbvserver_bindings::message="+str(e.args))
        
    

    def enable_lbvserver(self, client) :
        try :
            lbvserver.enable(client,"lb_vip")
            print("enable_lbvserver - Done")
        except nitro_exception as e :
            print("Exception::enable_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::enable_lbvserver::message="+str(e.args))
        
    

    def disable_lbvserver(self, client) :
        try :
            lbvserver.disable(client, "lb_vip")
            print("disable_lbvserver - Done")
        except nitro_exception as e :
            print("Exception::disable_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::disable_lbvserver::message="+str(e.args))
        
    

    def rename_lbvserver(self, client, name, newname) :
        try :
            obj = lbvserver()
            obj.name = name
            lbvserver.rename(client, obj, newname)
            print("rename_lbvserver - Done")
        except nitro_exception as e :
            print("Exception::rename_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::rename_lbvserver::message="+str(e.args))

    def enable_nsfeature(self, client) :
        try : 
            feature = [nsfeature.Feature.BGP, nsfeature.Feature.REWRITE]
            client.enable_features(feature)
            print("enable_nsfeature - Done")
        except nitro_exception as e :
            print("Exception::enable_nsfeature::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::enable_nsfeature::message="+str(e.args))

    def disable_nsfeature(self, client) :
        try : 
            feature = [nsfeature.Feature.BGP, nsfeature.Feature.REWRITE]
            client.disable_features(feature)
            print("disable_nsfeature - Done")
        except nitro_exception as e :
            print("Exception::disable_nsfeature::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::disable_nsfeature::message="+str(e.args))

    def enable_nsmode(self, client) :
        try : 
            mode = [nsmode.Mode.L2, nsmode.Mode.CKA]
            client.enable_modes(mode)
            print("enable_nsmode - Done")
        except nitro_exception as e :
            print("Exception::enable_nsmode::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::enable_nsmode::message="+str(e.args))

    def disable_nsmode(self, client) :
        try : 
            mode = [nsmode.Mode.L2, nsmode.Mode.CKA]
            client.disable_modes(mode)
            print("disable_nsmode - Done")
        except nitro_exception as e :
            print("Exception::disable_nsmode::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::disable_nsmode::message="+str(e.args))
    
    def addcspolicy(self, client) : 
        try : 
            obj = cspolicy()
            obj.policyname = "cs_pol"
            obj.rule = "HTTP.REQ.HEADER(\"host\").Length != 7"
            cspolicy.add(client, obj)
            print("addcspolicy - Done")
        except nitro_exception as e :
            print("Exception::addcspolicy::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::addcspolicy::message="+str(e.args))
        
    
    
    def bind_gslbvs_domain(self, client) : 
        try : 
            obj = gslbvserver_domain_binding()
            obj.name = "gsv1"
            obj.domainname = "my.dd.com"
            gslbvserver_domain_binding.add(client, obj)
            print("bind_gslbvs_domain - Done")
        except nitro_exception as e :
            print("Exception::bind_gslbvs_domain::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::bind_gslbvs_domain::message="+str(e.args))
        
    
    
    def unbind_gslbvs_domain(self, client) : 
        try : 
            obj = gslbvserver_domain_binding()
            obj.name = "gsv1"
            obj.domainname = "my.dd.com"
            gslbvserver_domain_binding.delete(client, obj)
            print("unbind_gslbvs_domain - Done")
        except nitro_exception as e :
            print("Exception::unbind_gslbvs_domain::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::unbind_gslbvs_domain::message="+str(e.args))
        
    
    
    def forceha_sync(self, client) : 
        try : 
            client.forcehasync(True, "YES")
            print("forceha_sync - Done")
        except nitro_exception as e :
            print("Exception::forceha_sync::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::forceha_sync::message="+str(e.args))
        
    

    def forceha_failover(self, client) : 
        try : 
            client.forcehafailover(True)
            print("forceha_failover - Done")
        except nitro_exception as e :
            print("Exception::forceha_failover::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::forceha_failover::message="+str(e.args))
        
    def run_sample(self, client) :
        self.clearconfig(client)
        self.add_lbvserver(client)
        self.flush_cacheobj(client)
        self.add_gslb_vserver(client)
        self.add_gslb_site(client)
        self.add_gslb_service(client)
        self.add_service(client)
        self.bind_gslbvserver_gslbservice(client)
        self.set_gslb_vserver_timeout(client)
        self.unset_gslb_vserver_timeout(client)
        self.enable_gslb_vserver(client)
        self.disable_gslb_vserver(client)
        self.rename_gslb_vserver(client)
        self.set_gslb_service_cip(client)
        self.unset_gslb_service_cip(client)
        self.rename_gslb_service(client)
        self.set_gslb_site_metricexchange(client)
        self.unset_gslb_site_metricexchange(client)
        self.nsconfig_diff(client)
        self.saveconfig(client)
        self.add_appfwprofile(client)
        self.update_appfwprofile(client)
        self.add_monitor(client)
        self.add_appfw_confidField(client)
        self.add_lbvserver_post(client)
        self.update_lbvserver(client)
        self.addlbvserver_bindings(client)
        self.add_lbvs_bulk(client)
        self.enable_lbvserver(client)
        self.disable_lbvserver(client)
        self.rename_lbvserver(client,"lb_vip", "lb_vip2")
        self.rename_lbvserver(client,"lb_vip2", "lb_vip")
        self.saveconfig(client)	
        self.enable_nsfeature(client)
        self.disable_nsfeature(client)
        self.bindlbvserver_rewritepol(client)
        self.add_csvserver(client) 
        self.enable_nsmode(client)
        self.disable_nsmode(client)
        self.addcspolicy(client)
        self.add_snmpgroup(client)
        self.bind_gslbvs_domain(client)
        self.unbind_gslbvs_domain(client)
        self.add_sslcipher(client)
        self.bind_authvs_authlocalpolicy(client)
        self.renumber_nsacls(client)
        self.add_filter_pol(client)
        self.Update_certkey(client)
        self.bind_csvs_cmppol(client)
        self.bind_vpnvserver_vpnclientlessacesspolicy(client)
        self.bind_systemgroup_systemuser(client)
        self.bind_servicegroup_server(client)
        self.apply_nspbrs(client)
        self.clear_nspbrs(client)
        self.bind_authvs_nspol(client)
        self.set_filter_policy(client)
        self.creat_ssldhparam(client)
        self.create_sslpkcs12(client)
        self.convert_sslpkcs8(client)
        self.bindsslvs_cert(client)


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
            set_config().main(set_config(),sys.argv)
    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")
