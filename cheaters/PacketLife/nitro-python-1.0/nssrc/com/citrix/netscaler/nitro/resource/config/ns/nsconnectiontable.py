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

class nsconnectiontable(base_resource) :
	""" Configuration for TCP/IP connection table resource. """
	def __init__(self) :
		self._filterexpression = ""
		self._link = False
		self._name = False
		self._detail = []
		self._sourceip = ""
		self._sourceport = 0
		self._destip = ""
		self._destport = 0
		self._svctype = ""
		self._idletime = 0
		self._state = ""
		self._linksourceip = ""
		self._linksourceport = 0
		self._linkdestip = ""
		self._linkdestport = 0
		self._linkservicetype = ""
		self._linkidletime = 0
		self._linkstate = ""
		self._entityname = ""
		self._linkentityname = ""
		self._connid = 0
		self._linkconnid = 0
		self._optionflags = []
		self._nswsvalue = 0
		self._peerwsvalue = 0
		self._mss = 0
		self._retxretrycnt = 0
		self._rcvwnd = 0
		self._advwnd = 0
		self._sndcwnd = 0
		self._iss = 0
		self._irs = 0
		self._rcvnxt = 0
		self._maxack = 0
		self._sndnxt = 0
		self._sndunack = 0
		self._httpendseq = 0
		self._httpstate = ""
		self._trcount = 0
		self._priority = ""
		self._httpreqver = ""
		self._httprequest = ""
		self._httprspcode = 0
		self._rttsmoothed = 0
		self._rttvariance = 0
		self._outoforderpkts = 0
		self._linkoptionflag = []
		self._linknswsvalue = 0
		self._linkpeerwsvalue = 0
		self._targetnodeidnnm = 0
		self._sourcenodeidnnm = 0
		self._channelidnnm = 0
		self._msgversionnnm = 0
		self._td = 0
		self.___count = 0

	@property
	def filterexpression(self) :
		ur"""The maximum length of filter expression is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		connectiontable supports two types of filter expressions:
		Classic Expressions:
		<expression> = the expression string in the format:
		<qualifier> <operator> <qualifier-value>
		<qualifier> = SOURCEIP.
		<qualifier-value> = A valid IP address.
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
		<qualifier> = IDLETIME.
		<qualifier-value> = A positive integer indicating the idle time.
		<qualifier> = SVCNAME.
		<qualifier-value> = The name of a service.
		<qualifier> = VSVRNAME.
		<qualifier-value> = The name of a vserver.
		<qualifier> = CONNID
		<qualifier-value> = A valid PCB dev number.
		<qualifier> = INTF
		<qualifier-value> = A valid interface id in the form of x/y
		(n/x/y in case of cluster interface).
		<qualifier> = VLAN
		<qualifier-value> = A valid VLAN ID.
		<qualifier> = STATE.
		<qualifier-value> = ( CLOSE_WAIT | CLOSED | CLOSING | ESTABLISHED |
		FIN_WAIT_1 | FIN_WAIT_2 | LAST_ACK | LISTEN |
		SYN_RECEIVED | SYN_SENT | TIME_WAIT )
		<qualifier> = SVCTYPE.
		<qualifier-value> = ( HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | DNS | ADNS | SNMP | RTSP | DHCPRA | ANY |
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP | MYSQL | MSSQL | UNKNOWN )
		<operator> = ( == | eq | != | neq | > | gt | < | lt | >= |
		ge | <= | le | BETWEEN )
		Default Expressions:
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address
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
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = service name.
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
		<qualifier-value>  = A valid interface id in the form of
		x/y (n/x/y in case of cluster interface).
		examle = CONNECTION.INTF.EQ("0/1/1")
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
		<qualifier> = IDLETIME
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A positive integer indicating the
		idletime.
		example = CONNECTION.IDLETIME.LT(100)
		<qualifier> = TCPSTATE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( CLOSE_WAIT | CLOSED | CLOSING |
		ESTABLISHED | FIN_WAIT_1 | FIN_WAIT_2 | LAST_ACK |
		LISTEN | SYN_RECEIVED | SYN_SENT | TIME_WAIT |
		NOT_APPLICABLE)
		example = CONNECTION.TCPSTATE.EQ(LISTEN)
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
		common usecases:
		Filtering out loopback connections and view present
		connections through netsclaer
		show connectiontable "CONNECTION.IP.NEQ(127.0.0.1) &&
		CONNECTION.TCPSTATE.EQ(ESTABLISHED)" -detail full
		show connections from a particular sourceip and targeted
		to port 80
		show connectiontable "CONNECTION.SRCIP.EQ(10.102.1.91) &&
		CONNECTION.DSTPORT.EQ(80)"
		show connection particular to a service and its linked
		client connections
		show connectiontable "CONNECTION.SVCNAME.EQ("S1")"
		-detail link
		show connections for a particular servicetype(e.g.http)
		show connectiontable "CONNECTION.SERVICE_TYPE.EQ(TCP)"
		viewing connections that have been idle for a long time
		show connectiontable "CONNECTION.IDLETIME.GT(100)"
		show connections for a particular interface and vlan
		show connectiontable "CONNECTION.INTF.EQ("1/1") &&
		CONNECTION.VLANID.EQ(1)"
		.
		"""
		try :
			return self._filterexpression
		except Exception as e:
			raise e

	@filterexpression.setter
	def filterexpression(self, filterexpression) :
		ur"""The maximum length of filter expression is 255 and it can be of following format:
		<expression> [<relop> <expression>]
		<relop> = ( && | || )
		connectiontable supports two types of filter expressions:
		Classic Expressions:
		<expression> = the expression string in the format:
		<qualifier> <operator> <qualifier-value>
		<qualifier> = SOURCEIP.
		<qualifier-value> = A valid IP address.
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
		<qualifier> = IDLETIME.
		<qualifier-value> = A positive integer indicating the idle time.
		<qualifier> = SVCNAME.
		<qualifier-value> = The name of a service.
		<qualifier> = VSVRNAME.
		<qualifier-value> = The name of a vserver.
		<qualifier> = CONNID
		<qualifier-value> = A valid PCB dev number.
		<qualifier> = INTF
		<qualifier-value> = A valid interface id in the form of x/y
		(n/x/y in case of cluster interface).
		<qualifier> = VLAN
		<qualifier-value> = A valid VLAN ID.
		<qualifier> = STATE.
		<qualifier-value> = ( CLOSE_WAIT | CLOSED | CLOSING | ESTABLISHED |
		FIN_WAIT_1 | FIN_WAIT_2 | LAST_ACK | LISTEN |
		SYN_RECEIVED | SYN_SENT | TIME_WAIT )
		<qualifier> = SVCTYPE.
		<qualifier-value> = ( HTTP | FTP | TCP | UDP | SSL |
		SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |
		RPCCLNT | DNS | ADNS | SNMP | RTSP | DHCPRA | ANY |
		MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP | MYSQL | MSSQL | UNKNOWN )
		<operator> = ( == | eq | != | neq | > | gt | < | lt | >= |
		ge | <= | le | BETWEEN )
		Default Expressions:
		<expression> =:
		CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)
		<qualifier> = SRCIP
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = A valid IPv4 address
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
		<qualifier> = SVCNAME
		<qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH
		| ENDSWITH ]
		<qualifier-value>  = service name.
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
		<qualifier-value>  = A valid interface id in the form of
		x/y (n/x/y in case of cluster interface).
		examle = CONNECTION.INTF.EQ("0/1/1")
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
		<qualifier> = IDLETIME
		<qualifier-method> = [ EQ | NE | GT | GE | LT | LE
		| BETWEEN ]
		<qualifier-value>  = A positive integer indicating the
		idletime.
		example = CONNECTION.IDLETIME.LT(100)
		<qualifier> = TCPSTATE
		<qualifier-method> = [ EQ | NE ]
		<qualifier-value>  = ( CLOSE_WAIT | CLOSED | CLOSING |
		ESTABLISHED | FIN_WAIT_1 | FIN_WAIT_2 | LAST_ACK |
		LISTEN | SYN_RECEIVED | SYN_SENT | TIME_WAIT |
		NOT_APPLICABLE)
		example = CONNECTION.TCPSTATE.EQ(LISTEN)
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
		common usecases:
		Filtering out loopback connections and view present
		connections through netsclaer
		show connectiontable "CONNECTION.IP.NEQ(127.0.0.1) &&
		CONNECTION.TCPSTATE.EQ(ESTABLISHED)" -detail full
		show connections from a particular sourceip and targeted
		to port 80
		show connectiontable "CONNECTION.SRCIP.EQ(10.102.1.91) &&
		CONNECTION.DSTPORT.EQ(80)"
		show connection particular to a service and its linked
		client connections
		show connectiontable "CONNECTION.SVCNAME.EQ("S1")"
		-detail link
		show connections for a particular servicetype(e.g.http)
		show connectiontable "CONNECTION.SERVICE_TYPE.EQ(TCP)"
		viewing connections that have been idle for a long time
		show connectiontable "CONNECTION.IDLETIME.GT(100)"
		show connections for a particular interface and vlan
		show connectiontable "CONNECTION.INTF.EQ("1/1") &&
		CONNECTION.VLANID.EQ(1)"
		.
		"""
		try :
			self._filterexpression = filterexpression
		except Exception as e:
			raise e

	@property
	def link(self) :
		ur"""Display link information if available.
		"""
		try :
			return self._link
		except Exception as e:
			raise e

	@link.setter
	def link(self, link) :
		ur"""Display link information if available.
		"""
		try :
			self._link = link
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Display name instead of IP for local entities.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Display name instead of IP for local entities.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def detail(self) :
		ur"""Specify display options for the connection table.
		* LINK - Displays the linked PCB (Protocol Control Block).
		* NAME - Displays along with the service name.
		* CONNFAILOVER - Displays PCB with connection failover.
		* FULL - Displays all available details.<br/>Possible values = LINK, NAME, CONNFAILOVER, FULL, NNM.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		ur"""Specify display options for the connection table.
		* LINK - Displays the linked PCB (Protocol Control Block).
		* NAME - Displays along with the service name.
		* CONNFAILOVER - Displays PCB with connection failover.
		* FULL - Displays all available details.<br/>Possible values = LINK, NAME, CONNFAILOVER, FULL, NNM
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

	@property
	def sourceip(self) :
		ur"""Source IP of the connection.
		"""
		try :
			return self._sourceip
		except Exception as e:
			raise e

	@property
	def sourceport(self) :
		ur"""Source port of the connection.<br/>Range 1 - 65535.
		"""
		try :
			return self._sourceport
		except Exception as e:
			raise e

	@property
	def destip(self) :
		ur"""Destination IP of the connection.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		ur"""Destination port of the connection.<br/>Range 1 - 65535.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@property
	def svctype(self) :
		ur"""Protocol supported by the connection.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, DNS_TCP, ADNS_TCP, HTTPSVR, HTTPCLIENT, NAT, HA, AAA, SINCTCP, VPN AFTP, MONITORS, SSLVPN UDP, SINCUDP, RIP, UDP CLNT, SASP, RPCCLNTS, ROUTE, AUDIT, STA HTTP, STA SSL, DNS RESOLVE, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE, ICA, RADIUS, TFTP_DATA.
		"""
		try :
			return self._svctype
		except Exception as e:
			raise e

	@property
	def idletime(self) :
		ur"""Time since last activity was detected on the connection.
		"""
		try :
			return self._idletime
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Current TCP/IP state of the connection.<br/>Possible values = CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, CLOSE_WAIT, FIN_WAIT_1, CLOSING, LAST_ACK, FIN_WAIT_2, TIME_WAIT, NA.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def linksourceip(self) :
		ur"""Source IP of the link connection.
		"""
		try :
			return self._linksourceip
		except Exception as e:
			raise e

	@property
	def linksourceport(self) :
		ur"""Source port of the link connection.<br/>Range 1 - 65535.
		"""
		try :
			return self._linksourceport
		except Exception as e:
			raise e

	@property
	def linkdestip(self) :
		ur"""Destination IP of the link connection.
		"""
		try :
			return self._linkdestip
		except Exception as e:
			raise e

	@property
	def linkdestport(self) :
		ur"""Destination port of the link connection.<br/>Range 1 - 65535.
		"""
		try :
			return self._linkdestport
		except Exception as e:
			raise e

	@property
	def linkservicetype(self) :
		ur"""Protocol supported by the link connection.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, DNS_TCP, ADNS_TCP, HTTPSVR, HTTPCLIENT, NAT, HA, AAA, SINCTCP, VPN AFTP, MONITORS, SSLVPN UDP, SINCUDP, RIP, UDP CLNT, SASP, RPCCLNTS, ROUTE, AUDIT, STA HTTP, STA SSL, DNS RESOLVE, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE, ICA, RADIUS, TFTP_DATA.
		"""
		try :
			return self._linkservicetype
		except Exception as e:
			raise e

	@property
	def linkidletime(self) :
		ur"""Time since last activity was detected on link connection.
		"""
		try :
			return self._linkidletime
		except Exception as e:
			raise e

	@property
	def linkstate(self) :
		ur"""TCP/IP current state of link connection.<br/>Possible values = CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, CLOSE_WAIT, FIN_WAIT_1, CLOSING, LAST_ACK, FIN_WAIT_2, TIME_WAIT, NA.
		"""
		try :
			return self._linkstate
		except Exception as e:
			raise e

	@property
	def entityname(self) :
		ur"""NetScaler entity name for the connection.
		"""
		try :
			return self._entityname
		except Exception as e:
			raise e

	@property
	def linkentityname(self) :
		ur"""NetScaler entity name for link connection.
		"""
		try :
			return self._linkentityname
		except Exception as e:
			raise e

	@property
	def connid(self) :
		ur"""Unique transaction number for the connection.
		"""
		try :
			return self._connid
		except Exception as e:
			raise e

	@property
	def linkconnid(self) :
		ur"""Unique transaction number for the peer connection.
		"""
		try :
			return self._linkconnid
		except Exception as e:
			raise e

	@property
	def optionflags(self) :
		ur"""flags used to store TCP options like Sack, WS.<br/>Possible values = sack, timstmp, ws.
		"""
		try :
			return self._optionflags
		except Exception as e:
			raise e

	@property
	def nswsvalue(self) :
		ur"""netscaler window scaling value.
		"""
		try :
			return self._nswsvalue
		except Exception as e:
			raise e

	@property
	def peerwsvalue(self) :
		ur"""peer window scaling value.
		"""
		try :
			return self._peerwsvalue
		except Exception as e:
			raise e

	@property
	def mss(self) :
		ur"""Client side MSS for the connection - used in server SYN.
		"""
		try :
			return self._mss
		except Exception as e:
			raise e

	@property
	def retxretrycnt(self) :
		ur"""Retransmission retry count for the connection.
		"""
		try :
			return self._retxretrycnt
		except Exception as e:
			raise e

	@property
	def rcvwnd(self) :
		ur"""Received Advertised Window for the connection.
		"""
		try :
			return self._rcvwnd
		except Exception as e:
			raise e

	@property
	def advwnd(self) :
		ur"""Sent advertised window for the connection.
		"""
		try :
			return self._advwnd
		except Exception as e:
			raise e

	@property
	def sndcwnd(self) :
		ur"""sent congestion window for the connection.
		"""
		try :
			return self._sndcwnd
		except Exception as e:
			raise e

	@property
	def iss(self) :
		ur"""Initial send sequence number for the connection.
		"""
		try :
			return self._iss
		except Exception as e:
			raise e

	@property
	def irs(self) :
		ur"""Initial receive sequence number for the connection.
		"""
		try :
			return self._irs
		except Exception as e:
			raise e

	@property
	def rcvnxt(self) :
		ur"""next expecting seq number for the connection.
		"""
		try :
			return self._rcvnxt
		except Exception as e:
			raise e

	@property
	def maxack(self) :
		ur"""current running max ack sent for the connection.
		"""
		try :
			return self._maxack
		except Exception as e:
			raise e

	@property
	def sndnxt(self) :
		ur"""next bytes seq number for the connection.
		"""
		try :
			return self._sndnxt
		except Exception as e:
			raise e

	@property
	def sndunack(self) :
		ur"""Most recently received ACK for the connection.
		"""
		try :
			return self._sndunack
		except Exception as e:
			raise e

	@property
	def httpendseq(self) :
		ur"""HTTP parsing tracking seq number for the connection.
		"""
		try :
			return self._httpendseq
		except Exception as e:
			raise e

	@property
	def httpstate(self) :
		ur"""HTTP Protocol  state for the connection.<br/>Possible values = INITIALIZED, CONTENT_LENGTH, CHUNKED, WAIT_FINAL_ACK, UNKNOWN, DONE, WAIT_FIN.
		"""
		try :
			return self._httpstate
		except Exception as e:
			raise e

	@property
	def trcount(self) :
		ur"""Max reuests allowed per connection.
		"""
		try :
			return self._trcount
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""priority of the connection.<br/>Possible values = SC Priority, Priority queue1, priority queue2, priority queue3, DoS Priority, Surge Priority.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def httpreqver(self) :
		ur"""current HTTP request version on the connection.<br/>Possible values = HTTP_1_0, HTTP_1_1, HTTP_0_9, RTSP_1_0, SIP_2_0, VPN_ICA_SOCKS, VPN_ICA_CGP.
		"""
		try :
			return self._httpreqver
		except Exception as e:
			raise e

	@property
	def httprequest(self) :
		ur"""current HTTP request type on the connection.<br/>Possible values = OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT, RPCCONNECT.
		"""
		try :
			return self._httprequest
		except Exception as e:
			raise e

	@property
	def httprspcode(self) :
		ur"""current response type on the connection.
		"""
		try :
			return self._httprspcode
		except Exception as e:
			raise e

	@property
	def rttsmoothed(self) :
		ur"""smoothed RTT value of the connection.
		"""
		try :
			return self._rttsmoothed
		except Exception as e:
			raise e

	@property
	def rttvariance(self) :
		ur"""RTT variance for the connection.
		"""
		try :
			return self._rttvariance
		except Exception as e:
			raise e

	@property
	def outoforderpkts(self) :
		ur"""held packets on the connection.
		"""
		try :
			return self._outoforderpkts
		except Exception as e:
			raise e

	@property
	def linkoptionflag(self) :
		ur"""Link connection's TCP option flag for Sack and WS.<br/>Possible values = sack, timstmp, ws.
		"""
		try :
			return self._linkoptionflag
		except Exception as e:
			raise e

	@property
	def linknswsvalue(self) :
		ur"""Link connection-s netscaler window scaling value.
		"""
		try :
			return self._linknswsvalue
		except Exception as e:
			raise e

	@property
	def linkpeerwsvalue(self) :
		ur"""Link connection-s peer netscaler window scaling value.
		"""
		try :
			return self._linkpeerwsvalue
		except Exception as e:
			raise e

	@property
	def targetnodeidnnm(self) :
		ur"""NNM connection target node ID.
		"""
		try :
			return self._targetnodeidnnm
		except Exception as e:
			raise e

	@property
	def sourcenodeidnnm(self) :
		ur"""NNM connection source node ID.
		"""
		try :
			return self._sourcenodeidnnm
		except Exception as e:
			raise e

	@property
	def channelidnnm(self) :
		ur"""NNM connection channel ID.
		"""
		try :
			return self._channelidnnm
		except Exception as e:
			raise e

	@property
	def msgversionnnm(self) :
		ur"""nnm message version.
		"""
		try :
			return self._msgversionnnm
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Traffic Domain Id.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsconnectiontable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsconnectiontable
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
		ur""" Use this API to fetch all the nsconnectiontable resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsconnectiontable()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the nsconnectiontable resources that are configured on netscaler.
	# This uses nsconnectiontable_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nsconnectiontable resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nsconnectiontable resources configured on NetScaler.
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of nsconnectiontable resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsconnectiontable()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Priority:
		SC_Priority = "SC Priority"
		Priority_queue1 = "Priority queue1"
		priority_queue2 = "priority queue2"
		priority_queue3 = "priority queue3"
		DoS_Priority = "DoS Priority"
		Surge_Priority = "Surge Priority"

	class Linkoptionflag:
		sack = "sack"
		timstmp = "timstmp"
		ws = "ws"

	class State:
		CLOSED = "CLOSED"
		LISTEN = "LISTEN"
		SYN_SENT = "SYN_SENT"
		SYN_RECEIVED = "SYN_RECEIVED"
		ESTABLISHED = "ESTABLISHED"
		CLOSE_WAIT = "CLOSE_WAIT"
		FIN_WAIT_1 = "FIN_WAIT_1"
		CLOSING = "CLOSING"
		LAST_ACK = "LAST_ACK"
		FIN_WAIT_2 = "FIN_WAIT_2"
		TIME_WAIT = "TIME_WAIT"
		NA = "NA"

	class Svctype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
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
		HTTPSVR = "HTTPSVR"
		HTTPCLIENT = "HTTPCLIENT"
		NAT = "NAT"
		HA = "HA"
		AAA = "AAA"
		SINCTCP = "SINCTCP"
		VPN_AFTP = "VPN AFTP"
		MONITORS = "MONITORS"
		SSLVPN_UDP = "SSLVPN UDP"
		SINCUDP = "SINCUDP"
		RIP = "RIP"
		UDP_CLNT = "UDP CLNT"
		SASP = "SASP"
		RPCCLNTS = "RPCCLNTS"
		ROUTE = "ROUTE"
		AUDIT = "AUDIT"
		STA_HTTP = "STA HTTP"
		STA_SSL = "STA SSL"
		DNS_RESOLVE = "DNS RESOLVE"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"
		ICA = "ICA"
		RADIUS = "RADIUS"
		TFTP_DATA = "TFTP_DATA"

	class Httpreqver:
		HTTP_1_0 = "HTTP_1_0"
		HTTP_1_1 = "HTTP_1_1"
		HTTP_0_9 = "HTTP_0_9"
		RTSP_1_0 = "RTSP_1_0"
		SIP_2_0 = "SIP_2_0"
		VPN_ICA_SOCKS = "VPN_ICA_SOCKS"
		VPN_ICA_CGP = "VPN_ICA_CGP"

	class Httprequest:
		OPTIONS = "OPTIONS"
		GET = "GET"
		HEAD = "HEAD"
		POST = "POST"
		PUT = "PUT"
		DELETE = "DELETE"
		TRACE = "TRACE"
		CONNECT = "CONNECT"
		RPCCONNECT = "RPCCONNECT"

	class Httpstate:
		INITIALIZED = "INITIALIZED"
		CONTENT_LENGTH = "CONTENT_LENGTH"
		CHUNKED = "CHUNKED"
		WAIT_FINAL_ACK = "WAIT_FINAL_ACK"
		UNKNOWN = "UNKNOWN"
		DONE = "DONE"
		WAIT_FIN = "WAIT_FIN"

	class Linkstate:
		CLOSED = "CLOSED"
		LISTEN = "LISTEN"
		SYN_SENT = "SYN_SENT"
		SYN_RECEIVED = "SYN_RECEIVED"
		ESTABLISHED = "ESTABLISHED"
		CLOSE_WAIT = "CLOSE_WAIT"
		FIN_WAIT_1 = "FIN_WAIT_1"
		CLOSING = "CLOSING"
		LAST_ACK = "LAST_ACK"
		FIN_WAIT_2 = "FIN_WAIT_2"
		TIME_WAIT = "TIME_WAIT"
		NA = "NA"

	class Optionflags:
		sack = "sack"
		timstmp = "timstmp"
		ws = "ws"

	class Detail:
		LINK = "LINK"
		NAME = "NAME"
		CONNFAILOVER = "CONNFAILOVER"
		FULL = "FULL"
		NNM = "NNM"

	class Linkservicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
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
		HTTPSVR = "HTTPSVR"
		HTTPCLIENT = "HTTPCLIENT"
		NAT = "NAT"
		HA = "HA"
		AAA = "AAA"
		SINCTCP = "SINCTCP"
		VPN_AFTP = "VPN AFTP"
		MONITORS = "MONITORS"
		SSLVPN_UDP = "SSLVPN UDP"
		SINCUDP = "SINCUDP"
		RIP = "RIP"
		UDP_CLNT = "UDP CLNT"
		SASP = "SASP"
		RPCCLNTS = "RPCCLNTS"
		ROUTE = "ROUTE"
		AUDIT = "AUDIT"
		STA_HTTP = "STA HTTP"
		STA_SSL = "STA SSL"
		DNS_RESOLVE = "DNS RESOLVE"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"
		ICA = "ICA"
		RADIUS = "RADIUS"
		TFTP_DATA = "TFTP_DATA"

class nsconnectiontable_response(base_response) :
	def __init__(self, length=1) :
		self.nsconnectiontable = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsconnectiontable = [nsconnectiontable() for _ in range(length)]

