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

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class nsencryptionparams(base_resource) :
	def __init__(self) :
		self._method = ""
		self._keyvalue = ""

	@property
	def method(self) :
		ur"""Cipher method (and key length) to be used to encrypt and decrypt content. The default value is AES256.<br/>Possible values = NONE, RC4, DES3, AES128, AES192, AES256.
		"""
		try :
			return self._method
		except Exception as e:
			raise e

	@method.setter
	def method(self, method) :
		ur"""Cipher method (and key length) to be used to encrypt and decrypt content. The default value is AES256.<br/>Possible values = NONE, RC4, DES3, AES128, AES192, AES256
		"""
		try :
			self._method = method
		except Exception as e:
			raise e

	@property
	def keyvalue(self) :
		ur"""The base64-encoded key generation number, method, and key value.
		Note:
		* Do not include this argument if you are changing the encryption method.
		* To generate a new key value for the current encryption method, specify an empty string \(""\) as the value of this parameter. The parameter is passed implicitly, with its automatically generated value, to the NetScaler packet engines even when it is not included in the command. Passing the parameter to the packet engines enables the appliance to save the key value to the configuration file and to propagate the key value to the secondary appliance in a high availability setup.
		"""
		try :
			return self._keyvalue
		except Exception as e:
			raise e

	@keyvalue.setter
	def keyvalue(self, keyvalue) :
		ur"""The base64-encoded key generation number, method, and key value.
		Note:
		* Do not include this argument if you are changing the encryption method.
		* To generate a new key value for the current encryption method, specify an empty string \(""\) as the value of this parameter. The parameter is passed implicitly, with its automatically generated value, to the NetScaler packet engines even when it is not included in the command. Passing the parameter to the packet engines enables the appliance to save the key value to the configuration file and to propagate the key value to the secondary appliance in a high availability setup.
		"""
		try :
			self._keyvalue = keyvalue
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsencryptionparams_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsencryptionparams
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nsencryptionparams.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsencryptionparams()
				updateresource.method = resource.method
				updateresource.keyvalue = resource.keyvalue
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsencryptionparams resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsencryptionparams()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Method:
		NONE = "NONE"
		RC4 = "RC4"
		DES3 = "DES3"
		AES128 = "AES128"
		AES192 = "AES192"
		AES256 = "AES256"

class nsencryptionparams_response(base_response) :
	def __init__(self, length=1) :
		self.nsencryptionparams = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsencryptionparams = [nsencryptionparams() for _ in range(length)]

