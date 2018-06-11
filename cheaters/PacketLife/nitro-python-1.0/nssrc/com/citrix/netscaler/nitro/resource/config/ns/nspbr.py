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

class nspbr(base_resource) :
	""" Configuration for Policy Based Routing(PBR) entry resource. """
	def __init__(self) :
		self._name = ""
		self._action = ""
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
		self._nexthop = False
		self._nexthopval = ""
		self._iptunnel = False
		self._iptunnelname = ""
		self._srcmac = ""
		self._protocol = ""
		self._protocolnumber = 0
		self._vlan = 0
		self._vxlan = 0
		self._Interface = ""
		self._priority = 0
		self._msr = ""
		self._monitor = ""
		self._state = ""
		self._detail = False
		self._hits = 0
		self._kernelstate = ""
		self._curstate = 0
		self._totalprobes = 0
		self._totalfailedprobes = 0
		self._failedprobes = 0
		self._monstatcode = 0
		self._monstatparam1 = 0
		self._monstatparam2 = 0
		self._monstatparam3 = 0
		self._data = False
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the PBR. Must begin with an ASCII alphabetic or underscore \(_\) character, and must contain only ASCII alphanumeric, underscore, hash \(\#\), period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen \(-\) characters. Can be changed after the PBR is created.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the PBR. Must begin with an ASCII alphabetic or underscore \(_\) character, and must contain only ASCII alphanumeric, underscore, hash \(\#\), period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen \(-\) characters. Can be changed after the PBR is created.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def action(self) :
		ur"""Action to perform on the outgoing IPv4 packets that match the PBR.
		Available settings function as follows:
		* ALLOW - The NetScaler appliance sends the packet to the designated next-hop router.
		* DENY - The NetScaler appliance applies the routing table for normal destination-based routing.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		ur"""Action to perform on the outgoing IPv4 packets that match the PBR.
		Available settings function as follows:
		* ALLOW - The NetScaler appliance sends the packet to the designated next-hop router.
		* DENY - The NetScaler appliance applies the routing table for normal destination-based routing.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._action = action
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
		ur"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		ur"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
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
		ur"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._srcipval
		except Exception as e:
			raise e

	@srcipval.setter
	def srcipval(self, srcipval) :
		ur"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			self._srcipval = srcipval
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		ur"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@srcport.setter
	def srcport(self, srcport) :
		ur"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._srcport = srcport
		except Exception as e:
			raise e

	@property
	def srcportop(self) :
		ur"""Logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcportop
		except Exception as e:
			raise e

	@srcportop.setter
	def srcportop(self, srcportop) :
		ur"""Logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcportop = srcportop
		except Exception as e:
			raise e

	@property
	def srcportval(self) :
		ur"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535.
		"""
		try :
			return self._srcportval
		except Exception as e:
			raise e

	@srcportval.setter
	def srcportval(self, srcportval) :
		ur"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535
		"""
		try :
			self._srcportval = srcportval
		except Exception as e:
			raise e

	@property
	def destip(self) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet.  In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet.  In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def destipop(self) :
		ur"""Logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destipop
		except Exception as e:
			raise e

	@destipop.setter
	def destipop(self, destipop) :
		ur"""Logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destipop = destipop
		except Exception as e:
			raise e

	@property
	def destipval(self) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			return self._destipval
		except Exception as e:
			raise e

	@destipval.setter
	def destipval(self, destipval) :
		ur"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [10.102.29.30-10.102.29.189].
		"""
		try :
			self._destipval = destipval
		except Exception as e:
			raise e

	@property
	def destport(self) :
		ur"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		ur"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def destportop(self) :
		ur"""Logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destportop
		except Exception as e:
			raise e

	@destportop.setter
	def destportop(self, destportop) :
		ur"""Logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destportop = destportop
		except Exception as e:
			raise e

	@property
	def destportval(self) :
		ur"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535.
		"""
		try :
			return self._destportval
		except Exception as e:
			raise e

	@destportval.setter
	def destportval(self, destportval) :
		ur"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen and enclose within brackets. For example: [40-90].
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535
		"""
		try :
			self._destportval = destportval
		except Exception as e:
			raise e

	@property
	def nexthop(self) :
		ur"""IP address of the next hop router or the name of the link load balancing virtual server to which to send matching packets if action is set to ALLOW.
		If you specify a link load balancing (LLB) virtual server, which can provide a backup if a next hop link fails, first make sure that the next hops bound to the LLB virtual server are actually next hops that are directly connected to the NetScaler appliance. Otherwise, the NetScaler throws an error when you attempt to create the PBR.
		"""
		try :
			return self._nexthop
		except Exception as e:
			raise e

	@nexthop.setter
	def nexthop(self, nexthop) :
		ur"""IP address of the next hop router or the name of the link load balancing virtual server to which to send matching packets if action is set to ALLOW.
		If you specify a link load balancing (LLB) virtual server, which can provide a backup if a next hop link fails, first make sure that the next hops bound to the LLB virtual server are actually next hops that are directly connected to the NetScaler appliance. Otherwise, the NetScaler throws an error when you attempt to create the PBR.
		"""
		try :
			self._nexthop = nexthop
		except Exception as e:
			raise e

	@property
	def nexthopval(self) :
		ur"""The Next Hop IP address or gateway name.
		"""
		try :
			return self._nexthopval
		except Exception as e:
			raise e

	@nexthopval.setter
	def nexthopval(self, nexthopval) :
		ur"""The Next Hop IP address or gateway name.
		"""
		try :
			self._nexthopval = nexthopval
		except Exception as e:
			raise e

	@property
	def iptunnel(self) :
		ur"""The Tunnel name.
		"""
		try :
			return self._iptunnel
		except Exception as e:
			raise e

	@iptunnel.setter
	def iptunnel(self, iptunnel) :
		ur"""The Tunnel name.
		"""
		try :
			self._iptunnel = iptunnel
		except Exception as e:
			raise e

	@property
	def iptunnelname(self) :
		ur"""The iptunnel name where packets need to be forwarded upon.
		"""
		try :
			return self._iptunnelname
		except Exception as e:
			raise e

	@iptunnelname.setter
	def iptunnelname(self, iptunnelname) :
		ur"""The iptunnel name where packets need to be forwarded upon.
		"""
		try :
			self._iptunnelname = iptunnelname
		except Exception as e:
			raise e

	@property
	def srcmac(self) :
		ur"""MAC address to match against the source MAC address of an outgoing IPv4 packet.
		"""
		try :
			return self._srcmac
		except Exception as e:
			raise e

	@srcmac.setter
	def srcmac(self, srcmac) :
		ur"""MAC address to match against the source MAC address of an outgoing IPv4 packet.
		"""
		try :
			self._srcmac = srcmac
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		ur"""Protocol, identified by protocol name, to match against the protocol of an outgoing IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		ur"""Protocol, identified by protocol name, to match against the protocol of an outgoing IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def protocolnumber(self) :
		ur"""Protocol, identified by protocol number, to match against the protocol of an outgoing IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._protocolnumber
		except Exception as e:
			raise e

	@protocolnumber.setter
	def protocolnumber(self, protocolnumber) :
		ur"""Protocol, identified by protocol number, to match against the protocol of an outgoing IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._protocolnumber = protocolnumber
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		ur"""ID of the VLAN. The NetScaler appliance compares the PBR only to the outgoing packets on the specified VLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		ur"""ID of the VLAN. The NetScaler appliance compares the PBR only to the outgoing packets on the specified VLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		ur"""ID of the VXLAN. The NetScaler appliance compares the PBR only to the outgoing packets on the specified VXLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		ur"""ID of the VXLAN. The NetScaler appliance compares the PBR only to the outgoing packets on the specified VXLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def Interface(self) :
		ur"""ID of an interface. The NetScaler appliance compares the PBR only to the outgoing packets on the specified interface. If you do not specify any value, the appliance compares the PBR to the outgoing packets on all interfaces.
		"""
		try :
			return self._Interface
		except Exception as e:
			raise e

	@Interface.setter
	def Interface(self, Interface) :
		ur"""ID of an interface. The NetScaler appliance compares the PBR only to the outgoing packets on the specified interface. If you do not specify any value, the appliance compares the PBR to the outgoing packets on all interfaces.
		"""
		try :
			self._Interface = Interface
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Priority of the PBR, which determines the order in which it is evaluated relative to the other PBRs. If you do not specify priorities while creating PBRs, the PBRs are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  81920.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Priority of the PBR, which determines the order in which it is evaluated relative to the other PBRs. If you do not specify priorities while creating PBRs, the PBRs are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  81920
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def msr(self) :
		ur"""Monitor the route specified byte Next Hop parameter. This parameter is not applicable if you specify a link load balancing (LLB) virtual server name with the Next Hop parameter.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._msr
		except Exception as e:
			raise e

	@msr.setter
	def msr(self, msr) :
		ur"""Monitor the route specified byte Next Hop parameter. This parameter is not applicable if you specify a link load balancing (LLB) virtual server name with the Next Hop parameter.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._msr = msr
		except Exception as e:
			raise e

	@property
	def monitor(self) :
		ur"""The name of the monitor.(Can be only of type ping or ARP ).<br/>Minimum length =  1.
		"""
		try :
			return self._monitor
		except Exception as e:
			raise e

	@monitor.setter
	def monitor(self, monitor) :
		ur"""The name of the monitor.(Can be only of type ping or ARP ).<br/>Minimum length =  1
		"""
		try :
			self._monitor = monitor
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Enable or disable the PBR. After you apply the PBRs, the NetScaler appliance compares outgoing packets to the enabled PBRs.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Enable or disable the PBR. After you apply the PBRs, the NetScaler appliance compares outgoing packets to the enabled PBRs.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def detail(self) :
		ur"""To get a detailed view.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		ur"""To get a detailed view.
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The hits of this PBR.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def kernelstate(self) :
		ur"""The commit status of the PBR.<br/>Default value: NOTAPPLIED<br/>Possible values = APPLIED, NOTAPPLIED, RE-APPLY, SFAPPLIED, SFNOTAPPLIED, SFAPPLIED61, SFNOTAPPLIED61.
		"""
		try :
			return self._kernelstate
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		ur"""If this route is UP/DOWN.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def totalprobes(self) :
		ur"""The total number of probes sent.
		"""
		try :
			return self._totalprobes
		except Exception as e:
			raise e

	@property
	def totalfailedprobes(self) :
		ur"""The total number of failed probes.
		"""
		try :
			return self._totalfailedprobes
		except Exception as e:
			raise e

	@property
	def failedprobes(self) :
		ur"""Number of the current failed monitoring probes.
		"""
		try :
			return self._failedprobes
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		ur"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		ur"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		ur"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		ur"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def data(self) :
		ur"""Internal data of this route.
		"""
		try :
			return self._data
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nspbr_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nspbr
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
		ur""" Use this API to add nspbr.
		"""
		try :
			if type(resource) is not list :
				addresource = nspbr()
				addresource.name = resource.name
				addresource.action = resource.action
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
				addresource.nexthop = resource.nexthop
				addresource.nexthopval = resource.nexthopval
				addresource.iptunnel = resource.iptunnel
				addresource.iptunnelname = resource.iptunnelname
				addresource.srcmac = resource.srcmac
				addresource.protocol = resource.protocol
				addresource.protocolnumber = resource.protocolnumber
				addresource.vlan = resource.vlan
				addresource.vxlan = resource.vxlan
				addresource.Interface = resource.Interface
				addresource.priority = resource.priority
				addresource.msr = resource.msr
				addresource.monitor = resource.monitor
				addresource.state = resource.state
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nspbr() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].action = resource[i].action
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
						addresources[i].nexthop = resource[i].nexthop
						addresources[i].nexthopval = resource[i].nexthopval
						addresources[i].iptunnel = resource[i].iptunnel
						addresources[i].iptunnelname = resource[i].iptunnelname
						addresources[i].srcmac = resource[i].srcmac
						addresources[i].protocol = resource[i].protocol
						addresources[i].protocolnumber = resource[i].protocolnumber
						addresources[i].vlan = resource[i].vlan
						addresources[i].vxlan = resource[i].vxlan
						addresources[i].Interface = resource[i].Interface
						addresources[i].priority = resource[i].priority
						addresources[i].msr = resource[i].msr
						addresources[i].monitor = resource[i].monitor
						addresources[i].state = resource[i].state
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nspbr.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nspbr()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nspbr.
		"""
		try :
			if type(resource) is not list :
				updateresource = nspbr()
				updateresource.name = resource.name
				updateresource.action = resource.action
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
				updateresource.nexthop = resource.nexthop
				updateresource.nexthopval = resource.nexthopval
				updateresource.iptunnel = resource.iptunnel
				updateresource.iptunnelname = resource.iptunnelname
				updateresource.srcmac = resource.srcmac
				updateresource.protocol = resource.protocol
				updateresource.protocolnumber = resource.protocolnumber
				updateresource.vlan = resource.vlan
				updateresource.vxlan = resource.vxlan
				updateresource.Interface = resource.Interface
				updateresource.priority = resource.priority
				updateresource.msr = resource.msr
				updateresource.monitor = resource.monitor
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nspbr() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].action = resource[i].action
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
						updateresources[i].nexthop = resource[i].nexthop
						updateresources[i].nexthopval = resource[i].nexthopval
						updateresources[i].iptunnel = resource[i].iptunnel
						updateresources[i].iptunnelname = resource[i].iptunnelname
						updateresources[i].srcmac = resource[i].srcmac
						updateresources[i].protocol = resource[i].protocol
						updateresources[i].protocolnumber = resource[i].protocolnumber
						updateresources[i].vlan = resource[i].vlan
						updateresources[i].vxlan = resource[i].vxlan
						updateresources[i].Interface = resource[i].Interface
						updateresources[i].priority = resource[i].priority
						updateresources[i].msr = resource[i].msr
						updateresources[i].monitor = resource[i].monitor
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nspbr resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nspbr()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable nspbr.
		"""
		try :
			if type(resource) is not list :
				enableresource = nspbr()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable nspbr.
		"""
		try :
			if type(resource) is not list :
				disableresource = nspbr()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nspbr resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nspbr()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nspbr()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nspbr() for _ in range(len(name))]
							obj = [nspbr() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nspbr()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the nspbr resources that are configured on netscaler.
	# This uses nspbr_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nspbr()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nspbr resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nspbr()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nspbr resources configured on NetScaler.
		"""
		try :
			obj = nspbr()
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
		ur""" Use this API to count filtered the set of nspbr resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nspbr()
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

	class Msr:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

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

	class Destportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Action:
		ALLOW = "ALLOW"
		DENY = "DENY"

class nspbr_response(base_response) :
	def __init__(self, length=1) :
		self.nspbr = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nspbr = [nspbr() for _ in range(length)]

