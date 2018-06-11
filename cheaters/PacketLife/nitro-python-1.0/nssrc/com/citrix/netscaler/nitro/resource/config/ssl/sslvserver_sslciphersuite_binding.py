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

class sslvserver_sslciphersuite_binding(base_resource) :
	""" Binding class showing the sslciphersuite that can be bound to sslvserver.
	"""
	def __init__(self) :
		self._ciphername = ""
		self._description = ""
		self._vservername = ""
		self.___count = 0

	@property
	def ciphername(self) :
		ur"""The cipher group/alias/individual cipher configuration.
		"""
		try :
			return self._ciphername
		except Exception as e:
			raise e

	@ciphername.setter
	def ciphername(self, ciphername) :
		ur"""The cipher group/alias/individual cipher configuration.
		"""
		try :
			self._ciphername = ciphername
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""The cipher suite description.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@description.setter
	def description(self, description) :
		ur"""The cipher suite description.
		"""
		try :
			self._description = description
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		ur"""Name of the SSL virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		ur"""Name of the SSL virtual server.<br/>Minimum length =  1
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslvserver_sslciphersuite_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslvserver_sslciphersuite_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.vservername is not None :
				return str(self.vservername)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = sslvserver_sslciphersuite_binding()
				updateresource.vservername = resource.vservername
				updateresource.ciphername = resource.ciphername
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslvserver_sslciphersuite_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].vservername = resource[i].vservername
						updateresources[i].ciphername = resource[i].ciphername
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslvserver_sslciphersuite_binding()
				deleteresource.vservername = resource.vservername
				deleteresource.ciphername = resource.ciphername
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslvserver_sslciphersuite_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].vservername = resource[i].vservername
						deleteresources[i].ciphername = resource[i].ciphername
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, vservername) :
		ur""" Use this API to fetch sslvserver_sslciphersuite_binding resources.
		"""
		try :
			obj = sslvserver_sslciphersuite_binding()
			obj.vservername = vservername
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, vservername, filter_) :
		ur""" Use this API to fetch filtered set of sslvserver_sslciphersuite_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver_sslciphersuite_binding()
			obj.vservername = vservername
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, vservername) :
		ur""" Use this API to count sslvserver_sslciphersuite_binding resources configued on NetScaler.
		"""
		try :
			obj = sslvserver_sslciphersuite_binding()
			obj.vservername = vservername
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, vservername, filter_) :
		ur""" Use this API to count the filtered set of sslvserver_sslciphersuite_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver_sslciphersuite_binding()
			obj.vservername = vservername
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Ecccurvename:
		ALL = "ALL"
		P_224 = "P_224"
		P_256 = "P_256"
		P_384 = "P_384"
		P_521 = "P_521"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Labeltype:
		vserver = "vserver"
		service = "service"
		policylabel = "policylabel"

class sslvserver_sslciphersuite_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslvserver_sslciphersuite_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslvserver_sslciphersuite_binding = [sslvserver_sslciphersuite_binding() for _ in range(length)]

