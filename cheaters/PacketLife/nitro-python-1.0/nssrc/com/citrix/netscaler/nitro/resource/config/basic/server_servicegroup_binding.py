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

class server_servicegroup_binding(base_resource) :
	""" Binding class showing the servicegroup that can be bound to server.
	"""
	def __init__(self) :
		self._servicegroupname = ""
		self._svctype = ""
		self._serviceipaddress = ""
		self._port = 0
		self._customserverid = ""
		self._svrstate = ""
		self._dup_svctype = ""
		self._dup_port = 0
		self._svrcfgflags = 0
		self._serviceipstr = ""
		self._monthreshold = 0
		self._maxclient = 0
		self._maxreq = 0
		self._maxbandwidth = 0
		self._usip = ""
		self._cka = ""
		self._tcpb = ""
		self._cmp = ""
		self._clttimeout = 0
		self._svrtimeout = 0
		self._cipheader = ""
		self._cip = ""
		self._cacheable = ""
		self._sc = ""
		self._sp = ""
		self._downstateflush = ""
		self._appflowlog = ""
		self._boundtd = 0
		self._name = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the server for which to display parameters.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the server for which to display parameters.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def servicegroupname(self) :
		ur"""servicegroups bind to this server.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		ur"""servicegroups bind to this server.
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def sp(self) :
		ur"""Enable surge protection for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sp
		except Exception as e:
			raise e

	@property
	def sc(self) :
		ur"""State of the SureConnect feature for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@property
	def svrtimeout(self) :
		ur"""Time, in seconds, after which to terminate an idle server connection.<br/>Minimum value =  0<br/>Maximum value =  31536000.
		"""
		try :
			return self._svrtimeout
		except Exception as e:
			raise e

	@property
	def serviceipstr(self) :
		ur"""This field has been intorduced to show the dbs services ip.
		"""
		try :
			return self._serviceipstr
		except Exception as e:
			raise e

	@property
	def tcpb(self) :
		ur"""Enable TCP buffering for the service group.<br/>Possible values = YES, NO.
		"""
		try :
			return self._tcpb
		except Exception as e:
			raise e

	@property
	def cip(self) :
		ur"""Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@property
	def dup_port(self) :
		ur"""port of the service.<br/>Range 1 - 65535.
		"""
		try :
			return self._dup_port
		except Exception as e:
			raise e

	@property
	def customserverid(self) :
		ur"""A positive integer to identify the service. Used when the persistency type is set to Custom Server ID.<br/>Default value: "None".
		"""
		try :
			return self._customserverid
		except Exception as e:
			raise e

	@property
	def boundtd(self) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._boundtd
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		ur"""Perform delayed clean-up of connections to all services in the service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@property
	def svctype(self) :
		ur"""The type of bound service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RDP, DIAMETER, SSL_DIAMETER, TFTP.
		"""
		try :
			return self._svctype
		except Exception as e:
			raise e

	@property
	def cka(self) :
		ur"""Enable client keep-alive for the service group.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cka
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		ur"""The state of the bound service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		ur"""Enable logging of AppFlow information for the specified service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		ur"""Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@property
	def maxclient(self) :
		ur"""Maximum number of simultaneous open connections for the service group.<br/>Minimum value =  0<br/>Maximum value =  4294967294.
		"""
		try :
			return self._maxclient
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		ur"""Time, in seconds, after which to terminate an idle client connection.<br/>Minimum value =  0<br/>Maximum value =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""The port number to be used for the bound service.<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@property
	def dup_svctype(self) :
		ur"""service type of the service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RDP, DIAMETER, SSL_DIAMETER, TFTP.
		"""
		try :
			return self._dup_svctype
		except Exception as e:
			raise e

	@property
	def cmp(self) :
		ur"""Enable compression for the specified service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cmp
		except Exception as e:
			raise e

	@property
	def monthreshold(self) :
		ur"""Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.<br/>Minimum value =  0<br/>Maximum value =  65535.
		"""
		try :
			return self._monthreshold
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		ur"""Maximum number of requests that can be sent on a persistent connection to the service group. 
		Note: Connection requests beyond this value are rejected.<br/>Minimum value =  0<br/>Maximum value =  65535.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@property
	def serviceipaddress(self) :
		ur"""The IP address of the bound service.
		"""
		try :
			return self._serviceipaddress
		except Exception as e:
			raise e

	@property
	def usip(self) :
		ur"""Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._usip
		except Exception as e:
			raise e

	@property
	def cacheable(self) :
		ur"""Use the transparent cache redirection virtual server to forward the request to the cache server.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheable
		except Exception as e:
			raise e

	@property
	def maxbandwidth(self) :
		ur"""Maximum bandwidth, in Kbps, allocated for all the services in the service group.<br/>Minimum value =  0<br/>Maximum value =  4294967287.
		"""
		try :
			return self._maxbandwidth
		except Exception as e:
			raise e

	@property
	def svrcfgflags(self) :
		ur"""service flags to denote its a db enabled.
		"""
		try :
			return self._svrcfgflags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(server_servicegroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.server_servicegroup_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch server_servicegroup_binding resources.
		"""
		try :
			obj = server_servicegroup_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of server_servicegroup_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = server_servicegroup_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count server_servicegroup_binding resources configued on NetScaler.
		"""
		try :
			obj = server_servicegroup_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of server_servicegroup_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = server_servicegroup_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Sp:
		ON = "ON"
		OFF = "OFF"

	class Sc:
		ON = "ON"
		OFF = "OFF"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Svctype:
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

	class Dup_svctype:
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

	class Usip:
		YES = "YES"
		NO = "NO"

	class Cacheable:
		YES = "YES"
		NO = "NO"

	class Tcpb:
		YES = "YES"
		NO = "NO"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cka:
		YES = "YES"
		NO = "NO"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cmp:
		YES = "YES"
		NO = "NO"

class server_servicegroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.server_servicegroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.server_servicegroup_binding = [server_servicegroup_binding() for _ in range(length)]

