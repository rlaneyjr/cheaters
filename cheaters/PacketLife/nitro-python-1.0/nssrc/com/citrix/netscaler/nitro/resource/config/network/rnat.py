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

class rnat(base_resource) :
	""" Configuration for RNAT configured route resource. """
	def __init__(self) :
		self._network = ""
		self._netmask = ""
		self._aclname = ""
		self._redirectport = False
		self._natip = ""
		self._td = 0
		self._natip2 = ""
		self._srcippersistency = ""
		self.___count = 0

	@property
	def network(self) :
		ur"""The network address defined for the RNAT entry.<br/>Minimum length =  1.
		"""
		try :
			return self._network
		except Exception as e:
			raise e

	@network.setter
	def network(self, network) :
		ur"""The network address defined for the RNAT entry.<br/>Minimum length =  1
		"""
		try :
			self._network = network
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""The subnet mask for the network address.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""The subnet mask for the network address.<br/>Minimum length =  1
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def aclname(self) :
		ur"""An extended ACL defined for the RNAT entry.<br/>Minimum length =  1.
		"""
		try :
			return self._aclname
		except Exception as e:
			raise e

	@aclname.setter
	def aclname(self, aclname) :
		ur"""An extended ACL defined for the RNAT entry.<br/>Minimum length =  1
		"""
		try :
			self._aclname = aclname
		except Exception as e:
			raise e

	@property
	def redirectport(self) :
		ur"""The port number to which the packets are redirected.
		"""
		try :
			return self._redirectport
		except Exception as e:
			raise e

	@redirectport.setter
	def redirectport(self, redirectport) :
		ur"""The port number to which the packets are redirected.
		"""
		try :
			self._redirectport = redirectport
		except Exception as e:
			raise e

	@property
	def natip(self) :
		ur"""The NAT IP address defined for the RNAT entry. .<br/>Minimum length =  1.
		"""
		try :
			return self._natip
		except Exception as e:
			raise e

	@natip.setter
	def natip(self, natip) :
		ur"""The NAT IP address defined for the RNAT entry. .<br/>Minimum length =  1
		"""
		try :
			self._natip = natip
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def natip2(self) :
		ur"""The NAT IP(s) assigned to the RNAT.<br/>Minimum length =  1.
		"""
		try :
			return self._natip2
		except Exception as e:
			raise e

	@natip2.setter
	def natip2(self, natip2) :
		ur"""The NAT IP(s) assigned to the RNAT.<br/>Minimum length =  1
		"""
		try :
			self._natip2 = natip2
		except Exception as e:
			raise e

	@property
	def srcippersistency(self) :
		ur"""Enables the NetScaler appliance to use the same NAT IP address for all RNAT sessions initiated from a particular server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._srcippersistency
		except Exception as e:
			raise e

	@srcippersistency.setter
	def srcippersistency(self, srcippersistency) :
		ur"""Enables the NetScaler appliance to use the same NAT IP address for all RNAT sessions initiated from a particular server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._srcippersistency = srcippersistency
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rnat_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rnat
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
	def clear(cls, client, resource) :
		ur""" Use this API to clear rnat.
		"""
		try :
			if type(resource) is not list :
				clearresource = rnat()
				clearresource.network = resource.network
				clearresource.netmask = resource.netmask
				clearresource.aclname = resource.aclname
				clearresource.redirectport = resource.redirectport
				clearresource.natip = resource.natip
				clearresource.td = resource.td
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ rnat() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].network = resource[i].network
						clearresources[i].netmask = resource[i].netmask
						clearresources[i].aclname = resource[i].aclname
						clearresources[i].redirectport = resource[i].redirectport
						clearresources[i].natip = resource[i].natip
						clearresources[i].td = resource[i].td
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update rnat.
		"""
		try :
			if type(resource) is not list :
				updateresource = rnat()
				updateresource.network = resource.network
				updateresource.netmask = resource.netmask
				updateresource.natip = resource.natip
				updateresource.td = resource.td
				updateresource.aclname = resource.aclname
				updateresource.redirectport = resource.redirectport
				updateresource.natip2 = resource.natip2
				updateresource.srcippersistency = resource.srcippersistency
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ rnat() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].network = resource[i].network
						updateresources[i].netmask = resource[i].netmask
						updateresources[i].natip = resource[i].natip
						updateresources[i].td = resource[i].td
						updateresources[i].aclname = resource[i].aclname
						updateresources[i].redirectport = resource[i].redirectport
						updateresources[i].natip2 = resource[i].natip2
						updateresources[i].srcippersistency = resource[i].srcippersistency
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of rnat resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = rnat()
				unsetresource.network = resource.network
				unsetresource.netmask = resource.netmask
				unsetresource.td = resource.td
				unsetresource.aclname = resource.aclname
				unsetresource.redirectport = resource.redirectport
				unsetresource.natip = resource.natip
				return unsetresource.unset_resource(client, args)
			else :
				if (resource and len(resource) > 0) :
					unsetresources = [ rnat() for _ in range(len(resource))]
					for i in range(len(resource)) :
						unsetresources[i].network = resource[i].network
						unsetresources[i].netmask = resource[i].netmask
						unsetresources[i].td = resource[i].td
						unsetresources[i].aclname = resource[i].aclname
						unsetresources[i].redirectport = resource[i].redirectport
						unsetresources[i].natip = resource[i].natip
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the rnat resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rnat()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of rnat resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rnat()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the rnat resources configured on NetScaler.
		"""
		try :
			obj = rnat()
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
		ur""" Use this API to count filtered the set of rnat resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rnat()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Srcippersistency:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class rnat_response(base_response) :
	def __init__(self, length=1) :
		self.rnat = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rnat = [rnat() for _ in range(length)]

