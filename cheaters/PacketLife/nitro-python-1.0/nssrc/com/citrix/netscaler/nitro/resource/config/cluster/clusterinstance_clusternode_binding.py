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

class clusterinstance_clusternode_binding(base_resource) :
	""" Binding class showing the clusternode that can be bound to clusterinstance.
	"""
	def __init__(self) :
		self._nodeid = 0
		self._nodeid = 0
		self._ipaddress = ""
		self._health = ""
		self._clusterhealth = ""
		self._effectivestate = ""
		self._masterstate = ""
		self._state = ""
		self._isconfigurationcoordinator = False
		self._islocalnode = False
		self._nodersskeymismatch = False
		self._nodelicensemismatch = False
		self._nodejumbonotsupported = False
		self._clid = 0
		self.___count = 0

	@property
	def nodeid(self) :
		ur"""The unique number that identiies a cluster.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		ur"""The unique number that identiies a cluster.<br/>Minimum value =  0<br/>Maximum value =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def clid(self) :
		ur"""Unique number that identifies the cluster.<br/>Minimum value =  1<br/>Maximum value =  16.
		"""
		try :
			return self._clid
		except Exception as e:
			raise e

	@clid.setter
	def clid(self, clid) :
		ur"""Unique number that identifies the cluster.<br/>Minimum value =  1<br/>Maximum value =  16
		"""
		try :
			self._clid = clid
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		ur"""The unique number that identiies a cluster.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Active, Spare or Passive. An active node serves traffic. A spare node serves as a backup for active nodes. A passive node does not serve traffic. This may be useful during temporary maintenance activity where it is desirable that the node takes part in the consensus protocol, but not serve traffic.<br/>Default value: PASSIVE<br/>Possible values = ACTIVE, SPARE, PASSIVE.
		"""
		try :
			return self._state
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
	def effectivestate(self) :
		ur"""Node effective health state.<br/>Possible values = UP, NOT UP, UNKNOWN, INIT.
		"""
		try :
			return self._effectivestate
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
	def isconfigurationcoordinator(self) :
		ur"""This argument is used to determine whether the node is configuration coordinator (CCO).
		"""
		try :
			return self._isconfigurationcoordinator
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
	def health(self) :
		ur"""Node Health state.<br/>Possible values = UNKNOWN, INIT, DOWN, UP, Some enabled and HAMON interfaces of the node are down, All interfaces of the node are down or disabled, SSL card(s) of the node have failed, Route Monitor(s) of the node have failed, Service state is being synchronized with the cluster, The backplane interface is not set,  is down,  or is disabled, The CLAG member(s) of the node are down, Persistence sessions are being synchronized with the cluster, The Syn Cookie is being synchronized with the cluster, Unknown Health, AAA keys are being sychronized with the cluster.
		"""
		try :
			return self._health
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
	def masterstate(self) :
		ur"""Master state.<br/>Possible values = INACTIVE, ACTIVE, UNKNOWN.
		"""
		try :
			return self._masterstate
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""The IP Address of the node.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusterinstance_clusternode_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusterinstance_clusternode_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.clid is not None :
				return str(self.clid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, clid) :
		ur""" Use this API to fetch clusterinstance_clusternode_binding resources.
		"""
		try :
			obj = clusterinstance_clusternode_binding()
			obj.clid = clid
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, clid, filter_) :
		ur""" Use this API to fetch filtered set of clusterinstance_clusternode_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusterinstance_clusternode_binding()
			obj.clid = clid
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, clid) :
		ur""" Use this API to count clusterinstance_clusternode_binding resources configued on NetScaler.
		"""
		try :
			obj = clusterinstance_clusternode_binding()
			obj.clid = clid
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, clid, filter_) :
		ur""" Use this API to count the filtered set of clusterinstance_clusternode_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusterinstance_clusternode_binding()
			obj.clid = clid
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class State:
		ACTIVE = "ACTIVE"
		SPARE = "SPARE"
		PASSIVE = "PASSIVE"

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

class clusterinstance_clusternode_binding_response(base_response) :
	def __init__(self, length=1) :
		self.clusterinstance_clusternode_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusterinstance_clusternode_binding = [clusterinstance_clusternode_binding() for _ in range(length)]

