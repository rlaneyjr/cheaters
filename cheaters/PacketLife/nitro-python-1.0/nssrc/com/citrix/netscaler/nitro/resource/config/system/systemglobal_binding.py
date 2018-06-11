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

class systemglobal_binding(base_resource):
	""" Binding class showing the resources that can be bound to systemglobal_binding. 
	"""
	def __init__(self) :
		self.systemglobal_auditnslogpolicy_binding = []
		self.systemglobal_authenticationpolicy_binding = []
		self.systemglobal_authenticationradiuspolicy_binding = []
		self.systemglobal_authenticationldappolicy_binding = []
		self.systemglobal_authenticationlocalpolicy_binding = []
		self.systemglobal_authenticationtacacspolicy_binding = []
		self.systemglobal_auditsyslogpolicy_binding = []

	@property
	def systemglobal_authenticationtacacspolicy_bindings(self) :
		ur"""authenticationtacacspolicy that can be bound to systemglobal.
		"""
		try :
			return self._systemglobal_authenticationtacacspolicy_binding
		except Exception as e:
			raise e

	@property
	def systemglobal_authenticationpolicy_bindings(self) :
		ur"""authenticationpolicy that can be bound to systemglobal.
		"""
		try :
			return self._systemglobal_authenticationpolicy_binding
		except Exception as e:
			raise e

	@property
	def systemglobal_authenticationldappolicy_bindings(self) :
		ur"""authenticationldappolicy that can be bound to systemglobal.
		"""
		try :
			return self._systemglobal_authenticationldappolicy_binding
		except Exception as e:
			raise e

	@property
	def systemglobal_auditsyslogpolicy_bindings(self) :
		ur"""auditsyslogpolicy that can be bound to systemglobal.
		"""
		try :
			return self._systemglobal_auditsyslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def systemglobal_authenticationlocalpolicy_bindings(self) :
		ur"""authenticationlocalpolicy that can be bound to systemglobal.
		"""
		try :
			return self._systemglobal_authenticationlocalpolicy_binding
		except Exception as e:
			raise e

	@property
	def systemglobal_authenticationradiuspolicy_bindings(self) :
		ur"""authenticationradiuspolicy that can be bound to systemglobal.
		"""
		try :
			return self._systemglobal_authenticationradiuspolicy_binding
		except Exception as e:
			raise e

	@property
	def systemglobal_auditnslogpolicy_bindings(self) :
		ur"""auditnslogpolicy that can be bound to systemglobal.
		"""
		try :
			return self._systemglobal_auditnslogpolicy_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemglobal_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemglobal_binding
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
	def get(self, service) :
		ur""" Use this API to fetch a systemglobal_binding resource .
		"""
		try :
			obj = systemglobal_binding()
			response = obj.get_resource(service)
			return response

		except Exception as e:
			raise e

class systemglobal_binding_response(base_response) :
	def __init__(self, length=1) :
		self.systemglobal_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemglobal_binding = [systemglobal_binding() for _ in range(length)]

