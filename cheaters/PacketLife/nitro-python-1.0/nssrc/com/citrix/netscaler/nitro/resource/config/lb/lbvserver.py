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

class lbvserver(base_resource) :
	""" Configuration for Load Balancing Virtual Server resource. """
	def __init__(self) :
		self._name = ""
		self._servicetype = ""
		self._ipv46 = ""
		self._ippattern = ""
		self._ipmask = ""
		self._port = 0
		self._range = 0
		self._persistencetype = ""
		self._timeout = 0
		self._persistencebackup = ""
		self._backuppersistencetimeout = 0
		self._lbmethod = ""
		self._hashlength = 0
		self._netmask = ""
		self._v6netmasklen = 0
		self._cookiename = ""
		self._rule = ""
		self._listenpolicy = ""
		self._listenpriority = 0
		self._resrule = ""
		self._persistmask = ""
		self._v6persistmasklen = 0
		self._pq = ""
		self._sc = ""
		self._rtspnat = ""
		self._m = ""
		self._tosid = 0
		self._datalength = 0
		self._dataoffset = 0
		self._sessionless = ""
		self._state = ""
		self._connfailover = ""
		self._redirurl = ""
		self._cacheable = ""
		self._clttimeout = 0
		self._somethod = ""
		self._sopersistence = ""
		self._sopersistencetimeout = 0
		self._healththreshold = 0
		self._sothreshold = 0
		self._sobackupaction = ""
		self._redirectportrewrite = ""
		self._downstateflush = ""
		self._backupvserver = ""
		self._disableprimaryondown = ""
		self._insertvserveripport = ""
		self._vipheader = ""
		self._authenticationhost = ""
		self._authentication = ""
		self._authn401 = ""
		self._authnvsname = ""
		self._push = ""
		self._pushvserver = ""
		self._pushlabel = ""
		self._pushmulticlients = ""
		self._tcpprofilename = ""
		self._httpprofilename = ""
		self._dbprofilename = ""
		self._comment = ""
		self._l2conn = ""
		self._oracleserverversion = ""
		self._mssqlserverversion = ""
		self._mysqlprotocolversion = 0
		self._mysqlserverversion = ""
		self._mysqlcharacterset = 0
		self._mysqlservercapabilities = 0
		self._appflowlog = ""
		self._netprofile = ""
		self._icmpvsrresponse = ""
		self._rhistate = ""
		self._newservicerequest = 0
		self._newservicerequestunit = ""
		self._newservicerequestincrementinterval = 0
		self._minautoscalemembers = 0
		self._maxautoscalemembers = 0
		self._persistavpno = []
		self._skippersistency = ""
		self._td = 0
		self._authnprofile = ""
		self._macmoderetainvlan = ""
		self._dbslb = ""
		self._dns64 = ""
		self._bypassaaaa = ""
		self._recursionavailable = ""
		self._processlocal = ""
		self._weight = 0
		self._servicename = ""
		self._redirurlflags = False
		self._newname = ""
		self._value = ""
		self._ipmapping = ""
		self._ngname = ""
		self._type = ""
		self._curstate = ""
		self._effectivestate = ""
		self._status = 0
		self._lbrrreason = 0
		self._redirect = ""
		self._precedence = ""
		self._homepage = ""
		self._dnsvservername = ""
		self._domain = ""
		self._policyname = ""
		self._cachevserver = ""
		self._health = 0
		self._gotopriorityexpression = ""
		self._ruletype = 0
		self._groupname = ""
		self._cookiedomain = ""
		self._map = ""
		self._gt2gb = ""
		self._consolidatedlconn = ""
		self._consolidatedlconngbl = ""
		self._thresholdvalue = 0
		self._bindpoint = ""
		self._invoke = False
		self._labeltype = ""
		self._labelname = ""
		self._version = 0
		self._totalservices = 0
		self._activeservices = 0
		self._statechangetimesec = ""
		self._statechangetimeseconds = 0
		self._statechangetimemsec = 0
		self._tickssincelaststatechange = 0
		self._isgslb = False
		self._vsvrdynconnsothreshold = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		ur"""Protocol used by the service (also called the service type).<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, DNS, DHCPRA, ANY, SIP_UDP, DNS_TCP, RTSP, PUSH, SSL_PUSH, RADIUS, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		ur"""Protocol used by the service (also called the service type).<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, DNS, DHCPRA, ANY, SIP_UDP, DNS_TCP, RTSP, PUSH, SSL_PUSH, RADIUS, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def ipv46(self) :
		ur"""IPv4 or IPv6 address to assign to the virtual server.
		"""
		try :
			return self._ipv46
		except Exception as e:
			raise e

	@ipv46.setter
	def ipv46(self, ipv46) :
		ur"""IPv4 or IPv6 address to assign to the virtual server.
		"""
		try :
			self._ipv46 = ipv46
		except Exception as e:
			raise e

	@property
	def ippattern(self) :
		ur"""IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern.  Mutually exclusive with the IP Address parameter. 
		For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254.  You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).
		If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if virtual servers vs1 and vs2 have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.
		"""
		try :
			return self._ippattern
		except Exception as e:
			raise e

	@ippattern.setter
	def ippattern(self, ippattern) :
		ur"""IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern.  Mutually exclusive with the IP Address parameter. 
		For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254.  You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).
		If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if virtual servers vs1 and vs2 have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.
		"""
		try :
			self._ippattern = ippattern
		except Exception as e:
			raise e

	@property
	def ipmask(self) :
		ur"""IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
		"""
		try :
			return self._ipmask
		except Exception as e:
			raise e

	@ipmask.setter
	def ipmask(self, ipmask) :
		ur"""IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
		"""
		try :
			self._ipmask = ipmask
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port number for the virtual server.<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""Port number for the virtual server.<br/>Range 1 - 65535
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def range(self) :
		ur"""Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual server then functions as a network virtual server, accepting traffic on any of the generated IP addresses. The IP addresses are generated automatically, as follows: 
		* For a range of n, the last octet of the address specified by the IP Address parameter increments n-1 times. 
		* If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1.
		Note: The Range parameter assigns multiple IP addresses to one virtual server. To generate an array of virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name parameters to specify the range. For example:
		add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254.
		"""
		try :
			return self._range
		except Exception as e:
			raise e

	@range.setter
	def range(self, range) :
		ur"""Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual server then functions as a network virtual server, accepting traffic on any of the generated IP addresses. The IP addresses are generated automatically, as follows: 
		* For a range of n, the last octet of the address specified by the IP Address parameter increments n-1 times. 
		* If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1.
		Note: The Range parameter assigns multiple IP addresses to one virtual server. To generate an array of virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name parameters to specify the range. For example:
		add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254
		"""
		try :
			self._range = range
		except Exception as e:
			raise e

	@property
	def persistencetype(self) :
		ur"""Type of persistence for the virtual server. Available settings function as follows:
		* SOURCEIP - Connections from the same client IP address belong to the same persistence session.
		* COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from a server, belong to the same persistence session. 
		* SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session.
		* CUSTOMSERVERID - Connections with the same server ID form part of the same session. For this persistence type, set the Server ID (CustomServerID) parameter for each service and configure the Rule parameter to identify the server ID in a request.
		* RULE - All connections that match a user defined rule belong to the same persistence session. 
		* URLPASSIVE - Requests that have the same server ID in the URL query belong to the same persistence session. The server ID is the hexadecimal representation of the IP address and port of the service to which the request must be forwarded. This persistence type requires a rule to identify the server ID in the request. 
		* DESTIP - Connections to the same destination IP address belong to the same persistence session.
		* SRCIPDESTIP - Connections that have the same source IP address and destination IP address belong to the same persistence session.
		* CALLID - Connections that have the same CALL-ID SIP header belong to the same persistence session.
		* RTSPSID - Connections that have the same RTSP Session ID belong to the same persistence session.<br/>Possible values = SOURCEIP, COOKIEINSERT, SSLSESSION, RULE, URLPASSIVE, CUSTOMSERVERID, DESTIP, SRCIPDESTIP, CALLID, RTSPSID, DIAMETER, NONE.
		"""
		try :
			return self._persistencetype
		except Exception as e:
			raise e

	@persistencetype.setter
	def persistencetype(self, persistencetype) :
		ur"""Type of persistence for the virtual server. Available settings function as follows:
		* SOURCEIP - Connections from the same client IP address belong to the same persistence session.
		* COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from a server, belong to the same persistence session. 
		* SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session.
		* CUSTOMSERVERID - Connections with the same server ID form part of the same session. For this persistence type, set the Server ID (CustomServerID) parameter for each service and configure the Rule parameter to identify the server ID in a request.
		* RULE - All connections that match a user defined rule belong to the same persistence session. 
		* URLPASSIVE - Requests that have the same server ID in the URL query belong to the same persistence session. The server ID is the hexadecimal representation of the IP address and port of the service to which the request must be forwarded. This persistence type requires a rule to identify the server ID in the request. 
		* DESTIP - Connections to the same destination IP address belong to the same persistence session.
		* SRCIPDESTIP - Connections that have the same source IP address and destination IP address belong to the same persistence session.
		* CALLID - Connections that have the same CALL-ID SIP header belong to the same persistence session.
		* RTSPSID - Connections that have the same RTSP Session ID belong to the same persistence session.<br/>Possible values = SOURCEIP, COOKIEINSERT, SSLSESSION, RULE, URLPASSIVE, CUSTOMSERVERID, DESTIP, SRCIPDESTIP, CALLID, RTSPSID, DIAMETER, NONE
		"""
		try :
			self._persistencetype = persistencetype
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		ur"""Time period for which a persistence session is in effect.<br/>Default value: 2<br/>Maximum length =  1440.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		ur"""Time period for which a persistence session is in effect.<br/>Default value: 2<br/>Maximum length =  1440
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def persistencebackup(self) :
		ur"""Backup persistence type for the virtual server. Becomes operational if the primary persistence mechanism fails.<br/>Possible values = SOURCEIP, NONE.
		"""
		try :
			return self._persistencebackup
		except Exception as e:
			raise e

	@persistencebackup.setter
	def persistencebackup(self, persistencebackup) :
		ur"""Backup persistence type for the virtual server. Becomes operational if the primary persistence mechanism fails.<br/>Possible values = SOURCEIP, NONE
		"""
		try :
			self._persistencebackup = persistencebackup
		except Exception as e:
			raise e

	@property
	def backuppersistencetimeout(self) :
		ur"""Time period for which backup persistence is in effect.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._backuppersistencetimeout
		except Exception as e:
			raise e

	@backuppersistencetimeout.setter
	def backuppersistencetimeout(self, backuppersistencetimeout) :
		ur"""Time period for which backup persistence is in effect.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._backuppersistencetimeout = backuppersistencetimeout
		except Exception as e:
			raise e

	@property
	def lbmethod(self) :
		ur"""Load balancing method.  The available settings function as follows:
		* ROUNDROBIN - Distribute requests in rotation, regardless of the load. Weights can be assigned to services to enforce weighted round robin distribution.
		* LEASTCONNECTION (default) - Select the service with the fewest connections. 
		* LEASTRESPONSETIME - Select the service with the lowest average response time. 
		* LEASTBANDWIDTH - Select the service currently handling the least traffic.
		* LEASTPACKETS - Select the service currently serving the lowest number of packets per second.
		* CUSTOMLOAD - Base service selection on the SNMP metrics obtained by custom load monitors.
		* LRTM - Select the service with the lowest response time. Response times are learned through monitoring probes. This method also takes the number of active connections into account.
		Also available are a number of hashing methods, in which the appliance extracts a predetermined portion of the request, creates a hash of the portion, and then checks whether any previous requests had the same hash value. If it finds a match, it forwards the request to the service that served those previous requests. Following are the hashing methods: 
		* URLHASH - Create a hash of the request URL (or part of the URL).
		* DOMAINHASH - Create a hash of the domain name in the request (or part of the domain name). The domain name is taken from either the URL or the Host header. If the domain name appears in both locations, the URL is preferred. If the request does not contain a domain name, the load balancing method defaults to LEASTCONNECTION.
		* DESTINATIONIPHASH - Create a hash of the destination IP address in the IP header. 
		* SOURCEIPHASH - Create a hash of the source IP address in the IP header.  
		* TOKEN - Extract a token from the request, create a hash of the token, and then select the service to which any previous requests with the same token hash value were sent. 
		* SRCIPDESTIPHASH - Create a hash of the string obtained by concatenating the source IP address and destination IP address in the IP header.  
		* SRCIPSRCPORTHASH - Create a hash of the source IP address and source port in the IP header.  
		* CALLIDHASH - Create a hash of the SIP Call-ID header.<br/>Default value: LEASTCONNECTION<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, URLHASH, DOMAINHASH, DESTINATIONIPHASH, SOURCEIPHASH, SRCIPDESTIPHASH, LEASTBANDWIDTH, LEASTPACKETS, TOKEN, SRCIPSRCPORTHASH, LRTM, CALLIDHASH, CUSTOMLOAD, LEASTREQUEST.
		"""
		try :
			return self._lbmethod
		except Exception as e:
			raise e

	@lbmethod.setter
	def lbmethod(self, lbmethod) :
		ur"""Load balancing method.  The available settings function as follows:
		* ROUNDROBIN - Distribute requests in rotation, regardless of the load. Weights can be assigned to services to enforce weighted round robin distribution.
		* LEASTCONNECTION (default) - Select the service with the fewest connections. 
		* LEASTRESPONSETIME - Select the service with the lowest average response time. 
		* LEASTBANDWIDTH - Select the service currently handling the least traffic.
		* LEASTPACKETS - Select the service currently serving the lowest number of packets per second.
		* CUSTOMLOAD - Base service selection on the SNMP metrics obtained by custom load monitors.
		* LRTM - Select the service with the lowest response time. Response times are learned through monitoring probes. This method also takes the number of active connections into account.
		Also available are a number of hashing methods, in which the appliance extracts a predetermined portion of the request, creates a hash of the portion, and then checks whether any previous requests had the same hash value. If it finds a match, it forwards the request to the service that served those previous requests. Following are the hashing methods: 
		* URLHASH - Create a hash of the request URL (or part of the URL).
		* DOMAINHASH - Create a hash of the domain name in the request (or part of the domain name). The domain name is taken from either the URL or the Host header. If the domain name appears in both locations, the URL is preferred. If the request does not contain a domain name, the load balancing method defaults to LEASTCONNECTION.
		* DESTINATIONIPHASH - Create a hash of the destination IP address in the IP header. 
		* SOURCEIPHASH - Create a hash of the source IP address in the IP header.  
		* TOKEN - Extract a token from the request, create a hash of the token, and then select the service to which any previous requests with the same token hash value were sent. 
		* SRCIPDESTIPHASH - Create a hash of the string obtained by concatenating the source IP address and destination IP address in the IP header.  
		* SRCIPSRCPORTHASH - Create a hash of the source IP address and source port in the IP header.  
		* CALLIDHASH - Create a hash of the SIP Call-ID header.<br/>Default value: LEASTCONNECTION<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, URLHASH, DOMAINHASH, DESTINATIONIPHASH, SOURCEIPHASH, SRCIPDESTIPHASH, LEASTBANDWIDTH, LEASTPACKETS, TOKEN, SRCIPSRCPORTHASH, LRTM, CALLIDHASH, CUSTOMLOAD, LEASTREQUEST
		"""
		try :
			self._lbmethod = lbmethod
		except Exception as e:
			raise e

	@property
	def hashlength(self) :
		ur"""Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing methods.<br/>Default value: 80<br/>Minimum length =  1<br/>Maximum length =  4096.
		"""
		try :
			return self._hashlength
		except Exception as e:
			raise e

	@hashlength.setter
	def hashlength(self, hashlength) :
		ur"""Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing methods.<br/>Default value: 80<br/>Minimum length =  1<br/>Maximum length =  4096
		"""
		try :
			self._hashlength = hashlength
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing method is DESTINATIONIPHASH or SOURCEIPHASH.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing method is DESTINATIONIPHASH or SOURCEIPHASH.<br/>Minimum length =  1
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def v6netmasklen(self) :
		ur"""Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is required by the DESTINATIONIPHASH and SOURCEIPHASH load balancing methods.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6netmasklen
		except Exception as e:
			raise e

	@v6netmasklen.setter
	def v6netmasklen(self, v6netmasklen) :
		ur"""Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is required by the DESTINATIONIPHASH and SOURCEIPHASH load balancing methods.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6netmasklen = v6netmasklen
		except Exception as e:
			raise e

	@property
	def cookiename(self) :
		ur"""Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
		"""
		try :
			return self._cookiename
		except Exception as e:
			raise e

	@cookiename.setter
	def cookiename(self, cookiename) :
		ur"""Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
		"""
		try :
			self._cookiename = cookiename
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Default value: "none".
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Default value: "none"
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def listenpolicy(self) :
		ur"""Default syntax expression identifying traffic accepted by the virtual server. Can be either an expression (for example, CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24) or the name of a named expression. In the above example, the virtual server accepts all requests whose destination IP address is in the 192.0.2.0/24 subnet.<br/>Default value: "none".
		"""
		try :
			return self._listenpolicy
		except Exception as e:
			raise e

	@listenpolicy.setter
	def listenpolicy(self, listenpolicy) :
		ur"""Default syntax expression identifying traffic accepted by the virtual server. Can be either an expression (for example, CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24) or the name of a named expression. In the above example, the virtual server accepts all requests whose destination IP address is in the 192.0.2.0/24 subnet.<br/>Default value: "none"
		"""
		try :
			self._listenpolicy = listenpolicy
		except Exception as e:
			raise e

	@property
	def listenpriority(self) :
		ur"""Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.<br/>Default value: 101<br/>Maximum length =  101.
		"""
		try :
			return self._listenpriority
		except Exception as e:
			raise e

	@listenpriority.setter
	def listenpriority(self, listenpriority) :
		ur"""Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.<br/>Default value: 101<br/>Maximum length =  101
		"""
		try :
			self._listenpriority = listenpriority
		except Exception as e:
			raise e

	@property
	def resrule(self) :
		ur"""Default syntax expression specifying which part of a server's response to use for creating rule based persistence sessions (persistence type RULE). Can be either an expression or the name of a named expression.
		Example:
		HTTP.RES.HEADER("setcookie").VALUE(0).TYPECAST_NVLIST_T('=',';').VALUE("server1").<br/>Default value: "none".
		"""
		try :
			return self._resrule
		except Exception as e:
			raise e

	@resrule.setter
	def resrule(self, resrule) :
		ur"""Default syntax expression specifying which part of a server's response to use for creating rule based persistence sessions (persistence type RULE). Can be either an expression or the name of a named expression.
		Example:
		HTTP.RES.HEADER("setcookie").VALUE(0).TYPECAST_NVLIST_T('=',';').VALUE("server1").<br/>Default value: "none"
		"""
		try :
			self._resrule = resrule
		except Exception as e:
			raise e

	@property
	def persistmask(self) :
		ur"""Persistence mask for IP based persistence types, for IPv4 virtual servers.<br/>Minimum length =  1.
		"""
		try :
			return self._persistmask
		except Exception as e:
			raise e

	@persistmask.setter
	def persistmask(self, persistmask) :
		ur"""Persistence mask for IP based persistence types, for IPv4 virtual servers.<br/>Minimum length =  1
		"""
		try :
			self._persistmask = persistmask
		except Exception as e:
			raise e

	@property
	def v6persistmasklen(self) :
		ur"""Persistence mask for IP based persistence types, for IPv6 virtual servers.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6persistmasklen
		except Exception as e:
			raise e

	@v6persistmasklen.setter
	def v6persistmasklen(self, v6persistmasklen) :
		ur"""Persistence mask for IP based persistence types, for IPv6 virtual servers.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6persistmasklen = v6persistmasklen
		except Exception as e:
			raise e

	@property
	def pq(self) :
		ur"""Use priority queuing on the virtual server. based persistence types, for IPv6 virtual servers.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._pq
		except Exception as e:
			raise e

	@pq.setter
	def pq(self, pq) :
		ur"""Use priority queuing on the virtual server. based persistence types, for IPv6 virtual servers.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._pq = pq
		except Exception as e:
			raise e

	@property
	def sc(self) :
		ur"""Use SureConnect on the virtual server.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@sc.setter
	def sc(self, sc) :
		ur"""Use SureConnect on the virtual server.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sc = sc
		except Exception as e:
			raise e

	@property
	def rtspnat(self) :
		ur"""Use network address translation (NAT) for RTSP data connections.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._rtspnat
		except Exception as e:
			raise e

	@rtspnat.setter
	def rtspnat(self, rtspnat) :
		ur"""Use network address translation (NAT) for RTSP data connections.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._rtspnat = rtspnat
		except Exception as e:
			raise e

	@property
	def m(self) :
		ur"""Redirection mode for load balancing. Available settings function as follows:
		* IP - Before forwarding a request to a server, change the destination IP address to the server's IP address. 
		* MAC - Before forwarding a request to a server, change the destination MAC address to the server's MAC address.  The destination IP address is not changed. MAC-based redirection mode is used mostly in firewall load balancing deployments. 
		* IPTUNNEL - Perform IP-in-IP encapsulation for client IP packets. In the outer IP headers, set the destination IP address to the IP address of the server and the source IP address to the subnet IP (SNIP). The client IP packets are not modified. Applicable to both IPv4 and IPv6 packets. 
		* TOS - Encode the virtual server's TOS ID in the TOS field of the IP header. 
		You can use either the IPTUNNEL or the TOS option to implement Direct Server Return (DSR).<br/>Default value: IP<br/>Possible values = IP, MAC, IPTUNNEL, TOS.
		"""
		try :
			return self._m
		except Exception as e:
			raise e

	@m.setter
	def m(self, m) :
		ur"""Redirection mode for load balancing. Available settings function as follows:
		* IP - Before forwarding a request to a server, change the destination IP address to the server's IP address. 
		* MAC - Before forwarding a request to a server, change the destination MAC address to the server's MAC address.  The destination IP address is not changed. MAC-based redirection mode is used mostly in firewall load balancing deployments. 
		* IPTUNNEL - Perform IP-in-IP encapsulation for client IP packets. In the outer IP headers, set the destination IP address to the IP address of the server and the source IP address to the subnet IP (SNIP). The client IP packets are not modified. Applicable to both IPv4 and IPv6 packets. 
		* TOS - Encode the virtual server's TOS ID in the TOS field of the IP header. 
		You can use either the IPTUNNEL or the TOS option to implement Direct Server Return (DSR).<br/>Default value: IP<br/>Possible values = IP, MAC, IPTUNNEL, TOS
		"""
		try :
			self._m = m
		except Exception as e:
			raise e

	@property
	def tosid(self) :
		ur"""TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.<br/>Minimum length =  1<br/>Maximum length =  63.
		"""
		try :
			return self._tosid
		except Exception as e:
			raise e

	@tosid.setter
	def tosid(self, tosid) :
		ur"""TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.<br/>Minimum length =  1<br/>Maximum length =  63
		"""
		try :
			self._tosid = tosid
		except Exception as e:
			raise e

	@property
	def datalength(self) :
		ur"""Length of the token to be extracted from the data segment of an incoming packet, for use in the token method of load balancing. The length of the token, specified in bytes, must not be greater than 24 KB. Applicable to virtual servers of type TCP.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._datalength
		except Exception as e:
			raise e

	@datalength.setter
	def datalength(self, datalength) :
		ur"""Length of the token to be extracted from the data segment of an incoming packet, for use in the token method of load balancing. The length of the token, specified in bytes, must not be greater than 24 KB. Applicable to virtual servers of type TCP.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._datalength = datalength
		except Exception as e:
			raise e

	@property
	def dataoffset(self) :
		ur"""Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers, of type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP payload.<br/>Maximum length =  25400.
		"""
		try :
			return self._dataoffset
		except Exception as e:
			raise e

	@dataoffset.setter
	def dataoffset(self, dataoffset) :
		ur"""Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers, of type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP payload.<br/>Maximum length =  25400
		"""
		try :
			self._dataoffset = dataoffset
		except Exception as e:
			raise e

	@property
	def sessionless(self) :
		ur"""Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load balancing of intrusion detection system (IDS) servers and scenarios involving direct server return (DSR), where session information is unnecessary.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionless
		except Exception as e:
			raise e

	@sessionless.setter
	def sessionless(self, sessionless) :
		ur"""Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load balancing of intrusion detection system (IDS) servers and scenarios involving direct server return (DSR), where session information is unnecessary.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionless = sessionless
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of the load balancing virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""State of the load balancing virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def connfailover(self) :
		ur"""Mode in which the connection failover feature must operate for the virtual server. After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary appliance. Clients remain connected to the same servers. Available settings function as follows:
		* STATEFUL - The primary appliance shares state information with the secondary appliance, in real time, resulting in some runtime processing overhead. 
		* STATELESS - State information is not shared, and the new primary appliance tries to re-create the packet flow on the basis of the information contained in the packets it receives. 
		* DISABLED - Connection failover does not occur.<br/>Default value: DISABLED<br/>Possible values = DISABLED, STATEFUL, STATELESS.
		"""
		try :
			return self._connfailover
		except Exception as e:
			raise e

	@connfailover.setter
	def connfailover(self, connfailover) :
		ur"""Mode in which the connection failover feature must operate for the virtual server. After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary appliance. Clients remain connected to the same servers. Available settings function as follows:
		* STATEFUL - The primary appliance shares state information with the secondary appliance, in real time, resulting in some runtime processing overhead. 
		* STATELESS - State information is not shared, and the new primary appliance tries to re-create the packet flow on the basis of the information contained in the packets it receives. 
		* DISABLED - Connection failover does not occur.<br/>Default value: DISABLED<br/>Possible values = DISABLED, STATEFUL, STATELESS
		"""
		try :
			self._connfailover = connfailover
		except Exception as e:
			raise e

	@property
	def redirurl(self) :
		ur"""URL to which to redirect traffic if the virtual server becomes unavailable. 
		WARNING! Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._redirurl
		except Exception as e:
			raise e

	@redirurl.setter
	def redirurl(self, redirurl) :
		ur"""URL to which to redirect traffic if the virtual server becomes unavailable. 
		WARNING! Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.<br/>Minimum length =  1
		"""
		try :
			self._redirurl = redirurl
		except Exception as e:
			raise e

	@property
	def cacheable(self) :
		ur"""Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can forward requests only to a transparent cache redirection virtual server that has an IP address and port combination of *:80, so such a cache redirection virtual server must be configured on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheable
		except Exception as e:
			raise e

	@cacheable.setter
	def cacheable(self, cacheable) :
		ur"""Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can forward requests only to a transparent cache redirection virtual server that has an IP address and port combination of *:80, so such a cache redirection virtual server must be configured on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._cacheable = cacheable
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		ur"""Idle time, in seconds, after which a client connection is terminated.<br/>Maximum length =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@clttimeout.setter
	def clttimeout(self, clttimeout) :
		ur"""Idle time, in seconds, after which a client connection is terminated.<br/>Maximum length =  31536000
		"""
		try :
			self._clttimeout = clttimeout
		except Exception as e:
			raise e

	@property
	def somethod(self) :
		ur"""Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:
		* CONNECTION - Spillover occurs when the number of client connections exceeds the threshold.
		* DYNAMICCONNECTION - Spillover occurs when the number of client connections at the virtual server exceeds the sum of the maximum client (Max Clients) settings for bound services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of bound services.
		* BANDWIDTH - Spillover occurs when the bandwidth consumed by the virtual server's incoming and outgoing traffic exceeds the threshold. 
		* HEALTH - Spillover occurs when the percentage of weights of the services that are UP drops below the threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and svc3 transition to DOWN. 
		* NONE - Spillover does not occur.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE.
		"""
		try :
			return self._somethod
		except Exception as e:
			raise e

	@somethod.setter
	def somethod(self, somethod) :
		ur"""Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:
		* CONNECTION - Spillover occurs when the number of client connections exceeds the threshold.
		* DYNAMICCONNECTION - Spillover occurs when the number of client connections at the virtual server exceeds the sum of the maximum client (Max Clients) settings for bound services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of bound services.
		* BANDWIDTH - Spillover occurs when the bandwidth consumed by the virtual server's incoming and outgoing traffic exceeds the threshold. 
		* HEALTH - Spillover occurs when the percentage of weights of the services that are UP drops below the threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and svc3 transition to DOWN. 
		* NONE - Spillover does not occur.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE
		"""
		try :
			self._somethod = somethod
		except Exception as e:
			raise e

	@property
	def sopersistence(self) :
		ur"""If spillover occurs, maintain source IP address based persistence for both primary and backup virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sopersistence
		except Exception as e:
			raise e

	@sopersistence.setter
	def sopersistence(self, sopersistence) :
		ur"""If spillover occurs, maintain source IP address based persistence for both primary and backup virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sopersistence = sopersistence
		except Exception as e:
			raise e

	@property
	def sopersistencetimeout(self) :
		ur"""Timeout for spillover persistence, in minutes.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._sopersistencetimeout
		except Exception as e:
			raise e

	@sopersistencetimeout.setter
	def sopersistencetimeout(self, sopersistencetimeout) :
		ur"""Timeout for spillover persistence, in minutes.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._sopersistencetimeout = sopersistencetimeout
		except Exception as e:
			raise e

	@property
	def healththreshold(self) :
		ur"""Threshold in percent of active services below which vserver state is made down. If this threshold is 0, vserver state will be up even if one bound service is up.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._healththreshold
		except Exception as e:
			raise e

	@healththreshold.setter
	def healththreshold(self, healththreshold) :
		ur"""Threshold in percent of active services below which vserver state is made down. If this threshold is 0, vserver state will be up even if one bound service is up.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._healththreshold = healththreshold
		except Exception as e:
			raise e

	@property
	def sothreshold(self) :
		ur"""Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).<br/>Minimum length =  1<br/>Maximum length =  4294967287.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@sothreshold.setter
	def sothreshold(self, sothreshold) :
		ur"""Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).<br/>Minimum length =  1<br/>Maximum length =  4294967287
		"""
		try :
			self._sothreshold = sothreshold
		except Exception as e:
			raise e

	@property
	def sobackupaction(self) :
		ur"""Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.<br/>Possible values = DROP, ACCEPT, REDIRECT.
		"""
		try :
			return self._sobackupaction
		except Exception as e:
			raise e

	@sobackupaction.setter
	def sobackupaction(self, sobackupaction) :
		ur"""Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.<br/>Possible values = DROP, ACCEPT, REDIRECT
		"""
		try :
			self._sobackupaction = sobackupaction
		except Exception as e:
			raise e

	@property
	def redirectportrewrite(self) :
		ur"""Rewrite the port and change the protocol to ensure successful HTTP redirects from services.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._redirectportrewrite
		except Exception as e:
			raise e

	@redirectportrewrite.setter
	def redirectportrewrite(self, redirectportrewrite) :
		ur"""Rewrite the port and change the protocol to ensure successful HTTP redirects from services.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._redirectportrewrite = redirectportrewrite
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		ur"""Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@downstateflush.setter
	def downstateflush(self, downstateflush) :
		ur"""Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._downstateflush = downstateflush
		except Exception as e:
			raise e

	@property
	def backupvserver(self) :
		ur"""Name of the backup virtual server to which to forward requests if the primary virtual server goes DOWN or reaches its spillover threshold.<br/>Minimum length =  1.
		"""
		try :
			return self._backupvserver
		except Exception as e:
			raise e

	@backupvserver.setter
	def backupvserver(self, backupvserver) :
		ur"""Name of the backup virtual server to which to forward requests if the primary virtual server goes DOWN or reaches its spillover threshold.<br/>Minimum length =  1
		"""
		try :
			self._backupvserver = backupvserver
		except Exception as e:
			raise e

	@property
	def disableprimaryondown(self) :
		ur"""If the primary virtual server goes down, do not allow it to return to primary status until manually enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._disableprimaryondown
		except Exception as e:
			raise e

	@disableprimaryondown.setter
	def disableprimaryondown(self, disableprimaryondown) :
		ur"""If the primary virtual server goes down, do not allow it to return to primary status until manually enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._disableprimaryondown = disableprimaryondown
		except Exception as e:
			raise e

	@property
	def insertvserveripport(self) :
		ur"""Insert an HTTP header, whose value is the IP address and port number of the virtual server, before forwarding a request to the server. The format of the header is <vipHeader>: <virtual server IP address>_<port number >, where vipHeader is the name that you specify for the header. If the virtual server has an IPv6 address, the address in the header is enclosed in brackets ([ and ]) to separate it from the port number. If you have mapped an IPv4 address to a virtual server's IPv6 address, the value of this parameter determines which IP address is inserted in the header, as follows:
		* VIPADDR - Insert the IP address of the virtual server in the HTTP header regardless of whether the virtual server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is ignored.
		* V6TOV4MAPPING - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a mapped IPv4 address is not configured, insert the IPv6 address.
		* OFF - Disable header insertion.<br/>Possible values = OFF, VIPADDR, V6TOV4MAPPING.
		"""
		try :
			return self._insertvserveripport
		except Exception as e:
			raise e

	@insertvserveripport.setter
	def insertvserveripport(self, insertvserveripport) :
		ur"""Insert an HTTP header, whose value is the IP address and port number of the virtual server, before forwarding a request to the server. The format of the header is <vipHeader>: <virtual server IP address>_<port number >, where vipHeader is the name that you specify for the header. If the virtual server has an IPv6 address, the address in the header is enclosed in brackets ([ and ]) to separate it from the port number. If you have mapped an IPv4 address to a virtual server's IPv6 address, the value of this parameter determines which IP address is inserted in the header, as follows:
		* VIPADDR - Insert the IP address of the virtual server in the HTTP header regardless of whether the virtual server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is ignored.
		* V6TOV4MAPPING - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a mapped IPv4 address is not configured, insert the IPv6 address.
		* OFF - Disable header insertion.<br/>Possible values = OFF, VIPADDR, V6TOV4MAPPING
		"""
		try :
			self._insertvserveripport = insertvserveripport
		except Exception as e:
			raise e

	@property
	def vipheader(self) :
		ur"""Name for the inserted header. The default name is vip-header.<br/>Minimum length =  1.
		"""
		try :
			return self._vipheader
		except Exception as e:
			raise e

	@vipheader.setter
	def vipheader(self, vipheader) :
		ur"""Name for the inserted header. The default name is vip-header.<br/>Minimum length =  1
		"""
		try :
			self._vipheader = vipheader
		except Exception as e:
			raise e

	@property
	def authenticationhost(self) :
		ur"""Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be redirected for authentication. Make sure that the Authentication parameter is set to ENABLED.<br/>Minimum length =  3<br/>Maximum length =  252.
		"""
		try :
			return self._authenticationhost
		except Exception as e:
			raise e

	@authenticationhost.setter
	def authenticationhost(self, authenticationhost) :
		ur"""Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be redirected for authentication. Make sure that the Authentication parameter is set to ENABLED.<br/>Minimum length =  3<br/>Maximum length =  252
		"""
		try :
			self._authenticationhost = authenticationhost
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		ur"""Enable or disable user authentication.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		ur"""Enable or disable user authentication.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	@property
	def authn401(self) :
		ur"""Enable or disable user authentication with HTTP 401 responses.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authn401
		except Exception as e:
			raise e

	@authn401.setter
	def authn401(self, authn401) :
		ur"""Enable or disable user authentication with HTTP 401 responses.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._authn401 = authn401
		except Exception as e:
			raise e

	@property
	def authnvsname(self) :
		ur"""Name of an authentication virtual server with which to authenticate users.<br/>Minimum length =  1<br/>Maximum length =  252.
		"""
		try :
			return self._authnvsname
		except Exception as e:
			raise e

	@authnvsname.setter
	def authnvsname(self, authnvsname) :
		ur"""Name of an authentication virtual server with which to authenticate users.<br/>Minimum length =  1<br/>Maximum length =  252
		"""
		try :
			self._authnvsname = authnvsname
		except Exception as e:
			raise e

	@property
	def push(self) :
		ur"""Process traffic with the push virtual server that is bound to this load balancing virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._push
		except Exception as e:
			raise e

	@push.setter
	def push(self, push) :
		ur"""Process traffic with the push virtual server that is bound to this load balancing virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._push = push
		except Exception as e:
			raise e

	@property
	def pushvserver(self) :
		ur"""Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes updates received on the load balancing virtual server that you are configuring.<br/>Minimum length =  1.
		"""
		try :
			return self._pushvserver
		except Exception as e:
			raise e

	@pushvserver.setter
	def pushvserver(self, pushvserver) :
		ur"""Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes updates received on the load balancing virtual server that you are configuring.<br/>Minimum length =  1
		"""
		try :
			self._pushvserver = pushvserver
		except Exception as e:
			raise e

	@property
	def pushlabel(self) :
		ur"""Expression for extracting a label from the server's response. Can be either an expression or the name of a named expression.<br/>Default value: "none".
		"""
		try :
			return self._pushlabel
		except Exception as e:
			raise e

	@pushlabel.setter
	def pushlabel(self, pushlabel) :
		ur"""Expression for extracting a label from the server's response. Can be either an expression or the name of a named expression.<br/>Default value: "none"
		"""
		try :
			self._pushlabel = pushlabel
		except Exception as e:
			raise e

	@property
	def pushmulticlients(self) :
		ur"""Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._pushmulticlients
		except Exception as e:
			raise e

	@pushmulticlients.setter
	def pushmulticlients(self, pushmulticlients) :
		ur"""Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._pushmulticlients = pushmulticlients
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		ur"""Name of the TCP profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@tcpprofilename.setter
	def tcpprofilename(self, tcpprofilename) :
		ur"""Name of the TCP profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._tcpprofilename = tcpprofilename
		except Exception as e:
			raise e

	@property
	def httpprofilename(self) :
		ur"""Name of the HTTP profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._httpprofilename
		except Exception as e:
			raise e

	@httpprofilename.setter
	def httpprofilename(self, httpprofilename) :
		ur"""Name of the HTTP profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._httpprofilename = httpprofilename
		except Exception as e:
			raise e

	@property
	def dbprofilename(self) :
		ur"""Name of the DB profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dbprofilename
		except Exception as e:
			raise e

	@dbprofilename.setter
	def dbprofilename(self, dbprofilename) :
		ur"""Name of the DB profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dbprofilename = dbprofilename
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments that you might want to associate with the virtual server.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments that you might want to associate with the virtual server.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def l2conn(self) :
		ur"""Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>) that is used to identify a connection. Allows multiple TCP and non-TCP connections with the same 4-tuple to co-exist on the NetScaler appliance.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._l2conn
		except Exception as e:
			raise e

	@l2conn.setter
	def l2conn(self, l2conn) :
		ur"""Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>) that is used to identify a connection. Allows multiple TCP and non-TCP connections with the same 4-tuple to co-exist on the NetScaler appliance.<br/>Possible values = ON, OFF
		"""
		try :
			self._l2conn = l2conn
		except Exception as e:
			raise e

	@property
	def oracleserverversion(self) :
		ur"""Oracle server version.<br/>Default value: 10G<br/>Possible values = 10G, 11G.
		"""
		try :
			return self._oracleserverversion
		except Exception as e:
			raise e

	@oracleserverversion.setter
	def oracleserverversion(self, oracleserverversion) :
		ur"""Oracle server version.<br/>Default value: 10G<br/>Possible values = 10G, 11G
		"""
		try :
			self._oracleserverversion = oracleserverversion
		except Exception as e:
			raise e

	@property
	def mssqlserverversion(self) :
		ur"""For a load balancing virtual server of type MSSQL, the Microsoft SQL Server version. Set this parameter if you expect some clients to run a version different from the version of the database. This setting provides compatibility between the client-side and server-side connections by ensuring that all communication conforms to the server's version.<br/>Default value: 2008R2<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012.
		"""
		try :
			return self._mssqlserverversion
		except Exception as e:
			raise e

	@mssqlserverversion.setter
	def mssqlserverversion(self, mssqlserverversion) :
		ur"""For a load balancing virtual server of type MSSQL, the Microsoft SQL Server version. Set this parameter if you expect some clients to run a version different from the version of the database. This setting provides compatibility between the client-side and server-side connections by ensuring that all communication conforms to the server's version.<br/>Default value: 2008R2<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012
		"""
		try :
			self._mssqlserverversion = mssqlserverversion
		except Exception as e:
			raise e

	@property
	def mysqlprotocolversion(self) :
		ur"""MySQL protocol version that the virtual server advertises to clients.
		"""
		try :
			return self._mysqlprotocolversion
		except Exception as e:
			raise e

	@mysqlprotocolversion.setter
	def mysqlprotocolversion(self, mysqlprotocolversion) :
		ur"""MySQL protocol version that the virtual server advertises to clients.
		"""
		try :
			self._mysqlprotocolversion = mysqlprotocolversion
		except Exception as e:
			raise e

	@property
	def mysqlserverversion(self) :
		ur"""MySQL server version string that the virtual server advertises to clients.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._mysqlserverversion
		except Exception as e:
			raise e

	@mysqlserverversion.setter
	def mysqlserverversion(self, mysqlserverversion) :
		ur"""MySQL server version string that the virtual server advertises to clients.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._mysqlserverversion = mysqlserverversion
		except Exception as e:
			raise e

	@property
	def mysqlcharacterset(self) :
		ur"""Character set that the virtual server advertises to clients.
		"""
		try :
			return self._mysqlcharacterset
		except Exception as e:
			raise e

	@mysqlcharacterset.setter
	def mysqlcharacterset(self, mysqlcharacterset) :
		ur"""Character set that the virtual server advertises to clients.
		"""
		try :
			self._mysqlcharacterset = mysqlcharacterset
		except Exception as e:
			raise e

	@property
	def mysqlservercapabilities(self) :
		ur"""Server capabilities that the virtual server advertises to clients.
		"""
		try :
			return self._mysqlservercapabilities
		except Exception as e:
			raise e

	@mysqlservercapabilities.setter
	def mysqlservercapabilities(self, mysqlservercapabilities) :
		ur"""Server capabilities that the virtual server advertises to clients.
		"""
		try :
			self._mysqlservercapabilities = mysqlservercapabilities
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		ur"""Apply AppFlow logging to the virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		ur"""Apply AppFlow logging to the virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		ur"""Name of the network profile to associate with the virtual server. If you set this parameter, the virtual server uses only the IP addresses in the network profile as source IP addresses when initiating connections with servers.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		ur"""Name of the network profile to associate with the virtual server. If you set this parameter, the virtual server uses only the IP addresses in the network profile as source IP addresses when initiating connections with servers.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def icmpvsrresponse(self) :
		ur"""How the NetScaler appliance responds to ping requests received for an IP address that is common to one or more virtual servers. Available settings function as follows:
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always responds to the ping requests.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance responds to the ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not respond.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance responds if at least one virtual server with the ACTIVE setting is UP. Otherwise, the appliance does not respond.
		Note: This parameter is available at the virtual server level. A similar parameter, ICMP Response, is available at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add ip command in the CLI or the Create IP dialog box in the GUI.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._icmpvsrresponse
		except Exception as e:
			raise e

	@icmpvsrresponse.setter
	def icmpvsrresponse(self, icmpvsrresponse) :
		ur"""How the NetScaler appliance responds to ping requests received for an IP address that is common to one or more virtual servers. Available settings function as follows:
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always responds to the ping requests.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance responds to the ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not respond.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance responds if at least one virtual server with the ACTIVE setting is UP. Otherwise, the appliance does not respond.
		Note: This parameter is available at the virtual server level. A similar parameter, ICMP Response, is available at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add ip command in the CLI or the Create IP dialog box in the GUI.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._icmpvsrresponse = icmpvsrresponse
		except Exception as e:
			raise e

	@property
	def rhistate(self) :
		ur"""Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the VIP address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:
		* If you set RHI STATE to PASSIVE on all virtual servers, the NetScaler ADC always advertises the route for the VIP address.
		* If you set RHI STATE to ACTIVE on all virtual servers, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.
		* If you set RHI STATE to ACTIVE on some and PASSIVE on others, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is in UP state.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._rhistate
		except Exception as e:
			raise e

	@rhistate.setter
	def rhistate(self, rhistate) :
		ur"""Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the VIP address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:
		* If you set RHI STATE to PASSIVE on all virtual servers, the NetScaler ADC always advertises the route for the VIP address.
		* If you set RHI STATE to ACTIVE on all virtual servers, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.
		* If you set RHI STATE to ACTIVE on some and PASSIVE on others, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is in UP state.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._rhistate = rhistate
		except Exception as e:
			raise e

	@property
	def newservicerequest(self) :
		ur"""Number of requests, or percentage of the load on existing services, by which to increase the load on a new service at each interval in slow-start mode. A non-zero value indicates that slow-start is applicable. A zero value indicates that the global RR startup parameter is applied. Changing the value to zero will cause services currently in slow start to take the full traffic as determined by the LB method. Subsequently, any new services added will use the global RR factor.<br/>Default value: 0.
		"""
		try :
			return self._newservicerequest
		except Exception as e:
			raise e

	@newservicerequest.setter
	def newservicerequest(self, newservicerequest) :
		ur"""Number of requests, or percentage of the load on existing services, by which to increase the load on a new service at each interval in slow-start mode. A non-zero value indicates that slow-start is applicable. A zero value indicates that the global RR startup parameter is applied. Changing the value to zero will cause services currently in slow start to take the full traffic as determined by the LB method. Subsequently, any new services added will use the global RR factor.<br/>Default value: 0
		"""
		try :
			self._newservicerequest = newservicerequest
		except Exception as e:
			raise e

	@property
	def newservicerequestunit(self) :
		ur"""Units in which to increment load at each interval in slow-start mode.<br/>Default value: PER_SECOND<br/>Possible values = PER_SECOND, PERCENT.
		"""
		try :
			return self._newservicerequestunit
		except Exception as e:
			raise e

	@newservicerequestunit.setter
	def newservicerequestunit(self, newservicerequestunit) :
		ur"""Units in which to increment load at each interval in slow-start mode.<br/>Default value: PER_SECOND<br/>Possible values = PER_SECOND, PERCENT
		"""
		try :
			self._newservicerequestunit = newservicerequestunit
		except Exception as e:
			raise e

	@property
	def newservicerequestincrementinterval(self) :
		ur"""Interval, in seconds, between successive increments in the load on a new service or a service whose state has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.<br/>Default value: 0<br/>Maximum length =  3600.
		"""
		try :
			return self._newservicerequestincrementinterval
		except Exception as e:
			raise e

	@newservicerequestincrementinterval.setter
	def newservicerequestincrementinterval(self, newservicerequestincrementinterval) :
		ur"""Interval, in seconds, between successive increments in the load on a new service or a service whose state has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.<br/>Default value: 0<br/>Maximum length =  3600
		"""
		try :
			self._newservicerequestincrementinterval = newservicerequestincrementinterval
		except Exception as e:
			raise e

	@property
	def minautoscalemembers(self) :
		ur"""Minimum number of members expected to be present when vserver is used in Autoscale.<br/>Default value: 0<br/>Maximum length =  5000.
		"""
		try :
			return self._minautoscalemembers
		except Exception as e:
			raise e

	@minautoscalemembers.setter
	def minautoscalemembers(self, minautoscalemembers) :
		ur"""Minimum number of members expected to be present when vserver is used in Autoscale.<br/>Default value: 0<br/>Maximum length =  5000
		"""
		try :
			self._minautoscalemembers = minautoscalemembers
		except Exception as e:
			raise e

	@property
	def maxautoscalemembers(self) :
		ur"""Maximum number of members expected to be present when vserver is used in Autoscale.<br/>Default value: 0<br/>Maximum length =  5000.
		"""
		try :
			return self._maxautoscalemembers
		except Exception as e:
			raise e

	@maxautoscalemembers.setter
	def maxautoscalemembers(self, maxautoscalemembers) :
		ur"""Maximum number of members expected to be present when vserver is used in Autoscale.<br/>Default value: 0<br/>Maximum length =  5000
		"""
		try :
			self._maxautoscalemembers = maxautoscalemembers
		except Exception as e:
			raise e

	@property
	def persistavpno(self) :
		ur"""Persist AVP number for Diameter Persistency. 
		In case this AVP is not defined in Base RFC 3588 and it is nested inside a Grouped AVP, 
		define a sequence of AVP numbers (max 3) in order of parent to child. So say persist AVP number X 
		is nested inside AVP Y which is nested in Z, then define the list as  Z Y X.<br/>Minimum length =  1.
		"""
		try :
			return self._persistavpno
		except Exception as e:
			raise e

	@persistavpno.setter
	def persistavpno(self, persistavpno) :
		ur"""Persist AVP number for Diameter Persistency. 
		In case this AVP is not defined in Base RFC 3588 and it is nested inside a Grouped AVP, 
		define a sequence of AVP numbers (max 3) in order of parent to child. So say persist AVP number X 
		is nested inside AVP Y which is nested in Z, then define the list as  Z Y X.<br/>Minimum length =  1
		"""
		try :
			self._persistavpno = persistavpno
		except Exception as e:
			raise e

	@property
	def skippersistency(self) :
		ur"""This argument decides the behavior incase the service which is selected from an existing persistence session has reached threshold.<br/>Default value: None<br/>Possible values = Bypass, ReLb, None.
		"""
		try :
			return self._skippersistency
		except Exception as e:
			raise e

	@skippersistency.setter
	def skippersistency(self, skippersistency) :
		ur"""This argument decides the behavior incase the service which is selected from an existing persistence session has reached threshold.<br/>Default value: None<br/>Possible values = Bypass, ReLb, None
		"""
		try :
			self._skippersistency = skippersistency
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def authnprofile(self) :
		ur"""Name of the authentication profile to be used when authentication is turned on.
		"""
		try :
			return self._authnprofile
		except Exception as e:
			raise e

	@authnprofile.setter
	def authnprofile(self, authnprofile) :
		ur"""Name of the authentication profile to be used when authentication is turned on.
		"""
		try :
			self._authnprofile = authnprofile
		except Exception as e:
			raise e

	@property
	def macmoderetainvlan(self) :
		ur"""This option is used to retain vlan information of incoming packet when macmode is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._macmoderetainvlan
		except Exception as e:
			raise e

	@macmoderetainvlan.setter
	def macmoderetainvlan(self, macmoderetainvlan) :
		ur"""This option is used to retain vlan information of incoming packet when macmode is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._macmoderetainvlan = macmoderetainvlan
		except Exception as e:
			raise e

	@property
	def dbslb(self) :
		ur"""Enable database specific load balancing for MySQL and MSSQL service types.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dbslb
		except Exception as e:
			raise e

	@dbslb.setter
	def dbslb(self, dbslb) :
		ur"""Enable database specific load balancing for MySQL and MSSQL service types.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dbslb = dbslb
		except Exception as e:
			raise e

	@property
	def dns64(self) :
		ur"""This argument is for enabling/disabling the dns64 on lbvserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dns64
		except Exception as e:
			raise e

	@dns64.setter
	def dns64(self, dns64) :
		ur"""This argument is for enabling/disabling the dns64 on lbvserver.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dns64 = dns64
		except Exception as e:
			raise e

	@property
	def bypassaaaa(self) :
		ur"""If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns server.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._bypassaaaa
		except Exception as e:
			raise e

	@bypassaaaa.setter
	def bypassaaaa(self, bypassaaaa) :
		ur"""If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns server.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._bypassaaaa = bypassaaaa
		except Exception as e:
			raise e

	@property
	def recursionavailable(self) :
		ur"""When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on. Typically one would set this option to YES, when the vserver is load balancing a set of DNS servers thatsupport recursive queries.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._recursionavailable
		except Exception as e:
			raise e

	@recursionavailable.setter
	def recursionavailable(self, recursionavailable) :
		ur"""When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on. Typically one would set this option to YES, when the vserver is load balancing a set of DNS servers thatsupport recursive queries.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._recursionavailable = recursionavailable
		except Exception as e:
			raise e

	@property
	def processlocal(self) :
		ur"""By turning on this option packets destined to a vserver in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._processlocal
		except Exception as e:
			raise e

	@processlocal.setter
	def processlocal(self, processlocal) :
		ur"""By turning on this option packets destined to a vserver in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._processlocal = processlocal
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Weight to assign to the specified service.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur"""Weight to assign to the specified service.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""Service to bind to the virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""Service to bind to the virtual server.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def redirurlflags(self) :
		ur"""The redirect URL to be unset.
		"""
		try :
			return self._redirurlflags
		except Exception as e:
			raise e

	@redirurlflags.setter
	def redirurlflags(self, redirurlflags) :
		ur"""The redirect URL to be unset.
		"""
		try :
			self._redirurlflags = redirurlflags
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the virtual server.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def value(self) :
		ur"""SSL status.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def ipmapping(self) :
		ur"""The permanent mapping for the V6 Address.
		"""
		try :
			return self._ipmapping
		except Exception as e:
			raise e

	@property
	def ngname(self) :
		ur"""Nodegroup name to which this lbvsever belongs to.
		"""
		try :
			return self._ngname
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of LB vserver.<br/>Possible values = CONTENT, ADDRESS.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		ur"""Current LB vserver state.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def effectivestate(self) :
		ur"""Effective state of the LB vserver , based on the state of backup vservers.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._effectivestate
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""Current status of the lb vserver. During the initial phase if the configured lb method is not round robin , the vserver will adopt round robin to distribute traffic for a predefined number of requests.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def lbrrreason(self) :
		ur"""Reason why a vserver is in RR. The following are the reasons:
		1  - MEP is DOWN (GSLB)
		2  - LB method has changed
		3  - Bound service's state changed to UP
		4  - A new service is bound
		5  - Startup RR factor has changed
		6  - LB feature is enabled
		7  - Load monitor is not active on a service
		8  - Vserver is Enabled
		9  - SSL feature is Enabled
		10 - All bound services have reached threshold. Using effective state to load balance (GSLB)
		11 - Primary state of bound services are not UP. Using effective state to load balance (GSLB)
		12 - No LB decision can be made as all bound services have either reached threshold or are not UP (GSLB)
		13 - All load monitors are active
		.
		"""
		try :
			return self._lbrrreason
		except Exception as e:
			raise e

	@property
	def redirect(self) :
		ur"""Cache redirect type.<br/>Possible values = CACHE, POLICY, ORIGIN.
		"""
		try :
			return self._redirect
		except Exception as e:
			raise e

	@property
	def precedence(self) :
		ur"""Precedence.<br/>Possible values = RULE, URL.
		"""
		try :
			return self._precedence
		except Exception as e:
			raise e

	@property
	def homepage(self) :
		ur"""Home page.
		"""
		try :
			return self._homepage
		except Exception as e:
			raise e

	@property
	def dnsvservername(self) :
		ur"""DNS vserver name.
		"""
		try :
			return self._dnsvservername
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""Domain.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""Name of the policy bound to the LB vserver.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def cachevserver(self) :
		ur"""Cache virtual server.
		"""
		try :
			return self._cachevserver
		except Exception as e:
			raise e

	@property
	def health(self) :
		ur"""Health of vserver based on percentage of weights of active svcs/all svcs. This does not consider administratively disabled svcs.
		"""
		try :
			return self._health
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def ruletype(self) :
		ur"""Rule type.
		"""
		try :
			return self._ruletype
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		ur"""LB group to which the lb vserver is to be bound.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@property
	def cookiedomain(self) :
		ur"""Domain name to be used in the set cookie header in case of cookie persistence.
		"""
		try :
			return self._cookiedomain
		except Exception as e:
			raise e

	@property
	def map(self) :
		ur"""Map.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._map
		except Exception as e:
			raise e

	@property
	def gt2gb(self) :
		ur"""Allow for greater than 2 GB transactions on this vserver.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._gt2gb
		except Exception as e:
			raise e

	@property
	def consolidatedlconn(self) :
		ur"""Use consolidated stats for LeastConnection.<br/>Default value: GLOBAL<br/>Possible values = GLOBAL, NO, YES.
		"""
		try :
			return self._consolidatedlconn
		except Exception as e:
			raise e

	@property
	def consolidatedlconngbl(self) :
		ur"""Fetches Global setting.<br/>Possible values = YES, NO.
		"""
		try :
			return self._consolidatedlconngbl
		except Exception as e:
			raise e

	@property
	def thresholdvalue(self) :
		ur"""Tells whether threshold exceeded for this service participating in CUSTOMLB.
		"""
		try :
			return self._thresholdvalue
		except Exception as e:
			raise e

	@property
	def bindpoint(self) :
		ur"""The bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE.
		"""
		try :
			return self._bindpoint
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		ur"""Invoke policies bound to a virtual server or policy label.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""The invocation type.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the label invoked.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@property
	def version(self) :
		ur"""Cookie version.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@property
	def totalservices(self) :
		ur"""Total number of services bound to the vserver.
		"""
		try :
			return self._totalservices
		except Exception as e:
			raise e

	@property
	def activeservices(self) :
		ur"""Total number of active services bound to the vserver.
		"""
		try :
			return self._activeservices
		except Exception as e:
			raise e

	@property
	def statechangetimesec(self) :
		ur"""Time when last state change happened. Seconds part.
		"""
		try :
			return self._statechangetimesec
		except Exception as e:
			raise e

	@property
	def statechangetimeseconds(self) :
		ur"""Time when last state change happened. Seconds part.
		"""
		try :
			return self._statechangetimeseconds
		except Exception as e:
			raise e

	@property
	def statechangetimemsec(self) :
		ur"""Time at which last state change happened. Milliseconds part.
		"""
		try :
			return self._statechangetimemsec
		except Exception as e:
			raise e

	@property
	def tickssincelaststatechange(self) :
		ur"""Time in 10 millisecond ticks since the last state change.
		"""
		try :
			return self._tickssincelaststatechange
		except Exception as e:
			raise e

	@property
	def isgslb(self) :
		ur"""This field is set to true if it is a GSLBVserver.
		"""
		try :
			return self._isgslb
		except Exception as e:
			raise e

	@property
	def vsvrdynconnsothreshold(self) :
		ur"""Spillover threshold for dynamic connection.
		"""
		try :
			return self._vsvrdynconnsothreshold
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbvserver
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
	def add(cls, client, resource) :
		ur""" Use this API to add lbvserver.
		"""
		try :
			if type(resource) is not list :
				addresource = lbvserver()
				addresource.name = resource.name
				addresource.servicetype = resource.servicetype
				addresource.ipv46 = resource.ipv46
				addresource.ippattern = resource.ippattern
				addresource.ipmask = resource.ipmask
				addresource.port = resource.port
				addresource.range = resource.range
				addresource.persistencetype = resource.persistencetype
				addresource.timeout = resource.timeout
				addresource.persistencebackup = resource.persistencebackup
				addresource.backuppersistencetimeout = resource.backuppersistencetimeout
				addresource.lbmethod = resource.lbmethod
				addresource.hashlength = resource.hashlength
				addresource.netmask = resource.netmask
				addresource.v6netmasklen = resource.v6netmasklen
				addresource.cookiename = resource.cookiename
				addresource.rule = resource.rule
				addresource.listenpolicy = resource.listenpolicy
				addresource.listenpriority = resource.listenpriority
				addresource.resrule = resource.resrule
				addresource.persistmask = resource.persistmask
				addresource.v6persistmasklen = resource.v6persistmasklen
				addresource.pq = resource.pq
				addresource.sc = resource.sc
				addresource.rtspnat = resource.rtspnat
				addresource.m = resource.m
				addresource.tosid = resource.tosid
				addresource.datalength = resource.datalength
				addresource.dataoffset = resource.dataoffset
				addresource.sessionless = resource.sessionless
				addresource.state = resource.state
				addresource.connfailover = resource.connfailover
				addresource.redirurl = resource.redirurl
				addresource.cacheable = resource.cacheable
				addresource.clttimeout = resource.clttimeout
				addresource.somethod = resource.somethod
				addresource.sopersistence = resource.sopersistence
				addresource.sopersistencetimeout = resource.sopersistencetimeout
				addresource.healththreshold = resource.healththreshold
				addresource.sothreshold = resource.sothreshold
				addresource.sobackupaction = resource.sobackupaction
				addresource.redirectportrewrite = resource.redirectportrewrite
				addresource.downstateflush = resource.downstateflush
				addresource.backupvserver = resource.backupvserver
				addresource.disableprimaryondown = resource.disableprimaryondown
				addresource.insertvserveripport = resource.insertvserveripport
				addresource.vipheader = resource.vipheader
				addresource.authenticationhost = resource.authenticationhost
				addresource.authentication = resource.authentication
				addresource.authn401 = resource.authn401
				addresource.authnvsname = resource.authnvsname
				addresource.push = resource.push
				addresource.pushvserver = resource.pushvserver
				addresource.pushlabel = resource.pushlabel
				addresource.pushmulticlients = resource.pushmulticlients
				addresource.tcpprofilename = resource.tcpprofilename
				addresource.httpprofilename = resource.httpprofilename
				addresource.dbprofilename = resource.dbprofilename
				addresource.comment = resource.comment
				addresource.l2conn = resource.l2conn
				addresource.oracleserverversion = resource.oracleserverversion
				addresource.mssqlserverversion = resource.mssqlserverversion
				addresource.mysqlprotocolversion = resource.mysqlprotocolversion
				addresource.mysqlserverversion = resource.mysqlserverversion
				addresource.mysqlcharacterset = resource.mysqlcharacterset
				addresource.mysqlservercapabilities = resource.mysqlservercapabilities
				addresource.appflowlog = resource.appflowlog
				addresource.netprofile = resource.netprofile
				addresource.icmpvsrresponse = resource.icmpvsrresponse
				addresource.rhistate = resource.rhistate
				addresource.newservicerequest = resource.newservicerequest
				addresource.newservicerequestunit = resource.newservicerequestunit
				addresource.newservicerequestincrementinterval = resource.newservicerequestincrementinterval
				addresource.minautoscalemembers = resource.minautoscalemembers
				addresource.maxautoscalemembers = resource.maxautoscalemembers
				addresource.persistavpno = resource.persistavpno
				addresource.skippersistency = resource.skippersistency
				addresource.td = resource.td
				addresource.authnprofile = resource.authnprofile
				addresource.macmoderetainvlan = resource.macmoderetainvlan
				addresource.dbslb = resource.dbslb
				addresource.dns64 = resource.dns64
				addresource.bypassaaaa = resource.bypassaaaa
				addresource.recursionavailable = resource.recursionavailable
				addresource.processlocal = resource.processlocal
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].servicetype = resource[i].servicetype
						addresources[i].ipv46 = resource[i].ipv46
						addresources[i].ippattern = resource[i].ippattern
						addresources[i].ipmask = resource[i].ipmask
						addresources[i].port = resource[i].port
						addresources[i].range = resource[i].range
						addresources[i].persistencetype = resource[i].persistencetype
						addresources[i].timeout = resource[i].timeout
						addresources[i].persistencebackup = resource[i].persistencebackup
						addresources[i].backuppersistencetimeout = resource[i].backuppersistencetimeout
						addresources[i].lbmethod = resource[i].lbmethod
						addresources[i].hashlength = resource[i].hashlength
						addresources[i].netmask = resource[i].netmask
						addresources[i].v6netmasklen = resource[i].v6netmasklen
						addresources[i].cookiename = resource[i].cookiename
						addresources[i].rule = resource[i].rule
						addresources[i].listenpolicy = resource[i].listenpolicy
						addresources[i].listenpriority = resource[i].listenpriority
						addresources[i].resrule = resource[i].resrule
						addresources[i].persistmask = resource[i].persistmask
						addresources[i].v6persistmasklen = resource[i].v6persistmasklen
						addresources[i].pq = resource[i].pq
						addresources[i].sc = resource[i].sc
						addresources[i].rtspnat = resource[i].rtspnat
						addresources[i].m = resource[i].m
						addresources[i].tosid = resource[i].tosid
						addresources[i].datalength = resource[i].datalength
						addresources[i].dataoffset = resource[i].dataoffset
						addresources[i].sessionless = resource[i].sessionless
						addresources[i].state = resource[i].state
						addresources[i].connfailover = resource[i].connfailover
						addresources[i].redirurl = resource[i].redirurl
						addresources[i].cacheable = resource[i].cacheable
						addresources[i].clttimeout = resource[i].clttimeout
						addresources[i].somethod = resource[i].somethod
						addresources[i].sopersistence = resource[i].sopersistence
						addresources[i].sopersistencetimeout = resource[i].sopersistencetimeout
						addresources[i].healththreshold = resource[i].healththreshold
						addresources[i].sothreshold = resource[i].sothreshold
						addresources[i].sobackupaction = resource[i].sobackupaction
						addresources[i].redirectportrewrite = resource[i].redirectportrewrite
						addresources[i].downstateflush = resource[i].downstateflush
						addresources[i].backupvserver = resource[i].backupvserver
						addresources[i].disableprimaryondown = resource[i].disableprimaryondown
						addresources[i].insertvserveripport = resource[i].insertvserveripport
						addresources[i].vipheader = resource[i].vipheader
						addresources[i].authenticationhost = resource[i].authenticationhost
						addresources[i].authentication = resource[i].authentication
						addresources[i].authn401 = resource[i].authn401
						addresources[i].authnvsname = resource[i].authnvsname
						addresources[i].push = resource[i].push
						addresources[i].pushvserver = resource[i].pushvserver
						addresources[i].pushlabel = resource[i].pushlabel
						addresources[i].pushmulticlients = resource[i].pushmulticlients
						addresources[i].tcpprofilename = resource[i].tcpprofilename
						addresources[i].httpprofilename = resource[i].httpprofilename
						addresources[i].dbprofilename = resource[i].dbprofilename
						addresources[i].comment = resource[i].comment
						addresources[i].l2conn = resource[i].l2conn
						addresources[i].oracleserverversion = resource[i].oracleserverversion
						addresources[i].mssqlserverversion = resource[i].mssqlserverversion
						addresources[i].mysqlprotocolversion = resource[i].mysqlprotocolversion
						addresources[i].mysqlserverversion = resource[i].mysqlserverversion
						addresources[i].mysqlcharacterset = resource[i].mysqlcharacterset
						addresources[i].mysqlservercapabilities = resource[i].mysqlservercapabilities
						addresources[i].appflowlog = resource[i].appflowlog
						addresources[i].netprofile = resource[i].netprofile
						addresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						addresources[i].rhistate = resource[i].rhistate
						addresources[i].newservicerequest = resource[i].newservicerequest
						addresources[i].newservicerequestunit = resource[i].newservicerequestunit
						addresources[i].newservicerequestincrementinterval = resource[i].newservicerequestincrementinterval
						addresources[i].minautoscalemembers = resource[i].minautoscalemembers
						addresources[i].maxautoscalemembers = resource[i].maxautoscalemembers
						addresources[i].persistavpno = resource[i].persistavpno
						addresources[i].skippersistency = resource[i].skippersistency
						addresources[i].td = resource[i].td
						addresources[i].authnprofile = resource[i].authnprofile
						addresources[i].macmoderetainvlan = resource[i].macmoderetainvlan
						addresources[i].dbslb = resource[i].dbslb
						addresources[i].dns64 = resource[i].dns64
						addresources[i].bypassaaaa = resource[i].bypassaaaa
						addresources[i].recursionavailable = resource[i].recursionavailable
						addresources[i].processlocal = resource[i].processlocal
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lbvserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbvserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lbvserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = lbvserver()
				updateresource.name = resource.name
				updateresource.ipv46 = resource.ipv46
				updateresource.ippattern = resource.ippattern
				updateresource.ipmask = resource.ipmask
				updateresource.weight = resource.weight
				updateresource.servicename = resource.servicename
				updateresource.persistencetype = resource.persistencetype
				updateresource.timeout = resource.timeout
				updateresource.persistencebackup = resource.persistencebackup
				updateresource.backuppersistencetimeout = resource.backuppersistencetimeout
				updateresource.lbmethod = resource.lbmethod
				updateresource.hashlength = resource.hashlength
				updateresource.netmask = resource.netmask
				updateresource.v6netmasklen = resource.v6netmasklen
				updateresource.rule = resource.rule
				updateresource.cookiename = resource.cookiename
				updateresource.resrule = resource.resrule
				updateresource.persistmask = resource.persistmask
				updateresource.v6persistmasklen = resource.v6persistmasklen
				updateresource.pq = resource.pq
				updateresource.sc = resource.sc
				updateresource.rtspnat = resource.rtspnat
				updateresource.m = resource.m
				updateresource.tosid = resource.tosid
				updateresource.datalength = resource.datalength
				updateresource.dataoffset = resource.dataoffset
				updateresource.sessionless = resource.sessionless
				updateresource.connfailover = resource.connfailover
				updateresource.backupvserver = resource.backupvserver
				updateresource.redirurl = resource.redirurl
				updateresource.cacheable = resource.cacheable
				updateresource.clttimeout = resource.clttimeout
				updateresource.somethod = resource.somethod
				updateresource.sothreshold = resource.sothreshold
				updateresource.sopersistence = resource.sopersistence
				updateresource.sopersistencetimeout = resource.sopersistencetimeout
				updateresource.healththreshold = resource.healththreshold
				updateresource.sobackupaction = resource.sobackupaction
				updateresource.redirectportrewrite = resource.redirectportrewrite
				updateresource.downstateflush = resource.downstateflush
				updateresource.insertvserveripport = resource.insertvserveripport
				updateresource.vipheader = resource.vipheader
				updateresource.disableprimaryondown = resource.disableprimaryondown
				updateresource.authenticationhost = resource.authenticationhost
				updateresource.authentication = resource.authentication
				updateresource.authn401 = resource.authn401
				updateresource.authnvsname = resource.authnvsname
				updateresource.push = resource.push
				updateresource.pushvserver = resource.pushvserver
				updateresource.pushlabel = resource.pushlabel
				updateresource.pushmulticlients = resource.pushmulticlients
				updateresource.listenpolicy = resource.listenpolicy
				updateresource.listenpriority = resource.listenpriority
				updateresource.tcpprofilename = resource.tcpprofilename
				updateresource.httpprofilename = resource.httpprofilename
				updateresource.dbprofilename = resource.dbprofilename
				updateresource.comment = resource.comment
				updateresource.l2conn = resource.l2conn
				updateresource.oracleserverversion = resource.oracleserverversion
				updateresource.mssqlserverversion = resource.mssqlserverversion
				updateresource.mysqlprotocolversion = resource.mysqlprotocolversion
				updateresource.mysqlserverversion = resource.mysqlserverversion
				updateresource.mysqlcharacterset = resource.mysqlcharacterset
				updateresource.mysqlservercapabilities = resource.mysqlservercapabilities
				updateresource.appflowlog = resource.appflowlog
				updateresource.netprofile = resource.netprofile
				updateresource.icmpvsrresponse = resource.icmpvsrresponse
				updateresource.rhistate = resource.rhistate
				updateresource.newservicerequest = resource.newservicerequest
				updateresource.newservicerequestunit = resource.newservicerequestunit
				updateresource.newservicerequestincrementinterval = resource.newservicerequestincrementinterval
				updateresource.minautoscalemembers = resource.minautoscalemembers
				updateresource.maxautoscalemembers = resource.maxautoscalemembers
				updateresource.persistavpno = resource.persistavpno
				updateresource.skippersistency = resource.skippersistency
				updateresource.authnprofile = resource.authnprofile
				updateresource.macmoderetainvlan = resource.macmoderetainvlan
				updateresource.dbslb = resource.dbslb
				updateresource.dns64 = resource.dns64
				updateresource.bypassaaaa = resource.bypassaaaa
				updateresource.recursionavailable = resource.recursionavailable
				updateresource.processlocal = resource.processlocal
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lbvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipv46 = resource[i].ipv46
						updateresources[i].ippattern = resource[i].ippattern
						updateresources[i].ipmask = resource[i].ipmask
						updateresources[i].weight = resource[i].weight
						updateresources[i].servicename = resource[i].servicename
						updateresources[i].persistencetype = resource[i].persistencetype
						updateresources[i].timeout = resource[i].timeout
						updateresources[i].persistencebackup = resource[i].persistencebackup
						updateresources[i].backuppersistencetimeout = resource[i].backuppersistencetimeout
						updateresources[i].lbmethod = resource[i].lbmethod
						updateresources[i].hashlength = resource[i].hashlength
						updateresources[i].netmask = resource[i].netmask
						updateresources[i].v6netmasklen = resource[i].v6netmasklen
						updateresources[i].rule = resource[i].rule
						updateresources[i].cookiename = resource[i].cookiename
						updateresources[i].resrule = resource[i].resrule
						updateresources[i].persistmask = resource[i].persistmask
						updateresources[i].v6persistmasklen = resource[i].v6persistmasklen
						updateresources[i].pq = resource[i].pq
						updateresources[i].sc = resource[i].sc
						updateresources[i].rtspnat = resource[i].rtspnat
						updateresources[i].m = resource[i].m
						updateresources[i].tosid = resource[i].tosid
						updateresources[i].datalength = resource[i].datalength
						updateresources[i].dataoffset = resource[i].dataoffset
						updateresources[i].sessionless = resource[i].sessionless
						updateresources[i].connfailover = resource[i].connfailover
						updateresources[i].backupvserver = resource[i].backupvserver
						updateresources[i].redirurl = resource[i].redirurl
						updateresources[i].cacheable = resource[i].cacheable
						updateresources[i].clttimeout = resource[i].clttimeout
						updateresources[i].somethod = resource[i].somethod
						updateresources[i].sothreshold = resource[i].sothreshold
						updateresources[i].sopersistence = resource[i].sopersistence
						updateresources[i].sopersistencetimeout = resource[i].sopersistencetimeout
						updateresources[i].healththreshold = resource[i].healththreshold
						updateresources[i].sobackupaction = resource[i].sobackupaction
						updateresources[i].redirectportrewrite = resource[i].redirectportrewrite
						updateresources[i].downstateflush = resource[i].downstateflush
						updateresources[i].insertvserveripport = resource[i].insertvserveripport
						updateresources[i].vipheader = resource[i].vipheader
						updateresources[i].disableprimaryondown = resource[i].disableprimaryondown
						updateresources[i].authenticationhost = resource[i].authenticationhost
						updateresources[i].authentication = resource[i].authentication
						updateresources[i].authn401 = resource[i].authn401
						updateresources[i].authnvsname = resource[i].authnvsname
						updateresources[i].push = resource[i].push
						updateresources[i].pushvserver = resource[i].pushvserver
						updateresources[i].pushlabel = resource[i].pushlabel
						updateresources[i].pushmulticlients = resource[i].pushmulticlients
						updateresources[i].listenpolicy = resource[i].listenpolicy
						updateresources[i].listenpriority = resource[i].listenpriority
						updateresources[i].tcpprofilename = resource[i].tcpprofilename
						updateresources[i].httpprofilename = resource[i].httpprofilename
						updateresources[i].dbprofilename = resource[i].dbprofilename
						updateresources[i].comment = resource[i].comment
						updateresources[i].l2conn = resource[i].l2conn
						updateresources[i].oracleserverversion = resource[i].oracleserverversion
						updateresources[i].mssqlserverversion = resource[i].mssqlserverversion
						updateresources[i].mysqlprotocolversion = resource[i].mysqlprotocolversion
						updateresources[i].mysqlserverversion = resource[i].mysqlserverversion
						updateresources[i].mysqlcharacterset = resource[i].mysqlcharacterset
						updateresources[i].mysqlservercapabilities = resource[i].mysqlservercapabilities
						updateresources[i].appflowlog = resource[i].appflowlog
						updateresources[i].netprofile = resource[i].netprofile
						updateresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						updateresources[i].rhistate = resource[i].rhistate
						updateresources[i].newservicerequest = resource[i].newservicerequest
						updateresources[i].newservicerequestunit = resource[i].newservicerequestunit
						updateresources[i].newservicerequestincrementinterval = resource[i].newservicerequestincrementinterval
						updateresources[i].minautoscalemembers = resource[i].minautoscalemembers
						updateresources[i].maxautoscalemembers = resource[i].maxautoscalemembers
						updateresources[i].persistavpno = resource[i].persistavpno
						updateresources[i].skippersistency = resource[i].skippersistency
						updateresources[i].authnprofile = resource[i].authnprofile
						updateresources[i].macmoderetainvlan = resource[i].macmoderetainvlan
						updateresources[i].dbslb = resource[i].dbslb
						updateresources[i].dns64 = resource[i].dns64
						updateresources[i].bypassaaaa = resource[i].bypassaaaa
						updateresources[i].recursionavailable = resource[i].recursionavailable
						updateresources[i].processlocal = resource[i].processlocal
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lbvserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbvserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable lbvserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = lbvserver()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable lbvserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = lbvserver()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ lbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a lbvserver resource.
		"""
		try :
			renameresource = lbvserver()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lbvserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbvserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lbvserver()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lbvserver() for _ in range(len(name))]
							obj = [lbvserver() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lbvserver()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lbvserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbvserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lbvserver resources configured on NetScaler.
		"""
		try :
			obj = lbvserver()
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
		ur""" Use this API to count filtered the set of lbvserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbvserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Oracleserverversion:
		_10G = "10G"
		_11G = "11G"

	class Sc:
		ON = "ON"
		OFF = "OFF"

	class Pq:
		ON = "ON"
		OFF = "OFF"

	class Rhistate:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Macmoderetainvlan:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Authentication:
		ON = "ON"
		OFF = "OFF"

	class Redirectportrewrite:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Map:
		ON = "ON"
		OFF = "OFF"

	class Skippersistency:
		Bypass = "Bypass"
		ReLb = "ReLb"
		NONE = "None"

	class Dbslb:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Newservicerequestunit:
		PER_SECOND = "PER_SECOND"
		PERCENT = "PERCENT"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

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
		DNS = "DNS"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		DNS_TCP = "DNS_TCP"
		RTSP = "RTSP"
		PUSH = "PUSH"
		SSL_PUSH = "SSL_PUSH"
		RADIUS = "RADIUS"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"

	class Icmpvsrresponse:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Sessionless:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class L2conn:
		ON = "ON"
		OFF = "OFF"

	class Sobackupaction:
		DROP = "DROP"
		ACCEPT = "ACCEPT"
		REDIRECT = "REDIRECT"

	class Gt2gb:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Push:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		CONTENT = "CONTENT"
		ADDRESS = "ADDRESS"

	class Disableprimaryondown:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rtspnat:
		ON = "ON"
		OFF = "OFF"

	class Authn401:
		ON = "ON"
		OFF = "OFF"

	class Cacheable:
		YES = "YES"
		NO = "NO"

	class Processlocal:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Somethod:
		CONNECTION = "CONNECTION"
		DYNAMICCONNECTION = "DYNAMICCONNECTION"
		BANDWIDTH = "BANDWIDTH"
		HEALTH = "HEALTH"
		NONE = "NONE"

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"

	class Consolidatedlconn:
		GLOBAL = "GLOBAL"
		NO = "NO"
		YES = "YES"

	class Sopersistence:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Lbmethod:
		ROUNDROBIN = "ROUNDROBIN"
		LEASTCONNECTION = "LEASTCONNECTION"
		LEASTRESPONSETIME = "LEASTRESPONSETIME"
		URLHASH = "URLHASH"
		DOMAINHASH = "DOMAINHASH"
		DESTINATIONIPHASH = "DESTINATIONIPHASH"
		SOURCEIPHASH = "SOURCEIPHASH"
		SRCIPDESTIPHASH = "SRCIPDESTIPHASH"
		LEASTBANDWIDTH = "LEASTBANDWIDTH"
		LEASTPACKETS = "LEASTPACKETS"
		TOKEN = "TOKEN"
		SRCIPSRCPORTHASH = "SRCIPSRCPORTHASH"
		LRTM = "LRTM"
		CALLIDHASH = "CALLIDHASH"
		CUSTOMLOAD = "CUSTOMLOAD"
		LEASTREQUEST = "LEASTREQUEST"

	class Consolidatedlconngbl:
		YES = "YES"
		NO = "NO"

	class Redirect:
		CACHE = "CACHE"
		POLICY = "POLICY"
		ORIGIN = "ORIGIN"

	class Effectivestate:
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

	class Bypassaaaa:
		YES = "YES"
		NO = "NO"

	class Connfailover:
		DISABLED = "DISABLED"
		STATEFUL = "STATEFUL"
		STATELESS = "STATELESS"

	class Pushmulticlients:
		YES = "YES"
		NO = "NO"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

	class Persistencebackup:
		SOURCEIP = "SOURCEIP"
		NONE = "NONE"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class M:
		IP = "IP"
		MAC = "MAC"
		IPTUNNEL = "IPTUNNEL"
		TOS = "TOS"

	class Precedence:
		RULE = "RULE"
		URL = "URL"

	class Dns64:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Curstate:
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

	class Persistencetype:
		SOURCEIP = "SOURCEIP"
		COOKIEINSERT = "COOKIEINSERT"
		SSLSESSION = "SSLSESSION"
		RULE = "RULE"
		URLPASSIVE = "URLPASSIVE"
		CUSTOMSERVERID = "CUSTOMSERVERID"
		DESTIP = "DESTIP"
		SRCIPDESTIP = "SRCIPDESTIP"
		CALLID = "CALLID"
		RTSPSID = "RTSPSID"
		DIAMETER = "DIAMETER"
		NONE = "NONE"

	class Insertvserveripport:
		OFF = "OFF"
		VIPADDR = "VIPADDR"
		V6TOV4MAPPING = "V6TOV4MAPPING"

	class Recursionavailable:
		YES = "YES"
		NO = "NO"

	class Mssqlserverversion:
		_70 = "70"
		_2000 = "2000"
		_2000SP1 = "2000SP1"
		_2005 = "2005"
		_2008 = "2008"
		_2008R2 = "2008R2"
		_2012 = "2012"

class lbvserver_response(base_response) :
	def __init__(self, length=1) :
		self.lbvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbvserver = [lbvserver() for _ in range(length)]

