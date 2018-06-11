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

class appfwfieldtype(base_resource) :
	""" Configuration for application firewall form field type resource. """
	def __init__(self) :
		self._name = ""
		self._regex = ""
		self._priority = 0
		self._comment = ""
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the field type.
		Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at \(\@\), equals \(=\), colon \(:\), and underscore characters. Cannot be changed after the field type is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my field type" or 'my field type'\).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the field type.
		Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at \(\@\), equals \(=\), colon \(:\), and underscore characters. Cannot be changed after the field type is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my field type" or 'my field type'\).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def regex(self) :
		ur"""PCRE - format regular expression defining the characters and length allowed for this field type.<br/>Minimum length =  1.
		"""
		try :
			return self._regex
		except Exception as e:
			raise e

	@regex.setter
	def regex(self, regex) :
		ur"""PCRE - format regular expression defining the characters and length allowed for this field type.<br/>Minimum length =  1
		"""
		try :
			self._regex = regex
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Positive integer specifying the priority of the field type. A lower number specified a higher priority. Field types are checked in the order of their priority numbers.<br/>Maximum length =  64000.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Positive integer specifying the priority of the field type. A lower number specified a higher priority. Field types are checked in the order of their priority numbers.<br/>Maximum length =  64000
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Comment describing the type of field that this field type is intended to match.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Comment describing the type of field that this field type is intended to match.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine if fieldtype is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwfieldtype_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwfieldtype
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
		ur""" Use this API to add appfwfieldtype.
		"""
		try :
			if type(resource) is not list :
				addresource = appfwfieldtype()
				addresource.name = resource.name
				addresource.regex = resource.regex
				addresource.priority = resource.priority
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ appfwfieldtype() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].regex = resource[i].regex
						addresources[i].priority = resource[i].priority
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete appfwfieldtype.
		"""
		try :
			if type(resource) is not list :
				deleteresource = appfwfieldtype()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwfieldtype() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwfieldtype() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update appfwfieldtype.
		"""
		try :
			if type(resource) is not list :
				updateresource = appfwfieldtype()
				updateresource.name = resource.name
				updateresource.regex = resource.regex
				updateresource.priority = resource.priority
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ appfwfieldtype() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].regex = resource[i].regex
						updateresources[i].priority = resource[i].priority
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the appfwfieldtype resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwfieldtype()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = appfwfieldtype()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [appfwfieldtype() for _ in range(len(name))]
							obj = [appfwfieldtype() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = appfwfieldtype()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of appfwfieldtype resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwfieldtype()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the appfwfieldtype resources configured on NetScaler.
		"""
		try :
			obj = appfwfieldtype()
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
		ur""" Use this API to count filtered the set of appfwfieldtype resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwfieldtype()
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

class appfwfieldtype_response(base_response) :
	def __init__(self, length=1) :
		self.appfwfieldtype = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwfieldtype = [appfwfieldtype() for _ in range(length)]

