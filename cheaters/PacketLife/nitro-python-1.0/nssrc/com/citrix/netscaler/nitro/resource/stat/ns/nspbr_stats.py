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

class nspbr_stats(base_resource) :
	ur""" Statistics for Policy Based Routing(PBR) entry resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._pbrtotpktsallowed = 0
		self._pbrpktsallowedrate = 0
		self._pbrtotpktsdenied = 0
		self._pbrpktsdeniedrate = 0
		self._pbrtothits = 0
		self._pbrhitsrate = 0
		self._pbrtotmisses = 0
		self._pbrmissesrate = 0
		self._pbrperhits = 0
		self._pbrperhitsrate = 0

	@property
	def name(self) :
		ur"""Name of the PBR whose statistics you want the NetScaler appliance to display.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the PBR whose statistics you want the NetScaler appliance to display.
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
	def pbrpktsdeniedrate(self) :
		ur"""Rate (/s) counter for pbrtotpktsdenied.
		"""
		try :
			return self._pbrpktsdeniedrate
		except Exception as e:
			raise e

	@property
	def pbrmissesrate(self) :
		ur"""Rate (/s) counter for pbrtotmisses.
		"""
		try :
			return self._pbrmissesrate
		except Exception as e:
			raise e

	@property
	def pbrtothits(self) :
		ur"""Total packets that matched one of the configured PBR.
		"""
		try :
			return self._pbrtothits
		except Exception as e:
			raise e

	@property
	def pbrperhitsrate(self) :
		ur"""Rate (/s) counter for pbrperhits.
		"""
		try :
			return self._pbrperhitsrate
		except Exception as e:
			raise e

	@property
	def pbrhitsrate(self) :
		ur"""Rate (/s) counter for pbrtothits.
		"""
		try :
			return self._pbrhitsrate
		except Exception as e:
			raise e

	@property
	def pbrperhits(self) :
		ur"""Number of times the pbr was hit.
		"""
		try :
			return self._pbrperhits
		except Exception as e:
			raise e

	@property
	def pbrtotmisses(self) :
		ur"""Total packets that did not match any PBR.
		"""
		try :
			return self._pbrtotmisses
		except Exception as e:
			raise e

	@property
	def pbrtotpktsallowed(self) :
		ur"""Total packets that matched the PBR (Policy-Based Routes) with action ALLOW .
		"""
		try :
			return self._pbrtotpktsallowed
		except Exception as e:
			raise e

	@property
	def pbrtotpktsdenied(self) :
		ur"""Total packets that matched the PBR with action DENY .
		"""
		try :
			return self._pbrtotpktsdenied
		except Exception as e:
			raise e

	@property
	def pbrpktsallowedrate(self) :
		ur"""Rate (/s) counter for pbrtotpktsallowed.
		"""
		try :
			return self._pbrpktsallowedrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nspbr_response, response, self.__class__.__name__.replace('_stats',''))
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all nspbr_stats resources that are configured on netscaler.
		"""
		try :
			obj = nspbr_stats()
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

class nspbr_response(base_response) :
	def __init__(self, length=1) :
		self.nspbr = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nspbr = [nspbr_stats() for _ in range(length)]

