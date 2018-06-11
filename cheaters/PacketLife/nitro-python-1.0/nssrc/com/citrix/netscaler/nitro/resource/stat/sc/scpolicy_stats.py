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

class scpolicy_stats(base_resource) :
	ur""" Statistics for SureConnect policy resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._avgservertransactiontime = 0
		self._avgservertransactiontimerate = 0
		self._scaverageclientttlb = 0
		self._scaverageclientttlbrate = 0
		self._scphysicalserviceip = ""
		self._scphysicalserviceport = 0
		self._sccurrentclientconnections = 0
		self._sccurrentclientconnectionsrate = 0
		self._sccurrentwaitingclients = 0
		self._sccurrentwaitingclientsrate = 0
		self._totopenconn = 0
		self._openconnrate = 0
		self._sccurrentwaitingtime = 0
		self._sccurrentwaitingtimerate = 0
		self._sctotalclientconnections = 0
		self._scclientconnectionsrate = 0
		self._sctotalserverconnections = 0
		self._scserverconnectionsrate = 0
		self._totclienttransaction = 0
		self._clienttransactionrate = 0
		self._sctotalservertransactions = 0
		self._scservertransactionsrate = 0
		self._sctotalrequestsreceived = 0
		self._screquestsreceivedrate = 0
		self._sctotalrequestbytes = 0
		self._screquestbytesrate = 0
		self._sctotalresponsesreceived = 0
		self._scresponsesreceivedrate = 0
		self._sctotalresponsebytes = 0
		self._scresponsebytesrate = 0

	@property
	def name(self) :
		ur"""Name of the policy about which to display statistics. To display statistics about all SureConnect policies, do not set this parameter.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the policy about which to display statistics. To display statistics about all SureConnect policies, do not set this parameter.
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
	def scaverageclientttlb(self) :
		ur"""Average value of the client Time-To-Last-Byte in seconds for this SureConnect policy.
		"""
		try :
			return self._scaverageclientttlb
		except Exception as e:
			raise e

	@property
	def sctotalresponsesreceived(self) :
		ur"""Total number of server responses received by this SureConnect policy.
		"""
		try :
			return self._sctotalresponsesreceived
		except Exception as e:
			raise e

	@property
	def avgservertransactiontime(self) :
		ur"""Average server transaction time in seconds for this SureConnect Policy.
		"""
		try :
			return self._avgservertransactiontime
		except Exception as e:
			raise e

	@property
	def scphysicalserviceip(self) :
		ur"""IP address of the service in dotted notation for which these statistics are maintained.
		"""
		try :
			return self._scphysicalserviceip
		except Exception as e:
			raise e

	@property
	def sccurrentwaitingtime(self) :
		ur"""Value of the currently estimated waiting time in seconds for the configured URL.
		"""
		try :
			return self._sccurrentwaitingtime
		except Exception as e:
			raise e

	@property
	def sccurrentclientconnectionsrate(self) :
		ur"""Rate (/s) counter for sccurrentclientconnections.
		"""
		try :
			return self._sccurrentclientconnectionsrate
		except Exception as e:
			raise e

	@property
	def sccurrentclientconnections(self) :
		ur"""Number of clients currently  allowed a server connection by this SureConnect policy.
		"""
		try :
			return self._sccurrentclientconnections
		except Exception as e:
			raise e

	@property
	def openconnrate(self) :
		ur"""Rate (/s) counter for totopenconn.
		"""
		try :
			return self._openconnrate
		except Exception as e:
			raise e

	@property
	def clienttransactionrate(self) :
		ur"""Rate (/s) counter for totclienttransaction.
		"""
		try :
			return self._clienttransactionrate
		except Exception as e:
			raise e

	@property
	def sccurrentwaitingtimerate(self) :
		ur"""Rate (/s) counter for sccurrentwaitingtime.
		"""
		try :
			return self._sccurrentwaitingtimerate
		except Exception as e:
			raise e

	@property
	def sccurrentwaitingclients(self) :
		ur"""Current number of SureConnect priority clients that are waiting for a server connection.
		"""
		try :
			return self._sccurrentwaitingclients
		except Exception as e:
			raise e

	@property
	def scclientconnectionsrate(self) :
		ur"""Rate (/s) counter for sctotalclientconnections.
		"""
		try :
			return self._scclientconnectionsrate
		except Exception as e:
			raise e

	@property
	def scaverageclientttlbrate(self) :
		ur"""Rate (/s) counter for scaverageclientttlb.
		"""
		try :
			return self._scaverageclientttlbrate
		except Exception as e:
			raise e

	@property
	def totclienttransaction(self) :
		ur"""Total number of client transactions processed by this SureConnect policy.
		"""
		try :
			return self._totclienttransaction
		except Exception as e:
			raise e

	@property
	def scservertransactionsrate(self) :
		ur"""Rate (/s) counter for sctotalservertransactions.
		"""
		try :
			return self._scservertransactionsrate
		except Exception as e:
			raise e

	@property
	def sctotalrequestsreceived(self) :
		ur"""Total number of requests received by this SureConnect policy.
		"""
		try :
			return self._sctotalrequestsreceived
		except Exception as e:
			raise e

	@property
	def sctotalclientconnections(self) :
		ur"""Total number of clients that were allowed a server connection by this SureConnect policy.
		"""
		try :
			return self._sctotalclientconnections
		except Exception as e:
			raise e

	@property
	def screquestsreceivedrate(self) :
		ur"""Rate (/s) counter for sctotalrequestsreceived.
		"""
		try :
			return self._screquestsreceivedrate
		except Exception as e:
			raise e

	@property
	def scresponsebytesrate(self) :
		ur"""Rate (/s) counter for sctotalresponsebytes.
		"""
		try :
			return self._scresponsebytesrate
		except Exception as e:
			raise e

	@property
	def scphysicalserviceport(self) :
		ur"""Port of the service for which these statistics are maintained.
		"""
		try :
			return self._scphysicalserviceport
		except Exception as e:
			raise e

	@property
	def screquestbytesrate(self) :
		ur"""Rate (/s) counter for sctotalrequestbytes.
		"""
		try :
			return self._screquestbytesrate
		except Exception as e:
			raise e

	@property
	def sctotalresponsebytes(self) :
		ur"""Total number of response bytes received by this SureConnect policy.
		"""
		try :
			return self._sctotalresponsebytes
		except Exception as e:
			raise e

	@property
	def totopenconn(self) :
		ur"""Current number of open connections to the servers matching this policy.
		"""
		try :
			return self._totopenconn
		except Exception as e:
			raise e

	@property
	def avgservertransactiontimerate(self) :
		ur"""Rate (/s) counter for avgservertransactiontime.
		"""
		try :
			return self._avgservertransactiontimerate
		except Exception as e:
			raise e

	@property
	def scresponsesreceivedrate(self) :
		ur"""Rate (/s) counter for sctotalresponsesreceived.
		"""
		try :
			return self._scresponsesreceivedrate
		except Exception as e:
			raise e

	@property
	def sctotalrequestbytes(self) :
		ur"""Total number of request bytes received by this SureConnect policy.
		"""
		try :
			return self._sctotalrequestbytes
		except Exception as e:
			raise e

	@property
	def scserverconnectionsrate(self) :
		ur"""Rate (/s) counter for sctotalserverconnections.
		"""
		try :
			return self._scserverconnectionsrate
		except Exception as e:
			raise e

	@property
	def sctotalserverconnections(self) :
		ur"""Total number of server connections that were established through this SureConnect policy.
		"""
		try :
			return self._sctotalserverconnections
		except Exception as e:
			raise e

	@property
	def sctotalservertransactions(self) :
		ur"""Number of 200 OK responses received from the web server by this SureConnect policy.
		"""
		try :
			return self._sctotalservertransactions
		except Exception as e:
			raise e

	@property
	def sccurrentwaitingclientsrate(self) :
		ur"""Rate (/s) counter for sccurrentwaitingclients.
		"""
		try :
			return self._sccurrentwaitingclientsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(scpolicy_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.scpolicy
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
		ur""" Use this API to fetch the statistics of all scpolicy_stats resources that are configured on netscaler.
		"""
		try :
			obj = scpolicy_stats()
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

class scpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.scpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.scpolicy = [scpolicy_stats() for _ in range(length)]

