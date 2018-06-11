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

class service_lbmonitor_binding(base_resource) :
	""" Binding class showing the lbmonitor that can be bound to service.
	"""
	def __init__(self) :
		self._monitor_name = ""
		self._monstate = ""
		self._monitor_state = ""
		self._dup_state = ""
		self._weight = 0
		self._dup_weight = 0
		self._totalprobes = 0
		self._totalfailedprobes = 0
		self._failedprobes = 0
		self._monstatcode = 0
		self._lastresponse = ""
		self._monstatparam1 = 0
		self._monstatparam2 = 0
		self._monstatparam3 = 0
		self._responsetime = 0
		self._monitortotalprobes = 0
		self._monitortotalfailedprobes = 0
		self._monitorcurrentfailedprobes = 0
		self._passive = False
		self._name = ""
		self.___count = 0

	@property
	def weight(self) :
		ur"""Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its binding with the service determines how much the monitor contributes toward keeping the health of the service above the value configured for the Monitor Threshold parameter.<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur"""Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its binding with the service determines how much the monitor contributes toward keeping the health of the service above the value configured for the Monitor Threshold parameter.<br/>Minimum value =  1<br/>Maximum value =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name of the service to which to bind a policy or monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the service to which to bind a policy or monitor.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def passive(self) :
		ur"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			return self._passive
		except Exception as e:
			raise e

	@passive.setter
	def passive(self, passive) :
		ur"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			self._passive = passive
		except Exception as e:
			raise e

	@property
	def monitor_name(self) :
		ur"""The monitor Names.
		"""
		try :
			return self._monitor_name
		except Exception as e:
			raise e

	@monitor_name.setter
	def monitor_name(self, monitor_name) :
		ur"""The monitor Names.
		"""
		try :
			self._monitor_name = monitor_name
		except Exception as e:
			raise e

	@property
	def monstate(self) :
		ur"""The configured state (enable/disable) of the monitor on this server.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._monstate
		except Exception as e:
			raise e

	@monstate.setter
	def monstate(self, monstate) :
		ur"""The configured state (enable/disable) of the monitor on this server.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._monstate = monstate
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		ur"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def dup_weight(self) :
		ur"""The weight of the monitor.
		"""
		try :
			return self._dup_weight
		except Exception as e:
			raise e

	@property
	def responsetime(self) :
		ur"""Response time of this monitor.
		"""
		try :
			return self._responsetime
		except Exception as e:
			raise e

	@property
	def totalfailedprobes(self) :
		ur"""The total number of failed probs.
		"""
		try :
			return self._totalfailedprobes
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		ur"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def lastresponse(self) :
		ur"""The string form of monstatcode.
		"""
		try :
			return self._lastresponse
		except Exception as e:
			raise e

	@property
	def failedprobes(self) :
		ur"""Number of the current failed monitoring probes.
		"""
		try :
			return self._failedprobes
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		ur"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def totalprobes(self) :
		ur"""The total number of probs sent.
		"""
		try :
			return self._totalprobes
		except Exception as e:
			raise e

	@property
	def monitor_state(self) :
		ur"""The running state of the monitor on this service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._monitor_state
		except Exception as e:
			raise e

	@property
	def dup_state(self) :
		ur"""Added this field for getting state value from table.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dup_state
		except Exception as e:
			raise e

	@property
	def monitortotalprobes(self) :
		ur"""Total number of probes sent to monitor this service.
		"""
		try :
			return self._monitortotalprobes
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		ur"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monitortotalfailedprobes(self) :
		ur"""Total number of failed probes.
		"""
		try :
			return self._monitortotalfailedprobes
		except Exception as e:
			raise e

	@property
	def monitorcurrentfailedprobes(self) :
		ur"""Total number of currently failed probes.
		"""
		try :
			return self._monitorcurrentfailedprobes
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(service_lbmonitor_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.service_lbmonitor_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = service_lbmonitor_binding()
				updateresource.name = resource.name
				updateresource.monitor_name = resource.monitor_name
				updateresource.monstate = resource.monstate
				updateresource.weight = resource.weight
				updateresource.passive = resource.passive
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [service_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].monitor_name = resource[i].monitor_name
						updateresources[i].monstate = resource[i].monstate
						updateresources[i].weight = resource[i].weight
						updateresources[i].passive = resource[i].passive
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = service_lbmonitor_binding()
				deleteresource.name = resource.name
				deleteresource.monitor_name = resource.monitor_name
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [service_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].monitor_name = resource[i].monitor_name
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch service_lbmonitor_binding resources.
		"""
		try :
			obj = service_lbmonitor_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of service_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = service_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count service_lbmonitor_binding resources configued on NetScaler.
		"""
		try :
			obj = service_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of service_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = service_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Monitor_state:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Monstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dup_state:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class service_lbmonitor_binding_response(base_response) :
	def __init__(self, length=1) :
		self.service_lbmonitor_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.service_lbmonitor_binding = [service_lbmonitor_binding() for _ in range(length)]

