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

class vxlan_iptunnel_binding(base_resource) :
	""" Binding class showing the iptunnel that can be bound to vxlan.
	"""
	def __init__(self) :
		self._tunnel = ""
		self._id = 0
		self.___count = 0

	@property
	def id(self) :
		ur"""A positive integer, which is also called VXLAN Network Identifier (VNI), that uniquely identifies a VXLAN.<br/>Minimum value =  1<br/>Maximum value =  16777215.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""A positive integer, which is also called VXLAN Network Identifier (VNI), that uniquely identifies a VXLAN.<br/>Minimum value =  1<br/>Maximum value =  16777215
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def tunnel(self) :
		ur"""Specifies the name of the configured tunnel to be associated with this VXLAN.
		"""
		try :
			return self._tunnel
		except Exception as e:
			raise e

	@tunnel.setter
	def tunnel(self, tunnel) :
		ur"""Specifies the name of the configured tunnel to be associated with this VXLAN.
		"""
		try :
			self._tunnel = tunnel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vxlan_iptunnel_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vxlan_iptunnel_binding
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
				updateresource = vxlan_iptunnel_binding()
				updateresource.id = resource.id
				updateresource.tunnel = resource.tunnel
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vxlan_iptunnel_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].tunnel = resource[i].tunnel
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = vxlan_iptunnel_binding()
				deleteresource.id = resource.id
				deleteresource.tunnel = resource.tunnel
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vxlan_iptunnel_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].id = resource[i].id
						deleteresources[i].tunnel = resource[i].tunnel
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, id) :
		ur""" Use this API to fetch vxlan_iptunnel_binding resources.
		"""
		try :
			obj = vxlan_iptunnel_binding()
			obj.id = id
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, id, filter_) :
		ur""" Use this API to fetch filtered set of vxlan_iptunnel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vxlan_iptunnel_binding()
			obj.id = id
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, id) :
		ur""" Use this API to count vxlan_iptunnel_binding resources configued on NetScaler.
		"""
		try :
			obj = vxlan_iptunnel_binding()
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
		ur""" Use this API to count the filtered set of vxlan_iptunnel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vxlan_iptunnel_binding()
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

class vxlan_iptunnel_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vxlan_iptunnel_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vxlan_iptunnel_binding = [vxlan_iptunnel_binding() for _ in range(length)]

