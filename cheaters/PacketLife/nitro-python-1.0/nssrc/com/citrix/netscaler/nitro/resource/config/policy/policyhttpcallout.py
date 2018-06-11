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

class policyhttpcallout(base_resource) :
	""" Configuration for HTTP callout resource. """
	def __init__(self) :
		self._name = ""
		self._ipaddress = ""
		self._port = 0
		self._vserver = ""
		self._returntype = ""
		self._httpmethod = ""
		self._hostexpr = ""
		self._urlstemexpr = ""
		self._headers = []
		self._parameters = []
		self._bodyexpr = ""
		self._fullreqexpr = ""
		self._scheme = ""
		self._resultexpr = ""
		self._cacheforsecs = 0
		self._comment = ""
		self._hits = 0
		self._undefhits = 0
		self._svrstate = ""
		self._undefreason = ""
		self._recursivecallout = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the HTTP callout. Not case sensitive. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Must not begin with 're' or 'xp' or be a word reserved for use as a default syntax expression qualifier prefix (such as HTTP) or enumeration value (such as ASCII). Must not be the name of an existing named expression, pattern set, dataset, stringmap, or HTTP callout.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the HTTP callout. Not case sensitive. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Must not begin with 're' or 'xp' or be a word reserved for use as a default syntax expression qualifier prefix (such as HTTP) or enumeration value (such as ASCII). Must not be the name of an existing named expression, pattern set, dataset, stringmap, or HTTP callout.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""IP Address of the server (callout agent) to which the callout is sent. Can be an IPv4 or IPv6 address.
		Mutually exclusive with the Virtual Server parameter. Therefore, you cannot set the <IP Address, Port> and the Virtual Server in the same HTTP callout.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""IP Address of the server (callout agent) to which the callout is sent. Can be an IPv4 or IPv6 address.
		Mutually exclusive with the Virtual Server parameter. Therefore, you cannot set the <IP Address, Port> and the Virtual Server in the same HTTP callout.
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Server port to which the HTTP callout agent is mapped. Mutually exclusive with the Virtual Server parameter. Therefore, you cannot set the <IP Address, Port> and the Virtual Server in the same HTTP callout.<br/>Minimum length =  1.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""Server port to which the HTTP callout agent is mapped. Mutually exclusive with the Virtual Server parameter. Therefore, you cannot set the <IP Address, Port> and the Virtual Server in the same HTTP callout.<br/>Minimum length =  1
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def vserver(self) :
		ur"""Name of the load balancing, content switching, or cache redirection virtual server (the callout agent) to which the HTTP callout is sent. The service type of the virtual server must be HTTP. Mutually exclusive with the IP address and port parameters. Therefore, you cannot set the <IP Address, Port> and the Virtual Server in the same HTTP callout.<br/>Minimum length =  1.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		ur"""Name of the load balancing, content switching, or cache redirection virtual server (the callout agent) to which the HTTP callout is sent. The service type of the virtual server must be HTTP. Mutually exclusive with the IP address and port parameters. Therefore, you cannot set the <IP Address, Port> and the Virtual Server in the same HTTP callout.<br/>Minimum length =  1
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	@property
	def returntype(self) :
		ur"""Type of data that the target callout agent returns in response to the callout. 
		Available settings function as follows:
		* TEXT - Treat the returned value as a text string. 
		* NUM - Treat the returned value as a number.
		* BOOL - Treat the returned value as a Boolean value. 
		Note: You cannot change the return type after it is set.<br/>Possible values = BOOL, NUM, TEXT.
		"""
		try :
			return self._returntype
		except Exception as e:
			raise e

	@returntype.setter
	def returntype(self, returntype) :
		ur"""Type of data that the target callout agent returns in response to the callout. 
		Available settings function as follows:
		* TEXT - Treat the returned value as a text string. 
		* NUM - Treat the returned value as a number.
		* BOOL - Treat the returned value as a Boolean value. 
		Note: You cannot change the return type after it is set.<br/>Possible values = BOOL, NUM, TEXT
		"""
		try :
			self._returntype = returntype
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		ur"""Method used in the HTTP request that this callout sends.  Mutually exclusive with the full HTTP request expression.<br/>Possible values = GET, POST.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		ur"""Method used in the HTTP request that this callout sends.  Mutually exclusive with the full HTTP request expression.<br/>Possible values = GET, POST
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def hostexpr(self) :
		ur"""Default Syntax string expression to configure the Host header. Can contain a literal value (for example, 10.101.10.11) or a derived value (for example, http.req.header("Host")). The literal value can be an IP address or a fully qualified domain name. Mutually exclusive with the full HTTP request expression.<br/>Minimum length =  1.
		"""
		try :
			return self._hostexpr
		except Exception as e:
			raise e

	@hostexpr.setter
	def hostexpr(self, hostexpr) :
		ur"""Default Syntax string expression to configure the Host header. Can contain a literal value (for example, 10.101.10.11) or a derived value (for example, http.req.header("Host")). The literal value can be an IP address or a fully qualified domain name. Mutually exclusive with the full HTTP request expression.<br/>Minimum length =  1
		"""
		try :
			self._hostexpr = hostexpr
		except Exception as e:
			raise e

	@property
	def urlstemexpr(self) :
		ur"""Default Syntax string expression for generating the URL stem. Can contain a literal string (for example, "/mysite/index.html") or an expression that derives the value (for example, http.req.url). Mutually exclusive with the full HTTP request expression.<br/>Minimum length =  1.
		"""
		try :
			return self._urlstemexpr
		except Exception as e:
			raise e

	@urlstemexpr.setter
	def urlstemexpr(self, urlstemexpr) :
		ur"""Default Syntax string expression for generating the URL stem. Can contain a literal string (for example, "/mysite/index.html") or an expression that derives the value (for example, http.req.url). Mutually exclusive with the full HTTP request expression.<br/>Minimum length =  1
		"""
		try :
			self._urlstemexpr = urlstemexpr
		except Exception as e:
			raise e

	@property
	def headers(self) :
		ur"""One or more headers to insert into the HTTP request. Each header is specified as "name(expr)", where expr is a default syntax expression that is evaluated at runtime to provide the value for the named header. You can configure a maximum of eight headers for an HTTP callout. Mutually exclusive with the full HTTP request expression.
		"""
		try :
			return self._headers
		except Exception as e:
			raise e

	@headers.setter
	def headers(self, headers) :
		ur"""One or more headers to insert into the HTTP request. Each header is specified as "name(expr)", where expr is a default syntax expression that is evaluated at runtime to provide the value for the named header. You can configure a maximum of eight headers for an HTTP callout. Mutually exclusive with the full HTTP request expression.
		"""
		try :
			self._headers = headers
		except Exception as e:
			raise e

	@property
	def parameters(self) :
		ur"""One or more query parameters to insert into the HTTP request URL (for a GET request) or into the request body (for a POST request). Each parameter is specified as "name(expr)", where expr is an default syntax expression that is evaluated at run time to provide the value for the named parameter (name=value). The parameter values are URL encoded. Mutually exclusive with the full HTTP request expression.
		"""
		try :
			return self._parameters
		except Exception as e:
			raise e

	@parameters.setter
	def parameters(self, parameters) :
		ur"""One or more query parameters to insert into the HTTP request URL (for a GET request) or into the request body (for a POST request). Each parameter is specified as "name(expr)", where expr is an default syntax expression that is evaluated at run time to provide the value for the named parameter (name=value). The parameter values are URL encoded. Mutually exclusive with the full HTTP request expression.
		"""
		try :
			self._parameters = parameters
		except Exception as e:
			raise e

	@property
	def bodyexpr(self) :
		ur"""An advanced string expression for generating the body of the request. The expression can contain a literal string or an expression that derives the value (for example, client.ip.src). Mutually exclusive with -fullReqExpr.<br/>Minimum length =  1.
		"""
		try :
			return self._bodyexpr
		except Exception as e:
			raise e

	@bodyexpr.setter
	def bodyexpr(self, bodyexpr) :
		ur"""An advanced string expression for generating the body of the request. The expression can contain a literal string or an expression that derives the value (for example, client.ip.src). Mutually exclusive with -fullReqExpr.<br/>Minimum length =  1
		"""
		try :
			self._bodyexpr = bodyexpr
		except Exception as e:
			raise e

	@property
	def fullreqexpr(self) :
		ur"""Exact HTTP request, in the form of a default syntax expression, which the NetScaler appliance sends to the callout agent. If you set this parameter, you must not include HTTP method, host expression, URL stem expression, headers, or parameters.
		The request expression is constrained by the feature for which the callout is used. For example, an HTTP.RES expression cannot be used in a request-time policy bank or in a TCP content switching policy bank.
		The NetScaler appliance does not check the validity of this request. You must manually validate the request.<br/>Minimum length =  1.
		"""
		try :
			return self._fullreqexpr
		except Exception as e:
			raise e

	@fullreqexpr.setter
	def fullreqexpr(self, fullreqexpr) :
		ur"""Exact HTTP request, in the form of a default syntax expression, which the NetScaler appliance sends to the callout agent. If you set this parameter, you must not include HTTP method, host expression, URL stem expression, headers, or parameters.
		The request expression is constrained by the feature for which the callout is used. For example, an HTTP.RES expression cannot be used in a request-time policy bank or in a TCP content switching policy bank.
		The NetScaler appliance does not check the validity of this request. You must manually validate the request.<br/>Minimum length =  1
		"""
		try :
			self._fullreqexpr = fullreqexpr
		except Exception as e:
			raise e

	@property
	def scheme(self) :
		ur"""Type of scheme for the callout server.<br/>Possible values = http, https.
		"""
		try :
			return self._scheme
		except Exception as e:
			raise e

	@scheme.setter
	def scheme(self, scheme) :
		ur"""Type of scheme for the callout server.<br/>Possible values = http, https
		"""
		try :
			self._scheme = scheme
		except Exception as e:
			raise e

	@property
	def resultexpr(self) :
		ur"""Expression that extracts the callout results from the response sent by the HTTP callout agent. Must be a response based expression, that is, it must begin with HTTP.RES. The operations in this expression must match the return type. For example, if you configure a return type of TEXT, the result expression must be a text based expression. If the return type is NUM, the result expression (resultExpr) must return a numeric value, as in the following example: http.res.body(10000).length.<br/>Minimum length =  1.
		"""
		try :
			return self._resultexpr
		except Exception as e:
			raise e

	@resultexpr.setter
	def resultexpr(self, resultexpr) :
		ur"""Expression that extracts the callout results from the response sent by the HTTP callout agent. Must be a response based expression, that is, it must begin with HTTP.RES. The operations in this expression must match the return type. For example, if you configure a return type of TEXT, the result expression must be a text based expression. If the return type is NUM, the result expression (resultExpr) must return a numeric value, as in the following example: http.res.body(10000).length.<br/>Minimum length =  1
		"""
		try :
			self._resultexpr = resultexpr
		except Exception as e:
			raise e

	@property
	def cacheforsecs(self) :
		ur"""Duration, in seconds, for which the callout response is cached. The cached responses are stored in an integrated caching content group named "calloutContentGroup". If no duration is configured, the callout responses will not be cached unless normal caching configuration is used to cache them. This parameter takes precedence over any normal caching configuration that would otherwise apply to these responses.
		Note that the calloutContentGroup definition may not be modified or removed nor may it be used with other cache policies.<br/>Minimum length =  1<br/>Maximum length =  31536000.
		"""
		try :
			return self._cacheforsecs
		except Exception as e:
			raise e

	@cacheforsecs.setter
	def cacheforsecs(self, cacheforsecs) :
		ur"""Duration, in seconds, for which the callout response is cached. The cached responses are stored in an integrated caching content group named "calloutContentGroup". If no duration is configured, the callout responses will not be cached unless normal caching configuration is used to cache them. This parameter takes precedence over any normal caching configuration that would otherwise apply to these responses.
		Note that the calloutContentGroup definition may not be modified or removed nor may it be used with other cache policies.<br/>Minimum length =  1<br/>Maximum length =  31536000
		"""
		try :
			self._cacheforsecs = cacheforsecs
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments to preserve information about this HTTP callout.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments to preserve information about this HTTP callout.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Total hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		ur"""Total undefs.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		ur"""The state of the service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def undefreason(self) :
		ur"""Reason for last undef.<br/>Possible values = Failed to add service, Vserver not found, Not a HTTP or SSL vserver, Generated callout request is invalid, Content-Length header not found in callout request, Not enough space to put Content-Length value, Config incomplete, Server is DOWN, Creating callout connection failed, No memory to generate callout request packets, No memory to create callout task, No memory to create callout async, Callout request expression undef, No callout response expression, Skipped callout response eval, Callout response pixl init undef, Callout response expression undef.
		"""
		try :
			return self._undefreason
		except Exception as e:
			raise e

	@property
	def recursivecallout(self) :
		ur"""Number of recursive callouts.
		"""
		try :
			return self._recursivecallout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policyhttpcallout_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policyhttpcallout
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
		ur""" Use this API to add policyhttpcallout.
		"""
		try :
			if type(resource) is not list :
				addresource = policyhttpcallout()
				addresource.name = resource.name
				addresource.ipaddress = resource.ipaddress
				addresource.port = resource.port
				addresource.vserver = resource.vserver
				addresource.returntype = resource.returntype
				addresource.httpmethod = resource.httpmethod
				addresource.hostexpr = resource.hostexpr
				addresource.urlstemexpr = resource.urlstemexpr
				addresource.headers = resource.headers
				addresource.parameters = resource.parameters
				addresource.bodyexpr = resource.bodyexpr
				addresource.fullreqexpr = resource.fullreqexpr
				addresource.scheme = resource.scheme
				addresource.resultexpr = resource.resultexpr
				addresource.cacheforsecs = resource.cacheforsecs
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ policyhttpcallout() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].port = resource[i].port
						addresources[i].vserver = resource[i].vserver
						addresources[i].returntype = resource[i].returntype
						addresources[i].httpmethod = resource[i].httpmethod
						addresources[i].hostexpr = resource[i].hostexpr
						addresources[i].urlstemexpr = resource[i].urlstemexpr
						addresources[i].headers = resource[i].headers
						addresources[i].parameters = resource[i].parameters
						addresources[i].bodyexpr = resource[i].bodyexpr
						addresources[i].fullreqexpr = resource[i].fullreqexpr
						addresources[i].scheme = resource[i].scheme
						addresources[i].resultexpr = resource[i].resultexpr
						addresources[i].cacheforsecs = resource[i].cacheforsecs
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete policyhttpcallout.
		"""
		try :
			if type(resource) is not list :
				deleteresource = policyhttpcallout()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ policyhttpcallout() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ policyhttpcallout() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update policyhttpcallout.
		"""
		try :
			if type(resource) is not list :
				updateresource = policyhttpcallout()
				updateresource.name = resource.name
				updateresource.ipaddress = resource.ipaddress
				updateresource.port = resource.port
				updateresource.vserver = resource.vserver
				updateresource.returntype = resource.returntype
				updateresource.httpmethod = resource.httpmethod
				updateresource.hostexpr = resource.hostexpr
				updateresource.urlstemexpr = resource.urlstemexpr
				updateresource.headers = resource.headers
				updateresource.parameters = resource.parameters
				updateresource.bodyexpr = resource.bodyexpr
				updateresource.fullreqexpr = resource.fullreqexpr
				updateresource.scheme = resource.scheme
				updateresource.resultexpr = resource.resultexpr
				updateresource.cacheforsecs = resource.cacheforsecs
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ policyhttpcallout() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipaddress = resource[i].ipaddress
						updateresources[i].port = resource[i].port
						updateresources[i].vserver = resource[i].vserver
						updateresources[i].returntype = resource[i].returntype
						updateresources[i].httpmethod = resource[i].httpmethod
						updateresources[i].hostexpr = resource[i].hostexpr
						updateresources[i].urlstemexpr = resource[i].urlstemexpr
						updateresources[i].headers = resource[i].headers
						updateresources[i].parameters = resource[i].parameters
						updateresources[i].bodyexpr = resource[i].bodyexpr
						updateresources[i].fullreqexpr = resource[i].fullreqexpr
						updateresources[i].scheme = resource[i].scheme
						updateresources[i].resultexpr = resource[i].resultexpr
						updateresources[i].cacheforsecs = resource[i].cacheforsecs
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of policyhttpcallout resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = policyhttpcallout()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ policyhttpcallout() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ policyhttpcallout() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the policyhttpcallout resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = policyhttpcallout()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = policyhttpcallout()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [policyhttpcallout() for _ in range(len(name))]
							obj = [policyhttpcallout() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = policyhttpcallout()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of policyhttpcallout resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policyhttpcallout()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the policyhttpcallout resources configured on NetScaler.
		"""
		try :
			obj = policyhttpcallout()
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
		ur""" Use this API to count filtered the set of policyhttpcallout resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policyhttpcallout()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Svrstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Scheme:
		http = "http"
		https = "https"

	class Httpmethod:
		GET = "GET"
		POST = "POST"

	class Returntype:
		BOOL = "BOOL"
		NUM = "NUM"
		TEXT = "TEXT"

	class Undefreason:
		Failed_to_add_service = "Failed to add service"
		Vserver_not_found = "Vserver not found"
		Not_a_HTTP_or_SSL_vserver = "Not a HTTP or SSL vserver"
		Generated_callout_request_is_invalid = "Generated callout request is invalid"
		Content_Length_header_not_found_in_callout_request = "Content-Length header not found in callout request"
		Not_enough_space_to_put_Content_Length_value = "Not enough space to put Content-Length value"
		Config_incomplete = "Config incomplete"
		Server_is_DOWN = "Server is DOWN"
		Creating_callout_connection_failed = "Creating callout connection failed"
		No_memory_to_generate_callout_request_packets = "No memory to generate callout request packets"
		No_memory_to_create_callout_task = "No memory to create callout task"
		No_memory_to_create_callout_async = "No memory to create callout async"
		Callout_request_expression_undef = "Callout request expression undef"
		No_callout_response_expression = "No callout response expression"
		Skipped_callout_response_eval = "Skipped callout response eval"
		Callout_response_pixl_init_undef = "Callout response pixl init undef"
		Callout_response_expression_undef = "Callout response expression undef"

class policyhttpcallout_response(base_response) :
	def __init__(self, length=1) :
		self.policyhttpcallout = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policyhttpcallout = [policyhttpcallout() for _ in range(length)]

