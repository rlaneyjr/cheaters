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

class dos_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._dostotconditiontriggered = 0
		self._dosconditiontriggeredrate = 0
		self._dostotvalidcookies = 0
		self._dosvalidcookiesrate = 0
		self._dostotdospriorityclients = 0
		self._dosdospriorityclientsrate = 0

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
	def dostotvalidcookies(self) :
		ur"""Number of clients from whom the NetScaler appliance received a valid DOS cookie.
		"""
		try :
			return self._dostotvalidcookies
		except Exception as e:
			raise e

	@property
	def dosvalidcookiesrate(self) :
		ur"""Rate (/s) counter for dostotvalidcookies.
		"""
		try :
			return self._dosvalidcookiesrate
		except Exception as e:
			raise e

	@property
	def dosdospriorityclientsrate(self) :
		ur"""Rate (/s) counter for dostotdospriorityclients.
		"""
		try :
			return self._dosdospriorityclientsrate
		except Exception as e:
			raise e

	@property
	def dosconditiontriggeredrate(self) :
		ur"""Rate (/s) counter for dostotconditiontriggered.
		"""
		try :
			return self._dosconditiontriggeredrate
		except Exception as e:
			raise e

	@property
	def dostotconditiontriggered(self) :
		ur"""Number of times the NetScaler appliance triggered the DOS JavaScript due to a condition match.
		"""
		try :
			return self._dostotconditiontriggered
		except Exception as e:
			raise e

	@property
	def dostotdospriorityclients(self) :
		ur"""Number of valid clients that were given DOS priority.
		"""
		try :
			return self._dostotdospriorityclients
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dos_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dos
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
		ur""" Use this API to fetch the statistics of all dos_stats resources that are configured on netscaler.
		"""
		try :
			obj = dos_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class dos_response(base_response) :
	def __init__(self, length=1) :
		self.dos = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dos = [dos_stats() for _ in range(length)]

