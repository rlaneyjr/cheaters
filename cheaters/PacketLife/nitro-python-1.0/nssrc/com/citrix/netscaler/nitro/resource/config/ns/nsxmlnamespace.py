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

class nsxmlnamespace(base_resource) :
	""" Configuration for XML namespace resource. """
	def __init__(self) :
		self._prefix = ""
		self._Namespace = ""
		self._description = ""
		self.___count = 0

	@property
	def prefix(self) :
		ur"""XML prefix.<br/>Minimum length =  1.
		"""
		try :
			return self._prefix
		except Exception as e:
			raise e

	@prefix.setter
	def prefix(self, prefix) :
		ur"""XML prefix.<br/>Minimum length =  1
		"""
		try :
			self._prefix = prefix
		except Exception as e:
			raise e

	@property
	def Namespace(self) :
		ur"""Expanded namespace for which the XML prefix is provided.<br/>Minimum length =  1.
		"""
		try :
			return self._Namespace
		except Exception as e:
			raise e

	@Namespace.setter
	def Namespace(self, Namespace) :
		ur"""Expanded namespace for which the XML prefix is provided.<br/>Minimum length =  1
		"""
		try :
			self._Namespace = Namespace
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Description for the prefix.<br/>Minimum length =  1.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@description.setter
	def description(self, description) :
		ur"""Description for the prefix.<br/>Minimum length =  1
		"""
		try :
			self._description = description
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsxmlnamespace_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsxmlnamespace
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.prefix is not None :
				return str(self.prefix)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add nsxmlnamespace.
		"""
		try :
			if type(resource) is not list :
				addresource = nsxmlnamespace()
				addresource.prefix = resource.prefix
				addresource.Namespace = resource.Namespace
				addresource.description = resource.description
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsxmlnamespace() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].prefix = resource[i].prefix
						addresources[i].Namespace = resource[i].Namespace
						addresources[i].description = resource[i].description
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nsxmlnamespace.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsxmlnamespace()
				if type(resource) !=  type(deleteresource):
					deleteresource.prefix = resource
				else :
					deleteresource.prefix = resource.prefix
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsxmlnamespace() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].prefix = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsxmlnamespace() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].prefix = resource[i].prefix
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nsxmlnamespace.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsxmlnamespace()
				updateresource.prefix = resource.prefix
				updateresource.Namespace = resource.Namespace
				updateresource.description = resource.description
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsxmlnamespace() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].prefix = resource[i].prefix
						updateresources[i].Namespace = resource[i].Namespace
						updateresources[i].description = resource[i].description
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nsxmlnamespace resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsxmlnamespace()
				if type(resource) !=  type(unsetresource):
					unsetresource.prefix = resource
				else :
					unsetresource.prefix = resource.prefix
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsxmlnamespace() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].prefix = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsxmlnamespace() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].prefix = resource[i].prefix
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsxmlnamespace resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsxmlnamespace()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nsxmlnamespace()
						obj.prefix = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nsxmlnamespace() for _ in range(len(name))]
							obj = [nsxmlnamespace() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nsxmlnamespace()
								obj[i].prefix = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nsxmlnamespace resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsxmlnamespace()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nsxmlnamespace resources configured on NetScaler.
		"""
		try :
			obj = nsxmlnamespace()
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
		ur""" Use this API to count filtered the set of nsxmlnamespace resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsxmlnamespace()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nsxmlnamespace_response(base_response) :
	def __init__(self, length=1) :
		self.nsxmlnamespace = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsxmlnamespace = [nsxmlnamespace() for _ in range(length)]

