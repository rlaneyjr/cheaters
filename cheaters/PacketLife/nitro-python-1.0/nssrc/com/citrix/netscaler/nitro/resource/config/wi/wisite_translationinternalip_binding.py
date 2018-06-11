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

class wisite_translationinternalip_binding(base_resource) :
	""" Binding class showing the translationinternalip that can be bound to wisite.
	"""
	def __init__(self) :
		self._translationinternalip = ""
		self._accesstype = ""
		self._translationinternalport = 0
		self._translationexternalip = ""
		self._translationexternalport = 0
		self._sitepath = ""
		self.___count = 0

	@property
	def sitepath(self) :
		ur"""Path to the Web Interface site.<br/>Minimum length =  1<br/>Maximum length =  250.
		"""
		try :
			return self._sitepath
		except Exception as e:
			raise e

	@sitepath.setter
	def sitepath(self, sitepath) :
		ur"""Path to the Web Interface site.<br/>Minimum length =  1<br/>Maximum length =  250
		"""
		try :
			self._sitepath = sitepath
		except Exception as e:
			raise e

	@property
	def accesstype(self) :
		ur"""Type of access to the XenApp or XenDesktop server. 
		Available settings function as follows:
		* User Device - Clients can use the translated address of the mapping entry to connect to the XenApp or XenDesktop server.
		* Gateway - Access Gateway can use the translated address of the mapping entry to connect to the XenApp or XenDesktop server.
		* User Device and Gateway - Both clients and Access Gateway can use the translated address of the mapping entry to connect to the XenApp or XenDesktop server.<br/>Default value: UserDevice<br/>Possible values = UserDevice, Gateway, UserDeviceAndGateway.
		"""
		try :
			return self._accesstype
		except Exception as e:
			raise e

	@accesstype.setter
	def accesstype(self, accesstype) :
		ur"""Type of access to the XenApp or XenDesktop server. 
		Available settings function as follows:
		* User Device - Clients can use the translated address of the mapping entry to connect to the XenApp or XenDesktop server.
		* Gateway - Access Gateway can use the translated address of the mapping entry to connect to the XenApp or XenDesktop server.
		* User Device and Gateway - Both clients and Access Gateway can use the translated address of the mapping entry to connect to the XenApp or XenDesktop server.<br/>Default value: UserDevice<br/>Possible values = UserDevice, Gateway, UserDeviceAndGateway
		"""
		try :
			self._accesstype = accesstype
		except Exception as e:
			raise e

	@property
	def translationexternalport(self) :
		ur"""External port number associated with the server's port number.<br/>Range 1 - 65535.
		"""
		try :
			return self._translationexternalport
		except Exception as e:
			raise e

	@translationexternalport.setter
	def translationexternalport(self, translationexternalport) :
		ur"""External port number associated with the server's port number.<br/>Range 1 - 65535
		"""
		try :
			self._translationexternalport = translationexternalport
		except Exception as e:
			raise e

	@property
	def translationinternalip(self) :
		ur"""IP address of the server for which you want to associate an external IP address. (Clients access the server through the associated external address and port.).<br/>Default value: 0.
		"""
		try :
			return self._translationinternalip
		except Exception as e:
			raise e

	@translationinternalip.setter
	def translationinternalip(self, translationinternalip) :
		ur"""IP address of the server for which you want to associate an external IP address. (Clients access the server through the associated external address and port.).<br/>Default value: 0
		"""
		try :
			self._translationinternalip = translationinternalip
		except Exception as e:
			raise e

	@property
	def translationexternalip(self) :
		ur"""External IP address associated with server's IP address.
		"""
		try :
			return self._translationexternalip
		except Exception as e:
			raise e

	@translationexternalip.setter
	def translationexternalip(self, translationexternalip) :
		ur"""External IP address associated with server's IP address.
		"""
		try :
			self._translationexternalip = translationexternalip
		except Exception as e:
			raise e

	@property
	def translationinternalport(self) :
		ur"""Port number of the server for which you want to associate an external port.  (Clients access the server through the associated external address and port.).<br/>Range 1 - 65535.
		"""
		try :
			return self._translationinternalport
		except Exception as e:
			raise e

	@translationinternalport.setter
	def translationinternalport(self, translationinternalport) :
		ur"""Port number of the server for which you want to associate an external port.  (Clients access the server through the associated external address and port.).<br/>Range 1 - 65535
		"""
		try :
			self._translationinternalport = translationinternalport
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wisite_translationinternalip_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wisite_translationinternalip_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sitepath is not None :
				return str(self.sitepath)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = wisite_translationinternalip_binding()
				updateresource.sitepath = resource.sitepath
				updateresource.translationinternalip = resource.translationinternalip
				updateresource.translationinternalport = resource.translationinternalport
				updateresource.translationexternalip = resource.translationexternalip
				updateresource.translationexternalport = resource.translationexternalport
				updateresource.accesstype = resource.accesstype
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [wisite_translationinternalip_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].sitepath = resource[i].sitepath
						updateresources[i].translationinternalip = resource[i].translationinternalip
						updateresources[i].translationinternalport = resource[i].translationinternalport
						updateresources[i].translationexternalip = resource[i].translationexternalip
						updateresources[i].translationexternalport = resource[i].translationexternalport
						updateresources[i].accesstype = resource[i].accesstype
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = wisite_translationinternalip_binding()
				deleteresource.sitepath = resource.sitepath
				deleteresource.translationinternalip = resource.translationinternalip
				deleteresource.translationinternalport = resource.translationinternalport
				deleteresource.translationexternalip = resource.translationexternalip
				deleteresource.translationexternalport = resource.translationexternalport
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [wisite_translationinternalip_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].sitepath = resource[i].sitepath
						deleteresources[i].translationinternalip = resource[i].translationinternalip
						deleteresources[i].translationinternalport = resource[i].translationinternalport
						deleteresources[i].translationexternalip = resource[i].translationexternalip
						deleteresources[i].translationexternalport = resource[i].translationexternalport
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, sitepath) :
		ur""" Use this API to fetch wisite_translationinternalip_binding resources.
		"""
		try :
			obj = wisite_translationinternalip_binding()
			obj.sitepath = sitepath
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, sitepath, filter_) :
		ur""" Use this API to fetch filtered set of wisite_translationinternalip_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite_translationinternalip_binding()
			obj.sitepath = sitepath
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, sitepath) :
		ur""" Use this API to count wisite_translationinternalip_binding resources configued on NetScaler.
		"""
		try :
			obj = wisite_translationinternalip_binding()
			obj.sitepath = sitepath
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, sitepath, filter_) :
		ur""" Use this API to count the filtered set of wisite_translationinternalip_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite_translationinternalip_binding()
			obj.sitepath = sitepath
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Accessmethod:
		Direct = "Direct"
		Alternate = "Alternate"
		Translated = "Translated"
		GatewayDirect = "GatewayDirect"
		GatewayAlternate = "GatewayAlternate"
		GatewayTranslated = "GatewayTranslated"

	class Accesstype:
		UserDevice = "UserDevice"
		Gateway = "Gateway"
		UserDeviceAndGateway = "UserDeviceAndGateway"

	class Transport:
		HTTP = "HTTP"
		HTTPS = "HTTPS"
		SSLRELAY = "SSLRELAY"

	class Loadbalance:
		ON = "ON"
		OFF = "OFF"

	class Recoveryfarm:
		ON = "ON"
		OFF = "OFF"

class wisite_translationinternalip_binding_response(base_response) :
	def __init__(self, length=1) :
		self.wisite_translationinternalip_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wisite_translationinternalip_binding = [wisite_translationinternalip_binding() for _ in range(length)]

