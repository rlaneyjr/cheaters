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

class cachecontentgroup(base_resource) :
	""" Configuration for Integrated Cache content group resource. """
	def __init__(self) :
		self._name = ""
		self._weakposrelexpiry = 0
		self._heurexpiryparam = 0
		self._relexpiry = 0
		self._relexpirymillisec = 0
		self._absexpiry = []
		self._absexpirygmt = []
		self._weaknegrelexpiry = 0
		self._hitparams = []
		self._invalparams = []
		self._ignoreparamvaluecase = ""
		self._matchcookies = ""
		self._invalrestrictedtohost = ""
		self._polleverytime = ""
		self._ignorereloadreq = ""
		self._removecookies = ""
		self._prefetch = ""
		self._prefetchperiod = 0
		self._prefetchperiodmillisec = 0
		self._prefetchmaxpending = 0
		self._flashcache = ""
		self._expireatlastbyte = ""
		self._insertvia = ""
		self._insertage = ""
		self._insertetag = ""
		self._cachecontrol = ""
		self._quickabortsize = 0
		self._minressize = 0
		self._maxressize = 0
		self._memlimit = 0
		self._ignorereqcachinghdrs = ""
		self._minhits = 0
		self._alwaysevalpolicies = ""
		self._persistha = ""
		self._pinned = ""
		self._lazydnsresolve = ""
		self._hitselector = ""
		self._invalselector = ""
		self._type = ""
		self._query = ""
		self._host = ""
		self._selectorvalue = ""
		self._tosecondary = ""
		self._flags = 0
		self._prefetchcur = 0
		self._memusage = 0
		self._memdusage = 0
		self._disklimit = 0
		self._cachenon304hits = 0
		self._cache304hits = 0
		self._cachecells = 0
		self._cachegroupincarnation = 0
		self._persist = ""
		self._policyname = []
		self._cachenuminvalpolicy = 0
		self._markercells = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the content group.  Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the content group is created.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the content group.  Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the content group is created.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def weakposrelexpiry(self) :
		ur"""Relative expiry time, in seconds, for expiring positive responses with response codes between 200 and 399. Cannot be used in combination with other Expiry attributes. Similar to -relExpiry but has lower precedence.<br/>Maximum length =  31536000.
		"""
		try :
			return self._weakposrelexpiry
		except Exception as e:
			raise e

	@weakposrelexpiry.setter
	def weakposrelexpiry(self, weakposrelexpiry) :
		ur"""Relative expiry time, in seconds, for expiring positive responses with response codes between 200 and 399. Cannot be used in combination with other Expiry attributes. Similar to -relExpiry but has lower precedence.<br/>Maximum length =  31536000
		"""
		try :
			self._weakposrelexpiry = weakposrelexpiry
		except Exception as e:
			raise e

	@property
	def heurexpiryparam(self) :
		ur"""Heuristic expiry time, in percent of the duration, since the object was last modified.<br/>Maximum length =  100.
		"""
		try :
			return self._heurexpiryparam
		except Exception as e:
			raise e

	@heurexpiryparam.setter
	def heurexpiryparam(self, heurexpiryparam) :
		ur"""Heuristic expiry time, in percent of the duration, since the object was last modified.<br/>Maximum length =  100
		"""
		try :
			self._heurexpiryparam = heurexpiryparam
		except Exception as e:
			raise e

	@property
	def relexpiry(self) :
		ur"""Relative expiry time, in seconds, after which to expire an object cached in this content group.<br/>Maximum length =  31536000.
		"""
		try :
			return self._relexpiry
		except Exception as e:
			raise e

	@relexpiry.setter
	def relexpiry(self, relexpiry) :
		ur"""Relative expiry time, in seconds, after which to expire an object cached in this content group.<br/>Maximum length =  31536000
		"""
		try :
			self._relexpiry = relexpiry
		except Exception as e:
			raise e

	@property
	def relexpirymillisec(self) :
		ur"""Relative expiry time, in milliseconds, after which to expire an object cached in this content group.<br/>Maximum length =  86400000.
		"""
		try :
			return self._relexpirymillisec
		except Exception as e:
			raise e

	@relexpirymillisec.setter
	def relexpirymillisec(self, relexpirymillisec) :
		ur"""Relative expiry time, in milliseconds, after which to expire an object cached in this content group.<br/>Maximum length =  86400000
		"""
		try :
			self._relexpirymillisec = relexpirymillisec
		except Exception as e:
			raise e

	@property
	def absexpiry(self) :
		ur"""Local time, up to 4 times a day, at which all objects in the content group must expire. 
		CLI Users:
		For example, to specify that the objects in the content group should expire by 11:00 PM, type the following command: add cache contentgroup <contentgroup name> -absexpiry 23:00 
		To specify that the objects in the content group should expire at 10:00 AM, 3 PM, 6 PM, and 11:00 PM, type: add cache contentgroup <contentgroup name> -absexpiry 10:00 15:00 18:00 23:00.
		"""
		try :
			return self._absexpiry
		except Exception as e:
			raise e

	@absexpiry.setter
	def absexpiry(self, absexpiry) :
		ur"""Local time, up to 4 times a day, at which all objects in the content group must expire. 
		CLI Users:
		For example, to specify that the objects in the content group should expire by 11:00 PM, type the following command: add cache contentgroup <contentgroup name> -absexpiry 23:00 
		To specify that the objects in the content group should expire at 10:00 AM, 3 PM, 6 PM, and 11:00 PM, type: add cache contentgroup <contentgroup name> -absexpiry 10:00 15:00 18:00 23:00.
		"""
		try :
			self._absexpiry = absexpiry
		except Exception as e:
			raise e

	@property
	def absexpirygmt(self) :
		ur"""Coordinated Universal Time (GMT), up to 4 times a day, when all objects in the content group must expire.
		"""
		try :
			return self._absexpirygmt
		except Exception as e:
			raise e

	@absexpirygmt.setter
	def absexpirygmt(self, absexpirygmt) :
		ur"""Coordinated Universal Time (GMT), up to 4 times a day, when all objects in the content group must expire.
		"""
		try :
			self._absexpirygmt = absexpirygmt
		except Exception as e:
			raise e

	@property
	def weaknegrelexpiry(self) :
		ur"""Relative expiry time, in seconds, for expiring negative responses. This value is used only if the expiry time cannot be determined from any other source. It is applicable only to the following status codes: 307, 403, 404, and 410.<br/>Maximum length =  31536000.
		"""
		try :
			return self._weaknegrelexpiry
		except Exception as e:
			raise e

	@weaknegrelexpiry.setter
	def weaknegrelexpiry(self, weaknegrelexpiry) :
		ur"""Relative expiry time, in seconds, for expiring negative responses. This value is used only if the expiry time cannot be determined from any other source. It is applicable only to the following status codes: 307, 403, 404, and 410.<br/>Maximum length =  31536000
		"""
		try :
			self._weaknegrelexpiry = weaknegrelexpiry
		except Exception as e:
			raise e

	@property
	def hitparams(self) :
		ur"""Parameters to use for parameterized hit evaluation of an object. Up to 128 parameters can be specified. Mutually exclusive with the Hit Selector parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._hitparams
		except Exception as e:
			raise e

	@hitparams.setter
	def hitparams(self, hitparams) :
		ur"""Parameters to use for parameterized hit evaluation of an object. Up to 128 parameters can be specified. Mutually exclusive with the Hit Selector parameter.<br/>Minimum length =  1
		"""
		try :
			self._hitparams = hitparams
		except Exception as e:
			raise e

	@property
	def invalparams(self) :
		ur"""Parameters for parameterized invalidation of an object. You can specify up to 8 parameters. Mutually exclusive with invalSelector.<br/>Minimum length =  1.
		"""
		try :
			return self._invalparams
		except Exception as e:
			raise e

	@invalparams.setter
	def invalparams(self, invalparams) :
		ur"""Parameters for parameterized invalidation of an object. You can specify up to 8 parameters. Mutually exclusive with invalSelector.<br/>Minimum length =  1
		"""
		try :
			self._invalparams = invalparams
		except Exception as e:
			raise e

	@property
	def ignoreparamvaluecase(self) :
		ur"""Ignore case when comparing parameter values during parameterized hit evaluation. (Parameter value case is ignored by default during parameterized invalidation.).<br/>Possible values = YES, NO.
		"""
		try :
			return self._ignoreparamvaluecase
		except Exception as e:
			raise e

	@ignoreparamvaluecase.setter
	def ignoreparamvaluecase(self, ignoreparamvaluecase) :
		ur"""Ignore case when comparing parameter values during parameterized hit evaluation. (Parameter value case is ignored by default during parameterized invalidation.).<br/>Possible values = YES, NO
		"""
		try :
			self._ignoreparamvaluecase = ignoreparamvaluecase
		except Exception as e:
			raise e

	@property
	def matchcookies(self) :
		ur"""Evaluate for parameters in the cookie header also.<br/>Possible values = YES, NO.
		"""
		try :
			return self._matchcookies
		except Exception as e:
			raise e

	@matchcookies.setter
	def matchcookies(self, matchcookies) :
		ur"""Evaluate for parameters in the cookie header also.<br/>Possible values = YES, NO
		"""
		try :
			self._matchcookies = matchcookies
		except Exception as e:
			raise e

	@property
	def invalrestrictedtohost(self) :
		ur"""Take the host header into account during parameterized invalidation.<br/>Possible values = YES, NO.
		"""
		try :
			return self._invalrestrictedtohost
		except Exception as e:
			raise e

	@invalrestrictedtohost.setter
	def invalrestrictedtohost(self, invalrestrictedtohost) :
		ur"""Take the host header into account during parameterized invalidation.<br/>Possible values = YES, NO
		"""
		try :
			self._invalrestrictedtohost = invalrestrictedtohost
		except Exception as e:
			raise e

	@property
	def polleverytime(self) :
		ur"""Always poll for the objects in this content group. That is, retrieve the objects from the origin server whenever they are requested.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._polleverytime
		except Exception as e:
			raise e

	@polleverytime.setter
	def polleverytime(self, polleverytime) :
		ur"""Always poll for the objects in this content group. That is, retrieve the objects from the origin server whenever they are requested.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._polleverytime = polleverytime
		except Exception as e:
			raise e

	@property
	def ignorereloadreq(self) :
		ur"""Ignore any request to reload a cached object from the origin server.
		To guard against Denial of Service attacks, set this parameter to YES. For RFC-compliant behavior, set it to NO.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._ignorereloadreq
		except Exception as e:
			raise e

	@ignorereloadreq.setter
	def ignorereloadreq(self, ignorereloadreq) :
		ur"""Ignore any request to reload a cached object from the origin server.
		To guard against Denial of Service attacks, set this parameter to YES. For RFC-compliant behavior, set it to NO.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._ignorereloadreq = ignorereloadreq
		except Exception as e:
			raise e

	@property
	def removecookies(self) :
		ur"""Remove cookies from responses.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._removecookies
		except Exception as e:
			raise e

	@removecookies.setter
	def removecookies(self, removecookies) :
		ur"""Remove cookies from responses.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._removecookies = removecookies
		except Exception as e:
			raise e

	@property
	def prefetch(self) :
		ur"""Attempt to refresh objects that are about to go stale.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._prefetch
		except Exception as e:
			raise e

	@prefetch.setter
	def prefetch(self, prefetch) :
		ur"""Attempt to refresh objects that are about to go stale.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._prefetch = prefetch
		except Exception as e:
			raise e

	@property
	def prefetchperiod(self) :
		ur"""Time period, in seconds before an object's calculated expiry time, during which to attempt prefetch.<br/>Maximum length =  4294967294.
		"""
		try :
			return self._prefetchperiod
		except Exception as e:
			raise e

	@prefetchperiod.setter
	def prefetchperiod(self, prefetchperiod) :
		ur"""Time period, in seconds before an object's calculated expiry time, during which to attempt prefetch.<br/>Maximum length =  4294967294
		"""
		try :
			self._prefetchperiod = prefetchperiod
		except Exception as e:
			raise e

	@property
	def prefetchperiodmillisec(self) :
		ur"""Time period, in milliseconds before an object's calculated expiry time, during which to attempt prefetch.<br/>Maximum length =  4294967290.
		"""
		try :
			return self._prefetchperiodmillisec
		except Exception as e:
			raise e

	@prefetchperiodmillisec.setter
	def prefetchperiodmillisec(self, prefetchperiodmillisec) :
		ur"""Time period, in milliseconds before an object's calculated expiry time, during which to attempt prefetch.<br/>Maximum length =  4294967290
		"""
		try :
			self._prefetchperiodmillisec = prefetchperiodmillisec
		except Exception as e:
			raise e

	@property
	def prefetchmaxpending(self) :
		ur"""Maximum number of outstanding prefetches that can be queued for the content group.<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._prefetchmaxpending
		except Exception as e:
			raise e

	@prefetchmaxpending.setter
	def prefetchmaxpending(self, prefetchmaxpending) :
		ur"""Maximum number of outstanding prefetches that can be queued for the content group.<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._prefetchmaxpending = prefetchmaxpending
		except Exception as e:
			raise e

	@property
	def flashcache(self) :
		ur"""Perform flash cache. Mutually exclusive with Poll Every Time (PET) on the same content group.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._flashcache
		except Exception as e:
			raise e

	@flashcache.setter
	def flashcache(self, flashcache) :
		ur"""Perform flash cache. Mutually exclusive with Poll Every Time (PET) on the same content group.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._flashcache = flashcache
		except Exception as e:
			raise e

	@property
	def expireatlastbyte(self) :
		ur"""Force expiration of the content immediately after the response is downloaded (upon receipt of the last byte of the response body). Applicable only to positive responses.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._expireatlastbyte
		except Exception as e:
			raise e

	@expireatlastbyte.setter
	def expireatlastbyte(self, expireatlastbyte) :
		ur"""Force expiration of the content immediately after the response is downloaded (upon receipt of the last byte of the response body). Applicable only to positive responses.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._expireatlastbyte = expireatlastbyte
		except Exception as e:
			raise e

	@property
	def insertvia(self) :
		ur"""Insert a Via header into the response.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._insertvia
		except Exception as e:
			raise e

	@insertvia.setter
	def insertvia(self, insertvia) :
		ur"""Insert a Via header into the response.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._insertvia = insertvia
		except Exception as e:
			raise e

	@property
	def insertage(self) :
		ur"""Insert an Age header into the response. An Age header contains information about the age of the object, in seconds, as calculated by the integrated cache.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._insertage
		except Exception as e:
			raise e

	@insertage.setter
	def insertage(self, insertage) :
		ur"""Insert an Age header into the response. An Age header contains information about the age of the object, in seconds, as calculated by the integrated cache.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._insertage = insertage
		except Exception as e:
			raise e

	@property
	def insertetag(self) :
		ur"""Insert an ETag header in the response. With ETag header insertion, the integrated cache does not serve full responses on repeat requests.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._insertetag
		except Exception as e:
			raise e

	@insertetag.setter
	def insertetag(self, insertetag) :
		ur"""Insert an ETag header in the response. With ETag header insertion, the integrated cache does not serve full responses on repeat requests.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._insertetag = insertetag
		except Exception as e:
			raise e

	@property
	def cachecontrol(self) :
		ur"""Insert a Cache-Control header into the response.<br/>Minimum length =  1.
		"""
		try :
			return self._cachecontrol
		except Exception as e:
			raise e

	@cachecontrol.setter
	def cachecontrol(self, cachecontrol) :
		ur"""Insert a Cache-Control header into the response.<br/>Minimum length =  1
		"""
		try :
			self._cachecontrol = cachecontrol
		except Exception as e:
			raise e

	@property
	def quickabortsize(self) :
		ur"""If the size of an object that is being downloaded is less than or equal to the quick abort value, and a client aborts during the download, the cache stops downloading the response. If the object is larger than the quick abort size, the cache continues to download the response.<br/>Default value: 4194303<br/>Maximum length =  4194303.
		"""
		try :
			return self._quickabortsize
		except Exception as e:
			raise e

	@quickabortsize.setter
	def quickabortsize(self, quickabortsize) :
		ur"""If the size of an object that is being downloaded is less than or equal to the quick abort value, and a client aborts during the download, the cache stops downloading the response. If the object is larger than the quick abort size, the cache continues to download the response.<br/>Default value: 4194303<br/>Maximum length =  4194303
		"""
		try :
			self._quickabortsize = quickabortsize
		except Exception as e:
			raise e

	@property
	def minressize(self) :
		ur"""Minimum size of a response that can be cached in this content group.
		Default minimum response size is 0.<br/>Maximum length =  2097151.
		"""
		try :
			return self._minressize
		except Exception as e:
			raise e

	@minressize.setter
	def minressize(self, minressize) :
		ur"""Minimum size of a response that can be cached in this content group.
		Default minimum response size is 0.<br/>Maximum length =  2097151
		"""
		try :
			self._minressize = minressize
		except Exception as e:
			raise e

	@property
	def maxressize(self) :
		ur"""Maximum size of a response that can be cached in this content group.<br/>Default value: 80<br/>Maximum length =  2097151.
		"""
		try :
			return self._maxressize
		except Exception as e:
			raise e

	@maxressize.setter
	def maxressize(self, maxressize) :
		ur"""Maximum size of a response that can be cached in this content group.<br/>Default value: 80<br/>Maximum length =  2097151
		"""
		try :
			self._maxressize = maxressize
		except Exception as e:
			raise e

	@property
	def memlimit(self) :
		ur"""Maximum amount of memory that the cache can use. The effective limit is based on the available memory of the NetScaler appliance.<br/>Default value: 65536.
		"""
		try :
			return self._memlimit
		except Exception as e:
			raise e

	@memlimit.setter
	def memlimit(self, memlimit) :
		ur"""Maximum amount of memory that the cache can use. The effective limit is based on the available memory of the NetScaler appliance.<br/>Default value: 65536
		"""
		try :
			self._memlimit = memlimit
		except Exception as e:
			raise e

	@property
	def ignorereqcachinghdrs(self) :
		ur"""Ignore Cache-Control and Pragma headers in the incoming request.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._ignorereqcachinghdrs
		except Exception as e:
			raise e

	@ignorereqcachinghdrs.setter
	def ignorereqcachinghdrs(self, ignorereqcachinghdrs) :
		ur"""Ignore Cache-Control and Pragma headers in the incoming request.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._ignorereqcachinghdrs = ignorereqcachinghdrs
		except Exception as e:
			raise e

	@property
	def minhits(self) :
		ur"""Number of hits that qualifies a response for storage in this content group.<br/>Default value: 0.
		"""
		try :
			return self._minhits
		except Exception as e:
			raise e

	@minhits.setter
	def minhits(self, minhits) :
		ur"""Number of hits that qualifies a response for storage in this content group.<br/>Default value: 0
		"""
		try :
			self._minhits = minhits
		except Exception as e:
			raise e

	@property
	def alwaysevalpolicies(self) :
		ur"""Force policy evaluation for each response arriving from the origin server. Cannot be set to YES if the Prefetch parameter is also set to YES.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._alwaysevalpolicies
		except Exception as e:
			raise e

	@alwaysevalpolicies.setter
	def alwaysevalpolicies(self, alwaysevalpolicies) :
		ur"""Force policy evaluation for each response arriving from the origin server. Cannot be set to YES if the Prefetch parameter is also set to YES.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._alwaysevalpolicies = alwaysevalpolicies
		except Exception as e:
			raise e

	@property
	def persistha(self) :
		ur"""Setting persistHA to YES causes IC to save objects in contentgroup to Secondary node in HA deployment.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._persistha
		except Exception as e:
			raise e

	@persistha.setter
	def persistha(self, persistha) :
		ur"""Setting persistHA to YES causes IC to save objects in contentgroup to Secondary node in HA deployment.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._persistha = persistha
		except Exception as e:
			raise e

	@property
	def pinned(self) :
		ur"""Do not flush objects from this content group under memory pressure.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._pinned
		except Exception as e:
			raise e

	@pinned.setter
	def pinned(self, pinned) :
		ur"""Do not flush objects from this content group under memory pressure.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._pinned = pinned
		except Exception as e:
			raise e

	@property
	def lazydnsresolve(self) :
		ur"""Perform DNS resolution for responses only if the destination IP address in the request does not match the destination IP address of the cached response.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._lazydnsresolve
		except Exception as e:
			raise e

	@lazydnsresolve.setter
	def lazydnsresolve(self, lazydnsresolve) :
		ur"""Perform DNS resolution for responses only if the destination IP address in the request does not match the destination IP address of the cached response.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._lazydnsresolve = lazydnsresolve
		except Exception as e:
			raise e

	@property
	def hitselector(self) :
		ur"""Selector for evaluating whether an object gets stored in a particular content group. A selector is an abstraction for a collection of PIXL expressions.
		"""
		try :
			return self._hitselector
		except Exception as e:
			raise e

	@hitselector.setter
	def hitselector(self, hitselector) :
		ur"""Selector for evaluating whether an object gets stored in a particular content group. A selector is an abstraction for a collection of PIXL expressions.
		"""
		try :
			self._hitselector = hitselector
		except Exception as e:
			raise e

	@property
	def invalselector(self) :
		ur"""Selector for invalidating objects in the content group. A selector is an abstraction for a collection of PIXL expressions.
		"""
		try :
			return self._invalselector
		except Exception as e:
			raise e

	@invalselector.setter
	def invalselector(self, invalselector) :
		ur"""Selector for invalidating objects in the content group. A selector is an abstraction for a collection of PIXL expressions.
		"""
		try :
			self._invalselector = invalselector
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""The type of the content group.<br/>Default value: HTTP<br/>Possible values = HTTP, MYSQL, MSSQL.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""The type of the content group.<br/>Default value: HTTP<br/>Possible values = HTTP, MYSQL, MSSQL
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def query(self) :
		ur"""Query string specifying individual objects to flush from this group by using parameterized invalidation. If this parameter is not set, all objects are flushed from the group.<br/>Minimum length =  1.
		"""
		try :
			return self._query
		except Exception as e:
			raise e

	@query.setter
	def query(self, query) :
		ur"""Query string specifying individual objects to flush from this group by using parameterized invalidation. If this parameter is not set, all objects are flushed from the group.<br/>Minimum length =  1
		"""
		try :
			self._query = query
		except Exception as e:
			raise e

	@property
	def host(self) :
		ur"""Flush only objects that belong to the specified host. Do not use except with parameterized invalidation. Also, the Invalidation Restricted to Host parameter for the group must be set to YES.<br/>Minimum length =  1.
		"""
		try :
			return self._host
		except Exception as e:
			raise e

	@host.setter
	def host(self, host) :
		ur"""Flush only objects that belong to the specified host. Do not use except with parameterized invalidation. Also, the Invalidation Restricted to Host parameter for the group must be set to YES.<br/>Minimum length =  1
		"""
		try :
			self._host = host
		except Exception as e:
			raise e

	@property
	def selectorvalue(self) :
		ur"""Value of the selector to be used for flushing objects from the content group. Requires that an invalidation selector be configured for the content group.<br/>Minimum length =  1.
		"""
		try :
			return self._selectorvalue
		except Exception as e:
			raise e

	@selectorvalue.setter
	def selectorvalue(self, selectorvalue) :
		ur"""Value of the selector to be used for flushing objects from the content group. Requires that an invalidation selector be configured for the content group.<br/>Minimum length =  1
		"""
		try :
			self._selectorvalue = selectorvalue
		except Exception as e:
			raise e

	@property
	def tosecondary(self) :
		ur"""content group whose objects are to be sent to secondary.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._tosecondary
		except Exception as e:
			raise e

	@tosecondary.setter
	def tosecondary(self, tosecondary) :
		ur"""content group whose objects are to be sent to secondary.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._tosecondary = tosecondary
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""Flags.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def prefetchcur(self) :
		ur"""Current outstanding prefetches.
		"""
		try :
			return self._prefetchcur
		except Exception as e:
			raise e

	@property
	def memusage(self) :
		ur"""Current memory usage.
		"""
		try :
			return self._memusage
		except Exception as e:
			raise e

	@property
	def memdusage(self) :
		ur"""Current disk memory usage.
		"""
		try :
			return self._memdusage
		except Exception as e:
			raise e

	@property
	def disklimit(self) :
		ur"""Maximum amount of disk that the cache can use. The effective limit is based on the available memory of the NetScaler appliance.<br/>Default value: 0.
		"""
		try :
			return self._disklimit
		except Exception as e:
			raise e

	@property
	def cachenon304hits(self) :
		ur"""Cache non 304 hits.
		"""
		try :
			return self._cachenon304hits
		except Exception as e:
			raise e

	@property
	def cache304hits(self) :
		ur"""Cache 304 hits.
		"""
		try :
			return self._cache304hits
		except Exception as e:
			raise e

	@property
	def cachecells(self) :
		ur"""Number of cells.
		"""
		try :
			return self._cachecells
		except Exception as e:
			raise e

	@property
	def cachegroupincarnation(self) :
		ur"""Cache group incarnation.
		"""
		try :
			return self._cachegroupincarnation
		except Exception as e:
			raise e

	@property
	def persist(self) :
		ur"""Setting persist to YES causes IC to save objects in contentgroup to disk.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._persist
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""Active cache policies refering to this group.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def cachenuminvalpolicy(self) :
		ur"""Number of active Invalidation policies refering to this group.
		"""
		try :
			return self._cachenuminvalpolicy
		except Exception as e:
			raise e

	@property
	def markercells(self) :
		ur"""Numbers of marker cells in this group.
		"""
		try :
			return self._markercells
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur""".<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cachecontentgroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cachecontentgroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add cachecontentgroup.
		"""
		try :
			if type(resource) is not list :
				addresource = cachecontentgroup()
				addresource.name = resource.name
				addresource.weakposrelexpiry = resource.weakposrelexpiry
				addresource.heurexpiryparam = resource.heurexpiryparam
				addresource.relexpiry = resource.relexpiry
				addresource.relexpirymillisec = resource.relexpirymillisec
				addresource.absexpiry = resource.absexpiry
				addresource.absexpirygmt = resource.absexpirygmt
				addresource.weaknegrelexpiry = resource.weaknegrelexpiry
				addresource.hitparams = resource.hitparams
				addresource.invalparams = resource.invalparams
				addresource.ignoreparamvaluecase = resource.ignoreparamvaluecase
				addresource.matchcookies = resource.matchcookies
				addresource.invalrestrictedtohost = resource.invalrestrictedtohost
				addresource.polleverytime = resource.polleverytime
				addresource.ignorereloadreq = resource.ignorereloadreq
				addresource.removecookies = resource.removecookies
				addresource.prefetch = resource.prefetch
				addresource.prefetchperiod = resource.prefetchperiod
				addresource.prefetchperiodmillisec = resource.prefetchperiodmillisec
				addresource.prefetchmaxpending = resource.prefetchmaxpending
				addresource.flashcache = resource.flashcache
				addresource.expireatlastbyte = resource.expireatlastbyte
				addresource.insertvia = resource.insertvia
				addresource.insertage = resource.insertage
				addresource.insertetag = resource.insertetag
				addresource.cachecontrol = resource.cachecontrol
				addresource.quickabortsize = resource.quickabortsize
				addresource.minressize = resource.minressize
				addresource.maxressize = resource.maxressize
				addresource.memlimit = resource.memlimit
				addresource.ignorereqcachinghdrs = resource.ignorereqcachinghdrs
				addresource.minhits = resource.minhits
				addresource.alwaysevalpolicies = resource.alwaysevalpolicies
				addresource.persistha = resource.persistha
				addresource.pinned = resource.pinned
				addresource.lazydnsresolve = resource.lazydnsresolve
				addresource.hitselector = resource.hitselector
				addresource.invalselector = resource.invalselector
				addresource.type = resource.type
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cachecontentgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].weakposrelexpiry = resource[i].weakposrelexpiry
						addresources[i].heurexpiryparam = resource[i].heurexpiryparam
						addresources[i].relexpiry = resource[i].relexpiry
						addresources[i].relexpirymillisec = resource[i].relexpirymillisec
						addresources[i].absexpiry = resource[i].absexpiry
						addresources[i].absexpirygmt = resource[i].absexpirygmt
						addresources[i].weaknegrelexpiry = resource[i].weaknegrelexpiry
						addresources[i].hitparams = resource[i].hitparams
						addresources[i].invalparams = resource[i].invalparams
						addresources[i].ignoreparamvaluecase = resource[i].ignoreparamvaluecase
						addresources[i].matchcookies = resource[i].matchcookies
						addresources[i].invalrestrictedtohost = resource[i].invalrestrictedtohost
						addresources[i].polleverytime = resource[i].polleverytime
						addresources[i].ignorereloadreq = resource[i].ignorereloadreq
						addresources[i].removecookies = resource[i].removecookies
						addresources[i].prefetch = resource[i].prefetch
						addresources[i].prefetchperiod = resource[i].prefetchperiod
						addresources[i].prefetchperiodmillisec = resource[i].prefetchperiodmillisec
						addresources[i].prefetchmaxpending = resource[i].prefetchmaxpending
						addresources[i].flashcache = resource[i].flashcache
						addresources[i].expireatlastbyte = resource[i].expireatlastbyte
						addresources[i].insertvia = resource[i].insertvia
						addresources[i].insertage = resource[i].insertage
						addresources[i].insertetag = resource[i].insertetag
						addresources[i].cachecontrol = resource[i].cachecontrol
						addresources[i].quickabortsize = resource[i].quickabortsize
						addresources[i].minressize = resource[i].minressize
						addresources[i].maxressize = resource[i].maxressize
						addresources[i].memlimit = resource[i].memlimit
						addresources[i].ignorereqcachinghdrs = resource[i].ignorereqcachinghdrs
						addresources[i].minhits = resource[i].minhits
						addresources[i].alwaysevalpolicies = resource[i].alwaysevalpolicies
						addresources[i].persistha = resource[i].persistha
						addresources[i].pinned = resource[i].pinned
						addresources[i].lazydnsresolve = resource[i].lazydnsresolve
						addresources[i].hitselector = resource[i].hitselector
						addresources[i].invalselector = resource[i].invalselector
						addresources[i].type = resource[i].type
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete cachecontentgroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cachecontentgroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cachecontentgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cachecontentgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update cachecontentgroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = cachecontentgroup()
				updateresource.name = resource.name
				updateresource.weakposrelexpiry = resource.weakposrelexpiry
				updateresource.heurexpiryparam = resource.heurexpiryparam
				updateresource.relexpiry = resource.relexpiry
				updateresource.relexpirymillisec = resource.relexpirymillisec
				updateresource.absexpiry = resource.absexpiry
				updateresource.absexpirygmt = resource.absexpirygmt
				updateresource.weaknegrelexpiry = resource.weaknegrelexpiry
				updateresource.hitparams = resource.hitparams
				updateresource.invalparams = resource.invalparams
				updateresource.ignoreparamvaluecase = resource.ignoreparamvaluecase
				updateresource.matchcookies = resource.matchcookies
				updateresource.invalrestrictedtohost = resource.invalrestrictedtohost
				updateresource.polleverytime = resource.polleverytime
				updateresource.ignorereloadreq = resource.ignorereloadreq
				updateresource.removecookies = resource.removecookies
				updateresource.prefetch = resource.prefetch
				updateresource.prefetchperiod = resource.prefetchperiod
				updateresource.prefetchperiodmillisec = resource.prefetchperiodmillisec
				updateresource.prefetchmaxpending = resource.prefetchmaxpending
				updateresource.flashcache = resource.flashcache
				updateresource.expireatlastbyte = resource.expireatlastbyte
				updateresource.insertvia = resource.insertvia
				updateresource.insertage = resource.insertage
				updateresource.insertetag = resource.insertetag
				updateresource.cachecontrol = resource.cachecontrol
				updateresource.quickabortsize = resource.quickabortsize
				updateresource.minressize = resource.minressize
				updateresource.maxressize = resource.maxressize
				updateresource.memlimit = resource.memlimit
				updateresource.ignorereqcachinghdrs = resource.ignorereqcachinghdrs
				updateresource.minhits = resource.minhits
				updateresource.alwaysevalpolicies = resource.alwaysevalpolicies
				updateresource.persistha = resource.persistha
				updateresource.pinned = resource.pinned
				updateresource.lazydnsresolve = resource.lazydnsresolve
				updateresource.hitselector = resource.hitselector
				updateresource.invalselector = resource.invalselector
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ cachecontentgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].weakposrelexpiry = resource[i].weakposrelexpiry
						updateresources[i].heurexpiryparam = resource[i].heurexpiryparam
						updateresources[i].relexpiry = resource[i].relexpiry
						updateresources[i].relexpirymillisec = resource[i].relexpirymillisec
						updateresources[i].absexpiry = resource[i].absexpiry
						updateresources[i].absexpirygmt = resource[i].absexpirygmt
						updateresources[i].weaknegrelexpiry = resource[i].weaknegrelexpiry
						updateresources[i].hitparams = resource[i].hitparams
						updateresources[i].invalparams = resource[i].invalparams
						updateresources[i].ignoreparamvaluecase = resource[i].ignoreparamvaluecase
						updateresources[i].matchcookies = resource[i].matchcookies
						updateresources[i].invalrestrictedtohost = resource[i].invalrestrictedtohost
						updateresources[i].polleverytime = resource[i].polleverytime
						updateresources[i].ignorereloadreq = resource[i].ignorereloadreq
						updateresources[i].removecookies = resource[i].removecookies
						updateresources[i].prefetch = resource[i].prefetch
						updateresources[i].prefetchperiod = resource[i].prefetchperiod
						updateresources[i].prefetchperiodmillisec = resource[i].prefetchperiodmillisec
						updateresources[i].prefetchmaxpending = resource[i].prefetchmaxpending
						updateresources[i].flashcache = resource[i].flashcache
						updateresources[i].expireatlastbyte = resource[i].expireatlastbyte
						updateresources[i].insertvia = resource[i].insertvia
						updateresources[i].insertage = resource[i].insertage
						updateresources[i].insertetag = resource[i].insertetag
						updateresources[i].cachecontrol = resource[i].cachecontrol
						updateresources[i].quickabortsize = resource[i].quickabortsize
						updateresources[i].minressize = resource[i].minressize
						updateresources[i].maxressize = resource[i].maxressize
						updateresources[i].memlimit = resource[i].memlimit
						updateresources[i].ignorereqcachinghdrs = resource[i].ignorereqcachinghdrs
						updateresources[i].minhits = resource[i].minhits
						updateresources[i].alwaysevalpolicies = resource[i].alwaysevalpolicies
						updateresources[i].persistha = resource[i].persistha
						updateresources[i].pinned = resource[i].pinned
						updateresources[i].lazydnsresolve = resource[i].lazydnsresolve
						updateresources[i].hitselector = resource[i].hitselector
						updateresources[i].invalselector = resource[i].invalselector
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of cachecontentgroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cachecontentgroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ cachecontentgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ cachecontentgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def expire(cls, client, resource) :
		ur""" Use this API to expire cachecontentgroup.
		"""
		try :
			if type(resource) is not list :
				expireresource = cachecontentgroup()
				expireresource.name = resource.name
				return expireresource.perform_operation(client,"expire")
			else :
				if (resource and len(resource) > 0) :
					expireresources = [ cachecontentgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						expireresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, expireresources,"expire")
			return result
		except Exception as e :
			raise e

	@classmethod
	def flush(cls, client, resource) :
		ur""" Use this API to flush cachecontentgroup.
		"""
		try :
			if type(resource) is not list :
				flushresource = cachecontentgroup()
				flushresource.name = resource.name
				flushresource.query = resource.query
				flushresource.host = resource.host
				flushresource.selectorvalue = resource.selectorvalue
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ cachecontentgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						flushresources[i].name = resource[i].name
						flushresources[i].query = resource[i].query
						flushresources[i].host = resource[i].host
						flushresources[i].selectorvalue = resource[i].selectorvalue
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def save(cls, client, resource) :
		ur""" Use this API to save cachecontentgroup.
		"""
		try :
			if type(resource) is not list :
				saveresource = cachecontentgroup()
				saveresource.name = resource.name
				saveresource.tosecondary = resource.tosecondary
				return saveresource.perform_operation(client,"save")
			else :
				if (resource and len(resource) > 0) :
					saveresources = [ cachecontentgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						saveresources[i].name = resource[i].name
						saveresources[i].tosecondary = resource[i].tosecondary
				result = cls.perform_operation_bulk_request(client, saveresources,"save")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cachecontentgroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cachecontentgroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = cachecontentgroup()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [cachecontentgroup() for _ in range(len(name))]
							obj = [cachecontentgroup() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = cachecontentgroup()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of cachecontentgroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cachecontentgroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the cachecontentgroup resources configured on NetScaler.
		"""
		try :
			obj = cachecontentgroup()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of cachecontentgroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cachecontentgroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Tosecondary:
		YES = "YES"
		NO = "NO"

	class Persistha:
		YES = "YES"
		NO = "NO"

	class Alwaysevalpolicies:
		YES = "YES"
		NO = "NO"

	class Persist:
		YES = "YES"
		NO = "NO"

	class Pinned:
		YES = "YES"
		NO = "NO"

	class Ignoreparamvaluecase:
		YES = "YES"
		NO = "NO"

	class Expireatlastbyte:
		YES = "YES"
		NO = "NO"

	class Removecookies:
		YES = "YES"
		NO = "NO"

	class Ignorereloadreq:
		YES = "YES"
		NO = "NO"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

	class Flashcache:
		YES = "YES"
		NO = "NO"

	class Invalrestrictedtohost:
		YES = "YES"
		NO = "NO"

	class Type:
		HTTP = "HTTP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"

	class Polleverytime:
		YES = "YES"
		NO = "NO"

	class Ignorereqcachinghdrs:
		YES = "YES"
		NO = "NO"

	class Insertvia:
		YES = "YES"
		NO = "NO"

	class Matchcookies:
		YES = "YES"
		NO = "NO"

	class Insertetag:
		YES = "YES"
		NO = "NO"

	class Lazydnsresolve:
		YES = "YES"
		NO = "NO"

	class Insertage:
		YES = "YES"
		NO = "NO"

	class Prefetch:
		YES = "YES"
		NO = "NO"

class cachecontentgroup_response(base_response) :
	def __init__(self, length=1) :
		self.cachecontentgroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cachecontentgroup = [cachecontentgroup() for _ in range(length)]

