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

class csvserver_lbvserver_binding(base_resource) :
	""" Binding class showing the lbvserver that can be bound to csvserver.
	"""
	def __init__(self) :
		self._lbvserver = ""
		self._hits = 0
		self._name = ""
		self._targetvserver = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the content switching virtual server to which the content switching policy applies.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the content switching virtual server to which the content switching policy applies.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def targetvserver(self) :
		ur"""The virtual server name (created with the add lb vserver command) to which content will be switched.
		"""
		try :
			return self._targetvserver
		except Exception as e:
			raise e

	@targetvserver.setter
	def targetvserver(self, targetvserver) :
		ur"""The virtual server name (created with the add lb vserver command) to which content will be switched.
		"""
		try :
			self._targetvserver = targetvserver
		except Exception as e:
			raise e

	@property
	def lbvserver(self) :
		ur"""Name of the default lb vserver bound. Use this param for Default binding only. For Example: bind cs vserver cs1 -lbvserver lb1.<br/>Minimum length =  1.
		"""
		try :
			return self._lbvserver
		except Exception as e:
			raise e

	@lbvserver.setter
	def lbvserver(self, lbvserver) :
		ur"""Name of the default lb vserver bound. Use this param for Default binding only. For Example: bind cs vserver cs1 -lbvserver lb1.<br/>Minimum length =  1
		"""
		try :
			self._lbvserver = lbvserver
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(csvserver_lbvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.csvserver_lbvserver_binding
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
				updateresource = csvserver_lbvserver_binding()
				updateresource.name = resource.name
				updateresource.lbvserver = resource.lbvserver
				updateresource.targetvserver = resource.targetvserver
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [csvserver_lbvserver_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].lbvserver = resource[i].lbvserver
						updateresources[i].targetvserver = resource[i].targetvserver
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = csvserver_lbvserver_binding()
				deleteresource.name = resource.name
				deleteresource.lbvserver = resource.lbvserver
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [csvserver_lbvserver_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].lbvserver = resource[i].lbvserver
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch csvserver_lbvserver_binding resources.
		"""
		try :
			obj = csvserver_lbvserver_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of csvserver_lbvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = csvserver_lbvserver_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count csvserver_lbvserver_binding resources configued on NetScaler.
		"""
		try :
			obj = csvserver_lbvserver_binding()
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
		ur""" Use this API to count the filtered set of csvserver_lbvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = csvserver_lbvserver_binding()
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

class csvserver_lbvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.csvserver_lbvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.csvserver_lbvserver_binding = [csvserver_lbvserver_binding() for _ in range(length)]

