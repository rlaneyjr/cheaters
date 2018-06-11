
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
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource

class configobjects(base_resource): 
    _objects=[]
    
    def get_objects(self):
        try:
            return self.objects
        except Exception as e:
            raise e
    
    def _get_nitro_response(self, service, response):
        try:
            resources = [configobjects() for _ in range(1)]
            result = service.get_payload_formatter().string_to_resource(configobjects_response, response)
            if(result.errorcode != 0):
                if (result.errorcode == 444):
                    service.clear_session()
                if(result.severity is not None):
                    if (result.severity == "ERROR"):
                        raise nitro_exception(result.message,result.errorcode)
                else:
                    raise nitro_exception(result.message,result.errorcode)
            resources[0] = result.configobjects
            return resources
        except Exception as e:
            raise e

        

    def _get_object_name(self):
        return None
    
    
    @staticmethod
    def get(self, service):
        """ Use this API to fetch all the config objects resources that are available on netscaler.
        """
        try:
            obj = configobjects()
            response = obj.get_resources(service)
            return response[0]
        except Exception as e:
            raise e
        
class configobjects_response(base_response):
    configobjects = configobjects()
