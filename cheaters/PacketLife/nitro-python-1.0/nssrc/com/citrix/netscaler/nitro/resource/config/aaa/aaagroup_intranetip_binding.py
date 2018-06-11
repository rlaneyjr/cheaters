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

class aaagroup_intranetip_binding(base_resource) :
	""" Binding class showing the intranetip that can be bound to aaagroup.
	"""
	def __init__(self) :
		self._intranetip = ""
		self._netmask = ""
		self._groupname = ""
		self.___count = 0

	@property
	def intranetip(self) :
		ur"""The Intranet IP(s) bound to the group.
		"""
		try :
			return self._intranetip
		except Exception as e:
			raise e

	@intranetip.setter
	def intranetip(self, intranetip) :
		ur"""The Intranet IP(s) bound to the group.
		"""
		try :
			self._intranetip = intranetip
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		ur"""Name of the group that you are binding.<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name of the group that you are binding.<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""The netmask for the Intranet IP.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""The netmask for the Intranet IP.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaagroup_intranetip_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaagroup_intranetip_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.groupname is not None :
				return str(self.groupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = aaagroup_intranetip_binding()
				updateresource.groupname = resource.groupname
				updateresource.intranetip = resource.intranetip
				updateresource.netmask = resource.netmask
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [aaagroup_intranetip_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].groupname = resource[i].groupname
						updateresources[i].intranetip = resource[i].intranetip
						updateresources[i].netmask = resource[i].netmask
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = aaagroup_intranetip_binding()
				deleteresource.groupname = resource.groupname
				deleteresource.intranetip = resource.intranetip
				deleteresource.netmask = resource.netmask
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [aaagroup_intranetip_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].groupname = resource[i].groupname
						deleteresources[i].intranetip = resource[i].intranetip
						deleteresources[i].netmask = resource[i].netmask
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, groupname) :
		ur""" Use this API to fetch aaagroup_intranetip_binding resources.
		"""
		try :
			obj = aaagroup_intranetip_binding()
			obj.groupname = groupname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, groupname, filter_) :
		ur""" Use this API to fetch filtered set of aaagroup_intranetip_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaagroup_intranetip_binding()
			obj.groupname = groupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, groupname) :
		ur""" Use this API to count aaagroup_intranetip_binding resources configued on NetScaler.
		"""
		try :
			obj = aaagroup_intranetip_binding()
			obj.groupname = groupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, groupname, filter_) :
		ur""" Use this API to count the filtered set of aaagroup_intranetip_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaagroup_intranetip_binding()
			obj.groupname = groupname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class aaagroup_intranetip_binding_response(base_response) :
	def __init__(self, length=1) :
		self.aaagroup_intranetip_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaagroup_intranetip_binding = [aaagroup_intranetip_binding() for _ in range(length)]

