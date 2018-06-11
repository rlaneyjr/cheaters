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

class lbmetrictable_binding(base_resource):
	""" Binding class showing the resources that can be bound to lbmetrictable_binding. 
	"""
	def __init__(self) :
		self._metrictable = ""
		self.lbmetrictable_metric_binding = []

	@property
	def metrictable(self) :
		ur"""Name of the metric table.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._metrictable
		except Exception as e:
			raise e

	@metrictable.setter
	def metrictable(self, metrictable) :
		ur"""Name of the metric table.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._metrictable = metrictable
		except Exception as e:
			raise e

	@property
	def lbmetrictable_metric_bindings(self) :
		ur"""metric that can be bound to lbmetrictable.
		"""
		try :
			return self._lbmetrictable_metric_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmetrictable_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmetrictable_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.metrictable is not None :
				return str(self.metrictable)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, metrictable) :
		ur""" Use this API to fetch lbmetrictable_binding resource.
		"""
		try :
			if type(metrictable) is not list :
				obj = lbmetrictable_binding()
				obj.metrictable = metrictable
				response = obj.get_resource(service)
			else :
				if metrictable and len(metrictable) > 0 :
					obj = [lbmetrictable_binding() for _ in range(len(metrictable))]
					for i in range(len(metrictable)) :
						obj[i].metrictable = metrictable[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class lbmetrictable_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbmetrictable_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmetrictable_binding = [lbmetrictable_binding() for _ in range(length)]

