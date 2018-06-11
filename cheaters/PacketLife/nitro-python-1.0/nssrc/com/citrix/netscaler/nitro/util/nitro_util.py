
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
 
import urllib
 

class nitro_util:
    """nitro_util class provides a way to create a string out of the object fields that are set. 
    """

    @classmethod
    def encode(cls, st):
        """ encodes the given string using URLEncoder.
        
        Parameters:
            st String that is to be encoded.
        
        Returns:
            encoded string.
        """
        try:
            #check for whether user is using python version >= 3.0
            return urllib.quote_plus(st)
        except ImportError:
            #check for whether user is using python version < 3.0
            return urllib.quote(st, safe="")
        except Exception as e:
            raise e

            
    @classmethod
    def object_to_string(cls, obj):
        """ create a string out of the object fields that are set
        
        Parameters:
            obj Object
        
        Returns:
            String in Json format.
        
        Throws:
            Exception Nitro exception is thrown.
        """
        try:
            str_ = ""
            flds = obj.__dict__
            flds = dict((k.replace('_',''), v) for k, v in flds.items() if v)
            if (flds):
                for k,v in flds.items() :
                    str_ = str_ + "\"" + k + "\":"
                    if type(v) is unicode :
                        v = v.encode('utf8'); 	
                    if type(v) is bool :
                        str_ = str_ + v                     
                    elif type(v) is str :
                        str_ = str_ + "\"" + v + "\""                                        
                    elif type(v) is int :
                        str_ = str_ + "\"" + str(v) + "\""
                    if str_ :
                        str_ = str_ + ","
            return str_
        except Exception as e:
            raise e

            
    @classmethod
    def object_to_string_withoutquotes(cls, obj):
        """ create a string (without quotes)out of the object fields that are set
        
        Parameters:
            obj Object
        
        Returns:
            String in Json format.
        
        Throws:
            Exception Nitro exception is thrown.
        """
        try:
            str_ = ""
            flds = obj.__dict__
            flds = dict((k.replace('_',''), v) for k, v in flds.items() if v)
            i = 0
            if (flds):
                for k,v in flds.items() :
                    str_ = str_ + k + ":"
                    if type(v) is unicode :
                        v = v.encode('utf8'); 
                    if type(v) is bool :
                        str_ = str_ + v                     
                    elif type(v) is str :
                        str_ = str_ + cls.encode(v)                                         
                    elif type(v) is int :
                        str_ = str_ + str(v)
                    i = i + 1 
                    if i != (len(flds.items())) and str_ :
                        str_ = str_ + ","
            return str_
        except Exception as e:
            raise e


