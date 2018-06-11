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

class fis_interface_binding(base_resource) :
	""" Binding class showing the interface that can be bound to fis.
	"""
	def __init__(self) :
		self._ifnum = ""
		self._ownernode = 0
		self._name = ""

	@property
	def ownernode(self) :
		ur"""ID of the cluster node for which you are creating the FIS. Can be configured only through the cluster IP address.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		ur"""ID of the cluster node for which you are creating the FIS. Can be configured only through the cluster IP address.<br/>Minimum value =  0<br/>Maximum value =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""The name of the FIS to which you want to bind interfaces.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of the FIS to which you want to bind interfaces.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		ur"""Interface to be bound to the FIS, specified in slot/port notation (for example, 1/3).
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		ur"""Interface to be bound to the FIS, specified in slot/port notation (for example, 1/3).
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(fis_interface_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.fis_interface_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = fis_interface_binding()
				updateresource.name = resource.name
				updateresource.ifnum = resource.ifnum
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [fis_interface_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ifnum = resource[i].ifnum
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = fis_interface_binding()
				deleteresource.name = resource.name
				deleteresource.ifnum = resource.ifnum
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [fis_interface_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].ifnum = resource[i].ifnum
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

class fis_interface_binding_response(base_response) :
	def __init__(self, length=1) :
		self.fis_interface_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.fis_interface_binding = [fis_interface_binding() for _ in range(length)]

