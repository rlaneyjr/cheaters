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

class sslservicegroup(base_resource) :
	""" Configuration for SSL service group resource. """
	def __init__(self) :
		self._servicegroupname = ""
		self._sslprofile = ""
		self._sessreuse = ""
		self._sesstimeout = 0
		self._nonfipsciphers = ""
		self._ssl3 = ""
		self._tls1 = ""
		self._serverauth = ""
		self._commonname = ""
		self._sendclosenotify = ""
		self._cipherdetails = False
		self._dh = ""
		self._dhfile = ""
		self._dhcount = 0
		self._ersa = ""
		self._ersacount = 0
		self._cipherredirect = ""
		self._cipherurl = ""
		self._sslv2redirect = ""
		self._sslv2url = ""
		self._clientauth = ""
		self._clientcert = ""
		self._sslredirect = ""
		self._redirectportrewrite = ""
		self._ssl2 = ""
		self._ocspcheck = ""
		self._crlcheck = ""
		self._cleartextport = 0
		self._servicename = ""
		self._ca = False
		self._snicert = False
		self.___count = 0

	@property
	def servicegroupname(self) :
		ur"""Name of the SSL service group for which to set advanced configuration.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		ur"""Name of the SSL service group for which to set advanced configuration.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def sslprofile(self) :
		ur"""SSL Profile associated to serviceGroup.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._sslprofile
		except Exception as e:
			raise e

	@sslprofile.setter
	def sslprofile(self, sslprofile) :
		ur"""SSL Profile associated to serviceGroup.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._sslprofile = sslprofile
		except Exception as e:
			raise e

	@property
	def sessreuse(self) :
		ur"""State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessreuse
		except Exception as e:
			raise e

	@sessreuse.setter
	def sessreuse(self, sessreuse) :
		ur"""State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessreuse = sessreuse
		except Exception as e:
			raise e

	@property
	def sesstimeout(self) :
		ur"""Time, in seconds, for which to keep the session active. Any session resumption request received after the timeout period will require a fresh SSL handshake and establishment of a new SSL session.<br/>Default value: 300<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._sesstimeout
		except Exception as e:
			raise e

	@sesstimeout.setter
	def sesstimeout(self, sesstimeout) :
		ur"""Time, in seconds, for which to keep the session active. Any session resumption request received after the timeout period will require a fresh SSL handshake and establishment of a new SSL session.<br/>Default value: 300<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._sesstimeout = sesstimeout
		except Exception as e:
			raise e

	@property
	def nonfipsciphers(self) :
		ur"""State of usage of ciphers that are not FIPS approved. Valid only for an SSL service bound with a FIPS key and certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nonfipsciphers
		except Exception as e:
			raise e

	@nonfipsciphers.setter
	def nonfipsciphers(self, nonfipsciphers) :
		ur"""State of usage of ciphers that are not FIPS approved. Valid only for an SSL service bound with a FIPS key and certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nonfipsciphers = nonfipsciphers
		except Exception as e:
			raise e

	@property
	def ssl3(self) :
		ur"""State of SSLv3 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl3
		except Exception as e:
			raise e

	@ssl3.setter
	def ssl3(self, ssl3) :
		ur"""State of SSLv3 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssl3 = ssl3
		except Exception as e:
			raise e

	@property
	def tls1(self) :
		ur"""State of TLSv1.0 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls1
		except Exception as e:
			raise e

	@tls1.setter
	def tls1(self, tls1) :
		ur"""State of TLSv1.0 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls1 = tls1
		except Exception as e:
			raise e

	@property
	def serverauth(self) :
		ur"""State of server authentication support for the SSL service group.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._serverauth
		except Exception as e:
			raise e

	@serverauth.setter
	def serverauth(self, serverauth) :
		ur"""State of server authentication support for the SSL service group.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._serverauth = serverauth
		except Exception as e:
			raise e

	@property
	def commonname(self) :
		ur"""Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1.
		"""
		try :
			return self._commonname
		except Exception as e:
			raise e

	@commonname.setter
	def commonname(self, commonname) :
		ur"""Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1
		"""
		try :
			self._commonname = commonname
		except Exception as e:
			raise e

	@property
	def sendclosenotify(self) :
		ur"""Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._sendclosenotify
		except Exception as e:
			raise e

	@sendclosenotify.setter
	def sendclosenotify(self, sendclosenotify) :
		ur"""Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._sendclosenotify = sendclosenotify
		except Exception as e:
			raise e

	@property
	def cipherdetails(self) :
		ur"""Display details of the individual ciphers bound to the SSL service group.
		"""
		try :
			return self._cipherdetails
		except Exception as e:
			raise e

	@cipherdetails.setter
	def cipherdetails(self, cipherdetails) :
		ur"""Display details of the individual ciphers bound to the SSL service group.
		"""
		try :
			self._cipherdetails = cipherdetails
		except Exception as e:
			raise e

	@property
	def dh(self) :
		ur"""The state of DH key exchange support for the SSL service group.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dh
		except Exception as e:
			raise e

	@property
	def dhfile(self) :
		ur"""The  file name and path for the DH parameter.
		"""
		try :
			return self._dhfile
		except Exception as e:
			raise e

	@property
	def dhcount(self) :
		ur"""The  refresh  count  for  the re-generation of DH public-key and private-key from the DH parameter.
		"""
		try :
			return self._dhcount
		except Exception as e:
			raise e

	@property
	def ersa(self) :
		ur"""The state of Ephemeral RSA key exchange support for the SSL service group.Ephemeral RSA is used for export ciphers.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ersa
		except Exception as e:
			raise e

	@property
	def ersacount(self) :
		ur"""The  refresh  count  for the re-generation of RSA public-key and private-key pair.
		"""
		try :
			return self._ersacount
		except Exception as e:
			raise e

	@property
	def cipherredirect(self) :
		ur"""The state of Cipher Redirect feature. Cipher Redirect feature can be used to provide more readable information to SSL clients about mismatch in ciphers between the client and the SSL vserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cipherredirect
		except Exception as e:
			raise e

	@property
	def cipherurl(self) :
		ur"""The redirect URL to be used with the  Cipher  Redirect  feature.
		"""
		try :
			return self._cipherurl
		except Exception as e:
			raise e

	@property
	def sslv2redirect(self) :
		ur"""The state of SSLv2 Redirect feature.SSLv2 Redirect feature can be used to provide more readable information to SSL client about non-support of SSLv2 protocol on the SSL vserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslv2redirect
		except Exception as e:
			raise e

	@property
	def sslv2url(self) :
		ur"""The  redirect URL to be used with SSLv2 Redirect feature.
		"""
		try :
			return self._sslv2url
		except Exception as e:
			raise e

	@property
	def clientauth(self) :
		ur"""The state of Client-Authentication support for the SSL service group.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientauth
		except Exception as e:
			raise e

	@property
	def clientcert(self) :
		ur"""The rule for client certificate requirement in client authentication.<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._clientcert
		except Exception as e:
			raise e

	@property
	def sslredirect(self) :
		ur"""The state of HTTPS redirects for the SSL service group.
		This is required for the proper functioning of the redirect messages from the server. The redirect message from the server provides the new location for the moved object. This is contained in the HTTP header field: Location, e.g. Location: http://www.moved.org/here.html
		For the SSL session, if the client browser receives this message, the browser will try to connect to the new location. This will break the secure SSL session, as the object has moved from a secure site (https://) to an un-secure one (http://). Generally browsers flash a warning message on the screen and prompt the user, either to continue or disconnect.
		The above feature, when enabled will automatically convert all such http:// redirect message to https://. This will not break the client SSL session.
		Note: The set ssl service command can be used for configuring a front-end SSL service for service based SSL Off-Loading, or a backend SSL service for backend-encryption setup.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslredirect
		except Exception as e:
			raise e

	@property
	def redirectportrewrite(self) :
		ur"""The state of port-rewrite feature.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._redirectportrewrite
		except Exception as e:
			raise e

	@property
	def ssl2(self) :
		ur"""The  state of SSLv2 protocol support for the SSL service group.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl2
		except Exception as e:
			raise e

	@property
	def ocspcheck(self) :
		ur"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._ocspcheck
		except Exception as e:
			raise e

	@property
	def crlcheck(self) :
		ur"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@property
	def cleartextport(self) :
		ur"""The port on the back-end web-servers where the clear-text data is sent by system. Use this setting for the wildcard IP based SSL Acceleration configuration (*:443).<br/>Range 1 - 65535.
		"""
		try :
			return self._cleartextport
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""The service name.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def ca(self) :
		ur"""CA certificate.
		"""
		try :
			return self._ca
		except Exception as e:
			raise e

	@property
	def snicert(self) :
		ur"""The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing.
		"""
		try :
			return self._snicert
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslservicegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslservicegroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update sslservicegroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslservicegroup()
				updateresource.servicegroupname = resource.servicegroupname
				updateresource.sslprofile = resource.sslprofile
				updateresource.sessreuse = resource.sessreuse
				updateresource.sesstimeout = resource.sesstimeout
				updateresource.nonfipsciphers = resource.nonfipsciphers
				updateresource.ssl3 = resource.ssl3
				updateresource.tls1 = resource.tls1
				updateresource.serverauth = resource.serverauth
				updateresource.commonname = resource.commonname
				updateresource.sendclosenotify = resource.sendclosenotify
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslservicegroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicegroupname = resource[i].servicegroupname
						updateresources[i].sslprofile = resource[i].sslprofile
						updateresources[i].sessreuse = resource[i].sessreuse
						updateresources[i].sesstimeout = resource[i].sesstimeout
						updateresources[i].nonfipsciphers = resource[i].nonfipsciphers
						updateresources[i].ssl3 = resource[i].ssl3
						updateresources[i].tls1 = resource[i].tls1
						updateresources[i].serverauth = resource[i].serverauth
						updateresources[i].commonname = resource[i].commonname
						updateresources[i].sendclosenotify = resource[i].sendclosenotify
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of sslservicegroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslservicegroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.servicegroupname = resource
				else :
					unsetresource.servicegroupname = resource.servicegroupname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i].servicegroupname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslservicegroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslservicegroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = sslservicegroup()
						obj.servicegroupname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [sslservicegroup() for _ in range(len(name))]
							obj = [sslservicegroup() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = sslservicegroup()
								obj[i].servicegroupname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the sslservicegroup resources that are configured on netscaler.
	# This uses sslservicegroup_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = sslservicegroup()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of sslservicegroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the sslservicegroup resources configured on NetScaler.
		"""
		try :
			obj = sslservicegroup()
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
		ur""" Use this API to count filtered the set of sslservicegroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sslredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ersa:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Redirectportrewrite:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sessreuse:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssl3:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tls1:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslv2redirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sendclosenotify:
		YES = "YES"
		NO = "NO"

	class Dh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Serverauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nonfipsciphers:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cipherredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcert:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Clientauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssl2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

class sslservicegroup_response(base_response) :
	def __init__(self, length=1) :
		self.sslservicegroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslservicegroup = [sslservicegroup() for _ in range(length)]

