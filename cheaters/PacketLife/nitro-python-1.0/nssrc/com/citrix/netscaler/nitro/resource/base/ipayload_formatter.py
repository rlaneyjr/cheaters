
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


import abc

class ipayload_formatter: 
    """ ipayload_formatter is the interface class for Json.
    This includes methods for converting Json to nitro resource and vice versa.
    Provides classes necessary to create base_resource, base_response, Json, login, logout and 
    reboot objects.
    """
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def resource_to_string_convert(self, resrc):
        pass
    
    @abc.abstractmethod
    def resource_to_string(self, resrc):
        pass
    
    @abc.abstractmethod
    def unset_string(self, resrc, args):
        pass
    
    @abc.abstractmethod
    def unset_string_bulk(self, resrcources, args):
        pass
    
    @abc.abstractmethod
    def resource_to_string_bulk(self, resrcources):
        pass

    @abc.abstractmethod
    def string_to_resource(self, responseClass, response_dict, resrc_type):
        pass