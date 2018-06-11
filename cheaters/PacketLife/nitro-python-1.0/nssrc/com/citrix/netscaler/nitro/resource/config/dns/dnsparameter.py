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

class dnsparameter(base_resource) :
	""" Configuration for DNS parameter resource. """
	def __init__(self) :
		self._retries = 0
		self._minttl = 0
		self._maxttl = 0
		self._cacherecords = ""
		self._namelookuppriority = ""
		self._recursion = ""
		self._resolutionorder = ""
		self._dnssec = ""
		self._maxpipeline = 0
		self._dnsrootreferral = ""
		self._dns64timeout = 0

	@property
	def retries(self) :
		ur"""Maximum number of retry attempts when no response is received for a query sent to a name server. Applies to end resolver and forwarder configurations.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  5.
		"""
		try :
			return self._retries
		except Exception as e:
			raise e

	@retries.setter
	def retries(self, retries) :
		ur"""Maximum number of retry attempts when no response is received for a query sent to a name server. Applies to end resolver and forwarder configurations.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  5
		"""
		try :
			self._retries = retries
		except Exception as e:
			raise e

	@property
	def minttl(self) :
		ur"""Minimum permissible time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is lower than the value configured for minTTL, the TTL of the record is set to the value of minTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Maximum length =  604800.
		"""
		try :
			return self._minttl
		except Exception as e:
			raise e

	@minttl.setter
	def minttl(self, minttl) :
		ur"""Minimum permissible time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is lower than the value configured for minTTL, the TTL of the record is set to the value of minTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Maximum length =  604800
		"""
		try :
			self._minttl = minttl
		except Exception as e:
			raise e

	@property
	def maxttl(self) :
		ur"""Maximum time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is higher than the value configured for maxTTL, the TTL of the record is set to the value of maxTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Default value: 604800<br/>Minimum length =  1<br/>Maximum length =  604800.
		"""
		try :
			return self._maxttl
		except Exception as e:
			raise e

	@maxttl.setter
	def maxttl(self, maxttl) :
		ur"""Maximum time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is higher than the value configured for maxTTL, the TTL of the record is set to the value of maxTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Default value: 604800<br/>Minimum length =  1<br/>Maximum length =  604800
		"""
		try :
			self._maxttl = maxttl
		except Exception as e:
			raise e

	@property
	def cacherecords(self) :
		ur"""Cache resource records in the DNS cache. Applies to resource records obtained through proxy configurations only. End resolver and forwarder configurations always cache records in the DNS cache, and you cannot disable this behavior. When you disable record caching, the appliance stops caching server responses. However, cached records are not flushed. The appliance does not serve requests from the cache until record caching is enabled again.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacherecords
		except Exception as e:
			raise e

	@cacherecords.setter
	def cacherecords(self, cacherecords) :
		ur"""Cache resource records in the DNS cache. Applies to resource records obtained through proxy configurations only. End resolver and forwarder configurations always cache records in the DNS cache, and you cannot disable this behavior. When you disable record caching, the appliance stops caching server responses. However, cached records are not flushed. The appliance does not serve requests from the cache until record caching is enabled again.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._cacherecords = cacherecords
		except Exception as e:
			raise e

	@property
	def namelookuppriority(self) :
		ur"""Type of lookup (DNS or WINS) to attempt first. If the first-priority lookup fails, the second-priority lookup is attempted. Used only by the SSL VPN feature.<br/>Default value: WINS<br/>Possible values = WINS, DNS.
		"""
		try :
			return self._namelookuppriority
		except Exception as e:
			raise e

	@namelookuppriority.setter
	def namelookuppriority(self, namelookuppriority) :
		ur"""Type of lookup (DNS or WINS) to attempt first. If the first-priority lookup fails, the second-priority lookup is attempted. Used only by the SSL VPN feature.<br/>Default value: WINS<br/>Possible values = WINS, DNS
		"""
		try :
			self._namelookuppriority = namelookuppriority
		except Exception as e:
			raise e

	@property
	def recursion(self) :
		ur"""Function as an end resolver and recursively resolve queries for domains that are not hosted on the NetScaler appliance. Also resolve queries recursively when the external name servers configured on the appliance (for a forwarder configuration) are unavailable. When external name servers are unavailable, the appliance queries a root server and resolves the request recursively, as it does for an end resolver configuration.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._recursion
		except Exception as e:
			raise e

	@recursion.setter
	def recursion(self, recursion) :
		ur"""Function as an end resolver and recursively resolve queries for domains that are not hosted on the NetScaler appliance. Also resolve queries recursively when the external name servers configured on the appliance (for a forwarder configuration) are unavailable. When external name servers are unavailable, the appliance queries a root server and resolves the request recursively, as it does for an end resolver configuration.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._recursion = recursion
		except Exception as e:
			raise e

	@property
	def resolutionorder(self) :
		ur"""Type of DNS queries (A, AAAA, or both) to generate during the routine functioning of certain NetScaler features, such as SSL VPN, cache redirection, and the integrated cache. The queries are sent to the external name servers that are configured for the forwarder function. If you specify both query types, you can also specify the order. Available settings function as follows:
		* OnlyAQuery. Send queries for IPv4 address records (A records) only. 
		* OnlyAAAAQuery. Send queries for IPv6 address records (AAAA records) instead of queries for IPv4 address records (A records).
		* AThenAAAAQuery. Send a query for an A record, and then send a query for an AAAA record if the query for the A record results in a NODATA response from the name server.
		* AAAAThenAQuery. Send a query for an AAAA record, and then send a query for an A record if the query for the AAAA record results in a NODATA response from the name server.<br/>Default value: OnlyAQuery<br/>Possible values = OnlyAQuery, OnlyAAAAQuery, AThenAAAAQuery, AAAAThenAQuery.
		"""
		try :
			return self._resolutionorder
		except Exception as e:
			raise e

	@resolutionorder.setter
	def resolutionorder(self, resolutionorder) :
		ur"""Type of DNS queries (A, AAAA, or both) to generate during the routine functioning of certain NetScaler features, such as SSL VPN, cache redirection, and the integrated cache. The queries are sent to the external name servers that are configured for the forwarder function. If you specify both query types, you can also specify the order. Available settings function as follows:
		* OnlyAQuery. Send queries for IPv4 address records (A records) only. 
		* OnlyAAAAQuery. Send queries for IPv6 address records (AAAA records) instead of queries for IPv4 address records (A records).
		* AThenAAAAQuery. Send a query for an A record, and then send a query for an AAAA record if the query for the A record results in a NODATA response from the name server.
		* AAAAThenAQuery. Send a query for an AAAA record, and then send a query for an A record if the query for the AAAA record results in a NODATA response from the name server.<br/>Default value: OnlyAQuery<br/>Possible values = OnlyAQuery, OnlyAAAAQuery, AThenAAAAQuery, AAAAThenAQuery
		"""
		try :
			self._resolutionorder = resolutionorder
		except Exception as e:
			raise e

	@property
	def dnssec(self) :
		ur"""Enable or disable the Domain Name System Security Extensions (DNSSEC) feature on the appliance. Note: Even when the DNSSEC feature is enabled, forwarder configurations (used by internal NetScaler features such as SSL VPN and Cache Redirection for name resolution) do not support the DNSSEC OK (DO) bit in the EDNS0 OPT header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnssec
		except Exception as e:
			raise e

	@dnssec.setter
	def dnssec(self, dnssec) :
		ur"""Enable or disable the Domain Name System Security Extensions (DNSSEC) feature on the appliance. Note: Even when the DNSSEC feature is enabled, forwarder configurations (used by internal NetScaler features such as SSL VPN and Cache Redirection for name resolution) do not support the DNSSEC OK (DO) bit in the EDNS0 OPT header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnssec = dnssec
		except Exception as e:
			raise e

	@property
	def maxpipeline(self) :
		ur"""Maximum number of concurrent DNS requests to allow on a single client connection, which is identified by the <clientip:port>-<vserver ip:port> tuple. A value of 0 (zero) applies no limit to the number of concurrent DNS requests allowed on a single client connection.
		"""
		try :
			return self._maxpipeline
		except Exception as e:
			raise e

	@maxpipeline.setter
	def maxpipeline(self, maxpipeline) :
		ur"""Maximum number of concurrent DNS requests to allow on a single client connection, which is identified by the <clientip:port>-<vserver ip:port> tuple. A value of 0 (zero) applies no limit to the number of concurrent DNS requests allowed on a single client connection.
		"""
		try :
			self._maxpipeline = maxpipeline
		except Exception as e:
			raise e

	@property
	def dnsrootreferral(self) :
		ur"""Send a root referral if a client queries a domain name that is unrelated to the domains configured/cached on the NetScaler appliance. If the setting is disabled, the appliance sends a blank response instead of a root referral. Applicable to domains for which the appliance is authoritative. Disable the parameter when the appliance is under attack from a client that is sending a flood of queries for unrelated domains.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnsrootreferral
		except Exception as e:
			raise e

	@dnsrootreferral.setter
	def dnsrootreferral(self, dnsrootreferral) :
		ur"""Send a root referral if a client queries a domain name that is unrelated to the domains configured/cached on the NetScaler appliance. If the setting is disabled, the appliance sends a blank response instead of a root referral. Applicable to domains for which the appliance is authoritative. Disable the parameter when the appliance is under attack from a client that is sending a flood of queries for unrelated domains.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnsrootreferral = dnsrootreferral
		except Exception as e:
			raise e

	@property
	def dns64timeout(self) :
		ur"""While doing DNS64 resolution, this parameter specifies the time to wait before sending an A query if no response is received from backend DNS server for AAAA query.<br/>Maximum length =  10000.
		"""
		try :
			return self._dns64timeout
		except Exception as e:
			raise e

	@dns64timeout.setter
	def dns64timeout(self, dns64timeout) :
		ur"""While doing DNS64 resolution, this parameter specifies the time to wait before sending an A query if no response is received from backend DNS server for AAAA query.<br/>Maximum length =  10000
		"""
		try :
			self._dns64timeout = dns64timeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsparameter
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
	def update(cls, client, resource) :
		ur""" Use this API to update dnsparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnsparameter()
				updateresource.retries = resource.retries
				updateresource.minttl = resource.minttl
				updateresource.maxttl = resource.maxttl
				updateresource.cacherecords = resource.cacherecords
				updateresource.namelookuppriority = resource.namelookuppriority
				updateresource.recursion = resource.recursion
				updateresource.resolutionorder = resource.resolutionorder
				updateresource.dnssec = resource.dnssec
				updateresource.maxpipeline = resource.maxpipeline
				updateresource.dnsrootreferral = resource.dnsrootreferral
				updateresource.dns64timeout = resource.dns64timeout
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of dnsparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnsparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnsparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Cacherecords:
		YES = "YES"
		NO = "NO"

	class Recursion:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Resolutionorder:
		OnlyAQuery = "OnlyAQuery"
		OnlyAAAAQuery = "OnlyAAAAQuery"
		AThenAAAAQuery = "AThenAAAAQuery"
		AAAAThenAQuery = "AAAAThenAQuery"

	class Namelookuppriority:
		WINS = "WINS"
		DNS = "DNS"

	class Dnsrootreferral:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dnssec:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class dnsparameter_response(base_response) :
	def __init__(self, length=1) :
		self.dnsparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsparameter = [dnsparameter() for _ in range(length)]

