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

class tmtrafficaction(base_resource) :
	""" Configuration for TM traffic action resource. """
	def __init__(self) :
		self._name = ""
		self._apptimeout = 0
		self._sso = ""
		self._formssoaction = ""
		self._persistentcookie = ""
		self._initiatelogout = ""
		self._kcdaccount = ""
		self._samlssoprofile = ""
		self._forcedtimeout = ""
		self._forcedtimeoutval = 0
		self._userexpression = ""
		self._passwdexpression = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the traffic action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a traffic action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the traffic action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a traffic action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def apptimeout(self) :
		ur"""Time interval, in minutes, of user inactivity after which the connection is closed.<br/>Minimum length =  1<br/>Maximum length =  715827.
		"""
		try :
			return self._apptimeout
		except Exception as e:
			raise e

	@apptimeout.setter
	def apptimeout(self, apptimeout) :
		ur"""Time interval, in minutes, of user inactivity after which the connection is closed.<br/>Minimum length =  1<br/>Maximum length =  715827
		"""
		try :
			self._apptimeout = apptimeout
		except Exception as e:
			raise e

	@property
	def sso(self) :
		ur"""Use single sign-on for the resource that the user is accessing now.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sso
		except Exception as e:
			raise e

	@sso.setter
	def sso(self, sso) :
		ur"""Use single sign-on for the resource that the user is accessing now.<br/>Possible values = ON, OFF
		"""
		try :
			self._sso = sso
		except Exception as e:
			raise e

	@property
	def formssoaction(self) :
		ur"""Name of the configured form-based single sign-on profile.
		"""
		try :
			return self._formssoaction
		except Exception as e:
			raise e

	@formssoaction.setter
	def formssoaction(self, formssoaction) :
		ur"""Name of the configured form-based single sign-on profile.
		"""
		try :
			self._formssoaction = formssoaction
		except Exception as e:
			raise e

	@property
	def persistentcookie(self) :
		ur"""Use persistent cookies for the traffic session. A persistent cookie remains on the user device and is sent with each HTTP request. The cookie becomes stale if the session ends.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._persistentcookie
		except Exception as e:
			raise e

	@persistentcookie.setter
	def persistentcookie(self, persistentcookie) :
		ur"""Use persistent cookies for the traffic session. A persistent cookie remains on the user device and is sent with each HTTP request. The cookie becomes stale if the session ends.<br/>Possible values = ON, OFF
		"""
		try :
			self._persistentcookie = persistentcookie
		except Exception as e:
			raise e

	@property
	def initiatelogout(self) :
		ur"""Initiate logout for the traffic management (TM) session if the policy evaluates to true. The session is then terminated after two minutes.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._initiatelogout
		except Exception as e:
			raise e

	@initiatelogout.setter
	def initiatelogout(self, initiatelogout) :
		ur"""Initiate logout for the traffic management (TM) session if the policy evaluates to true. The session is then terminated after two minutes.<br/>Possible values = ON, OFF
		"""
		try :
			self._initiatelogout = initiatelogout
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		ur"""Kerberos constrained delegation account name.<br/>Default value: "None"<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		ur"""Kerberos constrained delegation account name.<br/>Default value: "None"<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def samlssoprofile(self) :
		ur"""Profile to be used for doing SAML SSO to remote relying party.<br/>Minimum length =  1.
		"""
		try :
			return self._samlssoprofile
		except Exception as e:
			raise e

	@samlssoprofile.setter
	def samlssoprofile(self, samlssoprofile) :
		ur"""Profile to be used for doing SAML SSO to remote relying party.<br/>Minimum length =  1
		"""
		try :
			self._samlssoprofile = samlssoprofile
		except Exception as e:
			raise e

	@property
	def forcedtimeout(self) :
		ur"""Setting to start, stop or reset TM session force timer.<br/>Possible values = START, STOP, RESET.
		"""
		try :
			return self._forcedtimeout
		except Exception as e:
			raise e

	@forcedtimeout.setter
	def forcedtimeout(self, forcedtimeout) :
		ur"""Setting to start, stop or reset TM session force timer.<br/>Possible values = START, STOP, RESET
		"""
		try :
			self._forcedtimeout = forcedtimeout
		except Exception as e:
			raise e

	@property
	def forcedtimeoutval(self) :
		ur"""Time interval, in minutes, for which force timer should be set.
		"""
		try :
			return self._forcedtimeoutval
		except Exception as e:
			raise e

	@forcedtimeoutval.setter
	def forcedtimeoutval(self, forcedtimeoutval) :
		ur"""Time interval, in minutes, for which force timer should be set.
		"""
		try :
			self._forcedtimeoutval = forcedtimeoutval
		except Exception as e:
			raise e

	@property
	def userexpression(self) :
		ur"""expression that will be evaluated to obtain username for SingleSignOn.<br/>Maximum length =  256.
		"""
		try :
			return self._userexpression
		except Exception as e:
			raise e

	@userexpression.setter
	def userexpression(self, userexpression) :
		ur"""expression that will be evaluated to obtain username for SingleSignOn.<br/>Maximum length =  256
		"""
		try :
			self._userexpression = userexpression
		except Exception as e:
			raise e

	@property
	def passwdexpression(self) :
		ur"""expression that will be evaluated to obtain password for SingleSignOn.<br/>Maximum length =  256.
		"""
		try :
			return self._passwdexpression
		except Exception as e:
			raise e

	@passwdexpression.setter
	def passwdexpression(self, passwdexpression) :
		ur"""expression that will be evaluated to obtain password for SingleSignOn.<br/>Maximum length =  256
		"""
		try :
			self._passwdexpression = passwdexpression
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(tmtrafficaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tmtrafficaction
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
		ur""" Use this API to add tmtrafficaction.
		"""
		try :
			if type(resource) is not list :
				addresource = tmtrafficaction()
				addresource.name = resource.name
				addresource.apptimeout = resource.apptimeout
				addresource.sso = resource.sso
				addresource.formssoaction = resource.formssoaction
				addresource.persistentcookie = resource.persistentcookie
				addresource.initiatelogout = resource.initiatelogout
				addresource.kcdaccount = resource.kcdaccount
				addresource.samlssoprofile = resource.samlssoprofile
				addresource.forcedtimeout = resource.forcedtimeout
				addresource.forcedtimeoutval = resource.forcedtimeoutval
				addresource.userexpression = resource.userexpression
				addresource.passwdexpression = resource.passwdexpression
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ tmtrafficaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].apptimeout = resource[i].apptimeout
						addresources[i].sso = resource[i].sso
						addresources[i].formssoaction = resource[i].formssoaction
						addresources[i].persistentcookie = resource[i].persistentcookie
						addresources[i].initiatelogout = resource[i].initiatelogout
						addresources[i].kcdaccount = resource[i].kcdaccount
						addresources[i].samlssoprofile = resource[i].samlssoprofile
						addresources[i].forcedtimeout = resource[i].forcedtimeout
						addresources[i].forcedtimeoutval = resource[i].forcedtimeoutval
						addresources[i].userexpression = resource[i].userexpression
						addresources[i].passwdexpression = resource[i].passwdexpression
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete tmtrafficaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = tmtrafficaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ tmtrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ tmtrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update tmtrafficaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = tmtrafficaction()
				updateresource.name = resource.name
				updateresource.apptimeout = resource.apptimeout
				updateresource.sso = resource.sso
				updateresource.formssoaction = resource.formssoaction
				updateresource.persistentcookie = resource.persistentcookie
				updateresource.initiatelogout = resource.initiatelogout
				updateresource.kcdaccount = resource.kcdaccount
				updateresource.samlssoprofile = resource.samlssoprofile
				updateresource.forcedtimeout = resource.forcedtimeout
				updateresource.forcedtimeoutval = resource.forcedtimeoutval
				updateresource.userexpression = resource.userexpression
				updateresource.passwdexpression = resource.passwdexpression
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ tmtrafficaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].apptimeout = resource[i].apptimeout
						updateresources[i].sso = resource[i].sso
						updateresources[i].formssoaction = resource[i].formssoaction
						updateresources[i].persistentcookie = resource[i].persistentcookie
						updateresources[i].initiatelogout = resource[i].initiatelogout
						updateresources[i].kcdaccount = resource[i].kcdaccount
						updateresources[i].samlssoprofile = resource[i].samlssoprofile
						updateresources[i].forcedtimeout = resource[i].forcedtimeout
						updateresources[i].forcedtimeoutval = resource[i].forcedtimeoutval
						updateresources[i].userexpression = resource[i].userexpression
						updateresources[i].passwdexpression = resource[i].passwdexpression
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of tmtrafficaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = tmtrafficaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ tmtrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ tmtrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the tmtrafficaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = tmtrafficaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = tmtrafficaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [tmtrafficaction() for _ in range(len(name))]
							obj = [tmtrafficaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = tmtrafficaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of tmtrafficaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tmtrafficaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the tmtrafficaction resources configured on NetScaler.
		"""
		try :
			obj = tmtrafficaction()
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
		ur""" Use this API to count filtered the set of tmtrafficaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tmtrafficaction()
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

	class Forcedtimeout:
		START = "START"
		STOP = "STOP"
		RESET = "RESET"

	class Initiatelogout:
		ON = "ON"
		OFF = "OFF"

	class Sso:
		ON = "ON"
		OFF = "OFF"

class tmtrafficaction_response(base_response) :
	def __init__(self, length=1) :
		self.tmtrafficaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.tmtrafficaction = [tmtrafficaction() for _ in range(length)]

