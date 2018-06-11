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

class aaaradiusparams(base_resource) :
	""" Configuration for RADIUS parameter resource. """
	def __init__(self) :
		self._serverip = ""
		self._serverport = 0
		self._authtimeout = 0
		self._radkey = ""
		self._radnasip = ""
		self._radnasid = ""
		self._radvendorid = 0
		self._radattributetype = 0
		self._radgroupsprefix = ""
		self._radgroupseparator = ""
		self._passencoding = ""
		self._ipvendorid = 0
		self._ipattributetype = 0
		self._accounting = ""
		self._pwdvendorid = 0
		self._pwdattributetype = 0
		self._defaultauthenticationgroup = ""
		self._callingstationid = ""
		self._groupauthname = ""
		self._ipaddress = ""

	@property
	def serverip(self) :
		ur"""IP address of your RADIUS server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		ur"""IP address of your RADIUS server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		ur"""Port number on which the RADIUS server listens for connections.<br/>Default value: 1812<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		ur"""Port number on which the RADIUS server listens for connections.<br/>Default value: 1812<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def authtimeout(self) :
		ur"""Maximum number of seconds that the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1.
		"""
		try :
			return self._authtimeout
		except Exception as e:
			raise e

	@authtimeout.setter
	def authtimeout(self, authtimeout) :
		ur"""Maximum number of seconds that the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1
		"""
		try :
			self._authtimeout = authtimeout
		except Exception as e:
			raise e

	@property
	def radkey(self) :
		ur"""The key shared between the RADIUS server and clients. 
		Required for allowing the NetScaler appliance to communicate with the RADIUS server.<br/>Minimum length =  1.
		"""
		try :
			return self._radkey
		except Exception as e:
			raise e

	@radkey.setter
	def radkey(self, radkey) :
		ur"""The key shared between the RADIUS server and clients. 
		Required for allowing the NetScaler appliance to communicate with the RADIUS server.<br/>Minimum length =  1
		"""
		try :
			self._radkey = radkey
		except Exception as e:
			raise e

	@property
	def radnasip(self) :
		ur"""Send the NetScaler IP (NSIP) address to the RADIUS server as the Network Access Server IP (NASIP) part of the Radius protocol.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._radnasip
		except Exception as e:
			raise e

	@radnasip.setter
	def radnasip(self, radnasip) :
		ur"""Send the NetScaler IP (NSIP) address to the RADIUS server as the Network Access Server IP (NASIP) part of the Radius protocol.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._radnasip = radnasip
		except Exception as e:
			raise e

	@property
	def radnasid(self) :
		ur"""Send the Network Access Server ID (NASID) for your NetScaler appliance to the RADIUS server as the nasid part of the Radius protocol.
		"""
		try :
			return self._radnasid
		except Exception as e:
			raise e

	@radnasid.setter
	def radnasid(self, radnasid) :
		ur"""Send the Network Access Server ID (NASID) for your NetScaler appliance to the RADIUS server as the nasid part of the Radius protocol.
		"""
		try :
			self._radnasid = radnasid
		except Exception as e:
			raise e

	@property
	def radvendorid(self) :
		ur"""Vendor ID for RADIUS group extraction.<br/>Minimum length =  1.
		"""
		try :
			return self._radvendorid
		except Exception as e:
			raise e

	@radvendorid.setter
	def radvendorid(self, radvendorid) :
		ur"""Vendor ID for RADIUS group extraction.<br/>Minimum length =  1
		"""
		try :
			self._radvendorid = radvendorid
		except Exception as e:
			raise e

	@property
	def radattributetype(self) :
		ur"""Attribute type for RADIUS group extraction.<br/>Minimum length =  1.
		"""
		try :
			return self._radattributetype
		except Exception as e:
			raise e

	@radattributetype.setter
	def radattributetype(self, radattributetype) :
		ur"""Attribute type for RADIUS group extraction.<br/>Minimum length =  1
		"""
		try :
			self._radattributetype = radattributetype
		except Exception as e:
			raise e

	@property
	def radgroupsprefix(self) :
		ur"""Prefix string that precedes group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			return self._radgroupsprefix
		except Exception as e:
			raise e

	@radgroupsprefix.setter
	def radgroupsprefix(self, radgroupsprefix) :
		ur"""Prefix string that precedes group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			self._radgroupsprefix = radgroupsprefix
		except Exception as e:
			raise e

	@property
	def radgroupseparator(self) :
		ur"""Group separator string that delimits group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			return self._radgroupseparator
		except Exception as e:
			raise e

	@radgroupseparator.setter
	def radgroupseparator(self, radgroupseparator) :
		ur"""Group separator string that delimits group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			self._radgroupseparator = radgroupseparator
		except Exception as e:
			raise e

	@property
	def passencoding(self) :
		ur"""Enable password encoding in RADIUS packets that the NetScaler appliance sends to the RADIUS server.<br/>Default value: pap<br/>Possible values = pap, chap, mschapv1, mschapv2.
		"""
		try :
			return self._passencoding
		except Exception as e:
			raise e

	@passencoding.setter
	def passencoding(self, passencoding) :
		ur"""Enable password encoding in RADIUS packets that the NetScaler appliance sends to the RADIUS server.<br/>Default value: pap<br/>Possible values = pap, chap, mschapv1, mschapv2
		"""
		try :
			self._passencoding = passencoding
		except Exception as e:
			raise e

	@property
	def ipvendorid(self) :
		ur"""Vendor ID attribute in the RADIUS response. 
		If the attribute is not vendor-encoded, it is set to 0.
		"""
		try :
			return self._ipvendorid
		except Exception as e:
			raise e

	@ipvendorid.setter
	def ipvendorid(self, ipvendorid) :
		ur"""Vendor ID attribute in the RADIUS response. 
		If the attribute is not vendor-encoded, it is set to 0.
		"""
		try :
			self._ipvendorid = ipvendorid
		except Exception as e:
			raise e

	@property
	def ipattributetype(self) :
		ur"""IP attribute type in the RADIUS response.<br/>Minimum length =  1.
		"""
		try :
			return self._ipattributetype
		except Exception as e:
			raise e

	@ipattributetype.setter
	def ipattributetype(self, ipattributetype) :
		ur"""IP attribute type in the RADIUS response.<br/>Minimum length =  1
		"""
		try :
			self._ipattributetype = ipattributetype
		except Exception as e:
			raise e

	@property
	def accounting(self) :
		ur"""Configure the RADIUS server state to accept or refuse accounting messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._accounting
		except Exception as e:
			raise e

	@accounting.setter
	def accounting(self, accounting) :
		ur"""Configure the RADIUS server state to accept or refuse accounting messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._accounting = accounting
		except Exception as e:
			raise e

	@property
	def pwdvendorid(self) :
		ur"""Vendor ID of the password in the RADIUS response. Used to extract the user password.<br/>Minimum length =  1.
		"""
		try :
			return self._pwdvendorid
		except Exception as e:
			raise e

	@pwdvendorid.setter
	def pwdvendorid(self, pwdvendorid) :
		ur"""Vendor ID of the password in the RADIUS response. Used to extract the user password.<br/>Minimum length =  1
		"""
		try :
			self._pwdvendorid = pwdvendorid
		except Exception as e:
			raise e

	@property
	def pwdattributetype(self) :
		ur"""Attribute type of the Vendor ID in the RADIUS response.<br/>Minimum length =  1.
		"""
		try :
			return self._pwdattributetype
		except Exception as e:
			raise e

	@pwdattributetype.setter
	def pwdattributetype(self, pwdattributetype) :
		ur"""Attribute type of the Vendor ID in the RADIUS response.<br/>Minimum length =  1
		"""
		try :
			self._pwdattributetype = pwdattributetype
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
	def callingstationid(self) :
		ur"""Send Calling-Station-ID of the client to the RADIUS server. IP Address of the client is sent as its Calling-Station-ID.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._callingstationid
		except Exception as e:
			raise e

	@callingstationid.setter
	def callingstationid(self, callingstationid) :
		ur"""Send Calling-Station-ID of the client to the RADIUS server. IP Address of the client is sent as its Calling-Station-ID.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._callingstationid = callingstationid
		except Exception as e:
			raise e

	@property
	def groupauthname(self) :
		ur"""To associate AAA users with an AAA group, use the command
		"bind AAA group ... -username ...".
		You can bind different policies to each AAA group. Use the command
		"bind AAA group ... -policy ...".
		"""
		try :
			return self._groupauthname
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""IP Address.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaaradiusparams_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaaradiusparams
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
		ur""" Use this API to update aaaradiusparams.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaaradiusparams()
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.authtimeout = resource.authtimeout
				updateresource.radkey = resource.radkey
				updateresource.radnasip = resource.radnasip
				updateresource.radnasid = resource.radnasid
				updateresource.radvendorid = resource.radvendorid
				updateresource.radattributetype = resource.radattributetype
				updateresource.radgroupsprefix = resource.radgroupsprefix
				updateresource.radgroupseparator = resource.radgroupseparator
				updateresource.passencoding = resource.passencoding
				updateresource.ipvendorid = resource.ipvendorid
				updateresource.ipattributetype = resource.ipattributetype
				updateresource.accounting = resource.accounting
				updateresource.pwdvendorid = resource.pwdvendorid
				updateresource.pwdattributetype = resource.pwdattributetype
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.callingstationid = resource.callingstationid
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of aaaradiusparams resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaaradiusparams()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the aaaradiusparams resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaaradiusparams()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Passencoding:
		pap = "pap"
		chap = "chap"
		mschapv1 = "mschapv1"
		mschapv2 = "mschapv2"

	class Callingstationid:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Accounting:
		ON = "ON"
		OFF = "OFF"

	class Radnasip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class aaaradiusparams_response(base_response) :
	def __init__(self, length=1) :
		self.aaaradiusparams = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaaradiusparams = [aaaradiusparams() for _ in range(length)]

