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

class channel(base_resource) :
	""" Configuration for channel resource. """
	def __init__(self) :
		self._id = ""
		self._ifnum = []
		self._state = ""
		self._mode = ""
		self._conndistr = ""
		self._macdistr = ""
		self._lamac = ""
		self._speed = ""
		self._flowctl = ""
		self._hamonitor = ""
		self._tagall = ""
		self._trunk = ""
		self._ifalias = ""
		self._throughput = 0
		self._bandwidthhigh = 0
		self._bandwidthnormal = 0
		self._mtu = 0
		self._lrminthroughput = 0
		self._linkredundancy = ""
		self._devicename = ""
		self._unit = 0
		self._description = ""
		self._flags = 0
		self._actualmtu = 0
		self._vlan = 0
		self._mac = ""
		self._uptime = 0
		self._downtime = 0
		self._reqmedia = ""
		self._reqspeed = ""
		self._reqduplex = ""
		self._reqflowcontrol = ""
		self._media = ""
		self._actspeed = ""
		self._duplex = ""
		self._actflowctl = ""
		self._lamode = ""
		self._autoneg = 0
		self._autonegresult = 0
		self._tagged = 0
		self._taggedany = 0
		self._taggedautolearn = 0
		self._hangdetect = 0
		self._hangreset = 0
		self._linkstate = 0
		self._intfstate = 0
		self._rxpackets = 0
		self._rxbytes = 0
		self._rxerrors = 0
		self._rxdrops = 0
		self._txpackets = 0
		self._txbytes = 0
		self._txerrors = 0
		self._txdrops = 0
		self._indisc = 0
		self._outdisc = 0
		self._fctls = 0
		self._hangs = 0
		self._stsstalls = 0
		self._txstalls = 0
		self._rxstalls = 0
		self._bdgmuted = 0
		self._vmac = ""
		self._vmac6 = ""
		self._reqthroughput = 0
		self._actthroughput = 0
		self._backplane = ""
		self._cleartime = 0
		self._lacpmode = ""
		self._lacptimeout = ""
		self._lacpactorpriority = 0
		self._lacpactorportno = 0
		self._lacppartnerstate = ""
		self._lacppartnertimeout = ""
		self._lacppartneraggregation = ""
		self._lacppartnerinsync = ""
		self._lacppartnercollecting = ""
		self._lacppartnerdistributing = ""
		self._lacppartnerdefaulted = ""
		self._lacppartnerexpired = ""
		self._lacppartnerpriority = 0
		self._lacppartnersystemmac = ""
		self._lacppartnersystempriority = 0
		self._lacppartnerportno = 0
		self._lacppartnerkey = 0
		self._lacpactoraggregation = ""
		self._lacpactorinsync = ""
		self._lacpactorcollecting = ""
		self._lacpactordistributing = ""
		self._lacpportmuxstate = ""
		self._lacpportrxstat = ""
		self._lacpportselectstate = ""
		self._lldpmode = ""
		self.___count = 0

	@property
	def id(self) :
		ur"""ID for the LA channel or cluster LA channel to be created. Specify an LA channel in LA/x notation, where x can range from 1 to 8 or cluster LA channel in CLA/x notation, where x can range from 1 to 4. Cannot be changed after the LA channel is created.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""ID for the LA channel or cluster LA channel to be created. Specify an LA channel in LA/x notation, where x can range from 1 to 8 or cluster LA channel in CLA/x notation, where x can range from 1 to 4. Cannot be changed after the LA channel is created.
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		ur"""Interfaces to be bound to the LA channel of a NetScaler appliance or to the LA channel of a cluster configuration.
		For an LA channel of a NetScaler appliance, specify an interface in C/U notation (for example, 1/3). 
		For an LA channel of a cluster configuration, specify an interface in N/C/U notation (for example, 2/1/3).
		where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		U is a unique integer for representing an interface in a particular port group.
		N is the ID of the node to which an interface belongs in a cluster configuration.
		Use spaces to separate multiple entries.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		ur"""Interfaces to be bound to the LA channel of a NetScaler appliance or to the LA channel of a cluster configuration.
		For an LA channel of a NetScaler appliance, specify an interface in C/U notation (for example, 1/3). 
		For an LA channel of a cluster configuration, specify an interface in N/C/U notation (for example, 2/1/3).
		where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		U is a unique integer for representing an interface in a particular port group.
		N is the ID of the node to which an interface belongs in a cluster configuration.
		Use spaces to separate multiple entries.
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Enable or disable the LA channel.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Enable or disable the LA channel.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def mode(self) :
		ur"""The initital mode for the LA channel.<br/>Possible values = MANUAL, AUTO.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		ur"""The initital mode for the LA channel.<br/>Possible values = MANUAL, AUTO
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	@property
	def conndistr(self) :
		ur"""The 'connection' distribution mode for the LA channel.<br/>Possible values = DISABLED, ENABLED.
		"""
		try :
			return self._conndistr
		except Exception as e:
			raise e

	@conndistr.setter
	def conndistr(self, conndistr) :
		ur"""The 'connection' distribution mode for the LA channel.<br/>Possible values = DISABLED, ENABLED
		"""
		try :
			self._conndistr = conndistr
		except Exception as e:
			raise e

	@property
	def macdistr(self) :
		ur"""The  'MAC' distribution mode for the LA channel.<br/>Possible values = SOURCE, DESTINATION, BOTH.
		"""
		try :
			return self._macdistr
		except Exception as e:
			raise e

	@macdistr.setter
	def macdistr(self, macdistr) :
		ur"""The  'MAC' distribution mode for the LA channel.<br/>Possible values = SOURCE, DESTINATION, BOTH
		"""
		try :
			self._macdistr = macdistr
		except Exception as e:
			raise e

	@property
	def lamac(self) :
		ur"""Specifies a MAC address for the LA channels configured in NetScaler virtual appliances (VPX). This MAC address is persistent after each reboot. If you don't specify this parameter, a MAC address is generated randomly for each LA channel. These MAC addresses changes after each reboot.
		"""
		try :
			return self._lamac
		except Exception as e:
			raise e

	@lamac.setter
	def lamac(self, lamac) :
		ur"""Specifies a MAC address for the LA channels configured in NetScaler virtual appliances (VPX). This MAC address is persistent after each reboot. If you don't specify this parameter, a MAC address is generated randomly for each LA channel. These MAC addresses changes after each reboot.
		"""
		try :
			self._lamac = lamac
		except Exception as e:
			raise e

	@property
	def speed(self) :
		ur"""Ethernet speed of the channel, in Mbps. If the speed of any bound interface is greater than or equal to the value set for this parameter, the state of the interface is UP. Otherwise, the state is INACTIVE. Bound Interfaces whose state is INACTIVE do not process any traffic.<br/>Default value: AUTO<br/>Possible values = AUTO, 10, 100, 1000, 10000.
		"""
		try :
			return self._speed
		except Exception as e:
			raise e

	@speed.setter
	def speed(self, speed) :
		ur"""Ethernet speed of the channel, in Mbps. If the speed of any bound interface is greater than or equal to the value set for this parameter, the state of the interface is UP. Otherwise, the state is INACTIVE. Bound Interfaces whose state is INACTIVE do not process any traffic.<br/>Default value: AUTO<br/>Possible values = AUTO, 10, 100, 1000, 10000
		"""
		try :
			self._speed = speed
		except Exception as e:
			raise e

	@property
	def flowctl(self) :
		ur"""Specifies the flow control type for this LA channel to manage the flow of frames. Flow control is a function as mentioned in clause 31 of the IEEE 802.3 standard. Flow control allows congested ports to pause traffic from the peer device. Flow control is achieved by sending PAUSE frames.<br/>Default value: OFF<br/>Possible values = OFF, RX, TX, RXTX.
		"""
		try :
			return self._flowctl
		except Exception as e:
			raise e

	@flowctl.setter
	def flowctl(self, flowctl) :
		ur"""Specifies the flow control type for this LA channel to manage the flow of frames. Flow control is a function as mentioned in clause 31 of the IEEE 802.3 standard. Flow control allows congested ports to pause traffic from the peer device. Flow control is achieved by sending PAUSE frames.<br/>Default value: OFF<br/>Possible values = OFF, RX, TX, RXTX
		"""
		try :
			self._flowctl = flowctl
		except Exception as e:
			raise e

	@property
	def hamonitor(self) :
		ur"""In a High Availability (HA) configuration, monitor the LA channel for failure events. Failure of any LA channel that has HA MON enabled triggers HA failover.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._hamonitor
		except Exception as e:
			raise e

	@hamonitor.setter
	def hamonitor(self, hamonitor) :
		ur"""In a High Availability (HA) configuration, monitor the LA channel for failure events. Failure of any LA channel that has HA MON enabled triggers HA failover.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._hamonitor = hamonitor
		except Exception as e:
			raise e

	@property
	def tagall(self) :
		ur"""Adds a four-byte 802.1q tag to every packet sent on this channel.  The ON setting applies tags for all VLANs that are bound to this channel. OFF applies the tag for all VLANs other than the native VLAN.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._tagall
		except Exception as e:
			raise e

	@tagall.setter
	def tagall(self, tagall) :
		ur"""Adds a four-byte 802.1q tag to every packet sent on this channel.  The ON setting applies tags for all VLANs that are bound to this channel. OFF applies the tag for all VLANs other than the native VLAN.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._tagall = tagall
		except Exception as e:
			raise e

	@property
	def trunk(self) :
		ur"""This is deprecated by tagall.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._trunk
		except Exception as e:
			raise e

	@trunk.setter
	def trunk(self, trunk) :
		ur"""This is deprecated by tagall.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._trunk = trunk
		except Exception as e:
			raise e

	@property
	def ifalias(self) :
		ur"""Alias name for the LA channel. Used only to enhance readability. To perform any operations, you have to specify the LA channel ID.<br/>Default value: " "<br/>Maximum length =  31.
		"""
		try :
			return self._ifalias
		except Exception as e:
			raise e

	@ifalias.setter
	def ifalias(self, ifalias) :
		ur"""Alias name for the LA channel. Used only to enhance readability. To perform any operations, you have to specify the LA channel ID.<br/>Default value: " "<br/>Maximum length =  31
		"""
		try :
			self._ifalias = ifalias
		except Exception as e:
			raise e

	@property
	def throughput(self) :
		ur"""Low threshold value for the throughput of the LA channel, in Mbps. In an high availability (HA) configuration, failover is triggered when the LA channel has HA MON enabled and the throughput is below the specified threshold.<br/>Maximum length =  160000.
		"""
		try :
			return self._throughput
		except Exception as e:
			raise e

	@throughput.setter
	def throughput(self, throughput) :
		ur"""Low threshold value for the throughput of the LA channel, in Mbps. In an high availability (HA) configuration, failover is triggered when the LA channel has HA MON enabled and the throughput is below the specified threshold.<br/>Maximum length =  160000
		"""
		try :
			self._throughput = throughput
		except Exception as e:
			raise e

	@property
	def bandwidthhigh(self) :
		ur"""High threshold value for the bandwidth usage of the LA channel, in Mbps. The NetScaler appliance generates an SNMP trap message when the bandwidth usage of the LA channel is greater than or equal to the specified high threshold value.<br/>Maximum length =  160000.
		"""
		try :
			return self._bandwidthhigh
		except Exception as e:
			raise e

	@bandwidthhigh.setter
	def bandwidthhigh(self, bandwidthhigh) :
		ur"""High threshold value for the bandwidth usage of the LA channel, in Mbps. The NetScaler appliance generates an SNMP trap message when the bandwidth usage of the LA channel is greater than or equal to the specified high threshold value.<br/>Maximum length =  160000
		"""
		try :
			self._bandwidthhigh = bandwidthhigh
		except Exception as e:
			raise e

	@property
	def bandwidthnormal(self) :
		ur"""Normal threshold value for the bandwidth usage of the LA channel, in Mbps. When the bandwidth usage of the LA channel returns to less than or equal to the specified normal threshold after exceeding the high threshold, the NetScaler appliance generates an SNMP trap message to indicate that the bandwidth usage has returned to normal.<br/>Maximum length =  160000.
		"""
		try :
			return self._bandwidthnormal
		except Exception as e:
			raise e

	@bandwidthnormal.setter
	def bandwidthnormal(self, bandwidthnormal) :
		ur"""Normal threshold value for the bandwidth usage of the LA channel, in Mbps. When the bandwidth usage of the LA channel returns to less than or equal to the specified normal threshold after exceeding the high threshold, the NetScaler appliance generates an SNMP trap message to indicate that the bandwidth usage has returned to normal.<br/>Maximum length =  160000
		"""
		try :
			self._bandwidthnormal = bandwidthnormal
		except Exception as e:
			raise e

	@property
	def mtu(self) :
		ur"""The maximum transmission unit (MTU) is the largest packet size, measured in bytes excluding 14 bytes ethernet header and 4 bytes crc, that can be transmitted and received by this interface. Default value of MTU is 1500 on all the interface of Netscaler appliance any value configured more than 1500 on the interface will make the interface as jumbo enabled. In case of cluster backplane interface MTU value will be changed to 1514 by default, user has to change the backplane interface value to maximum mtu configured on any of the interface in cluster system plus 14 bytes more for backplane interface if Jumbo is enabled on any of the interface in a cluster system. Changing the backplane will bring back the MTU of backplane interface to default value of 1500. If a channel is configured as backplane then the same holds true for channel as well as member interfaces. In case of channel if member interfaces is configured as different mtu then the highest MTU configured MTU is treated as the LA MTU if MTU is not specified on LA explicitly. Low MTU interfaces in channel will be taken out of LA distribution list.<br/>Default value: 1500<br/>Minimum length =  1500<br/>Maximum length =  9216.
		"""
		try :
			return self._mtu
		except Exception as e:
			raise e

	@mtu.setter
	def mtu(self, mtu) :
		ur"""The maximum transmission unit (MTU) is the largest packet size, measured in bytes excluding 14 bytes ethernet header and 4 bytes crc, that can be transmitted and received by this interface. Default value of MTU is 1500 on all the interface of Netscaler appliance any value configured more than 1500 on the interface will make the interface as jumbo enabled. In case of cluster backplane interface MTU value will be changed to 1514 by default, user has to change the backplane interface value to maximum mtu configured on any of the interface in cluster system plus 14 bytes more for backplane interface if Jumbo is enabled on any of the interface in a cluster system. Changing the backplane will bring back the MTU of backplane interface to default value of 1500. If a channel is configured as backplane then the same holds true for channel as well as member interfaces. In case of channel if member interfaces is configured as different mtu then the highest MTU configured MTU is treated as the LA MTU if MTU is not specified on LA explicitly. Low MTU interfaces in channel will be taken out of LA distribution list.<br/>Default value: 1500<br/>Minimum length =  1500<br/>Maximum length =  9216
		"""
		try :
			self._mtu = mtu
		except Exception as e:
			raise e

	@property
	def lrminthroughput(self) :
		ur"""Specifies the minimum throughput threshold (in Mbps) to be met by the active subchannel. Setting this parameter automatically divides an LACP channel into logical subchannels, with one subchannel active and the others in standby mode.  When the maximum supported throughput of the active channel falls below the lrMinThroughput value, link failover occurs and a standby subchannel becomes active.<br/>Maximum length =  80000.
		"""
		try :
			return self._lrminthroughput
		except Exception as e:
			raise e

	@lrminthroughput.setter
	def lrminthroughput(self, lrminthroughput) :
		ur"""Specifies the minimum throughput threshold (in Mbps) to be met by the active subchannel. Setting this parameter automatically divides an LACP channel into logical subchannels, with one subchannel active and the others in standby mode.  When the maximum supported throughput of the active channel falls below the lrMinThroughput value, link failover occurs and a standby subchannel becomes active.<br/>Maximum length =  80000
		"""
		try :
			self._lrminthroughput = lrminthroughput
		except Exception as e:
			raise e

	@property
	def linkredundancy(self) :
		ur"""Link Redundancy for Cluster LAG.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._linkredundancy
		except Exception as e:
			raise e

	@linkredundancy.setter
	def linkredundancy(self, linkredundancy) :
		ur"""Link Redundancy for Cluster LAG.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._linkredundancy = linkredundancy
		except Exception as e:
			raise e

	@property
	def devicename(self) :
		ur"""LA channel name in form LA/x, where x is channel ID, which ranges from 1 to 8.
		"""
		try :
			return self._devicename
		except Exception as e:
			raise e

	@property
	def unit(self) :
		ur"""Unit number of the channel. This is an internal reference number that the NetScaler uses to identify the channel.
		"""
		try :
			return self._unit
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""The IEEE standard that the channel is based on.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""Flags of this channel.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def actualmtu(self) :
		ur"""MTU of the channel. This is the maximum frame size that the channel can process.
		"""
		try :
			return self._actualmtu
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		ur"""Native VLAN of the channel.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@property
	def mac(self) :
		ur"""MAC address of the channel.
		"""
		try :
			return self._mac
		except Exception as e:
			raise e

	@property
	def uptime(self) :
		ur"""Duration for which the channel is UP. (Example: 3 hours 1 minute 1 second). This value is reset when the channel state changes to DOWN.
		"""
		try :
			return self._uptime
		except Exception as e:
			raise e

	@property
	def downtime(self) :
		ur"""Duration for which the channel is DOWN. (Example: 3 hours 1 minute 1 second). This value is reset when the channel state changes to UP.
		"""
		try :
			return self._downtime
		except Exception as e:
			raise e

	@property
	def reqmedia(self) :
		ur"""Requested media setting for this channel. Since there is no media associated with LA, the displayed values carry no significance.<br/>Possible values = AUTO, UTP, FIBER.
		"""
		try :
			return self._reqmedia
		except Exception as e:
			raise e

	@property
	def reqspeed(self) :
		ur"""Requested speed setting for this channel. Since no media are associated with LA, this speed is used to determine the threshold for the slave interfaces. If the speed of the member interface is less than the requested speed, that interface is considered inactive.<br/>Possible values = AUTO, 10, 100, 1000, 10000.
		"""
		try :
			return self._reqspeed
		except Exception as e:
			raise e

	@property
	def reqduplex(self) :
		ur"""Requested duplex setting for this channel. Since no media are associated with LA, the displayed values carry no significance.<br/>Possible values = AUTO, HALF, FULL.
		"""
		try :
			return self._reqduplex
		except Exception as e:
			raise e

	@property
	def reqflowcontrol(self) :
		ur"""Requested flow control setting for this channel. Since no media are associated with LA, the displayed values carry no significance.<br/>Possible values = OFF, RX, TX, RXTX.
		"""
		try :
			return self._reqflowcontrol
		except Exception as e:
			raise e

	@property
	def media(self) :
		ur"""Requested media setting for this interface.<br/>Possible values = AUTO, UTP, FIBER.
		"""
		try :
			return self._media
		except Exception as e:
			raise e

	@property
	def actspeed(self) :
		ur"""Actual speed setting for this channel.<br/>Possible values = AUTO, 10, 100, 1000, 10000.
		"""
		try :
			return self._actspeed
		except Exception as e:
			raise e

	@property
	def duplex(self) :
		ur"""Actualduplex setting for this interface.<br/>Possible values = AUTO, HALF, FULL.
		"""
		try :
			return self._duplex
		except Exception as e:
			raise e

	@property
	def actflowctl(self) :
		ur"""Actual flow control setting for this channel.<br/>Possible values = OFF, RX, TX, RXTX.
		"""
		try :
			return self._actflowctl
		except Exception as e:
			raise e

	@property
	def lamode(self) :
		ur"""The  mode(AUTO/MANNUAL) for the LA channel.<br/>Possible values = MANUAL, AUTO.
		"""
		try :
			return self._lamode
		except Exception as e:
			raise e

	@property
	def autoneg(self) :
		ur"""Requested auto negotiation setting for this channel. Since no media are associated with LA, this setting has no effect.
		"""
		try :
			return self._autoneg
		except Exception as e:
			raise e

	@property
	def autonegresult(self) :
		ur"""Actual  auto negotiation setting for this channel.
		"""
		try :
			return self._autonegresult
		except Exception as e:
			raise e

	@property
	def tagged(self) :
		ur"""VLAN tags setting on this channel.
		"""
		try :
			return self._tagged
		except Exception as e:
			raise e

	@property
	def taggedany(self) :
		ur"""Channel setting to accept/drop all tagged packets.
		"""
		try :
			return self._taggedany
		except Exception as e:
			raise e

	@property
	def taggedautolearn(self) :
		ur"""Dynaminc vlan membership on this channel.
		"""
		try :
			return self._taggedautolearn
		except Exception as e:
			raise e

	@property
	def hangdetect(self) :
		ur"""Hang detect for this channel.
		"""
		try :
			return self._hangdetect
		except Exception as e:
			raise e

	@property
	def hangreset(self) :
		ur"""Hang reset for this channel.
		"""
		try :
			return self._hangreset
		except Exception as e:
			raise e

	@property
	def linkstate(self) :
		ur"""The current state of the link associated with the interface. For logical interfaces (LA), the state of the link is dependent on the state of the slave interfaces. For the link to be UP at least one of the slave interfaces needs to be UP.
		"""
		try :
			return self._linkstate
		except Exception as e:
			raise e

	@property
	def intfstate(self) :
		ur"""Current state of the specified interface.  The interface state set to UP only if the link state is UP and administrative state is ENABLED.
		"""
		try :
			return self._intfstate
		except Exception as e:
			raise e

	@property
	def rxpackets(self) :
		ur"""Number of bytes received by all the slave interfaces of the channel since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._rxpackets
		except Exception as e:
			raise e

	@property
	def rxbytes(self) :
		ur"""Number of packets received by all member interfaces since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._rxbytes
		except Exception as e:
			raise e

	@property
	def rxerrors(self) :
		ur"""Number of inbound packets dropped by the hardware of the slave interfaces since the NetScaler appliance was started or the interface statistics were cleared. Possible causes of dropped packets are CRC, length (undersize or oversize), and alignment errors.
		"""
		try :
			return self._rxerrors
		except Exception as e:
			raise e

	@property
	def rxdrops(self) :
		ur"""Number of inbound packets dropped by the channel's slave interfaces. Commonly dropped packets are multicast frames, spanning tree BPDUs, packets destined to a MAC not owned by the NetScaler when L2 mode is disabled, or packets tagged for a VLAN that is not bound to the interface.  In most healthy networks, this statistic increments at a steady rate regardless of traffic load.  A sharp spike in dropped packets generally indicates an issue with connected L2 switches, such as a forwarding database overflow resulting in packets being broadcast on all ports.
		"""
		try :
			return self._rxdrops
		except Exception as e:
			raise e

	@property
	def txpackets(self) :
		ur"""Number of packets transmitted by slave interfaces of a channel since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._txpackets
		except Exception as e:
			raise e

	@property
	def txbytes(self) :
		ur"""Number of bytes transmitted by slave interfaces of a channel since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._txbytes
		except Exception as e:
			raise e

	@property
	def txerrors(self) :
		ur"""Number of outbound packets dropped by the hardware of a channel's slave interfaces since the NetScaler appliance was started or the interface statistics were cleared. Possible causes of dropped packets are length (undersize or oversize) errors and lack of resources.
		"""
		try :
			return self._txerrors
		except Exception as e:
			raise e

	@property
	def txdrops(self) :
		ur"""Number of packets dropped in transmission by a channel's slave interfaces for one of the following reasons:
		(1) VLAN mismatch.
		(2) Oversized packets.
		(3) Interface congestion.
		(4) Loopback packets sent on non-loopback interface.
		"""
		try :
			return self._txdrops
		except Exception as e:
			raise e

	@property
	def indisc(self) :
		ur"""Number of error-free inbound packets discarded by a channel's slave interfaces because of a lack of resources (for example, insufficient receive buffers).
		"""
		try :
			return self._indisc
		except Exception as e:
			raise e

	@property
	def outdisc(self) :
		ur"""Number of error-free outbound packets discarded by a channel's slave interfaces because of a lack of resources. This statistic is not available on:
		(1) 10G ports of NetScaler MPX 12500/12500/15500-10G  platforms.
		(2) 10G data ports on NetScaler MPX 17500/19500/21500 platforms.
		"""
		try :
			return self._outdisc
		except Exception as e:
			raise e

	@property
	def fctls(self) :
		ur"""Number of times flow control is performed on a channel's slave interfaces because of pause frames.
		"""
		try :
			return self._fctls
		except Exception as e:
			raise e

	@property
	def hangs(self) :
		ur"""Number of hangs that occurred on the channel's slave interfaces.
		"""
		try :
			return self._hangs
		except Exception as e:
			raise e

	@property
	def stsstalls(self) :
		ur"""Number of status stalls that occurred on the channel's slave interfaces.
		"""
		try :
			return self._stsstalls
		except Exception as e:
			raise e

	@property
	def txstalls(self) :
		ur"""Number of Tx stalls happened that occurred on the channel's slave interfaces.
		"""
		try :
			return self._txstalls
		except Exception as e:
			raise e

	@property
	def rxstalls(self) :
		ur"""Number of Rx stalls that occurred on the channel's slave interfaces.
		"""
		try :
			return self._rxstalls
		except Exception as e:
			raise e

	@property
	def bdgmuted(self) :
		ur"""Number of times a channel's slave interfaces stopped transmitting and receiving packets because of MAC moves between ports.
		"""
		try :
			return self._bdgmuted
		except Exception as e:
			raise e

	@property
	def vmac(self) :
		ur"""Virtual MAC of this channel.
		"""
		try :
			return self._vmac
		except Exception as e:
			raise e

	@property
	def vmac6(self) :
		ur"""Virtual MAC for IPv6 on this interface.
		"""
		try :
			return self._vmac6
		except Exception as e:
			raise e

	@property
	def reqthroughput(self) :
		ur"""Minimum required throughput for an interface. Failover is triggered if the operating throughput of a Link Aggregation (LA) channel for which HAMON is ON falls below this value.<br/>Minimum value =  0<br/>Maximum value =  160000.
		"""
		try :
			return self._reqthroughput
		except Exception as e:
			raise e

	@property
	def actthroughput(self) :
		ur"""Actual throughput for the interface.
		"""
		try :
			return self._actthroughput
		except Exception as e:
			raise e

	@property
	def backplane(self) :
		ur"""The cluster backplane status of the LA. If the status is enabled, the LA is part of the cluster backplane. By default, the backplane status is disabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._backplane
		except Exception as e:
			raise e

	@property
	def cleartime(self) :
		ur"""Time since the interface stats are cleared last time.
		"""
		try :
			return self._cleartime
		except Exception as e:
			raise e

	@property
	def lacpmode(self) :
		ur"""The LACP mode of the specified interface. The possible values are:
		1. Active: A port in active mode generates LACP protocol messages on a regular basis, regardless of any need expressed by its partner to receive them.
		2. Passive: A port in passive mode generally does not transmit LACP messages unless its partner is in the active mode; that is, it does not speak unless spoken to.
		3. Disabled: Removes the interface from the LA channel. If this is only interface in the LA channel, the LA channel is also deleted.
		.<br/>Possible values = DISABLED, ACTIVE, PASSIVE.
		"""
		try :
			return self._lacpmode
		except Exception as e:
			raise e

	@property
	def lacptimeout(self) :
		ur"""Time to wait for the LACPDU.  If a LACPDU is not received within this interval, the NetScaler markes the link partner port as DOWN. Possible values: Long and Short. Long lacptimeout is 90 sec and Short LACP timeout is 3 sec.<br/>Possible values = LONG, SHORT.
		"""
		try :
			return self._lacptimeout
		except Exception as e:
			raise e

	@property
	def lacpactorpriority(self) :
		ur"""LACP Actor Priority. A LACP port priority is configured on each port using LACP. LACP uses the port priority with the port number to form the port identifier. The port priority determines which ports should be put in standby mode when there is a hardware limitation that prevents all compatible ports from aggregating.
		"""
		try :
			return self._lacpactorpriority
		except Exception as e:
			raise e

	@property
	def lacpactorportno(self) :
		ur"""LACP Actor port number. LACP uses the port priority with the port number to form the port identifier.
		"""
		try :
			return self._lacpactorportno
		except Exception as e:
			raise e

	@property
	def lacppartnerstate(self) :
		ur"""LACP Partner State. Whether the port is in Active or Passive negotiating state.<br/>Possible values = MANUAL, AUTO.
		"""
		try :
			return self._lacppartnerstate
		except Exception as e:
			raise e

	@property
	def lacppartnertimeout(self) :
		ur"""The timeout value for the information revieved in LACPDUs. It can have values as SHORT or LONG. The SHORT timeout is 3s and the LONG timeout is 90s.<br/>Possible values = LONG, SHORT.
		"""
		try :
			return self._lacppartnertimeout
		except Exception as e:
			raise e

	@property
	def lacppartneraggregation(self) :
		ur"""The Aggregation flag indicates that the participant will allow the link to be used as part of an aggregate. Otherwise the link is to be used as an individual link, i.e. not aggregated with any other.<br/>Possible values = NS_EMPTY_STR, AGG.
		"""
		try :
			return self._lacppartneraggregation
		except Exception as e:
			raise e

	@property
	def lacppartnerinsync(self) :
		ur"""The Synchronization flag indicates that the transmitting participant.s mux component is in sync with the system id and key information transmitted.<br/>Possible values = NS_EMPTY_STR, SYNC.
		"""
		try :
			return self._lacppartnerinsync
		except Exception as e:
			raise e

	@property
	def lacppartnercollecting(self) :
		ur"""The Collecting flag indicates that the participant.s collector, i.e. the reception component of the mux, is definitely on. If set the flag communicates collecting.<br/>Possible values = NS_EMPTY_STR, COLLECTING.
		"""
		try :
			return self._lacppartnercollecting
		except Exception as e:
			raise e

	@property
	def lacppartnerdistributing(self) :
		ur"""The Distributing flag indicates that the participant.s distributor is not definitely off. If reset the flag indicates not distributing.<br/>Possible values = NS_EMPTY_STR, DISTRIBUTING.
		"""
		try :
			return self._lacppartnerdistributing
		except Exception as e:
			raise e

	@property
	def lacppartnerdefaulted(self) :
		ur"""If the timer expires in the Expired state, the Receive Machine enters the Defaulted state.<br/>Possible values = NS_EMPTY_STR, DEFAULTED.
		"""
		try :
			return self._lacppartnerdefaulted
		except Exception as e:
			raise e

	@property
	def lacppartnerexpired(self) :
		ur"""If the LACPDUs are received for timeout period, the Receive Machine enters the Expired state and the timer is restarted with the timeout value of SHORT timeout.<br/>Possible values = NS_EMPTY_STR, EXPIRED.
		"""
		try :
			return self._lacppartnerexpired
		except Exception as e:
			raise e

	@property
	def lacppartnerpriority(self) :
		ur"""LACP Partner Priority. A LACP port priority is configured on each port using LACP. LACP uses the port priority with the port number to form the port identifier. 
		The port priority determines which ports should be put in standby mode when there is a hardware limitation that prevents all compatible ports from aggregating.
		"""
		try :
			return self._lacppartnerpriority
		except Exception as e:
			raise e

	@property
	def lacppartnersystemmac(self) :
		ur"""LACP Partner System MAC.
		"""
		try :
			return self._lacppartnersystemmac
		except Exception as e:
			raise e

	@property
	def lacppartnersystempriority(self) :
		ur"""LACP Partner System Priority. The LACP partner's system priority. The values for the priority range from 0 to 65535. The lower the value, the higher the system priority. The switch with the lower system priority value determines which links between LACP partner are active and which are in the standby for each LACP Channel.
		"""
		try :
			return self._lacppartnersystempriority
		except Exception as e:
			raise e

	@property
	def lacppartnerportno(self) :
		ur"""LACP Partner Port number. LACP uses the port priority with the port number to form the port identifier.
		"""
		try :
			return self._lacppartnerportno
		except Exception as e:
			raise e

	@property
	def lacppartnerkey(self) :
		ur"""LACP Partner Key. The LACP key used by the partner port.
		"""
		try :
			return self._lacppartnerkey
		except Exception as e:
			raise e

	@property
	def lacpactoraggregation(self) :
		ur"""The Aggregation flag indicates that the participant will allow the link to be used as part of an aggregate. Otherwise the link is to be used as an individual link, i.e. not aggregated with any other.<br/>Possible values = NS_EMPTY_STR, AGG.
		"""
		try :
			return self._lacpactoraggregation
		except Exception as e:
			raise e

	@property
	def lacpactorinsync(self) :
		ur"""The Synchronization flag indicates that the transmitting participant.s mux component is in sync with the system id and key information transmitted.<br/>Possible values = NS_EMPTY_STR, SYNC.
		"""
		try :
			return self._lacpactorinsync
		except Exception as e:
			raise e

	@property
	def lacpactorcollecting(self) :
		ur"""The Collecting flag indicates that the participant.s collector, i.e. the reception component of the mux, is definitely on. If set the flag communicates collecting.<br/>Possible values = NS_EMPTY_STR, COLLECTING.
		"""
		try :
			return self._lacpactorcollecting
		except Exception as e:
			raise e

	@property
	def lacpactordistributing(self) :
		ur"""The Distributing flag indicates that the participant.s distributor is not definitely off. If reset the flag indicates not distributing.<br/>Possible values = NS_EMPTY_STR, DISTRIBUTING.
		"""
		try :
			return self._lacpactordistributing
		except Exception as e:
			raise e

	@property
	def lacpportmuxstate(self) :
		ur"""LACP Port MUX state. The state of the MUX control machine. The  Mux Control Machine attaches the physical port to an aggregate port, using the Selection Logic to choose an appropriate port, and turns the distributor and collector for the physical port on or off as required by protocol	information.<br/>Possible values = DETACHED, WAITING, ATTACHED, COLLECTING, DISTRIBUTING.
		"""
		try :
			return self._lacpportmuxstate
		except Exception as e:
			raise e

	@property
	def lacpportrxstat(self) :
		ur"""LACP Port RX state. The state of the Receive machine. The Receive Machine maintains partner information, recording protocol information from LACPDUs sent by remote partner(s). Received information is subject to a timeout, and if sufficient time elapses the receive machine will revert to using default partner information.<br/>Possible values = INIT, PORT_DISABLED, LACP_DISABLED, EXPIRED, DEFAULTED, CURRENT.
		"""
		try :
			return self._lacpportrxstat
		except Exception as e:
			raise e

	@property
	def lacpportselectstate(self) :
		ur"""LACP Port SELECT state. The state of the SELECT state machine, It could be SELECTED or UNSELECTED.<br/>Possible values = UNSELECTED, SELECTED, STANDBY.
		"""
		try :
			return self._lacpportselectstate
		except Exception as e:
			raise e

	@property
	def lldpmode(self) :
		ur"""Link Layer Discovery Protocol (LLDP) mode for an interface. The resultant LLDP mode of an interface depends on the LLDP mode configured at the global and the interface levels.<br/>Possible values = NONE, TRANSMITTER, RECEIVER, TRANSCEIVER.
		"""
		try :
			return self._lldpmode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(channel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.channel
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add channel.
		"""
		try :
			if type(resource) is not list :
				addresource = channel()
				addresource.id = resource.id
				addresource.ifnum = resource.ifnum
				addresource.state = resource.state
				addresource.mode = resource.mode
				addresource.conndistr = resource.conndistr
				addresource.macdistr = resource.macdistr
				addresource.lamac = resource.lamac
				addresource.speed = resource.speed
				addresource.flowctl = resource.flowctl
				addresource.hamonitor = resource.hamonitor
				addresource.tagall = resource.tagall
				addresource.trunk = resource.trunk
				addresource.ifalias = resource.ifalias
				addresource.throughput = resource.throughput
				addresource.bandwidthhigh = resource.bandwidthhigh
				addresource.bandwidthnormal = resource.bandwidthnormal
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ channel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].id = resource[i].id
						addresources[i].ifnum = resource[i].ifnum
						addresources[i].state = resource[i].state
						addresources[i].mode = resource[i].mode
						addresources[i].conndistr = resource[i].conndistr
						addresources[i].macdistr = resource[i].macdistr
						addresources[i].lamac = resource[i].lamac
						addresources[i].speed = resource[i].speed
						addresources[i].flowctl = resource[i].flowctl
						addresources[i].hamonitor = resource[i].hamonitor
						addresources[i].tagall = resource[i].tagall
						addresources[i].trunk = resource[i].trunk
						addresources[i].ifalias = resource[i].ifalias
						addresources[i].throughput = resource[i].throughput
						addresources[i].bandwidthhigh = resource[i].bandwidthhigh
						addresources[i].bandwidthnormal = resource[i].bandwidthnormal
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete channel.
		"""
		try :
			if type(resource) is not list :
				deleteresource = channel()
				if type(resource) !=  type(deleteresource):
					deleteresource.id = resource
				else :
					deleteresource.id = resource.id
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ channel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ channel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i].id
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update channel.
		"""
		try :
			if type(resource) is not list :
				updateresource = channel()
				updateresource.id = resource.id
				updateresource.state = resource.state
				updateresource.mode = resource.mode
				updateresource.conndistr = resource.conndistr
				updateresource.macdistr = resource.macdistr
				updateresource.lamac = resource.lamac
				updateresource.speed = resource.speed
				updateresource.mtu = resource.mtu
				updateresource.flowctl = resource.flowctl
				updateresource.hamonitor = resource.hamonitor
				updateresource.tagall = resource.tagall
				updateresource.trunk = resource.trunk
				updateresource.ifalias = resource.ifalias
				updateresource.throughput = resource.throughput
				updateresource.lrminthroughput = resource.lrminthroughput
				updateresource.linkredundancy = resource.linkredundancy
				updateresource.bandwidthhigh = resource.bandwidthhigh
				updateresource.bandwidthnormal = resource.bandwidthnormal
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ channel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].state = resource[i].state
						updateresources[i].mode = resource[i].mode
						updateresources[i].conndistr = resource[i].conndistr
						updateresources[i].macdistr = resource[i].macdistr
						updateresources[i].lamac = resource[i].lamac
						updateresources[i].speed = resource[i].speed
						updateresources[i].mtu = resource[i].mtu
						updateresources[i].flowctl = resource[i].flowctl
						updateresources[i].hamonitor = resource[i].hamonitor
						updateresources[i].tagall = resource[i].tagall
						updateresources[i].trunk = resource[i].trunk
						updateresources[i].ifalias = resource[i].ifalias
						updateresources[i].throughput = resource[i].throughput
						updateresources[i].lrminthroughput = resource[i].lrminthroughput
						updateresources[i].linkredundancy = resource[i].linkredundancy
						updateresources[i].bandwidthhigh = resource[i].bandwidthhigh
						updateresources[i].bandwidthnormal = resource[i].bandwidthnormal
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of channel resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = channel()
				if type(resource) !=  type(unsetresource):
					unsetresource.id = resource
				else :
					unsetresource.id = resource.id
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ channel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ channel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i].id
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the channel resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = channel()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = channel()
						obj.id = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [channel() for _ in range(len(name))]
							obj = [channel() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = channel()
								obj[i].id = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of channel resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = channel()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the channel resources configured on NetScaler.
		"""
		try :
			obj = channel()
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
		ur""" Use this API to count filtered the set of channel resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = channel()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Lacpportselectstate:
		UNSELECTED = "UNSELECTED"
		SELECTED = "SELECTED"
		STANDBY = "STANDBY"

	class Lamode:
		MANUAL = "MANUAL"
		AUTO = "AUTO"

	class Reqduplex:
		AUTO = "AUTO"
		HALF = "HALF"
		FULL = "FULL"

	class Backplane:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mode:
		MANUAL = "MANUAL"
		AUTO = "AUTO"

	class Lacpportrxstat:
		INIT = "INIT"
		PORT_DISABLED = "PORT_DISABLED"
		LACP_DISABLED = "LACP_DISABLED"
		EXPIRED = "EXPIRED"
		DEFAULTED = "DEFAULTED"
		CURRENT = "CURRENT"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Lacppartnerinsync:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		SYNC = "SYNC"

	class Hamonitor:
		ON = "ON"
		OFF = "OFF"

	class Media:
		AUTO = "AUTO"
		UTP = "UTP"
		FIBER = "FIBER"

	class Lacppartnerdistributing:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		DISTRIBUTING = "DISTRIBUTING"

	class Lacppartnercollecting:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		COLLECTING = "COLLECTING"

	class Conndistr:
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"

	class Reqspeed:
		AUTO = "AUTO"
		_10 = "10"
		_100 = "100"
		_1000 = "1000"
		_10000 = "10000"

	class Duplex:
		AUTO = "AUTO"
		HALF = "HALF"
		FULL = "FULL"

	class Actspeed:
		AUTO = "AUTO"
		_10 = "10"
		_100 = "100"
		_1000 = "1000"
		_10000 = "10000"

	class Reqmedia:
		AUTO = "AUTO"
		UTP = "UTP"
		FIBER = "FIBER"

	class Lacppartnertimeout:
		LONG = "LONG"
		SHORT = "SHORT"

	class Lldpmode:
		NONE = "NONE"
		TRANSMITTER = "TRANSMITTER"
		RECEIVER = "RECEIVER"
		TRANSCEIVER = "TRANSCEIVER"

	class Lacppartnerexpired:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		EXPIRED = "EXPIRED"

	class Macdistr:
		SOURCE = "SOURCE"
		DESTINATION = "DESTINATION"
		BOTH = "BOTH"

	class Lacppartnerstate:
		MANUAL = "MANUAL"
		AUTO = "AUTO"

	class Lacpportmuxstate:
		DETACHED = "DETACHED"
		WAITING = "WAITING"
		ATTACHED = "ATTACHED"
		COLLECTING = "COLLECTING"
		DISTRIBUTING = "DISTRIBUTING"

	class Lacpactordistributing:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		DISTRIBUTING = "DISTRIBUTING"

	class Lacpactorinsync:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		SYNC = "SYNC"

	class Lacppartnerdefaulted:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		DEFAULTED = "DEFAULTED"

	class Actflowctl:
		OFF = "OFF"
		RX = "RX"
		TX = "TX"
		RXTX = "RXTX"

	class Speed:
		AUTO = "AUTO"
		_10 = "10"
		_100 = "100"
		_1000 = "1000"
		_10000 = "10000"

	class Lacptimeout:
		LONG = "LONG"
		SHORT = "SHORT"

	class Tagall:
		ON = "ON"
		OFF = "OFF"

	class Lacppartneraggregation:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		AGG = "AGG"

	class Trunk:
		ON = "ON"
		OFF = "OFF"

	class Lacpmode:
		DISABLED = "DISABLED"
		ACTIVE = "ACTIVE"
		PASSIVE = "PASSIVE"

	class Reqflowcontrol:
		OFF = "OFF"
		RX = "RX"
		TX = "TX"
		RXTX = "RXTX"

	class Lacpactorcollecting:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		COLLECTING = "COLLECTING"

	class Lacpactoraggregation:
		NS_EMPTY_STR = "NS_EMPTY_STR"
		AGG = "AGG"

	class Linkredundancy:
		ON = "ON"
		OFF = "OFF"

	class Flowctl:
		OFF = "OFF"
		RX = "RX"
		TX = "TX"
		RXTX = "RXTX"

class channel_response(base_response) :
	def __init__(self, length=1) :
		self.channel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.channel = [channel() for _ in range(length)]

