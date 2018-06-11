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

class nsacl(base_resource) :
	""" Configuration for ACL entry resource. """
	def __init__(self) :
		self._aclname = ""
		self._aclaction = ""
		self._td = 0
		self._srcip = False
		self._srcipop = ""
		self._srcipval = ""
		self._srcport = False
		self._srcportop = ""
		self._srcportval = ""
		self._destip = False
		self._destipop = ""
		self._destipval = ""
		self._destport = False
		self._destportop = ""
		self._destportval = ""
		self._ttl = 0
		self._srcmac = ""
		self._protocol = ""
		self._protocolnumber = 0
		self._vlan = 0
		self._vxlan = 0
		self._Interface = ""
		self._established = False
		self._icmptype = 0
		self._icmpcode = 0
		self._priority = 0
		self._state = ""
		self._logstate = ""
		self._ratelimit = 0
		self._newname = ""
		self._hits = 0
		self._kernelstate = ""
		self.___count = 0

	@property
	def aclname(self) :
		ur"""Name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the extended ACL rule is created.<br/>Minimum length =  1.
		"""
		try :
			return self._aclname
		except Exception as e:
			raise e

	@aclname.setter
	def aclname(self, aclname) :
		ur"""Name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the extended ACL rule is created.<br/>Minimum length =  1
		"""
		try :
			self._aclname = aclname
		except Exception as e:
			raise e

	@property
	def aclaction(self) :
		ur"""Action to perform on incoming IPv4 packets that match the extended ACL rule.
		Available settings function as follows:
		* ALLOW - The NetScaler appliance processes the packet.
		* BRIDGE - The NetScaler appliance bridges the packet to the destination without processing it.
		* DENY - The NetScaler appliance drops the packet.<br/>Possible values = BRIDGE, DENY, ALLOW.
		"""
		try :
			return self._aclaction
		except Exception as e:
			raise e

	@aclaction.setter
	def aclaction(self, aclaction) :
		ur"""Action to perform on incoming IPv4 packets that match the extended ACL rule.
		Available settings function as follows:
		* ALLOW - The NetScaler appliance processes the packet.
		* BRIDGE - The NetScaler appliance bridges the packet to the destination without processing it.
		* DENY - The NetScaler appliance drops the packet.<br/>Possible values = BRIDGE, DENY, ALLOW
		"""
		try :
			self._aclaction = aclaction
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
	def srcip(self) :
		ur"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		ur"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def srcipop(self) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcipop
		except Exception as e:
			raise e

	@srcipop.setter
	def srcipop(self, srcipop) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcipop = srcipop
		except Exception as e:
			raise e

	@property
	def srcipval(self) :
		ur"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._srcipval
		except Exception as e:
			raise e

	@srcipval.setter
	def srcipval(self, srcipval) :
		ur"""IP address or range of IP addresses to match against the source IP address of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			self._srcipval = srcipval
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		ur"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@srcport.setter
	def srcport(self, srcport) :
		ur"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		"""
		try :
			self._srcport = srcport
		except Exception as e:
			raise e

	@property
	def srcportop(self) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcportop
		except Exception as e:
			raise e

	@srcportop.setter
	def srcportop(self, srcportop) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcportop = srcportop
		except Exception as e:
			raise e

	@property
	def srcportval(self) :
		ur"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].<br/>Maximum length =  65535.
		"""
		try :
			return self._srcportval
		except Exception as e:
			raise e

	@srcportval.setter
	def srcportval(self, srcportval) :
		ur"""Port number or range of port numbers to match against the source port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].<br/>Maximum length =  65535
		"""
		try :
			self._srcportval = srcportval
		except Exception as e:
			raise e

	@property
	def destip(self) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def destipop(self) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destipop
		except Exception as e:
			raise e

	@destipop.setter
	def destipop(self, destipop) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destipop = destipop
		except Exception as e:
			raise e

	@property
	def destipval(self) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._destipval
		except Exception as e:
			raise e

	@destipval.setter
	def destipval(self, destipval) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an incoming IPv4 packet.  In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			self._destipval = destipval
		except Exception as e:
			raise e

	@property
	def destport(self) :
		ur"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		ur"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def destportop(self) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destportop
		except Exception as e:
			raise e

	@destportop.setter
	def destportop(self, destportop) :
		ur"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destportop = destportop
		except Exception as e:
			raise e

	@property
	def destportval(self) :
		ur"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535.
		"""
		try :
			return self._destportval
		except Exception as e:
			raise e

	@destportval.setter
	def destportval(self, destportval) :
		ur"""Port number or range of port numbers to match against the destination port number of an incoming IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535
		"""
		try :
			self._destportval = destportval
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		ur"""Number of seconds, in multiples of four, after which the extended ACL rule expires. If you do not want the extended ACL rule to expire, do not specify a TTL value.<br/>Minimum length =  1<br/>Maximum length =  0x7FFFFFFF.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		ur"""Number of seconds, in multiples of four, after which the extended ACL rule expires. If you do not want the extended ACL rule to expire, do not specify a TTL value.<br/>Minimum length =  1<br/>Maximum length =  0x7FFFFFFF
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def srcmac(self) :
		ur"""MAC address to match against the source MAC address of an incoming IPv4 packet.
		"""
		try :
			return self._srcmac
		except Exception as e:
			raise e

	@srcmac.setter
	def srcmac(self, srcmac) :
		ur"""MAC address to match against the source MAC address of an incoming IPv4 packet.
		"""
		try :
			self._srcmac = srcmac
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		ur"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		ur"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def protocolnumber(self) :
		ur"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._protocolnumber
		except Exception as e:
			raise e

	@protocolnumber.setter
	def protocolnumber(self, protocolnumber) :
		ur"""Protocol to match against the protocol of an incoming IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._protocolnumber = protocolnumber
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		ur"""ID of the VLAN. The NetScaler appliance applies the ACL rule only to the incoming packets of the specified VLAN. If you do not specify a VLAN ID, the appliance applies the ACL rule to the incoming packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		ur"""ID of the VLAN. The NetScaler appliance applies the ACL rule only to the incoming packets of the specified VLAN. If you do not specify a VLAN ID, the appliance applies the ACL rule to the incoming packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		ur"""ID of the VXLAN. The NetScaler appliance applies the ACL rule only to the incoming packets of the specified VXLAN. If you do not specify a VXLAN ID, the appliance applies the ACL rule to the incoming packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		ur"""ID of the VXLAN. The NetScaler appliance applies the ACL rule only to the incoming packets of the specified VXLAN. If you do not specify a VXLAN ID, the appliance applies the ACL rule to the incoming packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def Interface(self) :
		ur"""ID of an interface. The NetScaler appliance applies the ACL rule only to the incoming packets from the specified interface. If you do not specify any value, the appliance applies the ACL rule to the incoming packets of all interfaces.
		"""
		try :
			return self._Interface
		except Exception as e:
			raise e

	@Interface.setter
	def Interface(self, Interface) :
		ur"""ID of an interface. The NetScaler appliance applies the ACL rule only to the incoming packets from the specified interface. If you do not specify any value, the appliance applies the ACL rule to the incoming packets of all interfaces.
		"""
		try :
			self._Interface = Interface
		except Exception as e:
			raise e

	@property
	def established(self) :
		ur"""Allow only incoming TCP packets that have the ACK or RST bit set, if the action set for the ACL rule is ALLOW and these packets match the other conditions in the ACL rule.
		"""
		try :
			return self._established
		except Exception as e:
			raise e

	@established.setter
	def established(self, established) :
		ur"""Allow only incoming TCP packets that have the ACK or RST bit set, if the action set for the ACL rule is ALLOW and these packets match the other conditions in the ACL rule.
		"""
		try :
			self._established = established
		except Exception as e:
			raise e

	@property
	def icmptype(self) :
		ur"""ICMP Message type to match against the message type of an incoming ICMP packet. For example, to block DESTINATION UNREACHABLE messages, you must specify 3 as the ICMP type.
		Note: This parameter can be specified only for the ICMP protocol.<br/>Maximum length =  65536.
		"""
		try :
			return self._icmptype
		except Exception as e:
			raise e

	@icmptype.setter
	def icmptype(self, icmptype) :
		ur"""ICMP Message type to match against the message type of an incoming ICMP packet. For example, to block DESTINATION UNREACHABLE messages, you must specify 3 as the ICMP type.
		Note: This parameter can be specified only for the ICMP protocol.<br/>Maximum length =  65536
		"""
		try :
			self._icmptype = icmptype
		except Exception as e:
			raise e

	@property
	def icmpcode(self) :
		ur"""Code of a particular ICMP message type to match against the ICMP code of an incoming ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE messages, specify 3 as the ICMP type and 1 as the ICMP code.
		If you set this parameter, you must set the ICMP Type parameter.<br/>Maximum length =  65536.
		"""
		try :
			return self._icmpcode
		except Exception as e:
			raise e

	@icmpcode.setter
	def icmpcode(self, icmpcode) :
		ur"""Code of a particular ICMP message type to match against the ICMP code of an incoming ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE messages, specify 3 as the ICMP type and 1 as the ICMP code.
		If you set this parameter, you must set the ICMP Type parameter.<br/>Maximum length =  65536
		"""
		try :
			self._icmpcode = icmpcode
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Priority for the extended ACL rule that determines the order in which it is evaluated relative to the other extended ACL rules. If you do not specify priorities while creating extended ACL rules, the ACL rules are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  100000.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Priority for the extended ACL rule that determines the order in which it is evaluated relative to the other extended ACL rules. If you do not specify priorities while creating extended ACL rules, the ACL rules are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  100000
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Enable or disable the extended ACL rule. After you apply the extended ACL rules, the NetScaler appliance compares incoming packets against the enabled extended ACL rules.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Enable or disable the extended ACL rule. After you apply the extended ACL rules, the NetScaler appliance compares incoming packets against the enabled extended ACL rules.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def logstate(self) :
		ur"""Enable or disable logging of events related to the extended ACL rule. The log messages are stored in the configured syslog or auditlog server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logstate
		except Exception as e:
			raise e

	@logstate.setter
	def logstate(self, logstate) :
		ur"""Enable or disable logging of events related to the extended ACL rule. The log messages are stored in the configured syslog or auditlog server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logstate = logstate
		except Exception as e:
			raise e

	@property
	def ratelimit(self) :
		ur"""Maximum number of log messages to be generated per second. If you set this parameter, you must enable the Log State parameter.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  10000.
		"""
		try :
			return self._ratelimit
		except Exception as e:
			raise e

	@ratelimit.setter
	def ratelimit(self, ratelimit) :
		ur"""Maximum number of log messages to be generated per second. If you set this parameter, you must enable the Log State parameter.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  10000
		"""
		try :
			self._ratelimit = ratelimit
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The hits of this ACL.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def kernelstate(self) :
		ur"""The commit status of the ACL.<br/>Default value: NOTAPPLIED<br/>Possible values = APPLIED, NOTAPPLIED, RE-APPLY, SFAPPLIED, SFNOTAPPLIED, SFAPPLIED61, SFNOTAPPLIED61.
		"""
		try :
			return self._kernelstate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsacl_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsacl
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.aclname is not None :
				return str(self.aclname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add nsacl.
		"""
		try :
			if type(resource) is not list :
				addresource = nsacl()
				addresource.aclname = resource.aclname
				addresource.aclaction = resource.aclaction
				addresource.td = resource.td
				addresource.srcip = resource.srcip
				addresource.srcipop = resource.srcipop
				addresource.srcipval = resource.srcipval
				addresource.srcport = resource.srcport
				addresource.srcportop = resource.srcportop
				addresource.srcportval = resource.srcportval
				addresource.destip = resource.destip
				addresource.destipop = resource.destipop
				addresource.destipval = resource.destipval
				addresource.destport = resource.destport
				addresource.destportop = resource.destportop
				addresource.destportval = resource.destportval
				addresource.ttl = resource.ttl
				addresource.srcmac = resource.srcmac
				addresource.protocol = resource.protocol
				addresource.protocolnumber = resource.protocolnumber
				addresource.vlan = resource.vlan
				addresource.vxlan = resource.vxlan
				addresource.Interface = resource.Interface
				addresource.established = resource.established
				addresource.icmptype = resource.icmptype
				addresource.icmpcode = resource.icmpcode
				addresource.priority = resource.priority
				addresource.state = resource.state
				addresource.logstate = resource.logstate
				addresource.ratelimit = resource.ratelimit
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsacl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].aclname = resource[i].aclname
						addresources[i].aclaction = resource[i].aclaction
						addresources[i].td = resource[i].td
						addresources[i].srcip = resource[i].srcip
						addresources[i].srcipop = resource[i].srcipop
						addresources[i].srcipval = resource[i].srcipval
						addresources[i].srcport = resource[i].srcport
						addresources[i].srcportop = resource[i].srcportop
						addresources[i].srcportval = resource[i].srcportval
						addresources[i].destip = resource[i].destip
						addresources[i].destipop = resource[i].destipop
						addresources[i].destipval = resource[i].destipval
						addresources[i].destport = resource[i].destport
						addresources[i].destportop = resource[i].destportop
						addresources[i].destportval = resource[i].destportval
						addresources[i].ttl = resource[i].ttl
						addresources[i].srcmac = resource[i].srcmac
						addresources[i].protocol = resource[i].protocol
						addresources[i].protocolnumber = resource[i].protocolnumber
						addresources[i].vlan = resource[i].vlan
						addresources[i].vxlan = resource[i].vxlan
						addresources[i].Interface = resource[i].Interface
						addresources[i].established = resource[i].established
						addresources[i].icmptype = resource[i].icmptype
						addresources[i].icmpcode = resource[i].icmpcode
						addresources[i].priority = resource[i].priority
						addresources[i].state = resource[i].state
						addresources[i].logstate = resource[i].logstate
						addresources[i].ratelimit = resource[i].ratelimit
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nsacl.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsacl()
				if type(resource) !=  type(deleteresource):
					deleteresource.aclname = resource
				else :
					deleteresource.aclname = resource.aclname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i].aclname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nsacl.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsacl()
				updateresource.aclname = resource.aclname
				updateresource.aclaction = resource.aclaction
				updateresource.srcip = resource.srcip
				updateresource.srcipop = resource.srcipop
				updateresource.srcipval = resource.srcipval
				updateresource.srcport = resource.srcport
				updateresource.srcportop = resource.srcportop
				updateresource.srcportval = resource.srcportval
				updateresource.destip = resource.destip
				updateresource.destipop = resource.destipop
				updateresource.destipval = resource.destipval
				updateresource.destport = resource.destport
				updateresource.destportop = resource.destportop
				updateresource.destportval = resource.destportval
				updateresource.srcmac = resource.srcmac
				updateresource.protocol = resource.protocol
				updateresource.protocolnumber = resource.protocolnumber
				updateresource.icmptype = resource.icmptype
				updateresource.icmpcode = resource.icmpcode
				updateresource.vlan = resource.vlan
				updateresource.vxlan = resource.vxlan
				updateresource.Interface = resource.Interface
				updateresource.priority = resource.priority
				updateresource.logstate = resource.logstate
				updateresource.ratelimit = resource.ratelimit
				updateresource.established = resource.established
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsacl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].aclname = resource[i].aclname
						updateresources[i].aclaction = resource[i].aclaction
						updateresources[i].srcip = resource[i].srcip
						updateresources[i].srcipop = resource[i].srcipop
						updateresources[i].srcipval = resource[i].srcipval
						updateresources[i].srcport = resource[i].srcport
						updateresources[i].srcportop = resource[i].srcportop
						updateresources[i].srcportval = resource[i].srcportval
						updateresources[i].destip = resource[i].destip
						updateresources[i].destipop = resource[i].destipop
						updateresources[i].destipval = resource[i].destipval
						updateresources[i].destport = resource[i].destport
						updateresources[i].destportop = resource[i].destportop
						updateresources[i].destportval = resource[i].destportval
						updateresources[i].srcmac = resource[i].srcmac
						updateresources[i].protocol = resource[i].protocol
						updateresources[i].protocolnumber = resource[i].protocolnumber
						updateresources[i].icmptype = resource[i].icmptype
						updateresources[i].icmpcode = resource[i].icmpcode
						updateresources[i].vlan = resource[i].vlan
						updateresources[i].vxlan = resource[i].vxlan
						updateresources[i].Interface = resource[i].Interface
						updateresources[i].priority = resource[i].priority
						updateresources[i].logstate = resource[i].logstate
						updateresources[i].ratelimit = resource[i].ratelimit
						updateresources[i].established = resource[i].established
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nsacl resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsacl()
				if type(resource) !=  type(unsetresource):
					unsetresource.aclname = resource
				else :
					unsetresource.aclname = resource.aclname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].aclname = resource[i].aclname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable nsacl.
		"""
		try :
			if type(resource) is not list :
				enableresource = nsacl()
				if type(resource) !=  type(enableresource):
					enableresource.aclname = resource
				else :
					enableresource.aclname = resource.aclname
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].aclname = resource[i].aclname
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable nsacl.
		"""
		try :
			if type(resource) is not list :
				disableresource = nsacl()
				if type(resource) !=  type(disableresource):
					disableresource.aclname = resource
				else :
					disableresource.aclname = resource.aclname
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ nsacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].aclname = resource[i].aclname
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_aclname) :
		ur""" Use this API to rename a nsacl resource.
		"""
		try :
			renameresource = nsacl()
			if type(resource) == cls :
				renameresource.aclname = resource.aclname
			else :
				renameresource.aclname = resource
			return renameresource.rename_resource(client,new_aclname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsacl resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsacl()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nsacl()
						obj.aclname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nsacl() for _ in range(len(name))]
							obj = [nsacl() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nsacl()
								obj[i].aclname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nsacl resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsacl()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nsacl resources configured on NetScaler.
		"""
		try :
			obj = nsacl()
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
		ur""" Use this API to count filtered the set of nsacl resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsacl()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Protocol:
		ICMP = "ICMP"
		IGMP = "IGMP"
		TCP = "TCP"
		EGP = "EGP"
		IGP = "IGP"
		ARGUS = "ARGUS"
		UDP = "UDP"
		RDP = "RDP"
		RSVP = "RSVP"
		EIGRP = "EIGRP"
		L2TP = "L2TP"
		ISIS = "ISIS"

	class Destipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Kernelstate:
		APPLIED = "APPLIED"
		NOTAPPLIED = "NOTAPPLIED"
		RE_APPLY = "RE-APPLY"
		SFAPPLIED = "SFAPPLIED"
		SFNOTAPPLIED = "SFNOTAPPLIED"
		SFAPPLIED61 = "SFAPPLIED61"
		SFNOTAPPLIED61 = "SFNOTAPPLIED61"

	class Aclaction:
		BRIDGE = "BRIDGE"
		DENY = "DENY"
		ALLOW = "ALLOW"

	class Srcportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Srcipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Logstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Destportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

class nsacl_response(base_response) :
	def __init__(self, length=1) :
		self.nsacl = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsacl = [nsacl() for _ in range(length)]

