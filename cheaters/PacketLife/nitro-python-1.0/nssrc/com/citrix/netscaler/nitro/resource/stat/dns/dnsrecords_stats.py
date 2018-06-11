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

class dnsrecords_stats(base_resource) :
	def __init__(self) :
		self._dnsrecordtype = ""
		self._clearstats = ""
		self._dnstotentries = 0
		self._dnstotupdates = 0
		self._dnstotresponses = 0
		self._dnstotrequests = 0
		self._dnscurentries = 0
		self._dnstoterrlimits = 0
		self._dnstoterrrespform = 0
		self._dnstoterraliasex = 0
		self._dnstoterrnodomains = 0
		self._dnscurrecords = 0

	@property
	def dnsrecordtype(self) :
		ur"""Display statistics for the specified DNS record or query type or, if a record or query type is not specified, statistics for all record types supported on the NetScaler appliance.
		"""
		try :
			return self._dnsrecordtype
		except Exception as e:
			raise e

	@dnsrecordtype.setter
	def dnsrecordtype(self, dnsrecordtype) :
		ur"""Display statistics for the specified DNS record or query type or, if a record or query type is not specified, statistics for all record types supported on the NetScaler appliance.
		"""
		try :
			self._dnsrecordtype = dnsrecordtype
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
	def dnscurentries(self) :
		ur"""Current number of DNS entries.
		"""
		try :
			return self._dnscurentries
		except Exception as e:
			raise e

	@property
	def dnstotupdates(self) :
		ur"""Total number of DNS proactive updates.
		"""
		try :
			return self._dnstotupdates
		except Exception as e:
			raise e

	@property
	def dnstotrequests(self) :
		ur"""Total number of DNS queries recieved.
		"""
		try :
			return self._dnstotrequests
		except Exception as e:
			raise e

	@property
	def dnstoterraliasex(self) :
		ur"""Total number of times we have recieved non-cname record for a domain for which an alias exists.
		"""
		try :
			return self._dnstoterraliasex
		except Exception as e:
			raise e

	@property
	def dnstoterrrespform(self) :
		ur"""Total number of times we have recieved malformed responses from the backend.
		"""
		try :
			return self._dnstoterrrespform
		except Exception as e:
			raise e

	@property
	def dnstotentries(self) :
		ur"""Total number of DNS record entries.
		"""
		try :
			return self._dnstotentries
		except Exception as e:
			raise e

	@property
	def dnscurrecords(self) :
		ur"""Current number of DNS Records.
		"""
		try :
			return self._dnscurrecords
		except Exception as e:
			raise e

	@property
	def dnstoterrnodomains(self) :
		ur"""Total number of cache misses.
		"""
		try :
			return self._dnstoterrnodomains
		except Exception as e:
			raise e

	@property
	def dnstoterrlimits(self) :
		ur"""Total number of times we have recieved dns record with more entries than we support.
		"""
		try :
			return self._dnstoterrlimits
		except Exception as e:
			raise e

	@property
	def dnstotresponses(self) :
		ur"""Total number of DNS server responses.
		"""
		try :
			return self._dnstotresponses
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsrecords_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsrecords
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.dnsrecordtype is not None :
				return str(self.dnsrecordtype)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all dnsrecords_stats resources that are configured on netscaler.
		"""
		try :
			obj = dnsrecords_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.dnsrecordtype = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class dnsrecords_response(base_response) :
	def __init__(self, length=1) :
		self.dnsrecords = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsrecords = [dnsrecords_stats() for _ in range(length)]

