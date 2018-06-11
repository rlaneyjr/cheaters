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

class authenticationvserver_binding(base_resource):
	""" Binding class showing the resources that can be bound to authenticationvserver_binding. 
	"""
	def __init__(self) :
		self._name = ""
		self.authenticationvserver_auditnslogpolicy_binding = []
		self.authenticationvserver_authenticationpolicy_binding = []
		self.authenticationvserver_authenticationradiuspolicy_binding = []
		self.authenticationvserver_authenticationldappolicy_binding = []
		self.authenticationvserver_authenticationsamlidppolicy_binding = []
		self.authenticationvserver_authenticationwebauthpolicy_binding = []
		self.authenticationvserver_authenticationlocalpolicy_binding = []
		self.authenticationvserver_authenticationnegotiatepolicy_binding = []
		self.authenticationvserver_authenticationtacacspolicy_binding = []
		self.authenticationvserver_authenticationsamlpolicy_binding = []
		self.authenticationvserver_auditsyslogpolicy_binding = []
		self.authenticationvserver_authenticationcertpolicy_binding = []
		self.authenticationvserver_tmsessionpolicy_binding = []

	@property
	def name(self) :
		ur"""Name of the authentication virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the authentication virtual server.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationlocalpolicy_bindings(self) :
		ur"""authenticationlocalpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationlocalpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_tmsessionpolicy_bindings(self) :
		ur"""tmsessionpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_tmsessionpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_auditsyslogpolicy_bindings(self) :
		ur"""auditsyslogpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_auditsyslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationsamlidppolicy_bindings(self) :
		ur"""authenticationsamlidppolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationsamlidppolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_auditnslogpolicy_bindings(self) :
		ur"""auditnslogpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_auditnslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationldappolicy_bindings(self) :
		ur"""authenticationldappolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationldappolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationcertpolicy_bindings(self) :
		ur"""authenticationcertpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationcertpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationsamlpolicy_bindings(self) :
		ur"""authenticationsamlpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationsamlpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationpolicy_bindings(self) :
		ur"""authenticationpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationradiuspolicy_bindings(self) :
		ur"""authenticationradiuspolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationradiuspolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationtacacspolicy_bindings(self) :
		ur"""authenticationtacacspolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationtacacspolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationwebauthpolicy_bindings(self) :
		ur"""authenticationwebauthpolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationwebauthpolicy_binding
		except Exception as e:
			raise e

	@property
	def authenticationvserver_authenticationnegotiatepolicy_bindings(self) :
		ur"""authenticationnegotiatepolicy that can be bound to authenticationvserver.
		"""
		try :
			return self._authenticationvserver_authenticationnegotiatepolicy_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationvserver_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, name) :
		ur""" Use this API to fetch authenticationvserver_binding resource.
		"""
		try :
			if type(name) is not list :
				obj = authenticationvserver_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [authenticationvserver_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class authenticationvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationvserver_binding = [authenticationvserver_binding() for _ in range(length)]

