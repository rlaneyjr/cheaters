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

class pqpolicy_stats(base_resource) :
	ur""" Statistics for PQ policy resource.
	"""
	def __init__(self) :
		self._policyname = ""
		self._clearstats = ""
		self._pqtotavgqueuewaittime = 0
		self._pqavgqueuewaittimerate = 0
		self._pqavgclienttransactiontimems = 0
		self._pqavgclienttransactiontimemsrate = 0
		self._pqvserverip = ""
		self._pqvserverport = 0
		self._pqqdepth = 0
		self._pqqdepthrate = 0
		self._pqcurrentclientconnections = 0
		self._pqcurrentclientconnectionsrate = 0
		self._pqtotclientconnections = 0
		self._pqclientconnectionsrate = 0
		self._pqdropped = 0
		self._pqdroppedrate = 0
		self._totclienttransactions = 0
		self._clienttransactionsrate = 0
		self._pqtotqueuedepth = 0
		self._pqqueuedepthrate = 0

	@property
	def policyname(self) :
		ur"""Name of the priority queuing policy whose statistics must be displayed. If a name is not provided, statistics of all priority queuing policies are shown.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name of the priority queuing policy whose statistics must be displayed. If a name is not provided, statistics of all priority queuing policies are shown.
		"""
		try :
			self._policyname = policyname
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
	def pqvserverip(self) :
		ur"""IP address of the virtual server to which this priority queuing policy is bound.
		"""
		try :
			return self._pqvserverip
		except Exception as e:
			raise e

	@property
	def pqqueuedepthrate(self) :
		ur"""Rate (/s) counter for pqtotqueuedepth.
		"""
		try :
			return self._pqqueuedepthrate
		except Exception as e:
			raise e

	@property
	def pqdroppedrate(self) :
		ur"""Rate (/s) counter for pqdropped.
		"""
		try :
			return self._pqdroppedrate
		except Exception as e:
			raise e

	@property
	def pqtotqueuedepth(self) :
		ur"""Total number of waiting clients for this priority queuing policy.
		"""
		try :
			return self._pqtotqueuedepth
		except Exception as e:
			raise e

	@property
	def pqvserverport(self) :
		ur"""Port number of the virtual server to which this priority queuing policy is bound.
		"""
		try :
			return self._pqvserverport
		except Exception as e:
			raise e

	@property
	def totclienttransactions(self) :
		ur"""Total number of client transactions for this priority queuing policy.
		"""
		try :
			return self._totclienttransactions
		except Exception as e:
			raise e

	@property
	def clienttransactionsrate(self) :
		ur"""Rate (/s) counter for totclienttransactions.
		"""
		try :
			return self._clienttransactionsrate
		except Exception as e:
			raise e

	@property
	def pqcurrentclientconnectionsrate(self) :
		ur"""Rate (/s) counter for pqcurrentclientconnections.
		"""
		try :
			return self._pqcurrentclientconnectionsrate
		except Exception as e:
			raise e

	@property
	def pqqdepthrate(self) :
		ur"""Rate (/s) counter for pqqdepth.
		"""
		try :
			return self._pqqdepthrate
		except Exception as e:
			raise e

	@property
	def pqqdepth(self) :
		ur"""Number of clients waiting currently for this priority queuing policy.
		"""
		try :
			return self._pqqdepth
		except Exception as e:
			raise e

	@property
	def pqclientconnectionsrate(self) :
		ur"""Rate (/s) counter for pqtotclientconnections.
		"""
		try :
			return self._pqclientconnectionsrate
		except Exception as e:
			raise e

	@property
	def pqavgclienttransactiontimems(self) :
		ur"""Average time taken by a priority queuing client to complete its transaction for this  priority queuing policy.
		"""
		try :
			return self._pqavgclienttransactiontimems
		except Exception as e:
			raise e

	@property
	def pqavgclienttransactiontimemsrate(self) :
		ur"""Rate (/s) counter for pqavgclienttransactiontimems.
		"""
		try :
			return self._pqavgclienttransactiontimemsrate
		except Exception as e:
			raise e

	@property
	def pqtotavgqueuewaittime(self) :
		ur"""Average wait time for clients for this priority queuing policy.
		"""
		try :
			return self._pqtotavgqueuewaittime
		except Exception as e:
			raise e

	@property
	def pqdropped(self) :
		ur"""Total number of dropped transactions for this priority queuing policy.
		"""
		try :
			return self._pqdropped
		except Exception as e:
			raise e

	@property
	def pqtotclientconnections(self) :
		ur"""Total number of server connections established for serving clients for this priority queuing policy.
		"""
		try :
			return self._pqtotclientconnections
		except Exception as e:
			raise e

	@property
	def pqavgqueuewaittimerate(self) :
		ur"""Rate (/s) counter for pqtotavgqueuewaittime.
		"""
		try :
			return self._pqavgqueuewaittimerate
		except Exception as e:
			raise e

	@property
	def pqcurrentclientconnections(self) :
		ur"""Current number of server connections established for serving clients for this priority queuing policy.
		"""
		try :
			return self._pqcurrentclientconnections
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(pqpolicy_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pqpolicy
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all pqpolicy_stats resources that are configured on netscaler.
		"""
		try :
			obj = pqpolicy_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.policyname = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class pqpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.pqpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.pqpolicy = [pqpolicy_stats() for _ in range(length)]

