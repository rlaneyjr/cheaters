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

class nsacl_stats(base_resource) :
	ur""" Statistics for ACL entry resource.
	"""
	def __init__(self) :
		self._aclname = ""
		self._clearstats = ""
		self._acltotpktsbridged = 0
		self._aclpktsbridgedrate = 0
		self._acltotpktsdenied = 0
		self._aclpktsdeniedrate = 0
		self._acltotpktsallowed = 0
		self._aclpktsallowedrate = 0
		self._acltotpktsnat = 0
		self._aclpktsnatrate = 0
		self._acltothits = 0
		self._aclhitsrate = 0
		self._acltotmisses = 0
		self._aclmissesrate = 0
		self._acltotcount = 0
		self._aclperhits = 0
		self._aclperhitsrate = 0

	@property
	def aclname(self) :
		ur"""Name of the extended ACL rule whose statistics you want the NetScaler appliance to display.<br/>Minimum length =  1.
		"""
		try :
			return self._aclname
		except Exception as e:
			raise e

	@aclname.setter
	def aclname(self, aclname) :
		ur"""Name of the extended ACL rule whose statistics you want the NetScaler appliance to display.
		"""
		try :
			self._aclname = aclname
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
	def acltotpktsdenied(self) :
		ur"""Packets dropped because they match ACLs with processing mode set to DENY.
		"""
		try :
			return self._acltotpktsdenied
		except Exception as e:
			raise e

	@property
	def acltothits(self) :
		ur"""Packets matching an ACL.
		"""
		try :
			return self._acltothits
		except Exception as e:
			raise e

	@property
	def aclperhits(self) :
		ur"""Number of times the acl was hit.
		"""
		try :
			return self._aclperhits
		except Exception as e:
			raise e

	@property
	def acltotpktsnat(self) :
		ur"""Packets matching a NAT ACL, resulting in a NAT session.
		"""
		try :
			return self._acltotpktsnat
		except Exception as e:
			raise e

	@property
	def aclperhitsrate(self) :
		ur"""Rate (/s) counter for aclperhits.
		"""
		try :
			return self._aclperhitsrate
		except Exception as e:
			raise e

	@property
	def aclpktsdeniedrate(self) :
		ur"""Rate (/s) counter for acltotpktsdenied.
		"""
		try :
			return self._aclpktsdeniedrate
		except Exception as e:
			raise e

	@property
	def aclhitsrate(self) :
		ur"""Rate (/s) counter for acltothits.
		"""
		try :
			return self._aclhitsrate
		except Exception as e:
			raise e

	@property
	def aclpktsallowedrate(self) :
		ur"""Rate (/s) counter for acltotpktsallowed.
		"""
		try :
			return self._aclpktsallowedrate
		except Exception as e:
			raise e

	@property
	def aclpktsnatrate(self) :
		ur"""Rate (/s) counter for acltotpktsnat.
		"""
		try :
			return self._aclpktsnatrate
		except Exception as e:
			raise e

	@property
	def acltotcount(self) :
		ur"""Total number of ACL rules configured.
		"""
		try :
			return self._acltotcount
		except Exception as e:
			raise e

	@property
	def acltotmisses(self) :
		ur"""Packets not matching any ACL.
		"""
		try :
			return self._acltotmisses
		except Exception as e:
			raise e

	@property
	def acltotpktsallowed(self) :
		ur"""Packets matching ACLs with processing mode set to ALLOW. NetScaler processes these packets.
		"""
		try :
			return self._acltotpktsallowed
		except Exception as e:
			raise e

	@property
	def aclpktsbridgedrate(self) :
		ur"""Rate (/s) counter for acltotpktsbridged.
		"""
		try :
			return self._aclpktsbridgedrate
		except Exception as e:
			raise e

	@property
	def acltotpktsbridged(self) :
		ur"""Packets matching a bridge ACL, which is in transparent mode and bypasses service processing.
		"""
		try :
			return self._acltotpktsbridged
		except Exception as e:
			raise e

	@property
	def aclmissesrate(self) :
		ur"""Rate (/s) counter for acltotmisses.
		"""
		try :
			return self._aclmissesrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsacl_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsacl
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.aclname is not None :
				return str(self.aclname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all nsacl_stats resources that are configured on netscaler.
		"""
		try :
			obj = nsacl_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.aclname = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class nsacl_response(base_response) :
	def __init__(self, length=1) :
		self.nsacl = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsacl = [nsacl_stats() for _ in range(length)]

