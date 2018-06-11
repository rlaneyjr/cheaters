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

class cacheglobal_cachepolicy_binding(base_resource) :
	""" Binding class showing the cachepolicy that can be bound to cacheglobal.
	"""
	def __init__(self) :
		self._policy = ""
		self._type = ""
		self._priority = 0
		self._gotopriorityexpression = ""
		self._invoke = False
		self._labeltype = ""
		self._labelname = ""
		self._numpol = 0
		self._flowtype = 0
		self._precededefrules = ""
		self.___count = 0

	@property
	def priority(self) :
		ur"""Specifies the priority of the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Specifies the priority of the policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		ur"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def policy(self) :
		ur"""Name of the cache policy.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@policy.setter
	def policy(self, policy) :
		ur"""Name of the cache policy.
		"""
		try :
			self._policy = policy
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""The bind point to which policy is bound. When you specify the type, detailed information about that bind point appears.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""The bind point to which policy is bound. When you specify the type, detailed information about that bind point appears.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def precededefrules(self) :
		ur"""Specify whether this policy should be evaluated.
		"""
		try :
			return self._precededefrules
		except Exception as e:
			raise e

	@precededefrules.setter
	def precededefrules(self, precededefrules) :
		ur"""Specify whether this policy should be evaluated.
		"""
		try :
			self._precededefrules = precededefrules
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of policy label to invoke.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		ur"""Type of policy label to invoke.<br/>Possible values = reqvserver, resvserver, policylabel
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the label to invoke if the current policy rule evaluates to TRUE. (To invoke a label associated with a virtual server, specify the name of the virtual server.).
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name of the label to invoke if the current policy rule evaluates to TRUE. (To invoke a label associated with a virtual server, specify the name of the virtual server.).
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		ur"""Invoke policies bound to a virtual server or a user-defined policy label. After the invoked policies are evaluated, the flow returns to the policy with the next priority. Applicable only to default-syntax policies.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@invoke.setter
	def invoke(self, invoke) :
		ur"""Invoke policies bound to a virtual server or a user-defined policy label. After the invoked policies are evaluated, the flow returns to the policy with the next priority. Applicable only to default-syntax policies.
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
	def flowtype(self) :
		ur"""flowtype of the bound cache policy.
		"""
		try :
			return self._flowtype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cacheglobal_cachepolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cacheglobal_cachepolicy_binding
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
				updateresource = cacheglobal_cachepolicy_binding()
				updateresource.policy = resource.policy
				updateresource.priority = resource.priority
				updateresource.precededefrules = resource.precededefrules
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.type = resource.type
				updateresource.invoke = resource.invoke
				updateresource.labeltype = resource.labeltype
				updateresource.labelname = resource.labelname
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [cacheglobal_cachepolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policy = resource[i].policy
						updateresources[i].priority = resource[i].priority
						updateresources[i].precededefrules = resource[i].precededefrules
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
				deleteresource = cacheglobal_cachepolicy_binding()
				deleteresource.policy = resource.policy
				deleteresource.type = resource.type
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [cacheglobal_cachepolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].policy = resource[i].policy
						deleteresources[i].type = resource[i].type
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		ur""" Use this API to fetch a cacheglobal_cachepolicy_binding resources.
		"""
		try :
			obj = cacheglobal_cachepolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		ur""" Use this API to fetch filtered set of cacheglobal_cachepolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheglobal_cachepolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		ur""" Use this API to count cacheglobal_cachepolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = cacheglobal_cachepolicy_binding()
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
		ur""" Use this API to count the filtered set of cacheglobal_cachepolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheglobal_cachepolicy_binding()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Type:
		REQ_OVERRIDE = "REQ_OVERRIDE"
		REQ_DEFAULT = "REQ_DEFAULT"
		RES_OVERRIDE = "RES_OVERRIDE"
		RES_DEFAULT = "RES_DEFAULT"

	class Precededefrules:
		YES = "YES"
		NO = "NO"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

class cacheglobal_cachepolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.cacheglobal_cachepolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cacheglobal_cachepolicy_binding = [cacheglobal_cachepolicy_binding() for _ in range(length)]

