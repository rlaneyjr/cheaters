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

class vpnsamlssoprofile(base_resource) :
	""" Configuration for SAML sso action resource. """
	def __init__(self) :
		self._name = ""
		self._samlsigningcertname = ""
		self._assertionconsumerserviceurl = ""
		self._relaystaterule = ""
		self._sendpassword = ""
		self._samlissuername = ""
		self._signaturealg = ""
		self._digestmethod = ""
		self._audience = ""
		self._nameidformat = ""
		self._nameidexpr = ""
		self._attribute1 = ""
		self._attribute1expr = ""
		self._attribute1friendlyname = ""
		self._attribute1format = ""
		self._attribute2 = ""
		self._attribute2expr = ""
		self._attribute2friendlyname = ""
		self._attribute2format = ""
		self._attribute3 = ""
		self._attribute3expr = ""
		self._attribute3friendlyname = ""
		self._attribute3format = ""
		self._attribute4 = ""
		self._attribute4expr = ""
		self._attribute4friendlyname = ""
		self._attribute4format = ""
		self._attribute5 = ""
		self._attribute5expr = ""
		self._attribute5friendlyname = ""
		self._attribute5format = ""
		self._attribute6 = ""
		self._attribute6expr = ""
		self._attribute6friendlyname = ""
		self._attribute6format = ""
		self._attribute7 = ""
		self._attribute7expr = ""
		self._attribute7friendlyname = ""
		self._attribute7format = ""
		self._attribute8 = ""
		self._attribute8expr = ""
		self._attribute8friendlyname = ""
		self._attribute8format = ""
		self._attribute9 = ""
		self._attribute9expr = ""
		self._attribute9friendlyname = ""
		self._attribute9format = ""
		self._attribute10 = ""
		self._attribute10expr = ""
		self._attribute10friendlyname = ""
		self._attribute10format = ""
		self._attribute11 = ""
		self._attribute11expr = ""
		self._attribute11friendlyname = ""
		self._attribute11format = ""
		self._attribute12 = ""
		self._attribute12expr = ""
		self._attribute12friendlyname = ""
		self._attribute12format = ""
		self._attribute13 = ""
		self._attribute13expr = ""
		self._attribute13friendlyname = ""
		self._attribute13format = ""
		self._attribute14 = ""
		self._attribute14expr = ""
		self._attribute14friendlyname = ""
		self._attribute14format = ""
		self._attribute15 = ""
		self._attribute15expr = ""
		self._attribute15friendlyname = ""
		self._attribute15format = ""
		self._attribute16 = ""
		self._attribute16expr = ""
		self._attribute16friendlyname = ""
		self._attribute16format = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the new saml single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an SSO action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the new saml single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an SSO action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def samlsigningcertname(self) :
		ur"""Name of the signing authority as given in the SAML server's SSL certificate.<br/>Minimum length =  1.
		"""
		try :
			return self._samlsigningcertname
		except Exception as e:
			raise e

	@samlsigningcertname.setter
	def samlsigningcertname(self, samlsigningcertname) :
		ur"""Name of the signing authority as given in the SAML server's SSL certificate.<br/>Minimum length =  1
		"""
		try :
			self._samlsigningcertname = samlsigningcertname
		except Exception as e:
			raise e

	@property
	def assertionconsumerserviceurl(self) :
		ur"""URL to which the assertion is to be sent.<br/>Minimum length =  1.
		"""
		try :
			return self._assertionconsumerserviceurl
		except Exception as e:
			raise e

	@assertionconsumerserviceurl.setter
	def assertionconsumerserviceurl(self, assertionconsumerserviceurl) :
		ur"""URL to which the assertion is to be sent.<br/>Minimum length =  1
		"""
		try :
			self._assertionconsumerserviceurl = assertionconsumerserviceurl
		except Exception as e:
			raise e

	@property
	def relaystaterule(self) :
		ur"""Expression to extract relaystate to be sent along with assertion. Evaluation of this expression should return TEXT content. This is typically a target url to which user is redirected after the recipient validates SAML token.
		"""
		try :
			return self._relaystaterule
		except Exception as e:
			raise e

	@relaystaterule.setter
	def relaystaterule(self, relaystaterule) :
		ur"""Expression to extract relaystate to be sent along with assertion. Evaluation of this expression should return TEXT content. This is typically a target url to which user is redirected after the recipient validates SAML token.
		"""
		try :
			self._relaystaterule = relaystaterule
		except Exception as e:
			raise e

	@property
	def sendpassword(self) :
		ur"""Option to send password in assertion.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sendpassword
		except Exception as e:
			raise e

	@sendpassword.setter
	def sendpassword(self, sendpassword) :
		ur"""Option to send password in assertion.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sendpassword = sendpassword
		except Exception as e:
			raise e

	@property
	def samlissuername(self) :
		ur"""The name to be used in requests sent from	Netscaler to IdP to uniquely identify Netscaler.<br/>Minimum length =  1.
		"""
		try :
			return self._samlissuername
		except Exception as e:
			raise e

	@samlissuername.setter
	def samlissuername(self, samlissuername) :
		ur"""The name to be used in requests sent from	Netscaler to IdP to uniquely identify Netscaler.<br/>Minimum length =  1
		"""
		try :
			self._samlissuername = samlissuername
		except Exception as e:
			raise e

	@property
	def signaturealg(self) :
		ur"""Algorithm to be used to sign/verify SAML transactions.<br/>Default value: RSA-SHA1<br/>Possible values = RSA-SHA1, RSA-SHA256.
		"""
		try :
			return self._signaturealg
		except Exception as e:
			raise e

	@signaturealg.setter
	def signaturealg(self, signaturealg) :
		ur"""Algorithm to be used to sign/verify SAML transactions.<br/>Default value: RSA-SHA1<br/>Possible values = RSA-SHA1, RSA-SHA256
		"""
		try :
			self._signaturealg = signaturealg
		except Exception as e:
			raise e

	@property
	def digestmethod(self) :
		ur"""Algorithm to be used to compute/verify digest for SAML transactions.<br/>Default value: SHA1<br/>Possible values = SHA1, SHA256.
		"""
		try :
			return self._digestmethod
		except Exception as e:
			raise e

	@digestmethod.setter
	def digestmethod(self, digestmethod) :
		ur"""Algorithm to be used to compute/verify digest for SAML transactions.<br/>Default value: SHA1<br/>Possible values = SHA1, SHA256
		"""
		try :
			self._digestmethod = digestmethod
		except Exception as e:
			raise e

	@property
	def audience(self) :
		ur"""Audience for which assertion sent by IdP is applicable. This is typically entity name or url that represents ServiceProvider.<br/>Maximum length =  256.
		"""
		try :
			return self._audience
		except Exception as e:
			raise e

	@audience.setter
	def audience(self, audience) :
		ur"""Audience for which assertion sent by IdP is applicable. This is typically entity name or url that represents ServiceProvider.<br/>Maximum length =  256
		"""
		try :
			self._audience = audience
		except Exception as e:
			raise e

	@property
	def nameidformat(self) :
		ur"""Format of Name Identifier sent in Assertion.<br/>Default value: transient<br/>Possible values = Unspecified, emailAddress, X509SubjectName, WindowsDomainQualifiedName, kerberos, entity, persistent, transient.
		"""
		try :
			return self._nameidformat
		except Exception as e:
			raise e

	@nameidformat.setter
	def nameidformat(self, nameidformat) :
		ur"""Format of Name Identifier sent in Assertion.<br/>Default value: transient<br/>Possible values = Unspecified, emailAddress, X509SubjectName, WindowsDomainQualifiedName, kerberos, entity, persistent, transient
		"""
		try :
			self._nameidformat = nameidformat
		except Exception as e:
			raise e

	@property
	def nameidexpr(self) :
		ur"""Expression that will be evaluated to obtain NameIdentifier to be sent in assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._nameidexpr
		except Exception as e:
			raise e

	@nameidexpr.setter
	def nameidexpr(self, nameidexpr) :
		ur"""Expression that will be evaluated to obtain NameIdentifier to be sent in assertion.<br/>Maximum length =  128
		"""
		try :
			self._nameidexpr = nameidexpr
		except Exception as e:
			raise e

	@property
	def attribute1(self) :
		ur"""Name of attribute1 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute1
		except Exception as e:
			raise e

	@attribute1.setter
	def attribute1(self, attribute1) :
		ur"""Name of attribute1 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute1 = attribute1
		except Exception as e:
			raise e

	@property
	def attribute1expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute1expr
		except Exception as e:
			raise e

	@attribute1expr.setter
	def attribute1expr(self, attribute1expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute1expr = attribute1expr
		except Exception as e:
			raise e

	@property
	def attribute1friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute1friendlyname
		except Exception as e:
			raise e

	@attribute1friendlyname.setter
	def attribute1friendlyname(self, attribute1friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute1friendlyname = attribute1friendlyname
		except Exception as e:
			raise e

	@property
	def attribute1format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute1format
		except Exception as e:
			raise e

	@attribute1format.setter
	def attribute1format(self, attribute1format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute1format = attribute1format
		except Exception as e:
			raise e

	@property
	def attribute2(self) :
		ur"""Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute2
		except Exception as e:
			raise e

	@attribute2.setter
	def attribute2(self, attribute2) :
		ur"""Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute2 = attribute2
		except Exception as e:
			raise e

	@property
	def attribute2expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute2expr
		except Exception as e:
			raise e

	@attribute2expr.setter
	def attribute2expr(self, attribute2expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute2expr = attribute2expr
		except Exception as e:
			raise e

	@property
	def attribute2friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute2friendlyname
		except Exception as e:
			raise e

	@attribute2friendlyname.setter
	def attribute2friendlyname(self, attribute2friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute2friendlyname = attribute2friendlyname
		except Exception as e:
			raise e

	@property
	def attribute2format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute2format
		except Exception as e:
			raise e

	@attribute2format.setter
	def attribute2format(self, attribute2format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute2format = attribute2format
		except Exception as e:
			raise e

	@property
	def attribute3(self) :
		ur"""Name of attribute3 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute3
		except Exception as e:
			raise e

	@attribute3.setter
	def attribute3(self, attribute3) :
		ur"""Name of attribute3 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute3 = attribute3
		except Exception as e:
			raise e

	@property
	def attribute3expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute3expr
		except Exception as e:
			raise e

	@attribute3expr.setter
	def attribute3expr(self, attribute3expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute3expr = attribute3expr
		except Exception as e:
			raise e

	@property
	def attribute3friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute3friendlyname
		except Exception as e:
			raise e

	@attribute3friendlyname.setter
	def attribute3friendlyname(self, attribute3friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute3friendlyname = attribute3friendlyname
		except Exception as e:
			raise e

	@property
	def attribute3format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute3format
		except Exception as e:
			raise e

	@attribute3format.setter
	def attribute3format(self, attribute3format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute3format = attribute3format
		except Exception as e:
			raise e

	@property
	def attribute4(self) :
		ur"""Name of attribute4 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute4
		except Exception as e:
			raise e

	@attribute4.setter
	def attribute4(self, attribute4) :
		ur"""Name of attribute4 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute4 = attribute4
		except Exception as e:
			raise e

	@property
	def attribute4expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute4expr
		except Exception as e:
			raise e

	@attribute4expr.setter
	def attribute4expr(self, attribute4expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute4expr = attribute4expr
		except Exception as e:
			raise e

	@property
	def attribute4friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute4friendlyname
		except Exception as e:
			raise e

	@attribute4friendlyname.setter
	def attribute4friendlyname(self, attribute4friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute4friendlyname = attribute4friendlyname
		except Exception as e:
			raise e

	@property
	def attribute4format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute4format
		except Exception as e:
			raise e

	@attribute4format.setter
	def attribute4format(self, attribute4format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute4format = attribute4format
		except Exception as e:
			raise e

	@property
	def attribute5(self) :
		ur"""Name of attribute5 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute5
		except Exception as e:
			raise e

	@attribute5.setter
	def attribute5(self, attribute5) :
		ur"""Name of attribute5 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute5 = attribute5
		except Exception as e:
			raise e

	@property
	def attribute5expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute5expr
		except Exception as e:
			raise e

	@attribute5expr.setter
	def attribute5expr(self, attribute5expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute5expr = attribute5expr
		except Exception as e:
			raise e

	@property
	def attribute5friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute5friendlyname
		except Exception as e:
			raise e

	@attribute5friendlyname.setter
	def attribute5friendlyname(self, attribute5friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute5friendlyname = attribute5friendlyname
		except Exception as e:
			raise e

	@property
	def attribute5format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute5format
		except Exception as e:
			raise e

	@attribute5format.setter
	def attribute5format(self, attribute5format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute5format = attribute5format
		except Exception as e:
			raise e

	@property
	def attribute6(self) :
		ur"""Name of attribute6 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute6
		except Exception as e:
			raise e

	@attribute6.setter
	def attribute6(self, attribute6) :
		ur"""Name of attribute6 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute6 = attribute6
		except Exception as e:
			raise e

	@property
	def attribute6expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute6expr
		except Exception as e:
			raise e

	@attribute6expr.setter
	def attribute6expr(self, attribute6expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute6expr = attribute6expr
		except Exception as e:
			raise e

	@property
	def attribute6friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute6friendlyname
		except Exception as e:
			raise e

	@attribute6friendlyname.setter
	def attribute6friendlyname(self, attribute6friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute6friendlyname = attribute6friendlyname
		except Exception as e:
			raise e

	@property
	def attribute6format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute6format
		except Exception as e:
			raise e

	@attribute6format.setter
	def attribute6format(self, attribute6format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute6format = attribute6format
		except Exception as e:
			raise e

	@property
	def attribute7(self) :
		ur"""Name of attribute7 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute7
		except Exception as e:
			raise e

	@attribute7.setter
	def attribute7(self, attribute7) :
		ur"""Name of attribute7 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute7 = attribute7
		except Exception as e:
			raise e

	@property
	def attribute7expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute7expr
		except Exception as e:
			raise e

	@attribute7expr.setter
	def attribute7expr(self, attribute7expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute7expr = attribute7expr
		except Exception as e:
			raise e

	@property
	def attribute7friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute7friendlyname
		except Exception as e:
			raise e

	@attribute7friendlyname.setter
	def attribute7friendlyname(self, attribute7friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute7friendlyname = attribute7friendlyname
		except Exception as e:
			raise e

	@property
	def attribute7format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute7format
		except Exception as e:
			raise e

	@attribute7format.setter
	def attribute7format(self, attribute7format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute7format = attribute7format
		except Exception as e:
			raise e

	@property
	def attribute8(self) :
		ur"""Name of attribute8 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute8
		except Exception as e:
			raise e

	@attribute8.setter
	def attribute8(self, attribute8) :
		ur"""Name of attribute8 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute8 = attribute8
		except Exception as e:
			raise e

	@property
	def attribute8expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute8expr
		except Exception as e:
			raise e

	@attribute8expr.setter
	def attribute8expr(self, attribute8expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute8expr = attribute8expr
		except Exception as e:
			raise e

	@property
	def attribute8friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute8friendlyname
		except Exception as e:
			raise e

	@attribute8friendlyname.setter
	def attribute8friendlyname(self, attribute8friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute8friendlyname = attribute8friendlyname
		except Exception as e:
			raise e

	@property
	def attribute8format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute8format
		except Exception as e:
			raise e

	@attribute8format.setter
	def attribute8format(self, attribute8format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute8format = attribute8format
		except Exception as e:
			raise e

	@property
	def attribute9(self) :
		ur"""Name of attribute9 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute9
		except Exception as e:
			raise e

	@attribute9.setter
	def attribute9(self, attribute9) :
		ur"""Name of attribute9 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute9 = attribute9
		except Exception as e:
			raise e

	@property
	def attribute9expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute9expr
		except Exception as e:
			raise e

	@attribute9expr.setter
	def attribute9expr(self, attribute9expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute9expr = attribute9expr
		except Exception as e:
			raise e

	@property
	def attribute9friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute9friendlyname
		except Exception as e:
			raise e

	@attribute9friendlyname.setter
	def attribute9friendlyname(self, attribute9friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute9friendlyname = attribute9friendlyname
		except Exception as e:
			raise e

	@property
	def attribute9format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute9format
		except Exception as e:
			raise e

	@attribute9format.setter
	def attribute9format(self, attribute9format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute9format = attribute9format
		except Exception as e:
			raise e

	@property
	def attribute10(self) :
		ur"""Name of attribute10 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute10
		except Exception as e:
			raise e

	@attribute10.setter
	def attribute10(self, attribute10) :
		ur"""Name of attribute10 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute10 = attribute10
		except Exception as e:
			raise e

	@property
	def attribute10expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute10expr
		except Exception as e:
			raise e

	@attribute10expr.setter
	def attribute10expr(self, attribute10expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute10expr = attribute10expr
		except Exception as e:
			raise e

	@property
	def attribute10friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute10friendlyname
		except Exception as e:
			raise e

	@attribute10friendlyname.setter
	def attribute10friendlyname(self, attribute10friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute10friendlyname = attribute10friendlyname
		except Exception as e:
			raise e

	@property
	def attribute10format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute10format
		except Exception as e:
			raise e

	@attribute10format.setter
	def attribute10format(self, attribute10format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute10format = attribute10format
		except Exception as e:
			raise e

	@property
	def attribute11(self) :
		ur"""Name of attribute11 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute11
		except Exception as e:
			raise e

	@attribute11.setter
	def attribute11(self, attribute11) :
		ur"""Name of attribute11 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute11 = attribute11
		except Exception as e:
			raise e

	@property
	def attribute11expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute11expr
		except Exception as e:
			raise e

	@attribute11expr.setter
	def attribute11expr(self, attribute11expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute11expr = attribute11expr
		except Exception as e:
			raise e

	@property
	def attribute11friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute11friendlyname
		except Exception as e:
			raise e

	@attribute11friendlyname.setter
	def attribute11friendlyname(self, attribute11friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute11friendlyname = attribute11friendlyname
		except Exception as e:
			raise e

	@property
	def attribute11format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute11format
		except Exception as e:
			raise e

	@attribute11format.setter
	def attribute11format(self, attribute11format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute11format = attribute11format
		except Exception as e:
			raise e

	@property
	def attribute12(self) :
		ur"""Name of attribute12 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute12
		except Exception as e:
			raise e

	@attribute12.setter
	def attribute12(self, attribute12) :
		ur"""Name of attribute12 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute12 = attribute12
		except Exception as e:
			raise e

	@property
	def attribute12expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute12expr
		except Exception as e:
			raise e

	@attribute12expr.setter
	def attribute12expr(self, attribute12expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute12expr = attribute12expr
		except Exception as e:
			raise e

	@property
	def attribute12friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute12friendlyname
		except Exception as e:
			raise e

	@attribute12friendlyname.setter
	def attribute12friendlyname(self, attribute12friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute12friendlyname = attribute12friendlyname
		except Exception as e:
			raise e

	@property
	def attribute12format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute12format
		except Exception as e:
			raise e

	@attribute12format.setter
	def attribute12format(self, attribute12format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute12format = attribute12format
		except Exception as e:
			raise e

	@property
	def attribute13(self) :
		ur"""Name of attribute13 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute13
		except Exception as e:
			raise e

	@attribute13.setter
	def attribute13(self, attribute13) :
		ur"""Name of attribute13 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute13 = attribute13
		except Exception as e:
			raise e

	@property
	def attribute13expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute13expr
		except Exception as e:
			raise e

	@attribute13expr.setter
	def attribute13expr(self, attribute13expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute13expr = attribute13expr
		except Exception as e:
			raise e

	@property
	def attribute13friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute13friendlyname
		except Exception as e:
			raise e

	@attribute13friendlyname.setter
	def attribute13friendlyname(self, attribute13friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute13friendlyname = attribute13friendlyname
		except Exception as e:
			raise e

	@property
	def attribute13format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute13format
		except Exception as e:
			raise e

	@attribute13format.setter
	def attribute13format(self, attribute13format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute13format = attribute13format
		except Exception as e:
			raise e

	@property
	def attribute14(self) :
		ur"""Name of attribute14 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute14
		except Exception as e:
			raise e

	@attribute14.setter
	def attribute14(self, attribute14) :
		ur"""Name of attribute14 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute14 = attribute14
		except Exception as e:
			raise e

	@property
	def attribute14expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute14expr
		except Exception as e:
			raise e

	@attribute14expr.setter
	def attribute14expr(self, attribute14expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute14expr = attribute14expr
		except Exception as e:
			raise e

	@property
	def attribute14friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute14friendlyname
		except Exception as e:
			raise e

	@attribute14friendlyname.setter
	def attribute14friendlyname(self, attribute14friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute14friendlyname = attribute14friendlyname
		except Exception as e:
			raise e

	@property
	def attribute14format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute14format
		except Exception as e:
			raise e

	@attribute14format.setter
	def attribute14format(self, attribute14format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute14format = attribute14format
		except Exception as e:
			raise e

	@property
	def attribute15(self) :
		ur"""Name of attribute15 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute15
		except Exception as e:
			raise e

	@attribute15.setter
	def attribute15(self, attribute15) :
		ur"""Name of attribute15 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute15 = attribute15
		except Exception as e:
			raise e

	@property
	def attribute15expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute15expr
		except Exception as e:
			raise e

	@attribute15expr.setter
	def attribute15expr(self, attribute15expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute15expr = attribute15expr
		except Exception as e:
			raise e

	@property
	def attribute15friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute15friendlyname
		except Exception as e:
			raise e

	@attribute15friendlyname.setter
	def attribute15friendlyname(self, attribute15friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute15friendlyname = attribute15friendlyname
		except Exception as e:
			raise e

	@property
	def attribute15format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute15format
		except Exception as e:
			raise e

	@attribute15format.setter
	def attribute15format(self, attribute15format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute15format = attribute15format
		except Exception as e:
			raise e

	@property
	def attribute16(self) :
		ur"""Name of attribute16 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute16
		except Exception as e:
			raise e

	@attribute16.setter
	def attribute16(self, attribute16) :
		ur"""Name of attribute16 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute16 = attribute16
		except Exception as e:
			raise e

	@property
	def attribute16expr(self) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute16expr
		except Exception as e:
			raise e

	@attribute16expr.setter
	def attribute16expr(self, attribute16expr) :
		ur"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute16expr = attribute16expr
		except Exception as e:
			raise e

	@property
	def attribute16friendlyname(self) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64.
		"""
		try :
			return self._attribute16friendlyname
		except Exception as e:
			raise e

	@attribute16friendlyname.setter
	def attribute16friendlyname(self, attribute16friendlyname) :
		ur"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.<br/>Maximum length =  64
		"""
		try :
			self._attribute16friendlyname = attribute16friendlyname
		except Exception as e:
			raise e

	@property
	def attribute16format(self) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute16format
		except Exception as e:
			raise e

	@attribute16format.setter
	def attribute16format(self, attribute16format) :
		ur"""Format of Attribute1 to be sent in Assertion.<br/>Default value: SAML_ATTR_UNSPECIFIED<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute16format = attribute16format
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnsamlssoprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnsamlssoprofile
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
		ur""" Use this API to add vpnsamlssoprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnsamlssoprofile()
				addresource.name = resource.name
				addresource.samlsigningcertname = resource.samlsigningcertname
				addresource.assertionconsumerserviceurl = resource.assertionconsumerserviceurl
				addresource.relaystaterule = resource.relaystaterule
				addresource.sendpassword = resource.sendpassword
				addresource.samlissuername = resource.samlissuername
				addresource.signaturealg = resource.signaturealg
				addresource.digestmethod = resource.digestmethod
				addresource.audience = resource.audience
				addresource.nameidformat = resource.nameidformat
				addresource.nameidexpr = resource.nameidexpr
				addresource.attribute1 = resource.attribute1
				addresource.attribute1expr = resource.attribute1expr
				addresource.attribute1friendlyname = resource.attribute1friendlyname
				addresource.attribute1format = resource.attribute1format
				addresource.attribute2 = resource.attribute2
				addresource.attribute2expr = resource.attribute2expr
				addresource.attribute2friendlyname = resource.attribute2friendlyname
				addresource.attribute2format = resource.attribute2format
				addresource.attribute3 = resource.attribute3
				addresource.attribute3expr = resource.attribute3expr
				addresource.attribute3friendlyname = resource.attribute3friendlyname
				addresource.attribute3format = resource.attribute3format
				addresource.attribute4 = resource.attribute4
				addresource.attribute4expr = resource.attribute4expr
				addresource.attribute4friendlyname = resource.attribute4friendlyname
				addresource.attribute4format = resource.attribute4format
				addresource.attribute5 = resource.attribute5
				addresource.attribute5expr = resource.attribute5expr
				addresource.attribute5friendlyname = resource.attribute5friendlyname
				addresource.attribute5format = resource.attribute5format
				addresource.attribute6 = resource.attribute6
				addresource.attribute6expr = resource.attribute6expr
				addresource.attribute6friendlyname = resource.attribute6friendlyname
				addresource.attribute6format = resource.attribute6format
				addresource.attribute7 = resource.attribute7
				addresource.attribute7expr = resource.attribute7expr
				addresource.attribute7friendlyname = resource.attribute7friendlyname
				addresource.attribute7format = resource.attribute7format
				addresource.attribute8 = resource.attribute8
				addresource.attribute8expr = resource.attribute8expr
				addresource.attribute8friendlyname = resource.attribute8friendlyname
				addresource.attribute8format = resource.attribute8format
				addresource.attribute9 = resource.attribute9
				addresource.attribute9expr = resource.attribute9expr
				addresource.attribute9friendlyname = resource.attribute9friendlyname
				addresource.attribute9format = resource.attribute9format
				addresource.attribute10 = resource.attribute10
				addresource.attribute10expr = resource.attribute10expr
				addresource.attribute10friendlyname = resource.attribute10friendlyname
				addresource.attribute10format = resource.attribute10format
				addresource.attribute11 = resource.attribute11
				addresource.attribute11expr = resource.attribute11expr
				addresource.attribute11friendlyname = resource.attribute11friendlyname
				addresource.attribute11format = resource.attribute11format
				addresource.attribute12 = resource.attribute12
				addresource.attribute12expr = resource.attribute12expr
				addresource.attribute12friendlyname = resource.attribute12friendlyname
				addresource.attribute12format = resource.attribute12format
				addresource.attribute13 = resource.attribute13
				addresource.attribute13expr = resource.attribute13expr
				addresource.attribute13friendlyname = resource.attribute13friendlyname
				addresource.attribute13format = resource.attribute13format
				addresource.attribute14 = resource.attribute14
				addresource.attribute14expr = resource.attribute14expr
				addresource.attribute14friendlyname = resource.attribute14friendlyname
				addresource.attribute14format = resource.attribute14format
				addresource.attribute15 = resource.attribute15
				addresource.attribute15expr = resource.attribute15expr
				addresource.attribute15friendlyname = resource.attribute15friendlyname
				addresource.attribute15format = resource.attribute15format
				addresource.attribute16 = resource.attribute16
				addresource.attribute16expr = resource.attribute16expr
				addresource.attribute16friendlyname = resource.attribute16friendlyname
				addresource.attribute16format = resource.attribute16format
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnsamlssoprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].samlsigningcertname = resource[i].samlsigningcertname
						addresources[i].assertionconsumerserviceurl = resource[i].assertionconsumerserviceurl
						addresources[i].relaystaterule = resource[i].relaystaterule
						addresources[i].sendpassword = resource[i].sendpassword
						addresources[i].samlissuername = resource[i].samlissuername
						addresources[i].signaturealg = resource[i].signaturealg
						addresources[i].digestmethod = resource[i].digestmethod
						addresources[i].audience = resource[i].audience
						addresources[i].nameidformat = resource[i].nameidformat
						addresources[i].nameidexpr = resource[i].nameidexpr
						addresources[i].attribute1 = resource[i].attribute1
						addresources[i].attribute1expr = resource[i].attribute1expr
						addresources[i].attribute1friendlyname = resource[i].attribute1friendlyname
						addresources[i].attribute1format = resource[i].attribute1format
						addresources[i].attribute2 = resource[i].attribute2
						addresources[i].attribute2expr = resource[i].attribute2expr
						addresources[i].attribute2friendlyname = resource[i].attribute2friendlyname
						addresources[i].attribute2format = resource[i].attribute2format
						addresources[i].attribute3 = resource[i].attribute3
						addresources[i].attribute3expr = resource[i].attribute3expr
						addresources[i].attribute3friendlyname = resource[i].attribute3friendlyname
						addresources[i].attribute3format = resource[i].attribute3format
						addresources[i].attribute4 = resource[i].attribute4
						addresources[i].attribute4expr = resource[i].attribute4expr
						addresources[i].attribute4friendlyname = resource[i].attribute4friendlyname
						addresources[i].attribute4format = resource[i].attribute4format
						addresources[i].attribute5 = resource[i].attribute5
						addresources[i].attribute5expr = resource[i].attribute5expr
						addresources[i].attribute5friendlyname = resource[i].attribute5friendlyname
						addresources[i].attribute5format = resource[i].attribute5format
						addresources[i].attribute6 = resource[i].attribute6
						addresources[i].attribute6expr = resource[i].attribute6expr
						addresources[i].attribute6friendlyname = resource[i].attribute6friendlyname
						addresources[i].attribute6format = resource[i].attribute6format
						addresources[i].attribute7 = resource[i].attribute7
						addresources[i].attribute7expr = resource[i].attribute7expr
						addresources[i].attribute7friendlyname = resource[i].attribute7friendlyname
						addresources[i].attribute7format = resource[i].attribute7format
						addresources[i].attribute8 = resource[i].attribute8
						addresources[i].attribute8expr = resource[i].attribute8expr
						addresources[i].attribute8friendlyname = resource[i].attribute8friendlyname
						addresources[i].attribute8format = resource[i].attribute8format
						addresources[i].attribute9 = resource[i].attribute9
						addresources[i].attribute9expr = resource[i].attribute9expr
						addresources[i].attribute9friendlyname = resource[i].attribute9friendlyname
						addresources[i].attribute9format = resource[i].attribute9format
						addresources[i].attribute10 = resource[i].attribute10
						addresources[i].attribute10expr = resource[i].attribute10expr
						addresources[i].attribute10friendlyname = resource[i].attribute10friendlyname
						addresources[i].attribute10format = resource[i].attribute10format
						addresources[i].attribute11 = resource[i].attribute11
						addresources[i].attribute11expr = resource[i].attribute11expr
						addresources[i].attribute11friendlyname = resource[i].attribute11friendlyname
						addresources[i].attribute11format = resource[i].attribute11format
						addresources[i].attribute12 = resource[i].attribute12
						addresources[i].attribute12expr = resource[i].attribute12expr
						addresources[i].attribute12friendlyname = resource[i].attribute12friendlyname
						addresources[i].attribute12format = resource[i].attribute12format
						addresources[i].attribute13 = resource[i].attribute13
						addresources[i].attribute13expr = resource[i].attribute13expr
						addresources[i].attribute13friendlyname = resource[i].attribute13friendlyname
						addresources[i].attribute13format = resource[i].attribute13format
						addresources[i].attribute14 = resource[i].attribute14
						addresources[i].attribute14expr = resource[i].attribute14expr
						addresources[i].attribute14friendlyname = resource[i].attribute14friendlyname
						addresources[i].attribute14format = resource[i].attribute14format
						addresources[i].attribute15 = resource[i].attribute15
						addresources[i].attribute15expr = resource[i].attribute15expr
						addresources[i].attribute15friendlyname = resource[i].attribute15friendlyname
						addresources[i].attribute15format = resource[i].attribute15format
						addresources[i].attribute16 = resource[i].attribute16
						addresources[i].attribute16expr = resource[i].attribute16expr
						addresources[i].attribute16friendlyname = resource[i].attribute16friendlyname
						addresources[i].attribute16format = resource[i].attribute16format
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete vpnsamlssoprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnsamlssoprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnsamlssoprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnsamlssoprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update vpnsamlssoprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpnsamlssoprofile()
				updateresource.name = resource.name
				updateresource.samlsigningcertname = resource.samlsigningcertname
				updateresource.assertionconsumerserviceurl = resource.assertionconsumerserviceurl
				updateresource.sendpassword = resource.sendpassword
				updateresource.samlissuername = resource.samlissuername
				updateresource.relaystaterule = resource.relaystaterule
				updateresource.signaturealg = resource.signaturealg
				updateresource.digestmethod = resource.digestmethod
				updateresource.audience = resource.audience
				updateresource.nameidformat = resource.nameidformat
				updateresource.nameidexpr = resource.nameidexpr
				updateresource.attribute1 = resource.attribute1
				updateresource.attribute1expr = resource.attribute1expr
				updateresource.attribute1friendlyname = resource.attribute1friendlyname
				updateresource.attribute1format = resource.attribute1format
				updateresource.attribute2 = resource.attribute2
				updateresource.attribute2expr = resource.attribute2expr
				updateresource.attribute2friendlyname = resource.attribute2friendlyname
				updateresource.attribute2format = resource.attribute2format
				updateresource.attribute3 = resource.attribute3
				updateresource.attribute3expr = resource.attribute3expr
				updateresource.attribute3friendlyname = resource.attribute3friendlyname
				updateresource.attribute3format = resource.attribute3format
				updateresource.attribute4 = resource.attribute4
				updateresource.attribute4expr = resource.attribute4expr
				updateresource.attribute4friendlyname = resource.attribute4friendlyname
				updateresource.attribute4format = resource.attribute4format
				updateresource.attribute5 = resource.attribute5
				updateresource.attribute5expr = resource.attribute5expr
				updateresource.attribute5friendlyname = resource.attribute5friendlyname
				updateresource.attribute5format = resource.attribute5format
				updateresource.attribute6 = resource.attribute6
				updateresource.attribute6expr = resource.attribute6expr
				updateresource.attribute6friendlyname = resource.attribute6friendlyname
				updateresource.attribute6format = resource.attribute6format
				updateresource.attribute7 = resource.attribute7
				updateresource.attribute7expr = resource.attribute7expr
				updateresource.attribute7friendlyname = resource.attribute7friendlyname
				updateresource.attribute7format = resource.attribute7format
				updateresource.attribute8 = resource.attribute8
				updateresource.attribute8expr = resource.attribute8expr
				updateresource.attribute8friendlyname = resource.attribute8friendlyname
				updateresource.attribute8format = resource.attribute8format
				updateresource.attribute9 = resource.attribute9
				updateresource.attribute9expr = resource.attribute9expr
				updateresource.attribute9friendlyname = resource.attribute9friendlyname
				updateresource.attribute9format = resource.attribute9format
				updateresource.attribute10 = resource.attribute10
				updateresource.attribute10expr = resource.attribute10expr
				updateresource.attribute10friendlyname = resource.attribute10friendlyname
				updateresource.attribute10format = resource.attribute10format
				updateresource.attribute11 = resource.attribute11
				updateresource.attribute11expr = resource.attribute11expr
				updateresource.attribute11friendlyname = resource.attribute11friendlyname
				updateresource.attribute11format = resource.attribute11format
				updateresource.attribute12 = resource.attribute12
				updateresource.attribute12expr = resource.attribute12expr
				updateresource.attribute12friendlyname = resource.attribute12friendlyname
				updateresource.attribute12format = resource.attribute12format
				updateresource.attribute13 = resource.attribute13
				updateresource.attribute13expr = resource.attribute13expr
				updateresource.attribute13friendlyname = resource.attribute13friendlyname
				updateresource.attribute13format = resource.attribute13format
				updateresource.attribute14 = resource.attribute14
				updateresource.attribute14expr = resource.attribute14expr
				updateresource.attribute14friendlyname = resource.attribute14friendlyname
				updateresource.attribute14format = resource.attribute14format
				updateresource.attribute15 = resource.attribute15
				updateresource.attribute15expr = resource.attribute15expr
				updateresource.attribute15friendlyname = resource.attribute15friendlyname
				updateresource.attribute15format = resource.attribute15format
				updateresource.attribute16 = resource.attribute16
				updateresource.attribute16expr = resource.attribute16expr
				updateresource.attribute16friendlyname = resource.attribute16friendlyname
				updateresource.attribute16format = resource.attribute16format
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnsamlssoprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].samlsigningcertname = resource[i].samlsigningcertname
						updateresources[i].assertionconsumerserviceurl = resource[i].assertionconsumerserviceurl
						updateresources[i].sendpassword = resource[i].sendpassword
						updateresources[i].samlissuername = resource[i].samlissuername
						updateresources[i].relaystaterule = resource[i].relaystaterule
						updateresources[i].signaturealg = resource[i].signaturealg
						updateresources[i].digestmethod = resource[i].digestmethod
						updateresources[i].audience = resource[i].audience
						updateresources[i].nameidformat = resource[i].nameidformat
						updateresources[i].nameidexpr = resource[i].nameidexpr
						updateresources[i].attribute1 = resource[i].attribute1
						updateresources[i].attribute1expr = resource[i].attribute1expr
						updateresources[i].attribute1friendlyname = resource[i].attribute1friendlyname
						updateresources[i].attribute1format = resource[i].attribute1format
						updateresources[i].attribute2 = resource[i].attribute2
						updateresources[i].attribute2expr = resource[i].attribute2expr
						updateresources[i].attribute2friendlyname = resource[i].attribute2friendlyname
						updateresources[i].attribute2format = resource[i].attribute2format
						updateresources[i].attribute3 = resource[i].attribute3
						updateresources[i].attribute3expr = resource[i].attribute3expr
						updateresources[i].attribute3friendlyname = resource[i].attribute3friendlyname
						updateresources[i].attribute3format = resource[i].attribute3format
						updateresources[i].attribute4 = resource[i].attribute4
						updateresources[i].attribute4expr = resource[i].attribute4expr
						updateresources[i].attribute4friendlyname = resource[i].attribute4friendlyname
						updateresources[i].attribute4format = resource[i].attribute4format
						updateresources[i].attribute5 = resource[i].attribute5
						updateresources[i].attribute5expr = resource[i].attribute5expr
						updateresources[i].attribute5friendlyname = resource[i].attribute5friendlyname
						updateresources[i].attribute5format = resource[i].attribute5format
						updateresources[i].attribute6 = resource[i].attribute6
						updateresources[i].attribute6expr = resource[i].attribute6expr
						updateresources[i].attribute6friendlyname = resource[i].attribute6friendlyname
						updateresources[i].attribute6format = resource[i].attribute6format
						updateresources[i].attribute7 = resource[i].attribute7
						updateresources[i].attribute7expr = resource[i].attribute7expr
						updateresources[i].attribute7friendlyname = resource[i].attribute7friendlyname
						updateresources[i].attribute7format = resource[i].attribute7format
						updateresources[i].attribute8 = resource[i].attribute8
						updateresources[i].attribute8expr = resource[i].attribute8expr
						updateresources[i].attribute8friendlyname = resource[i].attribute8friendlyname
						updateresources[i].attribute8format = resource[i].attribute8format
						updateresources[i].attribute9 = resource[i].attribute9
						updateresources[i].attribute9expr = resource[i].attribute9expr
						updateresources[i].attribute9friendlyname = resource[i].attribute9friendlyname
						updateresources[i].attribute9format = resource[i].attribute9format
						updateresources[i].attribute10 = resource[i].attribute10
						updateresources[i].attribute10expr = resource[i].attribute10expr
						updateresources[i].attribute10friendlyname = resource[i].attribute10friendlyname
						updateresources[i].attribute10format = resource[i].attribute10format
						updateresources[i].attribute11 = resource[i].attribute11
						updateresources[i].attribute11expr = resource[i].attribute11expr
						updateresources[i].attribute11friendlyname = resource[i].attribute11friendlyname
						updateresources[i].attribute11format = resource[i].attribute11format
						updateresources[i].attribute12 = resource[i].attribute12
						updateresources[i].attribute12expr = resource[i].attribute12expr
						updateresources[i].attribute12friendlyname = resource[i].attribute12friendlyname
						updateresources[i].attribute12format = resource[i].attribute12format
						updateresources[i].attribute13 = resource[i].attribute13
						updateresources[i].attribute13expr = resource[i].attribute13expr
						updateresources[i].attribute13friendlyname = resource[i].attribute13friendlyname
						updateresources[i].attribute13format = resource[i].attribute13format
						updateresources[i].attribute14 = resource[i].attribute14
						updateresources[i].attribute14expr = resource[i].attribute14expr
						updateresources[i].attribute14friendlyname = resource[i].attribute14friendlyname
						updateresources[i].attribute14format = resource[i].attribute14format
						updateresources[i].attribute15 = resource[i].attribute15
						updateresources[i].attribute15expr = resource[i].attribute15expr
						updateresources[i].attribute15friendlyname = resource[i].attribute15friendlyname
						updateresources[i].attribute15format = resource[i].attribute15format
						updateresources[i].attribute16 = resource[i].attribute16
						updateresources[i].attribute16expr = resource[i].attribute16expr
						updateresources[i].attribute16friendlyname = resource[i].attribute16friendlyname
						updateresources[i].attribute16format = resource[i].attribute16format
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of vpnsamlssoprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnsamlssoprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnsamlssoprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnsamlssoprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the vpnsamlssoprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnsamlssoprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = vpnsamlssoprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [vpnsamlssoprofile() for _ in range(len(name))]
							obj = [vpnsamlssoprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = vpnsamlssoprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of vpnsamlssoprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnsamlssoprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the vpnsamlssoprofile resources configured on NetScaler.
		"""
		try :
			obj = vpnsamlssoprofile()
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
		ur""" Use this API to count filtered the set of vpnsamlssoprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnsamlssoprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Attribute3format:
		URI = "URI"
		Basic = "Basic"

	class Sendpassword:
		ON = "ON"
		OFF = "OFF"

	class Attribute6format:
		URI = "URI"
		Basic = "Basic"

	class Attribute10format:
		URI = "URI"
		Basic = "Basic"

	class Attribute9format:
		URI = "URI"
		Basic = "Basic"

	class Nameidformat:
		Unspecified = "Unspecified"
		emailAddress = "emailAddress"
		X509SubjectName = "X509SubjectName"
		WindowsDomainQualifiedName = "WindowsDomainQualifiedName"
		kerberos = "kerberos"
		entity = "entity"
		persistent = "persistent"
		Transient = "transient"

	class Signaturealg:
		RSA_SHA1 = "RSA-SHA1"
		RSA_SHA256 = "RSA-SHA256"

	class Attribute1format:
		URI = "URI"
		Basic = "Basic"

	class Attribute12format:
		URI = "URI"
		Basic = "Basic"

	class Attribute8format:
		URI = "URI"
		Basic = "Basic"

	class Attribute5format:
		URI = "URI"
		Basic = "Basic"

	class Attribute7format:
		URI = "URI"
		Basic = "Basic"

	class Attribute15format:
		URI = "URI"
		Basic = "Basic"

	class Digestmethod:
		SHA1 = "SHA1"
		SHA256 = "SHA256"

	class Attribute2format:
		URI = "URI"
		Basic = "Basic"

	class Attribute4format:
		URI = "URI"
		Basic = "Basic"

	class Attribute13format:
		URI = "URI"
		Basic = "Basic"

	class Attribute14format:
		URI = "URI"
		Basic = "Basic"

	class Attribute16format:
		URI = "URI"
		Basic = "Basic"

	class Attribute11format:
		URI = "URI"
		Basic = "Basic"

class vpnsamlssoprofile_response(base_response) :
	def __init__(self, length=1) :
		self.vpnsamlssoprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnsamlssoprofile = [vpnsamlssoprofile() for _ in range(length)]

