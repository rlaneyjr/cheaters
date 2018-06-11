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

class clusterinstance_binding(base_resource):
	""" Binding class showing the resources that can be bound to clusterinstance_binding. 
	"""
	def __init__(self) :
		self._clid = 0
		self.clusterinstance_clusternode_binding = []

	@property
	def clid(self) :
		ur"""Unique number that identifies the cluster.<br/>Minimum value =  1<br/>Maximum value =  16.
		"""
		try :
			return self._clid
		except Exception as e:
			raise e

	@clid.setter
	def clid(self, clid) :
		ur"""Unique number that identifies the cluster.<br/>Minimum value =  1<br/>Maximum value =  16
		"""
		try :
			self._clid = clid
		except Exception as e:
			raise e

	@property
	def clusterinstance_clusternode_bindings(self) :
		ur"""clusternode that can be bound to clusterinstance.
		"""
		try :
			return self._clusterinstance_clusternode_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusterinstance_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusterinstance_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.clid is not None :
				return str(self.clid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, clid) :
		ur""" Use this API to fetch clusterinstance_binding resource.
		"""
		try :
			if type(clid) is not list :
				obj = clusterinstance_binding()
				obj.clid = clid
				response = obj.get_resource(service)
			else :
				if clid and len(clid) > 0 :
					obj = [clusterinstance_binding() for _ in range(len(clid))]
					for i in range(len(clid)) :
						obj[i].clid = clid[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class clusterinstance_binding_response(base_response) :
	def __init__(self, length=1) :
		self.clusterinstance_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusterinstance_binding = [clusterinstance_binding() for _ in range(length)]

