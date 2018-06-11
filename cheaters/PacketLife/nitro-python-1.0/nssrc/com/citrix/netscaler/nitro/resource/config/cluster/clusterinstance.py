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

class clusterinstance(base_resource) :
	""" Configuration for cluster instance resource. """
	def __init__(self) :
		self._clid = 0
		self._deadinterval = 0
		self._hellointerval = 0
		self._preemption = ""
		self._quorumtype = ""
		self._adminstate = ""
		self._propstate = ""
		self._operationalstate = ""
		self._status = ""
		self._rsskeymismatch = False
		self._licensemismatch = False
		self._jumbonotsupported = False
		self._operationalpropstate = ""
		self.___count = 0

	@property
	def clid(self) :
		ur"""Unique number that identifies the cluster.<br/>Minimum length =  1<br/>Maximum length =  16.
		"""
		try :
			return self._clid
		except Exception as e:
			raise e

	@clid.setter
	def clid(self, clid) :
		ur"""Unique number that identifies the cluster.<br/>Minimum length =  1<br/>Maximum length =  16
		"""
		try :
			self._clid = clid
		except Exception as e:
			raise e

	@property
	def deadinterval(self) :
		ur"""Amount of time, in seconds, after which nodes that do not respond to the heartbeats are assumed to be down.<br/>Default value: 3<br/>Minimum length =  3<br/>Maximum length =  60.
		"""
		try :
			return self._deadinterval
		except Exception as e:
			raise e

	@deadinterval.setter
	def deadinterval(self, deadinterval) :
		ur"""Amount of time, in seconds, after which nodes that do not respond to the heartbeats are assumed to be down.<br/>Default value: 3<br/>Minimum length =  3<br/>Maximum length =  60
		"""
		try :
			self._deadinterval = deadinterval
		except Exception as e:
			raise e

	@property
	def hellointerval(self) :
		ur"""Interval, in milliseconds, at which heartbeats are sent to each cluster node to check the health status.<br/>Default value: 200<br/>Minimum length =  200<br/>Maximum length =  1000.
		"""
		try :
			return self._hellointerval
		except Exception as e:
			raise e

	@hellointerval.setter
	def hellointerval(self, hellointerval) :
		ur"""Interval, in milliseconds, at which heartbeats are sent to each cluster node to check the health status.<br/>Default value: 200<br/>Minimum length =  200<br/>Maximum length =  1000
		"""
		try :
			self._hellointerval = hellointerval
		except Exception as e:
			raise e

	@property
	def preemption(self) :
		ur"""Preempt a cluster node that is configured as a SPARE if an ACTIVE node becomes available.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._preemption
		except Exception as e:
			raise e

	@preemption.setter
	def preemption(self, preemption) :
		ur"""Preempt a cluster node that is configured as a SPARE if an ACTIVE node becomes available.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._preemption = preemption
		except Exception as e:
			raise e

	@property
	def quorumtype(self) :
		ur"""Quorum Configuration Choices  - "Majority" (recommended) requires majority of nodes to be online for the cluster to be UP. "None" relaxes this requirement.<br/>Default value: MAJORITY<br/>Possible values = MAJORITY, NONE.
		"""
		try :
			return self._quorumtype
		except Exception as e:
			raise e

	@quorumtype.setter
	def quorumtype(self, quorumtype) :
		ur"""Quorum Configuration Choices  - "Majority" (recommended) requires majority of nodes to be online for the cluster to be UP. "None" relaxes this requirement.<br/>Default value: MAJORITY<br/>Possible values = MAJORITY, NONE
		"""
		try :
			self._quorumtype = quorumtype
		except Exception as e:
			raise e

	@property
	def adminstate(self) :
		ur"""Cluster Admin State.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._adminstate
		except Exception as e:
			raise e

	@property
	def propstate(self) :
		ur"""Enable/Disable the execution of commands on the cluster. This will not impact the execution of commands on individual cluster nodes by using the NSIP.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._propstate
		except Exception as e:
			raise e

	@property
	def operationalstate(self) :
		ur"""Cluster Operational State.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._operationalstate
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""Cluster Operational State.<br/>Possible values = DOWN, UP, PARTIAL-UP, UNKNOWN.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def rsskeymismatch(self) :
		ur"""This argument is used to determine if there is a RSS key mismatch at cluster instance level.
		"""
		try :
			return self._rsskeymismatch
		except Exception as e:
			raise e

	@property
	def licensemismatch(self) :
		ur"""This argument is used to determine if there is a License mismatch at cluster instance level.
		"""
		try :
			return self._licensemismatch
		except Exception as e:
			raise e

	@property
	def jumbonotsupported(self) :
		ur"""This argument is used to determine if Jumbo framework is not supported at cluster instance level.
		"""
		try :
			return self._jumbonotsupported
		except Exception as e:
			raise e

	@property
	def operationalpropstate(self) :
		ur"""Cluster Operational Propagation State.<br/>Default value: ENABLED<br/>Possible values = UNKNOWN, ENABLED, DISABLED, AUTO DISABLED.
		"""
		try :
			return self._operationalpropstate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusterinstance_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusterinstance
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
	def add(cls, client, resource) :
		ur""" Use this API to add clusterinstance.
		"""
		try :
			if type(resource) is not list :
				addresource = clusterinstance()
				addresource.clid = resource.clid
				addresource.deadinterval = resource.deadinterval
				addresource.hellointerval = resource.hellointerval
				addresource.preemption = resource.preemption
				addresource.quorumtype = resource.quorumtype
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ clusterinstance() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].clid = resource[i].clid
						addresources[i].deadinterval = resource[i].deadinterval
						addresources[i].hellointerval = resource[i].hellointerval
						addresources[i].preemption = resource[i].preemption
						addresources[i].quorumtype = resource[i].quorumtype
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete clusterinstance.
		"""
		try :
			if type(resource) is not list :
				deleteresource = clusterinstance()
				if type(resource) !=  type(deleteresource):
					deleteresource.clid = resource
				else :
					deleteresource.clid = resource.clid
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].clid = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].clid = resource[i].clid
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update clusterinstance.
		"""
		try :
			if type(resource) is not list :
				updateresource = clusterinstance()
				updateresource.clid = resource.clid
				updateresource.deadinterval = resource.deadinterval
				updateresource.hellointerval = resource.hellointerval
				updateresource.preemption = resource.preemption
				updateresource.quorumtype = resource.quorumtype
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ clusterinstance() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].clid = resource[i].clid
						updateresources[i].deadinterval = resource[i].deadinterval
						updateresources[i].hellointerval = resource[i].hellointerval
						updateresources[i].preemption = resource[i].preemption
						updateresources[i].quorumtype = resource[i].quorumtype
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of clusterinstance resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = clusterinstance()
				if type(resource) !=  type(unsetresource):
					unsetresource.clid = resource
				else :
					unsetresource.clid = resource.clid
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].clid = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].clid = resource[i].clid
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable clusterinstance.
		"""
		try :
			if type(resource) is not list :
				enableresource = clusterinstance()
				if type(resource) !=  type(enableresource):
					enableresource.clid = resource
				else :
					enableresource.clid = resource.clid
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].clid = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].clid = resource[i].clid
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable clusterinstance.
		"""
		try :
			if type(resource) is not list :
				disableresource = clusterinstance()
				if type(resource) !=  type(disableresource):
					disableresource.clid = resource
				else :
					disableresource.clid = resource.clid
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].clid = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ clusterinstance() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].clid = resource[i].clid
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the clusterinstance resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = clusterinstance()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = clusterinstance()
						obj.clid = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [clusterinstance() for _ in range(len(name))]
							obj = [clusterinstance() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = clusterinstance()
								obj[i].clid = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of clusterinstance resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusterinstance()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the clusterinstance resources configured on NetScaler.
		"""
		try :
			obj = clusterinstance()
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
		ur""" Use this API to count filtered the set of clusterinstance resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusterinstance()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Operationalpropstate:
		UNKNOWN = "UNKNOWN"
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"
		AUTO_DISABLED = "AUTO DISABLED"

	class Propstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Status:
		DOWN = "DOWN"
		UP = "UP"
		PARTIAL_UP = "PARTIAL-UP"
		UNKNOWN = "UNKNOWN"

	class Adminstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Preemption:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Operationalstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Quorumtype:
		MAJORITY = "MAJORITY"
		NONE = "NONE"

class clusterinstance_response(base_response) :
	def __init__(self, length=1) :
		self.clusterinstance = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusterinstance = [clusterinstance() for _ in range(length)]

