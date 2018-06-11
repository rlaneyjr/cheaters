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

class dns_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._dnstotqueries = 0
		self._dnsqueriesrate = 0
		self._dnstotmultiquery = 0
		self._dnstotanswers = 0
		self._dnsanswersrate = 0
		self._dnstotserverresponse = 0
		self._dnsserverresponserate = 0
		self._dnstotrecupdate = 0
		self._dnstotauthans = 0
		self._dnstotserverquery = 0
		self._dnsserverqueryrate = 0
		self._dnstotcacheflush = 0
		self._dnstotcacheentriesflush = 0
		self._dnscurnoauthentries = 0
		self._dnscurauthentries = 0
		self._dnstotauthnonames = 0
		self._dnstotunsupportedresponseclass = 0
		self._dnstotinvalidqueryformat = 0
		self._dnstotstrayanswer = 0
		self._dnstotresponsebadlen = 0
		self._dnstotreqrefusals = 0
		self._dnserrnullattack = 0
		self._dnstotunsupportedresponsetype = 0
		self._dnstotunsupportedqueryclass = 0
		self._dnstotnonauthnodatas = 0
		self._dnstotnodataresps = 0
		self._dnstotmultiquerydisableerror = 0
		self._dnstotothererrors = 0
		self._dns64totqueries = 0
		self._dns64queriesrate = 0
		self._dns64totanswers = 0
		self._dns64answersrate = 0
		self._dns64totrwanswers = 0
		self._dns64rwanswersrate = 0
		self._dns64totresponses = 0
		self._dns64responsesrate = 0
		self._dns64totgslbqueries = 0
		self._dns64gslbqueriesrate = 0
		self._dns64totgslbanswers = 0
		self._dns64gslbanswersrate = 0
		self._dns64tottcanswers = 0
		self._dns64tcanswersrate = 0
		self._dns64totsvraqueries = 0
		self._dns64svraqueriesrate = 0
		self._dns64totaaaabypass = 0
		self._dns64aaaabypassrate = 0
		self._dns64tottcpqueries = 0
		self._dns64tcpqueriesrate = 0
		self._dns64activepolicies = 0
		self._dns64totnodataresp = 0
		self._dns64nodataresprate = 0
		self._dnstotnsrecqueries = 0
		self._dnsnsrecqueriesrate = 0
		self._dnstotsoarecqueries = 0
		self._dnssoarecqueriesrate = 0
		self._dnstotptrrecqueries = 0
		self._dnsptrrecqueriesrate = 0
		self._dnstotsrvrecqueries = 0
		self._dnssrvrecqueriesrate = 0
		self._dnstotaresponse = 0
		self._dnsaresponserate = 0
		self._dnstotcnameresponse = 0
		self._dnscnameresponserate = 0
		self._dnstotmxresponse = 0
		self._dnsmxresponserate = 0
		self._dnstotanyresponse = 0
		self._dnsanyresponserate = 0
		self._dnstotnsrecupdate = 0
		self._dnstotsoarecupdate = 0
		self._dnstotptrrecupdate = 0
		self._dnstotsrvrecupdate = 0
		self._dnstotaaaarecqueries = 0
		self._dnsaaaarecqueriesrate = 0
		self._dnstotarecqueries = 0
		self._dnsarecqueriesrate = 0
		self._dnstotcnamerecqueries = 0
		self._dnscnamerecqueriesrate = 0
		self._dnstotmxrecqueries = 0
		self._dnsmxrecqueriesrate = 0
		self._dnstotanyqueries = 0
		self._dnsanyqueriesrate = 0
		self._dnstotaaaaresponse = 0
		self._dnsaaaaresponserate = 0
		self._dnstotnsresponse = 0
		self._dnsnsresponserate = 0
		self._dnstotsoaresponse = 0
		self._dnssoaresponserate = 0
		self._dnstotptrresponse = 0
		self._dnsptrresponserate = 0
		self._dnstotsrvresponse = 0
		self._dnssrvresponserate = 0
		self._dnstotaaaarecupdate = 0
		self._dnstotarecupdate = 0
		self._dnstotmxrecupdate = 0
		self._dnstotcnamerecupdate = 0
		self._dnscuraaaarecord = 0
		self._dnscurarecord = 0
		self._dnscurmxrecord = 0
		self._dnscurcnamerecord = 0
		self._dnscurnsrecord = 0
		self._dnscursoarecord = 0
		self._dnscurptrrecord = 0
		self._dnscursrvrecord = 0
		self._dnstotaaaarecfailed = 0
		self._dnstotarecfailed = 0
		self._dnstotmxrecfailed = 0
		self._dnstotptrrecfailed = 0
		self._dnstotnsrecfailed = 0
		self._dnstotcnamerecfailed = 0
		self._dnstotsoarecfailed = 0
		self._dnstotsrvrecfailed = 0
		self._dnstotanyrecfailed = 0
		self._dnstotunsupportedqueries = 0

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
	def dnstotcnameresponse(self) :
		ur"""Total number of CNAME responses received.
		"""
		try :
			return self._dnstotcnameresponse
		except Exception as e:
			raise e

	@property
	def dnsaresponserate(self) :
		ur"""Rate (/s) counter for dnstotaresponse.
		"""
		try :
			return self._dnsaresponserate
		except Exception as e:
			raise e

	@property
	def dns64rwanswersrate(self) :
		ur"""Rate (/s) counter for dns64totrwanswers.
		"""
		try :
			return self._dns64rwanswersrate
		except Exception as e:
			raise e

	@property
	def dnstotaaaarecupdate(self) :
		ur"""Total number of AAAA record updates.
		"""
		try :
			return self._dnstotaaaarecupdate
		except Exception as e:
			raise e

	@property
	def dnstotptrrecupdate(self) :
		ur"""Total number of PTR record updates.
		"""
		try :
			return self._dnstotptrrecupdate
		except Exception as e:
			raise e

	@property
	def dns64nodataresprate(self) :
		ur"""Rate (/s) counter for dns64totnodataresp.
		"""
		try :
			return self._dns64nodataresprate
		except Exception as e:
			raise e

	@property
	def dnserrnullattack(self) :
		ur"""Total number of queries received where all the counts are 0.
		"""
		try :
			return self._dnserrnullattack
		except Exception as e:
			raise e

	@property
	def dnstotunsupportedqueries(self) :
		ur"""Total number of requests for which query type requested was unsupported.
		"""
		try :
			return self._dnstotunsupportedqueries
		except Exception as e:
			raise e

	@property
	def dnstotauthnonames(self) :
		ur"""Number of queries for which no record was found.
		"""
		try :
			return self._dnstotauthnonames
		except Exception as e:
			raise e

	@property
	def dnstotmxrecupdate(self) :
		ur"""Total number of MX record updates.
		"""
		try :
			return self._dnstotmxrecupdate
		except Exception as e:
			raise e

	@property
	def dnstotanyqueries(self) :
		ur"""Total number of ANY queries received.
		"""
		try :
			return self._dnstotanyqueries
		except Exception as e:
			raise e

	@property
	def dns64totrwanswers(self) :
		ur"""Total number of DNS64 answers served after rewriting the response.
		"""
		try :
			return self._dns64totrwanswers
		except Exception as e:
			raise e

	@property
	def dnstotstrayanswer(self) :
		ur"""Total number of stray answers.
		"""
		try :
			return self._dnstotstrayanswer
		except Exception as e:
			raise e

	@property
	def dnstotptrrecfailed(self) :
		ur"""Total number of times PTR record lookup failed.
		"""
		try :
			return self._dnstotptrrecfailed
		except Exception as e:
			raise e

	@property
	def dns64activepolicies(self) :
		ur"""Total number of active dns64 policies.
		"""
		try :
			return self._dns64activepolicies
		except Exception as e:
			raise e

	@property
	def dnstotcnamerecupdate(self) :
		ur"""Total number of CNAME record updates.
		"""
		try :
			return self._dnstotcnamerecupdate
		except Exception as e:
			raise e

	@property
	def dnscursoarecord(self) :
		ur"""Total number of SOA records.
		"""
		try :
			return self._dnscursoarecord
		except Exception as e:
			raise e

	@property
	def dnstotcacheentriesflush(self) :
		ur"""Total number of cache entries flushed.
		"""
		try :
			return self._dnstotcacheentriesflush
		except Exception as e:
			raise e

	@property
	def dnsaaaaresponserate(self) :
		ur"""Rate (/s) counter for dnstotaaaaresponse.
		"""
		try :
			return self._dnsaaaaresponserate
		except Exception as e:
			raise e

	@property
	def dnsaaaarecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotaaaarecqueries.
		"""
		try :
			return self._dnsaaaarecqueriesrate
		except Exception as e:
			raise e

	@property
	def dnstotmxrecqueries(self) :
		ur"""Total number of MX queries received.
		"""
		try :
			return self._dnstotmxrecqueries
		except Exception as e:
			raise e

	@property
	def dnstotsoarecqueries(self) :
		ur"""Total number of SOA queries received.
		"""
		try :
			return self._dnstotsoarecqueries
		except Exception as e:
			raise e

	@property
	def dnscurarecord(self) :
		ur"""Total number of A records.
		"""
		try :
			return self._dnscurarecord
		except Exception as e:
			raise e

	@property
	def dnstotinvalidqueryformat(self) :
		ur"""Total number of queries whose format was invalid.
		"""
		try :
			return self._dnstotinvalidqueryformat
		except Exception as e:
			raise e

	@property
	def dnstotsrvrecfailed(self) :
		ur"""Total number of times SRV record lookup failed.
		"""
		try :
			return self._dnstotsrvrecfailed
		except Exception as e:
			raise e

	@property
	def dnsarecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotarecqueries.
		"""
		try :
			return self._dnsarecqueriesrate
		except Exception as e:
			raise e

	@property
	def dnstotsoaresponse(self) :
		ur"""Total number of SOA responses received.
		"""
		try :
			return self._dnstotsoaresponse
		except Exception as e:
			raise e

	@property
	def dnstotserverresponse(self) :
		ur"""Total number of Server responses received.
		"""
		try :
			return self._dnstotserverresponse
		except Exception as e:
			raise e

	@property
	def dnsanyqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotanyqueries.
		"""
		try :
			return self._dnsanyqueriesrate
		except Exception as e:
			raise e

	@property
	def dnscurauthentries(self) :
		ur"""Total number of authoritative entries.
		"""
		try :
			return self._dnscurauthentries
		except Exception as e:
			raise e

	@property
	def dnstotmxresponse(self) :
		ur"""Total number of MX responses received.
		"""
		try :
			return self._dnstotmxresponse
		except Exception as e:
			raise e

	@property
	def dnstotptrrecqueries(self) :
		ur"""Total number of PTR queries received.
		"""
		try :
			return self._dnstotptrrecqueries
		except Exception as e:
			raise e

	@property
	def dnstotunsupportedqueryclass(self) :
		ur"""Total number of queries for which query class was unsupported.
		"""
		try :
			return self._dnstotunsupportedqueryclass
		except Exception as e:
			raise e

	@property
	def dnsptrresponserate(self) :
		ur"""Rate (/s) counter for dnstotptrresponse.
		"""
		try :
			return self._dnsptrresponserate
		except Exception as e:
			raise e

	@property
	def dnssoarecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotsoarecqueries.
		"""
		try :
			return self._dnssoarecqueriesrate
		except Exception as e:
			raise e

	@property
	def dns64totgslbanswers(self) :
		ur"""Total number of DNS64 queries served.
		"""
		try :
			return self._dns64totgslbanswers
		except Exception as e:
			raise e

	@property
	def dns64answersrate(self) :
		ur"""Rate (/s) counter for dns64totanswers.
		"""
		try :
			return self._dns64answersrate
		except Exception as e:
			raise e

	@property
	def dns64totqueries(self) :
		ur"""Total number of DNS64 queries recieved.
		"""
		try :
			return self._dns64totqueries
		except Exception as e:
			raise e

	@property
	def dnsptrrecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotptrrecqueries.
		"""
		try :
			return self._dnsptrrecqueriesrate
		except Exception as e:
			raise e

	@property
	def dnstotsoarecfailed(self) :
		ur"""Total number of times SOA record lookup failed.
		"""
		try :
			return self._dnstotsoarecfailed
		except Exception as e:
			raise e

	@property
	def dns64tottcpqueries(self) :
		ur"""Total number of dns64 queries over TCP.
		"""
		try :
			return self._dns64tottcpqueries
		except Exception as e:
			raise e

	@property
	def dnstotaaaarecqueries(self) :
		ur"""Total number of AAAA queries received.
		"""
		try :
			return self._dnstotaaaarecqueries
		except Exception as e:
			raise e

	@property
	def dns64responsesrate(self) :
		ur"""Rate (/s) counter for dns64totresponses.
		"""
		try :
			return self._dns64responsesrate
		except Exception as e:
			raise e

	@property
	def dnstotmxrecfailed(self) :
		ur"""Total number of times MX record lookup failed.
		"""
		try :
			return self._dnstotmxrecfailed
		except Exception as e:
			raise e

	@property
	def dns64tottcanswers(self) :
		ur"""Total number of Answers served with TC bit set in DNS64 context.
		"""
		try :
			return self._dns64tottcanswers
		except Exception as e:
			raise e

	@property
	def dnstotaaaarecfailed(self) :
		ur"""Total number of times AAAA record lookup failed.
		"""
		try :
			return self._dnstotaaaarecfailed
		except Exception as e:
			raise e

	@property
	def dnssrvresponserate(self) :
		ur"""Rate (/s) counter for dnstotsrvresponse.
		"""
		try :
			return self._dnssrvresponserate
		except Exception as e:
			raise e

	@property
	def dnsnsrecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotnsrecqueries.
		"""
		try :
			return self._dnsnsrecqueriesrate
		except Exception as e:
			raise e

	@property
	def dnstotserverquery(self) :
		ur"""Total number of Server queries sent.
		"""
		try :
			return self._dnstotserverquery
		except Exception as e:
			raise e

	@property
	def dnssoaresponserate(self) :
		ur"""Rate (/s) counter for dnstotsoaresponse.
		"""
		try :
			return self._dnssoaresponserate
		except Exception as e:
			raise e

	@property
	def dnstotmultiquery(self) :
		ur"""Total number of Multi Query request received.
		"""
		try :
			return self._dnstotmultiquery
		except Exception as e:
			raise e

	@property
	def dnscuraaaarecord(self) :
		ur"""Total number of AAAA records.
		"""
		try :
			return self._dnscuraaaarecord
		except Exception as e:
			raise e

	@property
	def dnsqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotqueries.
		"""
		try :
			return self._dnsqueriesrate
		except Exception as e:
			raise e

	@property
	def dns64gslbqueriesrate(self) :
		ur"""Rate (/s) counter for dns64totgslbqueries.
		"""
		try :
			return self._dns64gslbqueriesrate
		except Exception as e:
			raise e

	@property
	def dnsanyresponserate(self) :
		ur"""Rate (/s) counter for dnstotanyresponse.
		"""
		try :
			return self._dnsanyresponserate
		except Exception as e:
			raise e

	@property
	def dnsanswersrate(self) :
		ur"""Rate (/s) counter for dnstotanswers.
		"""
		try :
			return self._dnsanswersrate
		except Exception as e:
			raise e

	@property
	def dnstotarecupdate(self) :
		ur"""Total number of A record updates.
		"""
		try :
			return self._dnstotarecupdate
		except Exception as e:
			raise e

	@property
	def dnscnameresponserate(self) :
		ur"""Rate (/s) counter for dnstotcnameresponse.
		"""
		try :
			return self._dnscnameresponserate
		except Exception as e:
			raise e

	@property
	def dnstotothererrors(self) :
		ur"""Total number of other errors. .
		"""
		try :
			return self._dnstotothererrors
		except Exception as e:
			raise e

	@property
	def dnstotnsrecfailed(self) :
		ur"""Total number of times NS record lookup failed.
		"""
		try :
			return self._dnstotnsrecfailed
		except Exception as e:
			raise e

	@property
	def dnscurcnamerecord(self) :
		ur"""Total number of CNAME records.
		"""
		try :
			return self._dnscurcnamerecord
		except Exception as e:
			raise e

	@property
	def dnscurnoauthentries(self) :
		ur"""Total number of non-authoritative entries.
		"""
		try :
			return self._dnscurnoauthentries
		except Exception as e:
			raise e

	@property
	def dnstotresponsebadlen(self) :
		ur"""Number of DNS responses received with invalid resoure data length.
		"""
		try :
			return self._dnstotresponsebadlen
		except Exception as e:
			raise e

	@property
	def dns64totaaaabypass(self) :
		ur"""Total number of times AAAA query has been bypassed in DNS64 trnsaction.
		"""
		try :
			return self._dns64totaaaabypass
		except Exception as e:
			raise e

	@property
	def dns64tcpqueriesrate(self) :
		ur"""Rate (/s) counter for dns64tottcpqueries.
		"""
		try :
			return self._dns64tcpqueriesrate
		except Exception as e:
			raise e

	@property
	def dnstotaaaaresponse(self) :
		ur"""Total number of AAAA responses received.
		"""
		try :
			return self._dnstotaaaaresponse
		except Exception as e:
			raise e

	@property
	def dns64gslbanswersrate(self) :
		ur"""Rate (/s) counter for dns64totgslbanswers.
		"""
		try :
			return self._dns64gslbanswersrate
		except Exception as e:
			raise e

	@property
	def dnstotunsupportedresponsetype(self) :
		ur"""Total number of responses for which response type requested was unsupported.
		"""
		try :
			return self._dnstotunsupportedresponsetype
		except Exception as e:
			raise e

	@property
	def dns64totsvraqueries(self) :
		ur"""Total number of Queries sent by DNS64 module to backend.
		"""
		try :
			return self._dns64totsvraqueries
		except Exception as e:
			raise e

	@property
	def dns64totresponses(self) :
		ur"""Total number of responses recieved from backend in DNS64 context.
		"""
		try :
			return self._dns64totresponses
		except Exception as e:
			raise e

	@property
	def dnstotnsrecqueries(self) :
		ur"""Total number of NS queries received.
		"""
		try :
			return self._dnstotnsrecqueries
		except Exception as e:
			raise e

	@property
	def dns64totanswers(self) :
		ur"""Total number of DNS64 answers served.
		"""
		try :
			return self._dns64totanswers
		except Exception as e:
			raise e

	@property
	def dnscursrvrecord(self) :
		ur"""Total number of SRV records.
		"""
		try :
			return self._dnscursrvrecord
		except Exception as e:
			raise e

	@property
	def dnscurptrrecord(self) :
		ur"""Total number of PTR records.
		"""
		try :
			return self._dnscurptrrecord
		except Exception as e:
			raise e

	@property
	def dnstotanyresponse(self) :
		ur"""Total number of ANY responses received.
		"""
		try :
			return self._dnstotanyresponse
		except Exception as e:
			raise e

	@property
	def dnstotanyrecfailed(self) :
		ur"""Total number of times ANY query lookup failed.
		"""
		try :
			return self._dnstotanyrecfailed
		except Exception as e:
			raise e

	@property
	def dns64aaaabypassrate(self) :
		ur"""Rate (/s) counter for dns64totaaaabypass.
		"""
		try :
			return self._dns64aaaabypassrate
		except Exception as e:
			raise e

	@property
	def dnstotnsresponse(self) :
		ur"""Total number of NS responses received.
		"""
		try :
			return self._dnstotnsresponse
		except Exception as e:
			raise e

	@property
	def dnssrvrecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotsrvrecqueries.
		"""
		try :
			return self._dnssrvrecqueriesrate
		except Exception as e:
			raise e

	@property
	def dnstotnsrecupdate(self) :
		ur"""Total number of NS record updates.
		"""
		try :
			return self._dnstotnsrecupdate
		except Exception as e:
			raise e

	@property
	def dnstotcnamerecqueries(self) :
		ur"""Total number of CNAME queries received.
		"""
		try :
			return self._dnstotcnamerecqueries
		except Exception as e:
			raise e

	@property
	def dnstotmultiquerydisableerror(self) :
		ur"""Total number of times a multi query was disabled and received a multi query.
		"""
		try :
			return self._dnstotmultiquerydisableerror
		except Exception as e:
			raise e

	@property
	def dnstotarecqueries(self) :
		ur"""Total number of A queries received.
		"""
		try :
			return self._dnstotarecqueries
		except Exception as e:
			raise e

	@property
	def dnsserverresponserate(self) :
		ur"""Rate (/s) counter for dnstotserverresponse.
		"""
		try :
			return self._dnsserverresponserate
		except Exception as e:
			raise e

	@property
	def dnsnsresponserate(self) :
		ur"""Rate (/s) counter for dnstotnsresponse.
		"""
		try :
			return self._dnsnsresponserate
		except Exception as e:
			raise e

	@property
	def dnstotanswers(self) :
		ur"""Total number of DNS responses received.
		"""
		try :
			return self._dnstotanswers
		except Exception as e:
			raise e

	@property
	def dnsmxrecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotmxrecqueries.
		"""
		try :
			return self._dnsmxrecqueriesrate
		except Exception as e:
			raise e

	@property
	def dnstotcnamerecfailed(self) :
		ur"""Total number of times CNAME record lookup failed.
		"""
		try :
			return self._dnstotcnamerecfailed
		except Exception as e:
			raise e

	@property
	def dnstotsrvrecqueries(self) :
		ur"""Total number of SRV queries received.
		"""
		try :
			return self._dnstotsrvrecqueries
		except Exception as e:
			raise e

	@property
	def dnstotaresponse(self) :
		ur"""Total number of A responses received.
		"""
		try :
			return self._dnstotaresponse
		except Exception as e:
			raise e

	@property
	def dnscnamerecqueriesrate(self) :
		ur"""Rate (/s) counter for dnstotcnamerecqueries.
		"""
		try :
			return self._dnscnamerecqueriesrate
		except Exception as e:
			raise e

	@property
	def dns64totnodataresp(self) :
		ur"""Total number of responses recieved from backend with ancount 0.
		"""
		try :
			return self._dns64totnodataresp
		except Exception as e:
			raise e

	@property
	def dnstotqueries(self) :
		ur"""Total number of DNS queries received.
		"""
		try :
			return self._dnstotqueries
		except Exception as e:
			raise e

	@property
	def dnstotsrvresponse(self) :
		ur"""Total number of SRV responses received.
		"""
		try :
			return self._dnstotsrvresponse
		except Exception as e:
			raise e

	@property
	def dnstotunsupportedresponseclass(self) :
		ur"""Total number of responses for which response types were unsupported.
		"""
		try :
			return self._dnstotunsupportedresponseclass
		except Exception as e:
			raise e

	@property
	def dnstotcacheflush(self) :
		ur"""Total number of times cache was flushed.
		"""
		try :
			return self._dnstotcacheflush
		except Exception as e:
			raise e

	@property
	def dnstotarecfailed(self) :
		ur"""Total number of times A record lookup failed.
		"""
		try :
			return self._dnstotarecfailed
		except Exception as e:
			raise e

	@property
	def dnstotsrvrecupdate(self) :
		ur"""Total number of SRV record updates.
		"""
		try :
			return self._dnstotsrvrecupdate
		except Exception as e:
			raise e

	@property
	def dns64svraqueriesrate(self) :
		ur"""Rate (/s) counter for dns64totsvraqueries.
		"""
		try :
			return self._dns64svraqueriesrate
		except Exception as e:
			raise e

	@property
	def dnsserverqueryrate(self) :
		ur"""Rate (/s) counter for dnstotserverquery.
		"""
		try :
			return self._dnsserverqueryrate
		except Exception as e:
			raise e

	@property
	def dnscurnsrecord(self) :
		ur"""Total number of NS records.
		"""
		try :
			return self._dnscurnsrecord
		except Exception as e:
			raise e

	@property
	def dnstotsoarecupdate(self) :
		ur"""Total number of SOA record updates.
		"""
		try :
			return self._dnstotsoarecupdate
		except Exception as e:
			raise e

	@property
	def dns64queriesrate(self) :
		ur"""Rate (/s) counter for dns64totqueries.
		"""
		try :
			return self._dns64queriesrate
		except Exception as e:
			raise e

	@property
	def dnstotnonauthnodatas(self) :
		ur"""Total number of responses for which there was a format error.
		"""
		try :
			return self._dnstotnonauthnodatas
		except Exception as e:
			raise e

	@property
	def dnstotauthans(self) :
		ur"""Number of queries which were authoritatively answered.
		"""
		try :
			return self._dnstotauthans
		except Exception as e:
			raise e

	@property
	def dnstotreqrefusals(self) :
		ur"""Number of DNS requests refused.
		"""
		try :
			return self._dnstotreqrefusals
		except Exception as e:
			raise e

	@property
	def dnscurmxrecord(self) :
		ur"""Total number of MX records.
		"""
		try :
			return self._dnscurmxrecord
		except Exception as e:
			raise e

	@property
	def dns64tcanswersrate(self) :
		ur"""Rate (/s) counter for dns64tottcanswers.
		"""
		try :
			return self._dns64tcanswersrate
		except Exception as e:
			raise e

	@property
	def dnstotrecupdate(self) :
		ur"""Total number of record updates.
		"""
		try :
			return self._dnstotrecupdate
		except Exception as e:
			raise e

	@property
	def dns64totgslbqueries(self) :
		ur"""Total number of DNS64 queries for GSLB domain.
		"""
		try :
			return self._dns64totgslbqueries
		except Exception as e:
			raise e

	@property
	def dnstotnodataresps(self) :
		ur"""Number of DNS responses received without answer.
		"""
		try :
			return self._dnstotnodataresps
		except Exception as e:
			raise e

	@property
	def dnstotptrresponse(self) :
		ur"""Total number of PTR responses received.
		"""
		try :
			return self._dnstotptrresponse
		except Exception as e:
			raise e

	@property
	def dnsmxresponserate(self) :
		ur"""Rate (/s) counter for dnstotmxresponse.
		"""
		try :
			return self._dnsmxresponserate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dns_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dns
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
		ur""" Use this API to fetch the statistics of all dns_stats resources that are configured on netscaler.
		"""
		try :
			obj = dns_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class dns_response(base_response) :
	def __init__(self, length=1) :
		self.dns = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dns = [dns_stats() for _ in range(length)]

