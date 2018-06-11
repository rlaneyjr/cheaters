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

class arp(base_resource) :
	""" Configuration for arp resource. """
	def __init__(self) :
		self._ipaddress = ""
		self._td = 0
		self._mac = ""
		self._ifnum = ""
		self._vxlan = 0
		self._vtep = ""
		self._ownernode = 0
		self._all = False
		self._timeout = 0
		self._state = 0
		self._flags = 0
		self._type = ""
		self._vlan = 0
		self._channel = 0
		self.___count = 0

	@property
	def ipaddress(self) :
		ur"""IP address of the network device that you want to add to the ARP table.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""IP address of the network device that you want to add to the ARP table.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
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
	def mac(self) :
		ur"""MAC address of the network device.
		"""
		try :
			return self._mac
		except Exception as e:
			raise e

	@mac.setter
	def mac(self, mac) :
		ur"""MAC address of the network device.
		"""
		try :
			self._mac = mac
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		ur"""Interface through which the network device is accessible. Specify the interface in (slot/port) notation. For example, 1/3.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		ur"""Interface through which the network device is accessible. Specify the interface in (slot/port) notation. For example, 1/3.
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		ur"""ID of the VXLAN on which the IP address of this ARP entry is reachable.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		ur"""ID of the VXLAN on which the IP address of this ARP entry is reachable.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def vtep(self) :
		ur"""IP address of the VXLAN tunnel endpoint (VTEP) through which the IP address of this ARP entry is reachable.<br/>Minimum length =  1.
		"""
		try :
			return self._vtep
		except Exception as e:
			raise e

	@vtep.setter
	def vtep(self, vtep) :
		ur"""IP address of the VXLAN tunnel endpoint (VTEP) through which the IP address of this ARP entry is reachable.<br/>Minimum length =  1
		"""
		try :
			self._vtep = vtep
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		ur"""The owner node for the Arp entry.<br/>Maximum length =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		ur"""The owner node for the Arp entry.<br/>Maximum length =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def all(self) :
		ur"""Remove all ARP entries from the ARP table of the NetScaler appliance.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		ur"""Remove all ARP entries from the ARP table of the NetScaler appliance.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		ur"""The time, in seconds, after which the entry times out.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""The state of the ARP entry.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""The flags for the entry.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Indicates whether this ARP entry was added manually or dynamically. When you manually add an ARP entry, the value for this parameter is STATIC. Otherwise, it is DYNAMIC. For the NSIP and loopback IP addresses, the value is PERMANENT.<br/>Possible values = STATIC, PERMANENT, DYNAMIC.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		ur"""The VLAN ID through which packets are to be sent after matching the ARP entry. This is a numeric value.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@property
	def channel(self) :
		ur"""The tunnel, channel, or physical interface through which the ARP entry is identified.
		"""
		try :
			return self._channel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(arp_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.arp
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ipaddress is not None :
				return str(self.ipaddress)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add arp.
		"""
		try :
			if type(resource) is not list :
				addresource = arp()
				addresource.ipaddress = resource.ipaddress
				addresource.td = resource.td
				addresource.mac = resource.mac
				addresource.ifnum = resource.ifnum
				addresource.vxlan = resource.vxlan
				addresource.vtep = resource.vtep
				addresource.ownernode = resource.ownernode
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ arp() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].td = resource[i].td
						addresources[i].mac = resource[i].mac
						addresources[i].ifnum = resource[i].ifnum
						addresources[i].vxlan = resource[i].vxlan
						addresources[i].vtep = resource[i].vtep
						addresources[i].ownernode = resource[i].ownernode
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete arp.
		"""
		try :
			if type(resource) is not list :
				deleteresource = arp()
				if type(resource) !=  type(deleteresource):
					deleteresource.ipaddress = resource
				else :
					deleteresource.ipaddress = resource.ipaddress
					deleteresource.td = resource.td
					deleteresource.all = resource.all
					deleteresource.ownernode = resource.ownernode
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ arp() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipaddress = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ arp() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipaddress = resource[i].ipaddress
							deleteresources[i].td = resource[i].td
							deleteresources[i].all = resource[i].all
							deleteresources[i].ownernode = resource[i].ownernode
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def send(cls, client, resource) :
		ur""" Use this API to send arp.
		"""
		try :
			if type(resource) is not list :
				sendresource = arp()
				sendresource.ipaddress = resource.ipaddress
				sendresource.td = resource.td
				sendresource.all = resource.all
				return sendresource.perform_operation(client,"send")
			else :
				if (resource and len(resource) > 0) :
					sendresources = [ arp() for _ in range(len(resource))]
					for i in range(len(resource)) :
						sendresources[i].ipaddress = resource[i].ipaddress
						sendresources[i].td = resource[i].td
						sendresources[i].all = resource[i].all
				result = cls.perform_operation_bulk_request(client, sendresources,"send")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the arp resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = arp()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [arp() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of arp resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = arp()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the arp resources configured on NetScaler.
		"""
		try :
			obj = arp()
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
		ur""" Use this API to count filtered the set of arp resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = arp()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		STATIC = "STATIC"
		PERMANENT = "PERMANENT"
		DYNAMIC = "DYNAMIC"

class arp_response(base_response) :
	def __init__(self, length=1) :
		self.arp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.arp = [arp() for _ in range(length)]

