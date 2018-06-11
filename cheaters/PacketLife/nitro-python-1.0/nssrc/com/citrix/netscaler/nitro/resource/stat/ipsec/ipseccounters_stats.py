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

class ipseccounters_stats(base_resource) :
	ur""" Statistics for counters resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._ipsectotrxbytes = 0
		self._ipsecrxbytesrate = 0
		self._ipsectottxbytes = 0
		self._ipsectxbytesrate = 0
		self._ipsectotrxpkts = 0
		self._ipsecrxpktsrate = 0
		self._ipsectottxpkts = 0
		self._ipsectxpktsrate = 0

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
	def ipsecrxbytesrate(self) :
		ur"""Rate (/s) counter for ipsectotrxbytes.
		"""
		try :
			return self._ipsecrxbytesrate
		except Exception as e:
			raise e

	@property
	def ipsectxbytesrate(self) :
		ur"""Rate (/s) counter for ipsectottxbytes.
		"""
		try :
			return self._ipsectxbytesrate
		except Exception as e:
			raise e

	@property
	def ipsectottxbytes(self) :
		ur"""Bytes sent during IPsec sessions.
		"""
		try :
			return self._ipsectottxbytes
		except Exception as e:
			raise e

	@property
	def ipsecrxpktsrate(self) :
		ur"""Rate (/s) counter for ipsectotrxpkts.
		"""
		try :
			return self._ipsecrxpktsrate
		except Exception as e:
			raise e

	@property
	def ipsectotrxpkts(self) :
		ur"""Packets received during IPsec sessions.
		"""
		try :
			return self._ipsectotrxpkts
		except Exception as e:
			raise e

	@property
	def ipsectottxpkts(self) :
		ur"""Packets sent during IPsec sessions.
		"""
		try :
			return self._ipsectottxpkts
		except Exception as e:
			raise e

	@property
	def ipsectotrxbytes(self) :
		ur"""Bytes received during IPsec sessions.
		"""
		try :
			return self._ipsectotrxbytes
		except Exception as e:
			raise e

	@property
	def ipsectxpktsrate(self) :
		ur"""Rate (/s) counter for ipsectottxpkts.
		"""
		try :
			return self._ipsectxpktsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ipseccounters_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipseccounters
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
		ur""" Use this API to fetch the statistics of all ipseccounters_stats resources that are configured on netscaler.
		"""
		try :
			obj = ipseccounters_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class ipseccounters_response(base_response) :
	def __init__(self, length=1) :
		self.ipseccounters = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ipseccounters = [ipseccounters_stats() for _ in range(length)]

