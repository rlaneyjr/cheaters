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

class feo_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._optcacheobjects = 0
		self._optcacheobjectsrate = 0
		self._origcacheobjects = 0
		self._origcacheobjectsrate = 0
		self._totalimgsdomainsharded = 0
		self._imgsdomainshardedrate = 0
		self._totalimgslazyloaded = 0
		self._imgslazyloadedrate = 0
		self._toturireplaced = 0
		self._urireplacedrate = 0
		self._totalimgsinlinedincss = 0
		self._imgsinlinedincssrate = 0
		self._totalinlinedjs = 0
		self._inlinedjsrate = 0
		self._totalinlinedcss = 0
		self._inlinedcssrate = 0
		self._totalinlinedimgs = 0
		self._inlinedimgsrate = 0
		self._totaldatasavings = 0
		self._datasavingsrate = 0
		self._htmlcommentsremoved = 0
		self._htmlcommentsremovedrate = 0
		self._totalcacheextended = 0
		self._cacheextendedrate = 0
		self._totalcsscombined = 0
		self._csscombinedrate = 0
		self._totalimporttolink = 0
		self._importtolinkrate = 0
		self._totaljsmoved = 0
		self._jsmovedrate = 0
		self._totalcssmoved = 0
		self._cssmovedrate = 0
		self._totaljsmin = 0
		self._jsminrate = 0
		self._totalcssmin = 0
		self._cssminrate = 0
		self._totaljpegsoptimized = 0
		self._jpegsoptimizedrate = 0
		self._totalgifstopng = 0
		self._gifstopngrate = 0
		self._totalimgsresized = 0
		self._imgsresizedrate = 0

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
	def totaljsmoved(self) :
		ur"""The total number of JS moved to end.
		"""
		try :
			return self._totaljsmoved
		except Exception as e:
			raise e

	@property
	def totalimgslazyloaded(self) :
		ur"""Total number of images modified for lazy loading.
		"""
		try :
			return self._totalimgslazyloaded
		except Exception as e:
			raise e

	@property
	def htmlcommentsremovedrate(self) :
		ur"""Rate (/s) counter for htmlcommentsremoved.
		"""
		try :
			return self._htmlcommentsremovedrate
		except Exception as e:
			raise e

	@property
	def urireplacedrate(self) :
		ur"""Rate (/s) counter for toturireplaced.
		"""
		try :
			return self._urireplacedrate
		except Exception as e:
			raise e

	@property
	def cssmovedrate(self) :
		ur"""Rate (/s) counter for totalcssmoved.
		"""
		try :
			return self._cssmovedrate
		except Exception as e:
			raise e

	@property
	def htmlcommentsremoved(self) :
		ur"""The total number of HTML comments removed.
		"""
		try :
			return self._htmlcommentsremoved
		except Exception as e:
			raise e

	@property
	def jsmovedrate(self) :
		ur"""Rate (/s) counter for totaljsmoved.
		"""
		try :
			return self._jsmovedrate
		except Exception as e:
			raise e

	@property
	def totalimgsinlinedincss(self) :
		ur"""Total number of images inlined in CSS.
		"""
		try :
			return self._totalimgsinlinedincss
		except Exception as e:
			raise e

	@property
	def totalinlinedcss(self) :
		ur"""Total number of inlined CSS files.
		"""
		try :
			return self._totalinlinedcss
		except Exception as e:
			raise e

	@property
	def inlinedimgsrate(self) :
		ur"""Rate (/s) counter for totalinlinedimgs.
		"""
		try :
			return self._inlinedimgsrate
		except Exception as e:
			raise e

	@property
	def toturireplaced(self) :
		ur"""Total number of URI replaced.
		"""
		try :
			return self._toturireplaced
		except Exception as e:
			raise e

	@property
	def totalinlinedjs(self) :
		ur"""Total number of inlined JS files.
		"""
		try :
			return self._totalinlinedjs
		except Exception as e:
			raise e

	@property
	def totalcssmoved(self) :
		ur"""The total number of CSS moved to head.
		"""
		try :
			return self._totalcssmoved
		except Exception as e:
			raise e

	@property
	def csscombinedrate(self) :
		ur"""Rate (/s) counter for totalcsscombined.
		"""
		try :
			return self._csscombinedrate
		except Exception as e:
			raise e

	@property
	def imgslazyloadedrate(self) :
		ur"""Rate (/s) counter for totalimgslazyloaded.
		"""
		try :
			return self._imgslazyloadedrate
		except Exception as e:
			raise e

	@property
	def totaljsmin(self) :
		ur"""The total number of JS files minified.
		"""
		try :
			return self._totaljsmin
		except Exception as e:
			raise e

	@property
	def optcacheobjects(self) :
		ur"""Total number of optimized cache objects ready to be served.
		"""
		try :
			return self._optcacheobjects
		except Exception as e:
			raise e

	@property
	def totalgifstopng(self) :
		ur"""The total number of images converted from GIF to PNG format.
		"""
		try :
			return self._totalgifstopng
		except Exception as e:
			raise e

	@property
	def totalimgsresized(self) :
		ur"""The total number of images resized to dimensions in the <img> tag.
		"""
		try :
			return self._totalimgsresized
		except Exception as e:
			raise e

	@property
	def imgsinlinedincssrate(self) :
		ur"""Rate (/s) counter for totalimgsinlinedincss.
		"""
		try :
			return self._imgsinlinedincssrate
		except Exception as e:
			raise e

	@property
	def inlinedcssrate(self) :
		ur"""Rate (/s) counter for totalinlinedcss.
		"""
		try :
			return self._inlinedcssrate
		except Exception as e:
			raise e

	@property
	def inlinedjsrate(self) :
		ur"""Rate (/s) counter for totalinlinedjs.
		"""
		try :
			return self._inlinedjsrate
		except Exception as e:
			raise e

	@property
	def origcacheobjectsrate(self) :
		ur"""Rate (/s) counter for origcacheobjects.
		"""
		try :
			return self._origcacheobjectsrate
		except Exception as e:
			raise e

	@property
	def cssminrate(self) :
		ur"""Rate (/s) counter for totalcssmin.
		"""
		try :
			return self._cssminrate
		except Exception as e:
			raise e

	@property
	def totalimgsdomainsharded(self) :
		ur"""Total no of images whose domain has been set from shards.
		"""
		try :
			return self._totalimgsdomainsharded
		except Exception as e:
			raise e

	@property
	def imgsdomainshardedrate(self) :
		ur"""Rate (/s) counter for totalimgsdomainsharded.
		"""
		try :
			return self._imgsdomainshardedrate
		except Exception as e:
			raise e

	@property
	def gifstopngrate(self) :
		ur"""Rate (/s) counter for totalgifstopng.
		"""
		try :
			return self._gifstopngrate
		except Exception as e:
			raise e

	@property
	def importtolinkrate(self) :
		ur"""Rate (/s) counter for totalimporttolink.
		"""
		try :
			return self._importtolinkrate
		except Exception as e:
			raise e

	@property
	def totalcsscombined(self) :
		ur"""The total number of CSS combined.
		"""
		try :
			return self._totalcsscombined
		except Exception as e:
			raise e

	@property
	def imgsresizedrate(self) :
		ur"""Rate (/s) counter for totalimgsresized.
		"""
		try :
			return self._imgsresizedrate
		except Exception as e:
			raise e

	@property
	def optcacheobjectsrate(self) :
		ur"""Rate (/s) counter for optcacheobjects.
		"""
		try :
			return self._optcacheobjectsrate
		except Exception as e:
			raise e

	@property
	def totaljpegsoptimized(self) :
		ur"""The total number of JPEG format images optimized.
		"""
		try :
			return self._totaljpegsoptimized
		except Exception as e:
			raise e

	@property
	def totalcacheextended(self) :
		ur"""The total number of objects cache extended.
		"""
		try :
			return self._totalcacheextended
		except Exception as e:
			raise e

	@property
	def origcacheobjects(self) :
		ur"""Total number of original cache objects ready to be served.
		"""
		try :
			return self._origcacheobjects
		except Exception as e:
			raise e

	@property
	def jsminrate(self) :
		ur"""Rate (/s) counter for totaljsmin.
		"""
		try :
			return self._jsminrate
		except Exception as e:
			raise e

	@property
	def jpegsoptimizedrate(self) :
		ur"""Rate (/s) counter for totaljpegsoptimized.
		"""
		try :
			return self._jpegsoptimizedrate
		except Exception as e:
			raise e

	@property
	def totaldatasavings(self) :
		ur"""Total data savings in bytes.
		"""
		try :
			return self._totaldatasavings
		except Exception as e:
			raise e

	@property
	def datasavingsrate(self) :
		ur"""Rate (/s) counter for totaldatasavings.
		"""
		try :
			return self._datasavingsrate
		except Exception as e:
			raise e

	@property
	def cacheextendedrate(self) :
		ur"""Rate (/s) counter for totalcacheextended.
		"""
		try :
			return self._cacheextendedrate
		except Exception as e:
			raise e

	@property
	def totalcssmin(self) :
		ur"""The total number of CSS files minified.
		"""
		try :
			return self._totalcssmin
		except Exception as e:
			raise e

	@property
	def totalinlinedimgs(self) :
		ur"""Total number of inlined images in HTML.
		"""
		try :
			return self._totalinlinedimgs
		except Exception as e:
			raise e

	@property
	def totalimporttolink(self) :
		ur"""The total number of CSS imports converted to links.
		"""
		try :
			return self._totalimporttolink
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(feo_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.feo
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
		ur""" Use this API to fetch the statistics of all feo_stats resources that are configured on netscaler.
		"""
		try :
			obj = feo_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class feo_response(base_response) :
	def __init__(self, length=1) :
		self.feo = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.feo = [feo_stats() for _ in range(length)]

