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

class cache_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._cachemaxmemorykb = 0
		self._cacherecentpercentsuccessfulrevalidation = 0
		self._cacherecentpercentstoreablemiss = 0
		self._cacherecentpercentparameterizedhits = 0
		self._cacherecentpercentoriginbandwidthsaved = 0
		self._cacherecentpercenthit = 0
		self._cacherecentpercentbytehit = 0
		self._cacherecentpercent304hits = 0
		self._cacheutilizedmemorykb = 0
		self._cachemaxmemoryactivekb = 0
		self._cache64maxmemorykb = 0
		self._cachepercentpethits = 0
		self._cachetotpethits = 0
		self._cachepethitsrate = 0
		self._cachepercentparameterized304hits = 0
		self._cachetotparameterizedhits = 0
		self._cacheparameterizedhitsrate = 0
		self._cachepercentsuccessfulrevalidation = 0
		self._cachepercentstoreablemiss = 0
		self._cachetotfulltoconditionalrequest = 0
		self._cachefulltoconditionalrequestrate = 0
		self._cachetotsuccessfulrevalidation = 0
		self._cachesuccessfulrevalidationrate = 0
		self._cachetotrevalidationmiss = 0
		self._cacherevalidationmissrate = 0
		self._cachetotnonstoreablemisses = 0
		self._cachenonstoreablemissesrate = 0
		self._cachetotstoreablemisses = 0
		self._cachestoreablemissesrate = 0
		self._cachecompressedbytesserved = 0
		self._cachecompressedbytesservedrate = 0
		self._cachepercentbytehit = 0
		self._cachebytesserved = 0
		self._cachebytesservedrate = 0
		self._cachetotresponsebytes = 0
		self._cacheresponsebytesrate = 0
		self._cachepercent304hits = 0
		self._cachenummarker = 0
		self._cachepercentoriginbandwidthsaved = 0
		self._cachepercenthit = 0
		self._cachetotmisses = 0
		self._cachemissesrate = 0
		self._cachetothits = 0
		self._cachehitsrate = 0
		self._cachetotrequests = 0
		self._cacherequestsrate = 0
		self._cachenumcached = 0
		self._cachecurhits = 0
		self._cachecurmisses = 0
		self._cachetotnon304hits = 0
		self._cachenon304hitsrate = 0
		self._cachetot304hits = 0
		self._cache304hitsrate = 0
		self._cachetotsqlhits = 0
		self._cachesqlhitsrate = 0
		self._cachetotexpireatlastbyte = 0
		self._cacheexpireatlastbyterate = 0
		self._cachetotflashcachemisses = 0
		self._cacheflashcachemissesrate = 0
		self._cachetotflashcachehits = 0
		self._cacheflashcachehitsrate = 0
		self._cachetotparameterizedinvalidationrequests = 0
		self._cacheparameterizedinvalidationrequestsrate = 0
		self._cachetotnonparameterizedinvalidationrequests = 0
		self._cachenonparameterizedinvalidationrequestsrate = 0
		self._cachetotinvalidationrequests = 0
		self._cacheinvalidationrequestsrate = 0
		self._cachetotparameterizedrequests = 0
		self._cacheparameterizedrequestsrate = 0
		self._cachetotparameterizednon304hits = 0
		self._cacheparameterizednon304hitsrate = 0
		self._cachetotparameterized304hits = 0
		self._cacheparameterized304hitsrate = 0
		self._cachetotpetrequests = 0
		self._cachepetrequestsrate = 0
		self._cacheerrmemalloc = 0
		self._cachelargestresponsereceived = 0

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
	def cachehitsrate(self) :
		ur"""Rate (/s) counter for cachetothits.
		"""
		try :
			return self._cachehitsrate
		except Exception as e:
			raise e

	@property
	def cachepethitsrate(self) :
		ur"""Rate (/s) counter for cachetotpethits.
		"""
		try :
			return self._cachepethitsrate
		except Exception as e:
			raise e

	@property
	def cachetotexpireatlastbyte(self) :
		ur"""Instances of content expiring immediately after receiving the last body byte due to the Expire at Last Byte setting for the content group.
		"""
		try :
			return self._cachetotexpireatlastbyte
		except Exception as e:
			raise e

	@property
	def cachenummarker(self) :
		ur"""Marker objects created when a response exceeds the maximum or minimum size for entries in its content group or has not yet received the minimum number of hits required for items in its content group.
		"""
		try :
			return self._cachenummarker
		except Exception as e:
			raise e

	@property
	def cachecurhits(self) :
		ur"""This number should be close to the number of hits being served currently.
		"""
		try :
			return self._cachecurhits
		except Exception as e:
			raise e

	@property
	def cacheresponsebytesrate(self) :
		ur"""Rate (/s) counter for cachetotresponsebytes.
		"""
		try :
			return self._cacheresponsebytesrate
		except Exception as e:
			raise e

	@property
	def cacheutilizedmemorykb(self) :
		ur"""Amount of memory the integrated cache is currently using.
		"""
		try :
			return self._cacheutilizedmemorykb
		except Exception as e:
			raise e

	@property
	def cachetotnonparameterizedinvalidationrequests(self) :
		ur"""Requests that match an invalidation policy where the invalGroups parameter is configured and expires one or more content groups.
		"""
		try :
			return self._cachetotnonparameterizedinvalidationrequests
		except Exception as e:
			raise e

	@property
	def cachepercentpethits(self) :
		ur"""Percentage of cache hits in content groups that have Poll Every Time enabled, relative to all searches of content groups with Poll Every Time enabled. .
		"""
		try :
			return self._cachepercentpethits
		except Exception as e:
			raise e

	@property
	def cachebytesserved(self) :
		ur"""Total number of bytes served from the integrated cache.
		"""
		try :
			return self._cachebytesserved
		except Exception as e:
			raise e

	@property
	def cachetotparameterizednon304hits(self) :
		ur"""Parameterized requests resulting in a full response (not status code 304: Object Not Updated) served from the cache.
		"""
		try :
			return self._cachetotparameterizednon304hits
		except Exception as e:
			raise e

	@property
	def cachebytesservedrate(self) :
		ur"""Rate (/s) counter for cachebytesserved.
		"""
		try :
			return self._cachebytesservedrate
		except Exception as e:
			raise e

	@property
	def cachepercent304hits(self) :
		ur"""304 responses as a percentage of all responses that the NetScaler served.
		"""
		try :
			return self._cachepercent304hits
		except Exception as e:
			raise e

	@property
	def cachepercentbytehit(self) :
		ur"""Bytes served from the cache divided by total bytes served to the client. If compression is On in the NetScaler, this ratio may not reflect the bytes served by the compression module. If the compression is Off, this ratio is the same as cachePercentOriginBandwidthSaved.
		"""
		try :
			return self._cachepercentbytehit
		except Exception as e:
			raise e

	@property
	def cachepercentstoreablemiss(self) :
		ur"""Responses that were fetched from the origin, stored in the cache, and then served to the client, as a percentage of all cache misses.
		"""
		try :
			return self._cachepercentstoreablemiss
		except Exception as e:
			raise e

	@property
	def cachetotpetrequests(self) :
		ur"""Requests that triggered a search of a content group that has Poll Every Time (PET) enabled (always consult the origin server before serving cached data).
		"""
		try :
			return self._cachetotpetrequests
		except Exception as e:
			raise e

	@property
	def cachecompressedbytesserved(self) :
		ur"""Number of compressed bytes served from the cache.
		"""
		try :
			return self._cachecompressedbytesserved
		except Exception as e:
			raise e

	@property
	def cachetotresponsebytes(self) :
		ur"""Total number of HTTP response bytes served by NetScaler from both the origin and the cache.
		"""
		try :
			return self._cachetotresponsebytes
		except Exception as e:
			raise e

	@property
	def cachelargestresponsereceived(self) :
		ur"""Size, in bytes, of largest response sent to client from the cache or the origin server.
		"""
		try :
			return self._cachelargestresponsereceived
		except Exception as e:
			raise e

	@property
	def cachenonparameterizedinvalidationrequestsrate(self) :
		ur"""Rate (/s) counter for cachetotnonparameterizedinvalidationrequests.
		"""
		try :
			return self._cachenonparameterizedinvalidationrequestsrate
		except Exception as e:
			raise e

	@property
	def cacherecentpercentbytehit(self) :
		ur"""Recently recorded cache byte hit ratio expressed as percentage. Here we define byte hit ratio as ((number of bytes served from the cache)/(total number of bytes served to the client)). This is the standard definition of Byte Hit Ratio. If compression is turned ON in NS then this ratio doesn't mean much. This might under or over estimate the origin-to-cache bandwidth saving (depending upon whether bytes served by CMP in NetScaler are more or less than compressed bytes served from the cache). If CMP is turned OFF in NS then this ratio is same as cacheRecentPercentOriginBandwidthSaved.
		"""
		try :
			return self._cacherecentpercentbytehit
		except Exception as e:
			raise e

	@property
	def cacherecentpercentsuccessfulrevalidation(self) :
		ur"""Recently recorded percentage of times stored content was successfully revalidated by a 304 response rather than by a full response.
		"""
		try :
			return self._cacherecentpercentsuccessfulrevalidation
		except Exception as e:
			raise e

	@property
	def cachesuccessfulrevalidationrate(self) :
		ur"""Rate (/s) counter for cachetotsuccessfulrevalidation.
		"""
		try :
			return self._cachesuccessfulrevalidationrate
		except Exception as e:
			raise e

	@property
	def cachesqlhitsrate(self) :
		ur"""Rate (/s) counter for cachetotsqlhits.
		"""
		try :
			return self._cachesqlhitsrate
		except Exception as e:
			raise e

	@property
	def cacherequestsrate(self) :
		ur"""Rate (/s) counter for cachetotrequests.
		"""
		try :
			return self._cacherequestsrate
		except Exception as e:
			raise e

	@property
	def cachemissesrate(self) :
		ur"""Rate (/s) counter for cachetotmisses.
		"""
		try :
			return self._cachemissesrate
		except Exception as e:
			raise e

	@property
	def cachemaxmemorykb(self) :
		ur"""Largest amount of memory the NetScaler can dedicate to caching, up to 50% of available memory. A 0 value disables caching, but the caching module continues to run. .
		"""
		try :
			return self._cachemaxmemorykb
		except Exception as e:
			raise e

	@property
	def cachenumcached(self) :
		ur"""Responses currently in integrated cache. Includes responses fully downloaded, in the process of being downloaded, and expired or flushed but not yet removed.
		"""
		try :
			return self._cachenumcached
		except Exception as e:
			raise e

	@property
	def cachetothits(self) :
		ur"""Responses served from the integrated cache. These responses match a policy with a CACHE action.
		"""
		try :
			return self._cachetothits
		except Exception as e:
			raise e

	@property
	def cachetotsuccessfulrevalidation(self) :
		ur"""Total number of times stored content was successfully revalidated by a 304 Not Modified response from the origin.
		"""
		try :
			return self._cachetotsuccessfulrevalidation
		except Exception as e:
			raise e

	@property
	def cachepercentparameterized304hits(self) :
		ur"""Percentage of parameterized 304 hits relative to all parameterized hits.
		"""
		try :
			return self._cachepercentparameterized304hits
		except Exception as e:
			raise e

	@property
	def cacheflashcachehitsrate(self) :
		ur"""Rate (/s) counter for cachetotflashcachehits.
		"""
		try :
			return self._cacheflashcachehitsrate
		except Exception as e:
			raise e

	@property
	def cachestoreablemissesrate(self) :
		ur"""Rate (/s) counter for cachetotstoreablemisses.
		"""
		try :
			return self._cachestoreablemissesrate
		except Exception as e:
			raise e

	@property
	def cachetotflashcachehits(self) :
		ur"""Number of requests to a content group with flash cache enabled that were cache hits. The flash cache setting queues requests that arrive simultaneously and distributes the response to all the clients in the queue.
		"""
		try :
			return self._cachetotflashcachehits
		except Exception as e:
			raise e

	@property
	def cachetotsqlhits(self) :
		ur"""sql response served from cache.
		"""
		try :
			return self._cachetotsqlhits
		except Exception as e:
			raise e

	@property
	def cachetotrevalidationmiss(self) :
		ur"""Responses that an intervening cache revalidated with the integrated cache before serving, as determined by a Cache-Control: Max-Age header configurable in the integrated cache.
		"""
		try :
			return self._cachetotrevalidationmiss
		except Exception as e:
			raise e

	@property
	def cachemaxmemoryactivekb(self) :
		ur"""Currently active value of maximum memory.
		"""
		try :
			return self._cachemaxmemoryactivekb
		except Exception as e:
			raise e

	@property
	def cachetotstoreablemisses(self) :
		ur"""Cache misses for which the fetched response is stored in the cache before serving it to the client. Storable misses conform to a built-in or user-defined caching policy that contains a CACHE action.
		"""
		try :
			return self._cachetotstoreablemisses
		except Exception as e:
			raise e

	@property
	def cacheparameterizedhitsrate(self) :
		ur"""Rate (/s) counter for cachetotparameterizedhits.
		"""
		try :
			return self._cacheparameterizedhitsrate
		except Exception as e:
			raise e

	@property
	def cacheparameterized304hitsrate(self) :
		ur"""Rate (/s) counter for cachetotparameterized304hits.
		"""
		try :
			return self._cacheparameterized304hitsrate
		except Exception as e:
			raise e

	@property
	def cacheexpireatlastbyterate(self) :
		ur"""Rate (/s) counter for cachetotexpireatlastbyte.
		"""
		try :
			return self._cacheexpireatlastbyterate
		except Exception as e:
			raise e

	@property
	def cachecurmisses(self) :
		ur"""Responses fetched from the origin and served from the cache. Should approximate storable misses. Does not include non-storable misses.
		"""
		try :
			return self._cachecurmisses
		except Exception as e:
			raise e

	@property
	def cacherevalidationmissrate(self) :
		ur"""Rate (/s) counter for cachetotrevalidationmiss.
		"""
		try :
			return self._cacherevalidationmissrate
		except Exception as e:
			raise e

	@property
	def cachenon304hitsrate(self) :
		ur"""Rate (/s) counter for cachetotnon304hits.
		"""
		try :
			return self._cachenon304hitsrate
		except Exception as e:
			raise e

	@property
	def cachepercentsuccessfulrevalidation(self) :
		ur"""Percentage of times stored content was successfully revalidated by a 304 (Object Not Modifed) response rather than by a full response.
		"""
		try :
			return self._cachepercentsuccessfulrevalidation
		except Exception as e:
			raise e

	@property
	def cachetotnon304hits(self) :
		ur"""Total number of full (non-304) responses served from the cache. A 304 status code indicates that a response has not been modified since the last time it was served.
		"""
		try :
			return self._cachetotnon304hits
		except Exception as e:
			raise e

	@property
	def cachefulltoconditionalrequestrate(self) :
		ur"""Rate (/s) counter for cachetotfulltoconditionalrequest.
		"""
		try :
			return self._cachefulltoconditionalrequestrate
		except Exception as e:
			raise e

	@property
	def cacherecentpercentoriginbandwidthsaved(self) :
		ur"""Bytes served from cache divided by total bytes served to client. This ratio can be greater than 1 because of the assumption that all compression has been done in the NetScaler.
		"""
		try :
			return self._cacherecentpercentoriginbandwidthsaved
		except Exception as e:
			raise e

	@property
	def cacherecentpercentparameterizedhits(self) :
		ur"""Recently recorded ratio of parameterized 304 hits to all parameterized hits expressed as a percentage.
		"""
		try :
			return self._cacherecentpercentparameterizedhits
		except Exception as e:
			raise e

	@property
	def cachetotparameterizedinvalidationrequests(self) :
		ur"""Requests matching a policy with an invalidation (INVAL) action and a content group that uses an invalidation selector or parameters.
		"""
		try :
			return self._cachetotparameterizedinvalidationrequests
		except Exception as e:
			raise e

	@property
	def cachetotflashcachemisses(self) :
		ur"""Number of requests to a content group with flash cache enabled that were cache misses. Flash cache distributes the response to all the clients in aqueue.
		"""
		try :
			return self._cachetotflashcachemisses
		except Exception as e:
			raise e

	@property
	def cacheparameterizedrequestsrate(self) :
		ur"""Rate (/s) counter for cachetotparameterizedrequests.
		"""
		try :
			return self._cacheparameterizedrequestsrate
		except Exception as e:
			raise e

	@property
	def cacheerrmemalloc(self) :
		ur"""Total number of times the cache failed to allocate memory to store responses.
		"""
		try :
			return self._cacheerrmemalloc
		except Exception as e:
			raise e

	@property
	def cacherecentpercenthit(self) :
		ur"""Recently recorded cache hit ratio expressed as percentage.
		"""
		try :
			return self._cacherecentpercenthit
		except Exception as e:
			raise e

	@property
	def cachecompressedbytesservedrate(self) :
		ur"""Rate (/s) counter for cachecompressedbytesserved.
		"""
		try :
			return self._cachecompressedbytesservedrate
		except Exception as e:
			raise e

	@property
	def cache304hitsrate(self) :
		ur"""Rate (/s) counter for cachetot304hits.
		"""
		try :
			return self._cache304hitsrate
		except Exception as e:
			raise e

	@property
	def cachepercenthit(self) :
		ur"""Cache hits as percentage of the total number of requests.
		"""
		try :
			return self._cachepercenthit
		except Exception as e:
			raise e

	@property
	def cachenonstoreablemissesrate(self) :
		ur"""Rate (/s) counter for cachetotnonstoreablemisses.
		"""
		try :
			return self._cachenonstoreablemissesrate
		except Exception as e:
			raise e

	@property
	def cachetotinvalidationrequests(self) :
		ur"""Requests that match an invalidation policy and result in expiration of specific cached responses or entire content groups.
		"""
		try :
			return self._cachetotinvalidationrequests
		except Exception as e:
			raise e

	@property
	def cache64maxmemorykb(self) :
		ur"""Largest amount of memory the NetScaler can dedicate to caching, up to 50% of available memory. A 0 value disables caching, but the caching module continues to run. .
		"""
		try :
			return self._cache64maxmemorykb
		except Exception as e:
			raise e

	@property
	def cachetot304hits(self) :
		ur"""Object not modified responses served from the cache. (Status code 304 served instead of the full response.).
		"""
		try :
			return self._cachetot304hits
		except Exception as e:
			raise e

	@property
	def cachetotfulltoconditionalrequest(self) :
		ur"""Number of user-agent requests for a cached  Poll Every Time (PET) response that were sent to the origin server as conditional requests. .
		"""
		try :
			return self._cachetotfulltoconditionalrequest
		except Exception as e:
			raise e

	@property
	def cachetotparameterizedhits(self) :
		ur"""Parameterized requests resulting in either a 304 or non-304 hit.
		"""
		try :
			return self._cachetotparameterizedhits
		except Exception as e:
			raise e

	@property
	def cachepetrequestsrate(self) :
		ur"""Rate (/s) counter for cachetotpetrequests.
		"""
		try :
			return self._cachepetrequestsrate
		except Exception as e:
			raise e

	@property
	def cacherecentpercent304hits(self) :
		ur"""Recently recorded ratio of 304 hits to all hits expressed as percentage.
		"""
		try :
			return self._cacherecentpercent304hits
		except Exception as e:
			raise e

	@property
	def cachetotnonstoreablemisses(self) :
		ur"""Cache misses for which the fetched response is not stored in the cache. These responses match policies with a NOCACHE action or are affected by Poll Every Time.
		"""
		try :
			return self._cachetotnonstoreablemisses
		except Exception as e:
			raise e

	@property
	def cachetotparameterizedrequests(self) :
		ur"""Total number of requests where the content group has hit and invalidation parameters or selectors.
		"""
		try :
			return self._cachetotparameterizedrequests
		except Exception as e:
			raise e

	@property
	def cachepercentoriginbandwidthsaved(self) :
		ur"""Percentage of origin bandwidth saved, expressed as number of bytes served from the integrated cache divided by all bytes served. The assumption is that all compression is done in the NetScaler.
		"""
		try :
			return self._cachepercentoriginbandwidthsaved
		except Exception as e:
			raise e

	@property
	def cachetotrequests(self) :
		ur"""Total cache hits plus total cache misses.
		"""
		try :
			return self._cachetotrequests
		except Exception as e:
			raise e

	@property
	def cacheparameterizednon304hitsrate(self) :
		ur"""Rate (/s) counter for cachetotparameterizednon304hits.
		"""
		try :
			return self._cacheparameterizednon304hitsrate
		except Exception as e:
			raise e

	@property
	def cachetotmisses(self) :
		ur"""Intercepted HTTP requests requiring fetches from origin server.
		"""
		try :
			return self._cachetotmisses
		except Exception as e:
			raise e

	@property
	def cachetotpethits(self) :
		ur"""Number of times a cache hit was found during a search of a content group that has Poll Every Time enabled.
		"""
		try :
			return self._cachetotpethits
		except Exception as e:
			raise e

	@property
	def cacheparameterizedinvalidationrequestsrate(self) :
		ur"""Rate (/s) counter for cachetotparameterizedinvalidationrequests.
		"""
		try :
			return self._cacheparameterizedinvalidationrequestsrate
		except Exception as e:
			raise e

	@property
	def cacherecentpercentstoreablemiss(self) :
		ur"""Recently recorded ratio of store-able misses to all misses expressed as percentage.
		"""
		try :
			return self._cacherecentpercentstoreablemiss
		except Exception as e:
			raise e

	@property
	def cacheflashcachemissesrate(self) :
		ur"""Rate (/s) counter for cachetotflashcachemisses.
		"""
		try :
			return self._cacheflashcachemissesrate
		except Exception as e:
			raise e

	@property
	def cacheinvalidationrequestsrate(self) :
		ur"""Rate (/s) counter for cachetotinvalidationrequests.
		"""
		try :
			return self._cacheinvalidationrequestsrate
		except Exception as e:
			raise e

	@property
	def cachetotparameterized304hits(self) :
		ur"""Parameterized requests resulting in an object not modified (status code 304) response. .
		"""
		try :
			return self._cachetotparameterized304hits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cache_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cache
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
		ur""" Use this API to fetch the statistics of all cache_stats resources that are configured on netscaler.
		"""
		try :
			obj = cache_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class cache_response(base_response) :
	def __init__(self, length=1) :
		self.cache = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cache = [cache_stats() for _ in range(length)]

