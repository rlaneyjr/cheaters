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

class tmsessionparameter(base_resource) :
	""" Configuration for session parameter resource. """
	def __init__(self) :
		self._sesstimeout = 0
		self._defaultauthorizationaction = ""
		self._sso = ""
		self._ssocredential = ""
		self._ssodomain = ""
		self._kcdaccount = ""
		self._httponlycookie = ""
		self._persistentcookie = ""
		self._persistentcookievalidity = 0
		self._homepage = ""
		self._name = ""

	@property
	def sesstimeout(self) :
		ur"""Session timeout, in minutes. If there is no traffic during the timeout period, the user is disconnected and must reauthenticate to access the intranet resources.<br/>Default value: 30<br/>Minimum length =  1.
		"""
		try :
			return self._sesstimeout
		except Exception as e:
			raise e

	@sesstimeout.setter
	def sesstimeout(self, sesstimeout) :
		ur"""Session timeout, in minutes. If there is no traffic during the timeout period, the user is disconnected and must reauthenticate to access the intranet resources.<br/>Default value: 30<br/>Minimum length =  1
		"""
		try :
			self._sesstimeout = sesstimeout
		except Exception as e:
			raise e

	@property
	def defaultauthorizationaction(self) :
		ur"""Allow or deny access to content for which there is no specific authorization policy.<br/>Default value: ALLOW<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._defaultauthorizationaction
		except Exception as e:
			raise e

	@defaultauthorizationaction.setter
	def defaultauthorizationaction(self, defaultauthorizationaction) :
		ur"""Allow or deny access to content for which there is no specific authorization policy.<br/>Default value: ALLOW<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._defaultauthorizationaction = defaultauthorizationaction
		except Exception as e:
			raise e

	@property
	def sso(self) :
		ur"""Log users on to all web applications automatically after they authenticate, or pass users to the web application logon page to authenticate for each application.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sso
		except Exception as e:
			raise e

	@sso.setter
	def sso(self, sso) :
		ur"""Log users on to all web applications automatically after they authenticate, or pass users to the web application logon page to authenticate for each application.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sso = sso
		except Exception as e:
			raise e

	@property
	def ssocredential(self) :
		ur"""Use primary or secondary authentication credentials for single sign-on.<br/>Default value: PRIMARY<br/>Possible values = PRIMARY, SECONDARY.
		"""
		try :
			return self._ssocredential
		except Exception as e:
			raise e

	@ssocredential.setter
	def ssocredential(self, ssocredential) :
		ur"""Use primary or secondary authentication credentials for single sign-on.<br/>Default value: PRIMARY<br/>Possible values = PRIMARY, SECONDARY
		"""
		try :
			self._ssocredential = ssocredential
		except Exception as e:
			raise e

	@property
	def ssodomain(self) :
		ur"""Domain to use for single sign-on.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._ssodomain
		except Exception as e:
			raise e

	@ssodomain.setter
	def ssodomain(self, ssodomain) :
		ur"""Domain to use for single sign-on.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._ssodomain = ssodomain
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		ur"""Kerberos constrained delegation account name.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		ur"""Kerberos constrained delegation account name.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def httponlycookie(self) :
		ur"""Allow only an HTTP session cookie, in which case the cookie cannot be accessed by scripts.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._httponlycookie
		except Exception as e:
			raise e

	@httponlycookie.setter
	def httponlycookie(self, httponlycookie) :
		ur"""Allow only an HTTP session cookie, in which case the cookie cannot be accessed by scripts.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._httponlycookie = httponlycookie
		except Exception as e:
			raise e

	@property
	def persistentcookie(self) :
		ur"""Use persistent SSO cookies for the traffic session. A persistent cookie remains on the user device and is sent with each HTTP request. The cookie becomes stale if the session ends.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._persistentcookie
		except Exception as e:
			raise e

	@persistentcookie.setter
	def persistentcookie(self, persistentcookie) :
		ur"""Use persistent SSO cookies for the traffic session. A persistent cookie remains on the user device and is sent with each HTTP request. The cookie becomes stale if the session ends.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._persistentcookie = persistentcookie
		except Exception as e:
			raise e

	@property
	def persistentcookievalidity(self) :
		ur"""Integer specifying the number of minutes for which the persistent cookie remains valid. Can be set only if the persistence cookie setting is enabled.<br/>Minimum length =  1.
		"""
		try :
			return self._persistentcookievalidity
		except Exception as e:
			raise e

	@persistentcookievalidity.setter
	def persistentcookievalidity(self, persistentcookievalidity) :
		ur"""Integer specifying the number of minutes for which the persistent cookie remains valid. Can be set only if the persistence cookie setting is enabled.<br/>Minimum length =  1
		"""
		try :
			self._persistentcookievalidity = persistentcookievalidity
		except Exception as e:
			raise e

	@property
	def homepage(self) :
		ur"""Web address of the home page that a user is displayed when authentication vserver is bookmarked and used to login.<br/>Default value: "None".
		"""
		try :
			return self._homepage
		except Exception as e:
			raise e

	@homepage.setter
	def homepage(self, homepage) :
		ur"""Web address of the home page that a user is displayed when authentication vserver is bookmarked and used to login.<br/>Default value: "None"
		"""
		try :
			self._homepage = homepage
		except Exception as e:
			raise e

	@property
	def name(self) :
		try :
			return self._name
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(tmsessionparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tmsessionparameter
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
		ur""" Use this API to update tmsessionparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = tmsessionparameter()
				updateresource.sesstimeout = resource.sesstimeout
				updateresource.defaultauthorizationaction = resource.defaultauthorizationaction
				updateresource.sso = resource.sso
				updateresource.ssocredential = resource.ssocredential
				updateresource.ssodomain = resource.ssodomain
				updateresource.kcdaccount = resource.kcdaccount
				updateresource.httponlycookie = resource.httponlycookie
				updateresource.persistentcookie = resource.persistentcookie
				updateresource.persistentcookievalidity = resource.persistentcookievalidity
				updateresource.homepage = resource.homepage
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of tmsessionparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = tmsessionparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the tmsessionparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = tmsessionparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Persistentcookie:
		ON = "ON"
		OFF = "OFF"

	class Httponlycookie:
		YES = "YES"
		NO = "NO"

	class Defaultauthorizationaction:
		ALLOW = "ALLOW"
		DENY = "DENY"

	class Ssocredential:
		PRIMARY = "PRIMARY"
		SECONDARY = "SECONDARY"

	class Sso:
		ON = "ON"
		OFF = "OFF"

class tmsessionparameter_response(base_response) :
	def __init__(self, length=1) :
		self.tmsessionparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.tmsessionparameter = [tmsessionparameter() for _ in range(length)]

