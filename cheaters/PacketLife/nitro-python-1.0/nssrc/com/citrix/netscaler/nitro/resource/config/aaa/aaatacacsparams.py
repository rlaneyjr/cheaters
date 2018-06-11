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

class aaatacacsparams(base_resource) :
	""" Configuration for tacacs parameters resource. """
	def __init__(self) :
		self._serverip = ""
		self._serverport = 0
		self._authtimeout = 0
		self._tacacssecret = ""
		self._authorization = ""
		self._accounting = ""
		self._auditfailedcmds = ""
		self._defaultauthenticationgroup = ""

	@property
	def serverip(self) :
		ur"""IP address of your TACACS+ server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		ur"""IP address of your TACACS+ server.<br/>Minimum length =  1
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
		ur"""Maximum number of seconds that the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1.
		"""
		try :
			return self._authtimeout
		except Exception as e:
			raise e

	@authtimeout.setter
	def authtimeout(self, authtimeout) :
		ur"""Maximum number of seconds that the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1
		"""
		try :
			self._authtimeout = authtimeout
		except Exception as e:
			raise e

	@property
	def tacacssecret(self) :
		ur"""Key shared between the TACACS+ server and clients. Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1.
		"""
		try :
			return self._tacacssecret
		except Exception as e:
			raise e

	@tacacssecret.setter
	def tacacssecret(self, tacacssecret) :
		ur"""Key shared between the TACACS+ server and clients. Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1
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
		ur"""Send accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._accounting
		except Exception as e:
			raise e

	@accounting.setter
	def accounting(self, accounting) :
		ur"""Send accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF
		"""
		try :
			self._accounting = accounting
		except Exception as e:
			raise e

	@property
	def auditfailedcmds(self) :
		ur"""The option for sending accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._auditfailedcmds
		except Exception as e:
			raise e

	@auditfailedcmds.setter
	def auditfailedcmds(self, auditfailedcmds) :
		ur"""The option for sending accounting messages to the TACACS+ server.<br/>Possible values = ON, OFF
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

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaatacacsparams_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaatacacsparams
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
		ur""" Use this API to update aaatacacsparams.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaatacacsparams()
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.authtimeout = resource.authtimeout
				updateresource.tacacssecret = resource.tacacssecret
				updateresource.authorization = resource.authorization
				updateresource.accounting = resource.accounting
				updateresource.auditfailedcmds = resource.auditfailedcmds
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of aaatacacsparams resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaatacacsparams()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the aaatacacsparams resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaatacacsparams()
				response = obj.get_resources(client, option_)
			return response
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

class aaatacacsparams_response(base_response) :
	def __init__(self, length=1) :
		self.aaatacacsparams = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaatacacsparams = [aaatacacsparams() for _ in range(length)]

