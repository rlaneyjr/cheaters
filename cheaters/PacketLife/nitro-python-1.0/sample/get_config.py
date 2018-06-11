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
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.stat.lb.lbvserver_stats import lbvserver_stats
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.util.filtervalue import filtervalue
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_cachepolicy_binding import lbvserver_cachepolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwconfidfield import appfwconfidfield
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwlearningdata import appfwlearningdata
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwlearningdata_args import appfwlearningdata_args
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwprofile import appfwprofile
from nssrc.com.citrix.netscaler.nitro.resource.config.audit.auditnslogaction import auditnslogaction
from nssrc.com.citrix.netscaler.nitro.resource.config.audit.auditsyslogparams import auditsyslogparams
from nssrc.com.citrix.netscaler.nitro.resource.config.authorization.authorizationpolicylabel_binding import authorizationpolicylabel_binding 
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_binding import service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_lbmonitor_binding import service_lbmonitor_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cache.cacheobject import cacheobject
from nssrc.com.citrix.netscaler.nitro.resource.config.cmp.cmppolicy_lbvserver_binding import cmppolicy_lbvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnsnsecrec import dnsnsecrec
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnssuffix import dnssuffix
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnsview_dnspolicy_binding import dnsview_dnspolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnszone import dnszone
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbldnsentries import gslbldnsentries
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbparameter import gslbparameter
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice import gslbservice
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice_binding import gslbservice_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbsite import gslbsite
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver import gslbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver_gslbservice_binding import gslbvserver_gslbservice_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ha.hanode import hanode
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_binding import lbvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.network.Interface import Interface
from nssrc.com.citrix.netscaler.nitro.resource.config.network.channel import channel
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsacl import nsacl
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsip import nsip
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsip_args import nsip_args
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nslimitidentifier import nslimitidentifier
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nstcpbufparam import nstcpbufparam
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsversion import nsversion
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsxmlnamespace import nsxmlnamespace
from nssrc.com.citrix.netscaler.nitro.resource.config.policy.policyexpression import policyexpression
from nssrc.com.citrix.netscaler.nitro.resource.config.policy.policyexpression_args import policyexpression_args
from nssrc.com.citrix.netscaler.nitro.resource.config.protocol.protocolhttpband import protocolhttpband
from nssrc.com.citrix.netscaler.nitro.resource.config.protocol.protocolhttpband_args import protocolhttpband_args
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpgroup import snmpgroup
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpmanager import snmpmanager
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpoid import snmpoid
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpoid_args import snmpoid_args
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmptrap import snmptrap
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpuser import snmpuser
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcipher_binding import sslcipher_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslfipskey import sslfipskey
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpolicy_binding import sslpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpolicy_csvserver_binding import sslpolicy_csvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemgroup_binding import systemgroup_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.transform.transformprofile_transformaction_binding import transformprofile_transformaction_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.vpn.vpnglobal_authenticationldappolicy_binding import vpnglobal_authenticationldappolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.vpn.vpnglobal_vpnclientlessaccesspolicy_binding import vpnglobal_vpnclientlessaccesspolicy_binding


