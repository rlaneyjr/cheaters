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

class pq_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._pqtotalpolicymatches = 0
		self._pqpolicymatchesrate = 0
		self._pqtotalthresholdfailed = 0
		self._pqthresholdfailedrate = 0
		self._pqpriority1requests = 0
		self._pqpriority1requestsrate = 0
		self._pqpriority2requests = 0
		self._pqpriority2requestsrate = 0
		self._pqpriority3requests = 0
		self._pqpriority3requestsrate = 0

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
	def pqpriority2requestsrate(self) :
		ur"""Rate (/s) counter for pqpriority2requests.
		"""
		try :
			return self._pqpriority2requestsrate
		except Exception as e:
			raise e

	@property
	def pqpolicymatchesrate(self) :
		ur"""Rate (/s) counter for pqtotalpolicymatches.
		"""
		try :
			return self._pqpolicymatchesrate
		except Exception as e:
			raise e

	@property
	def pqpriority1requestsrate(self) :
		ur"""Rate (/s) counter for pqpriority1requests.
		"""
		try :
			return self._pqpriority1requestsrate
		except Exception as e:
			raise e

	@property
	def pqthresholdfailedrate(self) :
		ur"""Rate (/s) counter for pqtotalthresholdfailed.
		"""
		try :
			return self._pqthresholdfailedrate
		except Exception as e:
			raise e

	@property
	def pqtotalpolicymatches(self) :
		ur"""Number of times the Netscaler appliance matched an incoming request using any priority queuing policy.
		"""
		try :
			return self._pqtotalpolicymatches
		except Exception as e:
			raise e

	@property
	def pqpriority1requests(self) :
		ur"""Number of priority 1 requests that the Netscaler appliance received.
		"""
		try :
			return self._pqpriority1requests
		except Exception as e:
			raise e

	@property
	def pqpriority3requestsrate(self) :
		ur"""Rate (/s) counter for pqpriority3requests.
		"""
		try :
			return self._pqpriority3requestsrate
		except Exception as e:
			raise e

	@property
	def pqpriority3requests(self) :
		ur"""Number of priority 3 requests that the Netscaler appliance received.
		"""
		try :
			return self._pqpriority3requests
		except Exception as e:
			raise e

	@property
	def pqpriority2requests(self) :
		ur"""Number of priority 2 requests that the Netscaler appliance received.
		"""
		try :
			return self._pqpriority2requests
		except Exception as e:
			raise e

	@property
	def pqtotalthresholdfailed(self) :
		ur"""Number of times the Netscaler appliance failed to match an incoming request to any of priority queing policy.
		"""
		try :
			return self._pqtotalthresholdfailed
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(pq_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pq
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
		ur""" Use this API to fetch the statistics of all pq_stats resources that are configured on netscaler.
		"""
		try :
			obj = pq_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class pq_response(base_response) :
	def __init__(self, length=1) :
		self.pq = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.pq = [pq_stats() for _ in range(length)]

