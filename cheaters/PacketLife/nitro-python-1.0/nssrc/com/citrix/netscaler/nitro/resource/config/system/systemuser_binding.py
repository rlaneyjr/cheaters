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

class systemuser_binding(base_resource):
	""" Binding class showing the resources that can be bound to systemuser_binding. 
	"""
	def __init__(self) :
		self._username = ""
		self.systemuser_systemgroup_binding = []
		self.systemuser_systemcmdpolicy_binding = []

	@property
	def username(self) :
		ur"""Name of a system user about whom to display information.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Name of a system user about whom to display information.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def systemuser_systemgroup_bindings(self) :
		ur"""systemgroup that can be bound to systemuser.
		"""
		try :
			return self._systemuser_systemgroup_binding
		except Exception as e:
			raise e

	@property
	def systemuser_systemcmdpolicy_bindings(self) :
		ur"""systemcmdpolicy that can be bound to systemuser.
		"""
		try :
			return self._systemuser_systemcmdpolicy_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemuser_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemuser_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.username is not None :
				return str(self.username)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, username) :
		ur""" Use this API to fetch systemuser_binding resource.
		"""
		try :
			if type(username) is not list :
				obj = systemuser_binding()
				obj.username = username
				response = obj.get_resource(service)
			else :
				if username and len(username) > 0 :
					obj = [systemuser_binding() for _ in range(len(username))]
					for i in range(len(username)) :
						obj[i].username = username[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class systemuser_binding_response(base_response) :
	def __init__(self, length=1) :
		self.systemuser_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemuser_binding = [systemuser_binding() for _ in range(length)]

