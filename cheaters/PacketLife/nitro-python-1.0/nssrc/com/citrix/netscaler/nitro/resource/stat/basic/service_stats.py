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

class service_stats(base_resource) :
	ur""" Statistics for service resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._throughput = 0
		self._throughputrate = 0
		self._avgsvrttfb = 0
		self._primaryipaddress = ""
		self._primaryport = 0
		self._servicetype = ""
		self._state = ""
		self._totalrequests = 0
		self._requestsrate = 0
		self._totalresponses = 0
		self._responsesrate = 0
		self._totalrequestbytes = 0
		self._requestbytesrate = 0
		self._totalresponsebytes = 0
		self._responsebytesrate = 0
		self._curclntconnections = 0
		self._surgecount = 0
		self._cursrvrconnections = 0
		self._svrestablishedconn = 0
		self._curreusepool = 0
		self._maxclients = 0
		self._curload = 0
		self._curtflags = 0
		self._vsvrservicehits = 0
		self._vsvrservicehitsrate = 0
		self._activetransactions = 0

	@property
	def name(self) :
		ur"""Name of the service.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the service.
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
	def svrestablishedconn(self) :
		ur"""Number of server connections in ESTABLISHED state.
		"""
		try :
			return self._svrestablishedconn
		except Exception as e:
			raise e

	@property
	def curclntconnections(self) :
		ur"""Number of current client connections.
		"""
		try :
			return self._curclntconnections
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		ur"""The service type of this service.Possible values are ADNS, DNS, MYSQL, RTSP, SSL_DIAMETER, ADNS_TCP, DNS_TCP, NNTP, SIP_UDP, SSL_TCP, ANY, FTP, RADIUS, SNMP, TCP, DHCPRA, HTTP, RDP, SSL, TFTP, DIAMETER, MSSQL, RPCSVR, SSL_BRIDGE, UDP.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@property
	def totalrequests(self) :
		ur"""Total number of requests received on this service or virtual server. (This applies to HTTP/SSL services and servers.).
		"""
		try :
			return self._totalrequests
		except Exception as e:
			raise e

	@property
	def surgecount(self) :
		ur"""Number of requests in the surge queue.
		"""
		try :
			return self._surgecount
		except Exception as e:
			raise e

	@property
	def responsebytesrate(self) :
		ur"""Rate (/s) counter for totalresponsebytes.
		"""
		try :
			return self._responsebytesrate
		except Exception as e:
			raise e

	@property
	def totalresponses(self) :
		ur"""Number of responses received on this service or virtual server. (This applies to HTTP/SSL services and servers.).
		"""
		try :
			return self._totalresponses
		except Exception as e:
			raise e

	@property
	def requestbytesrate(self) :
		ur"""Rate (/s) counter for totalrequestbytes.
		"""
		try :
			return self._requestbytesrate
		except Exception as e:
			raise e

	@property
	def throughput(self) :
		ur"""Number of bytes received or sent by this service (Mbps).
		"""
		try :
			return self._throughput
		except Exception as e:
			raise e

	@property
	def throughputrate(self) :
		ur"""Rate (/s) counter for throughput.
		"""
		try :
			return self._throughputrate
		except Exception as e:
			raise e

	@property
	def curtflags(self) :
		ur"""Current flags on the service for internal use in display handlers.
		"""
		try :
			return self._curtflags
		except Exception as e:
			raise e

	@property
	def cursrvrconnections(self) :
		ur"""Number of current connections to the actual servers behind the virtual server.
		"""
		try :
			return self._cursrvrconnections
		except Exception as e:
			raise e

	@property
	def primaryipaddress(self) :
		ur"""The IP address on which the service is running.
		"""
		try :
			return self._primaryipaddress
		except Exception as e:
			raise e

	@property
	def activetransactions(self) :
		ur"""Number of active transactions handled by this service. (Including those in the surge queue.)
		Active Transaction means number of transactions currently served by the server including those waiting in the SurgeQ.
		"""
		try :
			return self._activetransactions
		except Exception as e:
			raise e

	@property
	def responsesrate(self) :
		ur"""Rate (/s) counter for totalresponses.
		"""
		try :
			return self._responsesrate
		except Exception as e:
			raise e

	@property
	def maxclients(self) :
		ur"""Maximum open connections allowed on this service.
		"""
		try :
			return self._maxclients
		except Exception as e:
			raise e

	@property
	def avgsvrttfb(self) :
		ur"""Average TTFB between the NetScaler appliance and the server.TTFB is the time interval between sending the request packet to a service and receiving the first response from the service.
		"""
		try :
			return self._avgsvrttfb
		except Exception as e:
			raise e

	@property
	def curload(self) :
		ur"""Load on the service that is calculated from the bound load based monitor.
		"""
		try :
			return self._curload
		except Exception as e:
			raise e

	@property
	def totalrequestbytes(self) :
		ur"""Total number of request bytes received on this service or virtual server.
		"""
		try :
			return self._totalrequestbytes
		except Exception as e:
			raise e

	@property
	def curreusepool(self) :
		ur"""Number of requests in the idle queue/reuse pool.
		"""
		try :
			return self._curreusepool
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Current state of the server. Possible values are UP, DOWN, UNKNOWN, OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN(Down When going Out of Service).
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def vsvrservicehits(self) :
		ur"""Number of times that the service has been provided.
		"""
		try :
			return self._vsvrservicehits
		except Exception as e:
			raise e

	@property
	def totalresponsebytes(self) :
		ur"""Number of response bytes received by this service or virtual server.
		"""
		try :
			return self._totalresponsebytes
		except Exception as e:
			raise e

	@property
	def primaryport(self) :
		ur"""The port on which the service is running.
		"""
		try :
			return self._primaryport
		except Exception as e:
			raise e

	@property
	def requestsrate(self) :
		ur"""Rate (/s) counter for totalrequests.
		"""
		try :
			return self._requestsrate
		except Exception as e:
			raise e

	@property
	def vsvrservicehitsrate(self) :
		ur"""Rate (/s) counter for vsvrservicehits.
		"""
		try :
			return self._vsvrservicehitsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(service_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.service
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
		ur""" Use this API to fetch the statistics of all service_stats resources that are configured on netscaler.
		"""
		try :
			obj = service_stats()
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

class service_response(base_response) :
	def __init__(self, length=1) :
		self.service = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.service = [service_stats() for _ in range(length)]

