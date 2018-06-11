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

class nd6ravariables_onlinkipv6prefix_binding(base_resource) :
	""" Binding class showing the onlinkipv6prefix that can be bound to nd6ravariables.
	"""
	def __init__(self) :
		self._ipv6prefix = ""
		self._vlan = 0
		self.___count = 0

	@property
	def ipv6prefix(self) :
		ur"""Onlink prefixes for RA messages.
		"""
		try :
			return self._ipv6prefix
		except Exception as e:
			raise e

	@ipv6prefix.setter
	def ipv6prefix(self, ipv6prefix) :
		ur"""Onlink prefixes for RA messages.
		"""
		try :
			self._ipv6prefix = ipv6prefix
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		ur"""The VLAN number.<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		ur"""The VLAN number.<br/>Minimum value =  0<br/>Maximum value =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nd6ravariables_onlinkipv6prefix_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nd6ravariables_onlinkipv6prefix_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.vlan is not None :
				return str(self.vlan)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = nd6ravariables_onlinkipv6prefix_binding()
				updateresource.vlan = resource.vlan
				updateresource.ipv6prefix = resource.ipv6prefix
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [nd6ravariables_onlinkipv6prefix_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].vlan = resource[i].vlan
						updateresources[i].ipv6prefix = resource[i].ipv6prefix
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = nd6ravariables_onlinkipv6prefix_binding()
				deleteresource.vlan = resource.vlan
				deleteresource.ipv6prefix = resource.ipv6prefix
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [nd6ravariables_onlinkipv6prefix_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].vlan = resource[i].vlan
						deleteresources[i].ipv6prefix = resource[i].ipv6prefix
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, vlan) :
		ur""" Use this API to fetch nd6ravariables_onlinkipv6prefix_binding resources.
		"""
		try :
			obj = nd6ravariables_onlinkipv6prefix_binding()
			obj.vlan = vlan
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, vlan, filter_) :
		ur""" Use this API to fetch filtered set of nd6ravariables_onlinkipv6prefix_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nd6ravariables_onlinkipv6prefix_binding()
			obj.vlan = vlan
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, vlan) :
		ur""" Use this API to count nd6ravariables_onlinkipv6prefix_binding resources configued on NetScaler.
		"""
		try :
			obj = nd6ravariables_onlinkipv6prefix_binding()
			obj.vlan = vlan
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, vlan, filter_) :
		ur""" Use this API to count the filtered set of nd6ravariables_onlinkipv6prefix_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nd6ravariables_onlinkipv6prefix_binding()
			obj.vlan = vlan
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class nd6ravariables_onlinkipv6prefix_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nd6ravariables_onlinkipv6prefix_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nd6ravariables_onlinkipv6prefix_binding = [nd6ravariables_onlinkipv6prefix_binding() for _ in range(length)]

