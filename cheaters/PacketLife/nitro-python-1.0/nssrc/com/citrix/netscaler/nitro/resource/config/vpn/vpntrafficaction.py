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

class vpntrafficaction(base_resource) :
	""" Configuration for VPN traffic action resource. """
	def __init__(self) :
		self._name = ""
		self._qual = ""
		self._apptimeout = 0
		self._sso = ""
		self._hdx = ""
		self._formssoaction = ""
		self._fta = ""
		self._wanscaler = ""
		self._kcdaccount = ""
		self._samlssoprofile = ""
		self._proxy = ""
		self._userexpression = ""
		self._passwdexpression = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the traffic action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a traffic action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the traffic action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a traffic action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def qual(self) :
		ur"""Protocol, either HTTP or TCP, to be used with the action.<br/>Possible values = http, tcp.
		"""
		try :
			return self._qual
		except Exception as e:
			raise e

	@qual.setter
	def qual(self, qual) :
		ur"""Protocol, either HTTP or TCP, to be used with the action.<br/>Possible values = http, tcp
		"""
		try :
			self._qual = qual
		except Exception as e:
			raise e

	@property
	def apptimeout(self) :
		ur"""Maximum amount of time, in minutes, a user can stay logged on to the web application.<br/>Minimum length =  1<br/>Maximum length =  715827.
		"""
		try :
			return self._apptimeout
		except Exception as e:
			raise e

	@apptimeout.setter
	def apptimeout(self, apptimeout) :
		ur"""Maximum amount of time, in minutes, a user can stay logged on to the web application.<br/>Minimum length =  1<br/>Maximum length =  715827
		"""
		try :
			self._apptimeout = apptimeout
		except Exception as e:
			raise e

	@property
	def sso(self) :
		ur"""Provide single sign-on to the web application.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sso
		except Exception as e:
			raise e

	@sso.setter
	def sso(self, sso) :
		ur"""Provide single sign-on to the web application.<br/>Possible values = ON, OFF
		"""
		try :
			self._sso = sso
		except Exception as e:
			raise e

	@property
	def hdx(self) :
		ur"""Provide hdx proxy to the ICA traffic.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._hdx
		except Exception as e:
			raise e

	@hdx.setter
	def hdx(self, hdx) :
		ur"""Provide hdx proxy to the ICA traffic.<br/>Possible values = ON, OFF
		"""
		try :
			self._hdx = hdx
		except Exception as e:
			raise e

	@property
	def formssoaction(self) :
		ur"""Name of the form-based single sign-on profile. Form-based single sign-on allows users to log on one time to all protected applications in your network, instead of requiring them to log on separately to access each one.
		"""
		try :
			return self._formssoaction
		except Exception as e:
			raise e

	@formssoaction.setter
	def formssoaction(self, formssoaction) :
		ur"""Name of the form-based single sign-on profile. Form-based single sign-on allows users to log on one time to all protected applications in your network, instead of requiring them to log on separately to access each one.
		"""
		try :
			self._formssoaction = formssoaction
		except Exception as e:
			raise e

	@property
	def fta(self) :
		ur"""Specify file type association, which is a list of file extensions that users are allowed to open.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._fta
		except Exception as e:
			raise e

	@fta.setter
	def fta(self, fta) :
		ur"""Specify file type association, which is a list of file extensions that users are allowed to open.<br/>Possible values = ON, OFF
		"""
		try :
			self._fta = fta
		except Exception as e:
			raise e

	@property
	def wanscaler(self) :
		ur"""Use the Repeater Plug-in to optimize network traffic.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._wanscaler
		except Exception as e:
			raise e

	@wanscaler.setter
	def wanscaler(self, wanscaler) :
		ur"""Use the Repeater Plug-in to optimize network traffic.<br/>Possible values = ON, OFF
		"""
		try :
			self._wanscaler = wanscaler
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		ur"""Kerberos constrained delegation account name.<br/>Default value: "Default"<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		ur"""Kerberos constrained delegation account name.<br/>Default value: "Default"<br/>Minimum length =  1<br/>Maximum length =  32
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
	def proxy(self) :
		ur"""IP address and Port of the proxy server to be used for HTTP access for this request.<br/>Minimum length =  1.
		"""
		try :
			return self._proxy
		except Exception as e:
			raise e

	@proxy.setter
	def proxy(self, proxy) :
		ur"""IP address and Port of the proxy server to be used for HTTP access for this request.<br/>Minimum length =  1
		"""
		try :
			self._proxy = proxy
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
			result = service.payload_formatter.string_to_resource(vpntrafficaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpntrafficaction
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
		ur""" Use this API to add vpntrafficaction.
		"""
		try :
			if type(resource) is not list :
				addresource = vpntrafficaction()
				addresource.name = resource.name
				addresource.qual = resource.qual
				addresource.apptimeout = resource.apptimeout
				addresource.sso = resource.sso
				addresource.hdx = resource.hdx
				addresource.formssoaction = resource.formssoaction
				addresource.fta = resource.fta
				addresource.wanscaler = resource.wanscaler
				addresource.kcdaccount = resource.kcdaccount
				addresource.samlssoprofile = resource.samlssoprofile
				addresource.proxy = resource.proxy
				addresource.userexpression = resource.userexpression
				addresource.passwdexpression = resource.passwdexpression
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpntrafficaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].qual = resource[i].qual
						addresources[i].apptimeout = resource[i].apptimeout
						addresources[i].sso = resource[i].sso
						addresources[i].hdx = resource[i].hdx
						addresources[i].formssoaction = resource[i].formssoaction
						addresources[i].fta = resource[i].fta
						addresources[i].wanscaler = resource[i].wanscaler
						addresources[i].kcdaccount = resource[i].kcdaccount
						addresources[i].samlssoprofile = resource[i].samlssoprofile
						addresources[i].proxy = resource[i].proxy
						addresources[i].userexpression = resource[i].userexpression
						addresources[i].passwdexpression = resource[i].passwdexpression
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete vpntrafficaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpntrafficaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpntrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpntrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update vpntrafficaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpntrafficaction()
				updateresource.name = resource.name
				updateresource.apptimeout = resource.apptimeout
				updateresource.sso = resource.sso
				updateresource.hdx = resource.hdx
				updateresource.formssoaction = resource.formssoaction
				updateresource.fta = resource.fta
				updateresource.wanscaler = resource.wanscaler
				updateresource.kcdaccount = resource.kcdaccount
				updateresource.samlssoprofile = resource.samlssoprofile
				updateresource.proxy = resource.proxy
				updateresource.userexpression = resource.userexpression
				updateresource.passwdexpression = resource.passwdexpression
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpntrafficaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].apptimeout = resource[i].apptimeout
						updateresources[i].sso = resource[i].sso
						updateresources[i].hdx = resource[i].hdx
						updateresources[i].formssoaction = resource[i].formssoaction
						updateresources[i].fta = resource[i].fta
						updateresources[i].wanscaler = resource[i].wanscaler
						updateresources[i].kcdaccount = resource[i].kcdaccount
						updateresources[i].samlssoprofile = resource[i].samlssoprofile
						updateresources[i].proxy = resource[i].proxy
						updateresources[i].userexpression = resource[i].userexpression
						updateresources[i].passwdexpression = resource[i].passwdexpression
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of vpntrafficaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpntrafficaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpntrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpntrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the vpntrafficaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpntrafficaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = vpntrafficaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [vpntrafficaction() for _ in range(len(name))]
							obj = [vpntrafficaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = vpntrafficaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of vpntrafficaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpntrafficaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the vpntrafficaction resources configured on NetScaler.
		"""
		try :
			obj = vpntrafficaction()
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
		ur""" Use this API to count filtered the set of vpntrafficaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpntrafficaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Qual:
		http = "http"
		tcp = "tcp"

	class Wanscaler:
		ON = "ON"
		OFF = "OFF"

	class Hdx:
		ON = "ON"
		OFF = "OFF"

	class Fta:
		ON = "ON"
		OFF = "OFF"

	class Sso:
		ON = "ON"
		OFF = "OFF"

class vpntrafficaction_response(base_response) :
	def __init__(self, length=1) :
		self.vpntrafficaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpntrafficaction = [vpntrafficaction() for _ in range(length)]

