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

class inat_stats(base_resource) :
	ur""" Statistics for inbound nat resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._nat46tottcp46 = 0
		self._nat46tcp46rate = 0
		self._nat46totudp46 = 0
		self._nat46udp46rate = 0
		self._nat46toticmp46 = 0
		self._nat46icmp46rate = 0
		self._nat46totdrop46 = 0
		self._nat46drop46rate = 0
		self._nat46tottcp64 = 0
		self._nat46tcp64rate = 0
		self._nat46totudp64 = 0
		self._nat46udp64rate = 0
		self._nat46toticmp64 = 0
		self._nat46icmp64rate = 0
		self._nat46totdrop64 = 0
		self._nat46drop64rate = 0
		self._inatnat46tcp46 = 0
		self._inatnat46tcp46rate = 0
		self._inatnat46udp46 = 0
		self._inatnat46udp46rate = 0
		self._inatnat46icmp46 = 0
		self._inatnat46icmp46rate = 0
		self._inatnat46drop46 = 0
		self._inatnat46drop46rate = 0
		self._inatnat46tcp64 = 0
		self._inatnat46tcp64rate = 0
		self._inatnat46udp64 = 0
		self._inatnat46udp64rate = 0
		self._inatnat46icmp64 = 0
		self._inatnat46icmp64rate = 0
		self._inatnat46drop64 = 0
		self._inatnat46drop64rate = 0

	@property
	def name(self) :
		ur"""The INAT.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The INAT.
		"""
		try :
			self._name = name
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
	def nat46udp64rate(self) :
		ur"""Rate (/s) counter for nat46totudp64.
		"""
		try :
			return self._nat46udp64rate
		except Exception as e:
			raise e

	@property
	def nat46totdrop64(self) :
		ur"""Total IPV6 packets dropped.
		"""
		try :
			return self._nat46totdrop64
		except Exception as e:
			raise e

	@property
	def nat46totudp46(self) :
		ur"""Total UDP packets translated (V4->v6).
		"""
		try :
			return self._nat46totudp46
		except Exception as e:
			raise e

	@property
	def nat46icmp64rate(self) :
		ur"""Rate (/s) counter for nat46toticmp64.
		"""
		try :
			return self._nat46icmp64rate
		except Exception as e:
			raise e

	@property
	def inatnat46tcp46(self) :
		ur"""TCP packets translated (V4->v6).
		"""
		try :
			return self._inatnat46tcp46
		except Exception as e:
			raise e

	@property
	def nat46totdrop46(self) :
		ur"""Total IPV4 packets dropped.
		"""
		try :
			return self._nat46totdrop46
		except Exception as e:
			raise e

	@property
	def inatnat46tcp64(self) :
		ur"""TCP packets translated (V6->v4).
		"""
		try :
			return self._inatnat46tcp64
		except Exception as e:
			raise e

	@property
	def inatnat46drop46(self) :
		ur"""IPV4 packets dropped.
		"""
		try :
			return self._inatnat46drop46
		except Exception as e:
			raise e

	@property
	def inatnat46drop64(self) :
		ur"""IPV6 packets dropped.
		"""
		try :
			return self._inatnat46drop64
		except Exception as e:
			raise e

	@property
	def inatnat46udp46(self) :
		ur"""UDP packets translated (V4->v6).
		"""
		try :
			return self._inatnat46udp46
		except Exception as e:
			raise e

	@property
	def nat46tottcp64(self) :
		ur"""Total TCP packets translated (V6->v4).
		"""
		try :
			return self._nat46tottcp64
		except Exception as e:
			raise e

	@property
	def nat46drop46rate(self) :
		ur"""Rate (/s) counter for nat46totdrop46.
		"""
		try :
			return self._nat46drop46rate
		except Exception as e:
			raise e

	@property
	def inatnat46drop46rate(self) :
		ur"""Rate (/s) counter for inatnat46drop46.
		"""
		try :
			return self._inatnat46drop46rate
		except Exception as e:
			raise e

	@property
	def inatnat46tcp64rate(self) :
		ur"""Rate (/s) counter for inatnat46tcp64.
		"""
		try :
			return self._inatnat46tcp64rate
		except Exception as e:
			raise e

	@property
	def inatnat46icmp64(self) :
		ur"""ICMP packets translated (V6->v4).
		"""
		try :
			return self._inatnat46icmp64
		except Exception as e:
			raise e

	@property
	def nat46drop64rate(self) :
		ur"""Rate (/s) counter for nat46totdrop64.
		"""
		try :
			return self._nat46drop64rate
		except Exception as e:
			raise e

	@property
	def inatnat46tcp46rate(self) :
		ur"""Rate (/s) counter for inatnat46tcp46.
		"""
		try :
			return self._inatnat46tcp46rate
		except Exception as e:
			raise e

	@property
	def nat46tottcp46(self) :
		ur"""Total TCP packets translated (V4->v6).
		"""
		try :
			return self._nat46tottcp46
		except Exception as e:
			raise e

	@property
	def nat46toticmp46(self) :
		ur"""Total ICMP packets translated (V4->v6).
		"""
		try :
			return self._nat46toticmp46
		except Exception as e:
			raise e

	@property
	def inatnat46icmp46rate(self) :
		ur"""Rate (/s) counter for inatnat46icmp46.
		"""
		try :
			return self._inatnat46icmp46rate
		except Exception as e:
			raise e

	@property
	def inatnat46udp64(self) :
		ur"""UDP packets translated (V6->v4).
		"""
		try :
			return self._inatnat46udp64
		except Exception as e:
			raise e

	@property
	def nat46tcp46rate(self) :
		ur"""Rate (/s) counter for nat46tottcp46.
		"""
		try :
			return self._nat46tcp46rate
		except Exception as e:
			raise e

	@property
	def inatnat46drop64rate(self) :
		ur"""Rate (/s) counter for inatnat46drop64.
		"""
		try :
			return self._inatnat46drop64rate
		except Exception as e:
			raise e

	@property
	def inatnat46udp64rate(self) :
		ur"""Rate (/s) counter for inatnat46udp64.
		"""
		try :
			return self._inatnat46udp64rate
		except Exception as e:
			raise e

	@property
	def nat46icmp46rate(self) :
		ur"""Rate (/s) counter for nat46toticmp46.
		"""
		try :
			return self._nat46icmp46rate
		except Exception as e:
			raise e

	@property
	def inatnat46icmp46(self) :
		ur"""ICMP packets translated (V4->v6).
		"""
		try :
			return self._inatnat46icmp46
		except Exception as e:
			raise e

	@property
	def inatnat46icmp64rate(self) :
		ur"""Rate (/s) counter for inatnat46icmp64.
		"""
		try :
			return self._inatnat46icmp64rate
		except Exception as e:
			raise e

	@property
	def nat46tcp64rate(self) :
		ur"""Rate (/s) counter for nat46tottcp64.
		"""
		try :
			return self._nat46tcp64rate
		except Exception as e:
			raise e

	@property
	def nat46totudp64(self) :
		ur"""Total UDP packets translated (V6->v4).
		"""
		try :
			return self._nat46totudp64
		except Exception as e:
			raise e

	@property
	def nat46udp46rate(self) :
		ur"""Rate (/s) counter for nat46totudp46.
		"""
		try :
			return self._nat46udp46rate
		except Exception as e:
			raise e

	@property
	def nat46toticmp64(self) :
		ur"""Total ICMP packets translated (V6->v4).
		"""
		try :
			return self._nat46toticmp64
		except Exception as e:
			raise e

	@property
	def inatnat46udp46rate(self) :
		ur"""Rate (/s) counter for inatnat46udp46.
		"""
		try :
			return self._inatnat46udp46rate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(inat_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.inat
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all inat_stats resources that are configured on netscaler.
		"""
		try :
			obj = inat_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class inat_response(base_response) :
	def __init__(self, length=1) :
		self.inat = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.inat = [inat_stats() for _ in range(length)]

