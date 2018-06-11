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

class appfwpolicylabel_binding(base_resource):
	""" Binding class showing the resources that can be bound to appfwpolicylabel_binding. 
	"""
	def __init__(self) :
		self._labelname = ""
		self.appfwpolicylabel_policybinding_binding = []
		self.appfwpolicylabel_appfwpolicy_binding = []

	@property
	def labelname(self) :
		ur"""Name of the application firewall policy label.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name of the application firewall policy label.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def appfwpolicylabel_appfwpolicy_bindings(self) :
		ur"""appfwpolicy that can be bound to appfwpolicylabel.
		"""
		try :
			return self._appfwpolicylabel_appfwpolicy_binding
		except Exception as e:
			raise e

	@property
	def appfwpolicylabel_policybinding_bindings(self) :
		ur"""policybinding that can be bound to appfwpolicylabel.
		"""
		try :
			return self._appfwpolicylabel_policybinding_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwpolicylabel_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwpolicylabel_binding
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
	def get(self, service, labelname) :
		ur""" Use this API to fetch appfwpolicylabel_binding resource.
		"""
		try :
			if type(labelname) is not list :
				obj = appfwpolicylabel_binding()
				obj.labelname = labelname
				response = obj.get_resource(service)
			else :
				if labelname and len(labelname) > 0 :
					obj = [appfwpolicylabel_binding() for _ in range(len(labelname))]
					for i in range(len(labelname)) :
						obj[i].labelname = labelname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class appfwpolicylabel_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwpolicylabel_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwpolicylabel_binding = [appfwpolicylabel_binding() for _ in range(length)]

