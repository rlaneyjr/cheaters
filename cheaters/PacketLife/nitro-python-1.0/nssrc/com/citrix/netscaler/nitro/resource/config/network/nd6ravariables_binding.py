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

class nd6ravariables_binding(base_resource):
	""" Binding class showing the resources that can be bound to nd6ravariables_binding. 
	"""
	def __init__(self) :
		self._vlan = 0
		self.nd6ravariables_onlinkipv6prefix_binding = []

	@property
	def vlan(self) :
		ur"""The VLAN number.<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		ur"""The VLAN number.<br/>Minimum value =  0<br/>Maximum value =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def nd6ravariables_onlinkipv6prefix_bindings(self) :
		ur"""onlinkipv6prefix that can be bound to nd6ravariables.
		"""
		try :
			return self._nd6ravariables_onlinkipv6prefix_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nd6ravariables_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nd6ravariables_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.vlan is not None :
				return str(self.vlan)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, vlan) :
		ur""" Use this API to fetch nd6ravariables_binding resource.
		"""
		try :
			if type(vlan) is not list :
				obj = nd6ravariables_binding()
				obj.vlan = vlan
				response = obj.get_resource(service)
			else :
				if vlan and len(vlan) > 0 :
					obj = [nd6ravariables_binding() for _ in range(len(vlan))]
					for i in range(len(vlan)) :
						obj[i].vlan = vlan[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class nd6ravariables_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nd6ravariables_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nd6ravariables_binding = [nd6ravariables_binding() for _ in range(length)]

