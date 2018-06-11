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

class aaa_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._aaaauthsuccess = 0
		self._aaaauthsuccessrate = 0
		self._aaaauthfail = 0
		self._aaaauthfailrate = 0
		self._aaaauthonlyhttpsuccess = 0
		self._aaaauthonlyhttpsuccessrate = 0
		self._aaaauthonlyhttpfail = 0
		self._aaaauthonlyhttpfailrate = 0
		self._aaaauthnonhttpsuccess = 0
		self._aaaauthnonhttpsuccessrate = 0
		self._aaaauthnonhttpfail = 0
		self._aaaauthnonhttpfailrate = 0
		self._aaacursessions = 0
		self._aaacursessionsrate = 0
		self._aaatotsessions = 0
		self._aaasessionsrate = 0
		self._aaatotsessiontimeout = 0
		self._aaasessiontimeoutrate = 0
		self._aaacuricasessions = 0
		self._aaacuricasessionsrate = 0
		self._aaacuricaonlyconn = 0
		self._aaacuricaonlyconnrate = 0
		self._aaacuricaconn = 0
		self._aaacuricaconnrate = 0
		self._aaacurtmsessions = 0
		self._aaacurtmsessionsrate = 0
		self._aaatottmsessions = 0
		self._aaatmsessionsrate = 0

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
	def aaatotsessiontimeout(self) :
		ur"""Count of AAA sessions that have timed out.
		"""
		try :
			return self._aaatotsessiontimeout
		except Exception as e:
			raise e

	@property
	def aaaauthfail(self) :
		ur"""Count of authentication failures.
		"""
		try :
			return self._aaaauthfail
		except Exception as e:
			raise e

	@property
	def aaaauthsuccess(self) :
		ur"""Count of authentication successes.
		"""
		try :
			return self._aaaauthsuccess
		except Exception as e:
			raise e

	@property
	def aaatottmsessions(self) :
		ur"""Count of all AAATM sessions.
		"""
		try :
			return self._aaatottmsessions
		except Exception as e:
			raise e

	@property
	def aaaauthonlyhttpfailrate(self) :
		ur"""Rate (/s) counter for aaaauthonlyhttpfail.
		"""
		try :
			return self._aaaauthonlyhttpfailrate
		except Exception as e:
			raise e

	@property
	def aaaauthnonhttpsuccess(self) :
		ur"""Count of non HTTP connections that succeeded authorization.
		"""
		try :
			return self._aaaauthnonhttpsuccess
		except Exception as e:
			raise e

	@property
	def aaacuricaonlyconnrate(self) :
		ur"""Rate (/s) counter for aaacuricaonlyconn.
		"""
		try :
			return self._aaacuricaonlyconnrate
		except Exception as e:
			raise e

	@property
	def aaaauthonlyhttpsuccessrate(self) :
		ur"""Rate (/s) counter for aaaauthonlyhttpsuccess.
		"""
		try :
			return self._aaaauthonlyhttpsuccessrate
		except Exception as e:
			raise e

	@property
	def aaacurtmsessions(self) :
		ur"""Count of current AAATM sessions.
		"""
		try :
			return self._aaacurtmsessions
		except Exception as e:
			raise e

	@property
	def aaacuricasessions(self) :
		ur"""Count of current ICA only sessions.
		"""
		try :
			return self._aaacuricasessions
		except Exception as e:
			raise e

	@property
	def aaatotsessions(self) :
		ur"""Count of all AAA sessions.
		"""
		try :
			return self._aaatotsessions
		except Exception as e:
			raise e

	@property
	def aaaauthonlyhttpfail(self) :
		ur"""Count of HTTP connections that failed authorization.
		"""
		try :
			return self._aaaauthonlyhttpfail
		except Exception as e:
			raise e

	@property
	def aaacuricaonlyconn(self) :
		ur"""Count of current ICA only connections.
		"""
		try :
			return self._aaacuricaonlyconn
		except Exception as e:
			raise e

	@property
	def aaatmsessionsrate(self) :
		ur"""Rate (/s) counter for aaatottmsessions.
		"""
		try :
			return self._aaatmsessionsrate
		except Exception as e:
			raise e

	@property
	def aaaauthfailrate(self) :
		ur"""Rate (/s) counter for aaaauthfail.
		"""
		try :
			return self._aaaauthfailrate
		except Exception as e:
			raise e

	@property
	def aaacursessionsrate(self) :
		ur"""Rate (/s) counter for aaacursessions.
		"""
		try :
			return self._aaacursessionsrate
		except Exception as e:
			raise e

	@property
	def aaaauthnonhttpsuccessrate(self) :
		ur"""Rate (/s) counter for aaaauthnonhttpsuccess.
		"""
		try :
			return self._aaaauthnonhttpsuccessrate
		except Exception as e:
			raise e

	@property
	def aaacuricaconn(self) :
		ur"""Count of current ICA connections.
		"""
		try :
			return self._aaacuricaconn
		except Exception as e:
			raise e

	@property
	def aaaauthnonhttpfailrate(self) :
		ur"""Rate (/s) counter for aaaauthnonhttpfail.
		"""
		try :
			return self._aaaauthnonhttpfailrate
		except Exception as e:
			raise e

	@property
	def aaaauthnonhttpfail(self) :
		ur"""Count of non HTTP connections that failed authorization.
		"""
		try :
			return self._aaaauthnonhttpfail
		except Exception as e:
			raise e

	@property
	def aaacuricaconnrate(self) :
		ur"""Rate (/s) counter for aaacuricaconn.
		"""
		try :
			return self._aaacuricaconnrate
		except Exception as e:
			raise e

	@property
	def aaaauthsuccessrate(self) :
		ur"""Rate (/s) counter for aaaauthsuccess.
		"""
		try :
			return self._aaaauthsuccessrate
		except Exception as e:
			raise e

	@property
	def aaaauthonlyhttpsuccess(self) :
		ur"""Count of HTTP connections that succeeded authorization.
		"""
		try :
			return self._aaaauthonlyhttpsuccess
		except Exception as e:
			raise e

	@property
	def aaacurtmsessionsrate(self) :
		ur"""Rate (/s) counter for aaacurtmsessions.
		"""
		try :
			return self._aaacurtmsessionsrate
		except Exception as e:
			raise e

	@property
	def aaasessiontimeoutrate(self) :
		ur"""Rate (/s) counter for aaatotsessiontimeout.
		"""
		try :
			return self._aaasessiontimeoutrate
		except Exception as e:
			raise e

	@property
	def aaacuricasessionsrate(self) :
		ur"""Rate (/s) counter for aaacuricasessions.
		"""
		try :
			return self._aaacuricasessionsrate
		except Exception as e:
			raise e

	@property
	def aaacursessions(self) :
		ur"""Count of current AAA sessions.
		"""
		try :
			return self._aaacursessions
		except Exception as e:
			raise e

	@property
	def aaasessionsrate(self) :
		ur"""Rate (/s) counter for aaatotsessions.
		"""
		try :
			return self._aaasessionsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaa_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaa
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
		ur""" Use this API to fetch the statistics of all aaa_stats resources that are configured on netscaler.
		"""
		try :
			obj = aaa_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class aaa_response(base_response) :
	def __init__(self, length=1) :
		self.aaa = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaa = [aaa_stats() for _ in range(length)]