class get_config:
    def __init__(self):
        _ip=""
        _username=""
        _password=""
     
    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return

        config = get_config()
        config.ip = args_[1]
        config.username = args_[2]
        config.password = args_[3]       
            
        client = None
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

    #Getting GSLB vserver, service and site
    def get_gslbvserver(self, client) :
        try :
            result = gslbvserver.get(client, "newgvip1")
            if result :
                print("get_gslbvserver - name= "+result.name + ", servicetype= " + result.servicetype)
            else :
                print("get_gslbvserver - Done")
        except nitro_exception as e :
            print("Exception::get_gslbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :
            print("Exception::get_gslbvserver::message="+str(e.args))
     
    def get_gslbservice(self, client) :
        try :
            result = gslbservice.get(client, "newsvc0")
            if result :            
                print("get_gslbservice - servicename= "+result.servicename + ", servicetype= " + result.servicetype)    
            else :
                print("get_gslbservice - Done")            
        except nitro_exception as e :
            print("Exception::get_gslbservice::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e : 
            print("Exception::get_gslbservice::message="+str(e.args))
     
    def get_gslbsite(self, client) :
        try :
            result = gslbsite.get(client, "bangalore1")
            if result :            
                print("get_gslbsite - sitename= "+result.sitename + ", siteipaddress= " + result.siteipaddress)    
            else :
                print("get_gslbsite - Done")            
        except nitro_exception as e :
            print("Exception::get_gslbsite::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_gslbsite::message="+str(e.args))    
     
     
    def get_gslbvserver_service_binding(self, client) :
        try :
            result = gslbvserver_gslbservice_binding.get(client, "newgvip1")
            if result :
                for i in range(len(result)) :
                    print("get_gslbvserver_service_binding - vserver name= "+result[i].name + ", servicename= " + result[i].servicename)
            else :
                print("get_gslbvserver_service_binding - Done")
        except nitro_exception as e :
            print("Exception::get_gslbvserver_service_binding::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_gslbvserver_service_binding::message="+str(e.args))              
     
     
    def get_vpnglobal_authpol(self, client) :
        try :
            result = vpnglobal_authenticationldappolicy_binding.get(client)
            if result :
                for i in range(len(result)) :
                    print("get_vpnglobal_authpol - version= "+result[i].policyname + ", secondary= " + str(result[i].secondary))
            else :
                print("Exception::get_vpnglobal_authpol - Done")
        except nitro_exception as e :
            print("Exception::get_vpnglobal_authpol::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_vpnglobal_authpol::message="+str(e.args))              
     
     
    def getlbvs_svc_bind_bulk(self, client) :
        try :  
            str_ = ["v1", "v2"]
            result = lbvserver_binding.get(client, str_)
            if result :
                for i in range(len(result)) :            
                    if result[i].get_lbvserver_service_bindings() :                 
                        print("getlbvs_svc_bind_bulk - version= "+result[i].name + ", services= " + result[i].lbvserver_service_bindings.length)
            else :
                print("getlbvs_svc_bind_bulk - Done")    
        except nitro_exception as e :
            print("Exception::getlbvs_svc_bind_bulk::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::getlbvs_svc_bind_bulk::message="+str(e.args))              
    
     
    def getlbvserver_bulk(self, client) :
        try :
            str_ = ["v1", "v2"]
            result = lbvserver.get(client, str_)
            if result :
                for i in range(len(result)) :
                    print("getlbvserver_bulk - version= "+result[i].name + ", lbmethod= " + result[i].lbmethod)
            else :
                print("getlbvserver_bulk - Done")    
        except nitro_exception as e :
            print("Exception::getlbvserver_bulk::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::getlbvserver_bulk::message="+str(e.args))                          
       
     
    def get_nsversion(self, client) :
        try :
            result = nsversion.get(client)
            if result :
                print("get_nsversion - version= "+result[0].version + ", mode= " + result[0].mode)    
            else :
                print("get_nsversion - Done")    
        except nitro_exception as e :
            print("Exception::get_nsversion::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nsversion::message="+str(e.args))                                     
            
     
    def count_snmpoid(self, client) :
        try :
            obj = snmpoid()
            obj.entitytype = "VSERVER"
            count = snmpoid.count(client, obj)
            print("count_snmpoid - count:"+str(count))    
        except nitro_exception as e :
            print("Exception::count_snmpoid::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::count_snmpoid::message="+str(e.args))                                     
      
     
    def get_nsacl(self, client) :
        try :          
            result = nsacl.get(client, "xyz")
            if result :
                print("get_nsacl - aclname= "+result.aclname + ", kernelstate= " + result.kernelstate)    
            else :
                print("get_nsacl - Done")    
        except nitro_exception as e :
            print("Exception::get_nsacl::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nsacl::message="+str(e.args))                                               
     
     
    def get_nsxmlnamespace(self, client) :
        try :
            result = nsxmlnamespace.get(client)
            if result :
                for i in range(len(result)) :
                    print("get_nsxmlnamespace - prefix= "+result[i].prefix + ", namespace= " + result[i].Namespace)
            else :
                print("Exception::get_nsxmlnamespace - Done")
        except nitro_exception as e :
            print("Exception::get_nsxmlnamespace::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nsxmlnamespace::message="+str(e.args))                                               
 
     
    def get_nstcpbufparam(self, client) :
        try :
            result = nstcpbufparam.get(client) 
            if result :
                for i in range(len(result)) :
                    print("get_nstcpbufparam - size= "+str(result[i].size) + ", memlimit= " + str(result[i].memlimit))
            else :
                print("Exception::get_nstcpbufparam - Done")
        except nitro_exception as e :
            print("Exception::get_nstcpbufparam::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nstcpbufparam::message="+str(e.args))                                                           
    
     
    def get_nslimitidentifier(self, client) :
        try :
            result = nslimitidentifier.get(client) 
            if result :
                for i in range(len(result)) :
                    print("get_nslimitidentifier - timeslice: "+str(result[i].timeslice))
            else :
                print("get_nslimitidentifier - Done")
        except nitro_exception as e :
            print("Exception::get_nslimitidentifier::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nslimitidentifier::message="+str(e.args))                                                                      
   
    
    def get_sslfipskey(self, client) :
        try :
            result = sslfipskey.get(client)
            if result :
                for i in range(len(result)) :
                    print("get_sslfipskey - certkey: "+result[i].fipskeyname)
            else :
                print("get_sslfipskey - Done")
        except nitro_exception as e :
            print("Exception::get_sslfipskey::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_sslfipskey::message="+str(e.args))                                                                                
  
     
    def get_sslcertkey(self, client) :
        try :
            result = sslcertkey.get(client)
            if result :
                for i in range(len(result)) :
                    print("get_sslcertkey - certkey: "+result[i].certkey)
            else :
                print("get_sslcertkey - Done")            
        except nitro_exception as e :
            print("Exception::get_sslcertkey::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_sslcertkey::message="+str(e.args))                                                                                
         
 
     
    def get_nsip(self, client) :
        try :
            obj = nsip()
            obj.ipaddress = "1.1.1.77"   
            if obj :                
                result = nsip.get(client, obj)
                print("get_nsip - metric"+result.metric+ ", flags=" +result.flags+ ", ospfarea"+ result.ospfarea+ ", ospfareaval=" +result.ospfareaval)
            else :
                print("get_nsip - Done")                
        except nitro_exception as e :
            print("Exception::get_nsip::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nsip::message="+str(e.args))                                                                                
            
    
     
    def get_dnszone(self, client) :
        try :
            result = dnszone.get(client)
            if result :                
                for i in range(len(result)) :
                    print("    zone:"+result[i].zonename)
            else :
                print("get_dnszone - Done")
        except nitro_exception as e :
            print("Exception::get_dnszone::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_dnszone::message="+str(e.args))                                                                                
           
       
     
    def get_dnsnsecrec(self, client) :
        try :
            result = dnsnsecrec.get(client)
            if result :                
                for i in range(len(result)) :
                    print("    host:"+result[i].hostname)
            else :
                print("get_dnsnsecrec - Done")
        except nitro_exception as e :
            print("Exception::get_dnsnsecrec::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_dnsnsecrec::message="+str(e.args))                                                                                
      
     
    def get_dnsview_dnspol_binding(self, client) :
        try :
            obj = dnsview_dnspolicy_binding()
            obj.viewname = "xx"
            result = dnsview_dnspolicy_binding.get_filtered(client, "xx", "dnspolicyname:pol1")
            if result :                
                for i in range(len(result)) :
                    print("    pol:"+result[i].dnspolicyname)
            else :
                print("get_dnsview_dnspol_binding - Done")             
        except nitro_exception as e :
            print("Exception::get_dnsview_dnspol_binding::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_dnsview_dnspol_binding::message="+str(e.args))                                                                                
     
     
     
    def get_snmptrap(self, client) :
        try :
                str_ = "10.102.1.2"
                obj = snmptrap()
                obj.trapclass = "generic"
                obj.trapdestination = str_
                obj = snmptrap.get(client, obj)
                if obj :
                    print("get_snmptrap port:"+str(obj.get_destport())+" description: " +obj.get_trapdestination()+" srcIP: "+obj.get_srcip())                               
                else :
                    print("get_snmptrap - Done")             
        except nitro_exception as e :
            print("Exception::get_snmptrap::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_snmptrap::message="+str(e.args))                                                                                
        
     
    def get_snmpuser(self, client) :
        try :
            obj = snmpuser()
            obj.name = "u1"
            obj = snmpuser.get(client, "u1")
            if obj :
                print("get_snmpuser Name:"+obj.name+" grpName: " +obj.group+" storage Type: "+obj.storagetype)                               
            else :
                print("get_snmpuser - Done")             
        except nitro_exception as e :
            print("Exception::get_snmpuser::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_snmpuser::message="+str(e.args))                                                                                
     
     
    def get_snmpmanager(self, client) :
        try :
            obj = snmpmanager()
            obj.ipaddress = "10.102.31.20"
            if obj :
                obj1 = snmpmanager.get(client, obj)
                if obj1 :
                    print("get_snmpmanager id:"+obj1.ipaddress+"description" +obj1.netmask)
            else :
                print("get_snmpmanager - Done")
        except nitro_exception as e :
            print("Exception::get_snmpmanager::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_snmpmanager::message="+str(e.args))                                                                                
       
     
    def get_channel(self, client) :
        try :
            obj = channel.get(client,"LA/1")
            if obj :
                print("get_channel id:"+obj.id+", description" +obj.description)
            else :
                print("get_channel - Done")
        except nitro_exception as e :
            print("Exception::get_channel::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_channel::message="+str(e.args))                                                                                
      
     
    def get_interface(self, client) :
        try :
            obj = Interface.get(client, "1/3")
            if obj :
                print("get_interface id:"+obj.id+", reqduplex" +obj.reqduplex)
            else :
                print("get_interface - Done")
        except nitro_exception as e :
            print("Exception::get_interface::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_interface::message="+str(e.args))                                                                                
     
    
    def count_filtered_lbvserver_svc_bindings(self, client):
        try:
            filter_params = []
            filter_params = [ filtervalue() for _ in range(2)]
            filter_params[0] = filtervalue("servicetype","HTTP")
            filter_params[1] = filtervalue("port","80")        
            response = lbvserver_service_binding.count_filtered(client, "lb1", filter_params)
            print("count_filtered_lbvserver_svc_bindings:: " + str(response))
        except nitro_exception as e:
                print("Exception::count_filtered_lbvserver_svc_bindings::errocode - "+str(e.errorcode)+", message - "+e.message)            
        except Exception as e:    
                print("Exception::count_filtered_lbvserver_svc_bindings:: "+str(e.args)) 
                                 
     

    def count_lbvserver(self, client):
        try:
            lbvs_count = lbvserver.count(client)
            print("count_lbvserver::"+str(lbvs_count)) 
        except nitro_exception as e:
            print("Exception::count_lbvserver::errorcode="+str(e.errorcode)+", Message= "+e.errorcode)            
        except Exception as e:
            print("Exception::count_lbvserver::message="+str(e.args))
     
     
    def count_lbvserver_service_binding(self, client):
        try:
            response = lbvserver_service_binding.count(client, "lb1")
            print("count_lbvserver_service_binding:: " + str(response))
        except nitro_exception as e:
                print("Exception::count_lbvserver_service_binding::errocode - "+str(e.errorcode)+", message - "+e.message)            
        except Exception as e:    
                print("Exception::count_lbvserver_service_binding:: "+str(e.args)) 
                                                                                
     
     
    def count_lbvserver_cachepolicy_binding(self, client) :
        try :
            lbvs_count = lbvserver_cachepolicy_binding.count(client,"lbvip1")
            print("count_lbvserver_cachepolicy_binding : "+lbvs_count)
        except nitro_exception as e :
            print("Exception::count_lbvserver_cachepolicy_binding::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::count_lbvserver_cachepolicy_binding::message="+str(e.args))                                                                                
     
     
     
    def get_snmpoid(self, client) :
        try :
            obj = snmpoid()
            obj.entitytype = "VSERVER"
            result = snmpoid.get(client, obj)
            if result :
                print("get_snmpoid - enitity_name: "+result.entitytype+" name="+result.name+" cmnt= "+result.Snmpoid)
            else : 
                print("Exception::get_snmpoid::Done")
        except nitro_exception as e :
            print("Exception::get_snmpoid::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_snmpoid::message="+str(e.args))                                                                                
     
     
    def get_svcmon_binds(self, client) :
        try :
            result = service_lbmonitor_binding.get(client, "s1")
            print("get_svcmon_binds name="+str(len(result)))
            if result :
                for _ in range(len(result)) :
                    print("mon name: "+result[0].monitor_name)
            else :
                print("get_svcmon_binds - Done")
        except nitro_exception as e :
            print("Exception::get_svcmon_binds::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_svcmon_binds::message="+str(e.args))                                                                                
     
     
    def get_svcgrp_svr_bind(self, client) :
        try :
            result = servicegroup_servicegroupmember_binding.get(client, "svcgrp1")
            print("get_svcgrp_svr_bind name="+str(len(result)))
            if result :
                for i in range(len(result)) :
                    print("svrip: "+result[i].ip)
            else :
                print("get_svcgrp_svr_bind - Done")
        except nitro_exception as e :
            print("Exception::get_svcgrp_svr_bind::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_svcgrp_svr_bind::message="+str(e.args))                                                                                

            
    def get_nsfeature(self, client) : 
        try : 
            features = client.get_features()
            i=1
            print("nsfeature on given NS: ")
            for feature in features :
                print("\t"+ str(i) +") "+feature)
                i = i + 1 
        except nitro_exception as e :
            print("Exception::get_nsfeature::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nsfeature::message="+str(e.args))                                                                                                                                                                            
     
     
    def get_enabled_nsfeature(self, client) : 
        try : 
            enabled_features = client.get_enabled_features()
            i=1
            print("enabled nsfeatures: ")
            for en_feature in enabled_features :
                print("\t"+ str(i) +") "+en_feature)
                i= i + 1        
        except nitro_exception as e :
            print("Exception::get_enabled_nsfeature::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_enabled_nsfeature::message="+str(e.args))                                                                                
          
           
       
    def get_enabled_modes(self, client) : 
        try : 
            enabled_modes = client.get_enabled_modes()
            i =1
            print("enabled nsmodes: ")
            for en_mode in enabled_modes :
                print("\t"+ str(i) +") "+en_mode)
                i = i + 1 
        except nitro_exception as e :
            print("Exception::get_enabled_modes::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_enabled_modes::message="+str(e.args))                                                                                
      
     
    def get_nsmode(self, client) : 
        try : 
            modes = client.get_modes()
            i =1
            print("nsmodes on given NS: ")
            for mode in modes :
                print("\t"+ str(i) +") "+mode)
                i= i + 1
        except nitro_exception as e :
            print("Exception::get_nsmode::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_nsmode::message="+str(e.args))                                                                                                                                                              
         
     
    def get_sslcipher_binds(self, client) :
        try :
            result = sslcipher_binding.get(client, "g1")
            if result :
                print("get_sslcipher_binds name="+result.sslcipher_individualcipher_bindings.length)
            else :
                print("get_sslcipher_binds - Done")
        except nitro_exception as e :
            print("Exception::get_sslcipher_binds::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_sslcipher_binds::message="+str(e.args))                                                                                
      

    def get_vpnglobal_vpnclientlessaccesspolicy_bindings(self, client) :
        try :
            result = vpnglobal_vpnclientlessaccesspolicy_binding.get(client)
            if result :
                print("get_vpnglobal_binds name="+str(len(result)))
            else :
                print("get_vpnglobal_binds - Done")
        except nitro_exception as e :
            print("Exception::get_vpnglobal_binds::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_vpnglobal_binds::message="+str(e.args))                                                                                
     
     
    def get_auth_bindings(self, client) : 
        try :
            result = authorizationpolicylabel_binding.get(client, "trans_http_url")
            if result :
                print("get_auth_bindings name="+result.labelname)
                if result.get_authorizationpolicylabel_authorizationpolicy_bindings() : 
                    for i in range(len(result.authorizationpolicylabel_authorizationpolicy_bindings)) : 
                        print("    auth cmd policies polname="+result.authorizationpolicylabel_authorizationpolicy_bindings()[i].policyname+" priority="+result.get_authorizationpolicylabel_authorizationpolicy_bindings()[i].priority+"invoke"+result.get_authorizationpolicylabel_authorizationpolicy_bindings()[i].invoke)
            else :
                print("get_auth_bindings - Done")
        except nitro_exception as e :
            print("Exception::get_auth_bindings::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_auth_bindings::message="+str(e.args))                                                                                
     
     
    def get_systemgrp_binds(self, client) :
        try :
            result = systemgroup_binding.get(client, "g1")
            if result :
                print("get_systemgrp_binds name="+result.groupname)
                if(result.get_systemgroup_systemcmdpolicy_bindings()) :
                    for i in range(len(result.get_systemgroup_systemcmdpolicy_bindings())) :
                        print("system cmd policies polname="+result.get_systemgroup_systemcmdpolicy_bindings()[i].policyname+" priority="+result.get_systemgroup_systemcmdpolicy_bindings()[i].priority)
                if(result.get_systemgroup_systemuser_bindings())  :
                    for i in range(len(result.get_systemgroup_systemuser_bindings())) :
                        print("system cmd user username="+result.get_systemgroup_systemuser_bindings()[i].username)
        except nitro_exception as e :
            print("Exception::get_systemgrp_binds::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_systemgrp_binds::message="+str(e.args))                                                                                
    
     
    def get_gslbservice_binds(self, client) :
        try :
            result = gslbservice_binding.get(client, "sj_svc")
            if  result : 
                print("get_gslbservice_binds name="+result.servicename+", viewname=" + result.get_gslbservice_dnsview_bindings()[0].viewname)
            else : 
                print("get_gslbservice_binds - Done")
        except nitro_exception as e :
            print("Exception::get_gslbservice_binds::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_gslbservice_binds::message="+str(e.args))                                                                                         
    
     
    def get_gslbldnsentries(self, client) :
        try :
            result = gslbldnsentries.get(client)
            if result :
                print("get_gslbldnsentries result::length="+str(len(result)))
            else :
                print("get_gslbldnsentries - Done")
        except nitro_exception as e :
            print("Exception::get_gslbldnsentries::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_gslbldnsentries::message="+str(e.args))                                                                                
    
     
    def get_cmppolicy_bindings(self, client) :
        try :
            result = cmppolicy_lbvserver_binding.get(client, "pdf_cmp")
            if result :
                for i in range(len(result)) :
                    print("cmppol name="+result[i].name+", lbvserver=" + result[i].boundto)
            else :
                print("get_cmppolicy_bindings - Done")
        except nitro_exception as e :
            print("Exception::get_cmppolicy_bindings::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_cmppolicy_bindings::message="+str(e.args))                                                                                
    
     
    def get_auditnslogaction(self, client) :
        try :
            result = auditnslogaction.get(client)
            if result :
                for i in range(len(result)) :
                    print("cmppol name="+result[i].name+", ip=" + result[i].serverip)
            else :
                print("Exception::get_auditnslogaction - Done")
        except nitro_exception as e :
            print("Exception::get_auditnslogaction::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_auditnslogaction::message="+str(e.args))                                                                                
    
     
     
    def get_sslbindings(self, client) :
        try :
            obj = sslpolicy_binding()
            obj.name = "certInsert_pol"
            result = sslpolicy_binding.get(client, "certInsert_pol")
            if result :
                print("get_sslbindings result::name="+result.name)
                if result.get_sslpolicy_csvserver_bindings() :
                    xx = [sslpolicy_csvserver_binding() in range(len(result.get_sslpolicy_csvserver_bindings()))]
                    xx = result.get_sslpolicy_csvserver_bindings()
                    for j in range(len(xx)) : 
                        print("csvservername" + xx[j].boundto)
            else :
                print("get_sslbindings - Done")
        except nitro_exception as e :
            print("Exception::get_sslbindings::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_sslbindings::message="+str(e.args))                                                                                
     
     
    def get_hanode(self, client) :
        try :
            option_ = options()
            option_.detailview = True
            result = hanode.get(client, "", option_)
            if result :
                for i in range(len(result)) :
                    print("get_hanode result::Id="+result[i].id+", IP="+result[i].ipaddress+", effecive-interfaces="+result[i].enaifaces)
            else :
                print("get_hanode - Done")                
        except nitro_exception as e :
            print("Exception::get_hanode::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_hanode::message="+str(e.args))                                                                                
     
     
    def get_dnssuffix(self, client) :
        try :
            result = dnssuffix.get(client, "citrix.com")
            if result :
                print("get_dnssuffix result::name="+result.Dnssuffix)
            else :
                print("get_dnssuffix result - Done")
        except nitro_exception as e :
            print("Exception::get_dnssuffix::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_dnssuffix::message="+str(e.args))                                                                                
     
     
    def get_gslbparameter(self, client) :
        try :
            result = gslbparameter.get(client)
            if result :
                for i in range(len(result)) :
                    print("get_gslbparameter result::mask="+result[i].ldnsmask+", ldnsProbOrder="+str(result[i].ldnsprobeorder))
            else :
                print("get_gslbparameter result - Done")
        except nitro_exception as e :
            print("Exception::get_gslbparameter::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_gslbparameter::message="+str(e.args))                                                                                

            
    def get_auditsyslogparams(self, client) :
        try :
            result = auditsyslogparams.get(client)
            if result :
                for i in range(len(result)) :
                    print("get_auditsyslogparams result::ip="+result[i].serverip+", loglevel="+str((result[i].loglevel)[0]))
            else :
                print("get_auditsyslogparams result - Done")
        except nitro_exception as e :
            print("Exception::get_auditsyslogparams::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_auditsyslogparams::message="+str(e.args))                                                                                
     
     
    def get_appfwconfield(self, client) :
        try :
            obj = appfwconfidfield()
            obj.fieldname = "ap_con"
            obj.url = "/test1"
            result = appfwconfidfield.get(client, obj)
            if result :
                print("get_appfwconfield result::name="+result.fieldname+", url="+result.url)
            else :
                print("get_appfwconfield result - Done")
        except nitro_exception as e :
            print("Exception::get_appfwconfield::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_appfwconfield::message="+str(e.args))                                                                                
     
     
    def get_appfwprofile(self, client) :
        try :
            result = appfwprofile.get(client, "pr1")
            if result :
                print("get_appfwprofile result::name="+result.name+", StartURLAction="+result.starturlaction[0]+result.starturlaction[1]+ result.starturlaction[2])
            else :
                print("get_appfwprofile - Done ")
        except nitro_exception as e :
            print("Exception::get_appfwprofile::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_appfwprofile::message="+str(e.args))                                                                                
     
     
    def get_policyexpression(self, client) :
        try :
            args = policyexpression_args()
            args.type = "classic"
            result = policyexpression.get_args(client, args)
            if result :
                print("get_policyexpression result::length="+str(len(result)))
            else :
                print("get_policyexpression - Done ")
        except nitro_exception as e :
            print("Exception::get_policyexpression::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_policyexpression::message="+str(e.args))                                                                                
    

    def get_snmpgroup( self, client) :
        try :
            obj = snmpgroup()
            obj.name = "snmp_grp"
            obj.securitylevel = "noAuthNoPriv"
            result = snmpgroup.get(client, obj)
            if result :
                print("get_snmpgroup result::name="+result.name)
            else :
                print("get_snmpgroup - done")
        except nitro_exception as e :
            print("Exception::get_snmpgroup::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_snmpgroup::message="+str(e.args))                                                                                
        
    
    def get_cacheobjects(self, client) :
        try :
            result = cacheobject.get(client)
            if result :
                print("get_cacheobjects result::length="+str(len(result)))
            else:
                print("getlbvserver_svc_bindings :: Done")  
        except nitro_exception as e :
            print("Exception::get_cacheobjects::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_cacheobjects::message="+str(e.args))                                                                                
    
    
    def get_lbvserver(self, client):
        try:
            result = lbvserver.get(client)
            if result :
                print("get_lbvserver result::length="+str(len(result)))
            else:
                print("Exception::get_lbvserver - Done")
        except nitro_exception as e:
            print("Exception::get_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::get_lbvserver::message="+str(e.args))
    

    def get_svc_bind(self, client) :
        try :
            obj = service_binding()
            obj.name = "svc1"
            result = service_binding.get(client,"svc1")
            if result :
                print("get_svc_bind result::length="+result.get_service_lbmonitor_bindings().length)
                for i in range(len(result.get_service_lbmonitor_bindings())) :
                    print("resptime: "+result.get_service_lbmonitor_bindings()[i].get_responsetime())
            else :
                print("get_svc_bind - Done")
        except nitro_exception as e :
            print("Exception::get_svc_bind::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_svc_bind::message="+str(e.args))                                                                                
    
    
    def get_protocolhttpband(self, client) :
        try :
            obj = protocolhttpband()
            obj.type = "REQUEST"
            result = protocolhttpband.get(client, obj)
            if result :
                print("get_protocolhttpband result::length="+str(len(result.accesscount)))                
            else :
                print("get_protocolhttpband - Done")
        except nitro_exception as e :
            print("Exception::get_protocolhttpband::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_protocolhttpband::message="+str(e.args))                                                                                
    
    
    def getlbvserver_bindings(self, client) :
        try :
            obj = lbvserver_binding()
            obj.name = "lb_vip"
            result = lbvserver_binding.get(client,"lb_vip")
            if result :
                print("getlbvserver_bindings result::name="+result.name)
            else:
                print("getlbvserver_svc_bindings :: Done")  
        except nitro_exception as e :
            print("Exception::getlbvserver_bindings::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::getlbvserver_bindings::message="+str(e.args))                                                                                
    

    def getlbvserver_svc_bindings(self, client):
        try:
            result = lbvserver_service_binding.get(client, "lb1")
            if result :
                print("getlbvserver_svc_bindings result::length="+str(len(result)))
            else:
                print("getlbvserver_svc_bindings :: Done")  
        except nitro_exception as e:
                print("Exception::getlbvserver_svc_bindings::errocode - "+str(e.errorcode)+", message - "+e.message)            
        except Exception as e:    
                print("Exception::getlbvserver_svc_bindings:: "+str(e.args)) 
                                                                                
        
    
    def getfiltered_lbvserver_svc_bindings(self, client):
        try:
            filter_params = []
            filter_params = [ filtervalue() for _ in range(2)]
            filter_params[0] = filtervalue("servicetype","HTTP")
            filter_params[1] = filtervalue("port","80")        
            result = lbvserver_service_binding.get_filtered(client, "lb1", filter_params)
            if result :
                print("getlbvserver_svc_bindings result::length="+str(len(result)))
            else:
                print("getlbvserver_svc_bindings :: Done")  
        except nitro_exception as e:
                print("Exception::getfiltered_lbvserver_svc_bindings::errocode - "+str(e.errorcode)+", message - "+e.message)            
        except Exception as e:    
                print("Exception::getfiltered_lbvserver_svc_bindings:: "+str(e.args)) 
        
    
    def getlbvserver_byname(self, client):
        try:
            obj = lbvserver.get(client, "lb1")
            print("getlbvserver_byname result::name="+obj.name+", curstate="+obj.curstate+", effectivestate=" + obj.effectivestate)
        except nitro_exception as e:
            print("Exception::getlbvserver_byname::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::getlbvserver_byname::message="+str(e.args))
        
    
    def getfiltered_services(self, client) :
        try :
            filter_params = []
            filter_params = [ filtervalue() for _ in range(2)]
            filter_params[0] = filtervalue("port", "80")
            filter_params[1] = filtervalue("servicetype", "HTTP")
            result = service.get_filtered(client, filter_params)
            if  result : 
                print("getfiltered_services result::length="+str(len(result)))
            else : 
                print("Exception::getfiltered_services::Done")
        except nitro_exception as e :
            print("Exception::getfiltered_services::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::getfiltered_services::message="+str(e.args))                                                                                
    
    
    def get_appfwlearningdata(self, client) :
        try :
            args = appfwlearningdata()
            args.profilename = "pr_testsite_3"
            args.securitycheck = "starturl"
            result = appfwlearningdata.get(client, args)
            if result :
                print("get_appfwlearningdata result::profile name="+appfwlearningdata.profilename+"blob= "+appfwlearningdata.data)
            else :
                print("Exception::get_appfwlearningdata::Done")
        except nitro_exception as e :
            print("Exception::get_appfwlearningdata::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e :  
            print("Exception::get_appfwlearningdata::message="+str(e.args))                                                                                        

    def count_filtered_lbvserver(self, client):
        try:
            filter_params = []
            filter_params = [ filtervalue() for _ in range(2)]
            filter_params[0] = filtervalue("servicetype","HTTP")
            filter_params[1] = filtervalue("port","80")
            lbvs_count = lbvserver.count_filtered(client, filter_params)
            print("count_filtered_lbvserver:: " + str(lbvs_count))
        except nitro_exception as e:
                print("Exception::count_filtered_lbvserver::errocode - "+str(e.errorcode)+", message - "+e.message)            
        except Exception as e:    
                print("Exception::count_filtered_lbvserver:: "+str(e.args)) 

    def getfiltered_lbvserver(self, client):
        try:
            filter_params = []
            filter_params = [ filtervalue() for _ in range(2)]
            filter_params[0] = filtervalue("servicetype","HTTP")
            filter_params[1] = filtervalue("port","80")
            result = lbvserver.get_filtered(client, filter_params)
            if result :
                print("getfiltered_lbvserver result::length="+str(len(result)))
            else:
                print("Exception::getfiltered_lbvserver - Done")
        except nitro_exception as e:
            print("Exception::getfiltered_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::getfiltered_lbvserver::message="+str(e.args))
    

    def run_sample(self, client):
        self.get_svcgrp_svr_bind(client);
        self.get_protocolhttpband(client);
        self.get_lbvserver(client);                
        self.getlbvserver_byname(client);
        self.getlbvserver_bindings(client);
        self.getlbvserver_svc_bindings(client);
        self.get_policyexpression(client);
        self.get_cacheobjects(client);
        self.get_snmpgroup(client);   
        self.get_appfwprofile(client);
        self.get_appfwconfield(client);
        self.get_auditsyslogparams(client);
        self.get_gslbparameter(client);
        self.get_dnssuffix(client);
        self.get_hanode(client);
        self.get_sslbindings(client);
        self.get_cmppolicy_bindings(client);
        self.get_auditnslogaction(client);
        self.get_gslbldnsentries(client);
        self.get_gslbservice_binds(client);
        self.get_systemgrp_binds(client);
        self.get_auth_bindings(client);
        self.get_vpnglobal_vpnclientlessaccesspolicy_bindings(client);
        self.get_sslcipher_binds(client);
        self.get_nsmode(client);
        self.get_enabled_modes(client);
        self.get_nsfeature(client);
        self.get_enabled_nsfeature(client);
        self.get_svcmon_binds(client);
        self.get_snmpoid(client);
        self.get_appfwlearningdata(client);
        self.count_lbvserver(client);
        self.count_lbvserver_service_binding(client);
        self.count_filtered_lbvserver(client);
        self.getfiltered_lbvserver(client);
        self.getfiltered_services(client);
        self.getfiltered_lbvserver_svc_bindings(client);        
        self.get_channel(client);
        self.get_snmpmanager(client);
        self.get_snmptrap(client);
        self.count_lbvserver_cachepolicy_binding(client);
        self.get_interface(client);
        self.get_dnsview_dnspol_binding(client);
        self.get_svc_bind(client);
        self.get_sslcertkey(client);
        self.get_sslfipskey(client);
        self.get_nsip(client);
        self.get_nslimitidentifier(client);
        self.get_nstcpbufparam(client);
        self.get_nsxmlnamespace(client);
        self.get_snmpuser(client);
        self.get_nsacl(client);
        self.count_snmpoid(client);
        self.get_nsversion(client);
        self.getlbvserver_bulk(client);
        self.getlbvs_svc_bind_bulk(client);
        self.get_vpnglobal_authpol(client);
        self.get_gslbvserver(client);
        self.get_gslbsite(client);
        self.get_gslbservice(client);
        self.get_gslbvserver_service_binding(client);
       
        
        
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
            get_config().main(get_config(),sys.argv)
    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")
