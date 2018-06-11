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

class ns_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._rescpuusagepcnt = 0
		self._cpuusagepcnt = 0
		self._cachemaxmemorykb = 0
		self._delcmpratio = 0
		self._rescpuusage = 0
		self._cpuusage = 0
		self._resmemusage = 0
		self._comptotaldatacompressionratio = 0
		self._compratio = 0
		self._cacheutilizedmemorykb = 0
		self._cachemaxmemoryactivekb = 0
		self._cache64maxmemorykb = 0
		self._cachepercentoriginbandwidthsaved = 0
		self._cachetotmisses = 0
		self._cachemissesrate = 0
		self._cachetothits = 0
		self._cachehitsrate = 0
		self._sslnumcardsup = 0
		self._memusagepcnt = 0
		self._memuseinmb = 0
		self._mgmtcpuusagepcnt = 0
		self._pktcpuusagepcnt = 0
		self._starttime = ""
		self._transtime = ""
		self._hacurstate = ""
		self._hacurmasterstate = ""
		self._sslcards = 0
		self._disk0perusage = 0
		self._disk1perusage = 0
		self._disk0avail = 0
		self._disk1avail = 0
		self._totrxmbits = 0
		self._rxmbitsrate = 0
		self._tottxmbits = 0
		self._txmbitsrate = 0
		self._tcpcurclientconn = 0
		self._tcpcurclientconnestablished = 0
		self._tcpcurserverconn = 0
		self._tcpcurserverconnestablished = 0
		self._httptotrequests = 0
		self._httprequestsrate = 0
		self._httptotresponses = 0
		self._httpresponsesrate = 0
		self._httptotrxrequestbytes = 0
		self._httprxrequestbytesrate = 0
		self._httptotrxresponsebytes = 0
		self._httprxresponsebytesrate = 0
		self._ssltottransactions = 0
		self._ssltransactionsrate = 0
		self._ssltotsessionhits = 0
		self._sslsessionhitsrate = 0
		self._appfirewallrequests = 0
		self._appfirewallrequestsrate = 0
		self._appfirewallresponses = 0
		self._appfirewallresponsesrate = 0
		self._appfirewallaborts = 0
		self._appfirewallabortsrate = 0
		self._appfirewallredirects = 0
		self._appfirewallredirectsrate = 0
		self._misccounter0 = 0
		self._misccounter1 = 0
		self._numcpus = 0

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
	def cachehitsrate(self) :
		ur"""Rate (/s) counter for cachetothits.
		"""
		try :
			return self._cachehitsrate
		except Exception as e:
			raise e

	@property
	def appfirewallredirectsrate(self) :
		ur"""Rate (/s) counter for appfirewallredirects.
		"""
		try :
			return self._appfirewallredirectsrate
		except Exception as e:
			raise e

	@property
	def ssltottransactions(self) :
		ur"""Number of SSL transactions on the NetScaler appliance.
		"""
		try :
			return self._ssltottransactions
		except Exception as e:
			raise e

	@property
	def sslnumcardsup(self) :
		ur"""Number of SSL cards that are UP. If the number of cards UP is lower than a threshold, a failover is initiated.
		"""
		try :
			return self._sslnumcardsup
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
	def cacheutilizedmemorykb(self) :
		ur"""Amount of memory the integrated cache is currently using.
		"""
		try :
			return self._cacheutilizedmemorykb
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
	def httprxrequestbytesrate(self) :
		ur"""Rate (/s) counter for httptotrxrequestbytes.
		"""
		try :
			return self._httprxrequestbytesrate
		except Exception as e:
			raise e

	@property
	def httptotrxresponsebytes(self) :
		ur"""Total number of bytes of HTTP response data received.
		"""
		try :
			return self._httptotrxresponsebytes
		except Exception as e:
			raise e

	@property
	def disk1perusage(self) :
		ur"""Used space in /var partition of the disk, as a percentage. This is a critical counter. You can configure /var Used (%) by using the Set snmp alarm DISK-USAGE-HIGH command.
		"""
		try :
			return self._disk1perusage
		except Exception as e:
			raise e

	@property
	def rescpuusagepcnt(self) :
		ur"""Average CPU utilization percentage. Not applicable for a single-CPU system.
		"""
		try :
			return self._rescpuusagepcnt
		except Exception as e:
			raise e

	@property
	def appfirewallaborts(self) :
		ur"""Incomplete HTTP/HTTPS requests aborted by the client before the Application Firewall could finish processing them.
		"""
		try :
			return self._appfirewallaborts
		except Exception as e:
			raise e

	@property
	def disk1avail(self) :
		ur"""Available space in /var partition of the hard disk.
		"""
		try :
			return self._disk1avail
		except Exception as e:
			raise e

	@property
	def appfirewallresponsesrate(self) :
		ur"""Rate (/s) counter for appfirewallresponses.
		"""
		try :
			return self._appfirewallresponsesrate
		except Exception as e:
			raise e

	@property
	def tcpcurserverconnestablished(self) :
		ur"""Current server connections in the Established state, which indicates that data transfer can occur between the NetScaler and the server.
		"""
		try :
			return self._tcpcurserverconnestablished
		except Exception as e:
			raise e

	@property
	def delcmpratio(self) :
		ur"""Ratio of compressible data received to compressed data transmitted.If this ratio is one (uncmp:1.0) that means compression is disabled or we are not able to compress even a single compressible packet.
		"""
		try :
			return self._delcmpratio
		except Exception as e:
			raise e

	@property
	def appfirewallresponses(self) :
		ur"""HTTP/HTTPS responses sent by your protected web servers via the Application Firewall.
		"""
		try :
			return self._appfirewallresponses
		except Exception as e:
			raise e

	@property
	def tcpcurclientconn(self) :
		ur"""Client connections, including connections in the Opening, Established, and Closing state.
		"""
		try :
			return self._tcpcurclientconn
		except Exception as e:
			raise e

	@property
	def tcpcurserverconn(self) :
		ur"""Server connections, including connections in the Opening, Established, and Closing state.
		"""
		try :
			return self._tcpcurserverconn
		except Exception as e:
			raise e

	@property
	def rescpuusage(self) :
		ur"""Shows average CPU utilization percentage if more than 1 CPU is present.
		"""
		try :
			return self._rescpuusage
		except Exception as e:
			raise e

	@property
	def comptotaldatacompressionratio(self) :
		ur"""Ratio of total HTTP data received to total HTTP data transmitted.
		"""
		try :
			return self._comptotaldatacompressionratio
		except Exception as e:
			raise e

	@property
	def appfirewallrequests(self) :
		ur"""HTTP/HTTPS requests sent to your protected web servers via the Application Firewall.
		"""
		try :
			return self._appfirewallrequests
		except Exception as e:
			raise e

	@property
	def httprxresponsebytesrate(self) :
		ur"""Rate (/s) counter for httptotrxresponsebytes.
		"""
		try :
			return self._httprxresponsebytesrate
		except Exception as e:
			raise e

	@property
	def disk0perusage(self) :
		ur"""Used space in /flash partition of the disk, as a percentage. This is a critical counter.
		You can configure /flash Used (%) by using the Set snmp alarm DISK-USAGE-HIGH command.
		"""
		try :
			return self._disk0perusage
		except Exception as e:
			raise e

	@property
	def appfirewallabortsrate(self) :
		ur"""Rate (/s) counter for appfirewallaborts.
		"""
		try :
			return self._appfirewallabortsrate
		except Exception as e:
			raise e

	@property
	def appfirewallrequestsrate(self) :
		ur"""Rate (/s) counter for appfirewallrequests.
		"""
		try :
			return self._appfirewallrequestsrate
		except Exception as e:
			raise e

	@property
	def totrxmbits(self) :
		ur"""Number of megabytes received by the NetScaler appliance.
		"""
		try :
			return self._totrxmbits
		except Exception as e:
			raise e

	@property
	def tottxmbits(self) :
		ur"""Number of megabytes transmitted by the NetScaler appliance.
		"""
		try :
			return self._tottxmbits
		except Exception as e:
			raise e

	@property
	def ssltotsessionhits(self) :
		ur"""Number of SSL session reuse hits on the NetScaler appliance.
		"""
		try :
			return self._ssltotsessionhits
		except Exception as e:
			raise e

	@property
	def cachemissesrate(self) :
		ur"""Rate (/s) counter for cachetotmisses.
		"""
		try :
			return self._cachemissesrate
		except Exception as e:
			raise e

	@property
	def cachemaxmemorykb(self) :
		ur"""Largest amount of memory the NetScaler can dedicate to caching, up to 50% of available memory. A 0 value disables caching, but the caching module continues to run. .
		"""
		try :
			return self._cachemaxmemorykb
		except Exception as e:
			raise e

	@property
	def appfirewallredirects(self) :
		ur"""HTTP/HTTPS requests redirected by the Application Firewall to a different Web page or web server. (HTTP 302).
		"""
		try :
			return self._appfirewallredirects
		except Exception as e:
			raise e

	@property
	def mgmtcpuusagepcnt(self) :
		ur"""Management CPU utilization percentage.
		"""
		try :
			return self._mgmtcpuusagepcnt
		except Exception as e:
			raise e

	@property
	def cpuusage(self) :
		ur"""CPU utilization percentage.
		"""
		try :
			return self._cpuusage
		except Exception as e:
			raise e

	@property
	def httptotrequests(self) :
		ur"""Total number of HTTP requests received.
		"""
		try :
			return self._httptotrequests
		except Exception as e:
			raise e

	@property
	def httptotresponses(self) :
		ur"""Total number of HTTP responses sent.
		"""
		try :
			return self._httptotresponses
		except Exception as e:
			raise e

	@property
	def cachetothits(self) :
		ur"""Responses served from the integrated cache. These responses match a policy with a CACHE action.
		"""
		try :
			return self._cachetothits
		except Exception as e:
			raise e

	@property
	def misccounter1(self) :
		ur"""Miscellaneous Counter 1.
		"""
		try :
			return self._misccounter1
		except Exception as e:
			raise e

	@property
	def numcpus(self) :
		ur"""The number of CPUs on the NetScaler appliance.
		"""
		try :
			return self._numcpus
		except Exception as e:
			raise e

	@property
	def pktcpuusagepcnt(self) :
		ur"""Average CPU utilization percentage for all packet engines excluding management PE.
		"""
		try :
			return self._pktcpuusagepcnt
		except Exception as e:
			raise e

	@property
	def ssltransactionsrate(self) :
		ur"""Rate (/s) counter for ssltottransactions.
		"""
		try :
			return self._ssltransactionsrate
		except Exception as e:
			raise e

	@property
	def httprequestsrate(self) :
		ur"""Rate (/s) counter for httptotrequests.
		"""
		try :
			return self._httprequestsrate
		except Exception as e:
			raise e

	@property
	def cachemaxmemoryactivekb(self) :
		ur"""Currently active value of maximum memory.
		"""
		try :
			return self._cachemaxmemoryactivekb
		except Exception as e:
			raise e

	@property
	def httpresponsesrate(self) :
		ur"""Rate (/s) counter for httptotresponses.
		"""
		try :
			return self._httpresponsesrate
		except Exception as e:
			raise e

	@property
	def compratio(self) :
		ur"""Ratio of the compressible data received from the server to the compressed data sent to the client.
		"""
		try :
			return self._compratio
		except Exception as e:
			raise e

	@property
	def memuseinmb(self) :
		ur"""Main memory currently in use, in megabytes.
		"""
		try :
			return self._memuseinmb
		except Exception as e:
			raise e

	@property
	def disk0avail(self) :
		ur"""Available space in /flash partition of the hard disk.
		"""
		try :
			return self._disk0avail
		except Exception as e:
			raise e

	@property
	def txmbitsrate(self) :
		ur"""Rate (/s) counter for tottxmbits.
		"""
		try :
			return self._txmbitsrate
		except Exception as e:
			raise e

	@property
	def sslsessionhitsrate(self) :
		ur"""Rate (/s) counter for ssltotsessionhits.
		"""
		try :
			return self._sslsessionhitsrate
		except Exception as e:
			raise e

	@property
	def resmemusage(self) :
		ur"""Percentage of memory utilization on NetScaler.
		"""
		try :
			return self._resmemusage
		except Exception as e:
			raise e

	@property
	def sslcards(self) :
		ur"""Number of SSL crypto cards present on the NetScaler appliance.
		"""
		try :
			return self._sslcards
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
	def rxmbitsrate(self) :
		ur"""Rate (/s) counter for totrxmbits.
		"""
		try :
			return self._rxmbitsrate
		except Exception as e:
			raise e

	@property
	def cache64maxmemorykb(self) :
		ur"""Largest amount of memory the NetScaler can dedicate to caching, up to 50% of available memory. A 0 value disables caching, but the caching module continues to run. .
		"""
		try :
			return self._cache64maxmemorykb
		except Exception as e:
			raise e

	@property
	def starttime(self) :
		ur"""Time when the NetScaler appliance was last started.
		"""
		try :
			return self._starttime
		except Exception as e:
			raise e

	@property
	def tcpcurclientconnestablished(self) :
		ur"""Current client connections in the Established state, which indicates that data transfer can occur between the NetScaler and the client.
		"""
		try :
			return self._tcpcurclientconnestablished
		except Exception as e:
			raise e

	@property
	def cpuusagepcnt(self) :
		ur"""CPU utilization percentage.
		"""
		try :
			return self._cpuusagepcnt
		except Exception as e:
			raise e

	@property
	def cachepercentoriginbandwidthsaved(self) :
		ur"""Percentage of origin bandwidth saved, expressed as number of bytes served from the integrated cache divided by all bytes served. The assumption is that all compression is done in the NetScaler.
		"""
		try :
			return self._cachepercentoriginbandwidthsaved
		except Exception as e:
			raise e

	@property
	def misccounter0(self) :
		ur"""Miscellaneous Counter 0.
		"""
		try :
			return self._misccounter0
		except Exception as e:
			raise e

	@property
	def cachetotmisses(self) :
		ur"""Intercepted HTTP requests requiring fetches from origin server.
		"""
		try :
			return self._cachetotmisses
		except Exception as e:
			raise e

	@property
	def httptotrxrequestbytes(self) :
		ur"""Total number of bytes of HTTP request data received.
		"""
		try :
			return self._httptotrxrequestbytes
		except Exception as e:
			raise e

	@property
	def memusagepcnt(self) :
		ur"""Percentage of memory utilization on NetScaler.
		"""
		try :
			return self._memusagepcnt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ns_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns
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
		ur""" Use this API to fetch the statistics of all ns_stats resources that are configured on netscaler.
		"""
		try :
			obj = ns_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class ns_response(base_response) :
	def __init__(self, length=1) :
		self.ns = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ns = [ns_stats() for _ in range(length)]

