
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


# Provides the classes necessary to create nitro_exception.

class nitro_exception(Exception):
    """ nitro_exception class is used to handle Nitro exceptions.
    
    """
    _severity = ""
    _message = ""
    _errorcode = 0
    
    def __init__(self, errcode = 0, msg="", severity=""):
        """ nitro_exception Class constructor specifying the error message and error code.
        """
        self._severity = severity
        self._message = msg
        self._errorcode = errcode

    @property
    def errorcode(self):
        """Gets the error code.
           
           Returns:
           gets the error code.
        """
        return self._errorcode


    @property
    def message(self):
        """Gets the error message.
           
           Returns:
           gets the error message.
        """
        return self._message

    @property
    def severity(self):
        """ Gets the error severity.
            
            Returns:
            gets the error severity.
        """
        return self._severity

