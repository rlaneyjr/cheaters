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

class Interface_stats(base_resource) :
	ur""" Statistics for interface resource.
	"""
	def __init__(self) :
		self._id = ""
		self._clearstats = ""
		self._curintfstate = ""
		self._curlinkuptime = ""
		self._curlinkdowntime = ""
		self._totrxbytes = 0
		self._rxbytesrate = 0
		self._tottxbytes = 0
		self._txbytesrate = 0
		self._totrxpkts = 0
		self._rxpktsrate = 0
		self._tottxpkts = 0
		self._txpktsrate = 0
		self._jumbopktsreceived = 0
		self._jumbopktsreceivedrate = 0
		self._jumbopktstransmitted = 0
		self._jumbopktstransmittedrate = 0
		self._nictotmulticastpkts = 0
		self._nicmulticastpktsrate = 0
		self._totnetscalerpkts = 0
		self._netscalerpktsrate = 0
		self._rxlacpdu = 0
		self._rxlacpdurate = 0
		self._txlacpdu = 0
		self._txlacpdurate = 0
		self._errpktrx = 0
		self._errpktrxrate = 0
		self._errpkttx = 0
		self._errpkttxrate = 0
		self._errifindiscards = 0
		self._errifindiscardsrate = 0
		self._nicerrifoutdiscards = 0
		self._nicerrifoutdiscardsrate = 0
		self._errdroppedrxpkts = 0
		self._errdroppedrxpktsrate = 0
		self._errdroppedtxpkts = 0
		self._errdroppedtxpktsrate = 0
		self._errlinkhangs = 0
		self._nicstsstalls = 0
		self._nictxstalls = 0
		self._nicrxstalls = 0
		self._nicerrdisables = 0
		self._errduplexmismatch = 0
		self._linkreinits = 0
		self._totmacmoved = 0
		self._macmovedrate = 0
		self._errnicmuted = 0
		self._interfacealias = ""
		self._curlinkstate = ""

	@property
	def id(self) :
		ur"""Interface number, in C/U format, where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		* LA - Indicates a link aggregation port.
		* LO - Indicates a loop back port.
		U is a unique integer for representing an interface in a particular port group.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""Interface number, in C/U format, where C can take one of the following values:
		* 0 - Indicates a management interface.
		* 1 - Indicates a 1 Gbps port.
		* 10 - Indicates a 10 Gbps port.
		* LA - Indicates a link aggregation port.
		* LO - Indicates a loop back port.
		U is a unique integer for representing an interface in a particular port group.
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		ur"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		ur"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def errpkttx(self) :
		ur"""Number of outbound packets dropped by the hardware on a specified interface since the NetScaler appliance was started or the interface statistics were cleared. This could happen due to length (undersize or oversize) errors and lack of resources. This statistic is available only for: 
		(1) Loop back interface (LO) of all platforms.
		(2) All data ports on the NetScaler 12000 platform.
		(3) Management ports on the MPX 15000 and 17000 platforms.
		"""
		try :
			return self._errpkttx
		except Exception as e:
			raise e

	@property
	def nicrxstalls(self) :
		ur"""Number of times the interface stalled, when receiving packets, since the NetScaler appliance was started or the interface statistics were cleared. Receive (Rx) stalls are detected when the following conditions are met:
		(1)The link is up for more than 10 minutes. 
		(2)Packets are transmitted, but no packets is received for 16 seconds.
		"""
		try :
			return self._nicrxstalls
		except Exception as e:
			raise e

	@property
	def nictotmulticastpkts(self) :
		ur"""Number of multicast packets received by the specified interface since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._nictotmulticastpkts
		except Exception as e:
			raise e

	@property
	def jumbopktstransmitted(self) :
		ur"""Number of Jumbo packets transmitted on this interface by upper layer, with TSO enabled actual trasmission size could be non Jumbo.
		"""
		try :
			return self._jumbopktstransmitted
		except Exception as e:
			raise e

	@property
	def txbytesrate(self) :
		ur"""Rate (/s) counter for tottxbytes.
		"""
		try :
			return self._txbytesrate
		except Exception as e:
			raise e

	@property
	def rxlacpdu(self) :
		ur"""Number of Link Aggregation Control Protocol Data Units(LACPDUs) received by the specified interface since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._rxlacpdu
		except Exception as e:
			raise e

	@property
	def netscalerpktsrate(self) :
		ur"""Rate (/s) counter for totnetscalerpkts.
		"""
		try :
			return self._netscalerpktsrate
		except Exception as e:
			raise e

	@property
	def tottxpkts(self) :
		ur"""Number of packets transmitted by an interface since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._tottxpkts
		except Exception as e:
			raise e

	@property
	def macmovedrate(self) :
		ur"""Rate (/s) counter for totmacmoved.
		"""
		try :
			return self._macmovedrate
		except Exception as e:
			raise e

	@property
	def curintfstate(self) :
		ur"""Current state of the specified interface.  The interface state set to UP only if the link state is UP and administrative state is ENABLED .
		"""
		try :
			return self._curintfstate
		except Exception as e:
			raise e

	@property
	def errpktrx(self) :
		ur"""Number of inbound packets dropped by the hardware on a specified interface once the NetScaler appliance starts or the interface statistics are cleared. This happens due to following reasons:
		1)	The hardware receives packets at a rate higher rate than that at which the software is processing packets. In this case, the hardware FIFO overruns and starts dropping the packets .
		2)	The specified interface fails to receive inbound packets from the appliance because of insufficient memory.
		3)	The specified interface receives packets with CRC errors (Alignment or Frame Check Sequence).
		4)	The specified interface receives overly long packets.
		5)	The specified interface receives packets with alignment errors.
		6)	The software does less buffering because it is running out of available memory. When hardware detects that there is no space into which to push newly arrived packets, it starts dropping them.
		7)	The specified interface receives packets with Frame Check Sequence (FCS) errors.
		8)	The specified interface receives packets smaller than 64 bytes.
		9)	The specified interface discards error-free inbound packets because of insufficient resources. For example: NIC buffers.
		10)	Packets are missed because of collision detection, link lost, physical decoding error, or MAC abort.
		"""
		try :
			return self._errpktrx
		except Exception as e:
			raise e

	@property
	def curlinkdowntime(self) :
		ur"""Duration for which the link is DOWN. This statistic is reset when the state changes to UP.
		"""
		try :
			return self._curlinkdowntime
		except Exception as e:
			raise e

	@property
	def nicmulticastpktsrate(self) :
		ur"""Rate (/s) counter for nictotmulticastpkts.
		"""
		try :
			return self._nicmulticastpktsrate
		except Exception as e:
			raise e

	@property
	def rxbytesrate(self) :
		ur"""Rate (/s) counter for totrxbytes.
		"""
		try :
			return self._rxbytesrate
		except Exception as e:
			raise e

	@property
	def curlinkuptime(self) :
		ur"""Duration for which the link is UP. This statistic is reset when the state changes to DOWN.
		"""
		try :
			return self._curlinkuptime
		except Exception as e:
			raise e

	@property
	def tottxbytes(self) :
		ur"""Number of bytes transmitted by an interface since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._tottxbytes
		except Exception as e:
			raise e

	@property
	def errdroppedtxpktsrate(self) :
		ur"""Rate (/s) counter for errdroppedtxpkts.
		"""
		try :
			return self._errdroppedtxpktsrate
		except Exception as e:
			raise e

	@property
	def errpkttxrate(self) :
		ur"""Rate (/s) counter for errpkttx.
		"""
		try :
			return self._errpkttxrate
		except Exception as e:
			raise e

	@property
	def nictxstalls(self) :
		ur"""Number of times the interface stalled, when transmitting packets, since the NetScaler appliance was started or the interface statistics were cleared. Transmit (Tx) stalls are detected when a packet posted for transmission is not transmitted in 4 seconds.
		"""
		try :
			return self._nictxstalls
		except Exception as e:
			raise e

	@property
	def rxlacpdurate(self) :
		ur"""Rate (/s) counter for rxlacpdu.
		"""
		try :
			return self._rxlacpdurate
		except Exception as e:
			raise e

	@property
	def totnetscalerpkts(self) :
		ur"""Number of packets, destined to the NetScaler, received by an interface since the NetScaler appliance was started or the interface statistics were cleared. The packets destined to NetScaler are those that have the same MAC address as that of an interface or a VMAC address owned by the NetScaler.
		"""
		try :
			return self._totnetscalerpkts
		except Exception as e:
			raise e

	@property
	def jumbopktsreceivedrate(self) :
		ur"""Rate (/s) counter for jumbopktsreceived.
		"""
		try :
			return self._jumbopktsreceivedrate
		except Exception as e:
			raise e

	@property
	def totrxbytes(self) :
		ur"""Number of bytes received by an interface since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._totrxbytes
		except Exception as e:
			raise e

	@property
	def linkreinits(self) :
		ur"""Number of times the link has been re-initialized. A re-initialization occurs due to link state change, configuration parameter change, or administrative reset operation.
		"""
		try :
			return self._linkreinits
		except Exception as e:
			raise e

	@property
	def nicerrdisables(self) :
		ur"""Number of times the specified interface is disabled by the NetScaler, due to continuous Receive (Rx) or Transmit (Tx) stalls, since the NetScaler appliance was started or the interface statistics were cleared. The NetScaler disables an interface when one of the following conditions is met:
		(1) Three consecutive transmit stalls occurs with at most gap of 10 seconds between any two stalls.
		(2) Three consecutive receive stalls occurs with at most gap of 120 seconds between any two stalls.
		"""
		try :
			return self._nicerrdisables
		except Exception as e:
			raise e

	@property
	def txpktsrate(self) :
		ur"""Rate (/s) counter for tottxpkts.
		"""
		try :
			return self._txpktsrate
		except Exception as e:
			raise e

	@property
	def jumbopktsreceived(self) :
		ur"""Number of Jumbo Packets received on this interface.
		"""
		try :
			return self._jumbopktsreceived
		except Exception as e:
			raise e

	@property
	def txlacpdu(self) :
		ur"""Number of Link Aggregation Control Protocol Data Units(LACPDUs) transmitted by the specified interface since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._txlacpdu
		except Exception as e:
			raise e

	@property
	def errdroppedrxpktsrate(self) :
		ur"""Rate (/s) counter for errdroppedrxpkts.
		"""
		try :
			return self._errdroppedrxpktsrate
		except Exception as e:
			raise e

	@property
	def errnicmuted(self) :
		ur"""Number of times the specified interface stopped transmitting and receiving packets due to MAC moves between ports.
		"""
		try :
			return self._errnicmuted
		except Exception as e:
			raise e

	@property
	def errdroppedtxpkts(self) :
		ur"""Number of packets dropped in transmission by the specified interface due to one of the following reasons.
		(1) VLAN mismatch.
		(2) Oversized packets.
		(3) Interface congestion.  
		(4) Loopback packets sent on non loop back interface.
		"""
		try :
			return self._errdroppedtxpkts
		except Exception as e:
			raise e

	@property
	def nicerrifoutdiscardsrate(self) :
		ur"""Rate (/s) counter for nicerrifoutdiscards.
		"""
		try :
			return self._nicerrifoutdiscardsrate
		except Exception as e:
			raise e

	@property
	def errifindiscardsrate(self) :
		ur"""Rate (/s) counter for errifindiscards.
		"""
		try :
			return self._errifindiscardsrate
		except Exception as e:
			raise e

	@property
	def nicerrifoutdiscards(self) :
		ur"""Number of error-free outbound packets discarded by the specified interface due to a lack of resources. This statistic is not available on:
		(1) 10G ports of NetScaler MPX 12500/12500/15500-10G  platforms. 
		(2) 10G data ports on NetScaler MPX 17500/19500/21500 platforms.
		"""
		try :
			return self._nicerrifoutdiscards
		except Exception as e:
			raise e

	@property
	def curlinkstate(self) :
		ur"""The current state of the link associated with the interface. For logical interfaces (LA), the state of the link is dependent on the state of the slave interfaces. For the link to be UP at least one of the slave interfaces needs to be UP.
		"""
		try :
			return self._curlinkstate
		except Exception as e:
			raise e

	@property
	def errifindiscards(self) :
		ur"""Number of error-free inbound packets discarded by the specified interface due to a lack of resources, for example, insufficient receive buffers.
		"""
		try :
			return self._errifindiscards
		except Exception as e:
			raise e

	@property
	def interfacealias(self) :
		ur"""Alias Name for the Interface.
		"""
		try :
			return self._interfacealias
		except Exception as e:
			raise e

	@property
	def totrxpkts(self) :
		ur"""Number of packets received by an interface since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._totrxpkts
		except Exception as e:
			raise e

	@property
	def totmacmoved(self) :
		ur"""Number of MAC moves between ports. If a high rate of MAC moves is observed, it is likely that there is a bridge loop between two interfaces.
		"""
		try :
			return self._totmacmoved
		except Exception as e:
			raise e

	@property
	def rxpktsrate(self) :
		ur"""Rate (/s) counter for totrxpkts.
		"""
		try :
			return self._rxpktsrate
		except Exception as e:
			raise e

	@property
	def errduplexmismatch(self) :
		ur"""Number of times duplex mismatches were detected on the specified interface since the NetScaler appliance was started or the interface statistics were cleared. A mismatch will occur if the duplex mode is not identically set on both ends of the link. This statistic is only available on the NetScaler Classic edition.
		"""
		try :
			return self._errduplexmismatch
		except Exception as e:
			raise e

	@property
	def jumbopktstransmittedrate(self) :
		ur"""Rate (/s) counter for jumbopktstransmitted.
		"""
		try :
			return self._jumbopktstransmittedrate
		except Exception as e:
			raise e

	@property
	def errpktrxrate(self) :
		ur"""Rate (/s) counter for errpktrx.
		"""
		try :
			return self._errpktrxrate
		except Exception as e:
			raise e

	@property
	def errlinkhangs(self) :
		ur"""Number of times the specified interface detected hangs in the transmit and receive paths since the NetScaler appliance was started or the interface statistics were cleared.
		"""
		try :
			return self._errlinkhangs
		except Exception as e:
			raise e

	@property
	def errdroppedrxpkts(self) :
		ur"""Number of inbound packets dropped by the specified interface. Commonly dropped packets are multicast frames, spanning tree BPDUs, packets destined to a MAC not owned by the NetScaler when L2 mode is disabled, or packets tagged for a VLAN that is not bound to the interface.  This statistic will increment in most healthy networks at a steady rate regardless of traffic load.  If a sharp spike in dropped packets occurs, it generally indicates an issue with connected L2 switches, such as a forwarding database overflow resulting in packets being broadcast on all ports.
		"""
		try :
			return self._errdroppedrxpkts
		except Exception as e:
			raise e

	@property
	def txlacpdurate(self) :
		ur"""Rate (/s) counter for txlacpdu.
		"""
		try :
			return self._txlacpdurate
		except Exception as e:
			raise e

	@property
	def nicstsstalls(self) :
		ur"""Number of times the status updates for a specified interface were stalled since the NetScaler appliance was started or the interface statistics were cleared. A status stall is detected when the status of the interface is not updated by the NIC hardware within 0.8 seconds of the last update.
		"""
		try :
			return self._nicstsstalls
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(Interface_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.Interface
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all Interface_stats resources that are configured on netscaler.
		"""
		try :
			obj = Interface_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.id = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class Interface_response(base_response) :
	def __init__(self, length=1) :
		self.Interface = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.Interface = [Interface_stats() for _ in range(length)]

