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

class aaauser_vpnintranetapplication_binding(base_resource) :
	""" Binding class showing the vpnintranetapplication that can be bound to aaauser.
	"""
	def __init__(self) :
		self._intranetapplication = ""
		self._acttype = 0
		self._username = ""
		self.___count = 0

	@property
	def username(self) :
		ur"""User account to which to bind the policy.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""User account to which to bind the policy.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def intranetapplication(self) :
		ur"""Name of the intranet VPN application to which the policy applies.
		"""
		try :
			return self._intranetapplication
		except Exception as e:
			raise e

	@intranetapplication.setter
	def intranetapplication(self, intranetapplication) :
		ur"""Name of the intranet VPN application to which the policy applies.
		"""
		try :
			self._intranetapplication = intranetapplication
		except Exception as e:
			raise e

	@property
	def acttype(self) :
		try :
			return self._acttype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaauser_vpnintranetapplication_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaauser_vpnintranetapplication_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.username is not None :
				return str(self.username)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = aaauser_vpnintranetapplication_binding()
				updateresource.username = resource.username
				updateresource.intranetapplication = resource.intranetapplication
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [aaauser_vpnintranetapplication_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].username = resource[i].username
						updateresources[i].intranetapplication = resource[i].intranetapplication
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = aaauser_vpnintranetapplication_binding()
				deleteresource.username = resource.username
				deleteresource.intranetapplication = resource.intranetapplication
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [aaauser_vpnintranetapplication_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].username = resource[i].username
						deleteresources[i].intranetapplication = resource[i].intranetapplication
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, username) :
		ur""" Use this API to fetch aaauser_vpnintranetapplication_binding resources.
		"""
		try :
			obj = aaauser_vpnintranetapplication_binding()
			obj.username = username
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, username, filter_) :
		ur""" Use this API to fetch filtered set of aaauser_vpnintranetapplication_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaauser_vpnintranetapplication_binding()
			obj.username = username
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, username) :
		ur""" Use this API to count aaauser_vpnintranetapplication_binding resources configued on NetScaler.
		"""
		try :
			obj = aaauser_vpnintranetapplication_binding()
			obj.username = username
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, username, filter_) :
		ur""" Use this API to count the filtered set of aaauser_vpnintranetapplication_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaauser_vpnintranetapplication_binding()
			obj.username = username
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class aaauser_vpnintranetapplication_binding_response(base_response) :
	def __init__(self, length=1) :
		self.aaauser_vpnintranetapplication_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaauser_vpnintranetapplication_binding = [aaauser_vpnintranetapplication_binding() for _ in range(length)]

