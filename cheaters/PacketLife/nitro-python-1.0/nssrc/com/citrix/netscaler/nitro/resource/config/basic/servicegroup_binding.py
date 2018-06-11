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

class servicegroup_binding(base_resource):
	""" Binding class showing the resources that can be bound to servicegroup_binding. 
	"""
	def __init__(self) :
		self._servicegroupname = ""
		self.servicegroup_servicegroupentitymonbindings_binding = []
		self.servicegroup_lbmonitor_binding = []
		self.servicegroup_servicegroupmember_binding = []

	@property
	def servicegroupname(self) :
		ur"""Name of the service group.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		ur"""Name of the service group.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def servicegroup_lbmonitor_bindings(self) :
		ur"""lbmonitor that can be bound to servicegroup.
		"""
		try :
			return self._servicegroup_lbmonitor_binding
		except Exception as e:
			raise e

	@property
	def servicegroup_servicegroupmember_bindings(self) :
		ur"""servicegroupmember that can be bound to servicegroup.
		"""
		try :
			return self._servicegroup_servicegroupmember_binding
		except Exception as e:
			raise e

	@property
	def servicegroup_servicegroupentitymonbindings_bindings(self) :
		ur"""servicegroupentitymonbindings that can be bound to servicegroup.
		"""
		try :
			return self._servicegroup_servicegroupentitymonbindings_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(servicegroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicegroup_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, servicegroupname) :
		ur""" Use this API to fetch servicegroup_binding resource.
		"""
		try :
			if type(servicegroupname) is not list :
				obj = servicegroup_binding()
				obj.servicegroupname = servicegroupname
				response = obj.get_resource(service)
			else :
				if servicegroupname and len(servicegroupname) > 0 :
					obj = [servicegroup_binding() for _ in range(len(servicegroupname))]
					for i in range(len(servicegroupname)) :
						obj[i].servicegroupname = servicegroupname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class servicegroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.servicegroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.servicegroup_binding = [servicegroup_binding() for _ in range(length)]

