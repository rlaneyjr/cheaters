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

class authenticationradiusaction(base_resource) :
	""" Configuration for RADIUS action resource. """
	def __init__(self) :
		self._name = ""
		self._serverip = ""
		self._servername = ""
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
		self._ipaddress = ""
		self._success = 0
		self._failure = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the RADIUS action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the RADIUS action is added.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the RADIUS action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the RADIUS action is added.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		ur"""IP address assigned to the RADIUS server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		ur"""IP address assigned to the RADIUS server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def servername(self) :
		ur"""RADIUS server name as a FQDN.  Mutually exclusive with RADIUS IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		ur"""RADIUS server name as a FQDN.  Mutually exclusive with RADIUS IP address.<br/>Minimum length =  1
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		ur"""Port number on which the RADIUS server listens for connections.<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		ur"""Port number on which the RADIUS server listens for connections.<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def authtimeout(self) :
		ur"""Number of seconds the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1.
		"""
		try :
			return self._authtimeout
		except Exception as e:
			raise e

	@authtimeout.setter
	def authtimeout(self, authtimeout) :
		ur"""Number of seconds the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1
		"""
		try :
			self._authtimeout = authtimeout
		except Exception as e:
			raise e

	@property
	def radkey(self) :
		ur"""Key shared between the RADIUS server and the NetScaler appliance. 
		Required to allow the NetScaler appliance to communicate with the RADIUS server.<br/>Minimum length =  1.
		"""
		try :
			return self._radkey
		except Exception as e:
			raise e

	@radkey.setter
	def radkey(self, radkey) :
		ur"""Key shared between the RADIUS server and the NetScaler appliance. 
		Required to allow the NetScaler appliance to communicate with the RADIUS server.<br/>Minimum length =  1
		"""
		try :
			self._radkey = radkey
		except Exception as e:
			raise e

	@property
	def radnasip(self) :
		ur"""If enabled, the NetScaler appliance IP address (NSIP) is sent to the RADIUS server as the  Network Access Server IP (NASIP) address. 
		The RADIUS protocol defines the meaning and use of the NASIP address.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._radnasip
		except Exception as e:
			raise e

	@radnasip.setter
	def radnasip(self, radnasip) :
		ur"""If enabled, the NetScaler appliance IP address (NSIP) is sent to the RADIUS server as the  Network Access Server IP (NASIP) address. 
		The RADIUS protocol defines the meaning and use of the NASIP address.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._radnasip = radnasip
		except Exception as e:
			raise e

	@property
	def radnasid(self) :
		ur"""If configured, this string is sent to the RADIUS server as the Network Access Server ID (NASID).
		"""
		try :
			return self._radnasid
		except Exception as e:
			raise e

	@radnasid.setter
	def radnasid(self, radnasid) :
		ur"""If configured, this string is sent to the RADIUS server as the Network Access Server ID (NASID).
		"""
		try :
			self._radnasid = radnasid
		except Exception as e:
			raise e

	@property
	def radvendorid(self) :
		ur"""RADIUS vendor ID attribute, used for RADIUS group extraction.<br/>Minimum length =  1.
		"""
		try :
			return self._radvendorid
		except Exception as e:
			raise e

	@radvendorid.setter
	def radvendorid(self, radvendorid) :
		ur"""RADIUS vendor ID attribute, used for RADIUS group extraction.<br/>Minimum length =  1
		"""
		try :
			self._radvendorid = radvendorid
		except Exception as e:
			raise e

	@property
	def radattributetype(self) :
		ur"""RADIUS attribute type, used for RADIUS group extraction.<br/>Minimum length =  1.
		"""
		try :
			return self._radattributetype
		except Exception as e:
			raise e

	@radattributetype.setter
	def radattributetype(self, radattributetype) :
		ur"""RADIUS attribute type, used for RADIUS group extraction.<br/>Minimum length =  1
		"""
		try :
			self._radattributetype = radattributetype
		except Exception as e:
			raise e

	@property
	def radgroupsprefix(self) :
		ur"""RADIUS groups prefix string. 
		This groups prefix precedes the group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			return self._radgroupsprefix
		except Exception as e:
			raise e

	@radgroupsprefix.setter
	def radgroupsprefix(self, radgroupsprefix) :
		ur"""RADIUS groups prefix string. 
		This groups prefix precedes the group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			self._radgroupsprefix = radgroupsprefix
		except Exception as e:
			raise e

	@property
	def radgroupseparator(self) :
		ur"""RADIUS group separator string
		The group separator delimits group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			return self._radgroupseparator
		except Exception as e:
			raise e

	@radgroupseparator.setter
	def radgroupseparator(self, radgroupseparator) :
		ur"""RADIUS group separator string
		The group separator delimits group names within a RADIUS attribute for RADIUS group extraction.
		"""
		try :
			self._radgroupseparator = radgroupseparator
		except Exception as e:
			raise e

	@property
	def passencoding(self) :
		ur"""Encoding type for passwords in RADIUS packets that the NetScaler appliance sends to the RADIUS server.<br/>Default value: pap<br/>Possible values = pap, chap, mschapv1, mschapv2.
		"""
		try :
			return self._passencoding
		except Exception as e:
			raise e

	@passencoding.setter
	def passencoding(self, passencoding) :
		ur"""Encoding type for passwords in RADIUS packets that the NetScaler appliance sends to the RADIUS server.<br/>Default value: pap<br/>Possible values = pap, chap, mschapv1, mschapv2
		"""
		try :
			self._passencoding = passencoding
		except Exception as e:
			raise e

	@property
	def ipvendorid(self) :
		ur"""Vendor ID of the intranet IP attribute in the RADIUS response.
		NOTE: A value of 0 indicates that the attribute is not vendor encoded.
		"""
		try :
			return self._ipvendorid
		except Exception as e:
			raise e

	@ipvendorid.setter
	def ipvendorid(self, ipvendorid) :
		ur"""Vendor ID of the intranet IP attribute in the RADIUS response.
		NOTE: A value of 0 indicates that the attribute is not vendor encoded.
		"""
		try :
			self._ipvendorid = ipvendorid
		except Exception as e:
			raise e

	@property
	def ipattributetype(self) :
		ur"""Remote IP address attribute type in a RADIUS response.<br/>Minimum length =  1.
		"""
		try :
			return self._ipattributetype
		except Exception as e:
			raise e

	@ipattributetype.setter
	def ipattributetype(self, ipattributetype) :
		ur"""Remote IP address attribute type in a RADIUS response.<br/>Minimum length =  1
		"""
		try :
			self._ipattributetype = ipattributetype
		except Exception as e:
			raise e

	@property
	def accounting(self) :
		ur"""Whether the RADIUS server is currently accepting accounting messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._accounting
		except Exception as e:
			raise e

	@accounting.setter
	def accounting(self, accounting) :
		ur"""Whether the RADIUS server is currently accepting accounting messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._accounting = accounting
		except Exception as e:
			raise e

	@property
	def pwdvendorid(self) :
		ur"""Vendor ID of the attribute, in the RADIUS response, used to extract the user password.<br/>Minimum length =  1.
		"""
		try :
			return self._pwdvendorid
		except Exception as e:
			raise e

	@pwdvendorid.setter
	def pwdvendorid(self, pwdvendorid) :
		ur"""Vendor ID of the attribute, in the RADIUS response, used to extract the user password.<br/>Minimum length =  1
		"""
		try :
			self._pwdvendorid = pwdvendorid
		except Exception as e:
			raise e

	@property
	def pwdattributetype(self) :
		ur"""Vendor-specific password attribute type in a RADIUS response.<br/>Minimum length =  1.
		"""
		try :
			return self._pwdattributetype
		except Exception as e:
			raise e

	@pwdattributetype.setter
	def pwdattributetype(self, pwdattributetype) :
		ur"""Vendor-specific password attribute type in a RADIUS response.<br/>Minimum length =  1
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
	def ipaddress(self) :
		ur"""IP address.
		"""
		try :
			return self._ipaddress
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
			result = service.payload_formatter.string_to_resource(authenticationradiusaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationradiusaction
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
		ur""" Use this API to add authenticationradiusaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationradiusaction()
				addresource.name = resource.name
				addresource.serverip = resource.serverip
				addresource.servername = resource.servername
				addresource.serverport = resource.serverport
				addresource.authtimeout = resource.authtimeout
				addresource.radkey = resource.radkey
				addresource.radnasip = resource.radnasip
				addresource.radnasid = resource.radnasid
				addresource.radvendorid = resource.radvendorid
				addresource.radattributetype = resource.radattributetype
				addresource.radgroupsprefix = resource.radgroupsprefix
				addresource.radgroupseparator = resource.radgroupseparator
				addresource.passencoding = resource.passencoding
				addresource.ipvendorid = resource.ipvendorid
				addresource.ipattributetype = resource.ipattributetype
				addresource.accounting = resource.accounting
				addresource.pwdvendorid = resource.pwdvendorid
				addresource.pwdattributetype = resource.pwdattributetype
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				addresource.callingstationid = resource.callingstationid
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationradiusaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].serverip = resource[i].serverip
						addresources[i].servername = resource[i].servername
						addresources[i].serverport = resource[i].serverport
						addresources[i].authtimeout = resource[i].authtimeout
						addresources[i].radkey = resource[i].radkey
						addresources[i].radnasip = resource[i].radnasip
						addresources[i].radnasid = resource[i].radnasid
						addresources[i].radvendorid = resource[i].radvendorid
						addresources[i].radattributetype = resource[i].radattributetype
						addresources[i].radgroupsprefix = resource[i].radgroupsprefix
						addresources[i].radgroupseparator = resource[i].radgroupseparator
						addresources[i].passencoding = resource[i].passencoding
						addresources[i].ipvendorid = resource[i].ipvendorid
						addresources[i].ipattributetype = resource[i].ipattributetype
						addresources[i].accounting = resource[i].accounting
						addresources[i].pwdvendorid = resource[i].pwdvendorid
						addresources[i].pwdattributetype = resource[i].pwdattributetype
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						addresources[i].callingstationid = resource[i].callingstationid
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete authenticationradiusaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationradiusaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationradiusaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationradiusaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update authenticationradiusaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationradiusaction()
				updateresource.name = resource.name
				updateresource.serverip = resource.serverip
				updateresource.servername = resource.servername
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
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationradiusaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].serverip = resource[i].serverip
						updateresources[i].servername = resource[i].servername
						updateresources[i].serverport = resource[i].serverport
						updateresources[i].authtimeout = resource[i].authtimeout
						updateresources[i].radkey = resource[i].radkey
						updateresources[i].radnasip = resource[i].radnasip
						updateresources[i].radnasid = resource[i].radnasid
						updateresources[i].radvendorid = resource[i].radvendorid
						updateresources[i].radattributetype = resource[i].radattributetype
						updateresources[i].radgroupsprefix = resource[i].radgroupsprefix
						updateresources[i].radgroupseparator = resource[i].radgroupseparator
						updateresources[i].passencoding = resource[i].passencoding
						updateresources[i].ipvendorid = resource[i].ipvendorid
						updateresources[i].ipattributetype = resource[i].ipattributetype
						updateresources[i].accounting = resource[i].accounting
						updateresources[i].pwdvendorid = resource[i].pwdvendorid
						updateresources[i].pwdattributetype = resource[i].pwdattributetype
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						updateresources[i].callingstationid = resource[i].callingstationid
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of authenticationradiusaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationradiusaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationradiusaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationradiusaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the authenticationradiusaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationradiusaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = authenticationradiusaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [authenticationradiusaction() for _ in range(len(name))]
							obj = [authenticationradiusaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = authenticationradiusaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of authenticationradiusaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationradiusaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the authenticationradiusaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationradiusaction()
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
		ur""" Use this API to count filtered the set of authenticationradiusaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationradiusaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
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

class authenticationradiusaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationradiusaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationradiusaction = [authenticationradiusaction() for _ in range(length)]

