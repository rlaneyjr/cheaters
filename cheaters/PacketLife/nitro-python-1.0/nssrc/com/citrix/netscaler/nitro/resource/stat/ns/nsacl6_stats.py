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

class nsacl6_stats(base_resource) :
	ur""" Statistics for ACL6 entry resource.
	"""
	def __init__(self) :
		self._acl6name = ""
		self._clearstats = ""
		self._acl6totpktsbridged = 0
		self._acl6pktsbridgedrate = 0
		self._acl6totpktsdenied = 0
		self._acl6pktsdeniedrate = 0
		self._acl6totpktsallowed = 0
		self._acl6pktsallowedrate = 0
		self._acl6totpktsnat = 0
		self._acl6pktsnatrate = 0
		self._acl6tothits = 0
		self._acl6hitsrate = 0
		self._acl6totmisses = 0
		self._acl6missesrate = 0
		self._acl6totpktsnat64 = 0
		self._acl6pktsnat64rate = 0
		self._acl6totcount = 0
		self._acl6perhits = 0
		self._acl6perhitsrate = 0

	@property
	def acl6name(self) :
		ur"""Name of the ACL6 rule whose statistics you want the NetScaler appliance to display.<br/>Minimum length =  1.
		"""
		try :
			return self._acl6name
		except Exception as e:
			raise e

	@acl6name.setter
	def acl6name(self, acl6name) :
		ur"""Name of the ACL6 rule whose statistics you want the NetScaler appliance to display.
		"""
		try :
			self._acl6name = acl6name
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
	def acl6pktsnatrate(self) :
		ur"""Rate (/s) counter for acl6totpktsnat.
		"""
		try :
			return self._acl6pktsnatrate
		except Exception as e:
			raise e

	@property
	def acl6missesrate(self) :
		ur"""Rate (/s) counter for acl6totmisses.
		"""
		try :
			return self._acl6missesrate
		except Exception as e:
			raise e

	@property
	def acl6totmisses(self) :
		ur"""Packets not matching any IPv6 ACL.
		"""
		try :
			return self._acl6totmisses
		except Exception as e:
			raise e

	@property
	def acl6totpktsnat64(self) :
		ur"""Packets matching a NAT64 ACL6, resulting in a NAT64 translation.
		"""
		try :
			return self._acl6totpktsnat64
		except Exception as e:
			raise e

	@property
	def acl6pktsnat64rate(self) :
		ur"""Rate (/s) counter for acl6totpktsnat64.
		"""
		try :
			return self._acl6pktsnat64rate
		except Exception as e:
			raise e

	@property
	def acl6totpktsnat(self) :
		ur"""Packets matching a NAT ACL6, resulting in a NAT session.
		"""
		try :
			return self._acl6totpktsnat
		except Exception as e:
			raise e

	@property
	def acl6perhitsrate(self) :
		ur"""Rate (/s) counter for acl6perhits.
		"""
		try :
			return self._acl6perhitsrate
		except Exception as e:
			raise e

	@property
	def acl6perhits(self) :
		ur"""Number of times the acl6 was hit.
		"""
		try :
			return self._acl6perhits
		except Exception as e:
			raise e

	@property
	def acl6tothits(self) :
		ur"""Packets matching an IPv6 ACL.
		"""
		try :
			return self._acl6tothits
		except Exception as e:
			raise e

	@property
	def acl6pktsbridgedrate(self) :
		ur"""Rate (/s) counter for acl6totpktsbridged.
		"""
		try :
			return self._acl6pktsbridgedrate
		except Exception as e:
			raise e

	@property
	def acl6pktsallowedrate(self) :
		ur"""Rate (/s) counter for acl6totpktsallowed.
		"""
		try :
			return self._acl6pktsallowedrate
		except Exception as e:
			raise e

	@property
	def acl6totpktsbridged(self) :
		ur"""Packets matching a bridge IPv6 ACL, which is in transparent mode and bypasses service processing.
		"""
		try :
			return self._acl6totpktsbridged
		except Exception as e:
			raise e

	@property
	def acl6totpktsdenied(self) :
		ur"""Packets dropped because they match IPv6 ACLs with processing mode set to DENY.
		"""
		try :
			return self._acl6totpktsdenied
		except Exception as e:
			raise e

	@property
	def acl6totcount(self) :
		ur"""Total number of ACL6 rules configured.
		"""
		try :
			return self._acl6totcount
		except Exception as e:
			raise e

	@property
	def acl6totpktsallowed(self) :
		ur"""Packets matching IPv6 ACLs with processing mode set to ALLOW. NetScaler processes these packets.
		"""
		try :
			return self._acl6totpktsallowed
		except Exception as e:
			raise e

	@property
	def acl6pktsdeniedrate(self) :
		ur"""Rate (/s) counter for acl6totpktsdenied.
		"""
		try :
			return self._acl6pktsdeniedrate
		except Exception as e:
			raise e

	@property
	def acl6hitsrate(self) :
		ur"""Rate (/s) counter for acl6tothits.
		"""
		try :
			return self._acl6hitsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsacl6_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsacl6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.acl6name is not None :
				return str(self.acl6name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all nsacl6_stats resources that are configured on netscaler.
		"""
		try :
			obj = nsacl6_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.acl6name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class nsacl6_response(base_response) :
	def __init__(self, length=1) :
		self.nsacl6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsacl6 = [nsacl6_stats() for _ in range(length)]

