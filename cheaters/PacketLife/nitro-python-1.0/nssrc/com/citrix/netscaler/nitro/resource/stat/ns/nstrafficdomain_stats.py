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

class nstrafficdomain_stats(base_resource) :
	ur""" Statistics for Traffic Domain resource.
	"""
	def __init__(self) :
		self._td = 0
		self._clearstats = ""
		self._nstdtotrxpkts = 0
		self._nstdrxpktsrate = 0
		self._nstdtottxpkts = 0
		self._nstdtxpktsrate = 0
		self._nstdtotdroppedpkts = 0
		self._nstddroppedpktsrate = 0

	@property
	def td(self) :
		ur"""An integer specifying the Traffic Domain ID. Possible values: 1 through 4094.<br/>Minimum value =  1<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""An integer specifying the Traffic Domain ID. Possible values: 1 through 4094.
		"""
		try :
			self._td = td
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
	def nstdtotrxpkts(self) :
		ur"""Packets received on this TD.
		"""
		try :
			return self._nstdtotrxpkts
		except Exception as e:
			raise e

	@property
	def nstddroppedpktsrate(self) :
		ur"""Rate (/s) counter for nstdtotdroppedpkts.
		"""
		try :
			return self._nstddroppedpktsrate
		except Exception as e:
			raise e

	@property
	def nstdtotdroppedpkts(self) :
		ur"""Inbound packets dropped on this TD by reception.
		"""
		try :
			return self._nstdtotdroppedpkts
		except Exception as e:
			raise e

	@property
	def nstdrxpktsrate(self) :
		ur"""Rate (/s) counter for nstdtotrxpkts.
		"""
		try :
			return self._nstdrxpktsrate
		except Exception as e:
			raise e

	@property
	def nstdtottxpkts(self) :
		ur"""Packets transmitted from this TD.
		"""
		try :
			return self._nstdtottxpkts
		except Exception as e:
			raise e

	@property
	def nstdtxpktsrate(self) :
		ur"""Rate (/s) counter for nstdtottxpkts.
		"""
		try :
			return self._nstdtxpktsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstrafficdomain_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstrafficdomain
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.td is not None :
				return str(self.td)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all nstrafficdomain_stats resources that are configured on netscaler.
		"""
		try :
			obj = nstrafficdomain_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.td = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class nstrafficdomain_response(base_response) :
	def __init__(self, length=1) :
		self.nstrafficdomain = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstrafficdomain = [nstrafficdomain_stats() for _ in range(length)]

