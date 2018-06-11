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

class tmsessionaction(base_resource) :
	""" Configuration for TM session action resource. """
	def __init__(self) :
		self._name = ""
		self._sesstimeout = 0
		self._defaultauthorizationaction = ""
		self._sso = ""
		self._ssocredential = ""
		self._ssodomain = ""
		self._httponlycookie = ""
		self._kcdaccount = ""
		self._persistentcookie = ""
		self._persistentcookievalidity = 0
		self._homepage = ""
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the session action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a session action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the session action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a session action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def sesstimeout(self) :
		ur"""Session timeout, in minutes. If there is no traffic during the timeout period, the user is disconnected and must reauthenticate to access intranet resources.<br/>Minimum length =  1.
		"""
		try :
			return self._sesstimeout
		except Exception as e:
			raise e

	@sesstimeout.setter
	def sesstimeout(self, sesstimeout) :
		ur"""Session timeout, in minutes. If there is no traffic during the timeout period, the user is disconnected and must reauthenticate to access intranet resources.<br/>Minimum length =  1
		"""
		try :
			self._sesstimeout = sesstimeout
		except Exception as e:
			raise e

	@property
	def defaultauthorizationaction(self) :
		ur"""Allow or deny access to content for which there is no specific authorization policy.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._defaultauthorizationaction
		except Exception as e:
			raise e

	@defaultauthorizationaction.setter
	def defaultauthorizationaction(self, defaultauthorizationaction) :
		ur"""Allow or deny access to content for which there is no specific authorization policy.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._defaultauthorizationaction = defaultauthorizationaction
		except Exception as e:
			raise e

	@property
	def sso(self) :
		ur"""Use single sign-on (SSO) to log users on to all web applications automatically after they authenticate, or pass users to the web application logon page to authenticate to each application individually.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sso
		except Exception as e:
			raise e

	@sso.setter
	def sso(self, sso) :
		ur"""Use single sign-on (SSO) to log users on to all web applications automatically after they authenticate, or pass users to the web application logon page to authenticate to each application individually.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sso = sso
		except Exception as e:
			raise e

	@property
	def ssocredential(self) :
		ur"""Use the primary or secondary authentication credentials for single sign-on (SSO).<br/>Possible values = PRIMARY, SECONDARY.
		"""
		try :
			return self._ssocredential
		except Exception as e:
			raise e

	@ssocredential.setter
	def ssocredential(self, ssocredential) :
		ur"""Use the primary or secondary authentication credentials for single sign-on (SSO).<br/>Possible values = PRIMARY, SECONDARY
		"""
		try :
			self._ssocredential = ssocredential
		except Exception as e:
			raise e

	@property
	def ssodomain(self) :
		ur"""Domain to use for single sign-on (SSO).<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._ssodomain
		except Exception as e:
			raise e

	@ssodomain.setter
	def ssodomain(self, ssodomain) :
		ur"""Domain to use for single sign-on (SSO).<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._ssodomain = ssodomain
		except Exception as e:
			raise e

	@property
	def httponlycookie(self) :
		ur"""Allow only an HTTP session cookie, in which case the cookie cannot be accessed by scripts.<br/>Possible values = YES, NO.
		"""
		try :
			return self._httponlycookie
		except Exception as e:
			raise e

	@httponlycookie.setter
	def httponlycookie(self, httponlycookie) :
		ur"""Allow only an HTTP session cookie, in which case the cookie cannot be accessed by scripts.<br/>Possible values = YES, NO
		"""
		try :
			self._httponlycookie = httponlycookie
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
	def persistentcookie(self) :
		ur"""Enable or disable persistent SSO cookies for the traffic management (TM) session. A persistent cookie remains on the user device and is sent with each HTTP request. The cookie becomes stale if the session ends. This setting is overwritten if a traffic action sets persistent cookie to OFF. 
		Note: If persistent cookie is enabled, make sure you set the persistent cookie validity.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._persistentcookie
		except Exception as e:
			raise e

	@persistentcookie.setter
	def persistentcookie(self, persistentcookie) :
		ur"""Enable or disable persistent SSO cookies for the traffic management (TM) session. A persistent cookie remains on the user device and is sent with each HTTP request. The cookie becomes stale if the session ends. This setting is overwritten if a traffic action sets persistent cookie to OFF. 
		Note: If persistent cookie is enabled, make sure you set the persistent cookie validity.<br/>Possible values = ON, OFF
		"""
		try :
			self._persistentcookie = persistentcookie
		except Exception as e:
			raise e

	@property
	def persistentcookievalidity(self) :
		ur"""Integer specifying the number of minutes for which the persistent cookie remains valid. Can be set only if the persistent cookie setting is enabled.<br/>Minimum length =  1.
		"""
		try :
			return self._persistentcookievalidity
		except Exception as e:
			raise e

	@persistentcookievalidity.setter
	def persistentcookievalidity(self, persistentcookievalidity) :
		ur"""Integer specifying the number of minutes for which the persistent cookie remains valid. Can be set only if the persistent cookie setting is enabled.<br/>Minimum length =  1
		"""
		try :
			self._persistentcookievalidity = persistentcookievalidity
		except Exception as e:
			raise e

	@property
	def homepage(self) :
		ur"""Web address of the home page that a user is displayed when authentication vserver is bookmarked and used to login.
		"""
		try :
			return self._homepage
		except Exception as e:
			raise e

	@homepage.setter
	def homepage(self, homepage) :
		ur"""Web address of the home page that a user is displayed when authentication vserver is bookmarked and used to login.
		"""
		try :
			self._homepage = homepage
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(tmsessionaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tmsessionaction
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
		ur""" Use this API to add tmsessionaction.
		"""
		try :
			if type(resource) is not list :
				addresource = tmsessionaction()
				addresource.name = resource.name
				addresource.sesstimeout = resource.sesstimeout
				addresource.defaultauthorizationaction = resource.defaultauthorizationaction
				addresource.sso = resource.sso
				addresource.ssocredential = resource.ssocredential
				addresource.ssodomain = resource.ssodomain
				addresource.httponlycookie = resource.httponlycookie
				addresource.kcdaccount = resource.kcdaccount
				addresource.persistentcookie = resource.persistentcookie
				addresource.persistentcookievalidity = resource.persistentcookievalidity
				addresource.homepage = resource.homepage
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ tmsessionaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].sesstimeout = resource[i].sesstimeout
						addresources[i].defaultauthorizationaction = resource[i].defaultauthorizationaction
						addresources[i].sso = resource[i].sso
						addresources[i].ssocredential = resource[i].ssocredential
						addresources[i].ssodomain = resource[i].ssodomain
						addresources[i].httponlycookie = resource[i].httponlycookie
						addresources[i].kcdaccount = resource[i].kcdaccount
						addresources[i].persistentcookie = resource[i].persistentcookie
						addresources[i].persistentcookievalidity = resource[i].persistentcookievalidity
						addresources[i].homepage = resource[i].homepage
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete tmsessionaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = tmsessionaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ tmsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ tmsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update tmsessionaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = tmsessionaction()
				updateresource.name = resource.name
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
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ tmsessionaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].sesstimeout = resource[i].sesstimeout
						updateresources[i].defaultauthorizationaction = resource[i].defaultauthorizationaction
						updateresources[i].sso = resource[i].sso
						updateresources[i].ssocredential = resource[i].ssocredential
						updateresources[i].ssodomain = resource[i].ssodomain
						updateresources[i].kcdaccount = resource[i].kcdaccount
						updateresources[i].httponlycookie = resource[i].httponlycookie
						updateresources[i].persistentcookie = resource[i].persistentcookie
						updateresources[i].persistentcookievalidity = resource[i].persistentcookievalidity
						updateresources[i].homepage = resource[i].homepage
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of tmsessionaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = tmsessionaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ tmsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ tmsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the tmsessionaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = tmsessionaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = tmsessionaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [tmsessionaction() for _ in range(len(name))]
							obj = [tmsessionaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = tmsessionaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of tmsessionaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tmsessionaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the tmsessionaction resources configured on NetScaler.
		"""
		try :
			obj = tmsessionaction()
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
		ur""" Use this API to count filtered the set of tmsessionaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tmsessionaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Persistentcookie:
		ON = "ON"
		OFF = "OFF"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

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

class tmsessionaction_response(base_response) :
	def __init__(self, length=1) :
		self.tmsessionaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.tmsessionaction = [tmsessionaction() for _ in range(length)]

