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

class transformpolicylabel_policybinding_binding(base_resource) :
	""" Binding class showing the policybinding that can be bound to transformpolicylabel.
	"""
	def __init__(self) :
		self._policyname = ""
		self._priority = 0
		self._gotopriorityexpression = ""
		self._invoke = False
		self._labeltype = ""
		self._invoke_labelname = ""
		self._labelname = ""
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
	def policyname(self) :
		ur"""Name of the URL Transformation policy to bind to the policy label.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name of the URL Transformation policy to bind to the policy label.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of invocation. Available settings function as follows:
		* reqvserver - Forward the request to the specified request virtual server.
		* policylabel - Invoke the specified policy label.<br/>Possible values = reqvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		ur"""Type of invocation. Available settings function as follows:
		* reqvserver - Forward the request to the specified request virtual server.
		* policylabel - Invoke the specified policy label.<br/>Possible values = reqvserver, policylabel
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the URL Transformation policy label to which to bind the policy.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name of the URL Transformation policy label to which to bind the policy.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def invoke_labelname(self) :
		ur"""Name of the policy label.
		"""
		try :
			return self._invoke_labelname
		except Exception as e:
			raise e

	@invoke_labelname.setter
	def invoke_labelname(self, invoke_labelname) :
		ur"""Name of the policy label.
		"""
		try :
			self._invoke_labelname = invoke_labelname
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

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(transformpolicylabel_policybinding_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.transformpolicylabel_policybinding_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.labelname is not None :
				return str(self.labelname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, labelname) :
		ur""" Use this API to fetch transformpolicylabel_policybinding_binding resources.
		"""
		try :
			obj = transformpolicylabel_policybinding_binding()
			obj.labelname = labelname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, labelname, filter_) :
		ur""" Use this API to fetch filtered set of transformpolicylabel_policybinding_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformpolicylabel_policybinding_binding()
			obj.labelname = labelname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, labelname) :
		ur""" Use this API to count transformpolicylabel_policybinding_binding resources configued on NetScaler.
		"""
		try :
			obj = transformpolicylabel_policybinding_binding()
			obj.labelname = labelname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, labelname, filter_) :
		ur""" Use this API to count the filtered set of transformpolicylabel_policybinding_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformpolicylabel_policybinding_binding()
			obj.labelname = labelname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Labeltype:
		reqvserver = "reqvserver"
		policylabel = "policylabel"

class transformpolicylabel_policybinding_binding_response(base_response) :
	def __init__(self, length=1) :
		self.transformpolicylabel_policybinding_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.transformpolicylabel_policybinding_binding = [transformpolicylabel_policybinding_binding() for _ in range(length)]

