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

class bridge_stats(base_resource) :
	ur""" Statistics for bridge resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._tcptotbdgmacmoved = 0
		self._tcpbdgmacmovedrate = 0
		self._tcptotbdgcollisions = 0
		self._tcpbdgcollisionsrate = 0
		self._tcperrbdgmuted = 0
		self._tcperrbdgmutedrate = 0
		self._totbdgpkts = 0
		self._bdgpktsrate = 0
		self._totbdgmbits = 0
		self._bdgmbitsrate = 0

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
	def tcpbdgcollisionsrate(self) :
		ur"""Rate (/s) counter for tcptotbdgcollisions.
		"""
		try :
			return self._tcpbdgcollisionsrate
		except Exception as e:
			raise e

	@property
	def tcptotbdgcollisions(self) :
		ur"""The number of bridging table collisions.
		"""
		try :
			return self._tcptotbdgcollisions
		except Exception as e:
			raise e

	@property
	def bdgpktsrate(self) :
		ur"""Rate (/s) counter for totbdgpkts.
		"""
		try :
			return self._bdgpktsrate
		except Exception as e:
			raise e

	@property
	def totbdgmbits(self) :
		ur"""The total number of bridged Mbits.
		"""
		try :
			return self._totbdgmbits
		except Exception as e:
			raise e

	@property
	def tcperrbdgmutedrate(self) :
		ur"""Rate (/s) counter for tcperrbdgmuted.
		"""
		try :
			return self._tcperrbdgmutedrate
		except Exception as e:
			raise e

	@property
	def tcpbdgmacmovedrate(self) :
		ur"""Rate (/s) counter for tcptotbdgmacmoved.
		"""
		try :
			return self._tcpbdgmacmovedrate
		except Exception as e:
			raise e

	@property
	def bdgmbitsrate(self) :
		ur"""Rate (/s) counter for totbdgmbits.
		"""
		try :
			return self._bdgmbitsrate
		except Exception as e:
			raise e

	@property
	def totbdgpkts(self) :
		ur"""The total number of bridged packets.
		"""
		try :
			return self._totbdgpkts
		except Exception as e:
			raise e

	@property
	def tcperrbdgmuted(self) :
		ur"""The number of bridging related interface mutes.
		"""
		try :
			return self._tcperrbdgmuted
		except Exception as e:
			raise e

	@property
	def tcptotbdgmacmoved(self) :
		ur"""The number of times bridging registered MAC moved.
		"""
		try :
			return self._tcptotbdgmacmoved
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(bridge_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bridge
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
		ur""" Use this API to fetch the statistics of all bridge_stats resources that are configured on netscaler.
		"""
		try :
			obj = bridge_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class bridge_response(base_response) :
	def __init__(self, length=1) :
		self.bridge = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.bridge = [bridge_stats() for _ in range(length)]

