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

class lbwlm_binding(base_resource):
	""" Binding class showing the resources that can be bound to lbwlm_binding. 
	"""
	def __init__(self) :
		self._wlmname = ""
		self.lbwlm_lbvserver_binding = []

	@property
	def wlmname(self) :
		ur"""The name of the work load manager.<br/>Minimum length =  1.
		"""
		try :
			return self._wlmname
		except Exception as e:
			raise e

	@wlmname.setter
	def wlmname(self, wlmname) :
		ur"""The name of the work load manager.<br/>Minimum length =  1
		"""
		try :
			self._wlmname = wlmname
		except Exception as e:
			raise e

	@property
	def lbwlm_lbvserver_bindings(self) :
		ur"""lbvserver that can be bound to lbwlm.
		"""
		try :
			return self._lbwlm_lbvserver_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbwlm_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbwlm_binding
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
	def get(self, service, wlmname) :
		ur""" Use this API to fetch lbwlm_binding resource.
		"""
		try :
			if type(wlmname) is not list :
				obj = lbwlm_binding()
				obj.wlmname = wlmname
				response = obj.get_resource(service)
			else :
				if wlmname and len(wlmname) > 0 :
					obj = [lbwlm_binding() for _ in range(len(wlmname))]
					for i in range(len(wlmname)) :
						obj[i].wlmname = wlmname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lbwlm_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbwlm_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbwlm_binding = [lbwlm_binding() for _ in range(length)]

