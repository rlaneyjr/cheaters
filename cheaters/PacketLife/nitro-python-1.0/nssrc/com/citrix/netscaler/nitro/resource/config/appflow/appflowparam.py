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

class appflowparam(base_resource) :
	""" Configuration for AppFlow parameter resource. """
	def __init__(self) :
		self._templaterefresh = 0
		self._appnamerefresh = 0
		self._flowrecordinterval = 0
		self._udppmtu = 0
		self._httpurl = ""
		self._aaausername = ""
		self._httpcookie = ""
		self._httpreferer = ""
		self._httpmethod = ""
		self._httphost = ""
		self._httpuseragent = ""
		self._clienttrafficonly = ""
		self._httpcontenttype = ""
		self._httpauthorization = ""
		self._httpvia = ""
		self._httpxforwardedfor = ""
		self._httplocation = ""
		self._httpsetcookie = ""
		self._httpsetcookie2 = ""
		self._connectionchaining = ""
		self._httpdomain = ""
		self._skipcacheredirectionhttptransaction = ""

	@property
	def templaterefresh(self) :
		ur"""Refresh interval, in seconds, at which to export the template data. Because data transmission is in UDP, the templates must be resent at regular intervals.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._templaterefresh
		except Exception as e:
			raise e

	@templaterefresh.setter
	def templaterefresh(self, templaterefresh) :
		ur"""Refresh interval, in seconds, at which to export the template data. Because data transmission is in UDP, the templates must be resent at regular intervals.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._templaterefresh = templaterefresh
		except Exception as e:
			raise e

	@property
	def appnamerefresh(self) :
		ur"""Interval, in seconds, at which to send Appnames to the configured collectors. Appname refers to the name of an entity (virtual server, service, or service group) in the NetScaler appliance.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._appnamerefresh
		except Exception as e:
			raise e

	@appnamerefresh.setter
	def appnamerefresh(self, appnamerefresh) :
		ur"""Interval, in seconds, at which to send Appnames to the configured collectors. Appname refers to the name of an entity (virtual server, service, or service group) in the NetScaler appliance.<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._appnamerefresh = appnamerefresh
		except Exception as e:
			raise e

	@property
	def flowrecordinterval(self) :
		ur"""Interval, in seconds, at which to send flow records to the configured collectors.<br/>Default value: 60<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._flowrecordinterval
		except Exception as e:
			raise e

	@flowrecordinterval.setter
	def flowrecordinterval(self, flowrecordinterval) :
		ur"""Interval, in seconds, at which to send flow records to the configured collectors.<br/>Default value: 60<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._flowrecordinterval = flowrecordinterval
		except Exception as e:
			raise e

	@property
	def udppmtu(self) :
		ur"""MTU, in bytes, for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472.
		"""
		try :
			return self._udppmtu
		except Exception as e:
			raise e

	@udppmtu.setter
	def udppmtu(self, udppmtu) :
		ur"""MTU, in bytes, for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472
		"""
		try :
			self._udppmtu = udppmtu
		except Exception as e:
			raise e

	@property
	def httpurl(self) :
		ur"""Include the http URL that the NetScaler appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpurl
		except Exception as e:
			raise e

	@httpurl.setter
	def httpurl(self, httpurl) :
		ur"""Include the http URL that the NetScaler appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpurl = httpurl
		except Exception as e:
			raise e

	@property
	def aaausername(self) :
		ur"""Enable AppFlow AAA Username logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._aaausername
		except Exception as e:
			raise e

	@aaausername.setter
	def aaausername(self, aaausername) :
		ur"""Enable AppFlow AAA Username logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._aaausername = aaausername
		except Exception as e:
			raise e

	@property
	def httpcookie(self) :
		ur"""Include the cookie that was in the HTTP request the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpcookie
		except Exception as e:
			raise e

	@httpcookie.setter
	def httpcookie(self, httpcookie) :
		ur"""Include the cookie that was in the HTTP request the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpcookie = httpcookie
		except Exception as e:
			raise e

	@property
	def httpreferer(self) :
		ur"""Include the web page that was last visited by the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpreferer
		except Exception as e:
			raise e

	@httpreferer.setter
	def httpreferer(self, httpreferer) :
		ur"""Include the web page that was last visited by the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpreferer = httpreferer
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		ur"""Include the method that was specified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		ur"""Include the method that was specified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def httphost(self) :
		ur"""Include the host identified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httphost
		except Exception as e:
			raise e

	@httphost.setter
	def httphost(self, httphost) :
		ur"""Include the host identified in the HTTP request that the appliance received from the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httphost = httphost
		except Exception as e:
			raise e

	@property
	def httpuseragent(self) :
		ur"""Include the client application through which the HTTP request was received by the NetScaler appliance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpuseragent
		except Exception as e:
			raise e

	@httpuseragent.setter
	def httpuseragent(self, httpuseragent) :
		ur"""Include the client application through which the HTTP request was received by the NetScaler appliance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpuseragent = httpuseragent
		except Exception as e:
			raise e

	@property
	def clienttrafficonly(self) :
		ur"""Generate AppFlow records for only the traffic from the client.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._clienttrafficonly
		except Exception as e:
			raise e

	@clienttrafficonly.setter
	def clienttrafficonly(self, clienttrafficonly) :
		ur"""Generate AppFlow records for only the traffic from the client.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._clienttrafficonly = clienttrafficonly
		except Exception as e:
			raise e

	@property
	def httpcontenttype(self) :
		ur"""Include the HTTP Content-Type header sent from the server to the client to determine the type of the content sent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpcontenttype
		except Exception as e:
			raise e

	@httpcontenttype.setter
	def httpcontenttype(self, httpcontenttype) :
		ur"""Include the HTTP Content-Type header sent from the server to the client to determine the type of the content sent.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpcontenttype = httpcontenttype
		except Exception as e:
			raise e

	@property
	def httpauthorization(self) :
		ur"""Include the HTTP Authorization header information.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpauthorization
		except Exception as e:
			raise e

	@httpauthorization.setter
	def httpauthorization(self, httpauthorization) :
		ur"""Include the HTTP Authorization header information.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpauthorization = httpauthorization
		except Exception as e:
			raise e

	@property
	def httpvia(self) :
		ur"""Include the httpVia header which contains the IP address of proxy server through which the client accessed the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpvia
		except Exception as e:
			raise e

	@httpvia.setter
	def httpvia(self, httpvia) :
		ur"""Include the httpVia header which contains the IP address of proxy server through which the client accessed the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpvia = httpvia
		except Exception as e:
			raise e

	@property
	def httpxforwardedfor(self) :
		ur"""Include the httpXForwardedFor header, which contains the original IP Address of the client using a proxy server to access the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpxforwardedfor
		except Exception as e:
			raise e

	@httpxforwardedfor.setter
	def httpxforwardedfor(self, httpxforwardedfor) :
		ur"""Include the httpXForwardedFor header, which contains the original IP Address of the client using a proxy server to access the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpxforwardedfor = httpxforwardedfor
		except Exception as e:
			raise e

	@property
	def httplocation(self) :
		ur"""Include the HTTP location headers returned from the HTTP responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httplocation
		except Exception as e:
			raise e

	@httplocation.setter
	def httplocation(self, httplocation) :
		ur"""Include the HTTP location headers returned from the HTTP responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httplocation = httplocation
		except Exception as e:
			raise e

	@property
	def httpsetcookie(self) :
		ur"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpsetcookie
		except Exception as e:
			raise e

	@httpsetcookie.setter
	def httpsetcookie(self, httpsetcookie) :
		ur"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpsetcookie = httpsetcookie
		except Exception as e:
			raise e

	@property
	def httpsetcookie2(self) :
		ur"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpsetcookie2
		except Exception as e:
			raise e

	@httpsetcookie2.setter
	def httpsetcookie2(self, httpsetcookie2) :
		ur"""Include the Set-cookie header sent from the server to the client in response to a HTTP request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpsetcookie2 = httpsetcookie2
		except Exception as e:
			raise e

	@property
	def connectionchaining(self) :
		ur"""Enable connection chaining so that the client server flows of a connection are linked. Also the connection chain ID is propagated across NetScalers, so that in a multi-hop environment the flows belonging to the same logical connection are linked. This id is also logged as part of appflow record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._connectionchaining
		except Exception as e:
			raise e

	@connectionchaining.setter
	def connectionchaining(self, connectionchaining) :
		ur"""Enable connection chaining so that the client server flows of a connection are linked. Also the connection chain ID is propagated across NetScalers, so that in a multi-hop environment the flows belonging to the same logical connection are linked. This id is also logged as part of appflow record.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._connectionchaining = connectionchaining
		except Exception as e:
			raise e

	@property
	def httpdomain(self) :
		ur"""Include the http domain request to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpdomain
		except Exception as e:
			raise e

	@httpdomain.setter
	def httpdomain(self, httpdomain) :
		ur"""Include the http domain request to be exported.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpdomain = httpdomain
		except Exception as e:
			raise e

	@property
	def skipcacheredirectionhttptransaction(self) :
		ur"""Skip Cache http transaction. This HTTP transaction is specific to Cache Redirection module. In Case of Cache Miss there will be another HTTP transaction initiated by the cache server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skipcacheredirectionhttptransaction
		except Exception as e:
			raise e

	@skipcacheredirectionhttptransaction.setter
	def skipcacheredirectionhttptransaction(self, skipcacheredirectionhttptransaction) :
		ur"""Skip Cache http transaction. This HTTP transaction is specific to Cache Redirection module. In Case of Cache Miss there will be another HTTP transaction initiated by the cache server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skipcacheredirectionhttptransaction = skipcacheredirectionhttptransaction
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appflowparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appflowparam
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
		ur""" Use this API to update appflowparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = appflowparam()
				updateresource.templaterefresh = resource.templaterefresh
				updateresource.appnamerefresh = resource.appnamerefresh
				updateresource.flowrecordinterval = resource.flowrecordinterval
				updateresource.udppmtu = resource.udppmtu
				updateresource.httpurl = resource.httpurl
				updateresource.aaausername = resource.aaausername
				updateresource.httpcookie = resource.httpcookie
				updateresource.httpreferer = resource.httpreferer
				updateresource.httpmethod = resource.httpmethod
				updateresource.httphost = resource.httphost
				updateresource.httpuseragent = resource.httpuseragent
				updateresource.clienttrafficonly = resource.clienttrafficonly
				updateresource.httpcontenttype = resource.httpcontenttype
				updateresource.httpauthorization = resource.httpauthorization
				updateresource.httpvia = resource.httpvia
				updateresource.httpxforwardedfor = resource.httpxforwardedfor
				updateresource.httplocation = resource.httplocation
				updateresource.httpsetcookie = resource.httpsetcookie
				updateresource.httpsetcookie2 = resource.httpsetcookie2
				updateresource.connectionchaining = resource.connectionchaining
				updateresource.httpdomain = resource.httpdomain
				updateresource.skipcacheredirectionhttptransaction = resource.skipcacheredirectionhttptransaction
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of appflowparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appflowparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the appflowparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appflowparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Httpreferer:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpsetcookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpvia:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpdomain:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpsetcookie2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpauthorization:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Skipcacheredirectionhttptransaction:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Aaausername:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clienttrafficonly:
		YES = "YES"
		NO = "NO"

	class Httpcontenttype:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpmethod:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httplocation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Connectionchaining:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpxforwardedfor:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpcookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpurl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpuseragent:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httphost:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class appflowparam_response(base_response) :
	def __init__(self, length=1) :
		self.appflowparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appflowparam = [appflowparam() for _ in range(length)]

