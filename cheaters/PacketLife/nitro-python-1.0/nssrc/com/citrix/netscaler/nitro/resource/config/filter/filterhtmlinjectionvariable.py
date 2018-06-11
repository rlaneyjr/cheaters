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

class filterhtmlinjectionvariable(base_resource) :
	""" Configuration for HTML injection variable resource. """
	def __init__(self) :
		self._variable = ""
		self._value = ""
		self._builtin = []
		self._type = ""
		self.___count = 0

	@property
	def variable(self) :
		ur"""Name for the HTML injection variable to be added.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._variable
		except Exception as e:
			raise e

	@variable.setter
	def variable(self, variable) :
		ur"""Name for the HTML injection variable to be added.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._variable = variable
		except Exception as e:
			raise e

	@property
	def value(self) :
		ur"""Value to be assigned to the new variable.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@value.setter
	def value(self, value) :
		ur"""Value to be assigned to the new variable.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._value = value
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

	@property
	def type(self) :
		ur"""Type of the HTML injection variable.<br/>Possible values = System internal, User defined.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(filterhtmlinjectionvariable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filterhtmlinjectionvariable
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.variable is not None :
				return str(self.variable)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add filterhtmlinjectionvariable.
		"""
		try :
			if type(resource) is not list :
				addresource = filterhtmlinjectionvariable()
				addresource.variable = resource.variable
				addresource.value = resource.value
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ filterhtmlinjectionvariable() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].variable = resource[i].variable
						addresources[i].value = resource[i].value
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete filterhtmlinjectionvariable.
		"""
		try :
			if type(resource) is not list :
				deleteresource = filterhtmlinjectionvariable()
				if type(resource) !=  type(deleteresource):
					deleteresource.variable = resource
				else :
					deleteresource.variable = resource.variable
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ filterhtmlinjectionvariable() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].variable = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ filterhtmlinjectionvariable() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].variable = resource[i].variable
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update filterhtmlinjectionvariable.
		"""
		try :
			if type(resource) is not list :
				updateresource = filterhtmlinjectionvariable()
				updateresource.variable = resource.variable
				updateresource.value = resource.value
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ filterhtmlinjectionvariable() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].variable = resource[i].variable
						updateresources[i].value = resource[i].value
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of filterhtmlinjectionvariable resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = filterhtmlinjectionvariable()
				if type(resource) !=  type(unsetresource):
					unsetresource.variable = resource
				else :
					unsetresource.variable = resource.variable
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ filterhtmlinjectionvariable() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].variable = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ filterhtmlinjectionvariable() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].variable = resource[i].variable
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the filterhtmlinjectionvariable resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = filterhtmlinjectionvariable()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = filterhtmlinjectionvariable()
						obj.variable = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [filterhtmlinjectionvariable() for _ in range(len(name))]
							obj = [filterhtmlinjectionvariable() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = filterhtmlinjectionvariable()
								obj[i].variable = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of filterhtmlinjectionvariable resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = filterhtmlinjectionvariable()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the filterhtmlinjectionvariable resources configured on NetScaler.
		"""
		try :
			obj = filterhtmlinjectionvariable()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of filterhtmlinjectionvariable resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = filterhtmlinjectionvariable()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

	class Type:
		System_internal = "System internal"
		User_defined = "User defined"

class filterhtmlinjectionvariable_response(base_response) :
	def __init__(self, length=1) :
		self.filterhtmlinjectionvariable = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.filterhtmlinjectionvariable = [filterhtmlinjectionvariable() for _ in range(length)]

