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

class appflowpolicy_binding(base_resource):
	""" Binding class showing the resources that can be bound to appflowpolicy_binding. 
	"""
	def __init__(self) :
		self._name = ""
		self.appflowpolicy_csvserver_binding = []
		self.appflowpolicy_lbvserver_binding = []
		self.appflowpolicy_appflowglobal_binding = []
		self.appflowpolicy_vpnvserver_binding = []
		self.appflowpolicy_appflowpolicylabel_binding = []

	@property
	def name(self) :
		ur"""Name of the policy about which to display detailed information.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the policy about which to display detailed information.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def appflowpolicy_appflowpolicylabel_bindings(self) :
		ur"""appflowpolicylabel that can be bound to appflowpolicy.
		"""
		try :
			return self._appflowpolicy_appflowpolicylabel_binding
		except Exception as e:
			raise e

	@property
	def appflowpolicy_csvserver_bindings(self) :
		ur"""csvserver that can be bound to appflowpolicy.
		"""
		try :
			return self._appflowpolicy_csvserver_binding
		except Exception as e:
			raise e

	@property
	def appflowpolicy_vpnvserver_bindings(self) :
		ur"""vpnvserver that can be bound to appflowpolicy.
		"""
		try :
			return self._appflowpolicy_vpnvserver_binding
		except Exception as e:
			raise e

	@property
	def appflowpolicy_lbvserver_bindings(self) :
		ur"""lbvserver that can be bound to appflowpolicy.
		"""
		try :
			return self._appflowpolicy_lbvserver_binding
		except Exception as e:
			raise e

	@property
	def appflowpolicy_appflowglobal_bindings(self) :
		ur"""appflowglobal that can be bound to appflowpolicy.
		"""
		try :
			return self._appflowpolicy_appflowglobal_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appflowpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appflowpolicy_binding
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
		ur""" Use this API to fetch appflowpolicy_binding resource.
		"""
		try :
			if type(name) is not list :
				obj = appflowpolicy_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [appflowpolicy_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class appflowpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appflowpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appflowpolicy_binding = [appflowpolicy_binding() for _ in range(length)]

