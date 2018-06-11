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

class nslimitidentifier_binding(base_resource):
	""" Binding class showing the resources that can be bound to nslimitidentifier_binding. 
	"""
	def __init__(self) :
		self._limitidentifier = ""
		self.nslimitidentifier_nslimitsessions_binding = []

	@property
	def limitidentifier(self) :
		ur"""Name of the rate limit identifier about which to display information. If a name is not provided, information about all rate limit identifiers is shown.
		"""
		try :
			return self._limitidentifier
		except Exception as e:
			raise e

	@limitidentifier.setter
	def limitidentifier(self, limitidentifier) :
		ur"""Name of the rate limit identifier about which to display information. If a name is not provided, information about all rate limit identifiers is shown.
		"""
		try :
			self._limitidentifier = limitidentifier
		except Exception as e:
			raise e

	@property
	def nslimitidentifier_nslimitsessions_bindings(self) :
		ur"""nslimitsessions that can be bound to nslimitidentifier.
		"""
		try :
			return self._nslimitidentifier_nslimitsessions_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslimitidentifier_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslimitidentifier_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.limitidentifier is not None :
				return str(self.limitidentifier)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, limitidentifier) :
		ur""" Use this API to fetch nslimitidentifier_binding resource.
		"""
		try :
			if type(limitidentifier) is not list :
				obj = nslimitidentifier_binding()
				obj.limitidentifier = limitidentifier
				response = obj.get_resource(service)
			else :
				if limitidentifier and len(limitidentifier) > 0 :
					obj = [nslimitidentifier_binding() for _ in range(len(limitidentifier))]
					for i in range(len(limitidentifier)) :
						obj[i].limitidentifier = limitidentifier[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class nslimitidentifier_binding_response(base_response) :
	def __init__(self, length=1) :
		self.nslimitidentifier_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslimitidentifier_binding = [nslimitidentifier_binding() for _ in range(length)]

