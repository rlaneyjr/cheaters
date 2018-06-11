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

class sslrsakey(base_resource) :
	""" Configuration for RSA key resource. """
	def __init__(self) :
		self._keyfile = ""
		self._bits = 0
		self._exponent = ""
		self._keyform = ""
		self._des = False
		self._des3 = False
		self._password = ""

	@property
	def keyfile(self) :
		ur"""Name for and, optionally, path to the RSA key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._keyfile
		except Exception as e:
			raise e

	@keyfile.setter
	def keyfile(self, keyfile) :
		ur"""Name for and, optionally, path to the RSA key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._keyfile = keyfile
		except Exception as e:
			raise e

	@property
	def bits(self) :
		ur"""Size, in bits, of the RSA key.<br/>Minimum length =  512<br/>Maximum length =  4096.
		"""
		try :
			return self._bits
		except Exception as e:
			raise e

	@bits.setter
	def bits(self, bits) :
		ur"""Size, in bits, of the RSA key.<br/>Minimum length =  512<br/>Maximum length =  4096
		"""
		try :
			self._bits = bits
		except Exception as e:
			raise e

	@property
	def exponent(self) :
		ur"""Public exponent for the RSA key. The exponent is part of the cipher algorithm and is required for creating the RSA key.<br/>Default value: F4<br/>Possible values = 3, F4.
		"""
		try :
			return self._exponent
		except Exception as e:
			raise e

	@exponent.setter
	def exponent(self, exponent) :
		ur"""Public exponent for the RSA key. The exponent is part of the cipher algorithm and is required for creating the RSA key.<br/>Default value: F4<br/>Possible values = 3, F4
		"""
		try :
			self._exponent = exponent
		except Exception as e:
			raise e

	@property
	def keyform(self) :
		ur"""Format in which the RSA key file is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._keyform
		except Exception as e:
			raise e

	@keyform.setter
	def keyform(self, keyform) :
		ur"""Format in which the RSA key file is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._keyform = keyform
		except Exception as e:
			raise e

	@property
	def des(self) :
		ur"""Encrypt the generated RSA key by using the DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			return self._des
		except Exception as e:
			raise e

	@des.setter
	def des(self, des) :
		ur"""Encrypt the generated RSA key by using the DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			self._des = des
		except Exception as e:
			raise e

	@property
	def des3(self) :
		ur"""Encrypt the generated RSA key by using the Triple-DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			return self._des3
		except Exception as e:
			raise e

	@des3.setter
	def des3(self, des3) :
		ur"""Encrypt the generated RSA key by using the Triple-DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			self._des3 = des3
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Pass phrase to use for encryption if DES or DES3 option is selected.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Pass phrase to use for encryption if DES or DES3 option is selected.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslrsakey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslrsakey
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
	def create(cls, client, resource) :
		ur""" Use this API to create sslrsakey.
		"""
		try :
			if type(resource) is not list :
				createresource = sslrsakey()
				createresource.keyfile = resource.keyfile
				createresource.bits = resource.bits
				createresource.exponent = resource.exponent
				createresource.keyform = resource.keyform
				createresource.des = resource.des
				createresource.des3 = resource.des3
				createresource.password = resource.password
				return createresource.perform_operation(client,"create")
		except Exception as e :
			raise e

	class Keyform:
		DER = "DER"
		PEM = "PEM"

	class Exponent:
		_3 = "3"
		F4 = "F4"

class sslrsakey_response(base_response) :
	def __init__(self, length=1) :
		self.sslrsakey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslrsakey = [sslrsakey() for _ in range(length)]

