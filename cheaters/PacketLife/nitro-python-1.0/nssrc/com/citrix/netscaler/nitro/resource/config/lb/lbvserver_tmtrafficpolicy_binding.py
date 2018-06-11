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

class lbvserver_tmtrafficpolicy_binding(base_resource) :
	""" Binding class showing the tmtrafficpolicy that can be bound to lbvserver.
	"""
	def __init__(self) :
		self._policyname = ""
		self._priority = 0
		self._name = ""
		self._gotopriorityexpression = ""
		self._bindpoint = ""
		self._invoke = False
		self._labeltype = ""
		self._labelname = ""
		self.___count = 0

	@property
	def priority(self) :
		ur"""Priority.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Priority.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Expression or other value specifying the next policy to be evaluated if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
		* A default syntax expression that evaluates to a number.
		If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
		* If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
		* If the expression evaluates to a priority number that is numerically higher than the highest numbered priority, policy evaluation ends.
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
		ur"""Expression or other value specifying the next policy to be evaluated if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
		* A default syntax expression that evaluates to a number.
		If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
		* If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
		* If the expression evaluates to a priority number that is numerically higher than the highest numbered priority, policy evaluation ends.
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
		ur"""Name of the policy bound to the LB vserver.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name of the policy bound to the LB vserver.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def bindpoint(self) :
		ur"""Bind point to which to bind the policy. Applicable only to compression, rewrite, and cache policies.
		"""
		try :
			return self._bindpoint
		except Exception as e:
			raise e

	@bindpoint.setter
	def bindpoint(self, bindpoint) :
		ur"""Bind point to which to bind the policy. Applicable only to compression, rewrite, and cache policies.
		"""
		try :
			self._bindpoint = bindpoint
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of policy label to invoke. Applicable only to rewrite and cache policies. Available settings function as follows:
		* reqvserver - Evaluate the request against the request-based policies bound to the specified virtual server.
		* resvserver - Evaluate the response against the response-based policies bound to the specified virtual server.
		* policylabel - invoke the request or response against the specified user-defined policy label.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		ur"""Type of policy label to invoke. Applicable only to rewrite and cache policies. Available settings function as follows:
		* reqvserver - Evaluate the request against the request-based policies bound to the specified virtual server.
		* resvserver - Evaluate the response against the response-based policies bound to the specified virtual server.
		* policylabel - invoke the request or response against the specified user-defined policy label.
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the virtual server or user-defined policy label to invoke if the policy evaluates to TRUE.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name of the virtual server or user-defined policy label to invoke if the policy evaluates to TRUE.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		ur"""Invoke policies bound to a virtual server or policy label.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@invoke.setter
	def invoke(self, invoke) :
		ur"""Invoke policies bound to a virtual server or policy label.
		"""
		try :
			self._invoke = invoke
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbvserver_tmtrafficpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbvserver_tmtrafficpolicy_binding
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
				updateresource = lbvserver_tmtrafficpolicy_binding()
				updateresource.name = resource.name
				updateresource.policyname = resource.policyname
				updateresource.priority = resource.priority
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.bindpoint = resource.bindpoint
				updateresource.invoke = resource.invoke
				updateresource.labeltype = resource.labeltype
				updateresource.labelname = resource.labelname
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lbvserver_tmtrafficpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].priority = resource[i].priority
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].bindpoint = resource[i].bindpoint
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
				deleteresource = lbvserver_tmtrafficpolicy_binding()
				deleteresource.name = resource.name
				deleteresource.policyname = resource.policyname
				deleteresource.bindpoint = resource.bindpoint
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lbvserver_tmtrafficpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].policyname = resource[i].policyname
						deleteresources[i].bindpoint = resource[i].bindpoint
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch lbvserver_tmtrafficpolicy_binding resources.
		"""
		try :
			obj = lbvserver_tmtrafficpolicy_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of lbvserver_tmtrafficpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbvserver_tmtrafficpolicy_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count lbvserver_tmtrafficpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = lbvserver_tmtrafficpolicy_binding()
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
		ur""" Use this API to count the filtered set of lbvserver_tmtrafficpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbvserver_tmtrafficpolicy_binding()
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

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

class lbvserver_tmtrafficpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbvserver_tmtrafficpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbvserver_tmtrafficpolicy_binding = [lbvserver_tmtrafficpolicy_binding() for _ in range(length)]

