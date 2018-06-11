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

class nstrafficdomain_binding(base_resource):
	""" Binding class showing the resources that can be bound to nstrafficdomain_binding. 
	"""
	def __init__(self) :
		self._td = 0
		self.nstrafficdomain_bridgegroup_binding = []
		self.nstrafficdomain_vlan_binding = []
		self.nstrafficdomain_vxlan_binding = []

	@property
	def td(self) :
		ur"""Integer value that uniquely identifies a traffic domain.<br/>Minimum value =  1<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Integer value that uniquely identifies a traffic domain.<br/>Minimum value =  1<br/>Maximum value =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def nstrafficdomain_vlan_bindings(self) :
		ur"""vlan that can be bound to nstrafficdomain.
		"""
		try :
			return self._nstrafficdomain_vlan_binding
		except Exception as e:
			raise e

	@property
	def nstrafficdomain_bridgegroup_bindings(self) :
		ur"""bridgegroup that can be bound to nstrafficdomain.
		"""
		try :
			return self._nstrafficdomain_bridgegroup_binding
		except Exception as e:
			raise e

	@property
	def nstrafficdomain_vxlan_bindings(self) :
		ur"""vxlan that can be bound to nstrafficdomain.
		"""
		try :
			return self._nstrafficdomain_vxlan_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstrafficdomain_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstrafficdomain_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.td is not None :
				return str(self.td)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, td) :
		ur""" Use this API to fetch nstrafficdomain_binding resource.
		"""
		try :
			if type(td) is not list :
				obj = nstrafficdomain_binding()
				obj.td = td
				response = obj.get_resource(service)
			else :
				if td and len(td) > 0 :
					obj = [nstrafficdomain_binding() for _ in range(len(td))]
					for i in range(len(td)) :
						obj[i].td = td[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class nstrafficdomain_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nstrafficdomain_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstrafficdomain_binding = [nstrafficdomain_binding() for _ in range(length)]

