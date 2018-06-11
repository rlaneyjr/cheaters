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

class vpn_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._indexhtmlhit = 0
		self._indexhtmlnoserved = 0
		self._cfghtmlserved = 0
		self._cfghtmlservedrate = 0
		self._dnsreqhit = 0
		self._dnsreqhitrate = 0
		self._winsrequesthit = 0
		self._winsrequesthitrate = 0
		self._csrequesthit = 0
		self._csrequesthitrate = 0
		self._csnonhttpprobehit = 0
		self._csnonhttpprobehitrate = 0
		self._cshttpprobehit = 0
		self._cshttpprobehitrate = 0
		self._totalcsconnsucc = 0
		self._csconnsuccrate = 0
		self._totalfsrequest = 0
		self._fsrequestrate = 0
		self._iipdisabledmipused = 0
		self._iipdisabledmipusedrate = 0
		self._iipfailedmipused = 0
		self._iipfailedmipusedrate = 0
		self._iipspillovermipused = 0
		self._iipspillovermipusedrate = 0
		self._iipdisabledmipdisabled = 0
		self._iipdisabledmipdisabledrate = 0
		self._iipfailedmipdisabled = 0
		self._iipfailedmipdisabledrate = 0
		self._socksmethreqrcvd = 0
		self._socksmethreqrcvdrate = 0
		self._socksmethreqsent = 0
		self._socksmethreqsentrate = 0
		self._socksmethresprcvd = 0
		self._socksmethresprcvdrate = 0
		self._socksmethrespsent = 0
		self._socksmethrespsentrate = 0
		self._socksconnreqrcvd = 0
		self._socksconnreqrcvdrate = 0
		self._socksconnreqsent = 0
		self._socksconnreqsentrate = 0
		self._socksconnresprcvd = 0
		self._socksconnresprcvdrate = 0
		self._socksconnrespsent = 0
		self._socksconnrespsentrate = 0
		self._socksservererror = 0
		self._socksservererrorrate = 0
		self._socksclienterror = 0
		self._socksclienterrorrate = 0
		self._staconnsuccess = 0
		self._staconnsuccessrate = 0
		self._staconnfailure = 0
		self._staconnfailurerate = 0
		self._cpsconnsuccess = 0
		self._cpsconnsuccessrate = 0
		self._cpsconnfailure = 0
		self._cpsconnfailurerate = 0
		self._starequestsent = 0
		self._starequestsentrate = 0
		self._staresponserecvd = 0
		self._staresponserecvdrate = 0
		self._icalicensefailure = 0
		self._icalicensefailurerate = 0

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
	def staconnfailurerate(self) :
		ur"""Rate (/s) counter for staconnfailure.
		"""
		try :
			return self._staconnfailurerate
		except Exception as e:
			raise e

	@property
	def totalcsconnsucc(self) :
		ur"""Number of successful probes to all back-end servers.
		"""
		try :
			return self._totalcsconnsucc
		except Exception as e:
			raise e

	@property
	def csnonhttpprobehitrate(self) :
		ur"""Rate (/s) counter for csnonhttpprobehit.
		"""
		try :
			return self._csnonhttpprobehitrate
		except Exception as e:
			raise e

	@property
	def socksmethreqrcvd(self) :
		ur"""Number of received SOCKS method request.
		"""
		try :
			return self._socksmethreqrcvd
		except Exception as e:
			raise e

	@property
	def iipspillovermipusedrate(self) :
		ur"""Rate (/s) counter for iipspillovermipused.
		"""
		try :
			return self._iipspillovermipusedrate
		except Exception as e:
			raise e

	@property
	def iipfailedmipdisabled(self) :
		ur"""Number of times IIP assignment failed and MIP is disabled.
		"""
		try :
			return self._iipfailedmipdisabled
		except Exception as e:
			raise e

	@property
	def cshttpprobehitrate(self) :
		ur"""Rate (/s) counter for cshttpprobehit.
		"""
		try :
			return self._cshttpprobehitrate
		except Exception as e:
			raise e

	@property
	def socksconnrespsentrate(self) :
		ur"""Rate (/s) counter for socksconnrespsent.
		"""
		try :
			return self._socksconnrespsentrate
		except Exception as e:
			raise e

	@property
	def starequestsent(self) :
		ur"""Number of STA request sent.
		"""
		try :
			return self._starequestsent
		except Exception as e:
			raise e

	@property
	def socksservererrorrate(self) :
		ur"""Rate (/s) counter for socksservererror.
		"""
		try :
			return self._socksservererrorrate
		except Exception as e:
			raise e

	@property
	def winsrequesthitrate(self) :
		ur"""Rate (/s) counter for winsrequesthit.
		"""
		try :
			return self._winsrequesthitrate
		except Exception as e:
			raise e

	@property
	def socksservererror(self) :
		ur"""Number of SOCKS server error.
		"""
		try :
			return self._socksservererror
		except Exception as e:
			raise e

	@property
	def socksmethresprcvdrate(self) :
		ur"""Rate (/s) counter for socksmethresprcvd.
		"""
		try :
			return self._socksmethresprcvdrate
		except Exception as e:
			raise e

	@property
	def socksconnreqrcvd(self) :
		ur"""Number of received SOCKS connect request.
		"""
		try :
			return self._socksconnreqrcvd
		except Exception as e:
			raise e

	@property
	def totalfsrequest(self) :
		ur"""Number of file system requests received by VPN server.
		"""
		try :
			return self._totalfsrequest
		except Exception as e:
			raise e

	@property
	def socksmethreqrcvdrate(self) :
		ur"""Rate (/s) counter for socksmethreqrcvd.
		"""
		try :
			return self._socksmethreqrcvdrate
		except Exception as e:
			raise e

	@property
	def socksmethreqsentrate(self) :
		ur"""Rate (/s) counter for socksmethreqsent.
		"""
		try :
			return self._socksmethreqsentrate
		except Exception as e:
			raise e

	@property
	def cpsconnfailurerate(self) :
		ur"""Rate (/s) counter for cpsconnfailure.
		"""
		try :
			return self._cpsconnfailurerate
		except Exception as e:
			raise e

	@property
	def iipdisabledmipdisabled(self) :
		ur"""Both IIP and MIP is disabled.
		"""
		try :
			return self._iipdisabledmipdisabled
		except Exception as e:
			raise e

	@property
	def cshttpprobehit(self) :
		ur"""Number of probes from VPN to back-end HTTP servers that have been accessed by the VPN client.
		"""
		try :
			return self._cshttpprobehit
		except Exception as e:
			raise e

	@property
	def iipspillovermipused(self) :
		ur"""Number of times MIP is used on IIP Spillover.
		"""
		try :
			return self._iipspillovermipused
		except Exception as e:
			raise e

	@property
	def cpsconnsuccess(self) :
		ur"""Number of CPS connection success.
		"""
		try :
			return self._cpsconnsuccess
		except Exception as e:
			raise e

	@property
	def iipdisabledmipusedrate(self) :
		ur"""Rate (/s) counter for iipdisabledmipused.
		"""
		try :
			return self._iipdisabledmipusedrate
		except Exception as e:
			raise e

	@property
	def socksmethrespsentrate(self) :
		ur"""Rate (/s) counter for socksmethrespsent.
		"""
		try :
			return self._socksmethrespsentrate
		except Exception as e:
			raise e

	@property
	def socksmethreqsent(self) :
		ur"""Number of sent SOCKS method request.
		"""
		try :
			return self._socksmethreqsent
		except Exception as e:
			raise e

	@property
	def icalicensefailurerate(self) :
		ur"""Rate (/s) counter for icalicensefailure.
		"""
		try :
			return self._icalicensefailurerate
		except Exception as e:
			raise e

	@property
	def staconnfailure(self) :
		ur"""Number of STA connection failure.
		"""
		try :
			return self._staconnfailure
		except Exception as e:
			raise e

	@property
	def socksconnreqrcvdrate(self) :
		ur"""Rate (/s) counter for socksconnreqrcvd.
		"""
		try :
			return self._socksconnreqrcvdrate
		except Exception as e:
			raise e

	@property
	def socksclienterrorrate(self) :
		ur"""Rate (/s) counter for socksclienterror.
		"""
		try :
			return self._socksclienterrorrate
		except Exception as e:
			raise e

	@property
	def csrequesthit(self) :
		ur"""Number of SSL VPN tunnels formed between VPN server and client.
		"""
		try :
			return self._csrequesthit
		except Exception as e:
			raise e

	@property
	def winsrequesthit(self) :
		ur"""Number of WINS queries resolved by VPN server.
		"""
		try :
			return self._winsrequesthit
		except Exception as e:
			raise e

	@property
	def dnsreqhitrate(self) :
		ur"""Rate (/s) counter for dnsreqhit.
		"""
		try :
			return self._dnsreqhitrate
		except Exception as e:
			raise e

	@property
	def socksconnresprcvd(self) :
		ur"""Number of received SOCKS connect response.
		"""
		try :
			return self._socksconnresprcvd
		except Exception as e:
			raise e

	@property
	def socksmethrespsent(self) :
		ur"""Number of sent SOCKS method response.
		"""
		try :
			return self._socksmethrespsent
		except Exception as e:
			raise e

	@property
	def csconnsuccrate(self) :
		ur"""Rate (/s) counter for totalcsconnsucc.
		"""
		try :
			return self._csconnsuccrate
		except Exception as e:
			raise e

	@property
	def socksconnreqsent(self) :
		ur"""Number of sent SOCKS connect request.
		"""
		try :
			return self._socksconnreqsent
		except Exception as e:
			raise e

	@property
	def dnsreqhit(self) :
		ur"""Number of DNS queries resolved by VPN server.
		"""
		try :
			return self._dnsreqhit
		except Exception as e:
			raise e

	@property
	def staconnsuccessrate(self) :
		ur"""Rate (/s) counter for staconnsuccess.
		"""
		try :
			return self._staconnsuccessrate
		except Exception as e:
			raise e

	@property
	def iipfailedmipusedrate(self) :
		ur"""Rate (/s) counter for iipfailedmipused.
		"""
		try :
			return self._iipfailedmipusedrate
		except Exception as e:
			raise e

	@property
	def staconnsuccess(self) :
		ur"""Number of STA connection success.
		"""
		try :
			return self._staconnsuccess
		except Exception as e:
			raise e

	@property
	def cfghtmlservedrate(self) :
		ur"""Rate (/s) counter for cfghtmlserved.
		"""
		try :
			return self._cfghtmlservedrate
		except Exception as e:
			raise e

	@property
	def staresponserecvdrate(self) :
		ur"""Rate (/s) counter for staresponserecvd.
		"""
		try :
			return self._staresponserecvdrate
		except Exception as e:
			raise e

	@property
	def cpsconnfailure(self) :
		ur"""Number of CPS connection failure.
		"""
		try :
			return self._cpsconnfailure
		except Exception as e:
			raise e

	@property
	def csrequesthitrate(self) :
		ur"""Rate (/s) counter for csrequesthit.
		"""
		try :
			return self._csrequesthitrate
		except Exception as e:
			raise e

	@property
	def csnonhttpprobehit(self) :
		ur"""Number of probes from VPN to back-end non-HTTP servers that have been accessed by the VPN client.
		"""
		try :
			return self._csnonhttpprobehit
		except Exception as e:
			raise e

	@property
	def iipfailedmipdisabledrate(self) :
		ur"""Rate (/s) counter for iipfailedmipdisabled.
		"""
		try :
			return self._iipfailedmipdisabledrate
		except Exception as e:
			raise e

	@property
	def cpsconnsuccessrate(self) :
		ur"""Rate (/s) counter for cpsconnsuccess.
		"""
		try :
			return self._cpsconnsuccessrate
		except Exception as e:
			raise e

	@property
	def socksconnresprcvdrate(self) :
		ur"""Rate (/s) counter for socksconnresprcvd.
		"""
		try :
			return self._socksconnresprcvdrate
		except Exception as e:
			raise e

	@property
	def indexhtmlnoserved(self) :
		ur"""Number of failures to display VPN login page.
		"""
		try :
			return self._indexhtmlnoserved
		except Exception as e:
			raise e

	@property
	def fsrequestrate(self) :
		ur"""Rate (/s) counter for totalfsrequest.
		"""
		try :
			return self._fsrequestrate
		except Exception as e:
			raise e

	@property
	def indexhtmlhit(self) :
		ur"""Number of requests for VPN login page.
		"""
		try :
			return self._indexhtmlhit
		except Exception as e:
			raise e

	@property
	def cfghtmlserved(self) :
		ur"""Number of client configuration requests received by VPN server.
		"""
		try :
			return self._cfghtmlserved
		except Exception as e:
			raise e

	@property
	def icalicensefailure(self) :
		ur"""Number of ICA license failure.
		"""
		try :
			return self._icalicensefailure
		except Exception as e:
			raise e

	@property
	def staresponserecvd(self) :
		ur"""Number of STA response received.
		"""
		try :
			return self._staresponserecvd
		except Exception as e:
			raise e

	@property
	def socksclienterror(self) :
		ur"""Number of SOCKS client error.
		"""
		try :
			return self._socksclienterror
		except Exception as e:
			raise e

	@property
	def iipdisabledmipdisabledrate(self) :
		ur"""Rate (/s) counter for iipdisabledmipdisabled.
		"""
		try :
			return self._iipdisabledmipdisabledrate
		except Exception as e:
			raise e

	@property
	def socksconnrespsent(self) :
		ur"""Number of sent SOCKS connect response.
		"""
		try :
			return self._socksconnrespsent
		except Exception as e:
			raise e

	@property
	def socksmethresprcvd(self) :
		ur"""Number of received SOCKS method response.
		"""
		try :
			return self._socksmethresprcvd
		except Exception as e:
			raise e

	@property
	def iipdisabledmipused(self) :
		ur"""Number of times MIP is used as IIP is disabled.
		"""
		try :
			return self._iipdisabledmipused
		except Exception as e:
			raise e

	@property
	def iipfailedmipused(self) :
		ur"""Number of times MIP is used as IIP assignment failed.
		"""
		try :
			return self._iipfailedmipused
		except Exception as e:
			raise e

	@property
	def socksconnreqsentrate(self) :
		ur"""Rate (/s) counter for socksconnreqsent.
		"""
		try :
			return self._socksconnreqsentrate
		except Exception as e:
			raise e

	@property
	def starequestsentrate(self) :
		ur"""Rate (/s) counter for starequestsent.
		"""
		try :
			return self._starequestsentrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpn_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn
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
		ur""" Use this API to fetch the statistics of all vpn_stats resources that are configured on netscaler.
		"""
		try :
			obj = vpn_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class vpn_response(base_response) :
	def __init__(self, length=1) :
		self.vpn = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpn = [vpn_stats() for _ in range(length)]

