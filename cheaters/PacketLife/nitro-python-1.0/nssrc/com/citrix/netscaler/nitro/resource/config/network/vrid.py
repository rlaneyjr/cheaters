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

class vrid(base_resource) :
	""" Configuration for Virtual Router ID resource. """
	def __init__(self) :
		self._id = 0
		self._priority = 0
		self._preemption = ""
		self._sharing = ""
		self._tracking = ""
		self._ownernode = 0
		self._all = False
		self._ifaces = ""
		self._type = ""
		self._effectivepriority = 0
		self._flags = 0
		self._ipaddress = ""
		self._state = 0
		self._operationalownernode = 0
		self.___count = 0

	@property
	def id(self) :
		ur"""Integer that uniquely identifies the VMAC address. The generic VMAC address is in the form of 00:00:5e:00:01:<VRID>. For example, if you add a VRID with a value of 60 and bind it to an interface, the resulting VMAC address is 00:00:5e:00:01:3c, where 3c is the hexadecimal representation of 60.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""Integer that uniquely identifies the VMAC address. The generic VMAC address is in the form of 00:00:5e:00:01:<VRID>. For example, if you add a VRID with a value of 60 and bind it to an interface, the resulting VMAC address is 00:00:5e:00:01:3c, where 3c is the hexadecimal representation of 60.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Base priority (BP), in an active-active mode configuration, which ordinarily determines the master VIP address.<br/>Default value: 255<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Base priority (BP), in an active-active mode configuration, which ordinarily determines the master VIP address.<br/>Default value: 255<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def preemption(self) :
		ur"""In an active-active mode configuration, make a backup VIP address the master if its priority becomes higher than that of a master VIP address bound to this VMAC address. 
		If you disable pre-emption while a backup VIP address is the master, the backup VIP address remains master until the original master VIP's priority becomes higher than that of the current master.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._preemption
		except Exception as e:
			raise e

	@preemption.setter
	def preemption(self, preemption) :
		ur"""In an active-active mode configuration, make a backup VIP address the master if its priority becomes higher than that of a master VIP address bound to this VMAC address. 
		If you disable pre-emption while a backup VIP address is the master, the backup VIP address remains master until the original master VIP's priority becomes higher than that of the current master.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._preemption = preemption
		except Exception as e:
			raise e

	@property
	def sharing(self) :
		ur"""In an active-active mode configuration, enable the backup VIP address to process any traffic instead of dropping it.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sharing
		except Exception as e:
			raise e

	@sharing.setter
	def sharing(self, sharing) :
		ur"""In an active-active mode configuration, enable the backup VIP address to process any traffic instead of dropping it.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sharing = sharing
		except Exception as e:
			raise e

	@property
	def tracking(self) :
		ur"""The effective priority (EP) value, relative to the base priority (BP) value in an active-active mode configuration. When EP is set to a value other than None, it is EP, not BP, which determines the master VIP address.
		Available settings function as follows:
		* NONE - No tracking. EP = BP
		* ALL -  If the status of all virtual servers is UP, EP = BP. Otherwise, EP = 0.
		* ONE - If the status of at least one virtual server is UP, EP = BP. Otherwise, EP = 0.
		* PROGRESSIVE - If the status of all virtual servers is UP, EP = BP. If the status of all virtual servers is DOWN, EP = 0. Otherwise EP = BP (1 - K/N), where N is the total number of virtual servers associated with the VIP address and K is the number of virtual servers for which the status is DOWN.
		Default: NONE.<br/>Default value: NONE<br/>Possible values = NONE, ONE, ALL, PROGRESSIVE.
		"""
		try :
			return self._tracking
		except Exception as e:
			raise e

	@tracking.setter
	def tracking(self, tracking) :
		ur"""The effective priority (EP) value, relative to the base priority (BP) value in an active-active mode configuration. When EP is set to a value other than None, it is EP, not BP, which determines the master VIP address.
		Available settings function as follows:
		* NONE - No tracking. EP = BP
		* ALL -  If the status of all virtual servers is UP, EP = BP. Otherwise, EP = 0.
		* ONE - If the status of at least one virtual server is UP, EP = BP. Otherwise, EP = 0.
		* PROGRESSIVE - If the status of all virtual servers is UP, EP = BP. If the status of all virtual servers is DOWN, EP = 0. Otherwise EP = BP (1 - K/N), where N is the total number of virtual servers associated with the VIP address and K is the number of virtual servers for which the status is DOWN.
		Default: NONE.<br/>Default value: NONE<br/>Possible values = NONE, ONE, ALL, PROGRESSIVE
		"""
		try :
			self._tracking = tracking
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		ur"""Assign a cluster node as the owner of this VMAC address. If no owner is configured, owner node is displayed as ALL and one node is dynamically elected as the owner.<br/>Maximum length =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		ur"""Assign a cluster node as the owner of this VMAC address. If no owner is configured, owner node is displayed as ALL and one node is dynamically elected as the owner.<br/>Maximum length =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def all(self) :
		ur"""Remove all the configured VMAC addresses from the NetScaler appliance.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		ur"""Remove all the configured VMAC addresses from the NetScaler appliance.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def ifaces(self) :
		ur"""Interfaces bound to this VRID.
		"""
		try :
			return self._ifaces
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Indicates whether this VRID entry was added manually or dynamically. When you manually add a VRID entry, the value for this parameter is STATIC. Otherwise, it is DYNAMIC.<br/>Possible values = STATIC, DYNAMIC.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def effectivepriority(self) :
		ur"""The effective priority of this VRID.
		"""
		try :
			return self._effectivepriority
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""Flags.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""The IP address bound to the VRID.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of this VRID.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def operationalownernode(self) :
		ur"""Run time owner node of the vrid.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._operationalownernode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vrid_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vrid
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
		ur""" Use this API to add vrid.
		"""
		try :
			if type(resource) is not list :
				addresource = vrid()
				addresource.id = resource.id
				addresource.priority = resource.priority
				addresource.preemption = resource.preemption
				addresource.sharing = resource.sharing
				addresource.tracking = resource.tracking
				addresource.ownernode = resource.ownernode
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vrid() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].id = resource[i].id
						addresources[i].priority = resource[i].priority
						addresources[i].preemption = resource[i].preemption
						addresources[i].sharing = resource[i].sharing
						addresources[i].tracking = resource[i].tracking
						addresources[i].ownernode = resource[i].ownernode
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete vrid.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vrid()
				if type(resource) !=  type(deleteresource):
					deleteresource.id = resource
				else :
					deleteresource.id = resource.id
					deleteresource.all = resource.all
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vrid() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vrid() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i].id
							deleteresources[i].all = resource[i].all
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update vrid.
		"""
		try :
			if type(resource) is not list :
				updateresource = vrid()
				updateresource.id = resource.id
				updateresource.priority = resource.priority
				updateresource.preemption = resource.preemption
				updateresource.sharing = resource.sharing
				updateresource.tracking = resource.tracking
				updateresource.ownernode = resource.ownernode
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vrid() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].priority = resource[i].priority
						updateresources[i].preemption = resource[i].preemption
						updateresources[i].sharing = resource[i].sharing
						updateresources[i].tracking = resource[i].tracking
						updateresources[i].ownernode = resource[i].ownernode
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of vrid resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vrid()
				if type(resource) !=  type(unsetresource):
					unsetresource.id = resource
				else :
					unsetresource.id = resource.id
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vrid() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vrid() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i].id
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the vrid resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vrid()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = vrid()
						obj.id = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [vrid() for _ in range(len(name))]
							obj = [vrid() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = vrid()
								obj[i].id = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of vrid resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vrid()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the vrid resources configured on NetScaler.
		"""
		try :
			obj = vrid()
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
		ur""" Use this API to count filtered the set of vrid resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vrid()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sharing:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		STATIC = "STATIC"
		DYNAMIC = "DYNAMIC"

	class Tracking:
		NONE = "NONE"
		ONE = "ONE"
		ALL = "ALL"
		PROGRESSIVE = "PROGRESSIVE"

	class Preemption:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class vrid_response(base_response) :
	def __init__(self, length=1) :
		self.vrid = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vrid = [vrid() for _ in range(length)]

