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

class gslbsite_binding(base_resource):
	""" Binding class showing the resources that can be bound to gslbsite_binding. 
	"""
	def __init__(self) :
		self._sitename = ""
		self.gslbsite_gslbservice_binding = []

	@property
	def sitename(self) :
		ur"""Name of the GSLB site. If you specify a site name, details of all the site's constituent services are also displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@sitename.setter
	def sitename(self, sitename) :
		ur"""Name of the GSLB site. If you specify a site name, details of all the site's constituent services are also displayed.<br/>Minimum length =  1
		"""
		try :
			self._sitename = sitename
		except Exception as e:
			raise e

	@property
	def gslbsite_gslbservice_bindings(self) :
		ur"""gslbservice that can be bound to gslbsite.
		"""
		try :
			return self._gslbsite_gslbservice_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbsite_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbsite_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sitename is not None :
				return str(self.sitename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, sitename) :
		ur""" Use this API to fetch gslbsite_binding resource.
		"""
		try :
			if type(sitename) is not list :
				obj = gslbsite_binding()
				obj.sitename = sitename
				response = obj.get_resource(service)
			else :
				if sitename and len(sitename) > 0 :
					obj = [gslbsite_binding() for _ in range(len(sitename))]
					for i in range(len(sitename)) :
						obj[i].sitename = sitename[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class gslbsite_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbsite_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbsite_binding = [gslbsite_binding() for _ in range(length)]

