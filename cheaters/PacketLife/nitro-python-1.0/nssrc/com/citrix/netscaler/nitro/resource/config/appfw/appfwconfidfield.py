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

class appfwconfidfield(base_resource) :
	""" Configuration for configured confidential form fields resource. """
	def __init__(self) :
		self._fieldname = ""
		self._url = ""
		self._isregex = ""
		self._comment = ""
		self._state = ""
		self.___count = 0

	@property
	def fieldname(self) :
		ur"""Name of the form field to designate as confidential.<br/>Minimum length =  1.
		"""
		try :
			return self._fieldname
		except Exception as e:
			raise e

	@fieldname.setter
	def fieldname(self, fieldname) :
		ur"""Name of the form field to designate as confidential.<br/>Minimum length =  1
		"""
		try :
			self._fieldname = fieldname
		except Exception as e:
			raise e

	@property
	def url(self) :
		ur"""URL of the web page that contains the web form.<br/>Minimum length =  1.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		ur"""URL of the web page that contains the web form.<br/>Minimum length =  1
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def isregex(self) :
		ur"""Method of specifying the form field name. Available settings function as follows:
		* REGEX. Form field is a regular expression.
		* NOTREGEX. Form field is a literal string.<br/>Default value: NOTREGEX<br/>Possible values = REGEX, NOTREGEX.
		"""
		try :
			return self._isregex
		except Exception as e:
			raise e

	@isregex.setter
	def isregex(self, isregex) :
		ur"""Method of specifying the form field name. Available settings function as follows:
		* REGEX. Form field is a regular expression.
		* NOTREGEX. Form field is a literal string.<br/>Default value: NOTREGEX<br/>Possible values = REGEX, NOTREGEX
		"""
		try :
			self._isregex = isregex
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments to preserve information about the form field designation.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments to preserve information about the form field designation.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Enable or disable the confidential field designation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Enable or disable the confidential field designation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwconfidfield_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwconfidfield
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.fieldname is not None :
				return str(self.fieldname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add appfwconfidfield.
		"""
		try :
			if type(resource) is not list :
				addresource = appfwconfidfield()
				addresource.fieldname = resource.fieldname
				addresource.url = resource.url
				addresource.isregex = resource.isregex
				addresource.comment = resource.comment
				addresource.state = resource.state
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ appfwconfidfield() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].fieldname = resource[i].fieldname
						addresources[i].url = resource[i].url
						addresources[i].isregex = resource[i].isregex
						addresources[i].comment = resource[i].comment
						addresources[i].state = resource[i].state
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete appfwconfidfield.
		"""
		try :
			if type(resource) is not list :
				deleteresource = appfwconfidfield()
				if type(resource) !=  type(deleteresource):
					deleteresource.fieldname = resource
				else :
					deleteresource.fieldname = resource.fieldname
					deleteresource.url = resource.url
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwconfidfield() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].fieldname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwconfidfield() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].fieldname = resource[i].fieldname
							deleteresources[i].url = resource[i].url
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update appfwconfidfield.
		"""
		try :
			if type(resource) is not list :
				updateresource = appfwconfidfield()
				updateresource.fieldname = resource.fieldname
				updateresource.url = resource.url
				updateresource.comment = resource.comment
				updateresource.isregex = resource.isregex
				updateresource.state = resource.state
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ appfwconfidfield() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].fieldname = resource[i].fieldname
						updateresources[i].url = resource[i].url
						updateresources[i].comment = resource[i].comment
						updateresources[i].isregex = resource[i].isregex
						updateresources[i].state = resource[i].state
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of appfwconfidfield resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appfwconfidfield()
				unsetresource.fieldname = resource.fieldname
				unsetresource.url = resource.url
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) == cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ appfwconfidfield() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].fieldname = resource[i].fieldname
							unsetresources[i].url = resource[i].url
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the appfwconfidfield resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwconfidfield()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [appfwconfidfield() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of appfwconfidfield resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwconfidfield()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the appfwconfidfield resources configured on NetScaler.
		"""
		try :
			obj = appfwconfidfield()
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
		ur""" Use this API to count filtered the set of appfwconfidfield resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwconfidfield()
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

	class Isregex:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

class appfwconfidfield_response(base_response) :
	def __init__(self, length=1) :
		self.appfwconfidfield = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwconfidfield = [appfwconfidfield() for _ in range(length)]

