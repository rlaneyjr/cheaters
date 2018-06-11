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

class dospolicy_stats(base_resource) :
	ur""" Statistics for DoS policy resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._doscurrentcltdetectrate = 0
		self._dosphysicalserviceip = ""
		self._dosphysicalserviceport = 0
		self._doscurrentqueuesize = 0
		self._doscurrentqueuesizerate = 0
		self._dostotjssent = 0
		self._dosjssentrate = 0
		self._dostotjsrefused = 0
		self._dosjsrefusedrate = 0
		self._dostotvalidclients = 0
		self._dosvalidclientsrate = 0
		self._dostotjsbytessent = 0
		self._dosjsbytessentrate = 0
		self._dostotnongetpostrequests = 0
		self._dosnongetpostrequestsrate = 0

	@property
	def name(self) :
		ur"""The name of the DoS protection policy whose statistics must be displayed. If a name is not provided, statistics of all the DoS protection policies are displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of the DoS protection policy whose statistics must be displayed. If a name is not provided, statistics of all the DoS protection policies are displayed.
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
	def dosjsrefusedrate(self) :
		ur"""Rate (/s) counter for dostotjsrefused.
		"""
		try :
			return self._dosjsrefusedrate
		except Exception as e:
			raise e

	@property
	def dosphysicalserviceip(self) :
		ur"""IP address of the service to which this policy is bound.
		"""
		try :
			return self._dosphysicalserviceip
		except Exception as e:
			raise e

	@property
	def dosnongetpostrequestsrate(self) :
		ur"""Rate (/s) counter for dostotnongetpostrequests.
		"""
		try :
			return self._dosnongetpostrequestsrate
		except Exception as e:
			raise e

	@property
	def dosjssentrate(self) :
		ur"""Rate (/s) counter for dostotjssent.
		"""
		try :
			return self._dosjssentrate
		except Exception as e:
			raise e

	@property
	def dosphysicalserviceport(self) :
		ur"""Port address of the service to which this policy is bound.
		"""
		try :
			return self._dosphysicalserviceport
		except Exception as e:
			raise e

	@property
	def dosjsbytessentrate(self) :
		ur"""Rate (/s) counter for dostotjsbytessent.
		"""
		try :
			return self._dosjsbytessentrate
		except Exception as e:
			raise e

	@property
	def doscurrentcltdetectrate(self) :
		ur"""Current ratio of JavaScript send rate to the server response rate (Client detect rate).
		"""
		try :
			return self._doscurrentcltdetectrate
		except Exception as e:
			raise e

	@property
	def dostotnongetpostrequests(self) :
		ur"""Number of non-GET and non-POST requests for which DOS JavaScript was sent.
		"""
		try :
			return self._dostotnongetpostrequests
		except Exception as e:
			raise e

	@property
	def dostotvalidclients(self) :
		ur"""Total number of valid DoS cookies received for this policy.
		"""
		try :
			return self._dostotvalidclients
		except Exception as e:
			raise e

	@property
	def dosvalidclientsrate(self) :
		ur"""Rate (/s) counter for dostotvalidclients.
		"""
		try :
			return self._dosvalidclientsrate
		except Exception as e:
			raise e

	@property
	def doscurrentqueuesizerate(self) :
		ur"""Rate (/s) counter for doscurrentqueuesize.
		"""
		try :
			return self._doscurrentqueuesizerate
		except Exception as e:
			raise e

	@property
	def dostotjsbytessent(self) :
		ur"""Total number of DoS JavaScript bytes sent for this policy.
		"""
		try :
			return self._dostotjsbytessent
		except Exception as e:
			raise e

	@property
	def dostotjssent(self) :
		ur"""Total number of DoS JavaScript transactions performed for this policy.
		"""
		try :
			return self._dostotjssent
		except Exception as e:
			raise e

	@property
	def dostotjsrefused(self) :
		ur"""Number of times the DoS JavaScript was not sent because the set JavaScript rate was not met for this policy.
		"""
		try :
			return self._dostotjsrefused
		except Exception as e:
			raise e

	@property
	def doscurrentqueuesize(self) :
		ur"""Current queue size of the server to which this policy is bound.
		"""
		try :
			return self._doscurrentqueuesize
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dospolicy_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dospolicy
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
		ur""" Use this API to fetch the statistics of all dospolicy_stats resources that are configured on netscaler.
		"""
		try :
			obj = dospolicy_stats()
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

class dospolicy_response(base_response) :
	def __init__(self, length=1) :
		self.dospolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dospolicy = [dospolicy_stats() for _ in range(length)]

