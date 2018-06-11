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


class nsconnectiontable_args :
	ur""" Provides additional arguments required for fetching the nsconnectiontable resource.
	"""
	def __init__(self) :
		self._filterexpression = ""
		self._link = False
		self._name = False
		self._detail = []

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

	class Detail:
		LINK = "LINK"
		NAME = "NAME"
		CONNFAILOVER = "CONNFAILOVER"
		FULL = "FULL"
		NNM = "NNM"

