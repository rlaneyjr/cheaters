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

class sslpkcs8(base_resource) :
	""" Configuration for pkcs8 resource. """
	def __init__(self) :
		self._pkcs8file = ""
		self._keyfile = ""
		self._keyform = ""
		self._password = ""

	@property
	def pkcs8file(self) :
		ur"""Name for and, optionally, path to, the output file where the PKCS#8 format key file is stored. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._pkcs8file
		except Exception as e:
			raise e

	@pkcs8file.setter
	def pkcs8file(self, pkcs8file) :
		ur"""Name for and, optionally, path to, the output file where the PKCS#8 format key file is stored. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._pkcs8file = pkcs8file
		except Exception as e:
			raise e

	@property
	def keyfile(self) :
		ur"""Name of and, optionally, path to the input key file to be converted from PEM or DER format to PKCS#8 format. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._keyfile
		except Exception as e:
			raise e

	@keyfile.setter
	def keyfile(self, keyfile) :
		ur"""Name of and, optionally, path to the input key file to be converted from PEM or DER format to PKCS#8 format. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._keyfile = keyfile
		except Exception as e:
			raise e

	@property
	def keyform(self) :
		ur"""Format in which the key file is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._keyform
		except Exception as e:
			raise e

	@keyform.setter
	def keyform(self, keyform) :
		ur"""Format in which the key file is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._keyform = keyform
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password to assign to the file if the key is encrypted. Applies only for PEM format files.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password to assign to the file if the key is encrypted. Applies only for PEM format files.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslpkcs8_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslpkcs8
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
	def convert(cls, client, resource) :
		ur""" Use this API to convert sslpkcs8.
		"""
		try :
			if type(resource) is not list :
				convertresource = sslpkcs8()
				convertresource.pkcs8file = resource.pkcs8file
				convertresource.keyfile = resource.keyfile
				convertresource.keyform = resource.keyform
				convertresource.password = resource.password
				return convertresource.perform_operation(client,"convert")
		except Exception as e :
			raise e

	class Keyform:
		DER = "DER"
		PEM = "PEM"

class sslpkcs8_response(base_response) :
	def __init__(self, length=1) :
		self.sslpkcs8 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslpkcs8 = [sslpkcs8() for _ in range(length)]

