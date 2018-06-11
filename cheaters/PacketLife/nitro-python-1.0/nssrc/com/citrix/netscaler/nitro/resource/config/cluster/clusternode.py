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

class clusternode(base_resource) :
	""" Configuration for cluster node resource. """
	def __init__(self) :
		self._nodeid = 0
		self._ipaddress = ""
		self._state = ""
		self._backplane = ""
		self._priority = 0
		self._clusterhealth = ""
		self._effectivestate = ""
		self._operationalsyncstate = ""
		self._masterstate = ""
		self._health = ""
		self._isconfigurationcoordinator = False
		self._islocalnode = False
		self._nodersskeymismatch = False
		self._nodelicensemismatch = False
		self._nodejumbonotsupported = False
		self._nodelist = []
		self._ifaceslist = []
		self._enabledifaces = ""
		self._disabledifaces = ""
		self._partialfailifaces = ""
		self._hamonifaces = ""
		self.___count = 0

	@property
	def nodeid(self) :
		ur"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		ur"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""NetScaler IP (NSIP) address of the appliance to add to the cluster. Must be an IPv4 address.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""NetScaler IP (NSIP) address of the appliance to add to the cluster. Must be an IPv4 address.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Admin state of the cluster node. The available settings function as follows:
		ACTIVE - The node serves traffic.
		SPARE - The node does not serve traffic unless an ACTIVE node goes down.
		PASSIVE - The node does not serve traffic, unless you change its state. PASSIVE state is useful during temporary maintenance activities in which you want the node to take part in the consensus protocol but not to serve traffic.<br/>Default value: PASSIVE<br/>Possible values = ACTIVE, SPARE, PASSIVE.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Admin state of the cluster node. The available settings function as follows:
		ACTIVE - The node serves traffic.
		SPARE - The node does not serve traffic unless an ACTIVE node goes down.
		PASSIVE - The node does not serve traffic, unless you change its state. PASSIVE state is useful during temporary maintenance activities in which you want the node to take part in the consensus protocol but not to serve traffic.<br/>Default value: PASSIVE<br/>Possible values = ACTIVE, SPARE, PASSIVE
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def backplane(self) :
		ur"""Interface through which the node communicates with the other nodes in the cluster. Must be specified in the three-tuple form n/c/u, where n represents the node ID and c/u refers to the interface on the appliance.<br/>Minimum length =  1.
		"""
		try :
			return self._backplane
		except Exception as e:
			raise e

	@backplane.setter
	def backplane(self, backplane) :
		ur"""Interface through which the node communicates with the other nodes in the cluster. Must be specified in the three-tuple form n/c/u, where n represents the node ID and c/u refers to the interface on the appliance.<br/>Minimum length =  1
		"""
		try :
			self._backplane = backplane
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Preference for selecting a node as the configuration coordinator. The node with the lowest priority value is selected as the configuration coordinator.
		When the current configuration coordinator goes down, the node with the next lowest priority is made the new configuration coordinator. When the original node comes back up, it will preempt the new configuration coordinator and take over as the configuration coordinator.
		Note: When priority is not configured for any of the nodes or if multiple nodes have the same priority, the cluster elects one of the nodes as the configuration coordinator.<br/>Default value: 31<br/>Maximum length =  31.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Preference for selecting a node as the configuration coordinator. The node with the lowest priority value is selected as the configuration coordinator.
		When the current configuration coordinator goes down, the node with the next lowest priority is made the new configuration coordinator. When the original node comes back up, it will preempt the new configuration coordinator and take over as the configuration coordinator.
		Note: When priority is not configured for any of the nodes or if multiple nodes have the same priority, the cluster elects one of the nodes as the configuration coordinator.<br/>Default value: 31<br/>Maximum length =  31
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def clusterhealth(self) :
		ur"""Node clusterd state.<br/>Possible values = UP, Configurations of the node are lagging behind the cluster by more than 256 commands, The config sync operation has exceeded the time limit of 60 seconds, The config sync operation (full sync) is in progress, The node is not in sync with the cluster configurations as sync is disabled on this node, The execution of a configuration command has failed on this node, UNKNOWN.
		"""
		try :
			return self._clusterhealth
		except Exception as e:
			raise e

	@property
	def effectivestate(self) :
		ur"""Node effective health state.<br/>Possible values = UP, NOT UP, UNKNOWN, INIT.
		"""
		try :
			return self._effectivestate
		except Exception as e:
			raise e

	@property
	def operationalsyncstate(self) :
		ur"""Node Operational Reconciliation state.<br/>Default value: ENABLED<br/>Possible values = ENABLED, SUCCESS, IN PROGRESS, FAILED, INCREMENTAL SYNC DISABLED, DISABLED, UNKNOWN.
		"""
		try :
			return self._operationalsyncstate
		except Exception as e:
			raise e

	@property
	def masterstate(self) :
		ur"""Node Master state.<br/>Possible values = INACTIVE, ACTIVE, UNKNOWN.
		"""
		try :
			return self._masterstate
		except Exception as e:
			raise e

	@property
	def health(self) :
		ur"""Node Health state.<br/>Possible values = UNKNOWN, INIT, DOWN, UP, Some enabled and HAMON interfaces of the node are down, All interfaces of the node are down or disabled, SSL card(s) of the node have failed, Route Monitor(s) of the node have failed, Service state is being synchronized with the cluster, The backplane interface is not set,  is down,  or is disabled, The CLAG member(s) of the node are down, Persistence sessions are being synchronized with the cluster, The Syn Cookie is being synchronized with the cluster, Unknown Health, AAA keys are being sychronized with the cluster.
		"""
		try :
			return self._health
		except Exception as e:
			raise e

	@property
	def isconfigurationcoordinator(self) :
		ur"""This argument is used to determine whether the node is configuration coordinator (CCO).
		"""
		try :
			return self._isconfigurationcoordinator
		except Exception as e:
			raise e

	@property
	def islocalnode(self) :
		ur"""This argument is used to determine whether it is local node.
		"""
		try :
			return self._islocalnode
		except Exception as e:
			raise e

	@property
	def nodersskeymismatch(self) :
		ur"""This argument is used to determine if there is a RSS key mismatch at cluster node level.
		"""
		try :
			return self._nodersskeymismatch
		except Exception as e:
			raise e

	@property
	def nodelicensemismatch(self) :
		ur"""This argument is used to determine if there is a License mismatch at cluster node level.
		"""
		try :
			return self._nodelicensemismatch
		except Exception as e:
			raise e

	@property
	def nodejumbonotsupported(self) :
		ur"""This argument is used to determine if Jumbo framework not supported at cluster node level.
		"""
		try :
			return self._nodejumbonotsupported
		except Exception as e:
			raise e

	@property
	def nodelist(self) :
		ur"""Nodelist for displaying Heartbeat not seen interfaces on a cluster node.
		"""
		try :
			return self._nodelist
		except Exception as e:
			raise e

	@property
	def ifaceslist(self) :
		ur"""Interface list corresponding to nodelist for Heartbeat not seen interfaces on a cluster node.
		"""
		try :
			return self._ifaceslist
		except Exception as e:
			raise e

	@property
	def enabledifaces(self) :
		ur"""Enabled Interfaces on a cluster node.
		"""
		try :
			return self._enabledifaces
		except Exception as e:
			raise e

	@property
	def disabledifaces(self) :
		ur"""Disabled Interfaces on a cluster node.
		"""
		try :
			return self._disabledifaces
		except Exception as e:
			raise e

	@property
	def partialfailifaces(self) :
		ur"""Partial Failure Interfaces on a cluster node.
		"""
		try :
			return self._partialfailifaces
		except Exception as e:
			raise e

	@property
	def hamonifaces(self) :
		ur"""Hamon Interfaces on a cluster node.
		"""
		try :
			return self._hamonifaces
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusternode_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusternode
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.nodeid is not None :
				return str(self.nodeid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add clusternode.
		"""
		try :
			if type(resource) is not list :
				addresource = clusternode()
				addresource.nodeid = resource.nodeid
				addresource.ipaddress = resource.ipaddress
				addresource.state = resource.state
				addresource.backplane = resource.backplane
				addresource.priority = resource.priority
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ clusternode() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].nodeid = resource[i].nodeid
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].state = resource[i].state
						addresources[i].backplane = resource[i].backplane
						addresources[i].priority = resource[i].priority
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update clusternode.
		"""
		try :
			if type(resource) is not list :
				updateresource = clusternode()
				updateresource.nodeid = resource.nodeid
				updateresource.state = resource.state
				updateresource.backplane = resource.backplane
				updateresource.priority = resource.priority
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ clusternode() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].nodeid = resource[i].nodeid
						updateresources[i].state = resource[i].state
						updateresources[i].backplane = resource[i].backplane
						updateresources[i].priority = resource[i].priority
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of clusternode resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = clusternode()
				if type(resource) !=  type(unsetresource):
					unsetresource.nodeid = resource
				else :
					unsetresource.nodeid = resource.nodeid
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ clusternode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].nodeid = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ clusternode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].nodeid = resource[i].nodeid
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete clusternode.
		"""
		try :
			if type(resource) is not list :
				deleteresource = clusternode()
				if type(resource) !=  type(deleteresource):
					deleteresource.nodeid = resource
				else :
					deleteresource.nodeid = resource.nodeid
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ clusternode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].nodeid = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ clusternode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].nodeid = resource[i].nodeid
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the clusternode resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = clusternode()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = clusternode()
						obj.nodeid = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [clusternode() for _ in range(len(name))]
							obj = [clusternode() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = clusternode()
								obj[i].nodeid = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of clusternode resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternode()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the clusternode resources configured on NetScaler.
		"""
		try :
			obj = clusternode()
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
		ur""" Use this API to count filtered the set of clusternode resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternode()
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
		ACTIVE = "ACTIVE"
		SPARE = "SPARE"
		PASSIVE = "PASSIVE"

	class Operationalsyncstate:
		ENABLED = "ENABLED"
		SUCCESS = "SUCCESS"
		IN_PROGRESS = "IN PROGRESS"
		FAILED = "FAILED"
		INCREMENTAL_SYNC_DISABLED = "INCREMENTAL SYNC DISABLED"
		DISABLED = "DISABLED"
		UNKNOWN = "UNKNOWN"

	class Effectivestate:
		UP = "UP"
		NOT_UP = "NOT UP"
		UNKNOWN = "UNKNOWN"
		INIT = "INIT"

	class Health:
		UNKNOWN = "UNKNOWN"
		INIT = "INIT"
		DOWN = "DOWN"
		UP = "UP"
		Some_enabled_and_HAMON_interfaces_of_the_node_are_down = "Some enabled and HAMON interfaces of the node are down"
		All_interfaces_of_the_node_are_down_or_disabled = "All interfaces of the node are down or disabled"
		SSL_card_s__of_the_node_have_failed = "SSL card(s) of the node have failed"
		Route_Monitor_s__of_the_node_have_failed = "Route Monitor(s) of the node have failed"
		Service_state_is_being_synchronized_with_the_cluster = "Service state is being synchronized with the cluster"
		The_backplane_interface_is_not_set = "The backplane interface is not set"
		_is_down = " is down"
		_or_is_disabled = " or is disabled"
		The_CLAG_member_s__of_the_node_are_down = "The CLAG member(s) of the node are down"
		Persistence_sessions_are_being_synchronized_with_the_cluster = "Persistence sessions are being synchronized with the cluster"
		The_Syn_Cookie_is_being_synchronized_with_the_cluster = "The Syn Cookie is being synchronized with the cluster"
		Unknown_Health = "Unknown Health"
		AAA_keys_are_being_sychronized_with_the_cluster = "AAA keys are being sychronized with the cluster"

	class Clusterhealth:
		UP = "UP"
		Configurations_of_the_node_are_lagging_behind_the_cluster_by_more_than_256_commands = "Configurations of the node are lagging behind the cluster by more than 256 commands"
		The_config_sync_operation_has_exceeded_the_time_limit_of_60_seconds = "The config sync operation has exceeded the time limit of 60 seconds"
		The_config_sync_operation__full_sync__is_in_progress = "The config sync operation (full sync) is in progress"
		The_node_is_not_in_sync_with_the_cluster_configurations_as_sync_is_disabled_on_this_node = "The node is not in sync with the cluster configurations as sync is disabled on this node"
		The_execution_of_a_configuration_command_has_failed_on_this_node = "The execution of a configuration command has failed on this node"
		UNKNOWN = "UNKNOWN"

	class Masterstate:
		INACTIVE = "INACTIVE"
		ACTIVE = "ACTIVE"
		UNKNOWN = "UNKNOWN"

class clusternode_response(base_response) :
	def __init__(self, length=1) :
		self.clusternode = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusternode = [clusternode() for _ in range(length)]

