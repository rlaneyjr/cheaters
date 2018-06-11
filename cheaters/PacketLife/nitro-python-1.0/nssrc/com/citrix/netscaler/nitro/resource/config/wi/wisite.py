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

class wisite(base_resource) :
	""" Configuration for WI site resource. """
	def __init__(self) :
		self._sitepath = ""
		self._agurl = ""
		self._staurl = ""
		self._secondstaurl = ""
		self._sessionreliability = ""
		self._usetwotickets = ""
		self._authenticationpoint = ""
		self._agauthenticationmethod = ""
		self._wiauthenticationmethods = []
		self._defaultcustomtextlocale = ""
		self._websessiontimeout = 0
		self._defaultaccessmethod = ""
		self._logintitle = ""
		self._appwelcomemessage = ""
		self._welcomemessage = ""
		self._footertext = ""
		self._loginsysmessage = ""
		self._preloginbutton = ""
		self._preloginmessage = ""
		self._prelogintitle = ""
		self._domainselection = ""
		self._sitetype = ""
		self._userinterfacebranding = ""
		self._publishedresourcetype = ""
		self._kioskmode = ""
		self._showsearch = ""
		self._showrefresh = ""
		self._wiuserinterfacemodes = ""
		self._userinterfacelayouts = ""
		self._restrictdomains = ""
		self._logindomains = ""
		self._hidedomainfield = ""
		self.___count = 0

	@property
	def sitepath(self) :
		ur"""Path to the Web Interface site being created on the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  250.
		"""
		try :
			return self._sitepath
		except Exception as e:
			raise e

	@sitepath.setter
	def sitepath(self, sitepath) :
		ur"""Path to the Web Interface site being created on the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  250
		"""
		try :
			self._sitepath = sitepath
		except Exception as e:
			raise e

	@property
	def agurl(self) :
		ur"""URL of the Access Gateway.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._agurl
		except Exception as e:
			raise e

	@agurl.setter
	def agurl(self, agurl) :
		ur"""URL of the Access Gateway.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._agurl = agurl
		except Exception as e:
			raise e

	@property
	def staurl(self) :
		ur"""URL of the Secure Ticket Authority (STA) server.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._staurl
		except Exception as e:
			raise e

	@staurl.setter
	def staurl(self, staurl) :
		ur"""URL of the Secure Ticket Authority (STA) server.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._staurl = staurl
		except Exception as e:
			raise e

	@property
	def secondstaurl(self) :
		ur"""URL of the second Secure Ticket Authority (STA) server.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._secondstaurl
		except Exception as e:
			raise e

	@secondstaurl.setter
	def secondstaurl(self, secondstaurl) :
		ur"""URL of the second Secure Ticket Authority (STA) server.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._secondstaurl = secondstaurl
		except Exception as e:
			raise e

	@property
	def sessionreliability(self) :
		ur"""Enable session reliability through Access Gateway.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sessionreliability
		except Exception as e:
			raise e

	@sessionreliability.setter
	def sessionreliability(self, sessionreliability) :
		ur"""Enable session reliability through Access Gateway.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sessionreliability = sessionreliability
		except Exception as e:
			raise e

	@property
	def usetwotickets(self) :
		ur"""Request tickets issued by two separate Secure Ticket Authorities (STA) when a resource is accessed.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._usetwotickets
		except Exception as e:
			raise e

	@usetwotickets.setter
	def usetwotickets(self, usetwotickets) :
		ur"""Request tickets issued by two separate Secure Ticket Authorities (STA) when a resource is accessed.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._usetwotickets = usetwotickets
		except Exception as e:
			raise e

	@property
	def authenticationpoint(self) :
		ur"""Authentication point for the Web Interface site.<br/>Possible values = WebInterface, AccessGateway.
		"""
		try :
			return self._authenticationpoint
		except Exception as e:
			raise e

	@authenticationpoint.setter
	def authenticationpoint(self, authenticationpoint) :
		ur"""Authentication point for the Web Interface site.<br/>Possible values = WebInterface, AccessGateway
		"""
		try :
			self._authenticationpoint = authenticationpoint
		except Exception as e:
			raise e

	@property
	def agauthenticationmethod(self) :
		ur"""Method for authenticating a Web Interface site if you have specified Web Interface as the authentication point.
		Available settings function as follows:
		* Explicit - Users must provide a user name and password to log on to the Web Interface.
		* Anonymous - Users can log on to the Web Interface without providing a user name and password. They have access to resources published for anonymous users.<br/>Possible values = Explicit, SmartCard.
		"""
		try :
			return self._agauthenticationmethod
		except Exception as e:
			raise e

	@agauthenticationmethod.setter
	def agauthenticationmethod(self, agauthenticationmethod) :
		ur"""Method for authenticating a Web Interface site if you have specified Web Interface as the authentication point.
		Available settings function as follows:
		* Explicit - Users must provide a user name and password to log on to the Web Interface.
		* Anonymous - Users can log on to the Web Interface without providing a user name and password. They have access to resources published for anonymous users.<br/>Possible values = Explicit, SmartCard
		"""
		try :
			self._agauthenticationmethod = agauthenticationmethod
		except Exception as e:
			raise e

	@property
	def wiauthenticationmethods(self) :
		ur"""The method of authentication to be used at Web Interface.<br/>Default value: Explicit<br/>Possible values = Explicit, Anonymous.
		"""
		try :
			return self._wiauthenticationmethods
		except Exception as e:
			raise e

	@wiauthenticationmethods.setter
	def wiauthenticationmethods(self, wiauthenticationmethods) :
		ur"""The method of authentication to be used at Web Interface.<br/>Default value: Explicit<br/>Possible values = Explicit, Anonymous
		"""
		try :
			self._wiauthenticationmethods = wiauthenticationmethods
		except Exception as e:
			raise e

	@property
	def defaultcustomtextlocale(self) :
		ur"""Default language for the Web Interface site.<br/>Default value: English<br/>Possible values = German, English, Spanish, French, Japanese, Korean, Russian, Chinese_simplified, Chinese_traditional.
		"""
		try :
			return self._defaultcustomtextlocale
		except Exception as e:
			raise e

	@defaultcustomtextlocale.setter
	def defaultcustomtextlocale(self, defaultcustomtextlocale) :
		ur"""Default language for the Web Interface site.<br/>Default value: English<br/>Possible values = German, English, Spanish, French, Japanese, Korean, Russian, Chinese_simplified, Chinese_traditional
		"""
		try :
			self._defaultcustomtextlocale = defaultcustomtextlocale
		except Exception as e:
			raise e

	@property
	def websessiontimeout(self) :
		ur"""Time-out, in minutes, for idle Web Interface browser sessions. If a client's session is idle for a time that exceeds the time-out value, the NetScaler appliance terminates the connection.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._websessiontimeout
		except Exception as e:
			raise e

	@websessiontimeout.setter
	def websessiontimeout(self, websessiontimeout) :
		ur"""Time-out, in minutes, for idle Web Interface browser sessions. If a client's session is idle for a time that exceeds the time-out value, the NetScaler appliance terminates the connection.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._websessiontimeout = websessiontimeout
		except Exception as e:
			raise e

	@property
	def defaultaccessmethod(self) :
		ur"""Default access method for clients accessing the Web Interface site.
		Note: Before you configure an access method based on the client IP address, you must enable USIP mode on the Web Interface service to make the client's IP address available with the Web Interface.
		Depending on whether the Web Interface site is configured to use an HTTP or HTTPS virtual server or to use access gateway, you can send clients or access gateway the IP address, or the alternate address, of a XenApp or XenDesktop server. Or, you can send the IP address translated from a mapping entry, which defines mapping of an internal address and port to an external address and port.
		Note: In the NetScaler command line, mapping entries can be created by using the bind wi site command.<br/>Possible values = Direct, Alternate, Translated, GatewayDirect, GatewayAlternate, GatewayTranslated.
		"""
		try :
			return self._defaultaccessmethod
		except Exception as e:
			raise e

	@defaultaccessmethod.setter
	def defaultaccessmethod(self, defaultaccessmethod) :
		ur"""Default access method for clients accessing the Web Interface site.
		Note: Before you configure an access method based on the client IP address, you must enable USIP mode on the Web Interface service to make the client's IP address available with the Web Interface.
		Depending on whether the Web Interface site is configured to use an HTTP or HTTPS virtual server or to use access gateway, you can send clients or access gateway the IP address, or the alternate address, of a XenApp or XenDesktop server. Or, you can send the IP address translated from a mapping entry, which defines mapping of an internal address and port to an external address and port.
		Note: In the NetScaler command line, mapping entries can be created by using the bind wi site command.<br/>Possible values = Direct, Alternate, Translated, GatewayDirect, GatewayAlternate, GatewayTranslated
		"""
		try :
			self._defaultaccessmethod = defaultaccessmethod
		except Exception as e:
			raise e

	@property
	def logintitle(self) :
		ur"""A custom login page title for the Web Interface site.<br/>Default value: "Welcome to Web Interface on NetScaler"<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._logintitle
		except Exception as e:
			raise e

	@logintitle.setter
	def logintitle(self, logintitle) :
		ur"""A custom login page title for the Web Interface site.<br/>Default value: "Welcome to Web Interface on NetScaler"<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._logintitle = logintitle
		except Exception as e:
			raise e

	@property
	def appwelcomemessage(self) :
		ur"""Specifies localized text to appear at the top of the main content area of the Applications screen. LanguageCode is en, de, es, fr, ja, or any other supported language identifier.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._appwelcomemessage
		except Exception as e:
			raise e

	@appwelcomemessage.setter
	def appwelcomemessage(self, appwelcomemessage) :
		ur"""Specifies localized text to appear at the top of the main content area of the Applications screen. LanguageCode is en, de, es, fr, ja, or any other supported language identifier.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._appwelcomemessage = appwelcomemessage
		except Exception as e:
			raise e

	@property
	def welcomemessage(self) :
		ur"""Localized welcome message that appears on the welcome area of the login screen.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._welcomemessage
		except Exception as e:
			raise e

	@welcomemessage.setter
	def welcomemessage(self, welcomemessage) :
		ur"""Localized welcome message that appears on the welcome area of the login screen.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._welcomemessage = welcomemessage
		except Exception as e:
			raise e

	@property
	def footertext(self) :
		ur"""Localized text that appears in the footer area of all pages.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._footertext
		except Exception as e:
			raise e

	@footertext.setter
	def footertext(self, footertext) :
		ur"""Localized text that appears in the footer area of all pages.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._footertext = footertext
		except Exception as e:
			raise e

	@property
	def loginsysmessage(self) :
		ur"""Localized text that appears at the bottom of the main content area of the login screen.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._loginsysmessage
		except Exception as e:
			raise e

	@loginsysmessage.setter
	def loginsysmessage(self, loginsysmessage) :
		ur"""Localized text that appears at the bottom of the main content area of the login screen.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._loginsysmessage = loginsysmessage
		except Exception as e:
			raise e

	@property
	def preloginbutton(self) :
		ur"""Localized text that appears as the name of the pre-login message confirmation button.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._preloginbutton
		except Exception as e:
			raise e

	@preloginbutton.setter
	def preloginbutton(self, preloginbutton) :
		ur"""Localized text that appears as the name of the pre-login message confirmation button.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._preloginbutton = preloginbutton
		except Exception as e:
			raise e

	@property
	def preloginmessage(self) :
		ur"""Localized text that appears on the pre-login message page.<br/>Minimum length =  1<br/>Maximum length =  2048.
		"""
		try :
			return self._preloginmessage
		except Exception as e:
			raise e

	@preloginmessage.setter
	def preloginmessage(self, preloginmessage) :
		ur"""Localized text that appears on the pre-login message page.<br/>Minimum length =  1<br/>Maximum length =  2048
		"""
		try :
			self._preloginmessage = preloginmessage
		except Exception as e:
			raise e

	@property
	def prelogintitle(self) :
		ur"""Localized text that appears as the title of the pre-login message page.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._prelogintitle
		except Exception as e:
			raise e

	@prelogintitle.setter
	def prelogintitle(self, prelogintitle) :
		ur"""Localized text that appears as the title of the pre-login message page.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._prelogintitle = prelogintitle
		except Exception as e:
			raise e

	@property
	def domainselection(self) :
		ur"""Domain names listed on the login screen for explicit authentication.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._domainselection
		except Exception as e:
			raise e

	@domainselection.setter
	def domainselection(self, domainselection) :
		ur"""Domain names listed on the login screen for explicit authentication.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._domainselection = domainselection
		except Exception as e:
			raise e

	@property
	def sitetype(self) :
		ur"""Type of access to the Web Interface site. Available settings function as follows:
		* XenApp/XenDesktop web site - Configures the Web Interface site for access by a web browser.
		* XenApp/XenDesktop services site - Configures the Web Interface site for access by the XenApp plug-in.<br/>Default value: XenAppWeb<br/>Possible values = XenAppWeb, XenAppServices.
		"""
		try :
			return self._sitetype
		except Exception as e:
			raise e

	@sitetype.setter
	def sitetype(self, sitetype) :
		ur"""Type of access to the Web Interface site. Available settings function as follows:
		* XenApp/XenDesktop web site - Configures the Web Interface site for access by a web browser.
		* XenApp/XenDesktop services site - Configures the Web Interface site for access by the XenApp plug-in.<br/>Default value: XenAppWeb<br/>Possible values = XenAppWeb, XenAppServices
		"""
		try :
			self._sitetype = sitetype
		except Exception as e:
			raise e

	@property
	def userinterfacebranding(self) :
		ur"""Specifies whether the site is focused towards users accessing applications or desktops. Setting the parameter to Desktops changes the functionality of the site to improve the experience for XenDesktop users. Citrix recommends using this setting for any deployment that includes XenDesktop.<br/>Default value: Applications<br/>Possible values = Desktops, Applications.
		"""
		try :
			return self._userinterfacebranding
		except Exception as e:
			raise e

	@userinterfacebranding.setter
	def userinterfacebranding(self, userinterfacebranding) :
		ur"""Specifies whether the site is focused towards users accessing applications or desktops. Setting the parameter to Desktops changes the functionality of the site to improve the experience for XenDesktop users. Citrix recommends using this setting for any deployment that includes XenDesktop.<br/>Default value: Applications<br/>Possible values = Desktops, Applications
		"""
		try :
			self._userinterfacebranding = userinterfacebranding
		except Exception as e:
			raise e

	@property
	def publishedresourcetype(self) :
		ur"""Method for accessing the published XenApp and XenDesktop resources. 
		Available settings function as follows:
		* Online - Allows applications to be launched on the XenApp and XenDesktop servers. 
		* Offline - Allows streaming of applications to the client. 
		* DualMode - Allows both online and offline modes.<br/>Default value: Online<br/>Possible values = Online, Offline, DualMode.
		"""
		try :
			return self._publishedresourcetype
		except Exception as e:
			raise e

	@publishedresourcetype.setter
	def publishedresourcetype(self, publishedresourcetype) :
		ur"""Method for accessing the published XenApp and XenDesktop resources. 
		Available settings function as follows:
		* Online - Allows applications to be launched on the XenApp and XenDesktop servers. 
		* Offline - Allows streaming of applications to the client. 
		* DualMode - Allows both online and offline modes.<br/>Default value: Online<br/>Possible values = Online, Offline, DualMode
		"""
		try :
			self._publishedresourcetype = publishedresourcetype
		except Exception as e:
			raise e

	@property
	def kioskmode(self) :
		ur"""User settings do not persist from one session to another.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._kioskmode
		except Exception as e:
			raise e

	@kioskmode.setter
	def kioskmode(self, kioskmode) :
		ur"""User settings do not persist from one session to another.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._kioskmode = kioskmode
		except Exception as e:
			raise e

	@property
	def showsearch(self) :
		ur"""Enables search option on XenApp websites.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._showsearch
		except Exception as e:
			raise e

	@showsearch.setter
	def showsearch(self, showsearch) :
		ur"""Enables search option on XenApp websites.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._showsearch = showsearch
		except Exception as e:
			raise e

	@property
	def showrefresh(self) :
		ur"""Provides the Refresh button on the applications screen.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._showrefresh
		except Exception as e:
			raise e

	@showrefresh.setter
	def showrefresh(self, showrefresh) :
		ur"""Provides the Refresh button on the applications screen.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._showrefresh = showrefresh
		except Exception as e:
			raise e

	@property
	def wiuserinterfacemodes(self) :
		ur"""Appearance of the login screen.
		* Simple - Only the login fields for the selected authentication method are displayed.
		* Advanced - Displays the navigation bar, which provides access to the pre-login messages and preferences screens.<br/>Default value: SIMPLE<br/>Possible values = SIMPLE, ADVANCED.
		"""
		try :
			return self._wiuserinterfacemodes
		except Exception as e:
			raise e

	@wiuserinterfacemodes.setter
	def wiuserinterfacemodes(self, wiuserinterfacemodes) :
		ur"""Appearance of the login screen.
		* Simple - Only the login fields for the selected authentication method are displayed.
		* Advanced - Displays the navigation bar, which provides access to the pre-login messages and preferences screens.<br/>Default value: SIMPLE<br/>Possible values = SIMPLE, ADVANCED
		"""
		try :
			self._wiuserinterfacemodes = wiuserinterfacemodes
		except Exception as e:
			raise e

	@property
	def userinterfacelayouts(self) :
		ur"""Specifies whether or not to use the compact user interface.<br/>Default value: AUTO<br/>Possible values = AUTO, NORMAL, COMPACT.
		"""
		try :
			return self._userinterfacelayouts
		except Exception as e:
			raise e

	@userinterfacelayouts.setter
	def userinterfacelayouts(self, userinterfacelayouts) :
		ur"""Specifies whether or not to use the compact user interface.<br/>Default value: AUTO<br/>Possible values = AUTO, NORMAL, COMPACT
		"""
		try :
			self._userinterfacelayouts = userinterfacelayouts
		except Exception as e:
			raise e

	@property
	def restrictdomains(self) :
		ur"""The RestrictDomains setting is used to enable/disable domain restrictions. If domain restriction is enabled, the LoginDomains list is used for validating the login domain. It is applied to all the authentication methods except Anonymous for XenApp Web and XenApp Services sites.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._restrictdomains
		except Exception as e:
			raise e

	@restrictdomains.setter
	def restrictdomains(self, restrictdomains) :
		ur"""The RestrictDomains setting is used to enable/disable domain restrictions. If domain restriction is enabled, the LoginDomains list is used for validating the login domain. It is applied to all the authentication methods except Anonymous for XenApp Web and XenApp Services sites.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._restrictdomains = restrictdomains
		except Exception as e:
			raise e

	@property
	def logindomains(self) :
		ur"""[List of NetBIOS domain names], Domain names to use for access restriction.
		Only takes effect when used in conjunction with the RestrictDomains setting.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._logindomains
		except Exception as e:
			raise e

	@logindomains.setter
	def logindomains(self, logindomains) :
		ur"""[List of NetBIOS domain names], Domain names to use for access restriction.
		Only takes effect when used in conjunction with the RestrictDomains setting.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._logindomains = logindomains
		except Exception as e:
			raise e

	@property
	def hidedomainfield(self) :
		ur"""The HideDomainField setting is used to control whether the domain field is displayed on the logon screen.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._hidedomainfield
		except Exception as e:
			raise e

	@hidedomainfield.setter
	def hidedomainfield(self, hidedomainfield) :
		ur"""The HideDomainField setting is used to control whether the domain field is displayed on the logon screen.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._hidedomainfield = hidedomainfield
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wisite_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wisite
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sitepath is not None :
				return str(self.sitepath)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add wisite.
		"""
		try :
			if type(resource) is not list :
				addresource = wisite()
				addresource.sitepath = resource.sitepath
				addresource.agurl = resource.agurl
				addresource.staurl = resource.staurl
				addresource.secondstaurl = resource.secondstaurl
				addresource.sessionreliability = resource.sessionreliability
				addresource.usetwotickets = resource.usetwotickets
				addresource.authenticationpoint = resource.authenticationpoint
				addresource.agauthenticationmethod = resource.agauthenticationmethod
				addresource.wiauthenticationmethods = resource.wiauthenticationmethods
				addresource.defaultcustomtextlocale = resource.defaultcustomtextlocale
				addresource.websessiontimeout = resource.websessiontimeout
				addresource.defaultaccessmethod = resource.defaultaccessmethod
				addresource.logintitle = resource.logintitle
				addresource.appwelcomemessage = resource.appwelcomemessage
				addresource.welcomemessage = resource.welcomemessage
				addresource.footertext = resource.footertext
				addresource.loginsysmessage = resource.loginsysmessage
				addresource.preloginbutton = resource.preloginbutton
				addresource.preloginmessage = resource.preloginmessage
				addresource.prelogintitle = resource.prelogintitle
				addresource.domainselection = resource.domainselection
				addresource.sitetype = resource.sitetype
				addresource.userinterfacebranding = resource.userinterfacebranding
				addresource.publishedresourcetype = resource.publishedresourcetype
				addresource.kioskmode = resource.kioskmode
				addresource.showsearch = resource.showsearch
				addresource.showrefresh = resource.showrefresh
				addresource.wiuserinterfacemodes = resource.wiuserinterfacemodes
				addresource.userinterfacelayouts = resource.userinterfacelayouts
				addresource.restrictdomains = resource.restrictdomains
				addresource.logindomains = resource.logindomains
				addresource.hidedomainfield = resource.hidedomainfield
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ wisite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].sitepath = resource[i].sitepath
						addresources[i].agurl = resource[i].agurl
						addresources[i].staurl = resource[i].staurl
						addresources[i].secondstaurl = resource[i].secondstaurl
						addresources[i].sessionreliability = resource[i].sessionreliability
						addresources[i].usetwotickets = resource[i].usetwotickets
						addresources[i].authenticationpoint = resource[i].authenticationpoint
						addresources[i].agauthenticationmethod = resource[i].agauthenticationmethod
						addresources[i].wiauthenticationmethods = resource[i].wiauthenticationmethods
						addresources[i].defaultcustomtextlocale = resource[i].defaultcustomtextlocale
						addresources[i].websessiontimeout = resource[i].websessiontimeout
						addresources[i].defaultaccessmethod = resource[i].defaultaccessmethod
						addresources[i].logintitle = resource[i].logintitle
						addresources[i].appwelcomemessage = resource[i].appwelcomemessage
						addresources[i].welcomemessage = resource[i].welcomemessage
						addresources[i].footertext = resource[i].footertext
						addresources[i].loginsysmessage = resource[i].loginsysmessage
						addresources[i].preloginbutton = resource[i].preloginbutton
						addresources[i].preloginmessage = resource[i].preloginmessage
						addresources[i].prelogintitle = resource[i].prelogintitle
						addresources[i].domainselection = resource[i].domainselection
						addresources[i].sitetype = resource[i].sitetype
						addresources[i].userinterfacebranding = resource[i].userinterfacebranding
						addresources[i].publishedresourcetype = resource[i].publishedresourcetype
						addresources[i].kioskmode = resource[i].kioskmode
						addresources[i].showsearch = resource[i].showsearch
						addresources[i].showrefresh = resource[i].showrefresh
						addresources[i].wiuserinterfacemodes = resource[i].wiuserinterfacemodes
						addresources[i].userinterfacelayouts = resource[i].userinterfacelayouts
						addresources[i].restrictdomains = resource[i].restrictdomains
						addresources[i].logindomains = resource[i].logindomains
						addresources[i].hidedomainfield = resource[i].hidedomainfield
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete wisite.
		"""
		try :
			if type(resource) is not list :
				deleteresource = wisite()
				if type(resource) !=  type(deleteresource):
					deleteresource.sitepath = resource
				else :
					deleteresource.sitepath = resource.sitepath
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ wisite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitepath = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ wisite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitepath = resource[i].sitepath
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update wisite.
		"""
		try :
			if type(resource) is not list :
				updateresource = wisite()
				updateresource.sitepath = resource.sitepath
				updateresource.agurl = resource.agurl
				updateresource.staurl = resource.staurl
				updateresource.sessionreliability = resource.sessionreliability
				updateresource.usetwotickets = resource.usetwotickets
				updateresource.secondstaurl = resource.secondstaurl
				updateresource.wiauthenticationmethods = resource.wiauthenticationmethods
				updateresource.defaultaccessmethod = resource.defaultaccessmethod
				updateresource.defaultcustomtextlocale = resource.defaultcustomtextlocale
				updateresource.websessiontimeout = resource.websessiontimeout
				updateresource.logintitle = resource.logintitle
				updateresource.appwelcomemessage = resource.appwelcomemessage
				updateresource.welcomemessage = resource.welcomemessage
				updateresource.footertext = resource.footertext
				updateresource.loginsysmessage = resource.loginsysmessage
				updateresource.preloginbutton = resource.preloginbutton
				updateresource.preloginmessage = resource.preloginmessage
				updateresource.prelogintitle = resource.prelogintitle
				updateresource.domainselection = resource.domainselection
				updateresource.userinterfacebranding = resource.userinterfacebranding
				updateresource.authenticationpoint = resource.authenticationpoint
				updateresource.agauthenticationmethod = resource.agauthenticationmethod
				updateresource.publishedresourcetype = resource.publishedresourcetype
				updateresource.kioskmode = resource.kioskmode
				updateresource.showsearch = resource.showsearch
				updateresource.showrefresh = resource.showrefresh
				updateresource.wiuserinterfacemodes = resource.wiuserinterfacemodes
				updateresource.userinterfacelayouts = resource.userinterfacelayouts
				updateresource.restrictdomains = resource.restrictdomains
				updateresource.logindomains = resource.logindomains
				updateresource.hidedomainfield = resource.hidedomainfield
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ wisite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].sitepath = resource[i].sitepath
						updateresources[i].agurl = resource[i].agurl
						updateresources[i].staurl = resource[i].staurl
						updateresources[i].sessionreliability = resource[i].sessionreliability
						updateresources[i].usetwotickets = resource[i].usetwotickets
						updateresources[i].secondstaurl = resource[i].secondstaurl
						updateresources[i].wiauthenticationmethods = resource[i].wiauthenticationmethods
						updateresources[i].defaultaccessmethod = resource[i].defaultaccessmethod
						updateresources[i].defaultcustomtextlocale = resource[i].defaultcustomtextlocale
						updateresources[i].websessiontimeout = resource[i].websessiontimeout
						updateresources[i].logintitle = resource[i].logintitle
						updateresources[i].appwelcomemessage = resource[i].appwelcomemessage
						updateresources[i].welcomemessage = resource[i].welcomemessage
						updateresources[i].footertext = resource[i].footertext
						updateresources[i].loginsysmessage = resource[i].loginsysmessage
						updateresources[i].preloginbutton = resource[i].preloginbutton
						updateresources[i].preloginmessage = resource[i].preloginmessage
						updateresources[i].prelogintitle = resource[i].prelogintitle
						updateresources[i].domainselection = resource[i].domainselection
						updateresources[i].userinterfacebranding = resource[i].userinterfacebranding
						updateresources[i].authenticationpoint = resource[i].authenticationpoint
						updateresources[i].agauthenticationmethod = resource[i].agauthenticationmethod
						updateresources[i].publishedresourcetype = resource[i].publishedresourcetype
						updateresources[i].kioskmode = resource[i].kioskmode
						updateresources[i].showsearch = resource[i].showsearch
						updateresources[i].showrefresh = resource[i].showrefresh
						updateresources[i].wiuserinterfacemodes = resource[i].wiuserinterfacemodes
						updateresources[i].userinterfacelayouts = resource[i].userinterfacelayouts
						updateresources[i].restrictdomains = resource[i].restrictdomains
						updateresources[i].logindomains = resource[i].logindomains
						updateresources[i].hidedomainfield = resource[i].hidedomainfield
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of wisite resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = wisite()
				if type(resource) !=  type(unsetresource):
					unsetresource.sitepath = resource
				else :
					unsetresource.sitepath = resource.sitepath
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ wisite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sitepath = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ wisite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sitepath = resource[i].sitepath
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the wisite resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = wisite()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = wisite()
						obj.sitepath = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [wisite() for _ in range(len(name))]
							obj = [wisite() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = wisite()
								obj[i].sitepath = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of wisite resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the wisite resources configured on NetScaler.
		"""
		try :
			obj = wisite()
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
		ur""" Use this API to count filtered the set of wisite resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sessionreliability:
		ON = "ON"
		OFF = "OFF"

	class Showsearch:
		ON = "ON"
		OFF = "OFF"

	class Showrefresh:
		ON = "ON"
		OFF = "OFF"

	class Userinterfacelayouts:
		AUTO = "AUTO"
		NORMAL = "NORMAL"
		COMPACT = "COMPACT"

	class Wiauthenticationmethods:
		Explicit = "Explicit"
		Anonymous = "Anonymous"

	class Defaultaccessmethod:
		Direct = "Direct"
		Alternate = "Alternate"
		Translated = "Translated"
		GatewayDirect = "GatewayDirect"
		GatewayAlternate = "GatewayAlternate"
		GatewayTranslated = "GatewayTranslated"

	class Wiuserinterfacemodes:
		SIMPLE = "SIMPLE"
		ADVANCED = "ADVANCED"

	class Publishedresourcetype:
		Online = "Online"
		Offline = "Offline"
		DualMode = "DualMode"

	class Usetwotickets:
		ON = "ON"
		OFF = "OFF"

	class Agauthenticationmethod:
		Explicit = "Explicit"
		SmartCard = "SmartCard"

	class Hidedomainfield:
		ON = "ON"
		OFF = "OFF"

	class Authenticationpoint:
		WebInterface = "WebInterface"
		AccessGateway = "AccessGateway"

	class Restrictdomains:
		ON = "ON"
		OFF = "OFF"

	class Sitetype:
		XenAppWeb = "XenAppWeb"
		XenAppServices = "XenAppServices"

	class Userinterfacebranding:
		Desktops = "Desktops"
		Applications = "Applications"

	class Defaultcustomtextlocale:
		German = "German"
		English = "English"
		Spanish = "Spanish"
		French = "French"
		Japanese = "Japanese"
		Korean = "Korean"
		Russian = "Russian"
		Chinese_simplified = "Chinese_simplified"
		Chinese_traditional = "Chinese_traditional"

	class Kioskmode:
		ON = "ON"
		OFF = "OFF"

class wisite_response(base_response) :
	def __init__(self, length=1) :
		self.wisite = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wisite = [wisite() for _ in range(length)]

