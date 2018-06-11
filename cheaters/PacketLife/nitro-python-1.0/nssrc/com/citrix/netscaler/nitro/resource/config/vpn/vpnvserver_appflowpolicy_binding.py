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

class vpnvserver_appflowpolicy_binding(base_resource) :
	""" Binding class showing the appflowpolicy that can be bound to vpnvserver.
	"""
	def __init__(self) :
		self._policy = ""
		self._priority = 0
		self._gotopriorityexpression = ""
		self._bindpoint = ""
		self._name = ""
		self._secondary = False
		self._groupextraction = False
		self.___count = 0

	@property
	def priority(self) :
		ur"""The priority, if any, of the VPN virtual server policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""The priority, if any, of the VPN virtual server policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Next priority expression.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		ur"""Next priority expression.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def policy(self) :
		ur"""The name of the policy, if any, bound to the VPN virtual server.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@policy.setter
	def policy(self, policy) :
		ur"""The name of the policy, if any, bound to the VPN virtual server.
		"""
		try :
			self._policy = policy
		except Exception as e:
			raise e

	@property
	def groupextraction(self) :
		ur"""Binds the authentication policy to a tertiary chain which will be used only for group extraction.  The user will not authenticate against this server, and this will only be called if primary and/or secondary authentication has succeeded.
		"""
		try :
			return self._groupextraction
		except Exception as e:
			raise e

	@groupextraction.setter
	def groupextraction(self, groupextraction) :
		ur"""Binds the authentication policy to a tertiary chain which will be used only for group extraction.  The user will not authenticate against this server, and this will only be called if primary and/or secondary authentication has succeeded.
		"""
		try :
			self._groupextraction = groupextraction
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name of the virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the virtual server.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def secondary(self) :
		ur"""Binds the authentication policy as the secondary policy to use in a two-factor configuration. A user must then authenticate not only via a primary authentication method but also via a secondary authentication method. User groups are aggregated across both. The user name must be exactly the same for both authentication methods, but they can require different passwords.
		"""
		try :
			return self._secondary
		except Exception as e:
			raise e

	@secondary.setter
	def secondary(self, secondary) :
		ur"""Binds the authentication policy as the secondary policy to use in a two-factor configuration. A user must then authenticate not only via a primary authentication method but also via a secondary authentication method. User groups are aggregated across both. The user name must be exactly the same for both authentication methods, but they can require different passwords.
		"""
		try :
			self._secondary = secondary
		except Exception as e:
			raise e

	@property
	def bindpoint(self) :
		ur"""Bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE, ICA_REQUEST, OTHERTCP_REQUEST.
		"""
		try :
			return self._bindpoint
		except Exception as e:
			raise e

	@bindpoint.setter
	def bindpoint(self, bindpoint) :
		ur"""Bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE, ICA_REQUEST, OTHERTCP_REQUEST
		"""
		try :
			self._bindpoint = bindpoint
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnvserver_appflowpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnvserver_appflowpolicy_binding
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
				updateresource = vpnvserver_appflowpolicy_binding()
				updateresource.name = resource.name
				updateresource.policy = resource.policy
				updateresource.priority = resource.priority
				updateresource.secondary = resource.secondary
				updateresource.groupextraction = resource.groupextraction
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.bindpoint = resource.bindpoint
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vpnvserver_appflowpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].policy = resource[i].policy
						updateresources[i].priority = resource[i].priority
						updateresources[i].secondary = resource[i].secondary
						updateresources[i].groupextraction = resource[i].groupextraction
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].bindpoint = resource[i].bindpoint
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = vpnvserver_appflowpolicy_binding()
				deleteresource.name = resource.name
				deleteresource.policy = resource.policy
				deleteresource.secondary = resource.secondary
				deleteresource.groupextraction = resource.groupextraction
				deleteresource.bindpoint = resource.bindpoint
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vpnvserver_appflowpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].policy = resource[i].policy
						deleteresources[i].secondary = resource[i].secondary
						deleteresources[i].groupextraction = resource[i].groupextraction
						deleteresources[i].bindpoint = resource[i].bindpoint
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch vpnvserver_appflowpolicy_binding resources.
		"""
		try :
			obj = vpnvserver_appflowpolicy_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of vpnvserver_appflowpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver_appflowpolicy_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count vpnvserver_appflowpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = vpnvserver_appflowpolicy_binding()
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
		ur""" Use this API to count the filtered set of vpnvserver_appflowpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver_appflowpolicy_binding()
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

	class Staaddresstype:
		IPV4 = "IPV4"
		IPV6 = "IPV6"

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		ICA_REQUEST = "ICA_REQUEST"
		OTHERTCP_REQUEST = "OTHERTCP_REQUEST"

class vpnvserver_appflowpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vpnvserver_appflowpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnvserver_appflowpolicy_binding = [vpnvserver_appflowpolicy_binding() for _ in range(length)]

