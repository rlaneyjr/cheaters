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

class gslbservice_binding(base_resource):
	""" Binding class showing the resources that can be bound to gslbservice_binding. 
	"""
	def __init__(self) :
		self._servicename = ""
		self.gslbservice_lbmonitor_binding = []
		self.gslbservice_dnsview_binding = []

	@property
	def servicename(self) :
		ur"""Name of the GSLB service.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""Name of the GSLB service.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def gslbservice_lbmonitor_bindings(self) :
		ur"""lbmonitor that can be bound to gslbservice.
		"""
		try :
			return self._gslbservice_lbmonitor_binding
		except Exception as e:
			raise e

	@property
	def gslbservice_dnsview_bindings(self) :
		ur"""dnsview that can be bound to gslbservice.
		"""
		try :
			return self._gslbservice_dnsview_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbservice_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbservice_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicename is not None :
				return str(self.servicename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, servicename) :
		ur""" Use this API to fetch gslbservice_binding resource.
		"""
		try :
			if type(servicename) is not list :
				obj = gslbservice_binding()
				obj.servicename = servicename
				response = obj.get_resource(service)
			else :
				if servicename and len(servicename) > 0 :
					obj = [gslbservice_binding() for _ in range(len(servicename))]
					for i in range(len(servicename)) :
						obj[i].servicename = servicename[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class gslbservice_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbservice_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbservice_binding = [gslbservice_binding() for _ in range(length)]

