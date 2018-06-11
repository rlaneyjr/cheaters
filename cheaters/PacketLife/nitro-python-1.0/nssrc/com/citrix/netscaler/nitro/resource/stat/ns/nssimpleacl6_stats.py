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

class nssimpleacl6_stats(base_resource) :
	ur""" Statistics for simple ACL6 resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._sacl6tothits = 0
		self._sacl6hitsrate = 0
		self._sacl6totmisses = 0
		self._sacl6missesrate = 0
		self._sacl6scount = 0
		self._sacl6totpktsallowed = 0
		self._sacl6pktsallowedrate = 0
		self._sacl6totpktsbridged = 0
		self._sacl6pktsbridgedrate = 0
		self._sacl6totpktsdenied = 0
		self._sacl6pktsdeniedrate = 0

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
	def sacl6scount(self) :
		ur"""Number of SimpleACL6s configured.
		"""
		try :
			return self._sacl6scount
		except Exception as e:
			raise e

	@property
	def sacl6pktsbridgedrate(self) :
		ur"""Rate (/s) counter for sacl6totpktsbridged.
		"""
		try :
			return self._sacl6pktsbridgedrate
		except Exception as e:
			raise e

	@property
	def sacl6totpktsallowed(self) :
		ur"""Total packets that matched a SimpleACL6 with action ALLOW and got consumed by NetScaler.
		"""
		try :
			return self._sacl6totpktsallowed
		except Exception as e:
			raise e

	@property
	def sacl6totmisses(self) :
		ur"""Packets not matching any SimpleACL6.
		"""
		try :
			return self._sacl6totmisses
		except Exception as e:
			raise e

	@property
	def sacl6missesrate(self) :
		ur"""Rate (/s) counter for sacl6totmisses.
		"""
		try :
			return self._sacl6missesrate
		except Exception as e:
			raise e

	@property
	def sacl6hitsrate(self) :
		ur"""Rate (/s) counter for sacl6tothits.
		"""
		try :
			return self._sacl6hitsrate
		except Exception as e:
			raise e

	@property
	def sacl6tothits(self) :
		ur"""Packets matching a SimpleACL6.
		"""
		try :
			return self._sacl6tothits
		except Exception as e:
			raise e

	@property
	def sacl6totpktsdenied(self) :
		ur"""Packets dropped because they match SimpleACL6 with processing mode set to DENY.
		"""
		try :
			return self._sacl6totpktsdenied
		except Exception as e:
			raise e

	@property
	def sacl6pktsallowedrate(self) :
		ur"""Rate (/s) counter for sacl6totpktsallowed.
		"""
		try :
			return self._sacl6pktsallowedrate
		except Exception as e:
			raise e

	@property
	def sacl6totpktsbridged(self) :
		ur"""Total packets that matched a SimpleACL6 with action BRIDGE and got bridged by NetScaler.
		"""
		try :
			return self._sacl6totpktsbridged
		except Exception as e:
			raise e

	@property
	def sacl6pktsdeniedrate(self) :
		ur"""Rate (/s) counter for sacl6totpktsdenied.
		"""
		try :
			return self._sacl6pktsdeniedrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nssimpleacl6_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nssimpleacl6
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
		ur""" Use this API to fetch the statistics of all nssimpleacl6_stats resources that are configured on netscaler.
		"""
		try :
			obj = nssimpleacl6_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class nssimpleacl6_response(base_response) :
	def __init__(self, length=1) :
		self.nssimpleacl6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nssimpleacl6 = [nssimpleacl6_stats() for _ in range(length)]

