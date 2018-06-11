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

class nstrafficdomain_bridgegroup_binding(base_resource) :
	""" Binding class showing the bridgegroup that can be bound to nstrafficdomain.
	"""
	def __init__(self) :
		self._bridgegroup = 0
		self._bridgegroup = 0
		self._td = 0
		self.___count = 0

	@property
	def bridgegroup(self) :
		ur"""ID of the configured bridge to bind to this traffic domain. More than one bridge group can be bound to a traffic domain, but the same bridge group cannot be a part of multiple traffic domains.<br/>Minimum value =  1<br/>Maximum value =  1000.
		"""
		try :
			return self._bridgegroup
		except Exception as e:
			raise e

	@bridgegroup.setter
	def bridgegroup(self, bridgegroup) :
		ur"""ID of the configured bridge to bind to this traffic domain. More than one bridge group can be bound to a traffic domain, but the same bridge group cannot be a part of multiple traffic domains.<br/>Minimum value =  1<br/>Maximum value =  1000
		"""
		try :
			self._bridgegroup = bridgegroup
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Integer value that uniquely identifies a traffic domain.<br/>Minimum value =  1<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Integer value that uniquely identifies a traffic domain.<br/>Minimum value =  1<br/>Maximum value =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstrafficdomain_bridgegroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstrafficdomain_bridgegroup_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.td is not None :
				return str(self.td)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = nstrafficdomain_bridgegroup_binding()
				updateresource.td = resource.td
				updateresource.bridgegroup = resource.bridgegroup
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [nstrafficdomain_bridgegroup_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].td = resource[i].td
						updateresources[i].bridgegroup = resource[i].bridgegroup
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = nstrafficdomain_bridgegroup_binding()
				deleteresource.td = resource.td
				deleteresource.bridgegroup = resource.bridgegroup
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [nstrafficdomain_bridgegroup_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].td = resource[i].td
						deleteresources[i].bridgegroup = resource[i].bridgegroup
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, td) :
		ur""" Use this API to fetch nstrafficdomain_bridgegroup_binding resources.
		"""
		try :
			obj = nstrafficdomain_bridgegroup_binding()
			obj.td = td
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, td, filter_) :
		ur""" Use this API to fetch filtered set of nstrafficdomain_bridgegroup_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstrafficdomain_bridgegroup_binding()
			obj.td = td
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, td) :
		ur""" Use this API to count nstrafficdomain_bridgegroup_binding resources configued on NetScaler.
		"""
		try :
			obj = nstrafficdomain_bridgegroup_binding()
			obj.td = td
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, td, filter_) :
		ur""" Use this API to count the filtered set of nstrafficdomain_bridgegroup_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstrafficdomain_bridgegroup_binding()
			obj.td = td
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class nstrafficdomain_bridgegroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nstrafficdomain_bridgegroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstrafficdomain_bridgegroup_binding = [nstrafficdomain_bridgegroup_binding() for _ in range(length)]

