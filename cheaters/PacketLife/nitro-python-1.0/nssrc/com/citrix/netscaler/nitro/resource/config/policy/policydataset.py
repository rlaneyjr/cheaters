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

class policydataset(base_resource) :
	""" Configuration for TYPE set resource. """
	def __init__(self) :
		self._name = ""
		self._type = ""
		self._indextype = ""
		self._comment = ""
		self._description = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the dataset. Must not exceed 127 characters.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the dataset. Must not exceed 127 characters.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of value to bind to the dataset.<br/>Possible values = ipv4, number, ipv6, ulong, double, mac.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of value to bind to the dataset.<br/>Possible values = ipv4, number, ipv6, ulong, double, mac
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def indextype(self) :
		ur"""Index type.<br/>Possible values = Auto-generated, User-defined.
		"""
		try :
			return self._indextype
		except Exception as e:
			raise e

	@indextype.setter
	def indextype(self, indextype) :
		ur"""Index type.<br/>Possible values = Auto-generated, User-defined
		"""
		try :
			self._indextype = indextype
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments to preserve information about this dataset.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments to preserve information about this dataset.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Description of the set.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policydataset_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policydataset
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
		ur""" Use this API to add policydataset.
		"""
		try :
			if type(resource) is not list :
				addresource = policydataset()
				addresource.name = resource.name
				addresource.type = resource.type
				addresource.indextype = resource.indextype
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ policydataset() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].type = resource[i].type
						addresources[i].indextype = resource[i].indextype
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete policydataset.
		"""
		try :
			if type(resource) is not list :
				deleteresource = policydataset()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ policydataset() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ policydataset() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the policydataset resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = policydataset()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = policydataset()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [policydataset() for _ in range(len(name))]
							obj = [policydataset() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = policydataset()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of policydataset resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policydataset()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the policydataset resources configured on NetScaler.
		"""
		try :
			obj = policydataset()
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
		ur""" Use this API to count filtered the set of policydataset resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policydataset()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		ipv4 = "ipv4"
		number = "number"
		ipv6 = "ipv6"
		Ulong = "ulong"
		Double = "double"
		mac = "mac"

	class Indextype:
		Auto_generated = "Auto-generated"
		User_defined = "User-defined"

class policydataset_response(base_response) :
	def __init__(self, length=1) :
		self.policydataset = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policydataset = [policydataset() for _ in range(length)]

