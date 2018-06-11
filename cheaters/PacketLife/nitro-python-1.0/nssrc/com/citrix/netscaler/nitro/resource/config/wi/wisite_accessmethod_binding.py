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

class wisite_accessmethod_binding(base_resource) :
	""" Binding class showing the accessmethod that can be bound to wisite.
	"""
	def __init__(self) :
		self._accessmethod = ""
		self._clientipaddress = ""
		self._clientnetmask = ""
		self._sitepath = ""
		self.___count = 0

	@property
	def clientipaddress(self) :
		ur"""IPv4 or network address of the client for which you want to associate an access method.<br/>Default value: 0.
		"""
		try :
			return self._clientipaddress
		except Exception as e:
			raise e

	@clientipaddress.setter
	def clientipaddress(self, clientipaddress) :
		ur"""IPv4 or network address of the client for which you want to associate an access method.<br/>Default value: 0
		"""
		try :
			self._clientipaddress = clientipaddress
		except Exception as e:
			raise e

	@property
	def clientnetmask(self) :
		ur"""Subnet mask associated with the IPv4 or network address specified by the Client IP Address parameter.<br/>Default value: 0.
		"""
		try :
			return self._clientnetmask
		except Exception as e:
			raise e

	@clientnetmask.setter
	def clientnetmask(self, clientnetmask) :
		ur"""Subnet mask associated with the IPv4 or network address specified by the Client IP Address parameter.<br/>Default value: 0
		"""
		try :
			self._clientnetmask = clientnetmask
		except Exception as e:
			raise e

	@property
	def accessmethod(self) :
		ur"""Secure access method to be applied to the IPv4 or network address of the client specified by the Client IP Address parameter.
		Depending on whether the Web Interface site is configured to use an HTTP or HTTPS virtual server or to use access gateway, you can send clients or access gateway the IP address, or the alternate address, of a XenApp or XenDesktop server. Or, you can send the IP address translated from a mapping entry, which defines mapping of an internal address and port to an external address and port.<br/>Possible values = Direct, Alternate, Translated, GatewayDirect, GatewayAlternate, GatewayTranslated.
		"""
		try :
			return self._accessmethod
		except Exception as e:
			raise e

	@accessmethod.setter
	def accessmethod(self, accessmethod) :
		ur"""Secure access method to be applied to the IPv4 or network address of the client specified by the Client IP Address parameter.
		Depending on whether the Web Interface site is configured to use an HTTP or HTTPS virtual server or to use access gateway, you can send clients or access gateway the IP address, or the alternate address, of a XenApp or XenDesktop server. Or, you can send the IP address translated from a mapping entry, which defines mapping of an internal address and port to an external address and port.<br/>Possible values = Direct, Alternate, Translated, GatewayDirect, GatewayAlternate, GatewayTranslated
		"""
		try :
			self._accessmethod = accessmethod
		except Exception as e:
			raise e

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

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wisite_accessmethod_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wisite_accessmethod_binding
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
				updateresource = wisite_accessmethod_binding()
				updateresource.sitepath = resource.sitepath
				updateresource.accessmethod = resource.accessmethod
				updateresource.clientipaddress = resource.clientipaddress
				updateresource.clientnetmask = resource.clientnetmask
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [wisite_accessmethod_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].sitepath = resource[i].sitepath
						updateresources[i].accessmethod = resource[i].accessmethod
						updateresources[i].clientipaddress = resource[i].clientipaddress
						updateresources[i].clientnetmask = resource[i].clientnetmask
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = wisite_accessmethod_binding()
				deleteresource.sitepath = resource.sitepath
				deleteresource.clientipaddress = resource.clientipaddress
				deleteresource.clientnetmask = resource.clientnetmask
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [wisite_accessmethod_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].sitepath = resource[i].sitepath
						deleteresources[i].clientipaddress = resource[i].clientipaddress
						deleteresources[i].clientnetmask = resource[i].clientnetmask
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, sitepath) :
		ur""" Use this API to fetch wisite_accessmethod_binding resources.
		"""
		try :
			obj = wisite_accessmethod_binding()
			obj.sitepath = sitepath
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, sitepath, filter_) :
		ur""" Use this API to fetch filtered set of wisite_accessmethod_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite_accessmethod_binding()
			obj.sitepath = sitepath
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, sitepath) :
		ur""" Use this API to count wisite_accessmethod_binding resources configued on NetScaler.
		"""
		try :
			obj = wisite_accessmethod_binding()
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
		ur""" Use this API to count the filtered set of wisite_accessmethod_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite_accessmethod_binding()
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

class wisite_accessmethod_binding_response(base_response) :
	def __init__(self, length=1) :
		self.wisite_accessmethod_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wisite_accessmethod_binding = [wisite_accessmethod_binding() for _ in range(length)]

