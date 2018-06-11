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

class crvserver(base_resource) :
	""" Configuration for CR virtual server resource. """
	def __init__(self) :
		self._name = ""
		self._td = 0
		self._servicetype = ""
		self._ipv46 = ""
		self._port = 0
		self._range = 0
		self._cachetype = ""
		self._redirect = ""
		self._onpolicymatch = ""
		self._redirecturl = ""
		self._clttimeout = 0
		self._precedence = ""
		self._arp = ""
		self._ghost = ""
		self._map = ""
		self._format = ""
		self._via = ""
		self._cachevserver = ""
		self._dnsvservername = ""
		self._destinationvserver = ""
		self._domain = ""
		self._sopersistencetimeout = 0
		self._sothreshold = 0
		self._reuse = ""
		self._state = ""
		self._downstateflush = ""
		self._backupvserver = ""
		self._disableprimaryondown = ""
		self._l2conn = ""
		self._backendssl = ""
		self._listenpolicy = ""
		self._listenpriority = 0
		self._tcpprofilename = ""
		self._httpprofilename = ""
		self._comment = ""
		self._srcipexpr = ""
		self._originusip = ""
		self._useportrange = ""
		self._appflowlog = ""
		self._netprofile = ""
		self._icmpvsrresponse = ""
		self._rhistate = ""
		self._newname = ""
		self._ip = ""
		self._value = ""
		self._ngname = ""
		self._type = ""
		self._curstate = ""
		self._status = 0
		self._authentication = ""
		self._homepage = ""
		self._rule = ""
		self._policyname = ""
		self._servicename = ""
		self._weight = 0
		self._targetvserver = ""
		self._priority = 0
		self._somethod = ""
		self._sopersistence = ""
		self._lbvserver = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the cache redirection virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the cache redirection virtual server is created.
		The following requirement applies only to the NetScaler CLI:  
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my server" or 'my server').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the cache redirection virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the cache redirection virtual server is created.
		The following requirement applies only to the NetScaler CLI:  
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my server" or 'my server').<br/>Minimum length =  1
		"""
		try :
			self._name = name
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
	def servicetype(self) :
		ur"""Protocol (type of service) handled by the virtual server.<br/>Possible values = HTTP, SSL, NNTP, HDX.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		ur"""Protocol (type of service) handled by the virtual server.<br/>Possible values = HTTP, SSL, NNTP, HDX
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def ipv46(self) :
		ur"""IPv4 or IPv6 address of the cache redirection virtual server. Usually a public IP address. Clients send connection requests to this IP address.
		Note: For a transparent cache redirection virtual server, use an asterisk (*) to specify a wildcard virtual server address.
		"""
		try :
			return self._ipv46
		except Exception as e:
			raise e

	@ipv46.setter
	def ipv46(self, ipv46) :
		ur"""IPv4 or IPv6 address of the cache redirection virtual server. Usually a public IP address. Clients send connection requests to this IP address.
		Note: For a transparent cache redirection virtual server, use an asterisk (*) to specify a wildcard virtual server address.
		"""
		try :
			self._ipv46 = ipv46
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port number of the virtual server.<br/>Default value: 80<br/>Minimum length =  1<br/>Maximum length =  65534.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""Port number of the virtual server.<br/>Default value: 80<br/>Minimum length =  1<br/>Maximum length =  65534
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def range(self) :
		ur"""Number of consecutive IP addresses, starting with the address specified by the IPAddress parameter, to include in a range of addresses assigned to this virtual server.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254.
		"""
		try :
			return self._range
		except Exception as e:
			raise e

	@range.setter
	def range(self, range) :
		ur"""Number of consecutive IP addresses, starting with the address specified by the IPAddress parameter, to include in a range of addresses assigned to this virtual server.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  254
		"""
		try :
			self._range = range
		except Exception as e:
			raise e

	@property
	def cachetype(self) :
		ur"""Mode of operation for the cache redirection virtual server. Available settings function as follows:
		* TRANSPARENT - Intercept all traffic flowing to the appliance and apply cache redirection policies to determine whether content should be served from the cache or from the origin server.
		* FORWARD - Resolve the hostname of the incoming request, by using a DNS server, and forward requests for non-cacheable content to the resolved origin servers. Cacheable requests are sent to the configured cache servers.
		* REVERSE - Configure reverse proxy caches for specific origin servers. Incoming traffic directed to the reverse proxy can either be served from a cache server or be sent to the origin server with or without modification to the URL.<br/>Default value: TRANSPARENT<br/>Possible values = TRANSPARENT, REVERSE, FORWARD.
		"""
		try :
			return self._cachetype
		except Exception as e:
			raise e

	@cachetype.setter
	def cachetype(self, cachetype) :
		ur"""Mode of operation for the cache redirection virtual server. Available settings function as follows:
		* TRANSPARENT - Intercept all traffic flowing to the appliance and apply cache redirection policies to determine whether content should be served from the cache or from the origin server.
		* FORWARD - Resolve the hostname of the incoming request, by using a DNS server, and forward requests for non-cacheable content to the resolved origin servers. Cacheable requests are sent to the configured cache servers.
		* REVERSE - Configure reverse proxy caches for specific origin servers. Incoming traffic directed to the reverse proxy can either be served from a cache server or be sent to the origin server with or without modification to the URL.<br/>Default value: TRANSPARENT<br/>Possible values = TRANSPARENT, REVERSE, FORWARD
		"""
		try :
			self._cachetype = cachetype
		except Exception as e:
			raise e

	@property
	def redirect(self) :
		ur"""Type of cache server to which to redirect HTTP requests. Available settings function as follows:
		* CACHE - Direct all requests to the cache.
		* POLICY - Apply the cache redirection policy to determine whether the request should be directed to the cache or to the origin.
		* ORIGIN - Direct all requests to the origin server.<br/>Default value: POLICY<br/>Possible values = CACHE, POLICY, ORIGIN.
		"""
		try :
			return self._redirect
		except Exception as e:
			raise e

	@redirect.setter
	def redirect(self, redirect) :
		ur"""Type of cache server to which to redirect HTTP requests. Available settings function as follows:
		* CACHE - Direct all requests to the cache.
		* POLICY - Apply the cache redirection policy to determine whether the request should be directed to the cache or to the origin.
		* ORIGIN - Direct all requests to the origin server.<br/>Default value: POLICY<br/>Possible values = CACHE, POLICY, ORIGIN
		"""
		try :
			self._redirect = redirect
		except Exception as e:
			raise e

	@property
	def onpolicymatch(self) :
		ur"""Redirect requests that match the policy to either the cache or the origin server, as specified.
		Note: For this option to work, you must set the cache redirection type to POLICY.<br/>Default value: ORIGIN<br/>Possible values = CACHE, ORIGIN.
		"""
		try :
			return self._onpolicymatch
		except Exception as e:
			raise e

	@onpolicymatch.setter
	def onpolicymatch(self, onpolicymatch) :
		ur"""Redirect requests that match the policy to either the cache or the origin server, as specified.
		Note: For this option to work, you must set the cache redirection type to POLICY.<br/>Default value: ORIGIN<br/>Possible values = CACHE, ORIGIN
		"""
		try :
			self._onpolicymatch = onpolicymatch
		except Exception as e:
			raise e

	@property
	def redirecturl(self) :
		ur"""URL of the server to which to redirect traffic if the cache redirection virtual server configured on the NetScaler appliance becomes unavailable.<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._redirecturl
		except Exception as e:
			raise e

	@redirecturl.setter
	def redirecturl(self, redirecturl) :
		ur"""URL of the server to which to redirect traffic if the cache redirection virtual server configured on the NetScaler appliance becomes unavailable.<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._redirecturl = redirecturl
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		ur"""Time-out value, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@clttimeout.setter
	def clttimeout(self, clttimeout) :
		ur"""Time-out value, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000
		"""
		try :
			self._clttimeout = clttimeout
		except Exception as e:
			raise e

	@property
	def precedence(self) :
		ur"""Type of policy (URL or RULE) that takes precedence on the cache redirection virtual server. Applies only to cache redirection virtual servers that have both URL and RULE based policies. If you specify URL, URL based policies are applied first, in the following order:
		1.   Domain and exact URL
		2.   Domain, prefix and suffix
		3.   Domain and suffix
		4.   Domain and prefix
		5.   Domain only
		6.   Exact URL
		7.   Prefix and suffix
		8.   Suffix only
		9.   Prefix only
		10.  Default
		If you specify RULE, the rule based policies are applied before URL based policies are applied.<br/>Default value: RULE<br/>Possible values = RULE, URL.
		"""
		try :
			return self._precedence
		except Exception as e:
			raise e

	@precedence.setter
	def precedence(self, precedence) :
		ur"""Type of policy (URL or RULE) that takes precedence on the cache redirection virtual server. Applies only to cache redirection virtual servers that have both URL and RULE based policies. If you specify URL, URL based policies are applied first, in the following order:
		1.   Domain and exact URL
		2.   Domain, prefix and suffix
		3.   Domain and suffix
		4.   Domain and prefix
		5.   Domain only
		6.   Exact URL
		7.   Prefix and suffix
		8.   Suffix only
		9.   Prefix only
		10.  Default
		If you specify RULE, the rule based policies are applied before URL based policies are applied.<br/>Default value: RULE<br/>Possible values = RULE, URL
		"""
		try :
			self._precedence = precedence
		except Exception as e:
			raise e

	@property
	def arp(self) :
		ur"""Use ARP to determine the destination MAC address.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._arp
		except Exception as e:
			raise e

	@arp.setter
	def arp(self, arp) :
		ur"""Use ARP to determine the destination MAC address.<br/>Possible values = ON, OFF
		"""
		try :
			self._arp = arp
		except Exception as e:
			raise e

	@property
	def ghost(self) :
		ur""".<br/>Possible values = ON, OFF.
		"""
		try :
			return self._ghost
		except Exception as e:
			raise e

	@ghost.setter
	def ghost(self, ghost) :
		ur""".<br/>Possible values = ON, OFF
		"""
		try :
			self._ghost = ghost
		except Exception as e:
			raise e

	@property
	def map(self) :
		ur"""Obsolete.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._map
		except Exception as e:
			raise e

	@map.setter
	def map(self, map) :
		ur"""Obsolete.<br/>Possible values = ON, OFF
		"""
		try :
			self._map = map
		except Exception as e:
			raise e

	@property
	def format(self) :
		ur""".<br/>Possible values = ON, OFF.
		"""
		try :
			return self._format
		except Exception as e:
			raise e

	@format.setter
	def format(self, format) :
		ur""".<br/>Possible values = ON, OFF
		"""
		try :
			self._format = format
		except Exception as e:
			raise e

	@property
	def via(self) :
		ur"""Insert a via header in each HTTP request. In the case of a cache miss, the request is redirected from the cache server to the origin server. This header indicates whether the request is being sent from a cache server.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._via
		except Exception as e:
			raise e

	@via.setter
	def via(self, via) :
		ur"""Insert a via header in each HTTP request. In the case of a cache miss, the request is redirected from the cache server to the origin server. This header indicates whether the request is being sent from a cache server.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._via = via
		except Exception as e:
			raise e

	@property
	def cachevserver(self) :
		ur"""Name of the default cache virtual server to which to redirect requests (the default target of the cache redirection virtual server).<br/>Minimum length =  1.
		"""
		try :
			return self._cachevserver
		except Exception as e:
			raise e

	@cachevserver.setter
	def cachevserver(self, cachevserver) :
		ur"""Name of the default cache virtual server to which to redirect requests (the default target of the cache redirection virtual server).<br/>Minimum length =  1
		"""
		try :
			self._cachevserver = cachevserver
		except Exception as e:
			raise e

	@property
	def dnsvservername(self) :
		ur"""Name of the DNS virtual server that resolves domain names arriving at the forward proxy virtual server.
		Note: This parameter applies only to forward proxy virtual servers, not reverse or transparent.<br/>Minimum length =  1.
		"""
		try :
			return self._dnsvservername
		except Exception as e:
			raise e

	@dnsvservername.setter
	def dnsvservername(self, dnsvservername) :
		ur"""Name of the DNS virtual server that resolves domain names arriving at the forward proxy virtual server.
		Note: This parameter applies only to forward proxy virtual servers, not reverse or transparent.<br/>Minimum length =  1
		"""
		try :
			self._dnsvservername = dnsvservername
		except Exception as e:
			raise e

	@property
	def destinationvserver(self) :
		ur"""Destination virtual server for a transparent or forward proxy cache redirection virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._destinationvserver
		except Exception as e:
			raise e

	@destinationvserver.setter
	def destinationvserver(self, destinationvserver) :
		ur"""Destination virtual server for a transparent or forward proxy cache redirection virtual server.<br/>Minimum length =  1
		"""
		try :
			self._destinationvserver = destinationvserver
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""Default domain for reverse proxies. Domains are configured to direct an incoming request from a specified source domain to a specified target domain. There can be several configured pairs of source and target domains. You can select one pair to be the default. If the host header or URL of an incoming request does not include a source domain, this option sends the request to the specified target domain.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""Default domain for reverse proxies. Domains are configured to direct an incoming request from a specified source domain to a specified target domain. There can be several configured pairs of source and target domains. You can select one pair to be the default. If the host header or URL of an incoming request does not include a source domain, this option sends the request to the specified target domain.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def sopersistencetimeout(self) :
		ur"""Time-out, in minutes, for spillover persistence.<br/>Minimum length =  2<br/>Maximum length =  24.
		"""
		try :
			return self._sopersistencetimeout
		except Exception as e:
			raise e

	@sopersistencetimeout.setter
	def sopersistencetimeout(self, sopersistencetimeout) :
		ur"""Time-out, in minutes, for spillover persistence.<br/>Minimum length =  2<br/>Maximum length =  24
		"""
		try :
			self._sopersistencetimeout = sopersistencetimeout
		except Exception as e:
			raise e

	@property
	def sothreshold(self) :
		ur"""For CONNECTION (or) DYNAMICCONNECTION spillover, the number of connections above which the virtual server enters spillover mode. For BANDWIDTH spillover, the amount of incoming and outgoing traffic (in Kbps) before spillover. For HEALTH spillover, the percentage of active services (by weight) below which spillover occurs.<br/>Minimum length =  1.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@sothreshold.setter
	def sothreshold(self, sothreshold) :
		ur"""For CONNECTION (or) DYNAMICCONNECTION spillover, the number of connections above which the virtual server enters spillover mode. For BANDWIDTH spillover, the amount of incoming and outgoing traffic (in Kbps) before spillover. For HEALTH spillover, the percentage of active services (by weight) below which spillover occurs.<br/>Minimum length =  1
		"""
		try :
			self._sothreshold = sothreshold
		except Exception as e:
			raise e

	@property
	def reuse(self) :
		ur"""Reuse TCP connections to the origin server across client connections. Do not set this parameter unless the Service Type parameter is set to HTTP. If you set this parameter to OFF, the possible settings of the Redirect parameter function as follows:
		* CACHE - TCP connections to the cache servers are not reused.
		* ORIGIN - TCP connections to the origin servers are not reused. 
		* POLICY - TCP connections to the origin servers are not reused.
		If you set the Reuse parameter to ON, connections to origin servers and connections to cache servers are reused.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._reuse
		except Exception as e:
			raise e

	@reuse.setter
	def reuse(self, reuse) :
		ur"""Reuse TCP connections to the origin server across client connections. Do not set this parameter unless the Service Type parameter is set to HTTP. If you set this parameter to OFF, the possible settings of the Redirect parameter function as follows:
		* CACHE - TCP connections to the cache servers are not reused.
		* ORIGIN - TCP connections to the origin servers are not reused. 
		* POLICY - TCP connections to the origin servers are not reused.
		If you set the Reuse parameter to ON, connections to origin servers and connections to cache servers are reused.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._reuse = reuse
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Initial state of the cache redirection virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Initial state of the cache redirection virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		ur"""Perform delayed cleanup of connections to this virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@downstateflush.setter
	def downstateflush(self, downstateflush) :
		ur"""Perform delayed cleanup of connections to this virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._downstateflush = downstateflush
		except Exception as e:
			raise e

	@property
	def backupvserver(self) :
		ur"""Name of the backup virtual server to which traffic is forwarded if the active server becomes unavailable.<br/>Minimum length =  1.
		"""
		try :
			return self._backupvserver
		except Exception as e:
			raise e

	@backupvserver.setter
	def backupvserver(self, backupvserver) :
		ur"""Name of the backup virtual server to which traffic is forwarded if the active server becomes unavailable.<br/>Minimum length =  1
		"""
		try :
			self._backupvserver = backupvserver
		except Exception as e:
			raise e

	@property
	def disableprimaryondown(self) :
		ur"""Continue sending traffic to a backup virtual server even after the primary virtual server comes UP from the DOWN state.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._disableprimaryondown
		except Exception as e:
			raise e

	@disableprimaryondown.setter
	def disableprimaryondown(self, disableprimaryondown) :
		ur"""Continue sending traffic to a backup virtual server even after the primary virtual server comes UP from the DOWN state.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._disableprimaryondown = disableprimaryondown
		except Exception as e:
			raise e

	@property
	def l2conn(self) :
		ur"""Use L2 parameters, such as MAC, VLAN, and channel to identify a connection.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._l2conn
		except Exception as e:
			raise e

	@l2conn.setter
	def l2conn(self, l2conn) :
		ur"""Use L2 parameters, such as MAC, VLAN, and channel to identify a connection.<br/>Possible values = ON, OFF
		"""
		try :
			self._l2conn = l2conn
		except Exception as e:
			raise e

	@property
	def backendssl(self) :
		ur"""Decides whether the backend connection made by NS to the origin server will be HTTP or SSL. Applicable only for SSL type CR Forward proxy vserver.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._backendssl
		except Exception as e:
			raise e

	@backendssl.setter
	def backendssl(self, backendssl) :
		ur"""Decides whether the backend connection made by NS to the origin server will be HTTP or SSL. Applicable only for SSL type CR Forward proxy vserver.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._backendssl = backendssl
		except Exception as e:
			raise e

	@property
	def listenpolicy(self) :
		ur"""String specifying the listen policy for the cache redirection virtual server. Can be either an in-line expression or the name of a named expression.<br/>Default value: "none".
		"""
		try :
			return self._listenpolicy
		except Exception as e:
			raise e

	@listenpolicy.setter
	def listenpolicy(self, listenpolicy) :
		ur"""String specifying the listen policy for the cache redirection virtual server. Can be either an in-line expression or the name of a named expression.<br/>Default value: "none"
		"""
		try :
			self._listenpolicy = listenpolicy
		except Exception as e:
			raise e

	@property
	def listenpriority(self) :
		ur"""Priority of the listen policy specified by the Listen Policy parameter. The lower the number, higher the priority.<br/>Default value: 101<br/>Maximum length =  100.
		"""
		try :
			return self._listenpriority
		except Exception as e:
			raise e

	@listenpriority.setter
	def listenpriority(self, listenpriority) :
		ur"""Priority of the listen policy specified by the Listen Policy parameter. The lower the number, higher the priority.<br/>Default value: 101<br/>Maximum length =  100
		"""
		try :
			self._listenpriority = listenpriority
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		ur"""Name of the profile containing TCP configuration information for the cache redirection virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@tcpprofilename.setter
	def tcpprofilename(self, tcpprofilename) :
		ur"""Name of the profile containing TCP configuration information for the cache redirection virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._tcpprofilename = tcpprofilename
		except Exception as e:
			raise e

	@property
	def httpprofilename(self) :
		ur"""Name of the profile containing HTTP configuration information for cache redirection virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._httpprofilename
		except Exception as e:
			raise e

	@httpprofilename.setter
	def httpprofilename(self, httpprofilename) :
		ur"""Name of the profile containing HTTP configuration information for cache redirection virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._httpprofilename = httpprofilename
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Comments associated with this virtual server.<br/>Maximum length =  256.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Comments associated with this virtual server.<br/>Maximum length =  256
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def srcipexpr(self) :
		ur"""Expression used to extract the source IP addresses from the requests originating from the cache. Can be either an in-line expression or the name of a named expression.<br/>Minimum length =  1<br/>Maximum length =  1500.
		"""
		try :
			return self._srcipexpr
		except Exception as e:
			raise e

	@srcipexpr.setter
	def srcipexpr(self, srcipexpr) :
		ur"""Expression used to extract the source IP addresses from the requests originating from the cache. Can be either an in-line expression or the name of a named expression.<br/>Minimum length =  1<br/>Maximum length =  1500
		"""
		try :
			self._srcipexpr = srcipexpr
		except Exception as e:
			raise e

	@property
	def originusip(self) :
		ur"""Use the client's IP address as the source IP address in requests sent to the origin server.  
		Note: You can enable this parameter to implement fully transparent CR deployment.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._originusip
		except Exception as e:
			raise e

	@originusip.setter
	def originusip(self, originusip) :
		ur"""Use the client's IP address as the source IP address in requests sent to the origin server.  
		Note: You can enable this parameter to implement fully transparent CR deployment.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._originusip = originusip
		except Exception as e:
			raise e

	@property
	def useportrange(self) :
		ur"""Use a port number from the port range (set by using the set ns param command, or in the Create Virtual Server (Cache Redirection) dialog box) as the source port in the requests sent to the origin server.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._useportrange
		except Exception as e:
			raise e

	@useportrange.setter
	def useportrange(self, useportrange) :
		ur"""Use a port number from the port range (set by using the set ns param command, or in the Create Virtual Server (Cache Redirection) dialog box) as the source port in the requests sent to the origin server.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._useportrange = useportrange
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		ur"""Enable logging of AppFlow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		ur"""Enable logging of AppFlow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		ur"""Name of the network profile containing network configurations for the cache redirection virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		ur"""Name of the network profile containing network configurations for the cache redirection virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def icmpvsrresponse(self) :
		ur"""Criterion for responding to PING requests sent to this virtual server. If ACTIVE, respond only if the virtual server is available. If PASSIVE, respond even if the virtual server is not available.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._icmpvsrresponse
		except Exception as e:
			raise e

	@icmpvsrresponse.setter
	def icmpvsrresponse(self, icmpvsrresponse) :
		ur"""Criterion for responding to PING requests sent to this virtual server. If ACTIVE, respond only if the virtual server is available. If PASSIVE, respond even if the virtual server is not available.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._icmpvsrresponse = icmpvsrresponse
		except Exception as e:
			raise e

	@property
	def rhistate(self) :
		ur"""A host route is injected according to the setting on the virtual servers
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always injects the hostroute.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if one virtual server set to ACTIVE is UP.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._rhistate
		except Exception as e:
			raise e

	@rhistate.setter
	def rhistate(self, rhistate) :
		ur"""A host route is injected according to the setting on the virtual servers
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always injects the hostroute.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if one virtual server set to ACTIVE is UP.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._rhistate = rhistate
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the cache redirection virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my name" or 'my name').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the cache redirection virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my name" or 'my name').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def ip(self) :
		try :
			return self._ip
		except Exception as e:
			raise e

	@property
	def value(self) :
		ur"""The ssl card status for the transparent ssl cr vserver.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def ngname(self) :
		ur"""Nodegroup devno to which this crvserver belongs to.
		"""
		try :
			return self._ngname
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Virtual server type.<br/>Possible values = CONTENT, ADDRESS.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		ur"""The state of the cr vserver.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""Status.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		ur"""Authentication.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authentication
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
	def rule(self) :
		ur"""Rule.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""Policies bound to this vserver.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""Service name.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Weight for this service.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@property
	def targetvserver(self) :
		ur"""The CSW target server names.
		"""
		try :
			return self._targetvserver
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""The priority for the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def somethod(self) :
		ur"""The spillover factor. When the main virtual server reaches this spillover threshold, it will give further traffic to the backupvserver.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE.
		"""
		try :
			return self._somethod
		except Exception as e:
			raise e

	@property
	def sopersistence(self) :
		ur"""The state of spillover persistence.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sopersistence
		except Exception as e:
			raise e

	@property
	def lbvserver(self) :
		ur"""The Default target server name.<br/>Minimum length =  1.
		"""
		try :
			return self._lbvserver
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(crvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.crvserver
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
		ur""" Use this API to add crvserver.
		"""
		try :
			if type(resource) is not list :
				addresource = crvserver()
				addresource.name = resource.name
				addresource.td = resource.td
				addresource.servicetype = resource.servicetype
				addresource.ipv46 = resource.ipv46
				addresource.port = resource.port
				addresource.range = resource.range
				addresource.cachetype = resource.cachetype
				addresource.redirect = resource.redirect
				addresource.onpolicymatch = resource.onpolicymatch
				addresource.redirecturl = resource.redirecturl
				addresource.clttimeout = resource.clttimeout
				addresource.precedence = resource.precedence
				addresource.arp = resource.arp
				addresource.ghost = resource.ghost
				addresource.map = resource.map
				addresource.format = resource.format
				addresource.via = resource.via
				addresource.cachevserver = resource.cachevserver
				addresource.dnsvservername = resource.dnsvservername
				addresource.destinationvserver = resource.destinationvserver
				addresource.domain = resource.domain
				addresource.sopersistencetimeout = resource.sopersistencetimeout
				addresource.sothreshold = resource.sothreshold
				addresource.reuse = resource.reuse
				addresource.state = resource.state
				addresource.downstateflush = resource.downstateflush
				addresource.backupvserver = resource.backupvserver
				addresource.disableprimaryondown = resource.disableprimaryondown
				addresource.l2conn = resource.l2conn
				addresource.backendssl = resource.backendssl
				addresource.listenpolicy = resource.listenpolicy
				addresource.listenpriority = resource.listenpriority
				addresource.tcpprofilename = resource.tcpprofilename
				addresource.httpprofilename = resource.httpprofilename
				addresource.comment = resource.comment
				addresource.srcipexpr = resource.srcipexpr
				addresource.originusip = resource.originusip
				addresource.useportrange = resource.useportrange
				addresource.appflowlog = resource.appflowlog
				addresource.netprofile = resource.netprofile
				addresource.icmpvsrresponse = resource.icmpvsrresponse
				addresource.rhistate = resource.rhistate
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ crvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].td = resource[i].td
						addresources[i].servicetype = resource[i].servicetype
						addresources[i].ipv46 = resource[i].ipv46
						addresources[i].port = resource[i].port
						addresources[i].range = resource[i].range
						addresources[i].cachetype = resource[i].cachetype
						addresources[i].redirect = resource[i].redirect
						addresources[i].onpolicymatch = resource[i].onpolicymatch
						addresources[i].redirecturl = resource[i].redirecturl
						addresources[i].clttimeout = resource[i].clttimeout
						addresources[i].precedence = resource[i].precedence
						addresources[i].arp = resource[i].arp
						addresources[i].ghost = resource[i].ghost
						addresources[i].map = resource[i].map
						addresources[i].format = resource[i].format
						addresources[i].via = resource[i].via
						addresources[i].cachevserver = resource[i].cachevserver
						addresources[i].dnsvservername = resource[i].dnsvservername
						addresources[i].destinationvserver = resource[i].destinationvserver
						addresources[i].domain = resource[i].domain
						addresources[i].sopersistencetimeout = resource[i].sopersistencetimeout
						addresources[i].sothreshold = resource[i].sothreshold
						addresources[i].reuse = resource[i].reuse
						addresources[i].state = resource[i].state
						addresources[i].downstateflush = resource[i].downstateflush
						addresources[i].backupvserver = resource[i].backupvserver
						addresources[i].disableprimaryondown = resource[i].disableprimaryondown
						addresources[i].l2conn = resource[i].l2conn
						addresources[i].backendssl = resource[i].backendssl
						addresources[i].listenpolicy = resource[i].listenpolicy
						addresources[i].listenpriority = resource[i].listenpriority
						addresources[i].tcpprofilename = resource[i].tcpprofilename
						addresources[i].httpprofilename = resource[i].httpprofilename
						addresources[i].comment = resource[i].comment
						addresources[i].srcipexpr = resource[i].srcipexpr
						addresources[i].originusip = resource[i].originusip
						addresources[i].useportrange = resource[i].useportrange
						addresources[i].appflowlog = resource[i].appflowlog
						addresources[i].netprofile = resource[i].netprofile
						addresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						addresources[i].rhistate = resource[i].rhistate
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete crvserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = crvserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update crvserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = crvserver()
				updateresource.name = resource.name
				updateresource.ipv46 = resource.ipv46
				updateresource.redirect = resource.redirect
				updateresource.onpolicymatch = resource.onpolicymatch
				updateresource.precedence = resource.precedence
				updateresource.arp = resource.arp
				updateresource.via = resource.via
				updateresource.cachevserver = resource.cachevserver
				updateresource.dnsvservername = resource.dnsvservername
				updateresource.destinationvserver = resource.destinationvserver
				updateresource.domain = resource.domain
				updateresource.reuse = resource.reuse
				updateresource.backupvserver = resource.backupvserver
				updateresource.disableprimaryondown = resource.disableprimaryondown
				updateresource.redirecturl = resource.redirecturl
				updateresource.clttimeout = resource.clttimeout
				updateresource.downstateflush = resource.downstateflush
				updateresource.l2conn = resource.l2conn
				updateresource.backendssl = resource.backendssl
				updateresource.listenpolicy = resource.listenpolicy
				updateresource.listenpriority = resource.listenpriority
				updateresource.tcpprofilename = resource.tcpprofilename
				updateresource.httpprofilename = resource.httpprofilename
				updateresource.netprofile = resource.netprofile
				updateresource.comment = resource.comment
				updateresource.srcipexpr = resource.srcipexpr
				updateresource.originusip = resource.originusip
				updateresource.useportrange = resource.useportrange
				updateresource.appflowlog = resource.appflowlog
				updateresource.icmpvsrresponse = resource.icmpvsrresponse
				updateresource.rhistate = resource.rhistate
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ crvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipv46 = resource[i].ipv46
						updateresources[i].redirect = resource[i].redirect
						updateresources[i].onpolicymatch = resource[i].onpolicymatch
						updateresources[i].precedence = resource[i].precedence
						updateresources[i].arp = resource[i].arp
						updateresources[i].via = resource[i].via
						updateresources[i].cachevserver = resource[i].cachevserver
						updateresources[i].dnsvservername = resource[i].dnsvservername
						updateresources[i].destinationvserver = resource[i].destinationvserver
						updateresources[i].domain = resource[i].domain
						updateresources[i].reuse = resource[i].reuse
						updateresources[i].backupvserver = resource[i].backupvserver
						updateresources[i].disableprimaryondown = resource[i].disableprimaryondown
						updateresources[i].redirecturl = resource[i].redirecturl
						updateresources[i].clttimeout = resource[i].clttimeout
						updateresources[i].downstateflush = resource[i].downstateflush
						updateresources[i].l2conn = resource[i].l2conn
						updateresources[i].backendssl = resource[i].backendssl
						updateresources[i].listenpolicy = resource[i].listenpolicy
						updateresources[i].listenpriority = resource[i].listenpriority
						updateresources[i].tcpprofilename = resource[i].tcpprofilename
						updateresources[i].httpprofilename = resource[i].httpprofilename
						updateresources[i].netprofile = resource[i].netprofile
						updateresources[i].comment = resource[i].comment
						updateresources[i].srcipexpr = resource[i].srcipexpr
						updateresources[i].originusip = resource[i].originusip
						updateresources[i].useportrange = resource[i].useportrange
						updateresources[i].appflowlog = resource[i].appflowlog
						updateresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						updateresources[i].rhistate = resource[i].rhistate
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of crvserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = crvserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable crvserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = crvserver()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable crvserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = crvserver()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ crvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a crvserver resource.
		"""
		try :
			renameresource = crvserver()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the crvserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = crvserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = crvserver()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [crvserver() for _ in range(len(name))]
							obj = [crvserver() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = crvserver()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of crvserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = crvserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the crvserver resources configured on NetScaler.
		"""
		try :
			obj = crvserver()
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
		ur""" Use this API to count filtered the set of crvserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = crvserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Rhistate:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Authentication:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Map:
		ON = "ON"
		OFF = "OFF"

	class Cachetype:
		TRANSPARENT = "TRANSPARENT"
		REVERSE = "REVERSE"
		FORWARD = "FORWARD"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Servicetype:
		HTTP = "HTTP"
		SSL = "SSL"
		NNTP = "NNTP"
		HDX = "HDX"

	class Icmpvsrresponse:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class L2conn:
		ON = "ON"
		OFF = "OFF"

	class Type:
		CONTENT = "CONTENT"
		ADDRESS = "ADDRESS"

	class Useportrange:
		ON = "ON"
		OFF = "OFF"

	class Disableprimaryondown:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Somethod:
		CONNECTION = "CONNECTION"
		DYNAMICCONNECTION = "DYNAMICCONNECTION"
		BANDWIDTH = "BANDWIDTH"
		HEALTH = "HEALTH"
		NONE = "NONE"

	class Sopersistence:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Arp:
		ON = "ON"
		OFF = "OFF"

	class Redirect:
		CACHE = "CACHE"
		POLICY = "POLICY"
		ORIGIN = "ORIGIN"

	class Onpolicymatch:
		CACHE = "CACHE"
		ORIGIN = "ORIGIN"

	class Ghost:
		ON = "ON"
		OFF = "OFF"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Originusip:
		ON = "ON"
		OFF = "OFF"

	class Precedence:
		RULE = "RULE"
		URL = "URL"

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

	class Reuse:
		ON = "ON"
		OFF = "OFF"

	class Via:
		ON = "ON"
		OFF = "OFF"

	class Format:
		ON = "ON"
		OFF = "OFF"

	class Backendssl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class crvserver_response(base_response) :
	def __init__(self, length=1) :
		self.crvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.crvserver = [crvserver() for _ in range(length)]

