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

class nat64_stats(base_resource) :
	ur""" Statistics for nat64 config resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._nat64tottcpsessions = 0
		self._nat64tcpsessionsrate = 0
		self._nat64totudpsessions = 0
		self._nat64udpsessionsrate = 0
		self._nat64toticmpsessions = 0
		self._nat64icmpsessionsrate = 0
		self._nat64totsessions = 0
		self._nat64sessionsrate = 0

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
	def nat64icmpsessionsrate(self) :
		ur"""Rate (/s) counter for nat64toticmpsessions.
		"""
		try :
			return self._nat64icmpsessionsrate
		except Exception as e:
			raise e

	@property
	def nat64toticmpsessions(self) :
		ur"""Total number of ICMP sessions created by NAT64.
		"""
		try :
			return self._nat64toticmpsessions
		except Exception as e:
			raise e

	@property
	def nat64sessionsrate(self) :
		ur"""Rate (/s) counter for nat64totsessions.
		"""
		try :
			return self._nat64sessionsrate
		except Exception as e:
			raise e

	@property
	def nat64totudpsessions(self) :
		ur"""Total number of UDP sessions created by NAT64.
		"""
		try :
			return self._nat64totudpsessions
		except Exception as e:
			raise e

	@property
	def nat64udpsessionsrate(self) :
		ur"""Rate (/s) counter for nat64totudpsessions.
		"""
		try :
			return self._nat64udpsessionsrate
		except Exception as e:
			raise e

	@property
	def nat64tottcpsessions(self) :
		ur"""Total number of TCP sessions created by NAT64.
		"""
		try :
			return self._nat64tottcpsessions
		except Exception as e:
			raise e

	@property
	def nat64totsessions(self) :
		ur"""Total number of sessions created by NAT64.
		"""
		try :
			return self._nat64totsessions
		except Exception as e:
			raise e

	@property
	def nat64tcpsessionsrate(self) :
		ur"""Rate (/s) counter for nat64tottcpsessions.
		"""
		try :
			return self._nat64tcpsessionsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nat64_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nat64
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
		ur""" Use this API to fetch the statistics of all nat64_stats resources that are configured on netscaler.
		"""
		try :
			obj = nat64_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class nat64_response(base_response) :
	def __init__(self, length=1) :
		self.nat64 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nat64 = [nat64_stats() for _ in range(length)]

