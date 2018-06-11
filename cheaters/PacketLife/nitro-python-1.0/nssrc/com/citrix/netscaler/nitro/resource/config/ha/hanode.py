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

class hanode(base_resource) :
	""" Configuration for node resource. """
	def __init__(self) :
		self._id = 0
		self._ipaddress = ""
		self._inc = ""
		self._hastatus = ""
		self._hasync = ""
		self._haprop = ""
		self._hellointerval = 0
		self._deadinterval = 0
		self._failsafe = ""
		self._maxflips = 0
		self._maxfliptime = 0
		self._syncvlan = 0
		self._name = ""
		self._flags = 0
		self._state = ""
		self._enaifaces = ""
		self._disifaces = ""
		self._hamonifaces = ""
		self._pfifaces = ""
		self._ifaces = ""
		self._network = ""
		self._netmask = ""
		self._ssl2 = ""
		self._masterstatetime = 0
		self._routemonitor = ""
		self._curflips = 0
		self._completedfliptime = 0
		self._routemonitorstate = ""
		self.___count = 0

	@property
	def id(self) :
		ur"""Number that uniquely identifies the node. For self node, it will always be 0. Peer node values can range from 1-64.<br/>Minimum length =  1<br/>Maximum length =  64.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""Number that uniquely identifies the node. For self node, it will always be 0. Peer node values can range from 1-64.<br/>Minimum length =  1<br/>Maximum length =  64
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""The NSIP or NSIP6 address of the node to be added for an HA configuration. This setting is neither propagated nor synchronized.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""The NSIP or NSIP6 address of the node to be added for an HA configuration. This setting is neither propagated nor synchronized.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def inc(self) :
		ur"""This option is required if the HA nodes reside on different networks. When this mode is enabled, the following independent network entities and configurations are neither propagated nor synced to the other node: MIPs, SNIPs, VLANs, routes (except LLB routes), route monitors, RNAT rules (except any RNAT rule with a VIP as the NAT IP), and dynamic routing configurations. They are maintained independently on each node.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._inc
		except Exception as e:
			raise e

	@inc.setter
	def inc(self, inc) :
		ur"""This option is required if the HA nodes reside on different networks. When this mode is enabled, the following independent network entities and configurations are neither propagated nor synced to the other node: MIPs, SNIPs, VLANs, routes (except LLB routes), route monitors, RNAT rules (except any RNAT rule with a VIP as the NAT IP), and dynamic routing configurations. They are maintained independently on each node.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._inc = inc
		except Exception as e:
			raise e

	@property
	def hastatus(self) :
		ur"""The HA status of the node. The HA status STAYSECONDARY is used to force the secondary device stay as secondary independent of the state of the Primary device. For example, in an existing HA setup, the Primary node has to be upgraded and this process would take few seconds. During the upgradation, it is possible that the Primary node may suffer from a downtime for a few seconds. However, the Secondary should not take over as the Primary node. Thus, the Secondary node should remain as Secondary even if there is a failure in the Primary node.
		STAYPRIMARY configuration keeps the node in primary state in case if it is healthy, even if the peer node was the primary node initially. If the node with STAYPRIMARY setting (and no peer node) is added to a primary node (which has this node as the peer) then this node takes over as the new primary and the older node becomes secondary. ENABLED state means normal HA operation without any constraints/preferences. DISABLED state disables the normal HA operation of the node.<br/>Possible values = ENABLED, STAYSECONDARY, DISABLED, STAYPRIMARY.
		"""
		try :
			return self._hastatus
		except Exception as e:
			raise e

	@hastatus.setter
	def hastatus(self, hastatus) :
		ur"""The HA status of the node. The HA status STAYSECONDARY is used to force the secondary device stay as secondary independent of the state of the Primary device. For example, in an existing HA setup, the Primary node has to be upgraded and this process would take few seconds. During the upgradation, it is possible that the Primary node may suffer from a downtime for a few seconds. However, the Secondary should not take over as the Primary node. Thus, the Secondary node should remain as Secondary even if there is a failure in the Primary node.
		STAYPRIMARY configuration keeps the node in primary state in case if it is healthy, even if the peer node was the primary node initially. If the node with STAYPRIMARY setting (and no peer node) is added to a primary node (which has this node as the peer) then this node takes over as the new primary and the older node becomes secondary. ENABLED state means normal HA operation without any constraints/preferences. DISABLED state disables the normal HA operation of the node.<br/>Possible values = ENABLED, STAYSECONDARY, DISABLED, STAYPRIMARY
		"""
		try :
			self._hastatus = hastatus
		except Exception as e:
			raise e

	@property
	def hasync(self) :
		ur"""Automatically maintain synchronization by duplicating the configuration of the primary node on the secondary node. This setting is not propagated. Automatic synchronization requires that this setting be enabled (the default) on the current secondary node. Synchronization uses TCP port 3010.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._hasync
		except Exception as e:
			raise e

	@hasync.setter
	def hasync(self, hasync) :
		ur"""Automatically maintain synchronization by duplicating the configuration of the primary node on the secondary node. This setting is not propagated. Automatic synchronization requires that this setting be enabled (the default) on the current secondary node. Synchronization uses TCP port 3010.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._hasync = hasync
		except Exception as e:
			raise e

	@property
	def haprop(self) :
		ur"""Automatically propagate all commands from the primary to the secondary node, except the following:
		* All HA configuration related commands. For example, add ha node, set ha node, and bind ha node. 
		* All Interface related commands. For example, set interface and unset interface.
		* All channels related commands. For example, add channel, set channel, and bind channel.
		The propagated command is executed on the secondary node before it is executed on the primary. If command propagation fails, or if command execution fails on the secondary, the primary node executes the command and logs an error.  Command propagation uses port 3010.
		Note: After enabling propagation, run force synchronization on either node.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._haprop
		except Exception as e:
			raise e

	@haprop.setter
	def haprop(self, haprop) :
		ur"""Automatically propagate all commands from the primary to the secondary node, except the following:
		* All HA configuration related commands. For example, add ha node, set ha node, and bind ha node. 
		* All Interface related commands. For example, set interface and unset interface.
		* All channels related commands. For example, add channel, set channel, and bind channel.
		The propagated command is executed on the secondary node before it is executed on the primary. If command propagation fails, or if command execution fails on the secondary, the primary node executes the command and logs an error.  Command propagation uses port 3010.
		Note: After enabling propagation, run force synchronization on either node.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._haprop = haprop
		except Exception as e:
			raise e

	@property
	def hellointerval(self) :
		ur"""Interval, in milliseconds, between heartbeat messages sent to the peer node. The heartbeat messages are UDP packets sent to port 3003 of the peer node.<br/>Default value: 200<br/>Minimum length =  200<br/>Maximum length =  1000.
		"""
		try :
			return self._hellointerval
		except Exception as e:
			raise e

	@hellointerval.setter
	def hellointerval(self, hellointerval) :
		ur"""Interval, in milliseconds, between heartbeat messages sent to the peer node. The heartbeat messages are UDP packets sent to port 3003 of the peer node.<br/>Default value: 200<br/>Minimum length =  200<br/>Maximum length =  1000
		"""
		try :
			self._hellointerval = hellointerval
		except Exception as e:
			raise e

	@property
	def deadinterval(self) :
		ur"""Number of seconds after which a peer node is marked DOWN if heartbeat messages are not received from the peer node.<br/>Default value: 3<br/>Minimum length =  3<br/>Maximum length =  60.
		"""
		try :
			return self._deadinterval
		except Exception as e:
			raise e

	@deadinterval.setter
	def deadinterval(self, deadinterval) :
		ur"""Number of seconds after which a peer node is marked DOWN if heartbeat messages are not received from the peer node.<br/>Default value: 3<br/>Minimum length =  3<br/>Maximum length =  60
		"""
		try :
			self._deadinterval = deadinterval
		except Exception as e:
			raise e

	@property
	def failsafe(self) :
		ur"""Keep one node primary if both nodes fail the health check, so that a partially available node can back up data and handle traffic. This mode is set independently on each node.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._failsafe
		except Exception as e:
			raise e

	@failsafe.setter
	def failsafe(self, failsafe) :
		ur"""Keep one node primary if both nodes fail the health check, so that a partially available node can back up data and handle traffic. This mode is set independently on each node.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._failsafe = failsafe
		except Exception as e:
			raise e

	@property
	def maxflips(self) :
		ur"""Max number of flips allowed before becoming sticky primary.<br/>Default value: 0.
		"""
		try :
			return self._maxflips
		except Exception as e:
			raise e

	@maxflips.setter
	def maxflips(self, maxflips) :
		ur"""Max number of flips allowed before becoming sticky primary.<br/>Default value: 0
		"""
		try :
			self._maxflips = maxflips
		except Exception as e:
			raise e

	@property
	def maxfliptime(self) :
		ur"""Interval after which flipping of node states can again start.<br/>Default value: 0.
		"""
		try :
			return self._maxfliptime
		except Exception as e:
			raise e

	@maxfliptime.setter
	def maxfliptime(self, maxfliptime) :
		ur"""Interval after which flipping of node states can again start.<br/>Default value: 0
		"""
		try :
			self._maxfliptime = maxfliptime
		except Exception as e:
			raise e

	@property
	def syncvlan(self) :
		ur"""Vlan on which HA related communication is sent. This include sync, propagation , connection mirroring , LB persistency config sync, persistent session sync and session state sync. However HA heartbeats can go all interfaces.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._syncvlan
		except Exception as e:
			raise e

	@syncvlan.setter
	def syncvlan(self, syncvlan) :
		ur"""Vlan on which HA related communication is sent. This include sync, propagation , connection mirroring , LB persistency config sync, persistent session sync and session state sync. However HA heartbeats can go all interfaces.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._syncvlan = syncvlan
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Node Name.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""The flags for this entry.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""HA Master State.<br/>Possible values = Primary, Secondary, UNKNOWN.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def enaifaces(self) :
		ur"""Enabled interfaces.
		"""
		try :
			return self._enaifaces
		except Exception as e:
			raise e

	@property
	def disifaces(self) :
		ur"""Disabled interfaces.
		"""
		try :
			return self._disifaces
		except Exception as e:
			raise e

	@property
	def hamonifaces(self) :
		ur"""HAMON ON interfaces.
		"""
		try :
			return self._hamonifaces
		except Exception as e:
			raise e

	@property
	def pfifaces(self) :
		ur"""Interfaces causing Partial Failure.
		"""
		try :
			return self._pfifaces
		except Exception as e:
			raise e

	@property
	def ifaces(self) :
		ur"""Interfaces on which non-multicast is not seen.
		"""
		try :
			return self._ifaces
		except Exception as e:
			raise e

	@property
	def network(self) :
		ur"""The network.
		"""
		try :
			return self._network
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""The netmask.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@property
	def ssl2(self) :
		ur"""SSL card status.<br/>Possible values = DOWN, UP, NOT PRESENT, UNKNOWN.
		"""
		try :
			return self._ssl2
		except Exception as e:
			raise e

	@property
	def masterstatetime(self) :
		ur"""Time elapsed in current master state.
		"""
		try :
			return self._masterstatetime
		except Exception as e:
			raise e

	@property
	def routemonitor(self) :
		ur"""The IP address (IPv4 or IPv6).
		"""
		try :
			return self._routemonitor
		except Exception as e:
			raise e

	@property
	def curflips(self) :
		ur"""Keeps track of number of flips that have happened till now in current interval.
		"""
		try :
			return self._curflips
		except Exception as e:
			raise e

	@property
	def completedfliptime(self) :
		ur"""To inform user whether flip time is elapsed or not.
		"""
		try :
			return self._completedfliptime
		except Exception as e:
			raise e

	@property
	def routemonitorstate(self) :
		ur"""State for route monitor.<br/>Possible values = UP, DOWN.
		"""
		try :
			return self._routemonitorstate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(hanode_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.hanode
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
		ur""" Use this API to add hanode.
		"""
		try :
			if type(resource) is not list :
				addresource = hanode()
				addresource.id = resource.id
				addresource.ipaddress = resource.ipaddress
				addresource.inc = resource.inc
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ hanode() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].id = resource[i].id
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].inc = resource[i].inc
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete hanode.
		"""
		try :
			if type(resource) is not list :
				deleteresource = hanode()
				if type(resource) !=  type(deleteresource):
					deleteresource.id = resource
				else :
					deleteresource.id = resource.id
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ hanode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ hanode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].id = resource[i].id
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update hanode.
		"""
		try :
			if type(resource) is not list :
				updateresource = hanode()
				updateresource.id = resource.id
				updateresource.hastatus = resource.hastatus
				updateresource.hasync = resource.hasync
				updateresource.haprop = resource.haprop
				updateresource.hellointerval = resource.hellointerval
				updateresource.deadinterval = resource.deadinterval
				updateresource.failsafe = resource.failsafe
				updateresource.maxflips = resource.maxflips
				updateresource.maxfliptime = resource.maxfliptime
				updateresource.syncvlan = resource.syncvlan
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ hanode() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].id = resource[i].id
						updateresources[i].hastatus = resource[i].hastatus
						updateresources[i].hasync = resource[i].hasync
						updateresources[i].haprop = resource[i].haprop
						updateresources[i].hellointerval = resource[i].hellointerval
						updateresources[i].deadinterval = resource[i].deadinterval
						updateresources[i].failsafe = resource[i].failsafe
						updateresources[i].maxflips = resource[i].maxflips
						updateresources[i].maxfliptime = resource[i].maxfliptime
						updateresources[i].syncvlan = resource[i].syncvlan
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of hanode resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = hanode()
				if type(resource) !=  type(unsetresource):
					unsetresource.id = resource
				else :
					unsetresource.id = resource.id
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ hanode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ hanode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].id = resource[i].id
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the hanode resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = hanode()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = hanode()
						obj.id = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [hanode() for _ in range(len(name))]
							obj = [hanode() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = hanode()
								obj[i].id = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of hanode resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = hanode()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the hanode resources configured on NetScaler.
		"""
		try :
			obj = hanode()
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
		ur""" Use this API to count filtered the set of hanode resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = hanode()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		Primary = "Primary"
		Secondary = "Secondary"
		UNKNOWN = "UNKNOWN"

	class Haprop:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Inc:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Routemonitorstate:
		UP = "UP"
		DOWN = "DOWN"

	class Hasync:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Failsafe:
		ON = "ON"
		OFF = "OFF"

	class Hastatus:
		ENABLED = "ENABLED"
		STAYSECONDARY = "STAYSECONDARY"
		DISABLED = "DISABLED"
		STAYPRIMARY = "STAYPRIMARY"

	class Ssl2:
		DOWN = "DOWN"
		UP = "UP"
		NOT_PRESENT = "NOT PRESENT"
		UNKNOWN = "UNKNOWN"

class hanode_response(base_response) :
	def __init__(self, length=1) :
		self.hanode = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.hanode = [hanode() for _ in range(length)]

