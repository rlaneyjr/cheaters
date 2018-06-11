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

class lbmonitor_servicegroup_binding(base_resource) :
	""" Binding class showing the servicegroup that can be bound to lbmonitor.
	"""
	def __init__(self) :
		self._monitorname = ""
		self._servicename = ""
		self._dup_state = ""
		self._dup_weight = 0
		self._servicegroupname = ""
		self._state = ""
		self._weight = 0

	@property
	def servicegroupname(self) :
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def dup_state(self) :
		ur"""State of the monitor. The state setting for a monitor of a given type affects all monitors of that type. For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled. If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.
		"""
		try :
			return self._dup_state
		except Exception as e:
			raise e

	@dup_state.setter
	def dup_state(self, dup_state) :
		ur"""State of the monitor. The state setting for a monitor of a given type affects all monitors of that type. For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled. If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.
		"""
		try :
			self._dup_state = dup_state
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of the monitor. The state setting for a monitor of a given type affects all monitors of that type. For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled. If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""State of the monitor. The state setting for a monitor of a given type affects all monitors of that type. For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled. If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def dup_weight(self) :
		ur"""Weight to assign to the binding between the monitor and service.
		"""
		try :
			return self._dup_weight
		except Exception as e:
			raise e

	@dup_weight.setter
	def dup_weight(self, dup_weight) :
		ur"""Weight to assign to the binding between the monitor and service.
		"""
		try :
			self._dup_weight = dup_weight
		except Exception as e:
			raise e

	@property
	def monitorname(self) :
		ur"""Name of the monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._monitorname
		except Exception as e:
			raise e

	@monitorname.setter
	def monitorname(self, monitorname) :
		ur"""Name of the monitor.<br/>Minimum length =  1
		"""
		try :
			self._monitorname = monitorname
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Weight to assign to the binding between the monitor and service.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur"""Weight to assign to the binding between the monitor and service.
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmonitor_servicegroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmonitor_servicegroup_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.monitorname is not None :
				return str(self.monitorname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = lbmonitor_servicegroup_binding()
				updateresource.monitorname = resource.monitorname
				updateresource.servicename = resource.servicename
				updateresource.dup_state = resource.dup_state
				updateresource.dup_weight = resource.dup_weight
				updateresource.servicegroupname = resource.servicegroupname
				updateresource.state = resource.state
				updateresource.weight = resource.weight
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lbmonitor_servicegroup_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].monitorname = resource[i].monitorname
						updateresources[i].servicename = resource[i].servicename
						updateresources[i].dup_state = resource[i].dup_state
						updateresources[i].dup_weight = resource[i].dup_weight
						updateresources[i].servicegroupname = resource[i].servicegroupname
						updateresources[i].state = resource[i].state
						updateresources[i].weight = resource[i].weight
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = lbmonitor_servicegroup_binding()
				deleteresource.monitorname = resource.monitorname
				deleteresource.servicename = resource.servicename
				deleteresource.servicegroupname = resource.servicegroupname
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lbmonitor_servicegroup_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].monitorname = resource[i].monitorname
						deleteresources[i].servicename = resource[i].servicename
						deleteresources[i].servicegroupname = resource[i].servicegroupname
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	class Dup_state:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lbmonitor_servicegroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbmonitor_servicegroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmonitor_servicegroup_binding = [lbmonitor_servicegroup_binding() for _ in range(length)]

