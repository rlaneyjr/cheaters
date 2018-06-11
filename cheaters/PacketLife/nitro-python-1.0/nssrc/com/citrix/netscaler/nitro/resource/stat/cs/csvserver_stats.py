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

class csvserver_stats(base_resource) :
	ur""" Statistics for CS virtual server resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._establishedconn = 0
		self._primaryipaddress = ""
		self._primaryport = 0
		self._type = ""
		self._state = ""
		self._tothits = 0
		self._hitsrate = 0
		self._totalrequests = 0
		self._requestsrate = 0
		self._totalresponses = 0
		self._responsesrate = 0
		self._totalrequestbytes = 0
		self._requestbytesrate = 0
		self._totalresponsebytes = 0
		self._responsebytesrate = 0
		self._totalpktsrecvd = 0
		self._pktsrecvdrate = 0
		self._totalpktssent = 0
		self._pktssentrate = 0
		self._curclntconnections = 0
		self._cursrvrconnections = 0
		self._sothreshold = 0
		self._totspillovers = 0
		self._labelledconn = 0
		self._pushlabel = 0
		self._deferredreq = 0
		self._deferredreqrate = 0
		self._invalidrequestresponse = 0
		self._invalidrequestresponsedropped = 0

	@property
	def name(self) :
		ur"""Name of the content switching virtual server for which to display statistics. To display statistics for all configured Content Switching virtual servers, do not specify a value for this parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the content switching virtual server for which to display statistics. To display statistics for all configured Content Switching virtual servers, do not specify a value for this parameter.
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
	def curclntconnections(self) :
		ur"""Number of current client connections.
		"""
		try :
			return self._curclntconnections
		except Exception as e:
			raise e

	@property
	def establishedconn(self) :
		ur"""Number of client connections in ESTABLISHED state.
		"""
		try :
			return self._establishedconn
		except Exception as e:
			raise e

	@property
	def totalpktssent(self) :
		ur"""Total number of packets sent.
		"""
		try :
			return self._totalpktssent
		except Exception as e:
			raise e

	@property
	def labelledconn(self) :
		ur"""Number of Labeled connection on this vserver.
		"""
		try :
			return self._labelledconn
		except Exception as e:
			raise e

	@property
	def tothits(self) :
		ur"""Total vserver hits.
		"""
		try :
			return self._tothits
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
	def sothreshold(self) :
		ur"""Spill Over Threshold set on the VServer.
		"""
		try :
			return self._sothreshold
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
	def invalidrequestresponsedropped(self) :
		ur"""Number invalid requests/responses dropped on this vserver.
		"""
		try :
			return self._invalidrequestresponsedropped
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
	def type(self) :
		ur"""Protocol associated with the vserver.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def hitsrate(self) :
		ur"""Rate (/s) counter for tothits.
		"""
		try :
			return self._hitsrate
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
	def pktsrecvdrate(self) :
		ur"""Rate (/s) counter for totalpktsrecvd.
		"""
		try :
			return self._pktsrecvdrate
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
	def pushlabel(self) :
		ur"""Number of labels for this push vserver.
		"""
		try :
			return self._pushlabel
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
	def deferredreq(self) :
		ur"""Number of deferred request on this vserver.
		"""
		try :
			return self._deferredreq
		except Exception as e:
			raise e

	@property
	def totspillovers(self) :
		ur"""Number of times vserver experienced spill over.
		"""
		try :
			return self._totspillovers
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
	def invalidrequestresponse(self) :
		ur"""Number invalid requests/responses on this vserver.
		"""
		try :
			return self._invalidrequestresponse
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
	def deferredreqrate(self) :
		ur"""Rate (/s) counter for deferredreq.
		"""
		try :
			return self._deferredreqrate
		except Exception as e:
			raise e

	@property
	def totalpktsrecvd(self) :
		ur"""Total number of packets received by this service or virtual server.
		"""
		try :
			return self._totalpktsrecvd
		except Exception as e:
			raise e

	@property
	def pktssentrate(self) :
		ur"""Rate (/s) counter for totalpktssent.
		"""
		try :
			return self._pktssentrate
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

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(csvserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.csvserver
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
		ur""" Use this API to fetch the statistics of all csvserver_stats resources that are configured on netscaler.
		"""
		try :
			obj = csvserver_stats()
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

class csvserver_response(base_response) :
	def __init__(self, length=1) :
		self.csvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.csvserver = [csvserver_stats() for _ in range(length)]

