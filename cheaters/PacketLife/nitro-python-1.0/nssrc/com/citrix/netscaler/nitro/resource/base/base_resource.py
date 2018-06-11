
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
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

from nssrc.com.citrix.netscaler.nitro.resource.base.base_response import base_response
from nssrc.com.citrix.netscaler.nitro.resource.base.base_responses import base_responses
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util
from nssrc.com.citrix.netscaler.nitro.service.options import options


import requests
import json
import abc
import urllib2
import inspect

class base_resource:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def _get_nitro_response(self, service, string):
        pass
    
    @abc.abstractmethod    
    def _get_object_name(self):
        pass

    @classmethod
    def get_object_type(cls):
        """ Gets the resource type.
        
        Returns:
			Resource Type. eg:lbvserver, csvserver.
        """
        return cls.__name__

    def resource_to_string(self, service):
        """ Converts netscaler resource to Json string.
        
        Parameters:
			service - nitro_service object.
            id - sessionId.
        
        Returns:
			string in Json format.
        """
        try:
            result = service.payload_formatter.resource_to_string(self)
            return result
        except Exception as e:
            raise e

    def resource_to_string(self, service):
        """ Converts netscaler resource to Json string.
        
        Parameters:
			service - nitro_service object
        
        Returns:
			string in Json format.
        """
        result = service.payload_formatter.resource_to_string(self)
        return result

        
    def unset_string(self, service, args):
        """ forms a String for unset operation on a resource.
        
        Parameters:
			service - nitro_service object.
            id - session id.
            args - Array of args that are to be unset.
        
        Returns:
			string in Json format.
        
        Throws:
			Exception if invalid input is given.
        """
        try:
            result = "{\"" + self.__class__.get_object_type() + "\":" 
            result = result + service.payload_formatter.unset_string(self, args) + "}"
            return result
        except Exception as e:
            raise e

    
    def post_requestEx(self, service, opt):
        """ Use this method to perform a POST operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
            opt - Options class object.
        
        Returns:
			requested resource.
        
        Throws:
			Exception if invalid input is given.
        """
        try:
            request = self.resource_to_string(service)
            return self.post_dataEx(service, request)
        except Exception as e:
            raise e
    

    def post_request(self, service, opt):
        """ Use this method to perform a Add operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
        	opt - Options class object.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception if invalid input is given.
        """
        try:
            request = self.resource_to_string(service)
            return self.post_data(service, request, opt)
        except Exception as e:
            raise e


    def unset_request(self, service, opt, args):
        """ Use this method to perform an Unset operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
        	opt - options class object.
        	args - string.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception
        """
        try:
            request = self.unset_string(service, args)
            return self.post_data(service, request, opt)
        except Exception as e:
            raise e
   
    def add_resource(self, service, opt=""):
        """ Use this method to perform a add operation on netscaler resource.
        
        Parameters:
			service - nitro_service object. 
        	opt - options class object.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception
        """
        try:
            if not service.isLogin():
                service.login()
            request = self.resource_to_string(service)
            return self.post_data(service, request, opt)
        except Exception as e:
            raise e     
    

    def update_resource(self, service):
        """ Use this method to perform a modify operation on netscaler resource.
        
        Parameters:
			service - nitro_service object. 
        	opt - options class object.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception
        """
        try:
            if not service.isLogin():
                service.login()
            request = self.resource_to_string(service)
            return self.put_data(service, request)
        except Exception as e:
            raise e


    def delete_resource(self, service):
        """ Use this method to perform a delete operation on netscaler resource.
        
        Parameters:
			service - nitro_service object
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin() :
                service.login()
            str_ = nitro_util.object_to_string_withoutquotes(self)
            response = self.delete_request(service, str_)
            return response
        except Exception as e:
            raise e

            
    def getfiltered(self, service, opt):
        """ Use this method to perform a filtered get operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
        	opt - options class object.
        
        Returns:
			Array of nitro resources of given resource type.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.get_request(service, opt)
            return response
        except Exception as e:
            raise e
 
    def get_resources(self, service, opt=""):
        """ Use this method to perform a get operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
        	opt - options class object.
        
        Returns:
			Array of nitro resources of specified type.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.get_request(service, opt)
            return response
        except Exception as e:
            raise e

            
    def get_resource(self, service, opt=""):
        """ Use this method to perform a get operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
        	opt - options class object.
        
        Returns:
			Array of nitro resources of specified type.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.get_request(service, opt)
            if type(response) is list:
                return response[0]
            else :
                return response
            return None
        except Exception as e:
            raise e


    def stat_resources(self, service, opt="") :
        """ Use this method to perform a stat operation on netscaler resources.
        
        Parameters:
			service - nitro_service object. 
        	opt - options class object.
        
        Returns:
			Array of nitro stat resources of specified type.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin() :
                service.login()
            response = self.stat_request(service, opt)
            return response
        except Exception as e:
            raise e

            
    def stat_resource(self, service, opt=""):
        """ Use this method to perform a stat operation on a netscaler resource.
        
        Parameters:
			service - nitro_service object. 
        	opt - options class object.
        
        Returns:
			Requested Nitro stat resource.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.stat_request(service, opt)
            if (response and len(response) > 0) :
                return response[0]
            return None
        except Exception as e:
            raise e
    

    def perform_operation(self, service, action="", opt=""):
        """ Use this method to perform a clear/sync/link/unlink/save ...etc 
        operation on netscaler resource.
        
        Parameters:
			service - nitro_service object. 
        	action - action needs to be taken on resource. 
        	opt - options object with action that is to be performed set.     
        
        Returns:
			status of the operation performed.
                
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin() and self.__class__.get_object_type()!="login"):
                service.login()
            if not opt and not action:
                return self.post_request(service, None)
            elif not opt :
                opt = options()
                opt.action = action
            response = self.post_request(service, opt)
            return response
        except Exception as e:
            raise e


    def perform_operationEx(self, service, action):
        """ Use this method to perform a POST operation that returns a resource ...etc 
        operation on netscaler resource.
        
        Parameters:
			service - nitro_service object. 
        	action - action needs to be taken on resource. 
        
        Returns:
			requested resource
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin() and self.__class__.get_object_type() != "login"):
                service.login()
            opt = options()
            opt.action = action
            response = self.post_requestEx(service, opt)
            return response
        except Exception as e:
            raise e


    @classmethod       
    def perform_operation_bulk_request(cls, service, resources, action ):
        """ Use this method to perform a clear/sync/link/unlink/save ...etc 
        operation on netscaler resources.
        
        Parameters:
			service - nitro_service object. 
        	resources - Array of Nitro resources on which the specified action to be performed.
        	opt - options object with action that is to be performed set.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()

            opt = options()
            opt.action = action        
            request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.post_bulk_data(service, request, opt)
            return result
        except Exception as e:
            raise e

            
    def rename_resource(self, service, newname):
        """ Use this method to perform a rename operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
        	newname - new name to be set to the specified resource.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin():
                service.login()
                
            if '_newname' in self.__dict__ : 
                self.newname = newname
            else :
                raise nitro_exception(-1,str("Rename is not supported for this resource"),)
            opt = options()
            opt.action = "rename"
            response = self.post_request(service, opt)
            return response
        except Exception as e:
            raise e


    def unset_resource(self, service, args):
        """ Use this method to perform an Unset operation on netscaler resource.
        
        Parameters:
			service - nitro_service object.
        	args - Array of args that are to be unset.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin():
                service.login()
            opt = options()
            opt.action = "unset"
            response = self.unset_request(service, opt, args)
            return response
        except Exception as e:
            raise e


    @classmethod
    def update_bulk_request(cls, service, resources):
        """ Use this method to perform an update operation on netscaler resources.
        
        Parameters:
			service - nitro_service object.
        	resources - Array of nitro resources to be updated.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.put_bulk_data(service, request)
            return result
        except Exception as e:
            raise e

    
    @classmethod
    def unset_bulk_request(cls, service, resources, args):
        try:
            if (not service.isLogin()):
                service.login()
        
            opt = options()
            opt.action = "unset"
            request = service.payload_formatter.unset_string_bulk(resources, args)
            return cls.post_bulk_data(service, request, opt)
        except Exception as e:
            raise e

    
    @classmethod       
    def add_bulk_request(cls, service, resources, opt=""):
        """ Use this method to perform a add operation on netscaler resources.
        
        Parameters:
			service - nitro_service object.
        	resources - Nitro resources to be added on netscaler.
        	opt - options class object.
        
        Returns:
			status of the performed operation.
        
        Throws:
			Exception  Nitro exception is thrown.
        """
        try:
            if not service.isLogin():
                service.login()
            request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.post_bulk_data(service, request, opt)
            return result
        except Exception as e:
            raise e

    
    @classmethod   
    def delete_bulk_request(cls, service, resources, opt=""):
        """ Use this method to perform a delete operation on netscaler resources.
        
        Parameters:
			service - nitro_service object.
        	resources - Nitro resources to be deleted on netscaler.
        	opt - options class object.
        
        Returns:
			status of the performed operation.
        
        Throws:
			Exception  Nitro exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            opt = options()
            opt.action = "rm"
            type_ = resources[0].__class__.get_object_type()
            if (type_.find("_binding") > 0):
                opt.action = "unbind"
            request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.post_bulk_data(service, request, opt)
            return result
        except Exception as e:
            raise e


    @staticmethod
    def _put(resourcetype, service, request, bulk=""):
        """ This method, forms the http PUT request, applies on the netscaler.
        Reads the response from the netscaler and converts it to base response.
        
        Parameters:
			service - nitro_service object.
        	request - Json request.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception of the type nitro_exception is thrown.
        """
        try :
            ipaddress = service.ipaddress
            version = service.version
            protocol = service.protocol
            if inspect.isclass(resourcetype) :
                resrc_type = resourcetype.get_object_type()
                urlstr = protocol+"://" + ipaddress + "/nitro/" + version + "/config/" + resrc_type     
            else :
                resrc_type = resourcetype.__class__.get_object_type()
                urlstr = protocol+"://" + ipaddress + "/nitro/" + version + "/config/" + resrc_type + "/"+ resourcetype._get_object_name()
            warning = service.warning
            onerror = service.onerror
            if((warning and warning == True) or onerror): 
                if warning and warning==True :
                        urlstr = urlstr + "?warning=yes"
                if onerror :
                    if (warning and warning==True) :
                        urlstr = urlstr + "&onerror=" + onerror
                    else :
                        urlstr = urlstr + "?onerror=" + onerror
            if bulk :
                headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'_list+json','Connection': 'keep-alive', 'Set-Cookie':'NITRO_AUTH_TOKEN='+ service.sessionid}
            else :
                headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'+json','Connection': 'keep-alive', 'Set-Cookie':'NITRO_AUTH_TOKEN='+ service.sessionid}
            response = requests.put(urlstr, data=request, headers=headers, timeout=service.timeout)
            if not response.ok:
                response = json.loads(response.text)
                raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
            elif bulk:
                return response.text
            else:
                nitro_response = {}
                nitro_response['errorcode'] = 0
                nitro_response['message'] = "Done"
                nitro_response['severity']= ""
                return json.dumps(nitro_response)      
        except Exception as e:
            raise e
       
    def put_data(self, service, request):
        try:
            response = self._put(self, service, request)
            result = service.payload_formatter.string_to_resource(base_response, response, self.__class__.__name__)
            if (result.errorcode != 0):
                if (result.errorcode == 444):
                    service.clear_session()
                if (result.severity):
                    if(result.severity  == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result
        except Exception as e:
            raise e

    @classmethod
    def put_bulk_data(cls, service, request):
        try:
            response = cls._put(cls, service, request, True)
            result =service.payload_formatter.string_to_resource(base_responses, response, cls.__name__)
            if (result.errorcode != 0):
                if (result.errorcode == 444): 
                    service.clear_session()
                if(result.severity):
                    if(result.severity == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else:
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result
        except Exception as e:
            raise e

    
    @staticmethod
    def _post(resourcetype, service, request, opt, bulk=""):
        """ This method, forms the http POST request, applies on the netscaler.
        Reads the response from the netscaler and converts it to base response.
        
        Parameters:
			service - nitro_service object.
        	request - Json request.
        
        Returns:
			status of the operation performed.
        
        Throws:
			Exception
        """
        try:
            ipaddress = service.ipaddress
            version = service.version
            protocol = service.protocol
            if inspect.isclass(resourcetype) :
                resrc_type = resourcetype.get_object_type()
            else :
                resrc_type = resourcetype.__class__.get_object_type()
            urlstr = protocol+"://" + ipaddress + "/nitro/" + version + "/config/" + resrc_type 
            warning = service.warning
            onerror = service.onerror
            if( opt or (warning and warning == True) or onerror): 
                if opt :
                    if opt.action :
                        urlstr = urlstr + "?action=" + opt.action
                if warning and warning==True :
                    if opt :
                        urlstr = urlstr + "&warning=yes"
                    else :
                        urlstr = urlstr + "?warning=yes"
                if onerror :
                    if opt or (warning and warning==True) :
                        urlstr = urlstr + "&onerror=" + onerror
                    else :
                        urlstr = urlstr + "?onerror=" + onerror
            if service.sessionid :
                if bulk :
                    headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'_list+json','Connection': 'keep-alive', 'Set-Cookie':'NITRO_AUTH_TOKEN='+ service.sessionid}
                else :
                    headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'+json','Connection': 'keep-alive', 'Set-Cookie':'NITRO_AUTH_TOKEN='+ service.sessionid}
            else :
                headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'+json','Connection': 'keep-alive'}
            response = requests.post(urlstr, data=request, headers=headers, timeout=service.timeout)
            if not response.ok:
                response = json.loads(response.text)
                raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
            elif bulk and  response.text :
                return response.text
            else:
                nitro_response = {}
                if resrc_type == "login" :
                    nitro_response['sessionid']=urllib2.unquote(response.cookies['NITRO_AUTH_TOKEN'])
                nitro_response['errorcode'] = 0
                nitro_response['message'] = "Done"
                nitro_response['severity']= ""
                return json.dumps(nitro_response)      
        except Exception as e:
            raise e
    
    def post_dataEx(self, service, request):
        try:
            response = self._post(self, service, request)
            result = self._get_nitro_response(service, response)
            return result[0]
        except Exception as e:
            raise e
    
    
    def post_data(self, service, request, opt):
        try :
            response = self._post(self, service, request, opt)
            result = service.payload_formatter.string_to_resource(base_response, response, self.__class__.__name__)
            if (result.errorcode != 0 and result.errorcode != 1034):
                if (result.errorcode == 444):
                    service.clear_session()
                if result.severity:
                    if (result.severity == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else:
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result
        except Exception as e:
            raise e

    @classmethod
    def post_bulk_data(cls, service, request, opt=""):
        try:
            response = cls._post(cls, service, request, opt, True)
            result = service.payload_formatter.string_to_resource(base_responses, response, cls.__name__)
            if (result.errorcode != 0):
                if (result.errorcode == 444):
                    service.clear_session()
                if (result.severity):
                    if (result.severity == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else:
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result
        except Exception as e:
            raise e


    def get_request(self, service, opt): 
        """ This method, forms the http GET request, applies on the netscaler.
        Reads the response from the netscaler and converts it to corresponding 
        resource type.
        
        Parameters:
			service - nitro_service object.
        	opt - Options class object
        
        Returns:
			Array of requested resources.
        """
        try:
            ipaddress = service.ipaddress
            version = service.version
            sessionid = service.sessionid
            objtype = self.__class__.get_object_type()
            protocol = service.protocol

            # build URL
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/config/" + objtype;

            name = self._get_object_name();
            if (name and len(name) > 0):
                urlstr = urlstr+"/"+ str(nitro_util.encode(nitro_util.encode(name)))

            if (opt or (service.warning)):
                optionstr = ""
                if (opt):
                    optionstr = opt.to_string()
                    if (len(optionstr) > 0):
                        urlstr = urlstr +"?"
                        urlstr = urlstr + optionstr
                if (service.warning):
                    if (opt and len(optionstr) > 0):
                        urlstr = urlstr+"&"
                    else:
                        urlstr = urlstr+"?"
                    urlstr = urlstr+"warning=yes"
            headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ objtype +'+json','Connection': 'keep-alive', 'Set-Cookie':'NITRO_AUTH_TOKEN='+sessionid}
            response = requests.get(urlstr, headers=headers, timeout=service.timeout)
            if not response.ok:
                response = json.loads(response.text)
                raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
            else:
                result = self._get_nitro_response(service, response.text)
                return result
        except Exception as e:
            raise e

            

    def stat_request(self, service,opt):
        """ This method, forms the http GET request, applies on the netscaler.
        Reads the response from the netscaler and converts it to corresponding stat resource type.
        
        Parameters:
			service
        	opt - Options class object
        
        Returns:
			Array of requested resources.
        """
        try:
            ipaddress = service.ipaddress
            version = service.version
            sessionid = service.sessionid
            objtype = self.__class__.get_object_type()
            objtype = objtype.split('_stats')
            objtype = objtype[0]
            protocol = service.protocol

            # build URL
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/stat/" + objtype;

            name = self._get_object_name();
            if (name and len(name) > 0):
                urlstr = urlstr+"/"+ str(nitro_util.encode(nitro_util.encode(name)))

            if (opt or service.warning):
                optionstr = ""
                if (opt):
                    optionstr = opt.to_string()
                    if (len(optionstr) > 0):
                        urlstr = urlstr +"?"
                        urlstr = urlstr + optionstr
                if (service.warning):
                    if (opt and len(optionstr) > 0):
                        urlstr = urlstr+"&"
                    else:
                        urlstr = urlstr+"?"
                    urlstr = urlstr+"warning=yes"
            headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ objtype +'+json','Connection': 'keep-alive', 'Set-Cookie':'NITRO_AUTH_TOKEN='+sessionid}
            response = requests.get(urlstr, headers=headers, timeout=service.timeout)
            if not response.ok:
                response = json.loads(response.text)
                raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
            else:
                result = self._get_nitro_response(service, response.text)
                return result
        except Exception as e:
            raise e


    def delete_request(self, service, req_args):
        """ This method, forms the http DELETE request, applies on the netscaler.
        Reads the response from the netscaler and converts it to base response.
    
        Parameters:
			service - nitro_service object.
        	req_args
        
        Returns:
			Array of requested resources.
        
        Throws:
			Exception
        """
        try:
            ipaddress = service.ipaddress
            version = service.version
            sessionid = service.sessionid
            objtype = self.__class__.get_object_type()
            protocol = service.protocol

            # build URL
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/config/" + objtype

            name = self._get_object_name()
            if (name and len(name) > 0):
                urlstr = urlstr+"/"+nitro_util.encode(nitro_util.encode(name))

            if(req_args or service.warning):
                urlstr = urlstr+"?"
                if(req_args):
                    urlstr = urlstr + "args=" + req_args
                if(service.warning):
                    if (req_args):
                        urlstr = urlstr+"&"
                    urlstr = urlstr + "warning=yes"
            headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ objtype +'+json','Connection': 'keep-alive', 'Set-Cookie':'NITRO_AUTH_TOKEN='+sessionid}
            response = requests.delete(urlstr, headers=headers, timeout=service.timeout)
            if not response.ok:
                response = json.loads(response.text)
                raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
            result = service.payload_formatter.string_to_resource(base_response, response.text, self.__class__.__name__) 
            if(result.errorcode != 0):
                if (result.errorcode == 444):
                    service.clear_session(self) 
                if result.severity :
                    if (result.severity == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))          
                else:
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity)) 
            return result
        except Exception as e:
            raise e 
