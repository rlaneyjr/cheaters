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

class cmpglobal_cmppolicy_binding(base_resource) :
	""" Binding class showing the cmppolicy that can be bound to cmpglobal.
	"""
	def __init__(self) :
		self._policyname = ""
		self._priority = 0
		self._state = ""
		self._type = ""
		self._numpol = 0
		self._policytype = ""
		self._gotopriorityexpression = ""
		self._invoke = False
		self._labeltype = ""
		self._labelname = ""
		self.___count = 0

	@property
	def priority(self) :
		ur"""Positive integer specifying the priority of the policy. The lower the number, the higher the priority. By default, polices within a label are evaluated in the order of their priority numbers.
		In the configuration utility, you can click the Priority field and edit the priority level or drag the entry to a new position in the list. If you drag the entry to a new position, the priority level is updated automatically.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Positive integer specifying the priority of the policy. The lower the number, the higher the priority. By default, polices within a label are evaluated in the order of their priority numbers.
		In the configuration utility, you can click the Priority field and edit the priority level or drag the entry to a new position in the list. If you drag the entry to a new position, the priority level is updated automatically.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""The current state of the policy binding. This attribute is relevant only for CLASSIC policies.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""The current state of the policy binding. This attribute is relevant only for CLASSIC policies.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Expression or other value specifying the priority of the next policy, within the policy label, to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher numbered priority.
		* END - Stop evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
		* An expression that evaluates to a number.
		If you specify an expression, it's evaluation result determines the next policy to evaluate, as follows: 
		* If the expression evaluates to a higher numbered priority, that policy is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher priority number is evaluated next.
		* If the expression evaluates to a priority number that is numerically higher than the highest priority number, policy evaluation ends.
		An UNDEF event is triggered if:
		* The expression is invalid.
		* The expression evaluates to a priority number that is numerically lower than the current policy's priority.
		* The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		ur"""Expression or other value specifying the priority of the next policy, within the policy label, to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher numbered priority.
		* END - Stop evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
		* An expression that evaluates to a number.
		If you specify an expression, it's evaluation result determines the next policy to evaluate, as follows: 
		* If the expression evaluates to a higher numbered priority, that policy is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher priority number is evaluated next.
		* If the expression evaluates to a priority number that is numerically higher than the highest priority number, policy evaluation ends.
		An UNDEF event is triggered if:
		* The expression is invalid.
		* The expression evaluates to a priority number that is numerically lower than the current policy's priority.
		* The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""The name of the globally bound HTTP compression policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""The name of the globally bound HTTP compression policy.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Bind point to which the policy is bound.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Bind point to which the policy is bound.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of policy label invocation. This argument is relevant only for advanced (default-syntax) policies.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		ur"""Type of policy label invocation. This argument is relevant only for advanced (default-syntax) policies.
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the label to invoke if the current policy rule evaluates to TRUE. Applicable only to advanced (default-syntax) policies.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name of the label to invoke if the current policy rule evaluates to TRUE. Applicable only to advanced (default-syntax) policies.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		ur"""Invoke policies bound to a virtual server or a policy label. After the invoked policies are evaluated, the flow returns to the policy with the next priority. Applicable only for default-syntax policies.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@invoke.setter
	def invoke(self, invoke) :
		ur"""Invoke policies bound to a virtual server or a policy label. After the invoked policies are evaluated, the flow returns to the policy with the next priority. Applicable only for default-syntax policies.
		"""
		try :
			self._invoke = invoke
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		ur"""The number of policies bound to the bindpoint.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def policytype(self) :
		ur"""Policy type (Classic/Advanced) to be bound.Used for display.<br/>Possible values = Classic Policy, Advanced Policy.
		"""
		try :
			return self._policytype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cmpglobal_cmppolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cmpglobal_cmppolicy_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cmpglobal_cmppolicy_binding()
				updateresource.policyname = resource.policyname
				updateresource.priority = resource.priority
				updateresource.state = resource.state
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.type = resource.type
				updateresource.invoke = resource.invoke
				updateresource.labeltype = resource.labeltype
				updateresource.labelname = resource.labelname
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [cmpglobal_cmppolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].priority = resource[i].priority
						updateresources[i].state = resource[i].state
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].type = resource[i].type
						updateresources[i].invoke = resource[i].invoke
						updateresources[i].labeltype = resource[i].labeltype
						updateresources[i].labelname = resource[i].labelname
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cmpglobal_cmppolicy_binding()
				deleteresource.policyname = resource.policyname
				deleteresource.type = resource.type
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [cmpglobal_cmppolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].policyname = resource[i].policyname
						deleteresources[i].type = resource[i].type
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		ur""" Use this API to fetch a cmpglobal_cmppolicy_binding resources.
		"""
		try :
			obj = cmpglobal_cmppolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		ur""" Use this API to fetch filtered set of cmpglobal_cmppolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cmpglobal_cmppolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		ur""" Use this API to count cmpglobal_cmppolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = cmpglobal_cmppolicy_binding()
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, filter_) :
		ur""" Use this API to count the filtered set of cmpglobal_cmppolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cmpglobal_cmppolicy_binding()
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

	class Type:
		REQ_OVERRIDE = "REQ_OVERRIDE"
		REQ_DEFAULT = "REQ_DEFAULT"
		RES_OVERRIDE = "RES_OVERRIDE"
		RES_DEFAULT = "RES_DEFAULT"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

	class Policytype:
		Classic_Policy = "Classic Policy"
		Advanced_Policy = "Advanced Policy"

class cmpglobal_cmppolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.cmpglobal_cmppolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cmpglobal_cmppolicy_binding = [cmpglobal_cmppolicy_binding() for _ in range(length)]

