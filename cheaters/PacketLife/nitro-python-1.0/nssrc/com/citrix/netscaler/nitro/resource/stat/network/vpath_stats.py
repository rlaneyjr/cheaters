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

class vpath_stats(base_resource) :
	ur""" Statistics for Vpath resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._vpathtotl2datarx = 0
		self._vpathl2datarxrate = 0
		self._vpathtotl3datarx = 0
		self._vpathl3datarxrate = 0
		self._vpathtotl2cntrlpkts = 0
		self._vpathl2cntrlpktsrate = 0
		self._vpathtotl3cntrlpkts = 0
		self._vpathl3cntrlpktsrate = 0
		self._vpathtotfragpkts = 0
		self._vpathfragpktsrate = 0
		self._vpathtotl2encappkts = 0
		self._vpathl2encappktsrate = 0
		self._vpathtotl3encappkts = 0
		self._vpathl3encappktsrate = 0
		self._vpathtotfragencappkts = 0
		self._vpathfragencappktsrate = 0
		self._vpathtotoffload = 0
		self._vpathoffloadrate = 0

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
	def vpathfragencappktsrate(self) :
		ur"""Rate (/s) counter for vpathtotfragencappkts.
		"""
		try :
			return self._vpathfragencappktsrate
		except Exception as e:
			raise e

	@property
	def vpathtotl2cntrlpkts(self) :
		ur"""Total number of vPath control packets received in L2 adjacency.
		"""
		try :
			return self._vpathtotl2cntrlpkts
		except Exception as e:
			raise e

	@property
	def vpathtotoffload(self) :
		ur"""Number of offloaded vPath packets transmitted.
		"""
		try :
			return self._vpathtotoffload
		except Exception as e:
			raise e

	@property
	def vpathtotl3encappkts(self) :
		ur"""Total number of L3 vPath encapsulated packets injected to VEM.
		"""
		try :
			return self._vpathtotl3encappkts
		except Exception as e:
			raise e

	@property
	def vpathtotl2datarx(self) :
		ur"""Total number of non-fragmented vPath data packets decapsulated in L2 adjacency.
		"""
		try :
			return self._vpathtotl2datarx
		except Exception as e:
			raise e

	@property
	def vpathtotl2encappkts(self) :
		ur"""Total number of L2 vPath encapsulated packets injected to VEM.
		"""
		try :
			return self._vpathtotl2encappkts
		except Exception as e:
			raise e

	@property
	def vpathoffloadrate(self) :
		ur"""Rate (/s) counter for vpathtotoffload.
		"""
		try :
			return self._vpathoffloadrate
		except Exception as e:
			raise e

	@property
	def vpathl3cntrlpktsrate(self) :
		ur"""Rate (/s) counter for vpathtotl3cntrlpkts.
		"""
		try :
			return self._vpathl3cntrlpktsrate
		except Exception as e:
			raise e

	@property
	def vpathfragpktsrate(self) :
		ur"""Rate (/s) counter for vpathtotfragpkts.
		"""
		try :
			return self._vpathfragpktsrate
		except Exception as e:
			raise e

	@property
	def vpathtotl3datarx(self) :
		ur"""Total number of non-fragmented vPath data packets decapsulated in L3 adjacency.
		"""
		try :
			return self._vpathtotl3datarx
		except Exception as e:
			raise e

	@property
	def vpathtotl3cntrlpkts(self) :
		ur"""Total number of vPath control packets received in L3 adjacency.
		"""
		try :
			return self._vpathtotl3cntrlpkts
		except Exception as e:
			raise e

	@property
	def vpathtotfragencappkts(self) :
		ur"""Number of fragmented vPath packets transmitted.
		"""
		try :
			return self._vpathtotfragencappkts
		except Exception as e:
			raise e

	@property
	def vpathl3encappktsrate(self) :
		ur"""Rate (/s) counter for vpathtotl3encappkts.
		"""
		try :
			return self._vpathl3encappktsrate
		except Exception as e:
			raise e

	@property
	def vpathl2encappktsrate(self) :
		ur"""Rate (/s) counter for vpathtotl2encappkts.
		"""
		try :
			return self._vpathl2encappktsrate
		except Exception as e:
			raise e

	@property
	def vpathl2cntrlpktsrate(self) :
		ur"""Rate (/s) counter for vpathtotl2cntrlpkts.
		"""
		try :
			return self._vpathl2cntrlpktsrate
		except Exception as e:
			raise e

	@property
	def vpathl3datarxrate(self) :
		ur"""Rate (/s) counter for vpathtotl3datarx.
		"""
		try :
			return self._vpathl3datarxrate
		except Exception as e:
			raise e

	@property
	def vpathl2datarxrate(self) :
		ur"""Rate (/s) counter for vpathtotl2datarx.
		"""
		try :
			return self._vpathl2datarxrate
		except Exception as e:
			raise e

	@property
	def vpathtotfragpkts(self) :
		ur"""Total number of vPath fragments received.
		"""
		try :
			return self._vpathtotfragpkts
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpath_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpath
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
		ur""" Use this API to fetch the statistics of all vpath_stats resources that are configured on netscaler.
		"""
		try :
			obj = vpath_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class vpath_response(base_response) :
	def __init__(self, length=1) :
		self.vpath = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpath = [vpath_stats() for _ in range(length)]

