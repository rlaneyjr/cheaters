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

class protocolipv6_stats(base_resource) :
	ur""" Statistics for ip v6 resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._ipv6totrxpkts = 0
		self._ipv6rxpktsrate = 0
		self._ipv6totrxbytes = 0
		self._ipv6rxbytesrate = 0
		self._ipv6tottxpkts = 0
		self._ipv6txpktsrate = 0
		self._ipv6tottxbytes = 0
		self._ipv6txbytesrate = 0
		self._ipv6totroutepkts = 0
		self._ipv6routepktsrate = 0
		self._ipv6totroutembits = 0
		self._ipv6routembitsrate = 0
		self._ipv6fragtotrxpkts = 0
		self._ipv6fragrxpktsrate = 0
		self._ipv6fragtottcpreassembled = 0
		self._ipv6fragtcpreassembledrate = 0
		self._ipv6fragtotudpreassembled = 0
		self._ipv6fragudpreassembledrate = 0
		self._ipv6fragtotpktsprocessnoreass = 0
		self._ipv6fragpktsprocessnoreassrate = 0
		self._ipv6fragtotpktsforward = 0
		self._ipv6fragpktsforwardrate = 0
		self._ipv6errhdr = 0
		self._ipv6nextheadererr = 0
		self._ipv6landattack = 0
		self._ipv6fragpkttoobig = 0
		self._ipv6fragzerolenpkt = 0
		self._ipv6toticmpnarx = 0
		self._ipv6icmpnarxrate = 0
		self._ipv6toticmpnsrx = 0
		self._ipv6icmpnsrxrate = 0
		self._ipv6toticmpnatx = 0
		self._ipv6icmpnatxrate = 0
		self._ipv6toticmpnstx = 0
		self._ipv6icmpnstxrate = 0
		self._ipv6toticmprarx = 0
		self._ipv6icmprarxrate = 0
		self._ipv6toticmprstx = 0
		self._ipv6icmprstxrate = 0
		self._ipv6toticmprx = 0
		self._ipv6icmprxrate = 0
		self._ipv6toticmptx = 0
		self._ipv6icmptxrate = 0
		self._ipv6errrxhdr = 0
		self._ipv6errrxpkt = 0
		self._ipv6badcksum = 0
		self._icmpv6error = 0
		self._icmpv6unspt = 0
		self._icmpv6rtthsld = 0

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
	def ipv6fragpktsforwardrate(self) :
		ur"""Rate (/s) counter for ipv6fragtotpktsforward.
		"""
		try :
			return self._ipv6fragpktsforwardrate
		except Exception as e:
			raise e

	@property
	def ipv6icmprstxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmprstx.
		"""
		try :
			return self._ipv6icmprstxrate
		except Exception as e:
			raise e

	@property
	def ipv6fragrxpktsrate(self) :
		ur"""Rate (/s) counter for ipv6fragtotrxpkts.
		"""
		try :
			return self._ipv6fragrxpktsrate
		except Exception as e:
			raise e

	@property
	def ipv6totroutepkts(self) :
		ur"""IPv6 packets routed.
		"""
		try :
			return self._ipv6totroutepkts
		except Exception as e:
			raise e

	@property
	def ipv6fragpkttoobig(self) :
		ur"""Packets received for which the reassembled data exceeds the Ethernet packet data length of 1500 bytes.
		"""
		try :
			return self._ipv6fragpkttoobig
		except Exception as e:
			raise e

	@property
	def ipv6toticmpnarx(self) :
		ur"""Number of ICMPv6 NA packets received by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmpnarx
		except Exception as e:
			raise e

	@property
	def ipv6fragtotrxpkts(self) :
		ur"""IPv6 fragments received.
		"""
		try :
			return self._ipv6fragtotrxpkts
		except Exception as e:
			raise e

	@property
	def ipv6icmpnatxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmpnatx.
		"""
		try :
			return self._ipv6icmpnatxrate
		except Exception as e:
			raise e

	@property
	def ipv6toticmpnsrx(self) :
		ur"""Number of ICMPv6 NS packets received by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmpnsrx
		except Exception as e:
			raise e

	@property
	def ipv6routembitsrate(self) :
		ur"""Rate (/s) counter for ipv6totroutembits.
		"""
		try :
			return self._ipv6routembitsrate
		except Exception as e:
			raise e

	@property
	def ipv6txpktsrate(self) :
		ur"""Rate (/s) counter for ipv6tottxpkts.
		"""
		try :
			return self._ipv6txpktsrate
		except Exception as e:
			raise e

	@property
	def icmpv6rtthsld(self) :
		ur"""Number of ICMPv6 packets dropped for rate threshold exceeded (OBSOLETE).
		"""
		try :
			return self._icmpv6rtthsld
		except Exception as e:
			raise e

	@property
	def icmpv6unspt(self) :
		ur"""Number of ICMPv6 unsupported packets received (OBSOLETE).
		"""
		try :
			return self._icmpv6unspt
		except Exception as e:
			raise e

	@property
	def ipv6badcksum(self) :
		ur"""Number of bad checksum packets received (OBSOLETE).
		"""
		try :
			return self._ipv6badcksum
		except Exception as e:
			raise e

	@property
	def ipv6errrxhdr(self) :
		ur"""Number of erroneous header packets received (OBSOLETE).
		"""
		try :
			return self._ipv6errrxhdr
		except Exception as e:
			raise e

	@property
	def ipv6totrxbytes(self) :
		ur"""Bytes of IPv6 data received.
		"""
		try :
			return self._ipv6totrxbytes
		except Exception as e:
			raise e

	@property
	def ipv6rxpktsrate(self) :
		ur"""Rate (/s) counter for ipv6totrxpkts.
		"""
		try :
			return self._ipv6rxpktsrate
		except Exception as e:
			raise e

	@property
	def ipv6icmpnstxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmpnstx.
		"""
		try :
			return self._ipv6icmpnstxrate
		except Exception as e:
			raise e

	@property
	def ipv6icmprarxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmprarx.
		"""
		try :
			return self._ipv6icmprarxrate
		except Exception as e:
			raise e

	@property
	def ipv6errhdr(self) :
		ur"""Packets received that contain an error in one or more components of the IPv6 header.
		"""
		try :
			return self._ipv6errhdr
		except Exception as e:
			raise e

	@property
	def ipv6totrxpkts(self) :
		ur"""IPv6 packets received.
		"""
		try :
			return self._ipv6totrxpkts
		except Exception as e:
			raise e

	@property
	def ipv6toticmprx(self) :
		ur"""Number of ICMPv6 packets received by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmprx
		except Exception as e:
			raise e

	@property
	def ipv6fragtotpktsprocessnoreass(self) :
		ur"""IPv6 fragments processed without reassembly.
		"""
		try :
			return self._ipv6fragtotpktsprocessnoreass
		except Exception as e:
			raise e

	@property
	def ipv6rxbytesrate(self) :
		ur"""Rate (/s) counter for ipv6totrxbytes.
		"""
		try :
			return self._ipv6rxbytesrate
		except Exception as e:
			raise e

	@property
	def ipv6icmpnsrxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmpnsrx.
		"""
		try :
			return self._ipv6icmpnsrxrate
		except Exception as e:
			raise e

	@property
	def ipv6toticmpnatx(self) :
		ur"""Number of ICMPv6 NA packets transmitted by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmpnatx
		except Exception as e:
			raise e

	@property
	def ipv6routepktsrate(self) :
		ur"""Rate (/s) counter for ipv6totroutepkts.
		"""
		try :
			return self._ipv6routepktsrate
		except Exception as e:
			raise e

	@property
	def ipv6icmptxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmptx.
		"""
		try :
			return self._ipv6icmptxrate
		except Exception as e:
			raise e

	@property
	def ipv6toticmprstx(self) :
		ur"""Number of ICMPv6 RS packets transmitted by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmprstx
		except Exception as e:
			raise e

	@property
	def ipv6totroutembits(self) :
		ur"""IPv6 total Mbits.
		"""
		try :
			return self._ipv6totroutembits
		except Exception as e:
			raise e

	@property
	def ipv6icmprxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmprx.
		"""
		try :
			return self._ipv6icmprxrate
		except Exception as e:
			raise e

	@property
	def ipv6fragpktsprocessnoreassrate(self) :
		ur"""Rate (/s) counter for ipv6fragtotpktsprocessnoreass.
		"""
		try :
			return self._ipv6fragpktsprocessnoreassrate
		except Exception as e:
			raise e

	@property
	def ipv6fragtcpreassembledrate(self) :
		ur"""Rate (/s) counter for ipv6fragtottcpreassembled.
		"""
		try :
			return self._ipv6fragtcpreassembledrate
		except Exception as e:
			raise e

	@property
	def ipv6tottxpkts(self) :
		ur"""IPv6 packets transmitted.
		"""
		try :
			return self._ipv6tottxpkts
		except Exception as e:
			raise e

	@property
	def ipv6icmpnarxrate(self) :
		ur"""Rate (/s) counter for ipv6toticmpnarx.
		"""
		try :
			return self._ipv6icmpnarxrate
		except Exception as e:
			raise e

	@property
	def ipv6fragtotudpreassembled(self) :
		ur"""UDP fragments processed after reassembly.
		"""
		try :
			return self._ipv6fragtotudpreassembled
		except Exception as e:
			raise e

	@property
	def ipv6fragtottcpreassembled(self) :
		ur"""TCP fragments processed after reassembly.
		"""
		try :
			return self._ipv6fragtottcpreassembled
		except Exception as e:
			raise e

	@property
	def ipv6errrxpkt(self) :
		ur"""Number of erroneous packets received (OBSOLETE).
		"""
		try :
			return self._ipv6errrxpkt
		except Exception as e:
			raise e

	@property
	def ipv6nextheadererr(self) :
		ur"""Packets received that contain an unsupported next header. The supported next headers are TCP, ICMP, UDP, OSPF, and FRAGMENT.
		"""
		try :
			return self._ipv6nextheadererr
		except Exception as e:
			raise e

	@property
	def ipv6toticmptx(self) :
		ur"""Number of ICMPv6 packets transmitted by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmptx
		except Exception as e:
			raise e

	@property
	def ipv6toticmpnstx(self) :
		ur"""Number of ICMPv6 NS packets transmitted by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmpnstx
		except Exception as e:
			raise e

	@property
	def ipv6fragudpreassembledrate(self) :
		ur"""Rate (/s) counter for ipv6fragtotudpreassembled.
		"""
		try :
			return self._ipv6fragudpreassembledrate
		except Exception as e:
			raise e

	@property
	def ipv6txbytesrate(self) :
		ur"""Rate (/s) counter for ipv6tottxbytes.
		"""
		try :
			return self._ipv6txbytesrate
		except Exception as e:
			raise e

	@property
	def icmpv6error(self) :
		ur"""Number of erroneous ICMPv6 packets received (OBSOLETE).
		"""
		try :
			return self._icmpv6error
		except Exception as e:
			raise e

	@property
	def ipv6toticmprarx(self) :
		ur"""Number of ICMPv6 RA packets received by NetScaler (OBSOLETE).
		"""
		try :
			return self._ipv6toticmprarx
		except Exception as e:
			raise e

	@property
	def ipv6tottxbytes(self) :
		ur"""Bytes of IPv6 data transmitted.
		"""
		try :
			return self._ipv6tottxbytes
		except Exception as e:
			raise e

	@property
	def ipv6landattack(self) :
		ur"""Land-attack packets received. The source and destination addresses are the same. If not dropped, these packets can lock up the appliance.
		"""
		try :
			return self._ipv6landattack
		except Exception as e:
			raise e

	@property
	def ipv6fragtotpktsforward(self) :
		ur"""IPv6 fragments forwarded to the client or server without reassembly.
		"""
		try :
			return self._ipv6fragtotpktsforward
		except Exception as e:
			raise e

	@property
	def ipv6fragzerolenpkt(self) :
		ur"""Packets received with a fragment length of 0 bytes.
		"""
		try :
			return self._ipv6fragzerolenpkt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolipv6_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolipv6
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all protocolipv6_stats resources that are configured on netscaler.
		"""
		try :
			obj = protocolipv6_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolipv6_response(base_response) :
	def __init__(self, length=1) :
		self.protocolipv6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolipv6 = [protocolipv6_stats() for _ in range(length)]

