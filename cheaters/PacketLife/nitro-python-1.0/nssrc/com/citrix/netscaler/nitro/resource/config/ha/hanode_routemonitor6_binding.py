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

class hanode_routemonitor6_binding(base_resource) :
	""" Binding class showing the routemonitor6 that can be bound to hanode.
	"""
	def __init__(self) :
		self._routemonitor = ""
		self._netmask = ""
		self._flags = 0
		self._routemonitorstate = ""
		self._id = 0
		self.___count = 0

	@property
	def routemonitor(self) :
		ur"""The IP address (IPv4 or IPv6).
		"""
		try :
			return self._routemonitor
		except Exception as e:
			raise e

	@routemonitor.setter
	def routemonitor(self, routemonitor) :
		ur"""The IP address (IPv4 or IPv6).
		"""
		try :
			self._routemonitor = routemonitor
		except Exception as e:
			raise e

	@property
	def id(self) :
		ur"""Number that uniquely identifies the local node. The ID of the local node is always 0.<br/>Minimum value =  0<br/>Maximum value =  64.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""Number that uniquely identifies the local node. The ID of the local node is always 0.<br/>Minimum value =  0<br/>Maximum value =  64
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""The netmask.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""The netmask.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def routemonitorstate(self) :
		ur"""State for route monitor.<br/>Possible values = UP, DOWN.
		"""
		try :
			return self._routemonitorstate
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""The flags for this entry.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(hanode_routemonitor6_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.hanode_routemonitor6_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = hanode_routemonitor6_binding()
				updateresource.id = resource.id
				updateresource.routemonitor = resource.routemonitor
				updateresource.netmask = resource.netmask
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [hanode_routemonitor6_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].routemonitor = resource[i].routemonitor
						updateresources[i].netmask = resource[i].netmask
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = hanode_routemonitor6_binding()
				deleteresource.id = resource.id
				deleteresource.routemonitor = resource.routemonitor
				deleteresource.netmask = resource.netmask
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [hanode_routemonitor6_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].id = resource[i].id
						deleteresources[i].routemonitor = resource[i].routemonitor
						deleteresources[i].netmask = resource[i].netmask
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, id) :
		ur""" Use this API to fetch hanode_routemonitor6_binding resources.
		"""
		try :
			obj = hanode_routemonitor6_binding()
			obj.id = id
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, id, filter_) :
		ur""" Use this API to fetch filtered set of hanode_routemonitor6_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = hanode_routemonitor6_binding()
			obj.id = id
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, id) :
		ur""" Use this API to count hanode_routemonitor6_binding resources configued on NetScaler.
		"""
		try :
			obj = hanode_routemonitor6_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, id, filter_) :
		ur""" Use this API to count the filtered set of hanode_routemonitor6_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = hanode_routemonitor6_binding()
			obj.id = id
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Routemonitorstate:
		UP = "UP"
		DOWN = "DOWN"

class hanode_routemonitor6_binding_response(base_response) :
	def __init__(self, length=1) :
		self.hanode_routemonitor6_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.hanode_routemonitor6_binding = [hanode_routemonitor6_binding() for _ in range(length)]

