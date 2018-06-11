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

class spilloverpolicy_binding(base_resource):
	""" Binding class showing the resources that can be bound to spilloverpolicy_binding. 
	"""
	def __init__(self) :
		self._name = ""
		self.spilloverpolicy_gslbvserver_binding = []
		self.spilloverpolicy_csvserver_binding = []
		self.spilloverpolicy_lbvserver_binding = []

	@property
	def name(self) :
		ur"""Name of the spillover policy.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the spillover policy.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def spilloverpolicy_csvserver_bindings(self) :
		ur"""csvserver that can be bound to spilloverpolicy.
		"""
		try :
			return self._spilloverpolicy_csvserver_binding
		except Exception as e:
			raise e

	@property
	def spilloverpolicy_lbvserver_bindings(self) :
		ur"""lbvserver that can be bound to spilloverpolicy.
		"""
		try :
			return self._spilloverpolicy_lbvserver_binding
		except Exception as e:
			raise e

	@property
	def spilloverpolicy_gslbvserver_bindings(self) :
		ur"""gslbvserver that can be bound to spilloverpolicy.
		"""
		try :
			return self._spilloverpolicy_gslbvserver_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(spilloverpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.spilloverpolicy_binding
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
		ur""" Use this API to fetch spilloverpolicy_binding resource.
		"""
		try :
			if type(name) is not list :
				obj = spilloverpolicy_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [spilloverpolicy_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class spilloverpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.spilloverpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.spilloverpolicy_binding = [spilloverpolicy_binding() for _ in range(length)]

