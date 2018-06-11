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

class wisite_farmname_binding(base_resource) :
	""" Binding class showing the farmname that can be bound to wisite.
	"""
	def __init__(self) :
		self._farmname = ""
		self._xmlserveraddresses = ""
		self._xmlport = 0
		self._transport = ""
		self._sslrelayport = 0
		self._loadbalance = ""
		self._groups = ""
		self._recoveryfarm = ""
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
	def groups(self) :
		ur"""Active Directory groups that are permitted to enumerate resources from server farms. Including a setting for this parameter activates the user roaming feature. A maximum of 512 user groups can be specified for each farm defined with the Farm<n> parameter.  The groups must be comma separated.
		"""
		try :
			return self._groups
		except Exception as e:
			raise e

	@groups.setter
	def groups(self, groups) :
		ur"""Active Directory groups that are permitted to enumerate resources from server farms. Including a setting for this parameter activates the user roaming feature. A maximum of 512 user groups can be specified for each farm defined with the Farm<n> parameter.  The groups must be comma separated.
		"""
		try :
			self._groups = groups
		except Exception as e:
			raise e

	@property
	def xmlport(self) :
		ur"""Port number at which to contact the XML service.
		"""
		try :
			return self._xmlport
		except Exception as e:
			raise e

	@xmlport.setter
	def xmlport(self, xmlport) :
		ur"""Port number at which to contact the XML service.
		"""
		try :
			self._xmlport = xmlport
		except Exception as e:
			raise e

	@property
	def transport(self) :
		ur"""Transport protocol to use for transferring data, related to the Web Interface site, between the NetScaler appliance and the XML service.<br/>Possible values = HTTP, HTTPS, SSLRELAY.
		"""
		try :
			return self._transport
		except Exception as e:
			raise e

	@transport.setter
	def transport(self, transport) :
		ur"""Transport protocol to use for transferring data, related to the Web Interface site, between the NetScaler appliance and the XML service.<br/>Possible values = HTTP, HTTPS, SSLRELAY
		"""
		try :
			self._transport = transport
		except Exception as e:
			raise e

	@property
	def sslrelayport(self) :
		ur"""TCP port at which the XenApp or XenDesktop servers listenfor SSL Relay traffic from the NetScaler appliance. This parameter is required if you have set SSL Relay as the transport protocol. 
		Web Interface uses root certificates when authenticating a server running SSL Relay. Make sure that all the servers running SSL Relay are configured to listen on the same port.
		"""
		try :
			return self._sslrelayport
		except Exception as e:
			raise e

	@sslrelayport.setter
	def sslrelayport(self, sslrelayport) :
		ur"""TCP port at which the XenApp or XenDesktop servers listenfor SSL Relay traffic from the NetScaler appliance. This parameter is required if you have set SSL Relay as the transport protocol. 
		Web Interface uses root certificates when authenticating a server running SSL Relay. Make sure that all the servers running SSL Relay are configured to listen on the same port.
		"""
		try :
			self._sslrelayport = sslrelayport
		except Exception as e:
			raise e

	@property
	def farmname(self) :
		ur"""Name for the logical representation of a XenApp or XenDesktop farm to be bound to the Web Interface site. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			return self._farmname
		except Exception as e:
			raise e

	@farmname.setter
	def farmname(self, farmname) :
		ur"""Name for the logical representation of a XenApp or XenDesktop farm to be bound to the Web Interface site. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			self._farmname = farmname
		except Exception as e:
			raise e

	@property
	def loadbalance(self) :
		ur"""Use all the XML servers (load balancing mode) or only one server (failover mode).<br/>Possible values = ON, OFF.
		"""
		try :
			return self._loadbalance
		except Exception as e:
			raise e

	@loadbalance.setter
	def loadbalance(self, loadbalance) :
		ur"""Use all the XML servers (load balancing mode) or only one server (failover mode).<br/>Possible values = ON, OFF
		"""
		try :
			self._loadbalance = loadbalance
		except Exception as e:
			raise e

	@property
	def recoveryfarm(self) :
		ur"""Binded farm is set as a recovery farm.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._recoveryfarm
		except Exception as e:
			raise e

	@recoveryfarm.setter
	def recoveryfarm(self, recoveryfarm) :
		ur"""Binded farm is set as a recovery farm.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._recoveryfarm = recoveryfarm
		except Exception as e:
			raise e

	@property
	def xmlserveraddresses(self) :
		ur"""Comma-separated IP addresses or host names of XenApp or XenDesktop servers providing XML services.
		"""
		try :
			return self._xmlserveraddresses
		except Exception as e:
			raise e

	@xmlserveraddresses.setter
	def xmlserveraddresses(self, xmlserveraddresses) :
		ur"""Comma-separated IP addresses or host names of XenApp or XenDesktop servers providing XML services.
		"""
		try :
			self._xmlserveraddresses = xmlserveraddresses
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wisite_farmname_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wisite_farmname_binding
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
				updateresource = wisite_farmname_binding()
				updateresource.sitepath = resource.sitepath
				updateresource.farmname = resource.farmname
				updateresource.xmlserveraddresses = resource.xmlserveraddresses
				updateresource.groups = resource.groups
				updateresource.recoveryfarm = resource.recoveryfarm
				updateresource.xmlport = resource.xmlport
				updateresource.transport = resource.transport
				updateresource.sslrelayport = resource.sslrelayport
				updateresource.loadbalance = resource.loadbalance
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [wisite_farmname_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].sitepath = resource[i].sitepath
						updateresources[i].farmname = resource[i].farmname
						updateresources[i].xmlserveraddresses = resource[i].xmlserveraddresses
						updateresources[i].groups = resource[i].groups
						updateresources[i].recoveryfarm = resource[i].recoveryfarm
						updateresources[i].xmlport = resource[i].xmlport
						updateresources[i].transport = resource[i].transport
						updateresources[i].sslrelayport = resource[i].sslrelayport
						updateresources[i].loadbalance = resource[i].loadbalance
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = wisite_farmname_binding()
				deleteresource.sitepath = resource.sitepath
				deleteresource.farmname = resource.farmname
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [wisite_farmname_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].sitepath = resource[i].sitepath
						deleteresources[i].farmname = resource[i].farmname
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, sitepath) :
		ur""" Use this API to fetch wisite_farmname_binding resources.
		"""
		try :
			obj = wisite_farmname_binding()
			obj.sitepath = sitepath
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, sitepath, filter_) :
		ur""" Use this API to fetch filtered set of wisite_farmname_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite_farmname_binding()
			obj.sitepath = sitepath
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, sitepath) :
		ur""" Use this API to count wisite_farmname_binding resources configued on NetScaler.
		"""
		try :
			obj = wisite_farmname_binding()
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
		ur""" Use this API to count the filtered set of wisite_farmname_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = wisite_farmname_binding()
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

class wisite_farmname_binding_response(base_response) :
	def __init__(self, length=1) :
		self.wisite_farmname_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wisite_farmname_binding = [wisite_farmname_binding() for _ in range(length)]

