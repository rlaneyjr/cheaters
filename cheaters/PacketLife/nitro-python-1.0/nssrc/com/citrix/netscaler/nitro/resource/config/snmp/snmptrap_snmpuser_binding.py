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

class snmptrap_snmpuser_binding(base_resource) :
	""" Binding class showing the snmpuser that can be bound to snmptrap.
	"""
	def __init__(self) :
		self._username = ""
		self._securitylevel = ""
		self._trapclass = ""
		self._trapdestination = ""
		self._td = 0
		self._version = ""
		self.___count = 0

	@property
	def trapclass(self) :
		ur"""Type of trap messages that the NetScaler appliance sends to the trap listener: Generic or the enterprise-specific messages defined in the MIB file.<br/>Possible values = generic, specific.
		"""
		try :
			return self._trapclass
		except Exception as e:
			raise e

	@trapclass.setter
	def trapclass(self, trapclass) :
		ur"""Type of trap messages that the NetScaler appliance sends to the trap listener: Generic or the enterprise-specific messages defined in the MIB file.<br/>Possible values = generic, specific
		"""
		try :
			self._trapclass = trapclass
		except Exception as e:
			raise e

	@property
	def securitylevel(self) :
		ur"""Security level of the SNMPv3 trap.<br/>Default value: authNoPriv,<br/>Possible values = noAuthNoPriv, authNoPriv, authPriv.
		"""
		try :
			return self._securitylevel
		except Exception as e:
			raise e

	@securitylevel.setter
	def securitylevel(self, securitylevel) :
		ur"""Security level of the SNMPv3 trap.<br/>Default value: authNoPriv,<br/>Possible values = noAuthNoPriv, authNoPriv, authPriv
		"""
		try :
			self._securitylevel = securitylevel
		except Exception as e:
			raise e

	@property
	def username(self) :
		ur"""Name of the SNMP user that will send the SNMPv3 traps.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Name of the SNMP user that will send the SNMPv3 traps.
		"""
		try :
			self._username = username
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
	def trapdestination(self) :
		ur"""IPv4 or the IPv6 address of the trap listener to which the NetScaler appliance is to send SNMP trap messages.<br/>Minimum length =  1.
		"""
		try :
			return self._trapdestination
		except Exception as e:
			raise e

	@trapdestination.setter
	def trapdestination(self, trapdestination) :
		ur"""IPv4 or the IPv6 address of the trap listener to which the NetScaler appliance is to send SNMP trap messages.<br/>Minimum length =  1
		"""
		try :
			self._trapdestination = trapdestination
		except Exception as e:
			raise e

	@property
	def version(self) :
		ur"""SNMP version, which determines the format of trap messages sent to the trap listener. 
		This setting must match the setting on the trap listener. Otherwise, the listener drops the trap messages.<br/>Default value: V3<br/>Possible values = V1, V2, V3.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@version.setter
	def version(self, version) :
		ur"""SNMP version, which determines the format of trap messages sent to the trap listener. 
		This setting must match the setting on the trap listener. Otherwise, the listener drops the trap messages.<br/>Default value: V3<br/>Possible values = V1, V2, V3
		"""
		try :
			self._version = version
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmptrap_snmpuser_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmptrap_snmpuser_binding
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
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = snmptrap_snmpuser_binding()
				updateresource.trapclass = resource.trapclass
				updateresource.trapdestination = resource.trapdestination
				updateresource.td = resource.td
				updateresource.version = resource.version
				updateresource.username = resource.username
				updateresource.securitylevel = resource.securitylevel
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [snmptrap_snmpuser_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].trapclass = resource[i].trapclass
						updateresources[i].trapdestination = resource[i].trapdestination
						updateresources[i].td = resource[i].td
						updateresources[i].version = resource[i].version
						updateresources[i].username = resource[i].username
						updateresources[i].securitylevel = resource[i].securitylevel
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = snmptrap_snmpuser_binding()
				deleteresource.trapclass = resource.trapclass
				deleteresource.trapdestination = resource.trapdestination
				deleteresource.td = resource.td
				deleteresource.version = resource.version
				deleteresource.username = resource.username
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [snmptrap_snmpuser_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].trapclass = resource[i].trapclass
						deleteresources[i].trapdestination = resource[i].trapdestination
						deleteresources[i].td = resource[i].td
						deleteresources[i].version = resource[i].version
						deleteresources[i].username = resource[i].username
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, obj) :
		ur""" Use this API to fetch a snmptrap_snmpuser_binding resources.
		"""
		try :
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response =  obj.get_resources(service,option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, obj, filter_) :
		ur""" Use this API to fetch filtered set of snmptrap_snmpuser_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, obj) :
		ur""" Use this API to count snmptrap_snmpuser_binding resources configued on NetScaler.
		"""
		try :
			option_ = options()
			option_.count = True
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, obj, filter_) :
		ur""" Use this API to count the filtered set of snmptrap_snmpuser_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.count = True
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Trapclass:
		generic = "generic"
		specific = "specific"

	class Securitylevel:
		noAuthNoPriv = "noAuthNoPriv"
		authNoPriv = "authNoPriv"
		authPriv = "authPriv"

	class Version:
		V1 = "V1"
		V2 = "V2"
		V3 = "V3"

class snmptrap_snmpuser_binding_response(base_response) :
	def __init__(self, length=1) :
		self.snmptrap_snmpuser_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmptrap_snmpuser_binding = [snmptrap_snmpuser_binding() for _ in range(length)]

