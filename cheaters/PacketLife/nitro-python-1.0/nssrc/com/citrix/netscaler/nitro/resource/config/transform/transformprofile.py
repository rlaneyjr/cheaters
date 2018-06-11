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

class transformprofile(base_resource) :
	""" Configuration for URL Transformation profile resource. """
	def __init__(self) :
		self._name = ""
		self._type = ""
		self._onlytransformabsurlinbody = ""
		self._comment = ""
		self._regexforfindingurlinjavascript = ""
		self._regexforfindingurlincss = ""
		self._regexforfindingurlinxcomponent = ""
		self._regexforfindingurlinxml = ""
		self._additionalreqheaderslist = ""
		self._additionalrespheaderslist = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the URL transformation profile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the URL transformation profile is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, ^A"my transform profile^A" or ^A'my transform profile^A').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the URL transformation profile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the URL transformation profile is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, ^A"my transform profile^A" or ^A'my transform profile^A').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of transformation. Always URL for URL Transformation profiles.<br/>Possible values = URL.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of transformation. Always URL for URL Transformation profiles.<br/>Possible values = URL
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def onlytransformabsurlinbody(self) :
		ur"""In the HTTP body, transform only absolute URLs. Relative URLs are ignored.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._onlytransformabsurlinbody
		except Exception as e:
			raise e

	@onlytransformabsurlinbody.setter
	def onlytransformabsurlinbody(self, onlytransformabsurlinbody) :
		ur"""In the HTTP body, transform only absolute URLs. Relative URLs are ignored.<br/>Possible values = ON, OFF
		"""
		try :
			self._onlytransformabsurlinbody = onlytransformabsurlinbody
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments to preserve information about this URL Transformation profile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments to preserve information about this URL Transformation profile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def regexforfindingurlinjavascript(self) :
		ur"""Patclass having regexes to find the URLs in JavaScript.
		"""
		try :
			return self._regexforfindingurlinjavascript
		except Exception as e:
			raise e

	@property
	def regexforfindingurlincss(self) :
		ur"""Patclass having regexes to find the URLs in CSS.
		"""
		try :
			return self._regexforfindingurlincss
		except Exception as e:
			raise e

	@property
	def regexforfindingurlinxcomponent(self) :
		ur"""Patclass having regexes to find the URLs in X-Component.
		"""
		try :
			return self._regexforfindingurlinxcomponent
		except Exception as e:
			raise e

	@property
	def regexforfindingurlinxml(self) :
		ur"""Patclass having regexes to find the URLs in XML.
		"""
		try :
			return self._regexforfindingurlinxml
		except Exception as e:
			raise e

	@property
	def additionalreqheaderslist(self) :
		ur"""Patclass having a list of additional request header names that should transformed.
		"""
		try :
			return self._additionalreqheaderslist
		except Exception as e:
			raise e

	@property
	def additionalrespheaderslist(self) :
		ur"""Patclass having a list of additional response header names that should transformed.
		"""
		try :
			return self._additionalrespheaderslist
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(transformprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.transformprofile
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
		ur""" Use this API to add transformprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = transformprofile()
				addresource.name = resource.name
				addresource.type = resource.type
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ transformprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].type = resource[i].type
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete transformprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = transformprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ transformprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ transformprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update transformprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = transformprofile()
				updateresource.name = resource.name
				updateresource.type = resource.type
				updateresource.onlytransformabsurlinbody = resource.onlytransformabsurlinbody
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ transformprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].type = resource[i].type
						updateresources[i].onlytransformabsurlinbody = resource[i].onlytransformabsurlinbody
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of transformprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = transformprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ transformprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ transformprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the transformprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = transformprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = transformprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [transformprofile() for _ in range(len(name))]
							obj = [transformprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = transformprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of transformprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the transformprofile resources configured on NetScaler.
		"""
		try :
			obj = transformprofile()
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
		ur""" Use this API to count filtered the set of transformprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Onlytransformabsurlinbody:
		ON = "ON"
		OFF = "OFF"

	class Type:
		URL = "URL"

class transformprofile_response(base_response) :
	def __init__(self, length=1) :
		self.transformprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.transformprofile = [transformprofile() for _ in range(length)]

