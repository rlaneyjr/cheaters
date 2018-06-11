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

class policypatset_pattern_binding(base_resource) :
	""" Binding class showing the pattern that can be bound to policypatset.
	"""
	def __init__(self) :
		self._String = ""
		self._index = 0
		self._charset = ""
		self._builtin = []
		self._name = ""
		self.___count = 0

	@property
	def String(self) :
		ur"""String of characters that constitutes a pattern. For more information about the characters that can be used, refer to the character set parameter.
		Note: Minimum length for pattern sets used in rewrite actions of type REPLACE_ALL, DELETE_ALL, INSERT_AFTER_ALL, and INSERT_BEFORE_ALL, is three characters.
		"""
		try :
			return self._String
		except Exception as e:
			raise e

	@String.setter
	def String(self, String) :
		ur"""String of characters that constitutes a pattern. For more information about the characters that can be used, refer to the character set parameter.
		Note: Minimum length for pattern sets used in rewrite actions of type REPLACE_ALL, DELETE_ALL, INSERT_AFTER_ALL, and INSERT_BEFORE_ALL, is three characters.
		"""
		try :
			self._String = String
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
	def name(self) :
		ur"""Name of the pattern set to which to bind the string.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the pattern set to which to bind the string.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def charset(self) :
		ur"""Character set associated with the characters in the string.
		Note: UTF-8 characters can be entered directly (if the UI supports it) or can be encoded as a sequence of hexadecimal bytes '\xNN'. For example, the UTF-8 character 'ue' can be encoded as '\xC3\xBC'.<br/>Possible values = ASCII, UTF_8.
		"""
		try :
			return self._charset
		except Exception as e:
			raise e

	@charset.setter
	def charset(self, charset) :
		ur"""Character set associated with the characters in the string.
		Note: UTF-8 characters can be entered directly (if the UI supports it) or can be encoded as a sequence of hexadecimal bytes '\xNN'. For example, the UTF-8 character 'ue' can be encoded as '\xC3\xBC'.<br/>Possible values = ASCII, UTF_8
		"""
		try :
			self._charset = charset
		except Exception as e:
			raise e

	@property
	def index(self) :
		ur"""The index of the string associated with the patset.
		"""
		try :
			return self._index
		except Exception as e:
			raise e

	@index.setter
	def index(self, index) :
		ur"""The index of the string associated with the patset.
		"""
		try :
			self._index = index
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policypatset_pattern_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policypatset_pattern_binding
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
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = policypatset_pattern_binding()
				updateresource.name = resource.name
				updateresource.String = resource.String
				updateresource.index = resource.index
				updateresource.charset = resource.charset
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [policypatset_pattern_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].String = resource[i].String
						updateresources[i].index = resource[i].index
						updateresources[i].charset = resource[i].charset
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = policypatset_pattern_binding()
				deleteresource.name = resource.name
				deleteresource.String = resource.String
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [policypatset_pattern_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].String = resource[i].String
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch policypatset_pattern_binding resources.
		"""
		try :
			obj = policypatset_pattern_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of policypatset_pattern_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policypatset_pattern_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count policypatset_pattern_binding resources configued on NetScaler.
		"""
		try :
			obj = policypatset_pattern_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of policypatset_pattern_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policypatset_pattern_binding()
			obj.name = name
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

	class Charset:
		ASCII = "ASCII"
		UTF_8 = "UTF_8"

class policypatset_pattern_binding_response(base_response) :
	def __init__(self, length=1) :
		self.policypatset_pattern_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policypatset_pattern_binding = [policypatset_pattern_binding() for _ in range(length)]

