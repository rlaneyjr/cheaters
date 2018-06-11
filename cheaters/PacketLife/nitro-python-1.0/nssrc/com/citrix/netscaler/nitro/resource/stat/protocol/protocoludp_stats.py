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

class protocoludp_stats(base_resource) :
	ur""" Statistics for UDP Protocol resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._udptotrxpkts = 0
		self._udprxpktsrate = 0
		self._udptotrxbytes = 0
		self._udprxbytesrate = 0
		self._udptottxpkts = 0
		self._udptxpktsrate = 0
		self._udptottxbytes = 0
		self._udptxbytesrate = 0
		self._udpcurratethreshold = 0
		self._udptotunknownsvcpkts = 0
		self._udpbadchecksum = 0
		self._udpcurratethresholdexceeds = 0

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
	def udptxpktsrate(self) :
		ur"""Rate (/s) counter for udptottxpkts.
		"""
		try :
			return self._udptxpktsrate
		except Exception as e:
			raise e

	@property
	def udpcurratethreshold(self) :
		ur"""Limit for UDP packets handled every 10 milliseconds. Default value, 0, applies no limit.
		This is a configurable value using the set rateControl command.
		.
		"""
		try :
			return self._udpcurratethreshold
		except Exception as e:
			raise e

	@property
	def udptotrxpkts(self) :
		ur"""Total number of UDP packets received.
		"""
		try :
			return self._udptotrxpkts
		except Exception as e:
			raise e

	@property
	def udptottxpkts(self) :
		ur"""Total number of UDP packets transmitted.
		"""
		try :
			return self._udptottxpkts
		except Exception as e:
			raise e

	@property
	def udptotrxbytes(self) :
		ur"""Total number of UDP data received in bytes.
		"""
		try :
			return self._udptotrxbytes
		except Exception as e:
			raise e

	@property
	def udptxbytesrate(self) :
		ur"""Rate (/s) counter for udptottxbytes.
		"""
		try :
			return self._udptxbytesrate
		except Exception as e:
			raise e

	@property
	def udprxpktsrate(self) :
		ur"""Rate (/s) counter for udptotrxpkts.
		"""
		try :
			return self._udprxpktsrate
		except Exception as e:
			raise e

	@property
	def udpbadchecksum(self) :
		ur"""Packets received with a UDP checksum error.
		"""
		try :
			return self._udpbadchecksum
		except Exception as e:
			raise e

	@property
	def udptottxbytes(self) :
		ur"""Total number of UDP data transmitted in bytes.
		"""
		try :
			return self._udptottxbytes
		except Exception as e:
			raise e

	@property
	def udptotunknownsvcpkts(self) :
		ur"""Stray UDP packets dropped due to no configured listening  service.
		"""
		try :
			return self._udptotunknownsvcpkts
		except Exception as e:
			raise e

	@property
	def udprxbytesrate(self) :
		ur"""Rate (/s) counter for udptotrxbytes.
		"""
		try :
			return self._udprxbytesrate
		except Exception as e:
			raise e

	@property
	def udpcurratethresholdexceeds(self) :
		ur"""Number of times the UDP rate threshold is exceeded. If this counter continuously increases, first make sure the UDP packets received are genuine. 
		If they are, increase the current rate threshold. This is a configurable value using the set rateControl command.
		.
		"""
		try :
			return self._udpcurratethresholdexceeds
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocoludp_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocoludp
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
		ur""" Use this API to fetch the statistics of all protocoludp_stats resources that are configured on netscaler.
		"""
		try :
			obj = protocoludp_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocoludp_response(base_response) :
	def __init__(self, length=1) :
		self.protocoludp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocoludp = [protocoludp_stats() for _ in range(length)]

