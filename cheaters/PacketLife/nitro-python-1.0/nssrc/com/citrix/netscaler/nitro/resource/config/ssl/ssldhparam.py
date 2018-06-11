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

class ssldhparam(base_resource) :
	""" Configuration for dh Parameter resource. """
	def __init__(self) :
		self._dhfile = ""
		self._bits = 0
		self._gen = ""

	@property
	def dhfile(self) :
		ur"""Name of and, optionally, path to the DH key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._dhfile
		except Exception as e:
			raise e

	@dhfile.setter
	def dhfile(self, dhfile) :
		ur"""Name of and, optionally, path to the DH key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._dhfile = dhfile
		except Exception as e:
			raise e

	@property
	def bits(self) :
		ur"""Size, in bits, of the DH key being generated.<br/>Minimum length =  512<br/>Maximum length =  2048.
		"""
		try :
			return self._bits
		except Exception as e:
			raise e

	@bits.setter
	def bits(self, bits) :
		ur"""Size, in bits, of the DH key being generated.<br/>Minimum length =  512<br/>Maximum length =  2048
		"""
		try :
			self._bits = bits
		except Exception as e:
			raise e

	@property
	def gen(self) :
		ur"""Random number required for generating the DH key. Required as part of the DH key generation algorithm.<br/>Default value: 2<br/>Possible values = 2, 5.
		"""
		try :
			return self._gen
		except Exception as e:
			raise e

	@gen.setter
	def gen(self, gen) :
		ur"""Random number required for generating the DH key. Required as part of the DH key generation algorithm.<br/>Default value: 2<br/>Possible values = 2, 5
		"""
		try :
			self._gen = gen
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ssldhparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssldhparam
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
		ur""" Use this API to create ssldhparam.
		"""
		try :
			if type(resource) is not list :
				createresource = ssldhparam()
				createresource.dhfile = resource.dhfile
				createresource.bits = resource.bits
				createresource.gen = resource.gen
				return createresource.perform_operation(client,"create")
		except Exception as e :
			raise e

	class Gen:
		_2 = "2"
		_5 = "5"

class ssldhparam_response(base_response) :
	def __init__(self, length=1) :
		self.ssldhparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ssldhparam = [ssldhparam() for _ in range(length)]

