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

class filteraction(base_resource) :
	""" Configuration for filter action resource. """
	def __init__(self) :
		self._name = ""
		self._qual = ""
		self._servicename = ""
		self._value = ""
		self._respcode = 0
		self._page = ""
		self._isdefault = False
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the filtering action. Must begin with a letter, number, or the underscore character (_). Other characters allowed, after the first character, are the hyphen (-), period (.) hash (#), space ( ), at sign (@), equals (=), and colon (:) characters. Choose a name that helps identify the type of action. The name of a filter action cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the filtering action. Must begin with a letter, number, or the underscore character (_). Other characters allowed, after the first character, are the hyphen (-), period (.) hash (#), space ( ), at sign (@), equals (=), and colon (:) characters. Choose a name that helps identify the type of action. The name of a filter action cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def qual(self) :
		ur"""Qualifier, which is the action to be performed. The qualifier cannot be changed after it is set. The available options function as follows:
		ADD - Adds the specified HTTP header.
		RESET - Terminates the connection, sending the appropriate termination notice to the user's browser.
		FORWARD - Redirects the request to the designated service. You must specify either a service name or a page, but not both.
		DROP - Silently deletes the request, without sending a response to the user's browser. 
		CORRUPT - Modifies the designated HTTP header to prevent it from performing the function it was intended to perform, then sends the request/response to the server/browser.
		ERRORCODE. Returns the designated HTTP error code to the user's browser (for example, 404, the standard HTTP code for a non-existent Web page).<br/>Possible values = reset, add, corrupt, forward, errorcode, drop.
		"""
		try :
			return self._qual
		except Exception as e:
			raise e

	@qual.setter
	def qual(self, qual) :
		ur"""Qualifier, which is the action to be performed. The qualifier cannot be changed after it is set. The available options function as follows:
		ADD - Adds the specified HTTP header.
		RESET - Terminates the connection, sending the appropriate termination notice to the user's browser.
		FORWARD - Redirects the request to the designated service. You must specify either a service name or a page, but not both.
		DROP - Silently deletes the request, without sending a response to the user's browser. 
		CORRUPT - Modifies the designated HTTP header to prevent it from performing the function it was intended to perform, then sends the request/response to the server/browser.
		ERRORCODE. Returns the designated HTTP error code to the user's browser (for example, 404, the standard HTTP code for a non-existent Web page).<br/>Possible values = reset, add, corrupt, forward, errorcode, drop
		"""
		try :
			self._qual = qual
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""Service to which to forward HTTP requests. Required if the qualifier is FORWARD.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""Service to which to forward HTTP requests. Required if the qualifier is FORWARD.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def value(self) :
		ur"""String containing the header_name and header_value. If the qualifier is ADD, specify <header_name>:<header_value>. If the qualifier is CORRUPT, specify only the header_name.<br/>Minimum length =  1.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@value.setter
	def value(self, value) :
		ur"""String containing the header_name and header_value. If the qualifier is ADD, specify <header_name>:<header_value>. If the qualifier is CORRUPT, specify only the header_name.<br/>Minimum length =  1
		"""
		try :
			self._value = value
		except Exception as e:
			raise e

	@property
	def respcode(self) :
		ur"""Response code to be returned for HTTP requests (for use with the ERRORCODE qualifier).<br/>Minimum length =  1.
		"""
		try :
			return self._respcode
		except Exception as e:
			raise e

	@respcode.setter
	def respcode(self, respcode) :
		ur"""Response code to be returned for HTTP requests (for use with the ERRORCODE qualifier).<br/>Minimum length =  1
		"""
		try :
			self._respcode = respcode
		except Exception as e:
			raise e

	@property
	def page(self) :
		ur"""HTML page to return for HTTP requests (For use with the ERRORCODE qualifier).<br/>Minimum length =  1.
		"""
		try :
			return self._page
		except Exception as e:
			raise e

	@page.setter
	def page(self, page) :
		ur"""HTML page to return for HTTP requests (For use with the ERRORCODE qualifier).<br/>Minimum length =  1
		"""
		try :
			self._page = page
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		ur"""A value of true is returned if it is a default filteraction.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur""".<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(filteraction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filteraction
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
		ur""" Use this API to add filteraction.
		"""
		try :
			if type(resource) is not list :
				addresource = filteraction()
				addresource.name = resource.name
				addresource.qual = resource.qual
				addresource.servicename = resource.servicename
				addresource.value = resource.value
				addresource.respcode = resource.respcode
				addresource.page = resource.page
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ filteraction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].qual = resource[i].qual
						addresources[i].servicename = resource[i].servicename
						addresources[i].value = resource[i].value
						addresources[i].respcode = resource[i].respcode
						addresources[i].page = resource[i].page
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete filteraction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = filteraction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ filteraction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ filteraction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update filteraction.
		"""
		try :
			if type(resource) is not list :
				updateresource = filteraction()
				updateresource.name = resource.name
				updateresource.servicename = resource.servicename
				updateresource.value = resource.value
				updateresource.respcode = resource.respcode
				updateresource.page = resource.page
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ filteraction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].servicename = resource[i].servicename
						updateresources[i].value = resource[i].value
						updateresources[i].respcode = resource[i].respcode
						updateresources[i].page = resource[i].page
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of filteraction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = filteraction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ filteraction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ filteraction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the filteraction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = filteraction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = filteraction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [filteraction() for _ in range(len(name))]
							obj = [filteraction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = filteraction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of filteraction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = filteraction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the filteraction resources configured on NetScaler.
		"""
		try :
			obj = filteraction()
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
		ur""" Use this API to count filtered the set of filteraction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = filteraction()
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

	class Qual:
		reset = "reset"
		Add = "add"
		corrupt = "corrupt"
		forward = "forward"
		errorcode = "errorcode"
		drop = "drop"

class filteraction_response(base_response) :
	def __init__(self, length=1) :
		self.filteraction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.filteraction = [filteraction() for _ in range(length)]

