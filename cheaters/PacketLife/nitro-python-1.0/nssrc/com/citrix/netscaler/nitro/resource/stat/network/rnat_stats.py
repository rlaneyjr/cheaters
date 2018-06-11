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

class rnat_stats(base_resource) :
	ur""" Statistics for RNAT configured route resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._rnattotrxbytes = 0
		self._rnatrxbytesrate = 0
		self._rnattottxbytes = 0
		self._rnattxbytesrate = 0
		self._rnattotrxpkts = 0
		self._rnatrxpktsrate = 0
		self._rnattottxpkts = 0
		self._rnattxpktsrate = 0
		self._rnattottxsyn = 0
		self._rnattxsynrate = 0
		self._rnatcursessions = 0

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
	def rnattottxpkts(self) :
		ur"""Packets sent during RNAT sessions.
		"""
		try :
			return self._rnattottxpkts
		except Exception as e:
			raise e

	@property
	def rnatrxbytesrate(self) :
		ur"""Rate (/s) counter for rnattotrxbytes.
		"""
		try :
			return self._rnatrxbytesrate
		except Exception as e:
			raise e

	@property
	def rnattxsynrate(self) :
		ur"""Rate (/s) counter for rnattottxsyn.
		"""
		try :
			return self._rnattxsynrate
		except Exception as e:
			raise e

	@property
	def rnattxpktsrate(self) :
		ur"""Rate (/s) counter for rnattottxpkts.
		"""
		try :
			return self._rnattxpktsrate
		except Exception as e:
			raise e

	@property
	def rnattottxsyn(self) :
		ur"""Requests for connections sent during RNAT sessions.
		"""
		try :
			return self._rnattottxsyn
		except Exception as e:
			raise e

	@property
	def rnattxbytesrate(self) :
		ur"""Rate (/s) counter for rnattottxbytes.
		"""
		try :
			return self._rnattxbytesrate
		except Exception as e:
			raise e

	@property
	def rnatrxpktsrate(self) :
		ur"""Rate (/s) counter for rnattotrxpkts.
		"""
		try :
			return self._rnatrxpktsrate
		except Exception as e:
			raise e

	@property
	def rnatcursessions(self) :
		ur"""Currently active RNAT sessions.
		"""
		try :
			return self._rnatcursessions
		except Exception as e:
			raise e

	@property
	def rnattotrxpkts(self) :
		ur"""Packets received during RNAT sessions.
		"""
		try :
			return self._rnattotrxpkts
		except Exception as e:
			raise e

	@property
	def rnattotrxbytes(self) :
		ur"""Bytes received during RNAT sessions.
		"""
		try :
			return self._rnattotrxbytes
		except Exception as e:
			raise e

	@property
	def rnattottxbytes(self) :
		ur"""Bytes sent during RNAT sessions.
		"""
		try :
			return self._rnattottxbytes
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rnat_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rnat
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
		ur""" Use this API to fetch the statistics of all rnat_stats resources that are configured on netscaler.
		"""
		try :
			obj = rnat_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class rnat_response(base_response) :
	def __init__(self, length=1) :
		self.rnat = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rnat = [rnat_stats() for _ in range(length)]

