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

class transformaction(base_resource) :
	""" Configuration for transform action resource. """
	def __init__(self) :
		self._name = ""
		self._profilename = ""
		self._priority = 0
		self._state = ""
		self._requrlfrom = ""
		self._requrlinto = ""
		self._resurlfrom = ""
		self._resurlinto = ""
		self._cookiedomainfrom = ""
		self._cookiedomaininto = ""
		self._comment = ""
		self._continuematching = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the URL transformation action.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the URL Transformation action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, ^A"my transform action^A" or ^A'my transform action).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the URL transformation action.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the URL Transformation action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, ^A"my transform action^A" or ^A'my transform action).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def profilename(self) :
		ur"""Name of the URL Transformation profile with which to associate this action.<br/>Minimum length =  1.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@profilename.setter
	def profilename(self, profilename) :
		ur"""Name of the URL Transformation profile with which to associate this action.<br/>Minimum length =  1
		"""
		try :
			self._profilename = profilename
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Positive integer specifying the priority of the action within the profile. A lower number specifies a higher priority. Must be unique within the list of actions bound to the profile. Policies are evaluated in the order of their priority numbers, and the first policy that matches is applied.<br/>Minimum length =  1<br/>Maximum length =  2147483647.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Positive integer specifying the priority of the action within the profile. A lower number specifies a higher priority. Must be unique within the list of actions bound to the profile. Policies are evaluated in the order of their priority numbers, and the first policy that matches is applied.<br/>Minimum length =  1<br/>Maximum length =  2147483647
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Enable or disable this action.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Enable or disable this action.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def requrlfrom(self) :
		ur"""PCRE-format regular expression that describes the request URL pattern to be transformed.<br/>Minimum length =  1.
		"""
		try :
			return self._requrlfrom
		except Exception as e:
			raise e

	@requrlfrom.setter
	def requrlfrom(self, requrlfrom) :
		ur"""PCRE-format regular expression that describes the request URL pattern to be transformed.<br/>Minimum length =  1
		"""
		try :
			self._requrlfrom = requrlfrom
		except Exception as e:
			raise e

	@property
	def requrlinto(self) :
		ur"""PCRE-format regular expression that describes the transformation to be performed on URLs that match the reqUrlFrom pattern.<br/>Minimum length =  1.
		"""
		try :
			return self._requrlinto
		except Exception as e:
			raise e

	@requrlinto.setter
	def requrlinto(self, requrlinto) :
		ur"""PCRE-format regular expression that describes the transformation to be performed on URLs that match the reqUrlFrom pattern.<br/>Minimum length =  1
		"""
		try :
			self._requrlinto = requrlinto
		except Exception as e:
			raise e

	@property
	def resurlfrom(self) :
		ur"""PCRE-format regular expression that describes the response URL pattern to be transformed.<br/>Minimum length =  1.
		"""
		try :
			return self._resurlfrom
		except Exception as e:
			raise e

	@resurlfrom.setter
	def resurlfrom(self, resurlfrom) :
		ur"""PCRE-format regular expression that describes the response URL pattern to be transformed.<br/>Minimum length =  1
		"""
		try :
			self._resurlfrom = resurlfrom
		except Exception as e:
			raise e

	@property
	def resurlinto(self) :
		ur"""PCRE-format regular expression that describes the transformation to be performed on URLs that match the resUrlFrom pattern.<br/>Minimum length =  1.
		"""
		try :
			return self._resurlinto
		except Exception as e:
			raise e

	@resurlinto.setter
	def resurlinto(self, resurlinto) :
		ur"""PCRE-format regular expression that describes the transformation to be performed on URLs that match the resUrlFrom pattern.<br/>Minimum length =  1
		"""
		try :
			self._resurlinto = resurlinto
		except Exception as e:
			raise e

	@property
	def cookiedomainfrom(self) :
		ur"""Pattern that matches the domain to be transformed in Set-Cookie headers.<br/>Minimum length =  1.
		"""
		try :
			return self._cookiedomainfrom
		except Exception as e:
			raise e

	@cookiedomainfrom.setter
	def cookiedomainfrom(self, cookiedomainfrom) :
		ur"""Pattern that matches the domain to be transformed in Set-Cookie headers.<br/>Minimum length =  1
		"""
		try :
			self._cookiedomainfrom = cookiedomainfrom
		except Exception as e:
			raise e

	@property
	def cookiedomaininto(self) :
		ur"""PCRE-format regular expression that describes the transformation to be performed on cookie domains that match the cookieDomainFrom pattern. 
		NOTE: The cookie domain to be transformed is extracted from the request.<br/>Minimum length =  1.
		"""
		try :
			return self._cookiedomaininto
		except Exception as e:
			raise e

	@cookiedomaininto.setter
	def cookiedomaininto(self, cookiedomaininto) :
		ur"""PCRE-format regular expression that describes the transformation to be performed on cookie domains that match the cookieDomainFrom pattern. 
		NOTE: The cookie domain to be transformed is extracted from the request.<br/>Minimum length =  1
		"""
		try :
			self._cookiedomaininto = cookiedomaininto
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments to preserve information about this URL Transformation action.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments to preserve information about this URL Transformation action.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def continuematching(self) :
		ur"""Continue transforming using the next rule in the list.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._continuematching
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(transformaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.transformaction
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
		ur""" Use this API to add transformaction.
		"""
		try :
			if type(resource) is not list :
				addresource = transformaction()
				addresource.name = resource.name
				addresource.profilename = resource.profilename
				addresource.priority = resource.priority
				addresource.state = resource.state
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ transformaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].profilename = resource[i].profilename
						addresources[i].priority = resource[i].priority
						addresources[i].state = resource[i].state
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete transformaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = transformaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ transformaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ transformaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update transformaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = transformaction()
				updateresource.name = resource.name
				updateresource.priority = resource.priority
				updateresource.requrlfrom = resource.requrlfrom
				updateresource.requrlinto = resource.requrlinto
				updateresource.resurlfrom = resource.resurlfrom
				updateresource.resurlinto = resource.resurlinto
				updateresource.cookiedomainfrom = resource.cookiedomainfrom
				updateresource.cookiedomaininto = resource.cookiedomaininto
				updateresource.state = resource.state
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ transformaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].priority = resource[i].priority
						updateresources[i].requrlfrom = resource[i].requrlfrom
						updateresources[i].requrlinto = resource[i].requrlinto
						updateresources[i].resurlfrom = resource[i].resurlfrom
						updateresources[i].resurlinto = resource[i].resurlinto
						updateresources[i].cookiedomainfrom = resource[i].cookiedomainfrom
						updateresources[i].cookiedomaininto = resource[i].cookiedomaininto
						updateresources[i].state = resource[i].state
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of transformaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = transformaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ transformaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ transformaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the transformaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = transformaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = transformaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [transformaction() for _ in range(len(name))]
							obj = [transformaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = transformaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of transformaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the transformaction resources configured on NetScaler.
		"""
		try :
			obj = transformaction()
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
		ur""" Use this API to count filtered the set of transformaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Continuematching:
		ON = "ON"
		OFF = "OFF"

class transformaction_response(base_response) :
	def __init__(self, length=1) :
		self.transformaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.transformaction = [transformaction() for _ in range(length)]

