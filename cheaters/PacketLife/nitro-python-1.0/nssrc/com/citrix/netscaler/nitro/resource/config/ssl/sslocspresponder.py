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

class sslocspresponder(base_resource) :
	""" Configuration for OCSP responser resource. """
	def __init__(self) :
		self._name = ""
		self._url = ""
		self._cache = ""
		self._cachetimeout = 0
		self._batchingdepth = 0
		self._batchingdelay = 0
		self._resptimeout = 0
		self._respondercert = ""
		self._trustresponder = False
		self._producedattimeskew = 0
		self._signingcert = ""
		self._usenonce = ""
		self._insertclientcert = ""
		self._useaia = False
		self._dns = ""
		self._ipaddress = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the OCSP responder. Cannot begin with a hash (#) or space character and must contain only ASCII alphanumeric, underscore (_), hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the responder is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder" or 'my responder').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the OCSP responder. Cannot begin with a hash (#) or space character and must contain only ASCII alphanumeric, underscore (_), hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the responder is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder" or 'my responder').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def url(self) :
		ur"""URL of the OCSP responder.<br/>Minimum length =  1.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		ur"""URL of the OCSP responder.<br/>Minimum length =  1
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def cache(self) :
		ur"""Enable caching of responses. Caching of responses received from the OCSP responder enables faster responses to the clients and reduces the load on the OCSP responder.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cache
		except Exception as e:
			raise e

	@cache.setter
	def cache(self, cache) :
		ur"""Enable caching of responses. Caching of responses received from the OCSP responder enables faster responses to the clients and reduces the load on the OCSP responder.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cache = cache
		except Exception as e:
			raise e

	@property
	def cachetimeout(self) :
		ur"""Timeout for caching the OCSP response. After the timeout, the NetScaler sends a fresh request to the OCSP responder for the certificate status. If a timeout is not specified, the timeout provided in the OCSP response applies.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._cachetimeout
		except Exception as e:
			raise e

	@cachetimeout.setter
	def cachetimeout(self, cachetimeout) :
		ur"""Timeout for caching the OCSP response. After the timeout, the NetScaler sends a fresh request to the OCSP responder for the certificate status. If a timeout is not specified, the timeout provided in the OCSP response applies.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._cachetimeout = cachetimeout
		except Exception as e:
			raise e

	@property
	def batchingdepth(self) :
		ur"""Number of client certificates to batch together into one OCSP request. Batching avoids overloading the OCSP responder. A value of 1 signifies that each request is queried independently. For a value greater than 1, specify a timeout (batching delay) to avoid inordinately delaying the processing of a single certificate.<br/>Minimum length =  1<br/>Maximum length =  8.
		"""
		try :
			return self._batchingdepth
		except Exception as e:
			raise e

	@batchingdepth.setter
	def batchingdepth(self, batchingdepth) :
		ur"""Number of client certificates to batch together into one OCSP request. Batching avoids overloading the OCSP responder. A value of 1 signifies that each request is queried independently. For a value greater than 1, specify a timeout (batching delay) to avoid inordinately delaying the processing of a single certificate.<br/>Minimum length =  1<br/>Maximum length =  8
		"""
		try :
			self._batchingdepth = batchingdepth
		except Exception as e:
			raise e

	@property
	def batchingdelay(self) :
		ur"""Maximum time, in milliseconds, to wait to accumulate OCSP requests to batch.  Does not apply if the Batching Depth is 1.<br/>Maximum length =  10000.
		"""
		try :
			return self._batchingdelay
		except Exception as e:
			raise e

	@batchingdelay.setter
	def batchingdelay(self, batchingdelay) :
		ur"""Maximum time, in milliseconds, to wait to accumulate OCSP requests to batch.  Does not apply if the Batching Depth is 1.<br/>Maximum length =  10000
		"""
		try :
			self._batchingdelay = batchingdelay
		except Exception as e:
			raise e

	@property
	def resptimeout(self) :
		ur"""Time, in milliseconds, to wait for an OCSP response. When this time elapses, an error message appears or the transaction is forwarded, depending on the settings on the virtual server. Includes Batching Delay time.<br/>Maximum length =  120000.
		"""
		try :
			return self._resptimeout
		except Exception as e:
			raise e

	@resptimeout.setter
	def resptimeout(self, resptimeout) :
		ur"""Time, in milliseconds, to wait for an OCSP response. When this time elapses, an error message appears or the transaction is forwarded, depending on the settings on the virtual server. Includes Batching Delay time.<br/>Maximum length =  120000
		"""
		try :
			self._resptimeout = resptimeout
		except Exception as e:
			raise e

	@property
	def respondercert(self) :
		ur""".<br/>Minimum length =  1.
		"""
		try :
			return self._respondercert
		except Exception as e:
			raise e

	@respondercert.setter
	def respondercert(self, respondercert) :
		ur""".<br/>Minimum length =  1
		"""
		try :
			self._respondercert = respondercert
		except Exception as e:
			raise e

	@property
	def trustresponder(self) :
		ur"""A certificate to use to validate OCSP responses.  Alternatively, if -trustResponder is specified, no verification will be done on the reponse.  If both are omitted, only the response times (producedAt, lastUpdate, nextUpdate) will be verified.
		"""
		try :
			return self._trustresponder
		except Exception as e:
			raise e

	@trustresponder.setter
	def trustresponder(self, trustresponder) :
		ur"""A certificate to use to validate OCSP responses.  Alternatively, if -trustResponder is specified, no verification will be done on the reponse.  If both are omitted, only the response times (producedAt, lastUpdate, nextUpdate) will be verified.
		"""
		try :
			self._trustresponder = trustresponder
		except Exception as e:
			raise e

	@property
	def producedattimeskew(self) :
		ur"""Time, in seconds, for which the NetScaler waits before considering the response as invalid. The response is considered invalid if the Produced At time stamp in the OCSP response exceeds or precedes the current NetScaler clock time by the amount of time specified.<br/>Default value: 300<br/>Maximum length =  86400.
		"""
		try :
			return self._producedattimeskew
		except Exception as e:
			raise e

	@producedattimeskew.setter
	def producedattimeskew(self, producedattimeskew) :
		ur"""Time, in seconds, for which the NetScaler waits before considering the response as invalid. The response is considered invalid if the Produced At time stamp in the OCSP response exceeds or precedes the current NetScaler clock time by the amount of time specified.<br/>Default value: 300<br/>Maximum length =  86400
		"""
		try :
			self._producedattimeskew = producedattimeskew
		except Exception as e:
			raise e

	@property
	def signingcert(self) :
		ur"""Certificate-key pair that is used to sign OCSP requests. If this parameter is not set, the requests are not signed.<br/>Minimum length =  1.
		"""
		try :
			return self._signingcert
		except Exception as e:
			raise e

	@signingcert.setter
	def signingcert(self, signingcert) :
		ur"""Certificate-key pair that is used to sign OCSP requests. If this parameter is not set, the requests are not signed.<br/>Minimum length =  1
		"""
		try :
			self._signingcert = signingcert
		except Exception as e:
			raise e

	@property
	def usenonce(self) :
		ur"""Enable the OCSP nonce extension, which is designed to prevent replay attacks.<br/>Possible values = YES, NO.
		"""
		try :
			return self._usenonce
		except Exception as e:
			raise e

	@usenonce.setter
	def usenonce(self, usenonce) :
		ur"""Enable the OCSP nonce extension, which is designed to prevent replay attacks.<br/>Possible values = YES, NO
		"""
		try :
			self._usenonce = usenonce
		except Exception as e:
			raise e

	@property
	def insertclientcert(self) :
		ur"""Include the complete client certificate in the OCSP request.<br/>Possible values = YES, NO.
		"""
		try :
			return self._insertclientcert
		except Exception as e:
			raise e

	@insertclientcert.setter
	def insertclientcert(self, insertclientcert) :
		ur"""Include the complete client certificate in the OCSP request.<br/>Possible values = YES, NO
		"""
		try :
			self._insertclientcert = insertclientcert
		except Exception as e:
			raise e

	@property
	def useaia(self) :
		ur"""Only use the URL present in the certificate.
		"""
		try :
			return self._useaia
		except Exception as e:
			raise e

	@property
	def dns(self) :
		ur"""Was DNS resolution successful for a domain-based OCSP responder.
		"""
		try :
			return self._dns
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""The IPv6 address of the ocsp responder.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslocspresponder_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslocspresponder
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
		ur""" Use this API to add sslocspresponder.
		"""
		try :
			if type(resource) is not list :
				addresource = sslocspresponder()
				addresource.name = resource.name
				addresource.url = resource.url
				addresource.cache = resource.cache
				addresource.cachetimeout = resource.cachetimeout
				addresource.batchingdepth = resource.batchingdepth
				addresource.batchingdelay = resource.batchingdelay
				addresource.resptimeout = resource.resptimeout
				addresource.respondercert = resource.respondercert
				addresource.trustresponder = resource.trustresponder
				addresource.producedattimeskew = resource.producedattimeskew
				addresource.signingcert = resource.signingcert
				addresource.usenonce = resource.usenonce
				addresource.insertclientcert = resource.insertclientcert
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslocspresponder() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].url = resource[i].url
						addresources[i].cache = resource[i].cache
						addresources[i].cachetimeout = resource[i].cachetimeout
						addresources[i].batchingdepth = resource[i].batchingdepth
						addresources[i].batchingdelay = resource[i].batchingdelay
						addresources[i].resptimeout = resource[i].resptimeout
						addresources[i].respondercert = resource[i].respondercert
						addresources[i].trustresponder = resource[i].trustresponder
						addresources[i].producedattimeskew = resource[i].producedattimeskew
						addresources[i].signingcert = resource[i].signingcert
						addresources[i].usenonce = resource[i].usenonce
						addresources[i].insertclientcert = resource[i].insertclientcert
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete sslocspresponder.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslocspresponder()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update sslocspresponder.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslocspresponder()
				updateresource.name = resource.name
				updateresource.url = resource.url
				updateresource.cache = resource.cache
				updateresource.cachetimeout = resource.cachetimeout
				updateresource.batchingdepth = resource.batchingdepth
				updateresource.batchingdelay = resource.batchingdelay
				updateresource.resptimeout = resource.resptimeout
				updateresource.respondercert = resource.respondercert
				updateresource.trustresponder = resource.trustresponder
				updateresource.producedattimeskew = resource.producedattimeskew
				updateresource.signingcert = resource.signingcert
				updateresource.usenonce = resource.usenonce
				updateresource.insertclientcert = resource.insertclientcert
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslocspresponder() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].url = resource[i].url
						updateresources[i].cache = resource[i].cache
						updateresources[i].cachetimeout = resource[i].cachetimeout
						updateresources[i].batchingdepth = resource[i].batchingdepth
						updateresources[i].batchingdelay = resource[i].batchingdelay
						updateresources[i].resptimeout = resource[i].resptimeout
						updateresources[i].respondercert = resource[i].respondercert
						updateresources[i].trustresponder = resource[i].trustresponder
						updateresources[i].producedattimeskew = resource[i].producedattimeskew
						updateresources[i].signingcert = resource[i].signingcert
						updateresources[i].usenonce = resource[i].usenonce
						updateresources[i].insertclientcert = resource[i].insertclientcert
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of sslocspresponder resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslocspresponder()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
					unsetresource.insertclientcert = resource.insertclientcert
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
							unsetresources[i].insertclientcert = resource[i].insertclientcert
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslocspresponder resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslocspresponder()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = sslocspresponder()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [sslocspresponder() for _ in range(len(name))]
							obj = [sslocspresponder() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = sslocspresponder()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of sslocspresponder resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslocspresponder()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the sslocspresponder resources configured on NetScaler.
		"""
		try :
			obj = sslocspresponder()
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
		ur""" Use this API to count filtered the set of sslocspresponder resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslocspresponder()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Insertclientcert:
		YES = "YES"
		NO = "NO"

	class Usenonce:
		YES = "YES"
		NO = "NO"

	class Cache:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class sslocspresponder_response(base_response) :
	def __init__(self, length=1) :
		self.sslocspresponder = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslocspresponder = [sslocspresponder() for _ in range(length)]

