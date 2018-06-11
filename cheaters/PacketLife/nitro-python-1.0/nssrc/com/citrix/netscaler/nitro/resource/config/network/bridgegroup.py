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

class bridgegroup(base_resource) :
	""" Configuration for bridge group resource. """
	def __init__(self) :
		self._id = 0
		self._ipv6dynamicrouting = ""
		self._flags = False
		self._portbitmap = 0
		self._tagbitmap = 0
		self._ifaces = ""
		self._tagifaces = ""
		self._rnat = False
		self.___count = 0

	@property
	def id(self) :
		ur"""An integer that uniquely identifies the bridge group.<br/>Minimum length =  1<br/>Maximum length =  1000.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""An integer that uniquely identifies the bridge group.<br/>Minimum length =  1<br/>Maximum length =  1000
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def ipv6dynamicrouting(self) :
		ur"""Enable all IPv6 dynamic routing protocols on all VLANs bound to this bridgegroup. Note: For the ENABLED setting to work, you must configure IPv6 dynamic routing protocols from the VTYSH command line.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ipv6dynamicrouting
		except Exception as e:
			raise e

	@ipv6dynamicrouting.setter
	def ipv6dynamicrouting(self, ipv6dynamicrouting) :
		ur"""Enable all IPv6 dynamic routing protocols on all VLANs bound to this bridgegroup. Note: For the ENABLED setting to work, you must configure IPv6 dynamic routing protocols from the VTYSH command line.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ipv6dynamicrouting = ipv6dynamicrouting
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""Temporary flag used for internal purpose.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def portbitmap(self) :
		ur"""Member interfaces of this  bridge group.
		"""
		try :
			return self._portbitmap
		except Exception as e:
			raise e

	@property
	def tagbitmap(self) :
		ur"""Tagged members of this  bridge group.
		"""
		try :
			return self._tagbitmap
		except Exception as e:
			raise e

	@property
	def ifaces(self) :
		ur"""Names of all member interfaces of this bridge group.
		"""
		try :
			return self._ifaces
		except Exception as e:
			raise e

	@property
	def tagifaces(self) :
		ur"""Names of all tagged member interfaces of this bridge group.
		"""
		try :
			return self._tagifaces
		except Exception as e:
			raise e

	@property
	def rnat(self) :
		ur"""Temporary flag used for internal purpose.
		"""
		try :
			return self._rnat
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(bridgegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bridgegroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add bridgegroup.
		"""
		try :
			if type(resource) is not list :
				addresource = bridgegroup()
				addresource.id = resource.id
				addresource.ipv6dynamicrouting = resource.ipv6dynamicrouting
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ bridgegroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].id = resource[i].id
						addresources[i].ipv6dynamicrouting = resource[i].ipv6dynamicrouting
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete bridgegroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = bridgegroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.id = resource
				else :
					deleteresource.id = resource.id
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ bridgegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ bridgegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i].id
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update bridgegroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = bridgegroup()
				updateresource.id = resource.id
				updateresource.ipv6dynamicrouting = resource.ipv6dynamicrouting
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ bridgegroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].ipv6dynamicrouting = resource[i].ipv6dynamicrouting
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of bridgegroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = bridgegroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.id = resource
				else :
					unsetresource.id = resource.id
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ bridgegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ bridgegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i].id
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the bridgegroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = bridgegroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = bridgegroup()
						obj.id = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [bridgegroup() for _ in range(len(name))]
							obj = [bridgegroup() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = bridgegroup()
								obj[i].id = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of bridgegroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = bridgegroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the bridgegroup resources configured on NetScaler.
		"""
		try :
			obj = bridgegroup()
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
		ur""" Use this API to count filtered the set of bridgegroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = bridgegroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Ipv6dynamicrouting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class bridgegroup_response(base_response) :
	def __init__(self, length=1) :
		self.bridgegroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.bridgegroup = [bridgegroup() for _ in range(length)]

