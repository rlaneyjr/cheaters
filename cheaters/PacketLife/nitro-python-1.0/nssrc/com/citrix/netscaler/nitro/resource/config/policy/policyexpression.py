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

class policyexpression(base_resource) :
	""" Configuration for expression resource. """
	def __init__(self) :
		self._name = ""
		self._value = ""
		self._description = ""
		self._comment = ""
		self._clientsecuritymessage = ""
		self._type = ""
		self._hits = 0
		self._pihits = 0
		self._type1 = ""
		self._isdefault = False
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Unique name for the expression. Not case sensitive. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Must not begin with 're' or 'xp' or be a word reserved for use as a default syntax expression qualifier prefix (such as HTTP) or enumeration value (such as ASCII). Must not be the name of an existing named expression, pattern set, dataset, stringmap, or HTTP callout.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Unique name for the expression. Not case sensitive. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Must not begin with 're' or 'xp' or be a word reserved for use as a default syntax expression qualifier prefix (such as HTTP) or enumeration value (such as ASCII). Must not be the name of an existing named expression, pattern set, dataset, stringmap, or HTTP callout.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def value(self) :
		ur"""Expression string. For example: http.req.body(100).contains("this").
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@value.setter
	def value(self, value) :
		ur"""Expression string. For example: http.req.body(100).contains("this").
		"""
		try :
			self._value = value
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Description for the expression.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@description.setter
	def description(self, description) :
		ur"""Description for the expression.
		"""
		try :
			self._description = description
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments associated with the expression. Displayed upon viewing the policy expression.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments associated with the expression. Displayed upon viewing the policy expression.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def clientsecuritymessage(self) :
		ur"""Message to display if the expression fails. Allowed for classic end-point check expressions only.<br/>Minimum length =  1.
		"""
		try :
			return self._clientsecuritymessage
		except Exception as e:
			raise e

	@clientsecuritymessage.setter
	def clientsecuritymessage(self, clientsecuritymessage) :
		ur"""Message to display if the expression fails. Allowed for classic end-point check expressions only.<br/>Minimum length =  1
		"""
		try :
			self._clientsecuritymessage = clientsecuritymessage
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of expression. Can be a classic or default syntax (advanced) expression.<br/>Possible values = CLASSIC, ADVANCED.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of expression. Can be a classic or default syntax (advanced) expression.<br/>Possible values = CLASSIC, ADVANCED
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The total number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def pihits(self) :
		ur"""The total number of hits.
		"""
		try :
			return self._pihits
		except Exception as e:
			raise e

	@property
	def type1(self) :
		ur"""The type of expression. This is for output only.<br/>Possible values = CLASSIC, ADVANCED.
		"""
		try :
			return self._type1
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		ur"""A value of true is returned if it is a default policy expression.
		"""
		try :
			return self._isdefault
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

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policyexpression_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policyexpression
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
		ur""" Use this API to add policyexpression.
		"""
		try :
			if type(resource) is not list :
				addresource = policyexpression()
				addresource.name = resource.name
				addresource.value = resource.value
				addresource.description = resource.description
				addresource.comment = resource.comment
				addresource.clientsecuritymessage = resource.clientsecuritymessage
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ policyexpression() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].value = resource[i].value
						addresources[i].description = resource[i].description
						addresources[i].comment = resource[i].comment
						addresources[i].clientsecuritymessage = resource[i].clientsecuritymessage
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete policyexpression.
		"""
		try :
			if type(resource) is not list :
				deleteresource = policyexpression()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ policyexpression() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ policyexpression() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update policyexpression.
		"""
		try :
			if type(resource) is not list :
				updateresource = policyexpression()
				updateresource.name = resource.name
				updateresource.value = resource.value
				updateresource.description = resource.description
				updateresource.comment = resource.comment
				updateresource.clientsecuritymessage = resource.clientsecuritymessage
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ policyexpression() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].value = resource[i].value
						updateresources[i].description = resource[i].description
						updateresources[i].comment = resource[i].comment
						updateresources[i].clientsecuritymessage = resource[i].clientsecuritymessage
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of policyexpression resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = policyexpression()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ policyexpression() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ policyexpression() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the policyexpression resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = policyexpression()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = policyexpression()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [policyexpression() for _ in range(len(name))]
							obj = [policyexpression() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = policyexpression()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the policyexpression resources that are configured on netscaler.
	# This uses policyexpression_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = policyexpression()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of policyexpression resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policyexpression()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the policyexpression resources configured on NetScaler.
		"""
		try :
			obj = policyexpression()
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
		ur""" Use this API to count filtered the set of policyexpression resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policyexpression()
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
		CLASSIC = "CLASSIC"
		ADVANCED = "ADVANCED"

	class Type1:
		CLASSIC = "CLASSIC"
		ADVANCED = "ADVANCED"

class policyexpression_response(base_response) :
	def __init__(self, length=1) :
		self.policyexpression = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policyexpression = [policyexpression() for _ in range(length)]

