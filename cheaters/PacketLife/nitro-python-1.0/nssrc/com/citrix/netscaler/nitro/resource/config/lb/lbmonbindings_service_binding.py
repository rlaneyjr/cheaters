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

class lbmonbindings_service_binding(base_resource) :
	""" Binding class showing the service that can be bound to lbmonbindings.
	"""
	def __init__(self) :
		self._servicename = ""
		self._ipaddress = ""
		self._port = 0
		self._servicetype = ""
		self._svrstate = ""
		self._monsvcstate = ""
		self._monitorname = ""
		self.___count = 0

	@property
	def servicename(self) :
		ur"""The name of the service.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""The name of the service.
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def monitorname(self) :
		ur"""The name of the monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._monitorname
		except Exception as e:
			raise e

	@monitorname.setter
	def monitorname(self, monitorname) :
		ur"""The name of the monitor.<br/>Minimum length =  1
		"""
		try :
			self._monitorname = monitorname
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		ur"""The type of service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RDP, DIAMETER, SSL_DIAMETER, TFTP.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		ur"""The state of the service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def monsvcstate(self) :
		ur"""The configured state (enable/disable) of Monitor on this service.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._monsvcstate
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""The port of the service.<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""The IPAddress of the service.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmonbindings_service_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmonbindings_service_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.monitorname is not None :
				return str(self.monitorname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, monitorname) :
		ur""" Use this API to fetch lbmonbindings_service_binding resources.
		"""
		try :
			obj = lbmonbindings_service_binding()
			obj.monitorname = monitorname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, monitorname, filter_) :
		ur""" Use this API to fetch filtered set of lbmonbindings_service_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonbindings_service_binding()
			obj.monitorname = monitorname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, monitorname) :
		ur""" Use this API to count lbmonbindings_service_binding resources configued on NetScaler.
		"""
		try :
			obj = lbmonbindings_service_binding()
			obj.monitorname = monitorname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, monitorname, filter_) :
		ur""" Use this API to count the filtered set of lbmonbindings_service_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonbindings_service_binding()
			obj.monitorname = monitorname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		DTLS = "DTLS"
		NNTP = "NNTP"
		RPCSVR = "RPCSVR"
		DNS = "DNS"
		ADNS = "ADNS"
		SNMP = "SNMP"
		RTSP = "RTSP"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		DNS_TCP = "DNS_TCP"
		ADNS_TCP = "ADNS_TCP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"
		RADIUS = "RADIUS"
		RDP = "RDP"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"

	class Svrstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Monsvcstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lbmonbindings_service_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbmonbindings_service_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmonbindings_service_binding = [lbmonbindings_service_binding() for _ in range(length)]

