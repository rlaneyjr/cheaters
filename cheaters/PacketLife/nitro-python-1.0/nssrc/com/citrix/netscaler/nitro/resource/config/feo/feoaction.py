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

class feoaction(base_resource) :
	""" Configuration for Front end optimization action resource. """
	def __init__(self) :
		self._name = ""
		self._pageextendcache = False
		self._imgshrinktoattrib = False
		self._imggiftopng = False
		self._imginline = False
		self._cssimginline = False
		self._jpgoptimize = False
		self._imglazyload = False
		self._cssminify = False
		self._cssinline = False
		self._csscombine = False
		self._convertimporttolink = False
		self._jsminify = False
		self._jsinline = False
		self._htmlminify = False
		self._cssmovetohead = False
		self._jsmovetoend = False
		self._domainsharding = ""
		self._dnsshards = []
		self._clientsidemeasurements = False
		self._imgadddimensions = False
		self._imgshrinkformobile = False
		self._imgweaken = False
		self._jpgprogressive = False
		self._cssflattenimports = False
		self._jscombine = False
		self._htmlrmdefaultattribs = False
		self._htmlrmattribquotes = False
		self._htmltrimurls = False
		self._hits = 0
		self._undefhits = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""The name of the front end optimization action.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of the front end optimization action.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def pageextendcache(self) :
		ur"""Extend the time period during which the browser can use the cached resource.
		"""
		try :
			return self._pageextendcache
		except Exception as e:
			raise e

	@pageextendcache.setter
	def pageextendcache(self, pageextendcache) :
		ur"""Extend the time period during which the browser can use the cached resource.
		"""
		try :
			self._pageextendcache = pageextendcache
		except Exception as e:
			raise e

	@property
	def imgshrinktoattrib(self) :
		ur"""Shrink image dimensions as per the height and width attributes specified in the <img> tag.
		"""
		try :
			return self._imgshrinktoattrib
		except Exception as e:
			raise e

	@imgshrinktoattrib.setter
	def imgshrinktoattrib(self, imgshrinktoattrib) :
		ur"""Shrink image dimensions as per the height and width attributes specified in the <img> tag.
		"""
		try :
			self._imgshrinktoattrib = imgshrinktoattrib
		except Exception as e:
			raise e

	@property
	def imggiftopng(self) :
		ur"""Convert GIF image formats to PNG formats.
		"""
		try :
			return self._imggiftopng
		except Exception as e:
			raise e

	@imggiftopng.setter
	def imggiftopng(self, imggiftopng) :
		ur"""Convert GIF image formats to PNG formats.
		"""
		try :
			self._imggiftopng = imggiftopng
		except Exception as e:
			raise e

	@property
	def imginline(self) :
		ur"""Inline images whose size is less than 2KB.
		"""
		try :
			return self._imginline
		except Exception as e:
			raise e

	@imginline.setter
	def imginline(self, imginline) :
		ur"""Inline images whose size is less than 2KB.
		"""
		try :
			self._imginline = imginline
		except Exception as e:
			raise e

	@property
	def cssimginline(self) :
		ur"""Inline small images (less than 2KB) referred within CSS files as background-URLs.
		"""
		try :
			return self._cssimginline
		except Exception as e:
			raise e

	@cssimginline.setter
	def cssimginline(self, cssimginline) :
		ur"""Inline small images (less than 2KB) referred within CSS files as background-URLs.
		"""
		try :
			self._cssimginline = cssimginline
		except Exception as e:
			raise e

	@property
	def jpgoptimize(self) :
		ur"""Remove non-image data such as comments from JPEG images.
		"""
		try :
			return self._jpgoptimize
		except Exception as e:
			raise e

	@jpgoptimize.setter
	def jpgoptimize(self, jpgoptimize) :
		ur"""Remove non-image data such as comments from JPEG images.
		"""
		try :
			self._jpgoptimize = jpgoptimize
		except Exception as e:
			raise e

	@property
	def imglazyload(self) :
		ur"""Download images, only when the user scrolls the page to view them.
		"""
		try :
			return self._imglazyload
		except Exception as e:
			raise e

	@imglazyload.setter
	def imglazyload(self, imglazyload) :
		ur"""Download images, only when the user scrolls the page to view them.
		"""
		try :
			self._imglazyload = imglazyload
		except Exception as e:
			raise e

	@property
	def cssminify(self) :
		ur"""Remove comments and whitespaces from CSSs.
		"""
		try :
			return self._cssminify
		except Exception as e:
			raise e

	@cssminify.setter
	def cssminify(self, cssminify) :
		ur"""Remove comments and whitespaces from CSSs.
		"""
		try :
			self._cssminify = cssminify
		except Exception as e:
			raise e

	@property
	def cssinline(self) :
		ur"""Inline CSS files, whose size is less than 2KB, within the main page.
		"""
		try :
			return self._cssinline
		except Exception as e:
			raise e

	@cssinline.setter
	def cssinline(self, cssinline) :
		ur"""Inline CSS files, whose size is less than 2KB, within the main page.
		"""
		try :
			self._cssinline = cssinline
		except Exception as e:
			raise e

	@property
	def csscombine(self) :
		ur"""Combine one or more CSS files into one file.
		"""
		try :
			return self._csscombine
		except Exception as e:
			raise e

	@csscombine.setter
	def csscombine(self, csscombine) :
		ur"""Combine one or more CSS files into one file.
		"""
		try :
			self._csscombine = csscombine
		except Exception as e:
			raise e

	@property
	def convertimporttolink(self) :
		ur"""Convert CSS import statements to HTML link tags.
		"""
		try :
			return self._convertimporttolink
		except Exception as e:
			raise e

	@convertimporttolink.setter
	def convertimporttolink(self, convertimporttolink) :
		ur"""Convert CSS import statements to HTML link tags.
		"""
		try :
			self._convertimporttolink = convertimporttolink
		except Exception as e:
			raise e

	@property
	def jsminify(self) :
		ur"""Remove comments and whitespaces from JavaScript.
		"""
		try :
			return self._jsminify
		except Exception as e:
			raise e

	@jsminify.setter
	def jsminify(self, jsminify) :
		ur"""Remove comments and whitespaces from JavaScript.
		"""
		try :
			self._jsminify = jsminify
		except Exception as e:
			raise e

	@property
	def jsinline(self) :
		ur"""Convert linked JavaScript files (less than 2KB) to inline JavaScript files.
		"""
		try :
			return self._jsinline
		except Exception as e:
			raise e

	@jsinline.setter
	def jsinline(self, jsinline) :
		ur"""Convert linked JavaScript files (less than 2KB) to inline JavaScript files.
		"""
		try :
			self._jsinline = jsinline
		except Exception as e:
			raise e

	@property
	def htmlminify(self) :
		ur"""Remove comments and whitespaces from an HTML page.
		"""
		try :
			return self._htmlminify
		except Exception as e:
			raise e

	@htmlminify.setter
	def htmlminify(self, htmlminify) :
		ur"""Remove comments and whitespaces from an HTML page.
		"""
		try :
			self._htmlminify = htmlminify
		except Exception as e:
			raise e

	@property
	def cssmovetohead(self) :
		ur"""Move any CSS file present within the body tag of an HTML page to the head tag.
		"""
		try :
			return self._cssmovetohead
		except Exception as e:
			raise e

	@cssmovetohead.setter
	def cssmovetohead(self, cssmovetohead) :
		ur"""Move any CSS file present within the body tag of an HTML page to the head tag.
		"""
		try :
			self._cssmovetohead = cssmovetohead
		except Exception as e:
			raise e

	@property
	def jsmovetoend(self) :
		ur"""Move any JavaScript present in the body tag to the end of the body tag.
		"""
		try :
			return self._jsmovetoend
		except Exception as e:
			raise e

	@jsmovetoend.setter
	def jsmovetoend(self, jsmovetoend) :
		ur"""Move any JavaScript present in the body tag to the end of the body tag.
		"""
		try :
			self._jsmovetoend = jsmovetoend
		except Exception as e:
			raise e

	@property
	def domainsharding(self) :
		ur"""Domain name of the server.
		"""
		try :
			return self._domainsharding
		except Exception as e:
			raise e

	@domainsharding.setter
	def domainsharding(self, domainsharding) :
		ur"""Domain name of the server.
		"""
		try :
			self._domainsharding = domainsharding
		except Exception as e:
			raise e

	@property
	def dnsshards(self) :
		ur"""Set of domain names that replaces the parent domain.
		"""
		try :
			return self._dnsshards
		except Exception as e:
			raise e

	@dnsshards.setter
	def dnsshards(self, dnsshards) :
		ur"""Set of domain names that replaces the parent domain.
		"""
		try :
			self._dnsshards = dnsshards
		except Exception as e:
			raise e

	@property
	def clientsidemeasurements(self) :
		ur"""Collect the amount of time required for the client to load and render the web page.
		"""
		try :
			return self._clientsidemeasurements
		except Exception as e:
			raise e

	@clientsidemeasurements.setter
	def clientsidemeasurements(self, clientsidemeasurements) :
		ur"""Collect the amount of time required for the client to load and render the web page.
		"""
		try :
			self._clientsidemeasurements = clientsidemeasurements
		except Exception as e:
			raise e

	@property
	def imgadddimensions(self) :
		ur"""Add dimension attributes to images, if not specified within the <img> tag.
		"""
		try :
			return self._imgadddimensions
		except Exception as e:
			raise e

	@property
	def imgshrinkformobile(self) :
		ur"""Serve smaller images for mobile users.
		"""
		try :
			return self._imgshrinkformobile
		except Exception as e:
			raise e

	@property
	def imgweaken(self) :
		ur"""Reduce the image quality.
		"""
		try :
			return self._imgweaken
		except Exception as e:
			raise e

	@property
	def jpgprogressive(self) :
		ur"""Convert JPEG image formats to progressive formats.
		"""
		try :
			return self._jpgprogressive
		except Exception as e:
			raise e

	@property
	def cssflattenimports(self) :
		ur"""Replace CSS import statements with the file content.
		"""
		try :
			return self._cssflattenimports
		except Exception as e:
			raise e

	@property
	def jscombine(self) :
		ur"""Combine one or more JavaScript files into one file.
		"""
		try :
			return self._jscombine
		except Exception as e:
			raise e

	@property
	def htmlrmdefaultattribs(self) :
		ur"""Remove default redundant attributes from an HTML file.
		"""
		try :
			return self._htmlrmdefaultattribs
		except Exception as e:
			raise e

	@property
	def htmlrmattribquotes(self) :
		ur"""Remove unnecessary quotes present within the HTML attributes.
		"""
		try :
			return self._htmlrmattribquotes
		except Exception as e:
			raise e

	@property
	def htmltrimurls(self) :
		ur"""Trim URLs.
		"""
		try :
			return self._htmltrimurls
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The number of times the action has been taken.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		ur"""Total number of undefined policy hits.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine if front end optimization action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(feoaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.feoaction
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
		ur""" Use this API to add feoaction.
		"""
		try :
			if type(resource) is not list :
				addresource = feoaction()
				addresource.name = resource.name
				addresource.pageextendcache = resource.pageextendcache
				addresource.imgshrinktoattrib = resource.imgshrinktoattrib
				addresource.imggiftopng = resource.imggiftopng
				addresource.imginline = resource.imginline
				addresource.cssimginline = resource.cssimginline
				addresource.jpgoptimize = resource.jpgoptimize
				addresource.imglazyload = resource.imglazyload
				addresource.cssminify = resource.cssminify
				addresource.cssinline = resource.cssinline
				addresource.csscombine = resource.csscombine
				addresource.convertimporttolink = resource.convertimporttolink
				addresource.jsminify = resource.jsminify
				addresource.jsinline = resource.jsinline
				addresource.htmlminify = resource.htmlminify
				addresource.cssmovetohead = resource.cssmovetohead
				addresource.jsmovetoend = resource.jsmovetoend
				addresource.domainsharding = resource.domainsharding
				addresource.dnsshards = resource.dnsshards
				addresource.clientsidemeasurements = resource.clientsidemeasurements
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ feoaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].pageextendcache = resource[i].pageextendcache
						addresources[i].imgshrinktoattrib = resource[i].imgshrinktoattrib
						addresources[i].imggiftopng = resource[i].imggiftopng
						addresources[i].imginline = resource[i].imginline
						addresources[i].cssimginline = resource[i].cssimginline
						addresources[i].jpgoptimize = resource[i].jpgoptimize
						addresources[i].imglazyload = resource[i].imglazyload
						addresources[i].cssminify = resource[i].cssminify
						addresources[i].cssinline = resource[i].cssinline
						addresources[i].csscombine = resource[i].csscombine
						addresources[i].convertimporttolink = resource[i].convertimporttolink
						addresources[i].jsminify = resource[i].jsminify
						addresources[i].jsinline = resource[i].jsinline
						addresources[i].htmlminify = resource[i].htmlminify
						addresources[i].cssmovetohead = resource[i].cssmovetohead
						addresources[i].jsmovetoend = resource[i].jsmovetoend
						addresources[i].domainsharding = resource[i].domainsharding
						addresources[i].dnsshards = resource[i].dnsshards
						addresources[i].clientsidemeasurements = resource[i].clientsidemeasurements
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update feoaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = feoaction()
				updateresource.name = resource.name
				updateresource.pageextendcache = resource.pageextendcache
				updateresource.imgshrinktoattrib = resource.imgshrinktoattrib
				updateresource.imggiftopng = resource.imggiftopng
				updateresource.imginline = resource.imginline
				updateresource.cssimginline = resource.cssimginline
				updateresource.jpgoptimize = resource.jpgoptimize
				updateresource.imglazyload = resource.imglazyload
				updateresource.cssminify = resource.cssminify
				updateresource.cssinline = resource.cssinline
				updateresource.csscombine = resource.csscombine
				updateresource.convertimporttolink = resource.convertimporttolink
				updateresource.jsminify = resource.jsminify
				updateresource.jsinline = resource.jsinline
				updateresource.htmlminify = resource.htmlminify
				updateresource.cssmovetohead = resource.cssmovetohead
				updateresource.jsmovetoend = resource.jsmovetoend
				updateresource.domainsharding = resource.domainsharding
				updateresource.dnsshards = resource.dnsshards
				updateresource.clientsidemeasurements = resource.clientsidemeasurements
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ feoaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].pageextendcache = resource[i].pageextendcache
						updateresources[i].imgshrinktoattrib = resource[i].imgshrinktoattrib
						updateresources[i].imggiftopng = resource[i].imggiftopng
						updateresources[i].imginline = resource[i].imginline
						updateresources[i].cssimginline = resource[i].cssimginline
						updateresources[i].jpgoptimize = resource[i].jpgoptimize
						updateresources[i].imglazyload = resource[i].imglazyload
						updateresources[i].cssminify = resource[i].cssminify
						updateresources[i].cssinline = resource[i].cssinline
						updateresources[i].csscombine = resource[i].csscombine
						updateresources[i].convertimporttolink = resource[i].convertimporttolink
						updateresources[i].jsminify = resource[i].jsminify
						updateresources[i].jsinline = resource[i].jsinline
						updateresources[i].htmlminify = resource[i].htmlminify
						updateresources[i].cssmovetohead = resource[i].cssmovetohead
						updateresources[i].jsmovetoend = resource[i].jsmovetoend
						updateresources[i].domainsharding = resource[i].domainsharding
						updateresources[i].dnsshards = resource[i].dnsshards
						updateresources[i].clientsidemeasurements = resource[i].clientsidemeasurements
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of feoaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = feoaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete feoaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = feoaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ feoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the feoaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = feoaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = feoaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [feoaction() for _ in range(len(name))]
							obj = [feoaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = feoaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of feoaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = feoaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the feoaction resources configured on NetScaler.
		"""
		try :
			obj = feoaction()
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
		ur""" Use this API to count filtered the set of feoaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = feoaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

class feoaction_response(base_response) :
	def __init__(self, length=1) :
		self.feoaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.feoaction = [feoaction() for _ in range(length)]

