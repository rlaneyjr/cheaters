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

class lbwlm_lbvserver_binding(base_resource) :
	""" Binding class showing the lbvserver that can be bound to lbwlm.
	"""
	def __init__(self) :
		self._vservername = ""
		self._wlmname = ""
		self.___count = 0

	@property
	def wlmname(self) :
		ur"""The name of the Work Load Manager.<br/>Minimum length =  1.
		"""
		try :
			return self._wlmname
		except Exception as e:
			raise e

	@wlmname.setter
	def wlmname(self, wlmname) :
		ur"""The name of the Work Load Manager.<br/>Minimum length =  1
		"""
		try :
			self._wlmname = wlmname
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		ur"""Name of the virtual server which is to be bound to the WLM.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		ur"""Name of the virtual server which is to be bound to the WLM.
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbwlm_lbvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbwlm_lbvserver_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.wlmname is not None :
				return str(self.wlmname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = lbwlm_lbvserver_binding()
				updateresource.wlmname = resource.wlmname
				updateresource.vservername = resource.vservername
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lbwlm_lbvserver_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].wlmname = resource[i].wlmname
						updateresources[i].vservername = resource[i].vservername
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = lbwlm_lbvserver_binding()
				deleteresource.wlmname = resource.wlmname
				deleteresource.vservername = resource.vservername
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lbwlm_lbvserver_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].wlmname = resource[i].wlmname
						deleteresources[i].vservername = resource[i].vservername
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, wlmname) :
		ur""" Use this API to fetch lbwlm_lbvserver_binding resources.
		"""
		try :
			obj = lbwlm_lbvserver_binding()
			obj.wlmname = wlmname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, wlmname, filter_) :
		ur""" Use this API to fetch filtered set of lbwlm_lbvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbwlm_lbvserver_binding()
			obj.wlmname = wlmname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, wlmname) :
		ur""" Use this API to count lbwlm_lbvserver_binding resources configued on NetScaler.
		"""
		try :
			obj = lbwlm_lbvserver_binding()
			obj.wlmname = wlmname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, wlmname, filter_) :
		ur""" Use this API to count the filtered set of lbwlm_lbvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbwlm_lbvserver_binding()
			obj.wlmname = wlmname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class lbwlm_lbvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbwlm_lbvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbwlm_lbvserver_binding = [lbwlm_lbvserver_binding() for _ in range(length)]

