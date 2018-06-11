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

class snmpuser(base_resource) :
	""" Configuration for SNMP user resource. """
	def __init__(self) :
		self._name = ""
		self._group = ""
		self._authtype = ""
		self._authpasswd = ""
		self._privtype = ""
		self._privpasswd = ""
		self._engineid = ""
		self._storagetype = ""
		self._status = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the SNMPv3 user. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my user" or 'my user').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the SNMPv3 user. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my user" or 'my user').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def group(self) :
		ur"""Name of the configured SNMPv3 group to which to bind this SNMPv3 user. The access rights (bound SNMPv3 views) and security level set for this group are assigned to this user.<br/>Minimum length =  1.
		"""
		try :
			return self._group
		except Exception as e:
			raise e

	@group.setter
	def group(self, group) :
		ur"""Name of the configured SNMPv3 group to which to bind this SNMPv3 user. The access rights (bound SNMPv3 views) and security level set for this group are assigned to this user.<br/>Minimum length =  1
		"""
		try :
			self._group = group
		except Exception as e:
			raise e

	@property
	def authtype(self) :
		ur"""Authentication algorithm used by the NetScaler appliance and the SNMPv3 user for authenticating the communication between them. You must specify the same authentication algorithm when you configure the SNMPv3 user in the SNMP manager.<br/>Possible values = MD5, SHA.
		"""
		try :
			return self._authtype
		except Exception as e:
			raise e

	@authtype.setter
	def authtype(self, authtype) :
		ur"""Authentication algorithm used by the NetScaler appliance and the SNMPv3 user for authenticating the communication between them. You must specify the same authentication algorithm when you configure the SNMPv3 user in the SNMP manager.<br/>Possible values = MD5, SHA
		"""
		try :
			self._authtype = authtype
		except Exception as e:
			raise e

	@property
	def authpasswd(self) :
		ur"""Plain-text pass phrase to be used by the authentication algorithm specified by the authType (Authentication Type) parameter. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the pass phrase includes one or more spaces, enclose it in double or single quotation marks (for example, "my phrase" or 'my phrase').<br/>Minimum length =  8.
		"""
		try :
			return self._authpasswd
		except Exception as e:
			raise e

	@authpasswd.setter
	def authpasswd(self, authpasswd) :
		ur"""Plain-text pass phrase to be used by the authentication algorithm specified by the authType (Authentication Type) parameter. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the pass phrase includes one or more spaces, enclose it in double or single quotation marks (for example, "my phrase" or 'my phrase').<br/>Minimum length =  8
		"""
		try :
			self._authpasswd = authpasswd
		except Exception as e:
			raise e

	@property
	def privtype(self) :
		ur"""Encryption algorithm used by the NetScaler appliance and the SNMPv3 user for encrypting the communication between them. You must specify the same encryption algorithm when you configure the SNMPv3 user in the SNMP manager.<br/>Possible values = DES, AES.
		"""
		try :
			return self._privtype
		except Exception as e:
			raise e

	@privtype.setter
	def privtype(self, privtype) :
		ur"""Encryption algorithm used by the NetScaler appliance and the SNMPv3 user for encrypting the communication between them. You must specify the same encryption algorithm when you configure the SNMPv3 user in the SNMP manager.<br/>Possible values = DES, AES
		"""
		try :
			self._privtype = privtype
		except Exception as e:
			raise e

	@property
	def privpasswd(self) :
		ur"""Encryption key to be used by the encryption algorithm specified by the privType (Encryption Type) parameter. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the key includes one or more spaces, enclose it in double or single quotation marks (for example, "my key" or 'my key').<br/>Minimum length =  8.
		"""
		try :
			return self._privpasswd
		except Exception as e:
			raise e

	@privpasswd.setter
	def privpasswd(self, privpasswd) :
		ur"""Encryption key to be used by the encryption algorithm specified by the privType (Encryption Type) parameter. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the key includes one or more spaces, enclose it in double or single quotation marks (for example, "my key" or 'my key').<br/>Minimum length =  8
		"""
		try :
			self._privpasswd = privpasswd
		except Exception as e:
			raise e

	@property
	def engineid(self) :
		ur"""The context engine ID of the user.
		"""
		try :
			return self._engineid
		except Exception as e:
			raise e

	@property
	def storagetype(self) :
		ur"""The storage type for this user.<br/>Possible values = volatile, nonVolatile.
		"""
		try :
			return self._storagetype
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""The status of this user.<br/>Possible values = active.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmpuser_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmpuser
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
		ur""" Use this API to add snmpuser.
		"""
		try :
			if type(resource) is not list :
				addresource = snmpuser()
				addresource.name = resource.name
				addresource.group = resource.group
				addresource.authtype = resource.authtype
				addresource.authpasswd = resource.authpasswd
				addresource.privtype = resource.privtype
				addresource.privpasswd = resource.privpasswd
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ snmpuser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].group = resource[i].group
						addresources[i].authtype = resource[i].authtype
						addresources[i].authpasswd = resource[i].authpasswd
						addresources[i].privtype = resource[i].privtype
						addresources[i].privpasswd = resource[i].privpasswd
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete snmpuser.
		"""
		try :
			if type(resource) is not list :
				deleteresource = snmpuser()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ snmpuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ snmpuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update snmpuser.
		"""
		try :
			if type(resource) is not list :
				updateresource = snmpuser()
				updateresource.name = resource.name
				updateresource.group = resource.group
				updateresource.authtype = resource.authtype
				updateresource.authpasswd = resource.authpasswd
				updateresource.privtype = resource.privtype
				updateresource.privpasswd = resource.privpasswd
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ snmpuser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].group = resource[i].group
						updateresources[i].authtype = resource[i].authtype
						updateresources[i].authpasswd = resource[i].authpasswd
						updateresources[i].privtype = resource[i].privtype
						updateresources[i].privpasswd = resource[i].privpasswd
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of snmpuser resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = snmpuser()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ snmpuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ snmpuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the snmpuser resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = snmpuser()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = snmpuser()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [snmpuser() for _ in range(len(name))]
							obj = [snmpuser() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = snmpuser()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of snmpuser resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpuser()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the snmpuser resources configured on NetScaler.
		"""
		try :
			obj = snmpuser()
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
		ur""" Use this API to count filtered the set of snmpuser resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpuser()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Storagetype:
		Volatile = "volatile"
		nonVolatile = "nonVolatile"

	class Authtype:
		MD5 = "MD5"
		SHA = "SHA"

	class Status:
		active = "active"

	class Privtype:
		DES = "DES"
		AES = "AES"

class snmpuser_response(base_response) :
	def __init__(self, length=1) :
		self.snmpuser = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmpuser = [snmpuser() for _ in range(length)]

