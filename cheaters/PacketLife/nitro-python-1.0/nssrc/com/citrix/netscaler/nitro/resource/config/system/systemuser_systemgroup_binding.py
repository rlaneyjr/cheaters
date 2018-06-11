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

class systemuser_systemgroup_binding(base_resource) :
	""" Binding class showing the systemgroup that can be bound to systemuser.
	"""
	def __init__(self) :
		self._groupname = ""
		self._username = ""
		self._policyname = ""
		self._priority = 0
		self.___count = 0

	@property
	def priority(self) :
		ur"""Integer specifying the priority of the command policy. A lower number specifies a higher priority. Policies are evaluated in the order of their priority numbers.<br/>Minimum value =  0<br/>Maximum value =  999999999.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Integer specifying the priority of the command policy. A lower number specifies a higher priority. Policies are evaluated in the order of their priority numbers.<br/>Minimum value =  0<br/>Maximum value =  999999999
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""Name of the command policy to bind to the system user.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name of the command policy to bind to the system user.<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def username(self) :
		ur"""Name of the system-user entry to which to bind the command policy.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Name of the system-user entry to which to bind the command policy.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		ur"""The system group. .
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""The system group. .
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemuser_systemgroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemuser_systemgroup_binding
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
	def get(cls, service, username) :
		ur""" Use this API to fetch systemuser_systemgroup_binding resources.
		"""
		try :
			obj = systemuser_systemgroup_binding()
			obj.username = username
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, username, filter_) :
		ur""" Use this API to fetch filtered set of systemuser_systemgroup_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemuser_systemgroup_binding()
			obj.username = username
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, username) :
		ur""" Use this API to count systemuser_systemgroup_binding resources configued on NetScaler.
		"""
		try :
			obj = systemuser_systemgroup_binding()
			obj.username = username
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, username, filter_) :
		ur""" Use this API to count the filtered set of systemuser_systemgroup_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemuser_systemgroup_binding()
			obj.username = username
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class systemuser_systemgroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.systemuser_systemgroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemuser_systemgroup_binding = [systemuser_systemgroup_binding() for _ in range(length)]

