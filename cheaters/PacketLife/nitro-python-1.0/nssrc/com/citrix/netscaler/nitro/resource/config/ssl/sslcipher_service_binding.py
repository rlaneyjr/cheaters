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

class sslcipher_service_binding(base_resource) :
	""" Binding class showing the service that can be bound to sslcipher.
	"""
	def __init__(self) :
		self._ciphergroupname = ""
		self._servicename = ""
		self._service = False
		self._servicegroupname = ""
		self._servicegroup = False
		self._cipheroperation = ""
		self._ciphgrpals = ""

	@property
	def ciphgrpals(self) :
		ur"""A cipher-suite can consist of an individual cipher name, the system predefined cipher-alias name, or user defined cipher-group name.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphgrpals
		except Exception as e:
			raise e

	@ciphgrpals.setter
	def ciphgrpals(self, ciphgrpals) :
		ur"""A cipher-suite can consist of an individual cipher name, the system predefined cipher-alias name, or user defined cipher-group name.<br/>Minimum length =  1
		"""
		try :
			self._ciphgrpals = ciphgrpals
		except Exception as e:
			raise e

	@property
	def servicegroupname(self) :
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def servicegroup(self) :
		ur"""Indicates that the cipher operation is to be performed on the named SSL service or service group.
		"""
		try :
			return self._servicegroup
		except Exception as e:
			raise e

	@servicegroup.setter
	def servicegroup(self, servicegroup) :
		ur"""Indicates that the cipher operation is to be performed on the named SSL service or service group.
		"""
		try :
			self._servicegroup = servicegroup
		except Exception as e:
			raise e

	@property
	def service(self) :
		ur"""Indicates that the cipher operation is to be performed on the named SSL service or service group.
		"""
		try :
			return self._service
		except Exception as e:
			raise e

	@service.setter
	def service(self, service) :
		ur"""Indicates that the cipher operation is to be performed on the named SSL service or service group.
		"""
		try :
			self._service = service
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def ciphergroupname(self) :
		ur"""Name of the user-defined cipher group.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphergroupname
		except Exception as e:
			raise e

	@ciphergroupname.setter
	def ciphergroupname(self, ciphergroupname) :
		ur"""Name of the user-defined cipher group.<br/>Minimum length =  1
		"""
		try :
			self._ciphergroupname = ciphergroupname
		except Exception as e:
			raise e

	@property
	def cipheroperation(self) :
		ur"""The operation that is performed when adding the cipher-suite.
		Possible cipher operations are:
		ADD - Appends the given cipher-suite to the existing one configured for the virtual server.
		REM - Removes the given cipher-suite from the existing one configured for the virtual server.
		ORD - Overrides the current configured cipher-suite for the virtual server with the given cipher-suite.<br/>Default value: 0<br/>Possible values = ADD, REM, ORD.
		"""
		try :
			return self._cipheroperation
		except Exception as e:
			raise e

	@cipheroperation.setter
	def cipheroperation(self, cipheroperation) :
		ur"""The operation that is performed when adding the cipher-suite.
		Possible cipher operations are:
		ADD - Appends the given cipher-suite to the existing one configured for the virtual server.
		REM - Removes the given cipher-suite from the existing one configured for the virtual server.
		ORD - Overrides the current configured cipher-suite for the virtual server with the given cipher-suite.<br/>Default value: 0<br/>Possible values = ADD, REM, ORD
		"""
		try :
			self._cipheroperation = cipheroperation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcipher_service_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcipher_service_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ciphergroupname is not None :
				return str(self.ciphergroupname)
			return None
		except Exception as e :
			raise e



	class Cipheroperation:
		ADD = "ADD"
		REM = "REM"
		ORD = "ORD"

class sslcipher_service_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcipher_service_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcipher_service_binding = [sslcipher_service_binding() for _ in range(length)]

