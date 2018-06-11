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

class servicegroup_servicegroupentitymonbindings_binding(base_resource) :
	""" Binding class showing the servicegroupentitymonbindings that can be bound to servicegroup.
	"""
	def __init__(self) :
		self._servicegroupentname2 = ""
		self._monitor_name = ""
		self._monitor_state = ""
		self._passive = False
		self._monitortotalprobes = 0
		self._monitortotalfailedprobes = 0
		self._monitorcurrentfailedprobes = 0
		self._lastresponse = ""
		self._servicegroupname = ""
		self._port = 0
		self._weight = 0
		self._customserverid = ""
		self._serverid = 0
		self._state = ""
		self._hashid = 0
		self.___count = 0

	@property
	def servicegroupname(self) :
		ur"""Name of the service group.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		ur"""Name of the service group.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def servicegroupentname2(self) :
		try :
			return self._servicegroupentname2
		except Exception as e:
			raise e

	@servicegroupentname2.setter
	def servicegroupentname2(self, servicegroupentname2) :
		try :
			self._servicegroupentname2 = servicegroupentname2
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port number of the service. Each service must have a unique port number.<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""Port number of the service. Each service must have a unique port number.<br/>Range 1 - 65535
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Initial state of the service after binding.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Initial state of the service after binding.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def hashid(self) :
		ur"""Unique numerical identifier used by hash based load balancing methods to identify a service.<br/>Minimum value =  1.
		"""
		try :
			return self._hashid
		except Exception as e:
			raise e

	@hashid.setter
	def hashid(self, hashid) :
		ur"""Unique numerical identifier used by hash based load balancing methods to identify a service.<br/>Minimum value =  1
		"""
		try :
			self._hashid = hashid
		except Exception as e:
			raise e

	@property
	def serverid(self) :
		ur"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			return self._serverid
		except Exception as e:
			raise e

	@serverid.setter
	def serverid(self, serverid) :
		ur"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			self._serverid = serverid
		except Exception as e:
			raise e

	@property
	def customserverid(self) :
		ur"""Unique service identifier. Used when the persistency type for the virtual server is set to Custom Server ID.<br/>Default value: "None".
		"""
		try :
			return self._customserverid
		except Exception as e:
			raise e

	@customserverid.setter
	def customserverid(self, customserverid) :
		ur"""Unique service identifier. Used when the persistency type for the virtual server is set to Custom Server ID.<br/>Default value: "None"
		"""
		try :
			self._customserverid = customserverid
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur""".<br/>Default value: 1<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur""".<br/>Default value: 1<br/>Minimum value =  1<br/>Maximum value =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def monitor_name(self) :
		ur"""Monitor name.
		"""
		try :
			return self._monitor_name
		except Exception as e:
			raise e

	@monitor_name.setter
	def monitor_name(self, monitor_name) :
		ur"""Monitor name.
		"""
		try :
			self._monitor_name = monitor_name
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
	def lastresponse(self) :
		ur"""The string form of monstatcode.
		"""
		try :
			return self._lastresponse
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
	def monitortotalprobes(self) :
		ur"""Total number of probes sent to monitor this service.
		"""
		try :
			return self._monitortotalprobes
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
			result = service.payload_formatter.string_to_resource(servicegroup_servicegroupentitymonbindings_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicegroup_servicegroupentitymonbindings_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, servicegroupname) :
		ur""" Use this API to fetch servicegroup_servicegroupentitymonbindings_binding resources.
		"""
		try :
			obj = servicegroup_servicegroupentitymonbindings_binding()
			obj.servicegroupname = servicegroupname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicegroupname, filter_) :
		ur""" Use this API to fetch filtered set of servicegroup_servicegroupentitymonbindings_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup_servicegroupentitymonbindings_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicegroupname) :
		ur""" Use this API to count servicegroup_servicegroupentitymonbindings_binding resources configued on NetScaler.
		"""
		try :
			obj = servicegroup_servicegroupentitymonbindings_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, servicegroupname, filter_) :
		ur""" Use this API to count the filtered set of servicegroup_servicegroupentitymonbindings_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup_servicegroupentitymonbindings_binding()
			obj.servicegroupname = servicegroupname
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

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Monstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class servicegroup_servicegroupentitymonbindings_binding_response(base_response) :
	def __init__(self, length=1) :
		self.servicegroup_servicegroupentitymonbindings_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.servicegroup_servicegroupentitymonbindings_binding = [servicegroup_servicegroupentitymonbindings_binding() for _ in range(length)]

