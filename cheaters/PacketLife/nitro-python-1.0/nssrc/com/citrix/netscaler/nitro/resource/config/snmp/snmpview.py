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

class snmpview(base_resource) :
	""" Configuration for view resource. """
	def __init__(self) :
		self._name = ""
		self._subtree = ""
		self._type = ""
		self._storagetype = ""
		self._status = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the SNMPv3 view. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a name that helps identify the SNMPv3 view.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my view" or 'my view').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the SNMPv3 view. Can consist of 1 to 31 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a name that helps identify the SNMPv3 view.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my view" or 'my view').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def subtree(self) :
		ur"""A particular branch (subtree) of the MIB tree that you want to associate with this SNMPv3 view. You must specify the subtree as an SNMP OID.<br/>Minimum length =  1.
		"""
		try :
			return self._subtree
		except Exception as e:
			raise e

	@subtree.setter
	def subtree(self, subtree) :
		ur"""A particular branch (subtree) of the MIB tree that you want to associate with this SNMPv3 view. You must specify the subtree as an SNMP OID.<br/>Minimum length =  1
		"""
		try :
			self._subtree = subtree
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Include or exclude the subtree, specified by the subtree parameter, in or from this view. This setting can be useful when you have included a subtree, such as A, in an SNMPv3 view and you want to exclude a specific subtree of A, such as B, from the SNMPv3 view.<br/>Possible values = included, excluded.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Include or exclude the subtree, specified by the subtree parameter, in or from this view. This setting can be useful when you have included a subtree, such as A, in an SNMPv3 view and you want to exclude a specific subtree of A, such as B, from the SNMPv3 view.<br/>Possible values = included, excluded
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def storagetype(self) :
		ur"""The storage type for this view.<br/>Possible values = volatile, nonVolatile.
		"""
		try :
			return self._storagetype
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""The status of this view.<br/>Possible values = active.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmpview_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmpview
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
		ur""" Use this API to add snmpview.
		"""
		try :
			if type(resource) is not list :
				addresource = snmpview()
				addresource.name = resource.name
				addresource.subtree = resource.subtree
				addresource.type = resource.type
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ snmpview() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].subtree = resource[i].subtree
						addresources[i].type = resource[i].type
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete snmpview.
		"""
		try :
			if type(resource) is not list :
				deleteresource = snmpview()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
					deleteresource.subtree = resource.subtree
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ snmpview() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ snmpview() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
							deleteresources[i].subtree = resource[i].subtree
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update snmpview.
		"""
		try :
			if type(resource) is not list :
				updateresource = snmpview()
				updateresource.name = resource.name
				updateresource.subtree = resource.subtree
				updateresource.type = resource.type
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ snmpview() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].subtree = resource[i].subtree
						updateresources[i].type = resource[i].type
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the snmpview resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = snmpview()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [snmpview() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of snmpview resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpview()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the snmpview resources configured on NetScaler.
		"""
		try :
			obj = snmpview()
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
		ur""" Use this API to count filtered the set of snmpview resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpview()
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

	class Type:
		included = "included"
		excluded = "excluded"

	class Status:
		active = "active"

class snmpview_response(base_response) :
	def __init__(self, length=1) :
		self.snmpview = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmpview = [snmpview() for _ in range(length)]

