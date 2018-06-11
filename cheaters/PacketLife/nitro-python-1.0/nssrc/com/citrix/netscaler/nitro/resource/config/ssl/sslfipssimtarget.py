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

class sslfipssimtarget(base_resource) :
	""" Configuration for FIPS SIM Target resource. """
	def __init__(self) :
		self._keyvector = ""
		self._sourcesecret = ""
		self._certfile = ""
		self._targetsecret = ""

	@property
	def keyvector(self) :
		ur"""Name of and, optionally, path to the target FIPS appliance's key vector. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._keyvector
		except Exception as e:
			raise e

	@keyvector.setter
	def keyvector(self, keyvector) :
		ur"""Name of and, optionally, path to the target FIPS appliance's key vector. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._keyvector = keyvector
		except Exception as e:
			raise e

	@property
	def sourcesecret(self) :
		ur"""Name of and, optionally, path to the source FIPS appliance's secret data. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._sourcesecret
		except Exception as e:
			raise e

	@sourcesecret.setter
	def sourcesecret(self, sourcesecret) :
		ur"""Name of and, optionally, path to the source FIPS appliance's secret data. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._sourcesecret = sourcesecret
		except Exception as e:
			raise e

	@property
	def certfile(self) :
		ur"""Name of and, optionally, path to the source FIPS appliance's certificate file. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._certfile
		except Exception as e:
			raise e

	@certfile.setter
	def certfile(self, certfile) :
		ur"""Name of and, optionally, path to the source FIPS appliance's certificate file. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._certfile = certfile
		except Exception as e:
			raise e

	@property
	def targetsecret(self) :
		ur"""Name for and, optionally, path to the target FIPS appliance's secret data. The default input path for the secret data is /nsconfig/ssl/.<br/>Minimum length =  1.
		"""
		try :
			return self._targetsecret
		except Exception as e:
			raise e

	@targetsecret.setter
	def targetsecret(self, targetsecret) :
		ur"""Name for and, optionally, path to the target FIPS appliance's secret data. The default input path for the secret data is /nsconfig/ssl/.<br/>Minimum length =  1
		"""
		try :
			self._targetsecret = targetsecret
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslfipssimtarget_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslfipssimtarget
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
	def enable(cls, client, resource) :
		ur""" Use this API to enable sslfipssimtarget.
		"""
		try :
			if type(resource) is not list :
				enableresource = sslfipssimtarget()
				enableresource.keyvector = resource.keyvector
				enableresource.sourcesecret = resource.sourcesecret
				return enableresource.perform_operation(client,"enable")
		except Exception as e :
			raise e

	@classmethod
	def init(cls, client, resource) :
		ur""" Use this API to init sslfipssimtarget.
		"""
		try :
			if type(resource) is not list :
				initresource = sslfipssimtarget()
				initresource.certfile = resource.certfile
				initresource.keyvector = resource.keyvector
				initresource.targetsecret = resource.targetsecret
				return initresource.perform_operation(client,"init")
		except Exception as e :
			raise e

class sslfipssimtarget_response(base_response) :
	def __init__(self, length=1) :
		self.sslfipssimtarget = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslfipssimtarget = [sslfipssimtarget() for _ in range(length)]

