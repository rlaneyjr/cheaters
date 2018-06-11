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

class servicegroup_lbmonitor_binding(base_resource) :
	""" Binding class showing the lbmonitor that can be bound to servicegroup.
	"""
	def __init__(self) :
		self._monitor_name = ""
		self._monweight = 0
		self._monstate = ""
		self._weight = 0
		self._passive = False
		self._servicegroupname = ""
		self._port = 0
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
		ur"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum value =  1<br/>Maximum value =  100
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
	def monstate(self) :
		ur"""Monitor state.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._monstate
		except Exception as e:
			raise e

	@monstate.setter
	def monstate(self, monstate) :
		ur"""Monitor state.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._monstate = monstate
		except Exception as e:
			raise e

	@property
	def monweight(self) :
		ur"""weight of the monitor that is bound to servicegroup.
		"""
		try :
			return self._monweight
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(servicegroup_lbmonitor_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicegroup_lbmonitor_binding
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
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = servicegroup_lbmonitor_binding()
				updateresource.servicegroupname = resource.servicegroupname
				updateresource.port = resource.port
				updateresource.monitor_name = resource.monitor_name
				updateresource.monstate = resource.monstate
				updateresource.passive = resource.passive
				updateresource.weight = resource.weight
				updateresource.customserverid = resource.customserverid
				updateresource.serverid = resource.serverid
				updateresource.state = resource.state
				updateresource.hashid = resource.hashid
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [servicegroup_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicegroupname = resource[i].servicegroupname
						updateresources[i].port = resource[i].port
						updateresources[i].monitor_name = resource[i].monitor_name
						updateresources[i].monstate = resource[i].monstate
						updateresources[i].passive = resource[i].passive
						updateresources[i].weight = resource[i].weight
						updateresources[i].customserverid = resource[i].customserverid
						updateresources[i].serverid = resource[i].serverid
						updateresources[i].state = resource[i].state
						updateresources[i].hashid = resource[i].hashid
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = servicegroup_lbmonitor_binding()
				deleteresource.servicegroupname = resource.servicegroupname
				deleteresource.port = resource.port
				deleteresource.monitor_name = resource.monitor_name
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [servicegroup_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].servicegroupname = resource[i].servicegroupname
						deleteresources[i].port = resource[i].port
						deleteresources[i].monitor_name = resource[i].monitor_name
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, servicegroupname) :
		ur""" Use this API to fetch servicegroup_lbmonitor_binding resources.
		"""
		try :
			obj = servicegroup_lbmonitor_binding()
			obj.servicegroupname = servicegroupname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicegroupname, filter_) :
		ur""" Use this API to fetch filtered set of servicegroup_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup_lbmonitor_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicegroupname) :
		ur""" Use this API to count servicegroup_lbmonitor_binding resources configued on NetScaler.
		"""
		try :
			obj = servicegroup_lbmonitor_binding()
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
		ur""" Use this API to count the filtered set of servicegroup_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup_lbmonitor_binding()
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

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Monstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class servicegroup_lbmonitor_binding_response(base_response) :
	def __init__(self, length=1) :
		self.servicegroup_lbmonitor_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.servicegroup_lbmonitor_binding = [servicegroup_lbmonitor_binding() for _ in range(length)]

