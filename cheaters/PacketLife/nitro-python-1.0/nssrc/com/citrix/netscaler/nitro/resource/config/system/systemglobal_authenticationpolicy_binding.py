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

class systemglobal_authenticationpolicy_binding(base_resource) :
	""" Binding class showing the authenticationpolicy that can be bound to systemglobal.
	"""
	def __init__(self) :
		self._policyname = ""
		self._priority = 0
		self._builtin = []
		self.___count = 0

	@property
	def priority(self) :
		ur"""The priority of the command policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""The priority of the command policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@builtin.setter
	def builtin(self, builtin) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE
		"""
		try :
			self._builtin = builtin
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""The name of the  command policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""The name of the  command policy.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemglobal_authenticationpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemglobal_authenticationpolicy_binding
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
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = systemglobal_authenticationpolicy_binding()
				updateresource.policyname = resource.policyname
				updateresource.priority = resource.priority
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [systemglobal_authenticationpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].priority = resource[i].priority
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = systemglobal_authenticationpolicy_binding()
				deleteresource.policyname = resource.policyname
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [systemglobal_authenticationpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].policyname = resource[i].policyname
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		ur""" Use this API to fetch a systemglobal_authenticationpolicy_binding resources.
		"""
		try :
			obj = systemglobal_authenticationpolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		ur""" Use this API to fetch filtered set of systemglobal_authenticationpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemglobal_authenticationpolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		ur""" Use this API to count systemglobal_authenticationpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = systemglobal_authenticationpolicy_binding()
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, filter_) :
		ur""" Use this API to count the filtered set of systemglobal_authenticationpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemglobal_authenticationpolicy_binding()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

class systemglobal_authenticationpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.systemglobal_authenticationpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemglobal_authenticationpolicy_binding = [systemglobal_authenticationpolicy_binding() for _ in range(length)]

