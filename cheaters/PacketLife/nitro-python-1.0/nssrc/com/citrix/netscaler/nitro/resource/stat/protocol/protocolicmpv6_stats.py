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

class protocolicmpv6_stats(base_resource) :
	ur""" Statistics for icmpv6 resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._icmpv6totrxpkts = 0
		self._icmpv6rxpktsrate = 0
		self._icmpv6totrxbytes = 0
		self._icmpv6rxbytesrate = 0
		self._icmpv6tottxpkts = 0
		self._icmpv6txpktsrate = 0
		self._icmpv6tottxbytes = 0
		self._icmpv6txbytesrate = 0
		self._icmpv6totrxna = 0
		self._icmpv6rxnarate = 0
		self._icmpv6totrxns = 0
		self._icmpv6rxnsrate = 0
		self._icmpv6totrxra = 0
		self._icmpv6rxrarate = 0
		self._icmpv6totrxrs = 0
		self._icmpv6rxrsrate = 0
		self._icmpv6totrxechoreq = 0
		self._icmpv6rxechoreqrate = 0
		self._icmpv6totrxechoreply = 0
		self._icmpv6rxechoreplyrate = 0
		self._icmpv6tottxna = 0
		self._icmpv6txnarate = 0
		self._icmpv6tottxns = 0
		self._icmpv6txnsrate = 0
		self._icmpv6tottxra = 0
		self._icmpv6txrarate = 0
		self._icmpv6tottxrs = 0
		self._icmpv6txrsrate = 0
		self._icmpv6tottxechoreq = 0
		self._icmpv6txechoreqrate = 0
		self._icmpv6tottxechoreply = 0
		self._icmpv6txechoreplyrate = 0
		self._icmpv6errra = 0
		self._icmpv6errna = 0
		self._icmpv6errns = 0
		self._icmpv6badchecksums = 0
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
	def icmpv6tottxns(self) :
		ur"""ICMPv6 neighbor solicitation packets transmitted. These packets are sent to get the link layer addresses of neighboring nodes or to confirm that they are reachable.
		"""
		try :
			return self._icmpv6tottxns
		except Exception as e:
			raise e

	@property
	def icmpv6txpktsrate(self) :
		ur"""Rate (/s) counter for icmpv6tottxpkts.
		"""
		try :
			return self._icmpv6txpktsrate
		except Exception as e:
			raise e

	@property
	def icmpv6unspt(self) :
		ur"""ICMPv6 packets received that are not supported by the NetScaler.
		"""
		try :
			return self._icmpv6unspt
		except Exception as e:
			raise e

	@property
	def icmpv6totrxechoreply(self) :
		ur"""ICMPv6 Ping Echo Reply packets received.
		"""
		try :
			return self._icmpv6totrxechoreply
		except Exception as e:
			raise e

	@property
	def icmpv6tottxra(self) :
		ur"""ICMPv6 router advertisement packets transmitted. These packets are sent at regular intervals or in response to a router solicitation packet from a neighbor.
		"""
		try :
			return self._icmpv6tottxra
		except Exception as e:
			raise e

	@property
	def icmpv6tottxechoreply(self) :
		ur"""ICMP Ping Echo Reply packets transmitted.
		"""
		try :
			return self._icmpv6tottxechoreply
		except Exception as e:
			raise e

	@property
	def icmpv6badchecksums(self) :
		ur"""Packets received with an ICMPv6 checksum error.
		"""
		try :
			return self._icmpv6badchecksums
		except Exception as e:
			raise e

	@property
	def icmpv6txnarate(self) :
		ur"""Rate (/s) counter for icmpv6tottxna.
		"""
		try :
			return self._icmpv6txnarate
		except Exception as e:
			raise e

	@property
	def icmpv6txrsrate(self) :
		ur"""Rate (/s) counter for icmpv6tottxrs.
		"""
		try :
			return self._icmpv6txrsrate
		except Exception as e:
			raise e

	@property
	def icmpv6tottxna(self) :
		ur"""ICMPv6 neighbor advertisement packets transmitted. These packets are sent in response to a neighbor solicitation packet, or if the link layer address of this node has changed.
		"""
		try :
			return self._icmpv6tottxna
		except Exception as e:
			raise e

	@property
	def icmpv6totrxra(self) :
		ur"""ICMPv6 router advertisement packets received. These are received at defined intervals or in response to a router solicitation message.
		"""
		try :
			return self._icmpv6totrxra
		except Exception as e:
			raise e

	@property
	def icmpv6tottxrs(self) :
		ur"""ICMPv6 router solicitation packets transmitted. These packets are sent to request neighboring routers to generate router advertisements immediately rather than wait for the next defined time.
		"""
		try :
			return self._icmpv6tottxrs
		except Exception as e:
			raise e

	@property
	def icmpv6rxpktsrate(self) :
		ur"""Rate (/s) counter for icmpv6totrxpkts.
		"""
		try :
			return self._icmpv6rxpktsrate
		except Exception as e:
			raise e

	@property
	def icmpv6totrxpkts(self) :
		ur"""ICMPv6 packets received.
		"""
		try :
			return self._icmpv6totrxpkts
		except Exception as e:
			raise e

	@property
	def icmpv6totrxns(self) :
		ur"""ICMPv6 neighbor solicitation packets received. These packets are received if the link layer address of a neighbor has changed, or in response to a neighbor solicitation message sent out by this node.
		"""
		try :
			return self._icmpv6totrxns
		except Exception as e:
			raise e

	@property
	def icmpv6rxechoreplyrate(self) :
		ur"""Rate (/s) counter for icmpv6totrxechoreply.
		"""
		try :
			return self._icmpv6rxechoreplyrate
		except Exception as e:
			raise e

	@property
	def icmpv6txechoreqrate(self) :
		ur"""Rate (/s) counter for icmpv6tottxechoreq.
		"""
		try :
			return self._icmpv6txechoreqrate
		except Exception as e:
			raise e

	@property
	def icmpv6rxrsrate(self) :
		ur"""Rate (/s) counter for icmpv6totrxrs.
		"""
		try :
			return self._icmpv6rxrsrate
		except Exception as e:
			raise e

	@property
	def icmpv6errna(self) :
		ur"""ICMPv6 neighbor advertisement error packets received that contain an error in the header, such as an incorrect source IP address, destination IP address, or packet length.
		"""
		try :
			return self._icmpv6errna
		except Exception as e:
			raise e

	@property
	def icmpv6rxnsrate(self) :
		ur"""Rate (/s) counter for icmpv6totrxns.
		"""
		try :
			return self._icmpv6rxnsrate
		except Exception as e:
			raise e

	@property
	def icmpv6rxbytesrate(self) :
		ur"""Rate (/s) counter for icmpv6totrxbytes.
		"""
		try :
			return self._icmpv6rxbytesrate
		except Exception as e:
			raise e

	@property
	def icmpv6rtthsld(self) :
		ur"""Packets dropped because the default threshold of 100 requests per 10 milliseconds has been exceeded.
		This is a configurable value using the set rateControl command.
		"""
		try :
			return self._icmpv6rtthsld
		except Exception as e:
			raise e

	@property
	def icmpv6totrxrs(self) :
		ur"""ICMPv6 router solicitation packets received. These could be sent by a neighboring router to initiate address resolution.
		"""
		try :
			return self._icmpv6totrxrs
		except Exception as e:
			raise e

	@property
	def icmpv6totrxna(self) :
		ur"""ICMPv6 neighbor advertisement packets received. These packets are received in response to a neighbor solicitation message sent out by this node, or if the link layer address of a neighbor has changed.
		"""
		try :
			return self._icmpv6totrxna
		except Exception as e:
			raise e

	@property
	def icmpv6txechoreplyrate(self) :
		ur"""Rate (/s) counter for icmpv6tottxechoreply.
		"""
		try :
			return self._icmpv6txechoreplyrate
		except Exception as e:
			raise e

	@property
	def icmpv6totrxbytes(self) :
		ur"""Bytes of ICMPv6 data received.
		"""
		try :
			return self._icmpv6totrxbytes
		except Exception as e:
			raise e

	@property
	def icmpv6txrarate(self) :
		ur"""Rate (/s) counter for icmpv6tottxra.
		"""
		try :
			return self._icmpv6txrarate
		except Exception as e:
			raise e

	@property
	def icmpv6errns(self) :
		ur"""ICMPv6 neighbor solicitation error packets received that contain an error in the header, such as an incorrect source IP address, destination IP address, or packet length.
		"""
		try :
			return self._icmpv6errns
		except Exception as e:
			raise e

	@property
	def icmpv6totrxechoreq(self) :
		ur"""ICMPv6 Ping Echo Request packets received.
		"""
		try :
			return self._icmpv6totrxechoreq
		except Exception as e:
			raise e

	@property
	def icmpv6tottxechoreq(self) :
		ur"""ICMPv6 Ping Echo Request packets transmitted.
		"""
		try :
			return self._icmpv6tottxechoreq
		except Exception as e:
			raise e

	@property
	def icmpv6rxrarate(self) :
		ur"""Rate (/s) counter for icmpv6totrxra.
		"""
		try :
			return self._icmpv6rxrarate
		except Exception as e:
			raise e

	@property
	def icmpv6rxechoreqrate(self) :
		ur"""Rate (/s) counter for icmpv6totrxechoreq.
		"""
		try :
			return self._icmpv6rxechoreqrate
		except Exception as e:
			raise e

	@property
	def icmpv6tottxpkts(self) :
		ur"""ICMPv6 packets transmitted.
		"""
		try :
			return self._icmpv6tottxpkts
		except Exception as e:
			raise e

	@property
	def icmpv6tottxbytes(self) :
		ur"""Bytes of ICMPv6 data transmitted.
		"""
		try :
			return self._icmpv6tottxbytes
		except Exception as e:
			raise e

	@property
	def icmpv6rxnarate(self) :
		ur"""Rate (/s) counter for icmpv6totrxna.
		"""
		try :
			return self._icmpv6rxnarate
		except Exception as e:
			raise e

	@property
	def icmpv6txnsrate(self) :
		ur"""Rate (/s) counter for icmpv6tottxns.
		"""
		try :
			return self._icmpv6txnsrate
		except Exception as e:
			raise e

	@property
	def icmpv6errra(self) :
		ur"""ICMPv6 router advertisement error packets received that contain an error in the header, such as an incorrect source IP address, destination IP address, or packet length.
		"""
		try :
			return self._icmpv6errra
		except Exception as e:
			raise e

	@property
	def icmpv6txbytesrate(self) :
		ur"""Rate (/s) counter for icmpv6tottxbytes.
		"""
		try :
			return self._icmpv6txbytesrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolicmpv6_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolicmpv6
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
		ur""" Use this API to fetch the statistics of all protocolicmpv6_stats resources that are configured on netscaler.
		"""
		try :
			obj = protocolicmpv6_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolicmpv6_response(base_response) :
	def __init__(self, length=1) :
		self.protocolicmpv6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolicmpv6 = [protocolicmpv6_stats() for _ in range(length)]

