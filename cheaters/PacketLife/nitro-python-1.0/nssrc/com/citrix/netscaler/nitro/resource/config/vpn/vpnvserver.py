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

class vpnvserver(base_resource) :
	""" Configuration for VPN virtual server resource. """
	def __init__(self) :
		self._name = ""
		self._servicetype = ""
		self._ipv46 = ""
		self._range = 0
		self._port = 0
		self._state = ""
		self._authentication = ""
		self._doublehop = ""
		self._maxaaausers = 0
		self._icaonly = ""
		self._icaproxysessionmigration = ""
		self._advancedepa = ""
		self._devicecert = ""
		self._certkeynames = ""
		self._downstateflush = ""
		self._listenpolicy = ""
		self._listenpriority = 0
		self._tcpprofilename = ""
		self._httpprofilename = ""
		self._comment = ""
		self._appflowlog = ""
		self._icmpvsrresponse = ""
		self._rhistate = ""
		self._netprofile = ""
		self._cginfrahomepageredirect = ""
		self._maxloginattempts = 0
		self._failedlogintimeout = 0
		self._l2conn = ""
		self._deploymenttype = ""
		self._newname = ""
		self._ip = ""
		self._value = ""
		self._type = ""
		self._curstate = ""
		self._status = 0
		self._cachetype = ""
		self._redirect = ""
		self._precedence = ""
		self._redirecturl = ""
		self._curaaausers = 0
		self._curtotalusers = 0
		self._domain = ""
		self._rule = ""
		self._policy = ""
		self._servicename = ""
		self._weight = 0
		self._cachevserver = ""
		self._backupvserver = ""
		self._priority = 0
		self._clttimeout = 0
		self._somethod = ""
		self._sothreshold = 0
		self._sopersistence = ""
		self._sopersistencetimeout = 0
		self._usemip = ""
		self._map = ""
		self._bindpoint = ""
		self._gotopriorityexpression = ""
		self._disableprimaryondown = ""
		self._secondary = False
		self._groupextraction = False
		self._epaprofileoptional = False
		self._ngname = ""
		self._response = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the NetScaler Gateway virtual server. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my server" or 'my server').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the NetScaler Gateway virtual server. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my server" or 'my server').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		ur"""Protocol used by the NetScaler Gateway virtual server.<br/>Default value: SSL<br/>Possible values = SSL.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		ur"""Protocol used by the NetScaler Gateway virtual server.<br/>Default value: SSL<br/>Possible values = SSL
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def ipv46(self) :
		ur"""IPv4 or IPv6 address of the NetScaler Gateway virtual server. Usually a public IP address. User devices send connection requests to this IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._ipv46
		except Exception as e:
			raise e

	@ipv46.setter
	def ipv46(self, ipv46) :
		ur"""IPv4 or IPv6 address of the NetScaler Gateway virtual server. Usually a public IP address. User devices send connection requests to this IP address.<br/>Minimum length =  1
		"""
		try :
			self._ipv46 = ipv46
		except Exception as e:
			raise e

	@property
	def range(self) :
		ur"""Range of NetScaler Gateway virtual server IP addresses. The consecutively numbered range of IP addresses begins with the address specified by the IP Address parameter. 
		In the configuration utility, select Network VServer to enter a range.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._range
		except Exception as e:
			raise e

	@range.setter
	def range(self, range) :
		ur"""Range of NetScaler Gateway virtual server IP addresses. The consecutively numbered range of IP addresses begins with the address specified by the IP Address parameter. 
		In the configuration utility, select Network VServer to enter a range.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._range = range
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""TCP port on which the virtual server listens.<br/>Minimum length =  1<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""TCP port on which the virtual server listens.<br/>Minimum length =  1<br/>Range 1 - 65535
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of the virtual server. If the virtual server is disabled, requests are not processed.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""State of the virtual server. If the virtual server is disabled, requests are not processed.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		ur"""Require authentication for users connecting to NetScaler Gateway.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		ur"""Require authentication for users connecting to NetScaler Gateway.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	@property
	def doublehop(self) :
		ur"""Use the NetScaler Gateway appliance in a double-hop configuration. A double-hop deployment provides an extra layer of security for the internal network by using three firewalls to divide the DMZ into two stages. Such a deployment can have one appliance in the DMZ and one appliance in the secure network.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._doublehop
		except Exception as e:
			raise e

	@doublehop.setter
	def doublehop(self, doublehop) :
		ur"""Use the NetScaler Gateway appliance in a double-hop configuration. A double-hop deployment provides an extra layer of security for the internal network by using three firewalls to divide the DMZ into two stages. Such a deployment can have one appliance in the DMZ and one appliance in the secure network.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._doublehop = doublehop
		except Exception as e:
			raise e

	@property
	def maxaaausers(self) :
		ur"""Maximum number of concurrent user sessions allowed on this virtual server. The actual number of users allowed to log on to this virtual server depends on the total number of user licenses.
		"""
		try :
			return self._maxaaausers
		except Exception as e:
			raise e

	@maxaaausers.setter
	def maxaaausers(self, maxaaausers) :
		ur"""Maximum number of concurrent user sessions allowed on this virtual server. The actual number of users allowed to log on to this virtual server depends on the total number of user licenses.
		"""
		try :
			self._maxaaausers = maxaaausers
		except Exception as e:
			raise e

	@property
	def icaonly(self) :
		ur"""User can log on in Basic mode only, through either Citrix Receiver or a browser. Users are not allowed to connect by using the NetScaler Gateway Plug-in.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._icaonly
		except Exception as e:
			raise e

	@icaonly.setter
	def icaonly(self, icaonly) :
		ur"""User can log on in Basic mode only, through either Citrix Receiver or a browser. Users are not allowed to connect by using the NetScaler Gateway Plug-in.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._icaonly = icaonly
		except Exception as e:
			raise e

	@property
	def icaproxysessionmigration(self) :
		ur"""This option determines if an existing ICA Proxy session is transferred when the user logs on from another device.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._icaproxysessionmigration
		except Exception as e:
			raise e

	@icaproxysessionmigration.setter
	def icaproxysessionmigration(self, icaproxysessionmigration) :
		ur"""This option determines if an existing ICA Proxy session is transferred when the user logs on from another device.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._icaproxysessionmigration = icaproxysessionmigration
		except Exception as e:
			raise e

	@property
	def advancedepa(self) :
		ur"""This option tells whether advanced EPA is enabled on this virtual server.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._advancedepa
		except Exception as e:
			raise e

	@advancedepa.setter
	def advancedepa(self, advancedepa) :
		ur"""This option tells whether advanced EPA is enabled on this virtual server.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._advancedepa = advancedepa
		except Exception as e:
			raise e

	@property
	def devicecert(self) :
		ur"""Indicates whether device certificate check as a part of EPA is on or off.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._devicecert
		except Exception as e:
			raise e

	@devicecert.setter
	def devicecert(self, devicecert) :
		ur"""Indicates whether device certificate check as a part of EPA is on or off.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._devicecert = devicecert
		except Exception as e:
			raise e

	@property
	def certkeynames(self) :
		ur"""Name of the certificate key that was bound to the corresponding SSL virtual server as the Certificate Authority for the device certificate.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._certkeynames
		except Exception as e:
			raise e

	@certkeynames.setter
	def certkeynames(self, certkeynames) :
		ur"""Name of the certificate key that was bound to the corresponding SSL virtual server as the Certificate Authority for the device certificate.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._certkeynames = certkeynames
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		ur"""Close existing connections when the virtual server is marked DOWN, which means the server might have timed out. Disconnecting existing connections frees resources and in certain cases speeds recovery of overloaded load balancing setups. Enable this setting on servers in which the connections can safely be closed when they are marked DOWN.  Do not enable DOWN state flush on servers that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@downstateflush.setter
	def downstateflush(self, downstateflush) :
		ur"""Close existing connections when the virtual server is marked DOWN, which means the server might have timed out. Disconnecting existing connections frees resources and in certain cases speeds recovery of overloaded load balancing setups. Enable this setting on servers in which the connections can safely be closed when they are marked DOWN.  Do not enable DOWN state flush on servers that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._downstateflush = downstateflush
		except Exception as e:
			raise e

	@property
	def listenpolicy(self) :
		ur"""String specifying the listen policy for the NetScaler Gateway virtual server. Can be either a named expression or a default syntax expression. The NetScaler Gateway virtual server processes only the traffic for which the expression evaluates to true.<br/>Default value: "none".
		"""
		try :
			return self._listenpolicy
		except Exception as e:
			raise e

	@listenpolicy.setter
	def listenpolicy(self, listenpolicy) :
		ur"""String specifying the listen policy for the NetScaler Gateway virtual server. Can be either a named expression or a default syntax expression. The NetScaler Gateway virtual server processes only the traffic for which the expression evaluates to true.<br/>Default value: "none"
		"""
		try :
			self._listenpolicy = listenpolicy
		except Exception as e:
			raise e

	@property
	def listenpriority(self) :
		ur"""Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server, the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.<br/>Default value: 101<br/>Maximum length =  100.
		"""
		try :
			return self._listenpriority
		except Exception as e:
			raise e

	@listenpriority.setter
	def listenpriority(self, listenpriority) :
		ur"""Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server, the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.<br/>Default value: 101<br/>Maximum length =  100
		"""
		try :
			self._listenpriority = listenpriority
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		ur"""Name of the TCP profile to assign to this virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@tcpprofilename.setter
	def tcpprofilename(self, tcpprofilename) :
		ur"""Name of the TCP profile to assign to this virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._tcpprofilename = tcpprofilename
		except Exception as e:
			raise e

	@property
	def httpprofilename(self) :
		ur"""Name of the HTTP profile to assign to this virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._httpprofilename
		except Exception as e:
			raise e

	@httpprofilename.setter
	def httpprofilename(self, httpprofilename) :
		ur"""Name of the HTTP profile to assign to this virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._httpprofilename = httpprofilename
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments associated with the virtual server.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments associated with the virtual server.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		ur"""Log AppFlow records that contain standard NetFlow or IPFIX information, such as time stamps for the beginning and end of a flow, packet count, and byte count. Also log records that contain application-level information, such as HTTP web addresses, HTTP request methods and response status codes, server response time, and latency.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		ur"""Log AppFlow records that contain standard NetFlow or IPFIX information, such as time stamps for the beginning and end of a flow, packet count, and byte count. Also log records that contain application-level information, such as HTTP web addresses, HTTP request methods and response status codes, server response time, and latency.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def icmpvsrresponse(self) :
		ur"""Criterion for responding to PING requests sent to this virtual server. If this parameter is set to ACTIVE, respond only if the virtual server is available. With the PASSIVE setting, respond even if the virtual server is not available.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._icmpvsrresponse
		except Exception as e:
			raise e

	@icmpvsrresponse.setter
	def icmpvsrresponse(self, icmpvsrresponse) :
		ur"""Criterion for responding to PING requests sent to this virtual server. If this parameter is set to ACTIVE, respond only if the virtual server is available. With the PASSIVE setting, respond even if the virtual server is not available.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._icmpvsrresponse = icmpvsrresponse
		except Exception as e:
			raise e

	@property
	def rhistate(self) :
		ur"""A host route is injected according to the setting on the virtual servers.
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always injects the hostroute.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance injects even if one virtual server set to ACTIVE is UP.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE.
		"""
		try :
			return self._rhistate
		except Exception as e:
			raise e

	@rhistate.setter
	def rhistate(self, rhistate) :
		ur"""A host route is injected according to the setting on the virtual servers.
		* If set to PASSIVE on all the virtual servers that share the IP address, the appliance always injects the hostroute.
		* If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.
		* If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance injects even if one virtual server set to ACTIVE is UP.<br/>Default value: PASSIVE<br/>Possible values = PASSIVE, ACTIVE
		"""
		try :
			self._rhistate = rhistate
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		ur"""The name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		ur"""The name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def cginfrahomepageredirect(self) :
		ur"""When client requests ShareFile resources and NetScaler Gateway detects that the user is unauthenticated or the user session has expired, disabling this option takes the user to the originally requested ShareFile resource after authentication (instead of taking the user to the default VPN home page).<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cginfrahomepageredirect
		except Exception as e:
			raise e

	@cginfrahomepageredirect.setter
	def cginfrahomepageredirect(self, cginfrahomepageredirect) :
		ur"""When client requests ShareFile resources and NetScaler Gateway detects that the user is unauthenticated or the user session has expired, disabling this option takes the user to the originally requested ShareFile resource after authentication (instead of taking the user to the default VPN home page).<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cginfrahomepageredirect = cginfrahomepageredirect
		except Exception as e:
			raise e

	@property
	def maxloginattempts(self) :
		ur"""Maximum number of logon attempts.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._maxloginattempts
		except Exception as e:
			raise e

	@maxloginattempts.setter
	def maxloginattempts(self, maxloginattempts) :
		ur"""Maximum number of logon attempts.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._maxloginattempts = maxloginattempts
		except Exception as e:
			raise e

	@property
	def failedlogintimeout(self) :
		ur"""Number of minutes an account will be locked if user exceeds maximum permissible attempts.<br/>Minimum length =  1.
		"""
		try :
			return self._failedlogintimeout
		except Exception as e:
			raise e

	@failedlogintimeout.setter
	def failedlogintimeout(self, failedlogintimeout) :
		ur"""Number of minutes an account will be locked if user exceeds maximum permissible attempts.<br/>Minimum length =  1
		"""
		try :
			self._failedlogintimeout = failedlogintimeout
		except Exception as e:
			raise e

	@property
	def l2conn(self) :
		ur"""Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>) that is used to identify a connection. Allows multiple TCP and non-TCP connections with the same 4-tuple to coexist on the NetScaler appliance.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._l2conn
		except Exception as e:
			raise e

	@l2conn.setter
	def l2conn(self, l2conn) :
		ur"""Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>) that is used to identify a connection. Allows multiple TCP and non-TCP connections with the same 4-tuple to coexist on the NetScaler appliance.<br/>Possible values = ON, OFF
		"""
		try :
			self._l2conn = l2conn
		except Exception as e:
			raise e

	@property
	def deploymenttype(self) :
		ur""".<br/>Default value: 5<br/>Possible values = NONE, ICA_WEBINTERFACE, ICA_STOREFRONT, MOBILITY, WIONNS.
		"""
		try :
			return self._deploymenttype
		except Exception as e:
			raise e

	@deploymenttype.setter
	def deploymenttype(self, deploymenttype) :
		ur""".<br/>Default value: 5<br/>Possible values = NONE, ICA_WEBINTERFACE, ICA_STOREFRONT, MOBILITY, WIONNS
		"""
		try :
			self._deploymenttype = deploymenttype
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the NetScaler Gateway virtual server. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my server" or 'my server').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the NetScaler Gateway virtual server. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my server" or 'my server').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def ip(self) :
		ur"""The Virtual IP address of the VPN virtual server.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@property
	def value(self) :
		ur"""Indicates whether or not the certificate is bound or if SSL offload is disabled.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""The type of virtual server; for example, CONTENT based or ADDRESS based.<br/>Possible values = CONTENT, ADDRESS.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		ur"""The current state of the virtual server, as UP, DOWN, BUSY, and so on.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""Whether or not this virtual server responds to ARPs and whether or not round-robin selection is temporarily in effect.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def cachetype(self) :
		ur"""Virtual server cache type. The options are: TRANSPARENT, REVERSE, and FORWARD.<br/>Possible values = TRANSPARENT, REVERSE, FORWARD.
		"""
		try :
			return self._cachetype
		except Exception as e:
			raise e

	@property
	def redirect(self) :
		ur"""The cache redirect policy.
		The valid redirect policies are:
		l.	CACHE - Directs all requests to the cache.
		2.	POLICY - Applies cache redirection policy to determine whether the request should be directed to the cache or origin. This is the default setting.
		3.	ORIGIN - Directs all requests to the origin server.<br/>Possible values = CACHE, POLICY, ORIGIN.
		"""
		try :
			return self._redirect
		except Exception as e:
			raise e

	@property
	def precedence(self) :
		ur"""This argument is used only when configuring content switching on the specified virtual server. This is applicable only
		if both the URL and RULE-based policies have been configured on the same virtual server.
		It specifies the type of policy (URL or RULE) that takes precedence on the content switching virtual server. The default setting is RULE.
		l	URL - In this case, the incoming request is matched against the URL-based policies before the rule-based policies.
		l	RULE - In this case, the incoming request is matched against the rule-based policies before the URL-based policies.
		For all URL-based policies, the precedence hierarchy is:
		1.	Domain and exact URL
		2.	Domain, prefix, and suffix
		3.	Domain and suffix
		4.	Domain and prefix
		5.	Domain only
		6.	Exact URL
		7.	Prefix and suffix
		8.	Suffix only
		9.	Prefix only
		10.	Default.<br/>Possible values = RULE, URL.
		"""
		try :
			return self._precedence
		except Exception as e:
			raise e

	@property
	def redirecturl(self) :
		ur"""The URL where traffic is redirected if the virtual server in system becomes unavailable. WARNING!	Make sure that the domain you specify in the URL does not match the domain specified in the -d domainName argument of the ###add cs policy### command. If the same domain is specified in both arguments, the request will be continuously redirected to the same unavailable virtual server in the system. If so, the user may not get the requested content.
		"""
		try :
			return self._redirecturl
		except Exception as e:
			raise e

	@property
	def curaaausers(self) :
		ur"""The number of current users logged on to this virtual server.
		"""
		try :
			return self._curaaausers
		except Exception as e:
			raise e

	@property
	def curtotalusers(self) :
		ur"""The total number of current users connected through this virtual server.
		"""
		try :
			return self._curtotalusers
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""The domain name of the server for which a service needs to be added. If the IP address has been specified, the domain name does not need to be specified.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""The name of the rule, or expression, if any, that policy for the VPN server is to use. Rules are combinations of expressions. Expressions are simple conditions, such as a test for equality, applied to operands, such as a URL string or an IP address. Expression syntax is described in the Installation and Configuration Guide. The default rule is ns_true.<br/>Minimum length =  1.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@property
	def policy(self) :
		ur"""The name of the policy, if any, bound to the VPN virtual server.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""The name of the service, if any, to which the virtual server policy is bound.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Weight for this service, if any. This weight is used when the system performs load balancing, giving greater priority to a specific service. It is useful when the services bound to a virtual server are of different capacity.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@property
	def cachevserver(self) :
		ur"""The name of the default target cache virtual server, if any, to which requests are redirected.
		"""
		try :
			return self._cachevserver
		except Exception as e:
			raise e

	@property
	def backupvserver(self) :
		ur"""The name of the backup VPN virtual server for this VPN virtual server.
		"""
		try :
			return self._backupvserver
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""The priority, if any, of the VPN virtual server policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		ur"""The idle time, if any, in seconds after which the client connection is terminated.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@property
	def somethod(self) :
		ur"""VPN client applications are allocated from a block of intranet IP addresses.
		That block may be exhausted after a certain number of connections. This switch specifies the
		method used to determine whether or not a new connection will spill over, or exhaust, the allocated block of
		intranet IP addresses for that application. Possible values are CONNECTION or DYNAMICCONNECTION.
		CONNECTION means that a static integer value is the hard limit for the spillover threshold. The spillover
		threshold is described below. DYNAMICCONNECTION means that the spillover threshold is set according to
		the maximum number of connections defined for the VPN virtual server.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE.
		"""
		try :
			return self._somethod
		except Exception as e:
			raise e

	@property
	def sothreshold(self) :
		ur"""VPN client applications are allocated from a block of intranet IP addresses.
		That block may be exhausted after a certain number of connections.
		The value of this option is the number of client connections after which the mapped IP address is used
		as the client source IP address instead of an address from the allocated block of intranet IP addresses.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@property
	def sopersistence(self) :
		ur"""Whether or not cookie-based site persistance is enabled for this VPN vserver. Possible values are 'ConnectionProxy', HTTPRedirect, or NONE.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sopersistence
		except Exception as e:
			raise e

	@property
	def sopersistencetimeout(self) :
		ur"""The timeout, if any, for cookie-based site persistance of this VPN vserver.
		"""
		try :
			return self._sopersistencetimeout
		except Exception as e:
			raise e

	@property
	def usemip(self) :
		ur"""Deprecated. See 'map' below.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._usemip
		except Exception as e:
			raise e

	@property
	def map(self) :
		ur"""Whether or not mapped IP addresses are ON or OFF. Mapped IP addresses are source IP addresses
		for the virtual servers running on the NetScaler. Mapped IP addresses are used by the system to connect to the backend servers.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._map
		except Exception as e:
			raise e

	@property
	def bindpoint(self) :
		ur"""Bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE, ICA_REQUEST, OTHERTCP_REQUEST.
		"""
		try :
			return self._bindpoint
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Next priority expression.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def disableprimaryondown(self) :
		ur"""Tells whether traffic will continue reaching backup virtual servers even after the primary virtual server comes UP from DOWN state.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._disableprimaryondown
		except Exception as e:
			raise e

	@property
	def secondary(self) :
		ur"""Binds the authentication policy as the secondary policy to use in a two-factor configuration. A user must then authenticate not only via a primary authentication method but also via a secondary authentication method. User groups are aggregated across both. The user name must be exactly the same for both authentication methods, but they can require different passwords.
		"""
		try :
			return self._secondary
		except Exception as e:
			raise e

	@property
	def groupextraction(self) :
		ur"""Binds the authentication policy to a tertiary chain which will be used only for group extraction.  The user will not authenticate against this server, and this will only be called if primary and/or secondary authentication has succeeded.
		"""
		try :
			return self._groupextraction
		except Exception as e:
			raise e

	@property
	def epaprofileoptional(self) :
		ur"""Mark the EPA profile optional for preauthentication EPA profile. User would be shown a logon page even if the EPA profile fails to evaluate.
		"""
		try :
			return self._epaprofileoptional
		except Exception as e:
			raise e

	@property
	def ngname(self) :
		ur"""Node group devno to which this authentication virtual sever belongs.
		"""
		try :
			return self._ngname
		except Exception as e:
			raise e

	@property
	def response(self) :
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnvserver
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
		ur""" Use this API to add vpnvserver.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnvserver()
				addresource.name = resource.name
				addresource.servicetype = resource.servicetype
				addresource.ipv46 = resource.ipv46
				addresource.range = resource.range
				addresource.port = resource.port
				addresource.state = resource.state
				addresource.authentication = resource.authentication
				addresource.doublehop = resource.doublehop
				addresource.maxaaausers = resource.maxaaausers
				addresource.icaonly = resource.icaonly
				addresource.icaproxysessionmigration = resource.icaproxysessionmigration
				addresource.advancedepa = resource.advancedepa
				addresource.devicecert = resource.devicecert
				addresource.certkeynames = resource.certkeynames
				addresource.downstateflush = resource.downstateflush
				addresource.listenpolicy = resource.listenpolicy
				addresource.listenpriority = resource.listenpriority
				addresource.tcpprofilename = resource.tcpprofilename
				addresource.httpprofilename = resource.httpprofilename
				addresource.comment = resource.comment
				addresource.appflowlog = resource.appflowlog
				addresource.icmpvsrresponse = resource.icmpvsrresponse
				addresource.rhistate = resource.rhistate
				addresource.netprofile = resource.netprofile
				addresource.cginfrahomepageredirect = resource.cginfrahomepageredirect
				addresource.maxloginattempts = resource.maxloginattempts
				addresource.failedlogintimeout = resource.failedlogintimeout
				addresource.l2conn = resource.l2conn
				addresource.deploymenttype = resource.deploymenttype
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].servicetype = resource[i].servicetype
						addresources[i].ipv46 = resource[i].ipv46
						addresources[i].range = resource[i].range
						addresources[i].port = resource[i].port
						addresources[i].state = resource[i].state
						addresources[i].authentication = resource[i].authentication
						addresources[i].doublehop = resource[i].doublehop
						addresources[i].maxaaausers = resource[i].maxaaausers
						addresources[i].icaonly = resource[i].icaonly
						addresources[i].icaproxysessionmigration = resource[i].icaproxysessionmigration
						addresources[i].advancedepa = resource[i].advancedepa
						addresources[i].devicecert = resource[i].devicecert
						addresources[i].certkeynames = resource[i].certkeynames
						addresources[i].downstateflush = resource[i].downstateflush
						addresources[i].listenpolicy = resource[i].listenpolicy
						addresources[i].listenpriority = resource[i].listenpriority
						addresources[i].tcpprofilename = resource[i].tcpprofilename
						addresources[i].httpprofilename = resource[i].httpprofilename
						addresources[i].comment = resource[i].comment
						addresources[i].appflowlog = resource[i].appflowlog
						addresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						addresources[i].rhistate = resource[i].rhistate
						addresources[i].netprofile = resource[i].netprofile
						addresources[i].cginfrahomepageredirect = resource[i].cginfrahomepageredirect
						addresources[i].maxloginattempts = resource[i].maxloginattempts
						addresources[i].failedlogintimeout = resource[i].failedlogintimeout
						addresources[i].l2conn = resource[i].l2conn
						addresources[i].deploymenttype = resource[i].deploymenttype
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete vpnvserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnvserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update vpnvserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpnvserver()
				updateresource.name = resource.name
				updateresource.ipv46 = resource.ipv46
				updateresource.authentication = resource.authentication
				updateresource.doublehop = resource.doublehop
				updateresource.icaonly = resource.icaonly
				updateresource.icaproxysessionmigration = resource.icaproxysessionmigration
				updateresource.advancedepa = resource.advancedepa
				updateresource.devicecert = resource.devicecert
				updateresource.certkeynames = resource.certkeynames
				updateresource.maxaaausers = resource.maxaaausers
				updateresource.downstateflush = resource.downstateflush
				updateresource.listenpolicy = resource.listenpolicy
				updateresource.listenpriority = resource.listenpriority
				updateresource.tcpprofilename = resource.tcpprofilename
				updateresource.httpprofilename = resource.httpprofilename
				updateresource.comment = resource.comment
				updateresource.appflowlog = resource.appflowlog
				updateresource.icmpvsrresponse = resource.icmpvsrresponse
				updateresource.rhistate = resource.rhistate
				updateresource.netprofile = resource.netprofile
				updateresource.cginfrahomepageredirect = resource.cginfrahomepageredirect
				updateresource.maxloginattempts = resource.maxloginattempts
				updateresource.failedlogintimeout = resource.failedlogintimeout
				updateresource.l2conn = resource.l2conn
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipv46 = resource[i].ipv46
						updateresources[i].authentication = resource[i].authentication
						updateresources[i].doublehop = resource[i].doublehop
						updateresources[i].icaonly = resource[i].icaonly
						updateresources[i].icaproxysessionmigration = resource[i].icaproxysessionmigration
						updateresources[i].advancedepa = resource[i].advancedepa
						updateresources[i].devicecert = resource[i].devicecert
						updateresources[i].certkeynames = resource[i].certkeynames
						updateresources[i].maxaaausers = resource[i].maxaaausers
						updateresources[i].downstateflush = resource[i].downstateflush
						updateresources[i].listenpolicy = resource[i].listenpolicy
						updateresources[i].listenpriority = resource[i].listenpriority
						updateresources[i].tcpprofilename = resource[i].tcpprofilename
						updateresources[i].httpprofilename = resource[i].httpprofilename
						updateresources[i].comment = resource[i].comment
						updateresources[i].appflowlog = resource[i].appflowlog
						updateresources[i].icmpvsrresponse = resource[i].icmpvsrresponse
						updateresources[i].rhistate = resource[i].rhistate
						updateresources[i].netprofile = resource[i].netprofile
						updateresources[i].cginfrahomepageredirect = resource[i].cginfrahomepageredirect
						updateresources[i].maxloginattempts = resource[i].maxloginattempts
						updateresources[i].failedlogintimeout = resource[i].failedlogintimeout
						updateresources[i].l2conn = resource[i].l2conn
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of vpnvserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnvserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable vpnvserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = vpnvserver()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable vpnvserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = vpnvserver()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ vpnvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a vpnvserver resource.
		"""
		try :
			renameresource = vpnvserver()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def check(cls, client, resource) :
		ur""" Use this API to check vpnvserver.
		"""
		try :
			if type(resource) is not list :
				checkresource = vpnvserver()
				checkresource.name = resource.name
				return checkresource.perform_operation(client,"check")
			else :
				if (resource and len(resource) > 0) :
					checkresources = [ vpnvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						checkresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, checkresources,"check")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the vpnvserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnvserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = vpnvserver()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [vpnvserver() for _ in range(len(name))]
							obj = [vpnvserver() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = vpnvserver()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of vpnvserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the vpnvserver resources configured on NetScaler.
		"""
		try :
			obj = vpnvserver()
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
		ur""" Use this API to count filtered the set of vpnvserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Icaonly:
		ON = "ON"
		OFF = "OFF"

	class Cginfrahomepageredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rhistate:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Deploymenttype:
		NONE = "NONE"
		ICA_WEBINTERFACE = "ICA_WEBINTERFACE"
		ICA_STOREFRONT = "ICA_STOREFRONT"
		MOBILITY = "MOBILITY"
		WIONNS = "WIONNS"

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

	class Devicecert:
		ON = "ON"
		OFF = "OFF"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Servicetype:
		SSL = "SSL"

	class Icmpvsrresponse:
		PASSIVE = "PASSIVE"
		ACTIVE = "ACTIVE"

	class Usemip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class L2conn:
		ON = "ON"
		OFF = "OFF"

	class Icaproxysessionmigration:
		ON = "ON"
		OFF = "OFF"

	class Disableprimaryondown:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		CONTENT = "CONTENT"
		ADDRESS = "ADDRESS"

	class Advancedepa:
		ON = "ON"
		OFF = "OFF"

	class Somethod:
		CONNECTION = "CONNECTION"
		DYNAMICCONNECTION = "DYNAMICCONNECTION"
		BANDWIDTH = "BANDWIDTH"
		HEALTH = "HEALTH"
		NONE = "NONE"

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		ICA_REQUEST = "ICA_REQUEST"
		OTHERTCP_REQUEST = "OTHERTCP_REQUEST"

	class Sopersistence:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Redirect:
		CACHE = "CACHE"
		POLICY = "POLICY"
		ORIGIN = "ORIGIN"

	class Doublehop:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

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

class vpnvserver_response(base_response) :
	def __init__(self, length=1) :
		self.vpnvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnvserver = [vpnvserver() for _ in range(length)]

