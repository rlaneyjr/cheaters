
# Copyright (c) 2004-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use self file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource



class login(base_resource): 
    """ Nitro login resource class.
    """
    username=""
    password=""
    timeout=""
    eula=""    
    
    
    def __init__(self, username, password, timeout="", eula=""):    
        """ login class constructor specifying username and password for 
        logging into Netscaler.
        
        Parameters:
            username - username 
            password - password
            timeout - session timeout in seconds.default timeout is 1800secs.
            eula - response.
        """
        self.username = username
        self.password = password
        if timeout:
            self.timeout = timeout
        if eula:    
            self.eula = eula
        
    def _get_object_name(self): 
        return None
    
    def  _get_nitro_response(self, service, response): 
        """ gets the Nitro responce.
        """
        return None
