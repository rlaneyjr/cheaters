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

class nstrace(base_resource) :
	""" Configuration for nstrace operations resource. """
	def __init__(self) :
		self._nf = 0
		self._time = 0
		self._size = 0
		self._mode = []
		self._tcpdump = ""
		self._pernic = ""
		self._filename = ""
		self._fileid = ""
		self._filter = ""
		self._link = ""
		self._nodes = []
		self._doruntimemerge = ""
		self._doruntimecleanup = ""
		self._tracebuffers = 0
		self._skiprpc = ""
		self._inmemorytrace = ""
		self._state = ""
		self._scope = ""
		self._tracelocation = ""

	@property
	def nf(self) :
		ur"""Number of files to be generated in cycle.<br/>Default value: 24<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._nf
		except Exception as e:
			raise e

	@nf.setter
	def nf(self, nf) :
		ur"""Number of files to be generated in cycle.<br/>Default value: 24<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._nf = nf
		except Exception as e:
			raise e

	@property
	def time(self) :
		ur"""Time per file (sec).<br/>Default value: 3600<br/>Minimum length =  1.
		"""
		try :
			return self._time
		except Exception as e:
			raise e

	@time.setter
	def time(self, time) :
		ur"""Time per file (sec).<br/>Default value: 3600<br/>Minimum length =  1
		"""
		try :
			self._time = time
		except Exception as e:
			raise e

	@property
	def size(self) :
		ur"""Size of the captured data. Set 0 for full packet trace.<br/>Default value: 164<br/>Maximum length =  1514.
		"""
		try :
			return self._size
		except Exception as e:
			raise e

	@size.setter
	def size(self, size) :
		ur"""Size of the captured data. Set 0 for full packet trace.<br/>Default value: 164<br/>Maximum length =  1514
		"""
		try :
			self._size = size
		except Exception as e:
			raise e

	@property
	def mode(self) :
		ur"""Capturing mode for trace. Mode can be any of the following values or combination of these values:
		RX          Received packets before NIC pipelining (Filter does not work when RX capturing mode is ON)
		NEW_RX      Received packets after NIC pipelining
		TX          Transmitted packets
		TXB         Packets buffered for transmission
		IPV6        Translated IPv6 packets
		C2C         Capture C2C message
		NS_FR_TX    TX/TXB packets are not captured in flow receiver.
		Default mode: NEW_RX TXB .<br/>Default value: DEFAULT_MODE<br/>Possible values = TX, TXB, RX, IPV6, NEW_RX, C2C, NS_FR_TX.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		ur"""Capturing mode for trace. Mode can be any of the following values or combination of these values:
		RX          Received packets before NIC pipelining (Filter does not work when RX capturing mode is ON)
		NEW_RX      Received packets after NIC pipelining
		TX          Transmitted packets
		TXB         Packets buffered for transmission
		IPV6        Translated IPv6 packets
		C2C         Capture C2C message
		NS_FR_TX    TX/TXB packets are not captured in flow receiver.
		Default mode: NEW_RX TXB .<br/>Default value: DEFAULT_MODE<br/>Possible values = TX, TXB, RX, IPV6, NEW_RX, C2C, NS_FR_TX
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	@property
	def tcpdump(self) :
		ur"""Trace is captured in TCPDUMP(.pcap) format. Default capture format is NSTRACE(.cap).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpdump
		except Exception as e:
			raise e

	@tcpdump.setter
	def tcpdump(self, tcpdump) :
		ur"""Trace is captured in TCPDUMP(.pcap) format. Default capture format is NSTRACE(.cap).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tcpdump = tcpdump
		except Exception as e:
			raise e

	@property
	def pernic(self) :
		ur"""Use separate trace files for each interface. Works only with tcpdump format.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._pernic
		except Exception as e:
			raise e

	@pernic.setter
	def pernic(self, pernic) :
		ur"""Use separate trace files for each interface. Works only with tcpdump format.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._pernic = pernic
		except Exception as e:
			raise e

	@property
	def filename(self) :
		ur"""Name of the trace file.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		ur"""Name of the trace file.
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def fileid(self) :
		ur"""ID for the trace file name for uniqueness. Should be used only with -name option.
		"""
		try :
			return self._fileid
		except Exception as e:
			raise e

	@fileid.setter
	def fileid(self, fileid) :
		ur"""ID for the trace file name for uniqueness. Should be used only with -name option.
		"""
		try :
			self._fileid = fileid
		except Exception as e:
			raise e

	@property
	def filter(self) :
		ur"""Filter expression for nstrace. Maximum length of filter is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		nstrace supports two types of filter expressions:
		Classic Expressions:
		<expression> = the expression string in the format:
		<qualifier> <operator> <qualifier-value>
		<qualifier> = SOURCEIP.
		<qualifier-value> = A valid IP address
		<qualifier> = SOURCEPORT.
		<qualifier-value> = A valid port number.
		<qualifier> = DESTIP.
		<qualifier-value> = A valid IP address.
		<qualifier> = DESTPORT.
		<qualifier-value> = A valid port number.
		<qualifier> = IP.
		<qualifier-value> = A valid IP address.
		<qualifier> = PORT.
		<qualifier-value> = A valid port number.
		<qualifier> = SVCNAME.
		<qualifier-value> = The name of a service.
		<qualifier> = VSVRNAME.
		<qualifier-value> = The name of a vserver.
		<qualifier> = CONNID
		<qualifier-value> = A valid PCB dev number.
		<qualifier> = VLAN
		<qualifier-value> = A valid VLAN ID.
		<qualifier> = INTF
		<qualifier-value> = A valid interface id in the form of x/y 
		(n/x/y in case of cluster interface).
		<operator> = ( == | eq | != | neq | > | gt
		| < | lt | >= | ge | <= | le | BETWEEN )
		eg: start nstrace -filter "SOURCEIP == 10.102.34.201 || (SVCNAME != s1 && SOURCEPORT > 80)"
		The filter expression should be given in double quotes.
		Default Expressions:
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.SRCIP.EQ(127.0.0.1)
		<qualifier> = DSTIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.DSTIP.EQ(127.0.0.1)
		<qualifier> = IP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.IP.EQ(127.0.0.1)
		<qualifier> = SRCIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.SRCIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = DSTIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.DSTIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = IPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.IPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = SRCPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.SRCPORT.EQ(80)
		<qualifier> = DSTPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.DSTPORT.EQ(80)
		<qualifier> = PORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.PORT.EQ(80)
		<qualifier> = VLANID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid VLAN ID.
		example = CONNECTION.VLANID.EQ(0)
		<qualifier> = CONNID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid PCB dev number.
		example = CONNECTION.CONNID.EQ(0)
		<qualifier> = PPEID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid core ID.
		example = CONNECTION.PPEID.EQ(0)    
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH 
		| ENDSWITH ] 
		<qualifier-value>  = A valid text string.
		example = CONNECTION.SVCNAME.EQ("name")
		<qualifier> = LB_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = LB vserver name.
		example = CONNECTION.LB_VSERVER.NAME.EQ("name")
		<qualifier> = CS_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = CS vserver name.
		example = CONNECTION.CS_VSERVER.NAME.EQ("name")
		<qualifier> = INTF
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  =  A valid interface id in the
		form of x/y.
		example = CONNECTION.INTF.EQ("x/y")
		<qualifier> = SERVICE_TYPE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( SVC_HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | SVC_DNS | ADNS | SNMP | RTSP | DHCPRA | ANY|
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP |
		SVC_MYSQL | SVC_MSSQL | SERVICE_UNKNOWN )
		example = CONNECTION.SERVICE_TYPE.EQ(ANY)
		<qualifier> = TRAFFIC_DOMAIN_ID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid traffic domain ID.
		example = CONNECTION.TRAFFIC_DOMAIN_ID.EQ(0)
		eg: start nstrace -filter "CONNECTION.SRCIP.EQ(127.0.0.1) || (CONNECTION.SVCNAME.NE("s1") && CONNECTION.SRCPORT.EQ(80))"
		The filter expression should be given in double quotes. 
		common use cases:
		Trace capturing full sized traffic from/to ip 10.102.44.111, excluding loopback traffic
		start nstrace -size 0 -filter "CONNECTION.IP.NE(127.0.0.1) && CONNECTION.IP.EQ(10.102.44.111)"
		Trace capturing all traffic to (terminating at) port 80 or 443 
		start nstrace -size 0 -filter "CONNECTION.DSTPORT.EQ(443) || CONNECTION.DSTPORT.EQ(80)"
		Trace capturing all backend traffic specific to service service1 along with corresponding client side traffic
		start nstrace -size 0 -filter "CONNECTION.SVCNAME.EQ("service1")" -link ENABLED
		Trace capturing all traffic through NS interface 1/1
		start nstrace -filter "CONNECTION.INTF.EQ("1/1")"
		Trace capturing all traffic specific through vlan 2
		start nstrace -filter "CONNECTION.VLANID.EQ(2)"
		Trace capturing all frontend (client side) traffic specific to lb vserver vserver1 along with corresponding server side traffic
		start nstrace -size 0 -filter "CONNECTION.LB_VSERVER.NAME.EQ("vserver1")" -link ENABLED .
		"""
		try :
			return self._filter
		except Exception as e:
			raise e

	@filter.setter
	def filter(self, filter) :
		ur"""Filter expression for nstrace. Maximum length of filter is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		nstrace supports two types of filter expressions:
		Classic Expressions:
		<expression> = the expression string in the format:
		<qualifier> <operator> <qualifier-value>
		<qualifier> = SOURCEIP.
		<qualifier-value> = A valid IP address
		<qualifier> = SOURCEPORT.
		<qualifier-value> = A valid port number.
		<qualifier> = DESTIP.
		<qualifier-value> = A valid IP address.
		<qualifier> = DESTPORT.
		<qualifier-value> = A valid port number.
		<qualifier> = IP.
		<qualifier-value> = A valid IP address.
		<qualifier> = PORT.
		<qualifier-value> = A valid port number.
		<qualifier> = SVCNAME.
		<qualifier-value> = The name of a service.
		<qualifier> = VSVRNAME.
		<qualifier-value> = The name of a vserver.
		<qualifier> = CONNID
		<qualifier-value> = A valid PCB dev number.
		<qualifier> = VLAN
		<qualifier-value> = A valid VLAN ID.
		<qualifier> = INTF
		<qualifier-value> = A valid interface id in the form of x/y 
		(n/x/y in case of cluster interface).
		<operator> = ( == | eq | != | neq | > | gt
		| < | lt | >= | ge | <= | le | BETWEEN )
		eg: start nstrace -filter "SOURCEIP == 10.102.34.201 || (SVCNAME != s1 && SOURCEPORT > 80)"
		The filter expression should be given in double quotes.
		Default Expressions:
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.SRCIP.EQ(127.0.0.1)
		<qualifier> = DSTIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.DSTIP.EQ(127.0.0.1)
		<qualifier> = IP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address.
		example = CONNECTION.IP.EQ(127.0.0.1)
		<qualifier> = SRCIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.SRCIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = DSTIPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.DSTIPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = IPv6
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv6 address.
		example = CONNECTION.IPv6.EQ(2001:db8:0:0:1::1)
		<qualifier> = SRCPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.SRCPORT.EQ(80)
		<qualifier> = DSTPORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.DSTPORT.EQ(80)
		<qualifier> = PORT
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid port number.
		example = CONNECTION.PORT.EQ(80)
		<qualifier> = VLANID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid VLAN ID.
		example = CONNECTION.VLANID.EQ(0)
		<qualifier> = CONNID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid PCB dev number.
		example = CONNECTION.CONNID.EQ(0)
		<qualifier> = PPEID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid core ID.
		example = CONNECTION.PPEID.EQ(0)    
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH 
		| ENDSWITH ] 
		<qualifier-value>  = A valid text string.
		example = CONNECTION.SVCNAME.EQ("name")
		<qualifier> = LB_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = LB vserver name.
		example = CONNECTION.LB_VSERVER.NAME.EQ("name")
		<qualifier> = CS_VSERVER.NAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = CS vserver name.
		example = CONNECTION.CS_VSERVER.NAME.EQ("name")
		<qualifier> = INTF
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  =  A valid interface id in the
		form of x/y.
		example = CONNECTION.INTF.EQ("x/y")
		<qualifier> = SERVICE_TYPE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( SVC_HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | SVC_DNS | ADNS | SNMP | RTSP | DHCPRA | ANY|
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP |
		SVC_MYSQL | SVC_MSSQL | SERVICE_UNKNOWN )
		example = CONNECTION.SERVICE_TYPE.EQ(ANY)
		<qualifier> = TRAFFIC_DOMAIN_ID
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A valid traffic domain ID.
		example = CONNECTION.TRAFFIC_DOMAIN_ID.EQ(0)
		eg: start nstrace -filter "CONNECTION.SRCIP.EQ(127.0.0.1) || (CONNECTION.SVCNAME.NE("s1") && CONNECTION.SRCPORT.EQ(80))"
		The filter expression should be given in double quotes. 
		common use cases:
		Trace capturing full sized traffic from/to ip 10.102.44.111, excluding loopback traffic
		start nstrace -size 0 -filter "CONNECTION.IP.NE(127.0.0.1) && CONNECTION.IP.EQ(10.102.44.111)"
		Trace capturing all traffic to (terminating at) port 80 or 443 
		start nstrace -size 0 -filter "CONNECTION.DSTPORT.EQ(443) || CONNECTION.DSTPORT.EQ(80)"
		Trace capturing all backend traffic specific to service service1 along with corresponding client side traffic
		start nstrace -size 0 -filter "CONNECTION.SVCNAME.EQ("service1")" -link ENABLED
		Trace capturing all traffic through NS interface 1/1
		start nstrace -filter "CONNECTION.INTF.EQ("1/1")"
		Trace capturing all traffic specific through vlan 2
		start nstrace -filter "CONNECTION.VLANID.EQ(2)"
		Trace capturing all frontend (client side) traffic specific to lb vserver vserver1 along with corresponding server side traffic
		start nstrace -size 0 -filter "CONNECTION.LB_VSERVER.NAME.EQ("vserver1")" -link ENABLED .
		"""
		try :
			self._filter = filter
		except Exception as e:
			raise e

	@property
	def link(self) :
		ur"""Includes filtered connection's peer traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._link
		except Exception as e:
			raise e

	@link.setter
	def link(self, link) :
		ur"""Includes filtered connection's peer traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._link = link
		except Exception as e:
			raise e

	@property
	def nodes(self) :
		ur"""Nodes on which tracing is started.
		<br/>Maximum length =  32.
		"""
		try :
			return self._nodes
		except Exception as e:
			raise e

	@nodes.setter
	def nodes(self, nodes) :
		ur"""Nodes on which tracing is started.
		<br/>Maximum length =  32
		"""
		try :
			self._nodes = nodes
		except Exception as e:
			raise e

	@property
	def doruntimemerge(self) :
		ur"""Enable or disable runtime merge.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._doruntimemerge
		except Exception as e:
			raise e

	@doruntimemerge.setter
	def doruntimemerge(self, doruntimemerge) :
		ur"""Enable or disable runtime merge.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._doruntimemerge = doruntimemerge
		except Exception as e:
			raise e

	@property
	def doruntimecleanup(self) :
		ur"""Enable or disable runtime temp file cleanup.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._doruntimecleanup
		except Exception as e:
			raise e

	@doruntimecleanup.setter
	def doruntimecleanup(self, doruntimecleanup) :
		ur"""Enable or disable runtime temp file cleanup.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._doruntimecleanup = doruntimecleanup
		except Exception as e:
			raise e

	@property
	def tracebuffers(self) :
		ur"""Number of 16KB trace buffers.<br/>Default value: 5000<br/>Minimum length =  1000.
		"""
		try :
			return self._tracebuffers
		except Exception as e:
			raise e

	@tracebuffers.setter
	def tracebuffers(self, tracebuffers) :
		ur"""Number of 16KB trace buffers.<br/>Default value: 5000<br/>Minimum length =  1000
		"""
		try :
			self._tracebuffers = tracebuffers
		except Exception as e:
			raise e

	@property
	def skiprpc(self) :
		ur"""skip RPC packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skiprpc
		except Exception as e:
			raise e

	@skiprpc.setter
	def skiprpc(self, skiprpc) :
		ur"""skip RPC packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skiprpc = skiprpc
		except Exception as e:
			raise e

	@property
	def inmemorytrace(self) :
		ur"""Logs packets in appliance's memory and dumps the trace file on stopping the nstrace operation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._inmemorytrace
		except Exception as e:
			raise e

	@inmemorytrace.setter
	def inmemorytrace(self, inmemorytrace) :
		ur"""Logs packets in appliance's memory and dumps the trace file on stopping the nstrace operation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._inmemorytrace = inmemorytrace
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Current running state of trace.<br/>Default value: 0<br/>Possible values = RUNNING, STOPPED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def scope(self) :
		ur"""Scope of started trace, local or cluster level.<br/>Default value: 0<br/>Possible values = CLUSTER, LOCAL.
		"""
		try :
			return self._scope
		except Exception as e:
			raise e

	@property
	def tracelocation(self) :
		ur"""Directory where current trace files are saved.
		"""
		try :
			return self._tracelocation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstrace_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstrace
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nstrace resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nstrace()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Skiprpc:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mode:
		TX = "TX"
		TXB = "TXB"
		RX = "RX"
		IPV6 = "IPV6"
		NEW_RX = "NEW_RX"
		C2C = "C2C"
		NS_FR_TX = "NS_FR_TX"

	class State:
		RUNNING = "RUNNING"
		STOPPED = "STOPPED"

	class Scope:
		CLUSTER = "CLUSTER"
		LOCAL = "LOCAL"

	class Tcpdump:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Doruntimecleanup:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pernic:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Doruntimemerge:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Link:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Inmemorytrace:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nstrace_response(base_response) :
	def __init__(self, length=1) :
		self.nstrace = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstrace = [nstrace() for _ in range(length)]

