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

class snmpgroup(base_resource) :
	""" Configuration for SNMP group resource. """
	def __init__(self) :
		self._name = ""
		self._securitylevel = ""
		self._readviewname = ""
		self._storagetype = ""
		self._status = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the SNMPv3 group. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You should choose a name that helps identify the SNMPv3 group. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my name" or 'my name').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the SNMPv3 group. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You should choose a name that helps identify the SNMPv3 group. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my name" or 'my name').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def securitylevel(self) :
		ur"""Security level required for communication between the NetScaler appliance and the SNMPv3 users who belong to the group. Specify one of the following options:
		noAuthNoPriv. Require neither authentication nor encryption.
		authNoPriv. Require authentication but no encryption.
		authPriv. Require authentication and encryption.
		Note: If you specify authentication, you must specify an encryption algorithm when you assign an SNMPv3 user to the group. If you also specify encryption, you must assign both an authentication and an encryption algorithm for each group member.<br/>Possible values = noAuthNoPriv, authNoPriv, authPriv.
		"""
		try :
			return self._securitylevel
		except Exception as e:
			raise e

	@securitylevel.setter
	def securitylevel(self, securitylevel) :
		ur"""Security level required for communication between the NetScaler appliance and the SNMPv3 users who belong to the group. Specify one of the following options:
		noAuthNoPriv. Require neither authentication nor encryption.
		authNoPriv. Require authentication but no encryption.
		authPriv. Require authentication and encryption.
		Note: If you specify authentication, you must specify an encryption algorithm when you assign an SNMPv3 user to the group. If you also specify encryption, you must assign both an authentication and an encryption algorithm for each group member.<br/>Possible values = noAuthNoPriv, authNoPriv, authPriv
		"""
		try :
			self._securitylevel = securitylevel
		except Exception as e:
			raise e

	@property
	def readviewname(self) :
		ur"""Name of the configured SNMPv3 view that you want to bind to this SNMPv3 group. An SNMPv3 user bound to this group can access the subtrees that are bound to this SNMPv3 view as type INCLUDED, but cannot access the ones that are type EXCLUDED. If the NetScaler appliance has multiple SNMPv3 view entries with the same name, all such entries are associated with the SNMPv3 group.<br/>Minimum length =  1.
		"""
		try :
			return self._readviewname
		except Exception as e:
			raise e

	@readviewname.setter
	def readviewname(self, readviewname) :
		ur"""Name of the configured SNMPv3 view that you want to bind to this SNMPv3 group. An SNMPv3 user bound to this group can access the subtrees that are bound to this SNMPv3 view as type INCLUDED, but cannot access the ones that are type EXCLUDED. If the NetScaler appliance has multiple SNMPv3 view entries with the same name, all such entries are associated with the SNMPv3 group.<br/>Minimum length =  1
		"""
		try :
			self._readviewname = readviewname
		except Exception as e:
			raise e

	@property
	def storagetype(self) :
		ur"""The storage type for this group.<br/>Possible values = volatile, nonVolatile.
		"""
		try :
			return self._storagetype
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""The status of this group.<br/>Possible values = active.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmpgroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmpgroup
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
		ur""" Use this API to add snmpgroup.
		"""
		try :
			if type(resource) is not list :
				addresource = snmpgroup()
				addresource.name = resource.name
				addresource.securitylevel = resource.securitylevel
				addresource.readviewname = resource.readviewname
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ snmpgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].securitylevel = resource[i].securitylevel
						addresources[i].readviewname = resource[i].readviewname
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete snmpgroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = snmpgroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
					deleteresource.securitylevel = resource.securitylevel
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ snmpgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ snmpgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
							deleteresources[i].securitylevel = resource[i].securitylevel
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update snmpgroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = snmpgroup()
				updateresource.name = resource.name
				updateresource.securitylevel = resource.securitylevel
				updateresource.readviewname = resource.readviewname
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ snmpgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].securitylevel = resource[i].securitylevel
						updateresources[i].readviewname = resource[i].readviewname
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the snmpgroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = snmpgroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [snmpgroup() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of snmpgroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpgroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the snmpgroup resources configured on NetScaler.
		"""
		try :
			obj = snmpgroup()
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
		ur""" Use this API to count filtered the set of snmpgroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpgroup()
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

	class Securitylevel:
		noAuthNoPriv = "noAuthNoPriv"
		authNoPriv = "authNoPriv"
		authPriv = "authPriv"

	class Status:
		active = "active"

class snmpgroup_response(base_response) :
	def __init__(self, length=1) :
		self.snmpgroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmpgroup = [snmpgroup() for _ in range(length)]

