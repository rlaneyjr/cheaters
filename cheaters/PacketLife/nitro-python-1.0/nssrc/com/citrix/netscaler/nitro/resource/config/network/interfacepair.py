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

class interfacepair(base_resource) :
	""" Configuration for "Interface Pair" resource. """
	def __init__(self) :
		self._id = 0
		self._ifnum = []
		self._ifaces = ""
		self.___count = 0

	@property
	def id(self) :
		ur"""The Interface pair id.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""The Interface pair id.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		ur"""The constituent interfaces in the interface pair.<br/>Minimum length =  1.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		ur"""The constituent interfaces in the interface pair.<br/>Minimum length =  1
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def ifaces(self) :
		ur"""Names of all member interfaces of this Interface Pair.
		"""
		try :
			return self._ifaces
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(interfacepair_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.interfacepair
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add interfacepair.
		"""
		try :
			if type(resource) is not list :
				addresource = interfacepair()
				addresource.id = resource.id
				addresource.ifnum = resource.ifnum
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ interfacepair() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].id = resource[i].id
						addresources[i].ifnum = resource[i].ifnum
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete interfacepair.
		"""
		try :
			if type(resource) is not list :
				deleteresource = interfacepair()
				if type(resource) !=  type(deleteresource):
					deleteresource.id = resource
				else :
					deleteresource.id = resource.id
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ interfacepair() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ interfacepair() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i].id
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the interfacepair resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = interfacepair()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = interfacepair()
						obj.id = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [interfacepair() for _ in range(len(name))]
							obj = [interfacepair() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = interfacepair()
								obj[i].id = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of interfacepair resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = interfacepair()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the interfacepair resources configured on NetScaler.
		"""
		try :
			obj = interfacepair()
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
		ur""" Use this API to count filtered the set of interfacepair resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = interfacepair()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class interfacepair_response(base_response) :
	def __init__(self, length=1) :
		self.interfacepair = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.interfacepair = [interfacepair() for _ in range(length)]

