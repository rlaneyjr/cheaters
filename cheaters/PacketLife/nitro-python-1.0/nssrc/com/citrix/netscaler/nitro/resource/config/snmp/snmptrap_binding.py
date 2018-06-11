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

class snmptrap_binding(base_resource):
	""" Binding class showing the resources that can be bound to snmptrap_binding. 
	"""
	def __init__(self) :
		self._trapclass = ""
		self._trapdestination = ""
		self._version = ""
		self._td = 0
		self.snmptrap_snmpuser_binding = []

	@property
	def trapdestination(self) :
		ur"""IP address specified in the trap listener entry.<br/>Minimum length =  1.
		"""
		try :
			return self._trapdestination
		except Exception as e:
			raise e

	@trapdestination.setter
	def trapdestination(self, trapdestination) :
		ur"""IP address specified in the trap listener entry.<br/>Minimum length =  1
		"""
		try :
			self._trapdestination = trapdestination
		except Exception as e:
			raise e

	@property
	def version(self) :
		ur"""The SNMP version of the trap specified in the trap listener entry.<br/>Possible values = V1, V2, V3.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@version.setter
	def version(self, version) :
		ur"""The SNMP version of the trap specified in the trap listener entry.<br/>Possible values = V1, V2, V3
		"""
		try :
			self._version = version
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Minimum value =  0<br/>Maximum value =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def trapclass(self) :
		ur"""Trap type specified in the trap listener entry.<br/>Possible values = generic, specific.
		"""
		try :
			return self._trapclass
		except Exception as e:
			raise e

	@trapclass.setter
	def trapclass(self, trapclass) :
		ur"""Trap type specified in the trap listener entry.<br/>Possible values = generic, specific
		"""
		try :
			self._trapclass = trapclass
		except Exception as e:
			raise e

	@property
	def snmptrap_snmpuser_bindings(self) :
		ur"""snmpuser that can be bound to snmptrap.
		"""
		try :
			return self._snmptrap_snmpuser_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmptrap_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmptrap_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.trapclass is not None :
				return str(self.trapclass)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, obj) :
		ur""" Use this API to fetch a snmptrap_binding resource.
		"""
		try :
			if type(obj) is not list :
				option_ = options()
				option_.args = nitro_util.object_to_string_withoutquotes(obj)
				response = obj.get_resource(service, option_)
			else :
				if obj and len(obj) > 0 :
					for i in range(len(obj)) :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(obj[i])
						response[i] = obj[i].get_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Version:
		V1 = "V1"
		V2 = "V2"
		V3 = "V3"

	class Trapclass:
		generic = "generic"
		specific = "specific"

class snmptrap_binding_response(base_response) :
	def __init__(self, length=1) :
		self.snmptrap_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmptrap_binding = [snmptrap_binding() for _ in range(length)]

