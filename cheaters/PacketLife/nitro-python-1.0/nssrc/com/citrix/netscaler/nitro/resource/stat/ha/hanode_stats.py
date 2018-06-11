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

class hanode_stats(base_resource) :
	ur""" Statistics for node resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._hacurstatus = ""
		self._hacurstate = ""
		self._hacurmasterstate = ""
		self._transtime = ""
		self._hatotpktrx = 0
		self._hapktrxrate = 0
		self._hatotpkttx = 0
		self._hapkttxrate = 0
		self._haerrproptimeout = 0
		self._haerrsyncfailure = 0

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
	def haerrsyncfailure(self) :
		ur"""Number of times the configuration of the primary and secondary nodes failed to synchronize since that last transition. A synchronization failure results in mismatched configuration. It can be caused by a mismatch in the Remote Procedural Call (RPC) password on the two nodes forming the high availability pair.
		"""
		try :
			return self._haerrsyncfailure
		except Exception as e:
			raise e

	@property
	def transtime(self) :
		ur"""Time when the last master state transition occurred. You can use this statistic for debugging.
		"""
		try :
			return self._transtime
		except Exception as e:
			raise e

	@property
	def hacurstatus(self) :
		ur"""Whether a NetScaler appliance is configured for high availability. Possible values are YES and NO. If the value is NO, the high availability statistics below are invalid.
		"""
		try :
			return self._hacurstatus
		except Exception as e:
			raise e

	@property
	def hacurmasterstate(self) :
		ur"""Indicates the high availability state of the node. Possible values are: 
		STAYSECONDARY - Indicates that the selected node remains the secondary node in a high availability setup. In this case a forced failover does not change the state but, instead, returns an appropriate error message. This is a configured value and not a statistic.
		PRIMARY - Indicates that the selected node is the primary node in a high availability setup. 
		SECONDARY - Indicates that the selected node is the secondary node in a high availability setup. 
		CLAIMING - Indicates that the secondary node is in the process of taking over as the primary node. This is the intermediate state in the transition of the secondary node to primary status. 
		FORCE CHANGE - Indicates that the secondary node is forcibly changing its status to primary due to a forced failover issued on the secondary node. .
		"""
		try :
			return self._hacurmasterstate
		except Exception as e:
			raise e

	@property
	def hatotpkttx(self) :
		ur"""Number of heartbeat packets sent to the peer node. Heartbeats are sent at regular intervals (default is 200 milliseconds) to determine the state of the peer node.
		"""
		try :
			return self._hatotpkttx
		except Exception as e:
			raise e

	@property
	def hapktrxrate(self) :
		ur"""Rate (/s) counter for hatotpktrx.
		"""
		try :
			return self._hapktrxrate
		except Exception as e:
			raise e

	@property
	def haerrproptimeout(self) :
		ur"""Number of times propagation timed out.
		"""
		try :
			return self._haerrproptimeout
		except Exception as e:
			raise e

	@property
	def hapkttxrate(self) :
		ur"""Rate (/s) counter for hatotpkttx.
		"""
		try :
			return self._hapkttxrate
		except Exception as e:
			raise e

	@property
	def hacurstate(self) :
		ur"""State of the HA node, based on its health, in a high availability setup. Possible values are: 
		UP - Indicates that the node is accessible and can function as either a primary or secondary node.
		DISABLED - Indicates that the high availability status of the node has been manually disabled. Synchronization and propagation cannot take place between the peer nodes.
		INIT - Indicates that the node is in the process of becoming part of the high availability configuration. 
		PARTIALFAIL - Indicates that one of the high availability monitored interfaces has failed because of a card or link failure. This state triggers a failover.
		COMPLETEFAIL - Indicates that all the interfaces of the node are unusable, because the interfaces on which high availability monitoring is enabled are not connected or are manually disabled. This state triggers a failover.
		DUMB - Indicates that the node is in listening mode. It does not participate in high availability transitions or transfer configuration from the peer node. This is a configured value, not a statistic.
		PARTIALFAILSSL - Indicates that the SSL card has failed. This state triggers a failover.
		ROUTEMONITORFAIL - Indicates that the route monitor has failed. This state triggers a failover.
		"""
		try :
			return self._hacurstate
		except Exception as e:
			raise e

	@property
	def hatotpktrx(self) :
		ur"""Number of heartbeat packets received from the peer node. Heartbeats are sent at regular intervals (default is 200 milliseconds) to determine the state of the peer node.
		"""
		try :
			return self._hatotpktrx
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(hanode_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.hanode
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
		ur""" Use this API to fetch the statistics of all hanode_stats resources that are configured on netscaler.
		"""
		try :
			obj = hanode_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class hanode_response(base_response) :
	def __init__(self, length=1) :
		self.hanode = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.hanode = [hanode_stats() for _ in range(length)]

