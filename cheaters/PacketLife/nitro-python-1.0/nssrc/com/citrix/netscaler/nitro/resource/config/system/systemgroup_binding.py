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

class systemgroup_binding(base_resource):
	""" Binding class showing the resources that can be bound to systemgroup_binding. 
	"""
	def __init__(self) :
		self._groupname = ""
		self.systemgroup_systemuser_binding = []
		self.systemgroup_systemcmdpolicy_binding = []

	@property
	def groupname(self) :
		ur"""Name of the system group about which to display information.<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name of the system group about which to display information.<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def systemgroup_systemcmdpolicy_bindings(self) :
		ur"""systemcmdpolicy that can be bound to systemgroup.
		"""
		try :
			return self._systemgroup_systemcmdpolicy_binding
		except Exception as e:
			raise e

	@property
	def systemgroup_systemuser_bindings(self) :
		ur"""systemuser that can be bound to systemgroup.
		"""
		try :
			return self._systemgroup_systemuser_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemgroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemgroup_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.groupname is not None :
				return str(self.groupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, groupname) :
		ur""" Use this API to fetch systemgroup_binding resource.
		"""
		try :
			if type(groupname) is not list :
				obj = systemgroup_binding()
				obj.groupname = groupname
				response = obj.get_resource(service)
			else :
				if groupname and len(groupname) > 0 :
					obj = [systemgroup_binding() for _ in range(len(groupname))]
					for i in range(len(groupname)) :
						obj[i].groupname = groupname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class systemgroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.systemgroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemgroup_binding = [systemgroup_binding() for _ in range(length)]

