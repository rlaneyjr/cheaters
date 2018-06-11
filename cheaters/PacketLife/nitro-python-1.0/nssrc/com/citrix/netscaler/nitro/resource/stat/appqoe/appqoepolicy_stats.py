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

class appqoepolicy_stats(base_resource) :
	ur""" Statistics for AppQoS policy resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._qosavgserverttfb = 0
		self._qosavgserverttfbrate = 0
		self._qosavgserverttlb = 0
		self._qosavgserverttlbrate = 0
		self._qosavgclientttlb = 0
		self._qosavgclientttlbrate = 0
		self._totthroughput = 0
		self._throughputrate = 0
		self._totsvrlinkedto = 0
		self._svrlinkedtorate = 0
		self._totcltrequests = 0
		self._cltrequestsrate = 0
		self._totrequests = 0
		self._requestsrate = 0
		self._totrequestbytes = 0
		self._requestbytesrate = 0
		self._totresponse = 0
		self._responserate = 0
		self._totresponsebytes = 0
		self._responsebytesrate = 0
		self._totjssent = 0
		self._jssentrate = 0
		self._totjsbytessent = 0
		self._jsbytessentrate = 0
		self._pipolicyhits = 0
		self._pipolicyhitsrate = 0

	@property
	def name(self) :
		ur"""policyName.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""policyName
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
	def qosavgclientttlbrate(self) :
		ur"""Rate (/s) counter for qosavgclientttlb.
		"""
		try :
			return self._qosavgclientttlbrate
		except Exception as e:
			raise e

	@property
	def totjssent(self) :
		ur"""Total number of in-memory responses sent instead of expected responses through this AppQoE policy.
		"""
		try :
			return self._totjssent
		except Exception as e:
			raise e

	@property
	def responsebytesrate(self) :
		ur"""Rate (/s) counter for totresponsebytes.
		"""
		try :
			return self._responsebytesrate
		except Exception as e:
			raise e

	@property
	def cltrequestsrate(self) :
		ur"""Rate (/s) counter for totcltrequests.
		"""
		try :
			return self._cltrequestsrate
		except Exception as e:
			raise e

	@property
	def totthroughput(self) :
		ur"""Throughput in Kbps calculated on this AppQoE policy.
		"""
		try :
			return self._totthroughput
		except Exception as e:
			raise e

	@property
	def requestbytesrate(self) :
		ur"""Rate (/s) counter for totrequestbytes.
		"""
		try :
			return self._requestbytesrate
		except Exception as e:
			raise e

	@property
	def throughputrate(self) :
		ur"""Rate (/s) counter for totthroughput.
		"""
		try :
			return self._throughputrate
		except Exception as e:
			raise e

	@property
	def totjsbytessent(self) :
		ur"""Total bytes of in-memory responses sent through this AppQoE policy.
		"""
		try :
			return self._totjsbytessent
		except Exception as e:
			raise e

	@property
	def svrlinkedtorate(self) :
		ur"""Rate (/s) counter for totsvrlinkedto.
		"""
		try :
			return self._svrlinkedtorate
		except Exception as e:
			raise e

	@property
	def totsvrlinkedto(self) :
		ur"""Total number of server connections that were established through this AppQoE Policy.
		"""
		try :
			return self._totsvrlinkedto
		except Exception as e:
			raise e

	@property
	def totresponse(self) :
		ur"""Total number of responses received by this AppQoE policy.
		"""
		try :
			return self._totresponse
		except Exception as e:
			raise e

	@property
	def totresponsebytes(self) :
		ur"""Total number of response bytes received by this AppQoE policy.
		"""
		try :
			return self._totresponsebytes
		except Exception as e:
			raise e

	@property
	def qosavgserverttfb(self) :
		ur"""Average Server Time-To-First-Byte in milliseconds calculated for this AppQoE policy.
		"""
		try :
			return self._qosavgserverttfb
		except Exception as e:
			raise e

	@property
	def pipolicyhitsrate(self) :
		ur"""Rate (/s) counter for pipolicyhits.
		"""
		try :
			return self._pipolicyhitsrate
		except Exception as e:
			raise e

	@property
	def jssentrate(self) :
		ur"""Rate (/s) counter for totjssent.
		"""
		try :
			return self._jssentrate
		except Exception as e:
			raise e

	@property
	def qosavgserverttfbrate(self) :
		ur"""Rate (/s) counter for qosavgserverttfb.
		"""
		try :
			return self._qosavgserverttfbrate
		except Exception as e:
			raise e

	@property
	def pipolicyhits(self) :
		ur"""Number of hits on the policy.
		"""
		try :
			return self._pipolicyhits
		except Exception as e:
			raise e

	@property
	def qosavgclientttlb(self) :
		ur"""Average Client Time-To-Last-Byte in milliseconds calculated for this AppQoE policy.
		"""
		try :
			return self._qosavgclientttlb
		except Exception as e:
			raise e

	@property
	def jsbytessentrate(self) :
		ur"""Rate (/s) counter for totjsbytessent.
		"""
		try :
			return self._jsbytessentrate
		except Exception as e:
			raise e

	@property
	def totcltrequests(self) :
		ur"""Total number of client connections that were requested through this AppQoE Policy.
		"""
		try :
			return self._totcltrequests
		except Exception as e:
			raise e

	@property
	def totrequests(self) :
		ur"""Total number of requests that were requested through this AppQoE policy.
		"""
		try :
			return self._totrequests
		except Exception as e:
			raise e

	@property
	def qosavgserverttlbrate(self) :
		ur"""Rate (/s) counter for qosavgserverttlb.
		"""
		try :
			return self._qosavgserverttlbrate
		except Exception as e:
			raise e

	@property
	def responserate(self) :
		ur"""Rate (/s) counter for totresponse.
		"""
		try :
			return self._responserate
		except Exception as e:
			raise e

	@property
	def requestsrate(self) :
		ur"""Rate (/s) counter for totrequests.
		"""
		try :
			return self._requestsrate
		except Exception as e:
			raise e

	@property
	def totrequestbytes(self) :
		ur"""Total number of requests bytes that were requested through this AppQoE policy.
		"""
		try :
			return self._totrequestbytes
		except Exception as e:
			raise e

	@property
	def qosavgserverttlb(self) :
		ur"""Average Server Time-To-Last-Byte in milliseconds calculated for this AppQoE policy.
		"""
		try :
			return self._qosavgserverttlb
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appqoepolicy_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appqoepolicy
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
		ur""" Use this API to fetch the statistics of all appqoepolicy_stats resources that are configured on netscaler.
		"""
		try :
			obj = appqoepolicy_stats()
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

class appqoepolicy_response(base_response) :
	def __init__(self, length=1) :
		self.appqoepolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appqoepolicy = [appqoepolicy_stats() for _ in range(length)]

