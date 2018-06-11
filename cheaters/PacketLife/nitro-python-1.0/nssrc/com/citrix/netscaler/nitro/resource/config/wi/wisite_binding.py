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

class wisite_binding(base_resource):
	""" Binding class showing the resources that can be bound to wisite_binding. 
	"""
	def __init__(self) :
		self._sitepath = ""
		self.wisite_translationinternalip_binding = []
		self.wisite_accessmethod_binding = []
		self.wisite_farmname_binding = []

	@property
	def sitepath(self) :
		ur"""Path of a Web Interface site whose details you want the NetScaler appliance to display.<br/>Minimum length =  1<br/>Maximum length =  250.
		"""
		try :
			return self._sitepath
		except Exception as e:
			raise e

	@sitepath.setter
	def sitepath(self, sitepath) :
		ur"""Path of a Web Interface site whose details you want the NetScaler appliance to display.<br/>Minimum length =  1<br/>Maximum length =  250
		"""
		try :
			self._sitepath = sitepath
		except Exception as e:
			raise e

	@property
	def wisite_translationinternalip_bindings(self) :
		ur"""translationinternalip that can be bound to wisite.
		"""
		try :
			return self._wisite_translationinternalip_binding
		except Exception as e:
			raise e

	@property
	def wisite_accessmethod_bindings(self) :
		ur"""accessmethod that can be bound to wisite.
		"""
		try :
			return self._wisite_accessmethod_binding
		except Exception as e:
			raise e

	@property
	def wisite_farmname_bindings(self) :
		ur"""farmname that can be bound to wisite.
		"""
		try :
			return self._wisite_farmname_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wisite_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wisite_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sitepath is not None :
				return str(self.sitepath)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, sitepath) :
		ur""" Use this API to fetch wisite_binding resource.
		"""
		try :
			if type(sitepath) is not list :
				obj = wisite_binding()
				obj.sitepath = sitepath
				response = obj.get_resource(service)
			else :
				if sitepath and len(sitepath) > 0 :
					obj = [wisite_binding() for _ in range(len(sitepath))]
					for i in range(len(sitepath)) :
						obj[i].sitepath = sitepath[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class wisite_binding_response(base_response) :
	def __init__(self, length=1) :
		self.wisite_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wisite_binding = [wisite_binding() for _ in range(length)]

