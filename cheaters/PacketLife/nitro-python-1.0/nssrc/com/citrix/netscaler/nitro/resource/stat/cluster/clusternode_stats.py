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

class clusternode_stats(base_resource) :
	ur""" Statistics for cluster node resource.
	"""
	def __init__(self) :
		self._nodeid = 0
		self._clearstats = ""
		self._clsyncstate = ""
		self._clnodeeffectivehealth = ""
		self._clnodeip = ""
		self._clmasterstate = ""
		self._cltothbtx = 0
		self._cltothbrx = 0
		self._nnmcurconn = 0
		self._nnmtotconntx = 0
		self._nnmtotconnrx = 0
		self._clptpstate = ""
		self._clptptx = 0
		self._clptprx = 0
		self._nnmerrmsend = 0

	@property
	def nodeid(self) :
		ur"""ID of the cluster node for which to display statistics. If an ID is not provided, statistics are shown for all nodes.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		ur"""ID of the cluster node for which to display statistics. If an ID is not provided, statistics are shown for all nodes.
		"""
		try :
			self._nodeid = nodeid
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
	def clnodeip(self) :
		ur"""NSIP address of the cluster node.
		"""
		try :
			return self._clnodeip
		except Exception as e:
			raise e

	@property
	def clsyncstate(self) :
		ur"""Sync state of the cluster node.
		"""
		try :
			return self._clsyncstate
		except Exception as e:
			raise e

	@property
	def nnmcurconn(self) :
		ur"""Number of connections open for node-to-node communication.
		"""
		try :
			return self._nnmcurconn
		except Exception as e:
			raise e

	@property
	def nnmerrmsend(self) :
		ur"""Number of errors in sending node-to-node multicast/broadcast messages. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows a value of 0. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._nnmerrmsend
		except Exception as e:
			raise e

	@property
	def clnodeeffectivehealth(self) :
		ur"""Health of the cluster node.
		"""
		try :
			return self._clnodeeffectivehealth
		except Exception as e:
			raise e

	@property
	def nnmtotconnrx(self) :
		ur"""Number of node-to-node messages received. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows a value of 0. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._nnmtotconnrx
		except Exception as e:
			raise e

	@property
	def cltothbrx(self) :
		ur"""Number of heartbeats received. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows a value of 0. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._cltothbrx
		except Exception as e:
			raise e

	@property
	def clptprx(self) :
		ur"""Number of PTP packets received on the node. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows a value of 0. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._clptprx
		except Exception as e:
			raise e

	@property
	def nnmtotconntx(self) :
		ur"""Number of node-to-node messages sent. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows a value of 0. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._nnmtotconntx
		except Exception as e:
			raise e

	@property
	def clmasterstate(self) :
		ur"""Operational state of the cluster node.
		"""
		try :
			return self._clmasterstate
		except Exception as e:
			raise e

	@property
	def clptptx(self) :
		ur"""Number of PTP packets transmitted by the node. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows a value of 0. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._clptptx
		except Exception as e:
			raise e

	@property
	def clptpstate(self) :
		ur"""PTP state of the node. This state is Master for one node and Slave for the rest. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows UNKNOWN. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._clptpstate
		except Exception as e:
			raise e

	@property
	def cltothbtx(self) :
		ur"""Number of heartbeats sent. When executed from the NSIP address, shows the statistics for local node only. For remote node it shows a value of 0. When executed from the cluster IP address, shows all the statistics.
		"""
		try :
			return self._cltothbtx
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusternode_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusternode
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.nodeid is not None :
				return str(self.nodeid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all clusternode_stats resources that are configured on netscaler.
		"""
		try :
			obj = clusternode_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.nodeid = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class clusternode_response(base_response) :
	def __init__(self, length=1) :
		self.clusternode = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusternode = [clusternode_stats() for _ in range(length)]

