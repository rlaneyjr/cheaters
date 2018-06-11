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

class nssimpleacl_stats(base_resource) :
	ur""" Statistics for simple ACL resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._sacltothits = 0
		self._saclhitsrate = 0
		self._sacltotmisses = 0
		self._saclmissesrate = 0
		self._saclscount = 0
		self._sacltotpktsallowed = 0
		self._saclpktsallowedrate = 0
		self._sacltotpktsbridged = 0
		self._saclpktsbridgedrate = 0
		self._sacltotpktsdenied = 0
		self._saclpktsdeniedrate = 0

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
	def sacltothits(self) :
		ur"""Packets matching a SimpleACL.
		"""
		try :
			return self._sacltothits
		except Exception as e:
			raise e

	@property
	def saclscount(self) :
		ur"""Number of SimpleACLs configured.
		"""
		try :
			return self._saclscount
		except Exception as e:
			raise e

	@property
	def saclhitsrate(self) :
		ur"""Rate (/s) counter for sacltothits.
		"""
		try :
			return self._saclhitsrate
		except Exception as e:
			raise e

	@property
	def saclpktsbridgedrate(self) :
		ur"""Rate (/s) counter for sacltotpktsbridged.
		"""
		try :
			return self._saclpktsbridgedrate
		except Exception as e:
			raise e

	@property
	def sacltotpktsdenied(self) :
		ur"""Packets dropped because they match SimpleACL (Access Control List) with processing mode set to DENY.
		"""
		try :
			return self._sacltotpktsdenied
		except Exception as e:
			raise e

	@property
	def sacltotmisses(self) :
		ur"""Packets not matching any SimpleACL.
		"""
		try :
			return self._sacltotmisses
		except Exception as e:
			raise e

	@property
	def saclmissesrate(self) :
		ur"""Rate (/s) counter for sacltotmisses.
		"""
		try :
			return self._saclmissesrate
		except Exception as e:
			raise e

	@property
	def saclpktsallowedrate(self) :
		ur"""Rate (/s) counter for sacltotpktsallowed.
		"""
		try :
			return self._saclpktsallowedrate
		except Exception as e:
			raise e

	@property
	def sacltotpktsbridged(self) :
		ur"""Total packets that matched a SimpleACL with action BRIDGE and got bridged by NetScaler.
		"""
		try :
			return self._sacltotpktsbridged
		except Exception as e:
			raise e

	@property
	def saclpktsdeniedrate(self) :
		ur"""Rate (/s) counter for sacltotpktsdenied.
		"""
		try :
			return self._saclpktsdeniedrate
		except Exception as e:
			raise e

	@property
	def sacltotpktsallowed(self) :
		ur"""Total packets that matched a SimpleACL with action ALLOW and got consumed by NetScaler.
		"""
		try :
			return self._sacltotpktsallowed
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nssimpleacl_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nssimpleacl
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
		ur""" Use this API to fetch the statistics of all nssimpleacl_stats resources that are configured on netscaler.
		"""
		try :
			obj = nssimpleacl_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class nssimpleacl_response(base_response) :
	def __init__(self, length=1) :
		self.nssimpleacl = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nssimpleacl = [nssimpleacl_stats() for _ in range(length)]

