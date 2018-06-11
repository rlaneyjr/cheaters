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

class lbmonitor(base_resource) :
	""" Configuration for monitor resource. """
	def __init__(self) :
		self._monitorname = ""
		self._type = ""
		self._action = ""
		self._respcode = []
		self._httprequest = ""
		self._rtsprequest = ""
		self._customheaders = ""
		self._maxforwards = 0
		self._sipmethod = ""
		self._sipuri = ""
		self._sipreguri = ""
		self._send = ""
		self._recv = ""
		self._query = ""
		self._querytype = ""
		self._scriptname = ""
		self._scriptargs = ""
		self._dispatcherip = ""
		self._dispatcherport = 0
		self._username = ""
		self._password = ""
		self._secondarypassword = ""
		self._logonpointname = ""
		self._lasversion = ""
		self._radkey = ""
		self._radnasid = ""
		self._radnasip = ""
		self._radaccounttype = 0
		self._radframedip = ""
		self._radapn = ""
		self._radmsisdn = ""
		self._radaccountsession = ""
		self._lrtm = ""
		self._deviation = 0
		self._units1 = ""
		self._interval = 0
		self._units3 = ""
		self._resptimeout = 0
		self._units4 = ""
		self._resptimeoutthresh = 0
		self._retries = 0
		self._failureretries = 0
		self._alertretries = 0
		self._successretries = 0
		self._downtime = 0
		self._units2 = ""
		self._destip = ""
		self._destport = 0
		self._state = ""
		self._reverse = ""
		self._transparent = ""
		self._iptunnel = ""
		self._tos = ""
		self._tosid = 0
		self._secure = ""
		self._validatecred = ""
		self._domain = ""
		self._ipaddress = []
		self._group = ""
		self._filename = ""
		self._basedn = ""
		self._binddn = ""
		self._filter = ""
		self._attribute = ""
		self._database = ""
		self._oraclesid = ""
		self._sqlquery = ""
		self._evalrule = ""
		self._mssqlprotocolversion = ""
		self._Snmpoid = ""
		self._snmpcommunity = ""
		self._snmpthreshold = ""
		self._snmpversion = ""
		self._metrictable = ""
		self._application = ""
		self._sitepath = ""
		self._storename = ""
		self._storefrontacctservice = ""
		self._hostname = ""
		self._netprofile = ""
		self._originhost = ""
		self._originrealm = ""
		self._hostipaddress = ""
		self._vendorid = 0
		self._productname = ""
		self._firmwarerevision = 0
		self._authapplicationid = []
		self._acctapplicationid = []
		self._inbandsecurityid = ""
		self._supportedvendorids = []
		self._vendorspecificvendorid = 0
		self._vendorspecificauthapplicationids = []
		self._vendorspecificacctapplicationids = []
		self._kcdaccount = ""
		self._storedb = ""
		self._storefrontcheckbackendservices = ""
		self._metric = ""
		self._metricthreshold = 0
		self._metricweight = 0
		self._servicename = ""
		self._servicegroupname = ""
		self._lrtmconf = 0
		self._lrtmconfstr = ""
		self._dynamicresponsetimeout = 0
		self._dynamicinterval = 0
		self._multimetrictable = []
		self._dup_state = ""
		self._dup_weight = 0
		self._weight = 0
		self.___count = 0

	@property
	def monitorname(self) :
		ur"""Name for the monitor. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		CLI Users:  If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my monitor" or 'my monitor').<br/>Minimum length =  1.
		"""
		try :
			return self._monitorname
		except Exception as e:
			raise e

	@monitorname.setter
	def monitorname(self, monitorname) :
		ur"""Name for the monitor. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		CLI Users:  If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my monitor" or 'my monitor').<br/>Minimum length =  1
		"""
		try :
			self._monitorname = monitorname
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of monitor that you want to create.<br/>Possible values = PING, TCP, HTTP, TCP-ECV, HTTP-ECV, UDP-ECV, DNS, FTP, LDNS-PING, LDNS-TCP, LDNS-DNS, RADIUS, USER, HTTP-INLINE, SIP-UDP, LOAD, FTP-EXTENDED, SMTP, SNMP, NNTP, MYSQL, MYSQL-ECV, MSSQL-ECV, ORACLE-ECV, LDAP, POP3, CITRIX-XML-SERVICE, CITRIX-WEB-INTERFACE, DNS-TCP, RTSP, ARP, CITRIX-AG, CITRIX-AAC-LOGINPAGE, CITRIX-AAC-LAS, CITRIX-XD-DDC, ND6, CITRIX-WI-EXTENDED, DIAMETER, RADIUS_ACCOUNTING, STOREFRONT, APPC, CITRIX-XNC-ECV, CITRIX-XDM.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of monitor that you want to create.<br/>Possible values = PING, TCP, HTTP, TCP-ECV, HTTP-ECV, UDP-ECV, DNS, FTP, LDNS-PING, LDNS-TCP, LDNS-DNS, RADIUS, USER, HTTP-INLINE, SIP-UDP, LOAD, FTP-EXTENDED, SMTP, SNMP, NNTP, MYSQL, MYSQL-ECV, MSSQL-ECV, ORACLE-ECV, LDAP, POP3, CITRIX-XML-SERVICE, CITRIX-WEB-INTERFACE, DNS-TCP, RTSP, ARP, CITRIX-AG, CITRIX-AAC-LOGINPAGE, CITRIX-AAC-LAS, CITRIX-XD-DDC, ND6, CITRIX-WI-EXTENDED, DIAMETER, RADIUS_ACCOUNTING, STOREFRONT, APPC, CITRIX-XNC-ECV, CITRIX-XDM
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def action(self) :
		ur"""Action to perform when the response to an inline monitor (a monitor of type HTTP-INLINE) indicates that the service is down. A service monitored by an inline monitor is considered DOWN if the response code is not one of the codes that have been specified for the Response Code parameter. 
		Available settings function as follows: 
		* NONE - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.
		* LOG - Log the event in NSLOG or SYSLOG. 
		* DOWN - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as DOWN. Also, log the event in NSLOG or SYSLOG.<br/>Default value: DOWN<br/>Possible values = NONE, LOG, DOWN.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		ur"""Action to perform when the response to an inline monitor (a monitor of type HTTP-INLINE) indicates that the service is down. A service monitored by an inline monitor is considered DOWN if the response code is not one of the codes that have been specified for the Response Code parameter. 
		Available settings function as follows: 
		* NONE - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.
		* LOG - Log the event in NSLOG or SYSLOG. 
		* DOWN - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as DOWN. Also, log the event in NSLOG or SYSLOG.<br/>Default value: DOWN<br/>Possible values = NONE, LOG, DOWN
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def respcode(self) :
		ur"""Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. HTTP monitors and RADIUS monitors mark the service as DOWN, while HTTP-INLINE monitors perform the action indicated by the Action parameter.
		"""
		try :
			return self._respcode
		except Exception as e:
			raise e

	@respcode.setter
	def respcode(self, respcode) :
		ur"""Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. HTTP monitors and RADIUS monitors mark the service as DOWN, while HTTP-INLINE monitors perform the action indicated by the Action parameter.
		"""
		try :
			self._respcode = respcode
		except Exception as e:
			raise e

	@property
	def httprequest(self) :
		ur"""HTTP request to send to the server (for example, "HEAD /file.html").
		"""
		try :
			return self._httprequest
		except Exception as e:
			raise e

	@httprequest.setter
	def httprequest(self, httprequest) :
		ur"""HTTP request to send to the server (for example, "HEAD /file.html").
		"""
		try :
			self._httprequest = httprequest
		except Exception as e:
			raise e

	@property
	def rtsprequest(self) :
		ur"""RTSP request to send to the server (for example, "OPTIONS *").
		"""
		try :
			return self._rtsprequest
		except Exception as e:
			raise e

	@rtsprequest.setter
	def rtsprequest(self, rtsprequest) :
		ur"""RTSP request to send to the server (for example, "OPTIONS *").
		"""
		try :
			self._rtsprequest = rtsprequest
		except Exception as e:
			raise e

	@property
	def customheaders(self) :
		ur"""Custom header string to include in the monitoring probes.
		"""
		try :
			return self._customheaders
		except Exception as e:
			raise e

	@customheaders.setter
	def customheaders(self, customheaders) :
		ur"""Custom header string to include in the monitoring probes.
		"""
		try :
			self._customheaders = customheaders
		except Exception as e:
			raise e

	@property
	def maxforwards(self) :
		ur"""Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type SIP-UDP.<br/>Default value: 1<br/>Maximum length =  255.
		"""
		try :
			return self._maxforwards
		except Exception as e:
			raise e

	@maxforwards.setter
	def maxforwards(self, maxforwards) :
		ur"""Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type SIP-UDP.<br/>Default value: 1<br/>Maximum length =  255
		"""
		try :
			self._maxforwards = maxforwards
		except Exception as e:
			raise e

	@property
	def sipmethod(self) :
		ur"""SIP method to use for the query. Applicable only to monitors of type SIP-UDP.<br/>Possible values = OPTIONS, INVITE, REGISTER.
		"""
		try :
			return self._sipmethod
		except Exception as e:
			raise e

	@sipmethod.setter
	def sipmethod(self, sipmethod) :
		ur"""SIP method to use for the query. Applicable only to monitors of type SIP-UDP.<br/>Possible values = OPTIONS, INVITE, REGISTER
		"""
		try :
			self._sipmethod = sipmethod
		except Exception as e:
			raise e

	@property
	def sipuri(self) :
		ur"""SIP URI string to send to the service (for example, sip:sip.test). Applicable only to monitors of type SIP-UDP.<br/>Minimum length =  1.
		"""
		try :
			return self._sipuri
		except Exception as e:
			raise e

	@sipuri.setter
	def sipuri(self, sipuri) :
		ur"""SIP URI string to send to the service (for example, sip:sip.test). Applicable only to monitors of type SIP-UDP.<br/>Minimum length =  1
		"""
		try :
			self._sipuri = sipuri
		except Exception as e:
			raise e

	@property
	def sipreguri(self) :
		ur"""SIP user to be registered. Applicable only if the monitor is of type SIP-UDP and the SIP Method parameter is set to REGISTER.<br/>Minimum length =  1.
		"""
		try :
			return self._sipreguri
		except Exception as e:
			raise e

	@sipreguri.setter
	def sipreguri(self, sipreguri) :
		ur"""SIP user to be registered. Applicable only if the monitor is of type SIP-UDP and the SIP Method parameter is set to REGISTER.<br/>Minimum length =  1
		"""
		try :
			self._sipreguri = sipreguri
		except Exception as e:
			raise e

	@property
	def send(self) :
		ur"""String to send to the service. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			return self._send
		except Exception as e:
			raise e

	@send.setter
	def send(self, send) :
		ur"""String to send to the service. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			self._send = send
		except Exception as e:
			raise e

	@property
	def recv(self) :
		ur"""String expected from the server for the service to be marked as UP. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			return self._recv
		except Exception as e:
			raise e

	@recv.setter
	def recv(self, recv) :
		ur"""String expected from the server for the service to be marked as UP. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			self._recv = recv
		except Exception as e:
			raise e

	@property
	def query(self) :
		ur"""Domain name to resolve as part of monitoring the DNS service (for example, example.com).
		"""
		try :
			return self._query
		except Exception as e:
			raise e

	@query.setter
	def query(self, query) :
		ur"""Domain name to resolve as part of monitoring the DNS service (for example, example.com).
		"""
		try :
			self._query = query
		except Exception as e:
			raise e

	@property
	def querytype(self) :
		ur"""Type of DNS record for which to send monitoring queries. Set to Address for querying A records, AAAA for querying AAAA records, and Zone for querying the SOA record.<br/>Possible values = Address, Zone, AAAA.
		"""
		try :
			return self._querytype
		except Exception as e:
			raise e

	@querytype.setter
	def querytype(self, querytype) :
		ur"""Type of DNS record for which to send monitoring queries. Set to Address for querying A records, AAAA for querying AAAA records, and Zone for querying the SOA record.<br/>Possible values = Address, Zone, AAAA
		"""
		try :
			self._querytype = querytype
		except Exception as e:
			raise e

	@property
	def scriptname(self) :
		ur"""Path and name of the script to execute. The script must be available on the NetScaler appliance, in the /nsconfig/monitors/ directory.<br/>Minimum length =  1.
		"""
		try :
			return self._scriptname
		except Exception as e:
			raise e

	@scriptname.setter
	def scriptname(self, scriptname) :
		ur"""Path and name of the script to execute. The script must be available on the NetScaler appliance, in the /nsconfig/monitors/ directory.<br/>Minimum length =  1
		"""
		try :
			self._scriptname = scriptname
		except Exception as e:
			raise e

	@property
	def scriptargs(self) :
		ur"""String of arguments for the script. The string is copied verbatim into the request.
		"""
		try :
			return self._scriptargs
		except Exception as e:
			raise e

	@scriptargs.setter
	def scriptargs(self, scriptargs) :
		ur"""String of arguments for the script. The string is copied verbatim into the request.
		"""
		try :
			self._scriptargs = scriptargs
		except Exception as e:
			raise e

	@property
	def dispatcherip(self) :
		ur"""IP address of the dispatcher to which to send the probe.
		"""
		try :
			return self._dispatcherip
		except Exception as e:
			raise e

	@dispatcherip.setter
	def dispatcherip(self, dispatcherip) :
		ur"""IP address of the dispatcher to which to send the probe.
		"""
		try :
			self._dispatcherip = dispatcherip
		except Exception as e:
			raise e

	@property
	def dispatcherport(self) :
		ur"""Port number on which the dispatcher listens for the monitoring probe.
		"""
		try :
			return self._dispatcherport
		except Exception as e:
			raise e

	@dispatcherport.setter
	def dispatcherport(self, dispatcherport) :
		ur"""Port number on which the dispatcher listens for the monitoring probe.
		"""
		try :
			self._dispatcherport = dispatcherport
		except Exception as e:
			raise e

	@property
	def username(self) :
		ur"""User name with which to probe the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC or CITRIX-XDM server.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""User name with which to probe the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC or CITRIX-XDM server.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password that is required for logging on to the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC-ECV or CITRIX-XDM server. Used in conjunction with the user name specified for the User Name parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password that is required for logging on to the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC-ECV or CITRIX-XDM server. Used in conjunction with the user name specified for the User Name parameter.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def secondarypassword(self) :
		ur"""Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to CITRIX-AG monitors.
		"""
		try :
			return self._secondarypassword
		except Exception as e:
			raise e

	@secondarypassword.setter
	def secondarypassword(self, secondarypassword) :
		ur"""Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to CITRIX-AG monitors.
		"""
		try :
			self._secondarypassword = secondarypassword
		except Exception as e:
			raise e

	@property
	def logonpointname(self) :
		ur"""Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to CITRIX-AAC-LAS and CITRIX-AAC-LOGINPAGE monitors.
		"""
		try :
			return self._logonpointname
		except Exception as e:
			raise e

	@logonpointname.setter
	def logonpointname(self, logonpointname) :
		ur"""Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to CITRIX-AAC-LAS and CITRIX-AAC-LOGINPAGE monitors.
		"""
		try :
			self._logonpointname = logonpointname
		except Exception as e:
			raise e

	@property
	def lasversion(self) :
		ur"""Version number of the Citrix Advanced Access Control Logon Agent. Required by the CITRIX-AAC-LAS monitor.
		"""
		try :
			return self._lasversion
		except Exception as e:
			raise e

	@lasversion.setter
	def lasversion(self, lasversion) :
		ur"""Version number of the Citrix Advanced Access Control Logon Agent. Required by the CITRIX-AAC-LAS monitor.
		"""
		try :
			self._lasversion = lasversion
		except Exception as e:
			raise e

	@property
	def radkey(self) :
		ur"""Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radkey
		except Exception as e:
			raise e

	@radkey.setter
	def radkey(self, radkey) :
		ur"""Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radkey = radkey
		except Exception as e:
			raise e

	@property
	def radnasid(self) :
		ur"""NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type RADIUS.<br/>Minimum length =  1.
		"""
		try :
			return self._radnasid
		except Exception as e:
			raise e

	@radnasid.setter
	def radnasid(self, radnasid) :
		ur"""NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type RADIUS.<br/>Minimum length =  1
		"""
		try :
			self._radnasid = radnasid
		except Exception as e:
			raise e

	@property
	def radnasip(self) :
		ur"""Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.
		"""
		try :
			return self._radnasip
		except Exception as e:
			raise e

	@radnasip.setter
	def radnasip(self, radnasip) :
		ur"""Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.
		"""
		try :
			self._radnasip = radnasip
		except Exception as e:
			raise e

	@property
	def radaccounttype(self) :
		ur"""Account Type to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Default value: 1<br/>Maximum length =  15.
		"""
		try :
			return self._radaccounttype
		except Exception as e:
			raise e

	@radaccounttype.setter
	def radaccounttype(self, radaccounttype) :
		ur"""Account Type to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Default value: 1<br/>Maximum length =  15
		"""
		try :
			self._radaccounttype = radaccounttype
		except Exception as e:
			raise e

	@property
	def radframedip(self) :
		ur"""Source ip with which the packet will go out . Applicable to monitors of type RADIUS_ACCOUNTING.
		"""
		try :
			return self._radframedip
		except Exception as e:
			raise e

	@radframedip.setter
	def radframedip(self, radframedip) :
		ur"""Source ip with which the packet will go out . Applicable to monitors of type RADIUS_ACCOUNTING.
		"""
		try :
			self._radframedip = radframedip
		except Exception as e:
			raise e

	@property
	def radapn(self) :
		ur"""Called Station Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radapn
		except Exception as e:
			raise e

	@radapn.setter
	def radapn(self, radapn) :
		ur"""Called Station Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radapn = radapn
		except Exception as e:
			raise e

	@property
	def radmsisdn(self) :
		ur"""Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radmsisdn
		except Exception as e:
			raise e

	@radmsisdn.setter
	def radmsisdn(self, radmsisdn) :
		ur"""Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radmsisdn = radmsisdn
		except Exception as e:
			raise e

	@property
	def radaccountsession(self) :
		ur"""Account Session ID to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radaccountsession
		except Exception as e:
			raise e

	@radaccountsession.setter
	def radaccountsession(self, radaccountsession) :
		ur"""Account Session ID to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radaccountsession = radaccountsession
		except Exception as e:
			raise e

	@property
	def lrtm(self) :
		ur"""Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._lrtm
		except Exception as e:
			raise e

	@lrtm.setter
	def lrtm(self, lrtm) :
		ur"""Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._lrtm = lrtm
		except Exception as e:
			raise e

	@property
	def deviation(self) :
		ur"""Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.<br/>Maximum length =  20939000.
		"""
		try :
			return self._deviation
		except Exception as e:
			raise e

	@deviation.setter
	def deviation(self, deviation) :
		ur"""Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.<br/>Maximum length =  20939000
		"""
		try :
			self._deviation = deviation
		except Exception as e:
			raise e

	@property
	def units1(self) :
		ur"""Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units1
		except Exception as e:
			raise e

	@units1.setter
	def units1(self, units1) :
		ur"""Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units1 = units1
		except Exception as e:
			raise e

	@property
	def interval(self) :
		ur"""Time interval between two successive probes. Must be greater than the value of Response Time-out.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  20940000.
		"""
		try :
			return self._interval
		except Exception as e:
			raise e

	@interval.setter
	def interval(self, interval) :
		ur"""Time interval between two successive probes. Must be greater than the value of Response Time-out.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  20940000
		"""
		try :
			self._interval = interval
		except Exception as e:
			raise e

	@property
	def units3(self) :
		ur"""monitor interval units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units3
		except Exception as e:
			raise e

	@units3.setter
	def units3(self, units3) :
		ur"""monitor interval units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units3 = units3
		except Exception as e:
			raise e

	@property
	def resptimeout(self) :
		ur"""Amount of time for which the appliance must wait before it marks a probe as FAILED.  Must be less than the value specified for the Interval parameter.
		Note: For UDP-ECV monitors for which a receive string is not configured, response timeout does not apply. For UDP-ECV monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  20939000.
		"""
		try :
			return self._resptimeout
		except Exception as e:
			raise e

	@resptimeout.setter
	def resptimeout(self, resptimeout) :
		ur"""Amount of time for which the appliance must wait before it marks a probe as FAILED.  Must be less than the value specified for the Interval parameter.
		Note: For UDP-ECV monitors for which a receive string is not configured, response timeout does not apply. For UDP-ECV monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  20939000
		"""
		try :
			self._resptimeout = resptimeout
		except Exception as e:
			raise e

	@property
	def units4(self) :
		ur"""monitor response timeout units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units4
		except Exception as e:
			raise e

	@units4.setter
	def units4(self, units4) :
		ur"""monitor response timeout units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units4 = units4
		except Exception as e:
			raise e

	@property
	def resptimeoutthresh(self) :
		ur"""Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.<br/>Maximum length =  100.
		"""
		try :
			return self._resptimeoutthresh
		except Exception as e:
			raise e

	@resptimeoutthresh.setter
	def resptimeoutthresh(self, resptimeoutthresh) :
		ur"""Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.<br/>Maximum length =  100
		"""
		try :
			self._resptimeoutthresh = resptimeoutthresh
		except Exception as e:
			raise e

	@property
	def retries(self) :
		ur"""Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._retries
		except Exception as e:
			raise e

	@retries.setter
	def retries(self, retries) :
		ur"""Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._retries = retries
		except Exception as e:
			raise e

	@property
	def failureretries(self) :
		ur"""Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.<br/>Maximum length =  32.
		"""
		try :
			return self._failureretries
		except Exception as e:
			raise e

	@failureretries.setter
	def failureretries(self, failureretries) :
		ur"""Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.<br/>Maximum length =  32
		"""
		try :
			self._failureretries = failureretries
		except Exception as e:
			raise e

	@property
	def alertretries(self) :
		ur"""Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.<br/>Maximum length =  32.
		"""
		try :
			return self._alertretries
		except Exception as e:
			raise e

	@alertretries.setter
	def alertretries(self, alertretries) :
		ur"""Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.<br/>Maximum length =  32
		"""
		try :
			self._alertretries = alertretries
		except Exception as e:
			raise e

	@property
	def successretries(self) :
		ur"""Number of consecutive successful probes required to transition a service's state from DOWN to UP.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._successretries
		except Exception as e:
			raise e

	@successretries.setter
	def successretries(self, successretries) :
		ur"""Number of consecutive successful probes required to transition a service's state from DOWN to UP.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._successretries = successretries
		except Exception as e:
			raise e

	@property
	def downtime(self) :
		ur"""Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  20939000.
		"""
		try :
			return self._downtime
		except Exception as e:
			raise e

	@downtime.setter
	def downtime(self, downtime) :
		ur"""Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  20939000
		"""
		try :
			self._downtime = downtime
		except Exception as e:
			raise e

	@property
	def units2(self) :
		ur"""Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units2
		except Exception as e:
			raise e

	@units2.setter
	def units2(self, units2) :
		ur"""Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units2 = units2
		except Exception as e:
			raise e

	@property
	def destip(self) :
		ur"""IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		ur"""IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		ur"""TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type USER, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type PING.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		ur"""TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type USER, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type PING.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of the monitor. The DISABLED setting disables not only the monitor being configured, but all monitors of the same type, until the parameter is set to ENABLED. If the monitor is bound to a service, the state of the monitor is not taken into account when the state of the service is determined.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""State of the monitor. The DISABLED setting disables not only the monitor being configured, but all monitors of the same type, until the parameter is set to ENABLED. If the monitor is bound to a service, the state of the monitor is not taken into account when the state of the service is determined.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def reverse(self) :
		ur"""Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._reverse
		except Exception as e:
			raise e

	@reverse.setter
	def reverse(self, reverse) :
		ur"""Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._reverse = reverse
		except Exception as e:
			raise e

	@property
	def transparent(self) :
		ur"""The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._transparent
		except Exception as e:
			raise e

	@transparent.setter
	def transparent(self, transparent) :
		ur"""The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._transparent = transparent
		except Exception as e:
			raise e

	@property
	def iptunnel(self) :
		ur"""Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._iptunnel
		except Exception as e:
			raise e

	@iptunnel.setter
	def iptunnel(self, iptunnel) :
		ur"""Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._iptunnel = iptunnel
		except Exception as e:
			raise e

	@property
	def tos(self) :
		ur"""Probe the service by encoding the destination IP address in the IP TOS (6) bits.<br/>Possible values = YES, NO.
		"""
		try :
			return self._tos
		except Exception as e:
			raise e

	@tos.setter
	def tos(self, tos) :
		ur"""Probe the service by encoding the destination IP address in the IP TOS (6) bits.<br/>Possible values = YES, NO
		"""
		try :
			self._tos = tos
		except Exception as e:
			raise e

	@property
	def tosid(self) :
		ur"""The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.<br/>Minimum length =  1<br/>Maximum length =  63.
		"""
		try :
			return self._tosid
		except Exception as e:
			raise e

	@tosid.setter
	def tosid(self, tosid) :
		ur"""The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.<br/>Minimum length =  1<br/>Maximum length =  63
		"""
		try :
			self._tosid = tosid
		except Exception as e:
			raise e

	@property
	def secure(self) :
		ur"""Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a CITRIX-AG monitor, because a CITRIX-AG monitor uses a secure connection by default.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._secure
		except Exception as e:
			raise e

	@secure.setter
	def secure(self, secure) :
		ur"""Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a CITRIX-AG monitor, because a CITRIX-AG monitor uses a secure connection by default.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._secure = secure
		except Exception as e:
			raise e

	@property
	def validatecred(self) :
		ur"""Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type CITRIX-XD-DDC.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._validatecred
		except Exception as e:
			raise e

	@validatecred.setter
	def validatecred(self, validatecred) :
		ur"""Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type CITRIX-XD-DDC.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._validatecred = validatecred
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by CITRIX-XD-DDC and CITRIX-WI-EXTENDED monitors for logging on to the DDC servers and Web Interface servers, respectively.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by CITRIX-XD-DDC and CITRIX-WI-EXTENDED monitors for logging on to the DDC servers and Web Interface servers, respectively.
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to DNS monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to DNS monitors.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def group(self) :
		ur"""Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._group
		except Exception as e:
			raise e

	@group.setter
	def group(self, group) :
		ur"""Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.<br/>Minimum length =  1
		"""
		try :
			self._group = group
		except Exception as e:
			raise e

	@property
	def filename(self) :
		ur"""Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to FTP-EXTENDED monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		ur"""Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to FTP-EXTENDED monitors.<br/>Minimum length =  1
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def basedn(self) :
		ur"""The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for LDAP service monitoring.<br/>Minimum length =  1.
		"""
		try :
			return self._basedn
		except Exception as e:
			raise e

	@basedn.setter
	def basedn(self, basedn) :
		ur"""The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for LDAP service monitoring.<br/>Minimum length =  1
		"""
		try :
			self._basedn = basedn
		except Exception as e:
			raise e

	@property
	def binddn(self) :
		ur"""The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to LDAP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._binddn
		except Exception as e:
			raise e

	@binddn.setter
	def binddn(self, binddn) :
		ur"""The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to LDAP monitors.<br/>Minimum length =  1
		"""
		try :
			self._binddn = binddn
		except Exception as e:
			raise e

	@property
	def filter(self) :
		ur"""Filter criteria for the LDAP query. Optional.<br/>Minimum length =  1.
		"""
		try :
			return self._filter
		except Exception as e:
			raise e

	@filter.setter
	def filter(self, filter) :
		ur"""Filter criteria for the LDAP query. Optional.<br/>Minimum length =  1
		"""
		try :
			self._filter = filter
		except Exception as e:
			raise e

	@property
	def attribute(self) :
		ur"""Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.<br/>Minimum length =  1.
		"""
		try :
			return self._attribute
		except Exception as e:
			raise e

	@attribute.setter
	def attribute(self, attribute) :
		ur"""Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.<br/>Minimum length =  1
		"""
		try :
			self._attribute = attribute
		except Exception as e:
			raise e

	@property
	def database(self) :
		ur"""Name of the database to connect to during authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._database
		except Exception as e:
			raise e

	@database.setter
	def database(self, database) :
		ur"""Name of the database to connect to during authentication.<br/>Minimum length =  1
		"""
		try :
			self._database = database
		except Exception as e:
			raise e

	@property
	def oraclesid(self) :
		ur"""Name of the service identifier that is used to connect to the Oracle database during authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._oraclesid
		except Exception as e:
			raise e

	@oraclesid.setter
	def oraclesid(self, oraclesid) :
		ur"""Name of the service identifier that is used to connect to the Oracle database during authentication.<br/>Minimum length =  1
		"""
		try :
			self._oraclesid = oraclesid
		except Exception as e:
			raise e

	@property
	def sqlquery(self) :
		ur"""SQL query for a MYSQL-ECV or MSSQL-ECV monitor. Sent to the database server after the server authenticates the connection.<br/>Minimum length =  1.
		"""
		try :
			return self._sqlquery
		except Exception as e:
			raise e

	@sqlquery.setter
	def sqlquery(self, sqlquery) :
		ur"""SQL query for a MYSQL-ECV or MSSQL-ECV monitor. Sent to the database server after the server authenticates the connection.<br/>Minimum length =  1
		"""
		try :
			self._sqlquery = sqlquery
		except Exception as e:
			raise e

	@property
	def evalrule(self) :
		ur"""Default syntax expression that evaluates the database server's response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds. 
		For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule MYSQL.RES.ROW(10) .TEXT_ELEM(2).EQ("MySQL").
		"""
		try :
			return self._evalrule
		except Exception as e:
			raise e

	@evalrule.setter
	def evalrule(self, evalrule) :
		ur"""Default syntax expression that evaluates the database server's response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds. 
		For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule MYSQL.RES.ROW(10) .TEXT_ELEM(2).EQ("MySQL").
		"""
		try :
			self._evalrule = evalrule
		except Exception as e:
			raise e

	@property
	def mssqlprotocolversion(self) :
		ur"""Version of MSSQL server that is to be monitored.<br/>Default value: 70<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012.
		"""
		try :
			return self._mssqlprotocolversion
		except Exception as e:
			raise e

	@mssqlprotocolversion.setter
	def mssqlprotocolversion(self, mssqlprotocolversion) :
		ur"""Version of MSSQL server that is to be monitored.<br/>Default value: 70<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012
		"""
		try :
			self._mssqlprotocolversion = mssqlprotocolversion
		except Exception as e:
			raise e

	@property
	def Snmpoid(self) :
		ur"""SNMP OID for SNMP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._Snmpoid
		except Exception as e:
			raise e

	@Snmpoid.setter
	def Snmpoid(self, Snmpoid) :
		ur"""SNMP OID for SNMP monitors.<br/>Minimum length =  1
		"""
		try :
			self._Snmpoid = Snmpoid
		except Exception as e:
			raise e

	@property
	def snmpcommunity(self) :
		ur"""Community name for SNMP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._snmpcommunity
		except Exception as e:
			raise e

	@snmpcommunity.setter
	def snmpcommunity(self, snmpcommunity) :
		ur"""Community name for SNMP monitors.<br/>Minimum length =  1
		"""
		try :
			self._snmpcommunity = snmpcommunity
		except Exception as e:
			raise e

	@property
	def snmpthreshold(self) :
		ur"""Threshold for SNMP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._snmpthreshold
		except Exception as e:
			raise e

	@snmpthreshold.setter
	def snmpthreshold(self, snmpthreshold) :
		ur"""Threshold for SNMP monitors.<br/>Minimum length =  1
		"""
		try :
			self._snmpthreshold = snmpthreshold
		except Exception as e:
			raise e

	@property
	def snmpversion(self) :
		ur"""SNMP version to be used for SNMP monitors.<br/>Possible values = V1, V2.
		"""
		try :
			return self._snmpversion
		except Exception as e:
			raise e

	@snmpversion.setter
	def snmpversion(self, snmpversion) :
		ur"""SNMP version to be used for SNMP monitors.<br/>Possible values = V1, V2
		"""
		try :
			self._snmpversion = snmpversion
		except Exception as e:
			raise e

	@property
	def metrictable(self) :
		ur"""Metric table to which to bind metrics.<br/>Minimum length =  1<br/>Maximum length =  99.
		"""
		try :
			return self._metrictable
		except Exception as e:
			raise e

	@metrictable.setter
	def metrictable(self, metrictable) :
		ur"""Metric table to which to bind metrics.<br/>Minimum length =  1<br/>Maximum length =  99
		"""
		try :
			self._metrictable = metrictable
		except Exception as e:
			raise e

	@property
	def application(self) :
		ur"""Name of the application used to determine the state of the service. Applicable to monitors of type CITRIX-XML-SERVICE.<br/>Minimum length =  1.
		"""
		try :
			return self._application
		except Exception as e:
			raise e

	@application.setter
	def application(self, application) :
		ur"""Name of the application used to determine the state of the service. Applicable to monitors of type CITRIX-XML-SERVICE.<br/>Minimum length =  1
		"""
		try :
			self._application = application
		except Exception as e:
			raise e

	@property
	def sitepath(self) :
		ur"""URL of the logon page. For monitors of type CITRIX-WEB-INTERFACE, to monitor a dynamic page under the site path, terminate the site path with a slash (/). Applicable to CITRIX-WEB-INTERFACE, CITRIX-WI-EXTENDED and CITRIX-XDM monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._sitepath
		except Exception as e:
			raise e

	@sitepath.setter
	def sitepath(self, sitepath) :
		ur"""URL of the logon page. For monitors of type CITRIX-WEB-INTERFACE, to monitor a dynamic page under the site path, terminate the site path with a slash (/). Applicable to CITRIX-WEB-INTERFACE, CITRIX-WI-EXTENDED and CITRIX-XDM monitors.<br/>Minimum length =  1
		"""
		try :
			self._sitepath = sitepath
		except Exception as e:
			raise e

	@property
	def storename(self) :
		ur"""Store Name. For monitors of type STOREFRONT, STORENAME is an optional argument defining storefront service store name. Applicable to STOREFRONT monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._storename
		except Exception as e:
			raise e

	@storename.setter
	def storename(self, storename) :
		ur"""Store Name. For monitors of type STOREFRONT, STORENAME is an optional argument defining storefront service store name. Applicable to STOREFRONT monitors.<br/>Minimum length =  1
		"""
		try :
			self._storename = storename
		except Exception as e:
			raise e

	@property
	def storefrontacctservice(self) :
		ur"""Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._storefrontacctservice
		except Exception as e:
			raise e

	@storefrontacctservice.setter
	def storefrontacctservice(self, storefrontacctservice) :
		ur"""Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._storefrontacctservice = storefrontacctservice
		except Exception as e:
			raise e

	@property
	def hostname(self) :
		ur"""Hostname in the FQDN format (Example: porche.cars.org). Applicable to STOREFRONT monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._hostname
		except Exception as e:
			raise e

	@hostname.setter
	def hostname(self, hostname) :
		ur"""Hostname in the FQDN format (Example: porche.cars.org). Applicable to STOREFRONT monitors.<br/>Minimum length =  1
		"""
		try :
			self._hostname = hostname
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		ur"""Name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		ur"""Name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def originhost(self) :
		ur"""Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1.
		"""
		try :
			return self._originhost
		except Exception as e:
			raise e

	@originhost.setter
	def originhost(self, originhost) :
		ur"""Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1
		"""
		try :
			self._originhost = originhost
		except Exception as e:
			raise e

	@property
	def originrealm(self) :
		ur"""Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1.
		"""
		try :
			return self._originrealm
		except Exception as e:
			raise e

	@originrealm.setter
	def originrealm(self, originrealm) :
		ur"""Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1
		"""
		try :
			self._originrealm = originrealm
		except Exception as e:
			raise e

	@property
	def hostipaddress(self) :
		ur"""Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.<br/>Minimum length =  1.
		"""
		try :
			return self._hostipaddress
		except Exception as e:
			raise e

	@hostipaddress.setter
	def hostipaddress(self, hostipaddress) :
		ur"""Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.<br/>Minimum length =  1
		"""
		try :
			self._hostipaddress = hostipaddress
		except Exception as e:
			raise e

	@property
	def vendorid(self) :
		ur"""Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			return self._vendorid
		except Exception as e:
			raise e

	@vendorid.setter
	def vendorid(self, vendorid) :
		ur"""Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			self._vendorid = vendorid
		except Exception as e:
			raise e

	@property
	def productname(self) :
		ur"""Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1.
		"""
		try :
			return self._productname
		except Exception as e:
			raise e

	@productname.setter
	def productname(self, productname) :
		ur"""Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1
		"""
		try :
			self._productname = productname
		except Exception as e:
			raise e

	@property
	def firmwarerevision(self) :
		ur"""Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			return self._firmwarerevision
		except Exception as e:
			raise e

	@firmwarerevision.setter
	def firmwarerevision(self, firmwarerevision) :
		ur"""Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			self._firmwarerevision = firmwarerevision
		except Exception as e:
			raise e

	@property
	def authapplicationid(self) :
		ur"""List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._authapplicationid
		except Exception as e:
			raise e

	@authapplicationid.setter
	def authapplicationid(self, authapplicationid) :
		ur"""List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._authapplicationid = authapplicationid
		except Exception as e:
			raise e

	@property
	def acctapplicationid(self) :
		ur"""List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._acctapplicationid
		except Exception as e:
			raise e

	@acctapplicationid.setter
	def acctapplicationid(self, acctapplicationid) :
		ur"""List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._acctapplicationid = acctapplicationid
		except Exception as e:
			raise e

	@property
	def inbandsecurityid(self) :
		ur"""Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Possible values = NO_INBAND_SECURITY, TLS.
		"""
		try :
			return self._inbandsecurityid
		except Exception as e:
			raise e

	@inbandsecurityid.setter
	def inbandsecurityid(self, inbandsecurityid) :
		ur"""Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Possible values = NO_INBAND_SECURITY, TLS
		"""
		try :
			self._inbandsecurityid = inbandsecurityid
		except Exception as e:
			raise e

	@property
	def supportedvendorids(self) :
		ur"""List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._supportedvendorids
		except Exception as e:
			raise e

	@supportedvendorids.setter
	def supportedvendorids(self, supportedvendorids) :
		ur"""List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._supportedvendorids = supportedvendorids
		except Exception as e:
			raise e

	@property
	def vendorspecificvendorid(self) :
		ur"""Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.<br/>Minimum length =  1.
		"""
		try :
			return self._vendorspecificvendorid
		except Exception as e:
			raise e

	@vendorspecificvendorid.setter
	def vendorspecificvendorid(self, vendorspecificvendorid) :
		ur"""Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.<br/>Minimum length =  1
		"""
		try :
			self._vendorspecificvendorid = vendorspecificvendorid
		except Exception as e:
			raise e

	@property
	def vendorspecificauthapplicationids(self) :
		ur"""List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._vendorspecificauthapplicationids
		except Exception as e:
			raise e

	@vendorspecificauthapplicationids.setter
	def vendorspecificauthapplicationids(self, vendorspecificauthapplicationids) :
		ur"""List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._vendorspecificauthapplicationids = vendorspecificauthapplicationids
		except Exception as e:
			raise e

	@property
	def vendorspecificacctapplicationids(self) :
		ur"""List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._vendorspecificacctapplicationids
		except Exception as e:
			raise e

	@vendorspecificacctapplicationids.setter
	def vendorspecificacctapplicationids(self, vendorspecificacctapplicationids) :
		ur"""List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._vendorspecificacctapplicationids = vendorspecificacctapplicationids
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		ur"""KCD Account used by MSSQL monitor.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		ur"""KCD Account used by MSSQL monitor.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def storedb(self) :
		ur"""Store the database list populated with the responses to monitor probes. Used in database specific load balancing if MSSQL-ECV/MYSQL-ECV  monitor is configured.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._storedb
		except Exception as e:
			raise e

	@storedb.setter
	def storedb(self, storedb) :
		ur"""Store the database list populated with the responses to monitor probes. Used in database specific load balancing if MSSQL-ECV/MYSQL-ECV  monitor is configured.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._storedb = storedb
		except Exception as e:
			raise e

	@property
	def storefrontcheckbackendservices(self) :
		ur"""This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._storefrontcheckbackendservices
		except Exception as e:
			raise e

	@storefrontcheckbackendservices.setter
	def storefrontcheckbackendservices(self, storefrontcheckbackendservices) :
		ur"""This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._storefrontcheckbackendservices = storefrontcheckbackendservices
		except Exception as e:
			raise e

	@property
	def metric(self) :
		ur"""Metric name in the metric table, whose setting is changed. A value zero disables the metric and it will not be used for load calculation.<br/>Minimum length =  1<br/>Maximum length =  37.
		"""
		try :
			return self._metric
		except Exception as e:
			raise e

	@metric.setter
	def metric(self, metric) :
		ur"""Metric name in the metric table, whose setting is changed. A value zero disables the metric and it will not be used for load calculation.<br/>Minimum length =  1<br/>Maximum length =  37
		"""
		try :
			self._metric = metric
		except Exception as e:
			raise e

	@property
	def metricthreshold(self) :
		ur"""Threshold to be used for that metric.
		"""
		try :
			return self._metricthreshold
		except Exception as e:
			raise e

	@metricthreshold.setter
	def metricthreshold(self, metricthreshold) :
		ur"""Threshold to be used for that metric.
		"""
		try :
			self._metricthreshold = metricthreshold
		except Exception as e:
			raise e

	@property
	def metricweight(self) :
		ur"""The weight for the specified service metric with respect to others.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._metricweight
		except Exception as e:
			raise e

	@metricweight.setter
	def metricweight(self, metricweight) :
		ur"""The weight for the specified service metric with respect to others.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._metricweight = metricweight
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""The name of the service to which the monitor is bound.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""The name of the service to which the monitor is bound.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def servicegroupname(self) :
		ur"""The name of the service group to which the monitor is to be bound.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		ur"""The name of the service group to which the monitor is to be bound.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def lrtmconf(self) :
		ur"""State of LRTM configuration on the monitor.
		"""
		try :
			return self._lrtmconf
		except Exception as e:
			raise e

	@property
	def lrtmconfstr(self) :
		ur"""State of LRTM configuration on the monitor as STRING.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._lrtmconfstr
		except Exception as e:
			raise e

	@property
	def dynamicresponsetimeout(self) :
		ur"""Response timeout of the DRTM enabled monitor , calculated dynamically based on the history and current response time.
		"""
		try :
			return self._dynamicresponsetimeout
		except Exception as e:
			raise e

	@property
	def dynamicinterval(self) :
		ur"""Interval between monitoring probes for DRTM enabled monitor , calculated dynamically based monitor response time.
		"""
		try :
			return self._dynamicinterval
		except Exception as e:
			raise e

	@property
	def multimetrictable(self) :
		ur"""Metric table to which to bind metrics, to be used only for output purposes.
		"""
		try :
			return self._multimetrictable
		except Exception as e:
			raise e

	@property
	def dup_state(self) :
		ur""".<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dup_state
		except Exception as e:
			raise e

	@property
	def dup_weight(self) :
		ur""".<br/>Default value: 1<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._dup_weight
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur""".<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmonitor_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmonitor
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
	def add(cls, client, resource) :
		ur""" Use this API to add lbmonitor.
		"""
		try :
			if type(resource) is not list :
				addresource = lbmonitor()
				addresource.monitorname = resource.monitorname
				addresource.type = resource.type
				addresource.action = resource.action
				addresource.respcode = resource.respcode
				addresource.httprequest = resource.httprequest
				addresource.rtsprequest = resource.rtsprequest
				addresource.customheaders = resource.customheaders
				addresource.maxforwards = resource.maxforwards
				addresource.sipmethod = resource.sipmethod
				addresource.sipuri = resource.sipuri
				addresource.sipreguri = resource.sipreguri
				addresource.send = resource.send
				addresource.recv = resource.recv
				addresource.query = resource.query
				addresource.querytype = resource.querytype
				addresource.scriptname = resource.scriptname
				addresource.scriptargs = resource.scriptargs
				addresource.dispatcherip = resource.dispatcherip
				addresource.dispatcherport = resource.dispatcherport
				addresource.username = resource.username
				addresource.password = resource.password
				addresource.secondarypassword = resource.secondarypassword
				addresource.logonpointname = resource.logonpointname
				addresource.lasversion = resource.lasversion
				addresource.radkey = resource.radkey
				addresource.radnasid = resource.radnasid
				addresource.radnasip = resource.radnasip
				addresource.radaccounttype = resource.radaccounttype
				addresource.radframedip = resource.radframedip
				addresource.radapn = resource.radapn
				addresource.radmsisdn = resource.radmsisdn
				addresource.radaccountsession = resource.radaccountsession
				addresource.lrtm = resource.lrtm
				addresource.deviation = resource.deviation
				addresource.units1 = resource.units1
				addresource.interval = resource.interval
				addresource.units3 = resource.units3
				addresource.resptimeout = resource.resptimeout
				addresource.units4 = resource.units4
				addresource.resptimeoutthresh = resource.resptimeoutthresh
				addresource.retries = resource.retries
				addresource.failureretries = resource.failureretries
				addresource.alertretries = resource.alertretries
				addresource.successretries = resource.successretries
				addresource.downtime = resource.downtime
				addresource.units2 = resource.units2
				addresource.destip = resource.destip
				addresource.destport = resource.destport
				addresource.state = resource.state
				addresource.reverse = resource.reverse
				addresource.transparent = resource.transparent
				addresource.iptunnel = resource.iptunnel
				addresource.tos = resource.tos
				addresource.tosid = resource.tosid
				addresource.secure = resource.secure
				addresource.validatecred = resource.validatecred
				addresource.domain = resource.domain
				addresource.ipaddress = resource.ipaddress
				addresource.group = resource.group
				addresource.filename = resource.filename
				addresource.basedn = resource.basedn
				addresource.binddn = resource.binddn
				addresource.filter = resource.filter
				addresource.attribute = resource.attribute
				addresource.database = resource.database
				addresource.oraclesid = resource.oraclesid
				addresource.sqlquery = resource.sqlquery
				addresource.evalrule = resource.evalrule
				addresource.mssqlprotocolversion = resource.mssqlprotocolversion
				addresource.Snmpoid = resource.Snmpoid
				addresource.snmpcommunity = resource.snmpcommunity
				addresource.snmpthreshold = resource.snmpthreshold
				addresource.snmpversion = resource.snmpversion
				addresource.metrictable = resource.metrictable
				addresource.application = resource.application
				addresource.sitepath = resource.sitepath
				addresource.storename = resource.storename
				addresource.storefrontacctservice = resource.storefrontacctservice
				addresource.hostname = resource.hostname
				addresource.netprofile = resource.netprofile
				addresource.originhost = resource.originhost
				addresource.originrealm = resource.originrealm
				addresource.hostipaddress = resource.hostipaddress
				addresource.vendorid = resource.vendorid
				addresource.productname = resource.productname
				addresource.firmwarerevision = resource.firmwarerevision
				addresource.authapplicationid = resource.authapplicationid
				addresource.acctapplicationid = resource.acctapplicationid
				addresource.inbandsecurityid = resource.inbandsecurityid
				addresource.supportedvendorids = resource.supportedvendorids
				addresource.vendorspecificvendorid = resource.vendorspecificvendorid
				addresource.vendorspecificauthapplicationids = resource.vendorspecificauthapplicationids
				addresource.vendorspecificacctapplicationids = resource.vendorspecificacctapplicationids
				addresource.kcdaccount = resource.kcdaccount
				addresource.storedb = resource.storedb
				addresource.storefrontcheckbackendservices = resource.storefrontcheckbackendservices
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbmonitor() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].monitorname = resource[i].monitorname
						addresources[i].type = resource[i].type
						addresources[i].action = resource[i].action
						addresources[i].respcode = resource[i].respcode
						addresources[i].httprequest = resource[i].httprequest
						addresources[i].rtsprequest = resource[i].rtsprequest
						addresources[i].customheaders = resource[i].customheaders
						addresources[i].maxforwards = resource[i].maxforwards
						addresources[i].sipmethod = resource[i].sipmethod
						addresources[i].sipuri = resource[i].sipuri
						addresources[i].sipreguri = resource[i].sipreguri
						addresources[i].send = resource[i].send
						addresources[i].recv = resource[i].recv
						addresources[i].query = resource[i].query
						addresources[i].querytype = resource[i].querytype
						addresources[i].scriptname = resource[i].scriptname
						addresources[i].scriptargs = resource[i].scriptargs
						addresources[i].dispatcherip = resource[i].dispatcherip
						addresources[i].dispatcherport = resource[i].dispatcherport
						addresources[i].username = resource[i].username
						addresources[i].password = resource[i].password
						addresources[i].secondarypassword = resource[i].secondarypassword
						addresources[i].logonpointname = resource[i].logonpointname
						addresources[i].lasversion = resource[i].lasversion
						addresources[i].radkey = resource[i].radkey
						addresources[i].radnasid = resource[i].radnasid
						addresources[i].radnasip = resource[i].radnasip
						addresources[i].radaccounttype = resource[i].radaccounttype
						addresources[i].radframedip = resource[i].radframedip
						addresources[i].radapn = resource[i].radapn
						addresources[i].radmsisdn = resource[i].radmsisdn
						addresources[i].radaccountsession = resource[i].radaccountsession
						addresources[i].lrtm = resource[i].lrtm
						addresources[i].deviation = resource[i].deviation
						addresources[i].units1 = resource[i].units1
						addresources[i].interval = resource[i].interval
						addresources[i].units3 = resource[i].units3
						addresources[i].resptimeout = resource[i].resptimeout
						addresources[i].units4 = resource[i].units4
						addresources[i].resptimeoutthresh = resource[i].resptimeoutthresh
						addresources[i].retries = resource[i].retries
						addresources[i].failureretries = resource[i].failureretries
						addresources[i].alertretries = resource[i].alertretries
						addresources[i].successretries = resource[i].successretries
						addresources[i].downtime = resource[i].downtime
						addresources[i].units2 = resource[i].units2
						addresources[i].destip = resource[i].destip
						addresources[i].destport = resource[i].destport
						addresources[i].state = resource[i].state
						addresources[i].reverse = resource[i].reverse
						addresources[i].transparent = resource[i].transparent
						addresources[i].iptunnel = resource[i].iptunnel
						addresources[i].tos = resource[i].tos
						addresources[i].tosid = resource[i].tosid
						addresources[i].secure = resource[i].secure
						addresources[i].validatecred = resource[i].validatecred
						addresources[i].domain = resource[i].domain
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].group = resource[i].group
						addresources[i].filename = resource[i].filename
						addresources[i].basedn = resource[i].basedn
						addresources[i].binddn = resource[i].binddn
						addresources[i].filter = resource[i].filter
						addresources[i].attribute = resource[i].attribute
						addresources[i].database = resource[i].database
						addresources[i].oraclesid = resource[i].oraclesid
						addresources[i].sqlquery = resource[i].sqlquery
						addresources[i].evalrule = resource[i].evalrule
						addresources[i].mssqlprotocolversion = resource[i].mssqlprotocolversion
						addresources[i].Snmpoid = resource[i].Snmpoid
						addresources[i].snmpcommunity = resource[i].snmpcommunity
						addresources[i].snmpthreshold = resource[i].snmpthreshold
						addresources[i].snmpversion = resource[i].snmpversion
						addresources[i].metrictable = resource[i].metrictable
						addresources[i].application = resource[i].application
						addresources[i].sitepath = resource[i].sitepath
						addresources[i].storename = resource[i].storename
						addresources[i].storefrontacctservice = resource[i].storefrontacctservice
						addresources[i].hostname = resource[i].hostname
						addresources[i].netprofile = resource[i].netprofile
						addresources[i].originhost = resource[i].originhost
						addresources[i].originrealm = resource[i].originrealm
						addresources[i].hostipaddress = resource[i].hostipaddress
						addresources[i].vendorid = resource[i].vendorid
						addresources[i].productname = resource[i].productname
						addresources[i].firmwarerevision = resource[i].firmwarerevision
						addresources[i].authapplicationid = resource[i].authapplicationid
						addresources[i].acctapplicationid = resource[i].acctapplicationid
						addresources[i].inbandsecurityid = resource[i].inbandsecurityid
						addresources[i].supportedvendorids = resource[i].supportedvendorids
						addresources[i].vendorspecificvendorid = resource[i].vendorspecificvendorid
						addresources[i].vendorspecificauthapplicationids = resource[i].vendorspecificauthapplicationids
						addresources[i].vendorspecificacctapplicationids = resource[i].vendorspecificacctapplicationids
						addresources[i].kcdaccount = resource[i].kcdaccount
						addresources[i].storedb = resource[i].storedb
						addresources[i].storefrontcheckbackendservices = resource[i].storefrontcheckbackendservices
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lbmonitor.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbmonitor()
				if type(resource) !=  type(deleteresource):
					deleteresource.monitorname = resource
				else :
					deleteresource.monitorname = resource.monitorname
					deleteresource.type = resource.type
					deleteresource.respcode = resource.respcode
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].monitorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].monitorname = resource[i].monitorname
							deleteresources[i].type = resource[i].type
							deleteresources[i].respcode = resource[i].respcode
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lbmonitor.
		"""
		try :
			if type(resource) is not list :
				updateresource = lbmonitor()
				updateresource.monitorname = resource.monitorname
				updateresource.type = resource.type
				updateresource.action = resource.action
				updateresource.respcode = resource.respcode
				updateresource.httprequest = resource.httprequest
				updateresource.rtsprequest = resource.rtsprequest
				updateresource.customheaders = resource.customheaders
				updateresource.maxforwards = resource.maxforwards
				updateresource.sipmethod = resource.sipmethod
				updateresource.sipreguri = resource.sipreguri
				updateresource.sipuri = resource.sipuri
				updateresource.send = resource.send
				updateresource.recv = resource.recv
				updateresource.query = resource.query
				updateresource.querytype = resource.querytype
				updateresource.username = resource.username
				updateresource.password = resource.password
				updateresource.secondarypassword = resource.secondarypassword
				updateresource.logonpointname = resource.logonpointname
				updateresource.lasversion = resource.lasversion
				updateresource.radkey = resource.radkey
				updateresource.radnasid = resource.radnasid
				updateresource.radnasip = resource.radnasip
				updateresource.radaccounttype = resource.radaccounttype
				updateresource.radframedip = resource.radframedip
				updateresource.radapn = resource.radapn
				updateresource.radmsisdn = resource.radmsisdn
				updateresource.radaccountsession = resource.radaccountsession
				updateresource.lrtm = resource.lrtm
				updateresource.deviation = resource.deviation
				updateresource.units1 = resource.units1
				updateresource.scriptname = resource.scriptname
				updateresource.scriptargs = resource.scriptargs
				updateresource.validatecred = resource.validatecred
				updateresource.domain = resource.domain
				updateresource.dispatcherip = resource.dispatcherip
				updateresource.dispatcherport = resource.dispatcherport
				updateresource.interval = resource.interval
				updateresource.units3 = resource.units3
				updateresource.resptimeout = resource.resptimeout
				updateresource.units4 = resource.units4
				updateresource.resptimeoutthresh = resource.resptimeoutthresh
				updateresource.retries = resource.retries
				updateresource.failureretries = resource.failureretries
				updateresource.alertretries = resource.alertretries
				updateresource.successretries = resource.successretries
				updateresource.downtime = resource.downtime
				updateresource.units2 = resource.units2
				updateresource.destip = resource.destip
				updateresource.destport = resource.destport
				updateresource.state = resource.state
				updateresource.reverse = resource.reverse
				updateresource.transparent = resource.transparent
				updateresource.iptunnel = resource.iptunnel
				updateresource.tos = resource.tos
				updateresource.tosid = resource.tosid
				updateresource.secure = resource.secure
				updateresource.ipaddress = resource.ipaddress
				updateresource.group = resource.group
				updateresource.filename = resource.filename
				updateresource.basedn = resource.basedn
				updateresource.binddn = resource.binddn
				updateresource.filter = resource.filter
				updateresource.attribute = resource.attribute
				updateresource.database = resource.database
				updateresource.oraclesid = resource.oraclesid
				updateresource.sqlquery = resource.sqlquery
				updateresource.evalrule = resource.evalrule
				updateresource.Snmpoid = resource.Snmpoid
				updateresource.snmpcommunity = resource.snmpcommunity
				updateresource.snmpthreshold = resource.snmpthreshold
				updateresource.snmpversion = resource.snmpversion
				updateresource.metrictable = resource.metrictable
				updateresource.metric = resource.metric
				updateresource.metricthreshold = resource.metricthreshold
				updateresource.metricweight = resource.metricweight
				updateresource.application = resource.application
				updateresource.sitepath = resource.sitepath
				updateresource.storename = resource.storename
				updateresource.storefrontacctservice = resource.storefrontacctservice
				updateresource.storefrontcheckbackendservices = resource.storefrontcheckbackendservices
				updateresource.hostname = resource.hostname
				updateresource.netprofile = resource.netprofile
				updateresource.mssqlprotocolversion = resource.mssqlprotocolversion
				updateresource.originhost = resource.originhost
				updateresource.originrealm = resource.originrealm
				updateresource.hostipaddress = resource.hostipaddress
				updateresource.vendorid = resource.vendorid
				updateresource.productname = resource.productname
				updateresource.firmwarerevision = resource.firmwarerevision
				updateresource.authapplicationid = resource.authapplicationid
				updateresource.acctapplicationid = resource.acctapplicationid
				updateresource.inbandsecurityid = resource.inbandsecurityid
				updateresource.supportedvendorids = resource.supportedvendorids
				updateresource.vendorspecificvendorid = resource.vendorspecificvendorid
				updateresource.vendorspecificauthapplicationids = resource.vendorspecificauthapplicationids
				updateresource.vendorspecificacctapplicationids = resource.vendorspecificacctapplicationids
				updateresource.kcdaccount = resource.kcdaccount
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lbmonitor() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].monitorname = resource[i].monitorname
						updateresources[i].type = resource[i].type
						updateresources[i].action = resource[i].action
						updateresources[i].respcode = resource[i].respcode
						updateresources[i].httprequest = resource[i].httprequest
						updateresources[i].rtsprequest = resource[i].rtsprequest
						updateresources[i].customheaders = resource[i].customheaders
						updateresources[i].maxforwards = resource[i].maxforwards
						updateresources[i].sipmethod = resource[i].sipmethod
						updateresources[i].sipreguri = resource[i].sipreguri
						updateresources[i].sipuri = resource[i].sipuri
						updateresources[i].send = resource[i].send
						updateresources[i].recv = resource[i].recv
						updateresources[i].query = resource[i].query
						updateresources[i].querytype = resource[i].querytype
						updateresources[i].username = resource[i].username
						updateresources[i].password = resource[i].password
						updateresources[i].secondarypassword = resource[i].secondarypassword
						updateresources[i].logonpointname = resource[i].logonpointname
						updateresources[i].lasversion = resource[i].lasversion
						updateresources[i].radkey = resource[i].radkey
						updateresources[i].radnasid = resource[i].radnasid
						updateresources[i].radnasip = resource[i].radnasip
						updateresources[i].radaccounttype = resource[i].radaccounttype
						updateresources[i].radframedip = resource[i].radframedip
						updateresources[i].radapn = resource[i].radapn
						updateresources[i].radmsisdn = resource[i].radmsisdn
						updateresources[i].radaccountsession = resource[i].radaccountsession
						updateresources[i].lrtm = resource[i].lrtm
						updateresources[i].deviation = resource[i].deviation
						updateresources[i].units1 = resource[i].units1
						updateresources[i].scriptname = resource[i].scriptname
						updateresources[i].scriptargs = resource[i].scriptargs
						updateresources[i].validatecred = resource[i].validatecred
						updateresources[i].domain = resource[i].domain
						updateresources[i].dispatcherip = resource[i].dispatcherip
						updateresources[i].dispatcherport = resource[i].dispatcherport
						updateresources[i].interval = resource[i].interval
						updateresources[i].units3 = resource[i].units3
						updateresources[i].resptimeout = resource[i].resptimeout
						updateresources[i].units4 = resource[i].units4
						updateresources[i].resptimeoutthresh = resource[i].resptimeoutthresh
						updateresources[i].retries = resource[i].retries
						updateresources[i].failureretries = resource[i].failureretries
						updateresources[i].alertretries = resource[i].alertretries
						updateresources[i].successretries = resource[i].successretries
						updateresources[i].downtime = resource[i].downtime
						updateresources[i].units2 = resource[i].units2
						updateresources[i].destip = resource[i].destip
						updateresources[i].destport = resource[i].destport
						updateresources[i].state = resource[i].state
						updateresources[i].reverse = resource[i].reverse
						updateresources[i].transparent = resource[i].transparent
						updateresources[i].iptunnel = resource[i].iptunnel
						updateresources[i].tos = resource[i].tos
						updateresources[i].tosid = resource[i].tosid
						updateresources[i].secure = resource[i].secure
						updateresources[i].ipaddress = resource[i].ipaddress
						updateresources[i].group = resource[i].group
						updateresources[i].filename = resource[i].filename
						updateresources[i].basedn = resource[i].basedn
						updateresources[i].binddn = resource[i].binddn
						updateresources[i].filter = resource[i].filter
						updateresources[i].attribute = resource[i].attribute
						updateresources[i].database = resource[i].database
						updateresources[i].oraclesid = resource[i].oraclesid
						updateresources[i].sqlquery = resource[i].sqlquery
						updateresources[i].evalrule = resource[i].evalrule
						updateresources[i].Snmpoid = resource[i].Snmpoid
						updateresources[i].snmpcommunity = resource[i].snmpcommunity
						updateresources[i].snmpthreshold = resource[i].snmpthreshold
						updateresources[i].snmpversion = resource[i].snmpversion
						updateresources[i].metrictable = resource[i].metrictable
						updateresources[i].metric = resource[i].metric
						updateresources[i].metricthreshold = resource[i].metricthreshold
						updateresources[i].metricweight = resource[i].metricweight
						updateresources[i].application = resource[i].application
						updateresources[i].sitepath = resource[i].sitepath
						updateresources[i].storename = resource[i].storename
						updateresources[i].storefrontacctservice = resource[i].storefrontacctservice
						updateresources[i].storefrontcheckbackendservices = resource[i].storefrontcheckbackendservices
						updateresources[i].hostname = resource[i].hostname
						updateresources[i].netprofile = resource[i].netprofile
						updateresources[i].mssqlprotocolversion = resource[i].mssqlprotocolversion
						updateresources[i].originhost = resource[i].originhost
						updateresources[i].originrealm = resource[i].originrealm
						updateresources[i].hostipaddress = resource[i].hostipaddress
						updateresources[i].vendorid = resource[i].vendorid
						updateresources[i].productname = resource[i].productname
						updateresources[i].firmwarerevision = resource[i].firmwarerevision
						updateresources[i].authapplicationid = resource[i].authapplicationid
						updateresources[i].acctapplicationid = resource[i].acctapplicationid
						updateresources[i].inbandsecurityid = resource[i].inbandsecurityid
						updateresources[i].supportedvendorids = resource[i].supportedvendorids
						updateresources[i].vendorspecificvendorid = resource[i].vendorspecificvendorid
						updateresources[i].vendorspecificauthapplicationids = resource[i].vendorspecificauthapplicationids
						updateresources[i].vendorspecificacctapplicationids = resource[i].vendorspecificacctapplicationids
						updateresources[i].kcdaccount = resource[i].kcdaccount
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lbmonitor resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbmonitor()
				unsetresource.monitorname = resource.monitorname
				unsetresource.type = resource.type
				unsetresource.ipaddress = resource.ipaddress
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) == cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].monitorname = resource[i].monitorname
							unsetresources[i].type = resource[i].type
							unsetresources[i].ipaddress = resource[i].ipaddress
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable lbmonitor.
		"""
		try :
			if type(resource) is not list :
				enableresource = lbmonitor()
				if type(resource) !=  type(enableresource):
					enableresource.monitorname = resource
				else :
					enableresource.servicename = resource.servicename
					enableresource.servicegroupname = resource.servicegroupname
					enableresource.monitorname = resource.monitorname
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].monitorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].servicename = resource[i].servicename
							enableresources[i].servicegroupname = resource[i].servicegroupname
							enableresources[i].monitorname = resource[i].monitorname
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable lbmonitor.
		"""
		try :
			if type(resource) is not list :
				disableresource = lbmonitor()
				if type(resource) !=  type(disableresource):
					disableresource.monitorname = resource
				else :
					disableresource.servicename = resource.servicename
					disableresource.servicegroupname = resource.servicegroupname
					disableresource.monitorname = resource.monitorname
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].monitorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].servicename = resource[i].servicename
							disableresources[i].servicegroupname = resource[i].servicegroupname
							disableresources[i].monitorname = resource[i].monitorname
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lbmonitor resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbmonitor()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lbmonitor()
						obj.monitorname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lbmonitor() for _ in range(len(name))]
							obj = [lbmonitor() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lbmonitor()
								obj[i].monitorname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the lbmonitor resources that are configured on netscaler.
	# This uses lbmonitor_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = lbmonitor()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lbmonitor resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonitor()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lbmonitor resources configured on NetScaler.
		"""
		try :
			obj = lbmonitor()
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
		ur""" Use this API to count filtered the set of lbmonitor resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonitor()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Secure:
		YES = "YES"
		NO = "NO"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Validatecred:
		YES = "YES"
		NO = "NO"

	class Inbandsecurityid:
		NO_INBAND_SECURITY = "NO_INBAND_SECURITY"
		TLS = "TLS"

	class Reverse:
		YES = "YES"
		NO = "NO"

	class Sipmethod:
		OPTIONS = "OPTIONS"
		INVITE = "INVITE"
		REGISTER = "REGISTER"

	class Type:
		PING = "PING"
		TCP = "TCP"
		HTTP = "HTTP"
		TCP_ECV = "TCP-ECV"
		HTTP_ECV = "HTTP-ECV"
		UDP_ECV = "UDP-ECV"
		DNS = "DNS"
		FTP = "FTP"
		LDNS_PING = "LDNS-PING"
		LDNS_TCP = "LDNS-TCP"
		LDNS_DNS = "LDNS-DNS"
		RADIUS = "RADIUS"
		USER = "USER"
		HTTP_INLINE = "HTTP-INLINE"
		SIP_UDP = "SIP-UDP"
		LOAD = "LOAD"
		FTP_EXTENDED = "FTP-EXTENDED"
		SMTP = "SMTP"
		SNMP = "SNMP"
		NNTP = "NNTP"
		MYSQL = "MYSQL"
		MYSQL_ECV = "MYSQL-ECV"
		MSSQL_ECV = "MSSQL-ECV"
		ORACLE_ECV = "ORACLE-ECV"
		LDAP = "LDAP"
		POP3 = "POP3"
		CITRIX_XML_SERVICE = "CITRIX-XML-SERVICE"
		CITRIX_WEB_INTERFACE = "CITRIX-WEB-INTERFACE"
		DNS_TCP = "DNS-TCP"
		RTSP = "RTSP"
		ARP = "ARP"
		CITRIX_AG = "CITRIX-AG"
		CITRIX_AAC_LOGINPAGE = "CITRIX-AAC-LOGINPAGE"
		CITRIX_AAC_LAS = "CITRIX-AAC-LAS"
		CITRIX_XD_DDC = "CITRIX-XD-DDC"
		ND6 = "ND6"
		CITRIX_WI_EXTENDED = "CITRIX-WI-EXTENDED"
		DIAMETER = "DIAMETER"
		RADIUS_ACCOUNTING = "RADIUS_ACCOUNTING"
		STOREFRONT = "STOREFRONT"
		APPC = "APPC"
		CITRIX_XNC_ECV = "CITRIX-XNC-ECV"
		CITRIX_XDM = "CITRIX-XDM"

	class Lrtm:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Iptunnel:
		YES = "YES"
		NO = "NO"

	class Tos:
		YES = "YES"
		NO = "NO"

	class Units3:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Storedb:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Transparent:
		YES = "YES"
		NO = "NO"

	class Lrtmconfstr:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Units1:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Dup_state:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Storefrontacctservice:
		YES = "YES"
		NO = "NO"

	class Storefrontcheckbackendservices:
		YES = "YES"
		NO = "NO"

	class Units2:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Units4:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Action:
		NONE = "NONE"
		LOG = "LOG"
		DOWN = "DOWN"

	class Mssqlprotocolversion:
		_70 = "70"
		_2000 = "2000"
		_2000SP1 = "2000SP1"
		_2005 = "2005"
		_2008 = "2008"
		_2008R2 = "2008R2"
		_2012 = "2012"

	class Snmpversion:
		V1 = "V1"
		V2 = "V2"

	class Querytype:
		Address = "Address"
		Zone = "Zone"
		AAAA = "AAAA"

class lbmonitor_response(base_response) :
	def __init__(self, length=1) :
		self.lbmonitor = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmonitor = [lbmonitor() for _ in range(length)]

