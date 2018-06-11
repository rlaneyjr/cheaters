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

class appqoe_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._totinmemrsp = 0
		self._inmemrsprate = 0
		self._totfaultycookies = 0
		self._faultycookiesrate = 0
		self._totvalidcookies = 0
		self._validcookiesrate = 0
		self._tothighprireq = 0
		self._highprireqrate = 0
		self._totmediumprireq = 0
		self._mediumprireqrate = 0
		self._totlowprireq = 0
		self._lowprireqrate = 0
		self._totlowestprireq = 0
		self._lowestprireqrate = 0
		self._totaltsvrsubfailed = 0
		self._tsvrsubfailedrate = 0
		self._totdostrig = 0
		self._dostrigrate = 0
		self._totdosqvalidcookies = 0
		self._dosqvalidcookiesrate = 0
		self._totdoshvalidcookies = 0
		self._doshvalidcookiesrate = 0
		self._totsidvalidcookies = 0
		self._sidvalidcookiesrate = 0
		self._totonhvalidcookies = 0
		self._onhvalidcookiesrate = 0
		self._totpriqvalidcookies = 0
		self._priqvalidcookiesrate = 0
		self._totdosqfaultycookies = 0
		self._dosqfaultycookiesrate = 0
		self._totdoshfaultycookies = 0
		self._doshfaultycookiesrate = 0
		self._totsidfaultycookies = 0
		self._sidfaultycookiesrate = 0
		self._totonhfaultycookies = 0
		self._onhfaultycookiesrate = 0
		self._totpriqfaultycookies = 0
		self._priqfaultycookiesrate = 0
		self._totpriembedlinks = 0
		self._priembedlinksrate = 0
		self._totsessreq = 0
		self._sessreqrate = 0
		self._totaltcntreq = 0
		self._tcntreqrate = 0
		self._totgetinmemrsp = 0
		self._getinmemrsprate = 0
		self._totpostinmemrsp = 0
		self._postinmemrsprate = 0
		self._totpostinmemrspbytes = 0
		self._postinmemrspbytesrate = 0

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
	def totpriqvalidcookies(self) :
		ur"""Total PRIQ valid cookies received.
		"""
		try :
			return self._totpriqvalidcookies
		except Exception as e:
			raise e

	@property
	def totonhvalidcookies(self) :
		ur"""Total ONH valid cookies received.
		"""
		try :
			return self._totonhvalidcookies
		except Exception as e:
			raise e

	@property
	def dosqvalidcookiesrate(self) :
		ur"""Rate (/s) counter for totdosqvalidcookies.
		"""
		try :
			return self._dosqvalidcookiesrate
		except Exception as e:
			raise e

	@property
	def sidvalidcookiesrate(self) :
		ur"""Rate (/s) counter for totsidvalidcookies.
		"""
		try :
			return self._sidvalidcookiesrate
		except Exception as e:
			raise e

	@property
	def onhvalidcookiesrate(self) :
		ur"""Rate (/s) counter for totonhvalidcookies.
		"""
		try :
			return self._onhvalidcookiesrate
		except Exception as e:
			raise e

	@property
	def totdosqvalidcookies(self) :
		ur"""Total DOSQ valid cookies received.
		"""
		try :
			return self._totdosqvalidcookies
		except Exception as e:
			raise e

	@property
	def dostrigrate(self) :
		ur"""Rate (/s) counter for totdostrig.
		"""
		try :
			return self._dostrigrate
		except Exception as e:
			raise e

	@property
	def totgetinmemrsp(self) :
		ur"""Total in-memory GET responses sent from NS.
		"""
		try :
			return self._totgetinmemrsp
		except Exception as e:
			raise e

	@property
	def totlowprireq(self) :
		ur"""Total Requests served from low priority queue.
		"""
		try :
			return self._totlowprireq
		except Exception as e:
			raise e

	@property
	def totdoshfaultycookies(self) :
		ur"""Total DOSH faulty cookies received.
		"""
		try :
			return self._totdoshfaultycookies
		except Exception as e:
			raise e

	@property
	def doshfaultycookiesrate(self) :
		ur"""Rate (/s) counter for totdoshfaultycookies.
		"""
		try :
			return self._doshfaultycookiesrate
		except Exception as e:
			raise e

	@property
	def sessreqrate(self) :
		ur"""Rate (/s) counter for totsessreq.
		"""
		try :
			return self._sessreqrate
		except Exception as e:
			raise e

	@property
	def totpostinmemrspbytes(self) :
		ur"""Total in-memory response bytes sent from NS.
		"""
		try :
			return self._totpostinmemrspbytes
		except Exception as e:
			raise e

	@property
	def totpriqfaultycookies(self) :
		ur"""Total PRIQ faulty cookies received.
		"""
		try :
			return self._totpriqfaultycookies
		except Exception as e:
			raise e

	@property
	def totpostinmemrsp(self) :
		ur"""Total in-memory POST responses sent from NS.
		"""
		try :
			return self._totpostinmemrsp
		except Exception as e:
			raise e

	@property
	def priembedlinksrate(self) :
		ur"""Rate (/s) counter for totpriembedlinks.
		"""
		try :
			return self._priembedlinksrate
		except Exception as e:
			raise e

	@property
	def mediumprireqrate(self) :
		ur"""Rate (/s) counter for totmediumprireq.
		"""
		try :
			return self._mediumprireqrate
		except Exception as e:
			raise e

	@property
	def totdostrig(self) :
		ur"""Total number of times HDOS condition triggered.
		"""
		try :
			return self._totdostrig
		except Exception as e:
			raise e

	@property
	def totvalidcookies(self) :
		ur"""Total valid cookies received.
		"""
		try :
			return self._totvalidcookies
		except Exception as e:
			raise e

	@property
	def totinmemrsp(self) :
		ur"""Total in-memory responses sent from NS.
		"""
		try :
			return self._totinmemrsp
		except Exception as e:
			raise e

	@property
	def totsidfaultycookies(self) :
		ur"""Total SID faulty cookies received.
		"""
		try :
			return self._totsidfaultycookies
		except Exception as e:
			raise e

	@property
	def totsidvalidcookies(self) :
		ur"""Total SID valid cookies received.
		"""
		try :
			return self._totsidvalidcookies
		except Exception as e:
			raise e

	@property
	def totdosqfaultycookies(self) :
		ur"""Total DOSQ faulty cookies received.
		"""
		try :
			return self._totdosqfaultycookies
		except Exception as e:
			raise e

	@property
	def tsvrsubfailedrate(self) :
		ur"""Rate (/s) counter for totaltsvrsubfailed.
		"""
		try :
			return self._tsvrsubfailedrate
		except Exception as e:
			raise e

	@property
	def postinmemrsprate(self) :
		ur"""Rate (/s) counter for totpostinmemrsp.
		"""
		try :
			return self._postinmemrsprate
		except Exception as e:
			raise e

	@property
	def totpriembedlinks(self) :
		ur"""Total requests for valid embedded links.
		"""
		try :
			return self._totpriembedlinks
		except Exception as e:
			raise e

	@property
	def totmediumprireq(self) :
		ur"""Total Requests served from medium priority queue.
		"""
		try :
			return self._totmediumprireq
		except Exception as e:
			raise e

	@property
	def priqvalidcookiesrate(self) :
		ur"""Rate (/s) counter for totpriqvalidcookies.
		"""
		try :
			return self._priqvalidcookiesrate
		except Exception as e:
			raise e

	@property
	def totfaultycookies(self) :
		ur"""Total faulty cookies received.
		"""
		try :
			return self._totfaultycookies
		except Exception as e:
			raise e

	@property
	def doshvalidcookiesrate(self) :
		ur"""Rate (/s) counter for totdoshvalidcookies.
		"""
		try :
			return self._doshvalidcookiesrate
		except Exception as e:
			raise e

	@property
	def sidfaultycookiesrate(self) :
		ur"""Rate (/s) counter for totsidfaultycookies.
		"""
		try :
			return self._sidfaultycookiesrate
		except Exception as e:
			raise e

	@property
	def highprireqrate(self) :
		ur"""Rate (/s) counter for tothighprireq.
		"""
		try :
			return self._highprireqrate
		except Exception as e:
			raise e

	@property
	def dosqfaultycookiesrate(self) :
		ur"""Rate (/s) counter for totdosqfaultycookies.
		"""
		try :
			return self._dosqfaultycookiesrate
		except Exception as e:
			raise e

	@property
	def inmemrsprate(self) :
		ur"""Rate (/s) counter for totinmemrsp.
		"""
		try :
			return self._inmemrsprate
		except Exception as e:
			raise e

	@property
	def getinmemrsprate(self) :
		ur"""Rate (/s) counter for totgetinmemrsp.
		"""
		try :
			return self._getinmemrsprate
		except Exception as e:
			raise e

	@property
	def onhfaultycookiesrate(self) :
		ur"""Rate (/s) counter for totonhfaultycookies.
		"""
		try :
			return self._onhfaultycookiesrate
		except Exception as e:
			raise e

	@property
	def validcookiesrate(self) :
		ur"""Rate (/s) counter for totvalidcookies.
		"""
		try :
			return self._validcookiesrate
		except Exception as e:
			raise e

	@property
	def totaltcntreq(self) :
		ur"""Total requests for alternate contents.
		"""
		try :
			return self._totaltcntreq
		except Exception as e:
			raise e

	@property
	def totsessreq(self) :
		ur"""Total valid SIDQ requests within session.
		"""
		try :
			return self._totsessreq
		except Exception as e:
			raise e

	@property
	def priqfaultycookiesrate(self) :
		ur"""Rate (/s) counter for totpriqfaultycookies.
		"""
		try :
			return self._priqfaultycookiesrate
		except Exception as e:
			raise e

	@property
	def tcntreqrate(self) :
		ur"""Rate (/s) counter for totaltcntreq.
		"""
		try :
			return self._tcntreqrate
		except Exception as e:
			raise e

	@property
	def totdoshvalidcookies(self) :
		ur"""Total DOSH valid cookies received.
		"""
		try :
			return self._totdoshvalidcookies
		except Exception as e:
			raise e

	@property
	def lowprireqrate(self) :
		ur"""Rate (/s) counter for totlowprireq.
		"""
		try :
			return self._lowprireqrate
		except Exception as e:
			raise e

	@property
	def tothighprireq(self) :
		ur"""Total Requests served from higher priority queue.
		"""
		try :
			return self._tothighprireq
		except Exception as e:
			raise e

	@property
	def totaltsvrsubfailed(self) :
		ur"""Total number of times alternate server substitution failed.
		"""
		try :
			return self._totaltsvrsubfailed
		except Exception as e:
			raise e

	@property
	def totlowestprireq(self) :
		ur"""Total Requests served from surge priority queue.
		"""
		try :
			return self._totlowestprireq
		except Exception as e:
			raise e

	@property
	def lowestprireqrate(self) :
		ur"""Rate (/s) counter for totlowestprireq.
		"""
		try :
			return self._lowestprireqrate
		except Exception as e:
			raise e

	@property
	def totonhfaultycookies(self) :
		ur"""Total ONH faulty cookies received.
		"""
		try :
			return self._totonhfaultycookies
		except Exception as e:
			raise e

	@property
	def faultycookiesrate(self) :
		ur"""Rate (/s) counter for totfaultycookies.
		"""
		try :
			return self._faultycookiesrate
		except Exception as e:
			raise e

	@property
	def postinmemrspbytesrate(self) :
		ur"""Rate (/s) counter for totpostinmemrspbytes.
		"""
		try :
			return self._postinmemrspbytesrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appqoe_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appqoe
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
		ur""" Use this API to fetch the statistics of all appqoe_stats resources that are configured on netscaler.
		"""
		try :
			obj = appqoe_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class appqoe_response(base_response) :
	def __init__(self, length=1) :
		self.appqoe = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appqoe = [appqoe_stats() for _ in range(length)]

