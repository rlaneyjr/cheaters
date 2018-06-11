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

class responderglobal_responderpolicy_binding(base_resource) :
	""" Binding class showing the responderpolicy that can be bound to responderglobal.
	"""
	def __init__(self) :
		self._policyname = ""
		self._type = ""
		self._priority = 0
		self._gotopriorityexpression = ""
		self._invoke = False
		self._labeltype = ""
		self._labelname = ""
		self._numpol = 0
		self._flowtype = 0
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
	def policyname(self) :
		ur"""Name of the responder policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name of the responder policy.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the policy label to invoke. If the current policy evaluates to TRUE, the invoke parameter is set, and Label Type is policylabel.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name of the policy label to invoke. If the current policy evaluates to TRUE, the invoke parameter is set, and Label Type is policylabel.
		"""
		try :
			self._labelname = labelname
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
	def invoke(self) :
		ur"""If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forward the request to the specified virtual server or evaluate the specified policy label.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@invoke.setter
	def invoke(self, invoke) :
		ur"""If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forward the request to the specified virtual server or evaluate the specified policy label.
		"""
		try :
			self._invoke = invoke
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Specifies the bind point whose policies you want to display. Available settings function as follows:
		* REQ_OVERRIDE - Request override. Binds the policy to the priority request queue.
		* REQ_DEFAULT - Binds the policy to the default request queue.
		* OTHERTCP_REQ_OVERRIDE - Binds the policy to the non-HTTP TCP priority request queue.
		* OTHERTCP_REQ_DEFAULT - Binds the policy to the non-HTTP TCP default request queue..
		* SIPUDP_REQ_OVERRIDE - Binds the policy to the SIP UDP priority response queue..
		* SIPUDP_REQ_DEFAULT - Binds the policy to the SIP UDP default response queue.
		* MSSQL_REQ_OVERRIDE - Binds the policy to the Microsoft SQL priority response queue..
		* MSSQL_REQ_DEFAULT - Binds the policy to the Microsoft SQL default response queue.
		* MYSQL_REQ_OVERRIDE - Binds the policy to the MySQL priority response queue.
		* MYSQL_REQ_DEFAULT - Binds the policy to the MySQL default response queue.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, OVERRIDE, DEFAULT, OTHERTCP_REQ_OVERRIDE, OTHERTCP_REQ_DEFAULT, SIPUDP_REQ_OVERRIDE, SIPUDP_REQ_DEFAULT, MSSQL_REQ_OVERRIDE, MSSQL_REQ_DEFAULT, MYSQL_REQ_OVERRIDE, MYSQL_REQ_DEFAULT, NAT_REQ_OVERRIDE, NAT_REQ_DEFAULT, DIAMETER_REQ_OVERRIDE, DIAMETER_REQ_DEFAULT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Specifies the bind point whose policies you want to display. Available settings function as follows:
		* REQ_OVERRIDE - Request override. Binds the policy to the priority request queue.
		* REQ_DEFAULT - Binds the policy to the default request queue.
		* OTHERTCP_REQ_OVERRIDE - Binds the policy to the non-HTTP TCP priority request queue.
		* OTHERTCP_REQ_DEFAULT - Binds the policy to the non-HTTP TCP default request queue..
		* SIPUDP_REQ_OVERRIDE - Binds the policy to the SIP UDP priority response queue..
		* SIPUDP_REQ_DEFAULT - Binds the policy to the SIP UDP default response queue.
		* MSSQL_REQ_OVERRIDE - Binds the policy to the Microsoft SQL priority response queue..
		* MSSQL_REQ_DEFAULT - Binds the policy to the Microsoft SQL default response queue.
		* MYSQL_REQ_OVERRIDE - Binds the policy to the MySQL priority response queue.
		* MYSQL_REQ_DEFAULT - Binds the policy to the MySQL default response queue.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, OVERRIDE, DEFAULT, OTHERTCP_REQ_OVERRIDE, OTHERTCP_REQ_DEFAULT, SIPUDP_REQ_OVERRIDE, SIPUDP_REQ_DEFAULT, MSSQL_REQ_OVERRIDE, MSSQL_REQ_DEFAULT, MYSQL_REQ_OVERRIDE, MYSQL_REQ_DEFAULT, NAT_REQ_OVERRIDE, NAT_REQ_DEFAULT, DIAMETER_REQ_OVERRIDE, DIAMETER_REQ_DEFAULT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of invocation, Available settings function as follows:
		* vserver - Forward the request to the specified virtual server.
		* policylabel - Invoke the specified policy label.<br/>Possible values = vserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		ur"""Type of invocation, Available settings function as follows:
		* vserver - Forward the request to the specified virtual server.
		* policylabel - Invoke the specified policy label.<br/>Possible values = vserver, policylabel
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		ur"""number of polices bound to label.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def flowtype(self) :
		ur"""flowtype of the bound responder policy.
		"""
		try :
			return self._flowtype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(responderglobal_responderpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.responderglobal_responderpolicy_binding
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
				updateresource = responderglobal_responderpolicy_binding()
				updateresource.policyname = resource.policyname
				updateresource.priority = resource.priority
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.type = resource.type
				updateresource.invoke = resource.invoke
				updateresource.labeltype = resource.labeltype
				updateresource.labelname = resource.labelname
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [responderglobal_responderpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].priority = resource[i].priority
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
				deleteresource = responderglobal_responderpolicy_binding()
				deleteresource.policyname = resource.policyname
				deleteresource.type = resource.type
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [responderglobal_responderpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].policyname = resource[i].policyname
						deleteresources[i].type = resource[i].type
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		ur""" Use this API to fetch a responderglobal_responderpolicy_binding resources.
		"""
		try :
			obj = responderglobal_responderpolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		ur""" Use this API to fetch filtered set of responderglobal_responderpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = responderglobal_responderpolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		ur""" Use this API to count responderglobal_responderpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = responderglobal_responderpolicy_binding()
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
		ur""" Use this API to count the filtered set of responderglobal_responderpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = responderglobal_responderpolicy_binding()
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
		OVERRIDE = "OVERRIDE"
		DEFAULT = "DEFAULT"
		OTHERTCP_REQ_OVERRIDE = "OTHERTCP_REQ_OVERRIDE"
		OTHERTCP_REQ_DEFAULT = "OTHERTCP_REQ_DEFAULT"
		SIPUDP_REQ_OVERRIDE = "SIPUDP_REQ_OVERRIDE"
		SIPUDP_REQ_DEFAULT = "SIPUDP_REQ_DEFAULT"
		MSSQL_REQ_OVERRIDE = "MSSQL_REQ_OVERRIDE"
		MSSQL_REQ_DEFAULT = "MSSQL_REQ_DEFAULT"
		MYSQL_REQ_OVERRIDE = "MYSQL_REQ_OVERRIDE"
		MYSQL_REQ_DEFAULT = "MYSQL_REQ_DEFAULT"
		NAT_REQ_OVERRIDE = "NAT_REQ_OVERRIDE"
		NAT_REQ_DEFAULT = "NAT_REQ_DEFAULT"
		DIAMETER_REQ_OVERRIDE = "DIAMETER_REQ_OVERRIDE"
		DIAMETER_REQ_DEFAULT = "DIAMETER_REQ_DEFAULT"

	class Labeltype:
		vserver = "vserver"
		policylabel = "policylabel"

class responderglobal_responderpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.responderglobal_responderpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.responderglobal_responderpolicy_binding = [responderglobal_responderpolicy_binding() for _ in range(length)]

