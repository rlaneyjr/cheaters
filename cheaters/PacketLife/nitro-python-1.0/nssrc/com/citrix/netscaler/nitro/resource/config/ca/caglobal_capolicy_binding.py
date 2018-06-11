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

class caglobal_capolicy_binding(base_resource) :
	""" Binding class showing the capolicy that can be bound to caglobal.
	"""
	def __init__(self) :
		self._policyname = ""
		self._type = ""
		self._priority = 0
		self._gotopriorityexpression = ""
		self._numpol = 0
		self._flowtype = 0
		self.___count = 0

	@property
	def priority(self) :
		ur"""Specifies the priority of the content accelerator policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Specifies the priority of the content accelerator policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""Name of the content accelerator policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name of the content accelerator policy.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur""".<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur""".<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, RES_OVERRIDE, RES_DEFAULT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		ur"""Number of polices bound to label.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def flowtype(self) :
		ur"""flowtype of the bound content accelerator policy.
		"""
		try :
			return self._flowtype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(caglobal_capolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.caglobal_capolicy_binding
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
				updateresource = caglobal_capolicy_binding()
				updateresource.policyname = resource.policyname
				updateresource.priority = resource.priority
				updateresource.gotopriorityexpression = resource.gotopriorityexpression
				updateresource.type = resource.type
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [caglobal_capolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].priority = resource[i].priority
						updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
						updateresources[i].type = resource[i].type
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = caglobal_capolicy_binding()
				deleteresource.policyname = resource.policyname
				deleteresource.type = resource.type
				deleteresource.priority = resource.priority
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [caglobal_capolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].policyname = resource[i].policyname
						deleteresources[i].type = resource[i].type
						deleteresources[i].priority = resource[i].priority
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		ur""" Use this API to fetch a caglobal_capolicy_binding resources.
		"""
		try :
			obj = caglobal_capolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		ur""" Use this API to fetch filtered set of caglobal_capolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = caglobal_capolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		ur""" Use this API to count caglobal_capolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = caglobal_capolicy_binding()
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
		ur""" Use this API to count the filtered set of caglobal_capolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = caglobal_capolicy_binding()
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

class caglobal_capolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.caglobal_capolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.caglobal_capolicy_binding = [caglobal_capolicy_binding() for _ in range(length)]

