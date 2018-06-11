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

class authenticationtacacsaction(base_resource) :
	""" Configuration for TACACS action resource. """
	def __init__(self) :
		self._name = ""
		self._serverip = ""
		self._serverport = 0
		self._authtimeout = 0
		self._tacacssecret = ""
		self._authorization = ""
		self._accounting = ""
		self._auditfailedcmds = ""
		self._defaultauthenticationgroup = ""
		self._success = 0
		self._failure = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the TACACS+ profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after TACACS profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the TACACS+ profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after TACACS profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		ur"""IP address assigned to the TACACS+ server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		ur"""IP address assigned to the TACACS+ server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		ur"""Port number on which the TACACS+ server listens for connections.<br/>Default value: 49<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		ur"""Port number on which the TACACS+ server listens for connections.<br/>Default value: 49<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def authtimeout(self) :
		ur"""Number of seconds the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1.
		"""
		try :
			return self._authtimeout
		except Exception as e:
			raise e

	@authtimeout.setter
	def authtimeout(self, authtimeout) :
		ur"""Number of seconds the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1
		"""
		try :
			self._authtimeout = authtimeout
		except Exception as e:
			raise e

	@property
	def tacacssecret(self) :
		ur"""Key shared between the TACACS+ server and the NetScaler appliance. 
		Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1.
		"""
		try :
			return self._tacacssecret
		except Exception as e:
			raise e

	@tacacssecret.setter
	def tacacssecret(self, tacacssecret) :
		ur"""Key shared between the TACACS+ server and the NetScaler appliance. 
		Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1
		"""
		try :
			self._tacacssecret = tacacssecret
		except Exception as e:
			raise e

	@property
	def authorization(self) :
		ur"""Use streaming authorization on the TACACS+ server.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authorization
		except Exception as e:
			raise e

	@authorization.setter
	def authorization(self, authorization) :
		ur"""Use streaming authorization on the TACACS+ server.<br/>Possible values = ON, OFF
		"""
		try :
			self._authorization = authorization
		except Exception as e:
			raise e

	@property
	def accounting(self) :
		ur"""Whether the TACACS+ server is currently accepting accounting messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._accounting
		except Exception as e:
			raise e

	@accounting.setter
	def accounting(self, accounting) :
		ur"""Whether the TACACS+ server is currently accepting accounting messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._accounting = accounting
		except Exception as e:
			raise e

	@property
	def auditfailedcmds(self) :
		ur"""The state of the TACACS+ server that will receive accounting messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._auditfailedcmds
		except Exception as e:
			raise e

	@auditfailedcmds.setter
	def auditfailedcmds(self, auditfailedcmds) :
		ur"""The state of the TACACS+ server that will receive accounting messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._auditfailedcmds = auditfailedcmds
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		ur"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		ur"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def success(self) :
		try :
			return self._success
		except Exception as e:
			raise e

	@property
	def failure(self) :
		try :
			return self._failure
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationtacacsaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationtacacsaction
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
		ur""" Use this API to add authenticationtacacsaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationtacacsaction()
				addresource.name = resource.name
				addresource.serverip = resource.serverip
				addresource.serverport = resource.serverport
				addresource.authtimeout = resource.authtimeout
				addresource.tacacssecret = resource.tacacssecret
				addresource.authorization = resource.authorization
				addresource.accounting = resource.accounting
				addresource.auditfailedcmds = resource.auditfailedcmds
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationtacacsaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].serverip = resource[i].serverip
						addresources[i].serverport = resource[i].serverport
						addresources[i].authtimeout = resource[i].authtimeout
						addresources[i].tacacssecret = resource[i].tacacssecret
						addresources[i].authorization = resource[i].authorization
						addresources[i].accounting = resource[i].accounting
						addresources[i].auditfailedcmds = resource[i].auditfailedcmds
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete authenticationtacacsaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationtacacsaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update authenticationtacacsaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationtacacsaction()
				updateresource.name = resource.name
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.authtimeout = resource.authtimeout
				updateresource.tacacssecret = resource.tacacssecret
				updateresource.authorization = resource.authorization
				updateresource.accounting = resource.accounting
				updateresource.auditfailedcmds = resource.auditfailedcmds
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationtacacsaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].serverip = resource[i].serverip
						updateresources[i].serverport = resource[i].serverport
						updateresources[i].authtimeout = resource[i].authtimeout
						updateresources[i].tacacssecret = resource[i].tacacssecret
						updateresources[i].authorization = resource[i].authorization
						updateresources[i].accounting = resource[i].accounting
						updateresources[i].auditfailedcmds = resource[i].auditfailedcmds
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of authenticationtacacsaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationtacacsaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the authenticationtacacsaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationtacacsaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = authenticationtacacsaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [authenticationtacacsaction() for _ in range(len(name))]
							obj = [authenticationtacacsaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = authenticationtacacsaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of authenticationtacacsaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationtacacsaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the authenticationtacacsaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationtacacsaction()
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
		ur""" Use this API to count filtered the set of authenticationtacacsaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationtacacsaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Auditfailedcmds:
		ON = "ON"
		OFF = "OFF"

	class Authorization:
		ON = "ON"
		OFF = "OFF"

	class Accounting:
		ON = "ON"
		OFF = "OFF"

class authenticationtacacsaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationtacacsaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationtacacsaction = [authenticationtacacsaction() for _ in range(length)]

