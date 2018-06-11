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

class sslvserver(base_resource) :
	""" Configuration for SSL virtual server resource. """
	def __init__(self) :
		self._vservername = ""
		self._cleartextport = 0
		self._dh = ""
		self._dhfile = ""
		self._dhcount = 0
		self._ersa = ""
		self._ersacount = 0
		self._sessreuse = ""
		self._sesstimeout = 0
		self._cipherredirect = ""
		self._cipherurl = ""
		self._sslv2redirect = ""
		self._sslv2url = ""
		self._clientauth = ""
		self._clientcert = ""
		self._sslredirect = ""
		self._redirectportrewrite = ""
		self._nonfipsciphers = ""
		self._ssl2 = ""
		self._ssl3 = ""
		self._tls1 = ""
		self._tls11 = ""
		self._tls12 = ""
		self._snienable = ""
		self._pushenctrigger = ""
		self._sendclosenotify = ""
		self._dtlsprofilename = ""
		self._sslprofile = ""
		self._cipherdetails = False
		self._crlcheck = ""
		self._service = 0
		self._servicename = ""
		self._ocspcheck = ""
		self._ca = False
		self._snicert = False
		self._skipcaname = False
		self._dtlsflag = False
		self.___count = 0

	@property
	def vservername(self) :
		ur"""Name of the SSL virtual server for which to set advanced configuration.<br/>Minimum length =  1.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		ur"""Name of the SSL virtual server for which to set advanced configuration.<br/>Minimum length =  1
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def cleartextport(self) :
		ur"""Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.<br/>Default value: 0.
		"""
		try :
			return self._cleartextport
		except Exception as e:
			raise e

	@cleartextport.setter
	def cleartextport(self, cleartextport) :
		ur"""Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.<br/>Default value: 0
		"""
		try :
			self._cleartextport = cleartextport
		except Exception as e:
			raise e

	@property
	def dh(self) :
		ur"""State of Diffie-Hellman (DH) key exchange.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dh
		except Exception as e:
			raise e

	@dh.setter
	def dh(self, dh) :
		ur"""State of Diffie-Hellman (DH) key exchange.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dh = dh
		except Exception as e:
			raise e

	@property
	def dhfile(self) :
		ur"""Name of and, optionally, path to the DH parameter file, in PEM format, to be installed. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._dhfile
		except Exception as e:
			raise e

	@dhfile.setter
	def dhfile(self, dhfile) :
		ur"""Name of and, optionally, path to the DH parameter file, in PEM format, to be installed. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._dhfile = dhfile
		except Exception as e:
			raise e

	@property
	def dhcount(self) :
		ur"""Number of interactions, between the client and the NetScaler appliance, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh).<br/>Maximum length =  65534.
		"""
		try :
			return self._dhcount
		except Exception as e:
			raise e

	@dhcount.setter
	def dhcount(self, dhcount) :
		ur"""Number of interactions, between the client and the NetScaler appliance, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh).<br/>Maximum length =  65534
		"""
		try :
			self._dhcount = dhcount
		except Exception as e:
			raise e

	@property
	def ersa(self) :
		ur"""State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ersa
		except Exception as e:
			raise e

	@ersa.setter
	def ersa(self, ersa) :
		ur"""State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ersa = ersa
		except Exception as e:
			raise e

	@property
	def ersacount(self) :
		ur"""Refresh count for regeneration of the RSA public-key and private-key pair. Zero (0) specifies infinite usage (no refresh).<br/>Maximum length =  65534.
		"""
		try :
			return self._ersacount
		except Exception as e:
			raise e

	@ersacount.setter
	def ersacount(self, ersacount) :
		ur"""Refresh count for regeneration of the RSA public-key and private-key pair. Zero (0) specifies infinite usage (no refresh).<br/>Maximum length =  65534
		"""
		try :
			self._ersacount = ersacount
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
		ur"""Time, in seconds, for which to keep the session active. Any session resumption request received after the timeout period will require a fresh SSL handshake and establishment of a new SSL session.<br/>Default value: 120<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._sesstimeout
		except Exception as e:
			raise e

	@sesstimeout.setter
	def sesstimeout(self, sesstimeout) :
		ur"""Time, in seconds, for which to keep the session active. Any session resumption request received after the timeout period will require a fresh SSL handshake and establishment of a new SSL session.<br/>Default value: 120<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._sesstimeout = sesstimeout
		except Exception as e:
			raise e

	@property
	def cipherredirect(self) :
		ur"""State of Cipher Redirect. If cipher redirect is enabled, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cipherredirect
		except Exception as e:
			raise e

	@cipherredirect.setter
	def cipherredirect(self, cipherredirect) :
		ur"""State of Cipher Redirect. If cipher redirect is enabled, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cipherredirect = cipherredirect
		except Exception as e:
			raise e

	@property
	def cipherurl(self) :
		ur"""The redirect URL to be used with the Cipher Redirect feature.
		"""
		try :
			return self._cipherurl
		except Exception as e:
			raise e

	@cipherurl.setter
	def cipherurl(self, cipherurl) :
		ur"""The redirect URL to be used with the Cipher Redirect feature.
		"""
		try :
			self._cipherurl = cipherurl
		except Exception as e:
			raise e

	@property
	def sslv2redirect(self) :
		ur"""State of SSLv2 Redirect. If SSLv2 redirect is enabled, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a protocol version mismatch between the virtual server or service and the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslv2redirect
		except Exception as e:
			raise e

	@sslv2redirect.setter
	def sslv2redirect(self, sslv2redirect) :
		ur"""State of SSLv2 Redirect. If SSLv2 redirect is enabled, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a protocol version mismatch between the virtual server or service and the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslv2redirect = sslv2redirect
		except Exception as e:
			raise e

	@property
	def sslv2url(self) :
		ur"""URL of the page to which to redirect the client in case of a protocol version mismatch. Typically, this page has a clear explanation of the error or an alternative location that the transaction can continue from.
		"""
		try :
			return self._sslv2url
		except Exception as e:
			raise e

	@sslv2url.setter
	def sslv2url(self, sslv2url) :
		ur"""URL of the page to which to redirect the client in case of a protocol version mismatch. Typically, this page has a clear explanation of the error or an alternative location that the transaction can continue from.
		"""
		try :
			self._sslv2url = sslv2url
		except Exception as e:
			raise e

	@property
	def clientauth(self) :
		ur"""State of client authentication. If client authentication is enabled, the virtual server terminates the SSL handshake if the SSL client does not provide a valid certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientauth
		except Exception as e:
			raise e

	@clientauth.setter
	def clientauth(self, clientauth) :
		ur"""State of client authentication. If client authentication is enabled, the virtual server terminates the SSL handshake if the SSL client does not provide a valid certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientauth = clientauth
		except Exception as e:
			raise e

	@property
	def clientcert(self) :
		ur"""Type of client authentication. If this parameter is set to MANDATORY, the appliance terminates the SSL handshake if the SSL client does not provide a valid certificate. With the OPTIONAL setting, the appliance requests a certificate from the SSL clients but proceeds with the SSL transaction even if the client presents an invalid certificate.
		Caution: Define proper access control policies before changing this setting to Optional.<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._clientcert
		except Exception as e:
			raise e

	@clientcert.setter
	def clientcert(self, clientcert) :
		ur"""Type of client authentication. If this parameter is set to MANDATORY, the appliance terminates the SSL handshake if the SSL client does not provide a valid certificate. With the OPTIONAL setting, the appliance requests a certificate from the SSL clients but proceeds with the SSL transaction even if the client presents an invalid certificate.
		Caution: Define proper access control policies before changing this setting to Optional.<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._clientcert = clientcert
		except Exception as e:
			raise e

	@property
	def sslredirect(self) :
		ur"""State of HTTPS redirects for the SSL virtual server. 
		For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
		If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslredirect
		except Exception as e:
			raise e

	@sslredirect.setter
	def sslredirect(self, sslredirect) :
		ur"""State of HTTPS redirects for the SSL virtual server. 
		For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
		If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslredirect = sslredirect
		except Exception as e:
			raise e

	@property
	def redirectportrewrite(self) :
		ur"""State of the port rewrite while performing HTTPS redirect. If this parameter is ENABLED and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._redirectportrewrite
		except Exception as e:
			raise e

	@redirectportrewrite.setter
	def redirectportrewrite(self, redirectportrewrite) :
		ur"""State of the port rewrite while performing HTTPS redirect. If this parameter is ENABLED and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._redirectportrewrite = redirectportrewrite
		except Exception as e:
			raise e

	@property
	def nonfipsciphers(self) :
		ur"""State of usage of non-FIPS approved ciphers. Valid only for an SSL service bound with a FIPS key and certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nonfipsciphers
		except Exception as e:
			raise e

	@nonfipsciphers.setter
	def nonfipsciphers(self, nonfipsciphers) :
		ur"""State of usage of non-FIPS approved ciphers. Valid only for an SSL service bound with a FIPS key and certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nonfipsciphers = nonfipsciphers
		except Exception as e:
			raise e

	@property
	def ssl2(self) :
		ur"""State of SSLv2 protocol support for the SSL Virtual Server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl2
		except Exception as e:
			raise e

	@ssl2.setter
	def ssl2(self, ssl2) :
		ur"""State of SSLv2 protocol support for the SSL Virtual Server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssl2 = ssl2
		except Exception as e:
			raise e

	@property
	def ssl3(self) :
		ur"""State of SSLv3 protocol support for the SSL Virtual Server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl3
		except Exception as e:
			raise e

	@ssl3.setter
	def ssl3(self, ssl3) :
		ur"""State of SSLv3 protocol support for the SSL Virtual Server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssl3 = ssl3
		except Exception as e:
			raise e

	@property
	def tls1(self) :
		ur"""State of TLSv1.0 protocol support for the SSL Virtual Server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls1
		except Exception as e:
			raise e

	@tls1.setter
	def tls1(self, tls1) :
		ur"""State of TLSv1.0 protocol support for the SSL Virtual Server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls1 = tls1
		except Exception as e:
			raise e

	@property
	def tls11(self) :
		ur"""State of TLSv1.1 protocol support for the SSL Virtual Server. TLSv1.1 protocol is supported only on the MPX appliance. Support is not available on a FIPS appliance or on a NetScaler VPX virtual appliance. On an SDX appliance, TLSv1.1 protocol is supported only if an SSL chip is assigned to the instance.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls11
		except Exception as e:
			raise e

	@tls11.setter
	def tls11(self, tls11) :
		ur"""State of TLSv1.1 protocol support for the SSL Virtual Server. TLSv1.1 protocol is supported only on the MPX appliance. Support is not available on a FIPS appliance or on a NetScaler VPX virtual appliance. On an SDX appliance, TLSv1.1 protocol is supported only if an SSL chip is assigned to the instance.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls11 = tls11
		except Exception as e:
			raise e

	@property
	def tls12(self) :
		ur"""State of TLSv1.2 protocol support for the SSL Virtual Server. TLSv1.2 protocol is supported only on the MPX appliance. Support is not available on a FIPS appliance or on a NetScaler VPX virtual appliance. On an SDX appliance, TLSv1.2 protocol is supported only if an SSL chip is assigned to the instance.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls12
		except Exception as e:
			raise e

	@tls12.setter
	def tls12(self, tls12) :
		ur"""State of TLSv1.2 protocol support for the SSL Virtual Server. TLSv1.2 protocol is supported only on the MPX appliance. Support is not available on a FIPS appliance or on a NetScaler VPX virtual appliance. On an SDX appliance, TLSv1.2 protocol is supported only if an SSL chip is assigned to the instance.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls12 = tls12
		except Exception as e:
			raise e

	@property
	def snienable(self) :
		ur"""State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snienable
		except Exception as e:
			raise e

	@snienable.setter
	def snienable(self, snienable) :
		ur"""State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snienable = snienable
		except Exception as e:
			raise e

	@property
	def pushenctrigger(self) :
		ur"""Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
		* ALWAYS - Any PUSH packet triggers encryption.
		* IGNORE - Ignore PUSH packet for triggering encryption.
		* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
		* TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer.
		"""
		try :
			return self._pushenctrigger
		except Exception as e:
			raise e

	@pushenctrigger.setter
	def pushenctrigger(self, pushenctrigger) :
		ur"""Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
		* ALWAYS - Any PUSH packet triggers encryption.
		* IGNORE - Ignore PUSH packet for triggering encryption.
		* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
		* TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer
		"""
		try :
			self._pushenctrigger = pushenctrigger
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
	def dtlsprofilename(self) :
		ur"""Name of the DTLS profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dtlsprofilename
		except Exception as e:
			raise e

	@dtlsprofilename.setter
	def dtlsprofilename(self, dtlsprofilename) :
		ur"""Name of the DTLS profile whose settings are to be applied to the virtual server.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dtlsprofilename = dtlsprofilename
		except Exception as e:
			raise e

	@property
	def sslprofile(self) :
		ur"""SSL profile associated to vserver.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._sslprofile
		except Exception as e:
			raise e

	@sslprofile.setter
	def sslprofile(self, sslprofile) :
		ur"""SSL profile associated to vserver.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._sslprofile = sslprofile
		except Exception as e:
			raise e

	@property
	def cipherdetails(self) :
		ur"""Display details of the individual ciphers bound to the SSL virtual server.
		"""
		try :
			return self._cipherdetails
		except Exception as e:
			raise e

	@cipherdetails.setter
	def cipherdetails(self, cipherdetails) :
		ur"""Display details of the individual ciphers bound to the SSL virtual server.
		"""
		try :
			self._cipherdetails = cipherdetails
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
	def service(self) :
		ur"""Service.
		"""
		try :
			return self._service
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""Service name.
		"""
		try :
			return self._servicename
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

	@property
	def skipcaname(self) :
		ur"""The flag is used to indicate whether this particular CA certificate's CA_Name needs to be sent to the SSL client while requesting for client certificate in a SSL handshake.
		"""
		try :
			return self._skipcaname
		except Exception as e:
			raise e

	@property
	def dtlsflag(self) :
		ur"""The flag is used to indicate whether DTLS is set or not.
		"""
		try :
			return self._dtlsflag
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslvserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.vservername is not None :
				return str(self.vservername)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update sslvserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslvserver()
				updateresource.vservername = resource.vservername
				updateresource.cleartextport = resource.cleartextport
				updateresource.dh = resource.dh
				updateresource.dhfile = resource.dhfile
				updateresource.dhcount = resource.dhcount
				updateresource.ersa = resource.ersa
				updateresource.ersacount = resource.ersacount
				updateresource.sessreuse = resource.sessreuse
				updateresource.sesstimeout = resource.sesstimeout
				updateresource.cipherredirect = resource.cipherredirect
				updateresource.cipherurl = resource.cipherurl
				updateresource.sslv2redirect = resource.sslv2redirect
				updateresource.sslv2url = resource.sslv2url
				updateresource.clientauth = resource.clientauth
				updateresource.clientcert = resource.clientcert
				updateresource.sslredirect = resource.sslredirect
				updateresource.redirectportrewrite = resource.redirectportrewrite
				updateresource.nonfipsciphers = resource.nonfipsciphers
				updateresource.ssl2 = resource.ssl2
				updateresource.ssl3 = resource.ssl3
				updateresource.tls1 = resource.tls1
				updateresource.tls11 = resource.tls11
				updateresource.tls12 = resource.tls12
				updateresource.snienable = resource.snienable
				updateresource.pushenctrigger = resource.pushenctrigger
				updateresource.sendclosenotify = resource.sendclosenotify
				updateresource.dtlsprofilename = resource.dtlsprofilename
				updateresource.sslprofile = resource.sslprofile
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].vservername = resource[i].vservername
						updateresources[i].cleartextport = resource[i].cleartextport
						updateresources[i].dh = resource[i].dh
						updateresources[i].dhfile = resource[i].dhfile
						updateresources[i].dhcount = resource[i].dhcount
						updateresources[i].ersa = resource[i].ersa
						updateresources[i].ersacount = resource[i].ersacount
						updateresources[i].sessreuse = resource[i].sessreuse
						updateresources[i].sesstimeout = resource[i].sesstimeout
						updateresources[i].cipherredirect = resource[i].cipherredirect
						updateresources[i].cipherurl = resource[i].cipherurl
						updateresources[i].sslv2redirect = resource[i].sslv2redirect
						updateresources[i].sslv2url = resource[i].sslv2url
						updateresources[i].clientauth = resource[i].clientauth
						updateresources[i].clientcert = resource[i].clientcert
						updateresources[i].sslredirect = resource[i].sslredirect
						updateresources[i].redirectportrewrite = resource[i].redirectportrewrite
						updateresources[i].nonfipsciphers = resource[i].nonfipsciphers
						updateresources[i].ssl2 = resource[i].ssl2
						updateresources[i].ssl3 = resource[i].ssl3
						updateresources[i].tls1 = resource[i].tls1
						updateresources[i].tls11 = resource[i].tls11
						updateresources[i].tls12 = resource[i].tls12
						updateresources[i].snienable = resource[i].snienable
						updateresources[i].pushenctrigger = resource[i].pushenctrigger
						updateresources[i].sendclosenotify = resource[i].sendclosenotify
						updateresources[i].dtlsprofilename = resource[i].dtlsprofilename
						updateresources[i].sslprofile = resource[i].sslprofile
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of sslvserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslvserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.vservername = resource
				else :
					unsetresource.vservername = resource.vservername
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].vservername = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].vservername = resource[i].vservername
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslvserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslvserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = sslvserver()
						obj.vservername = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [sslvserver() for _ in range(len(name))]
							obj = [sslvserver() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = sslvserver()
								obj[i].vservername = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the sslvserver resources that are configured on netscaler.
	# This uses sslvserver_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = sslvserver()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of sslvserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the sslvserver resources configured on NetScaler.
		"""
		try :
			obj = sslvserver()
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
		ur""" Use this API to count filtered the set of sslvserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver()
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

	class Tls11:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tls12:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nonfipsciphers:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Snienable:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cipherredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcert:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Pushenctrigger:
		Always = "Always"
		Merge = "Merge"
		Ignore = "Ignore"
		Timer = "Timer"

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

class sslvserver_response(base_response) :
	def __init__(self, length=1) :
		self.sslvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslvserver = [sslvserver() for _ in range(length)]

