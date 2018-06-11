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

class gslbvserver_gslbservice_binding(base_resource) :
	""" Binding class showing the gslbservice that can be bound to gslbvserver.
	"""
	def __init__(self) :
		self._servicename = ""
		self._weight = 0
		self._cnameentry = ""
		self._ipaddress = ""
		self._port = 0
		self._gslbboundsvctype = ""
		self._curstate = ""
		self._dynamicconfwt = 0
		self._cumulativeweight = 0
		self._svreffgslbstate = ""
		self._gslbthreshold = 0
		self._preferredlocation = ""
		self._thresholdvalue = 0
		self._iscname = ""
		self._domainname = ""
		self._sitepersistcookie = ""
		self._svcsitepersistence = ""
		self._name = ""
		self.___count = 0

	@property
	def weight(self) :
		ur"""Weight to assign to the GSLB service.<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur"""Weight to assign to the GSLB service.<br/>Minimum value =  1<br/>Maximum value =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name of the virtual server on which to perform the binding operation.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the virtual server on which to perform the binding operation.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""Name of the GSLB service for which to change the weight.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""Name of the GSLB service for which to change the weight.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def domainname(self) :
		ur"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._domainname
		except Exception as e:
			raise e

	@domainname.setter
	def domainname(self, domainname) :
		ur"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1
		"""
		try :
			self._domainname = domainname
		except Exception as e:
			raise e

	@property
	def cnameentry(self) :
		ur"""The cname of the gslb service.
		"""
		try :
			return self._cnameentry
		except Exception as e:
			raise e

	@property
	def svcsitepersistence(self) :
		ur"""Type of Site Persistence set on the bound service.<br/>Possible values = ConnectionProxy, HTTPRedirect, NONE.
		"""
		try :
			return self._svcsitepersistence
		except Exception as e:
			raise e

	@property
	def gslbboundsvctype(self) :
		ur"""Protocol used by services bound to the GSLBvirtual server.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE.
		"""
		try :
			return self._gslbboundsvctype
		except Exception as e:
			raise e

	@property
	def preferredlocation(self) :
		ur"""The target site to be returned in the DNS response when a policy is successfully evaluated against the incoming DNS request. Target site is specified in dotted notation with up to 6 qualifiers. Wildcard `*' is accepted as a valid qualifier token.
		"""
		try :
			return self._preferredlocation
		except Exception as e:
			raise e

	@property
	def dynamicconfwt(self) :
		ur"""Weight obtained by the virtue of bound service count or weight.
		"""
		try :
			return self._dynamicconfwt
		except Exception as e:
			raise e

	@property
	def cumulativeweight(self) :
		ur"""Cumulative weight is the weight of GSLB service considering both its configured weight and dynamic weight. It is equal to product of dynamic weight and configured weight of the gslb service .
		"""
		try :
			return self._cumulativeweight
		except Exception as e:
			raise e

	@property
	def gslbthreshold(self) :
		ur"""Indicates if gslb svc has reached threshold.
		"""
		try :
			return self._gslbthreshold
		except Exception as e:
			raise e

	@property
	def sitepersistcookie(self) :
		ur"""This field is introduced for displaying the cookie in cluster setup.<br/>Minimum length =  1.
		"""
		try :
			return self._sitepersistcookie
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port number.<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@property
	def iscname(self) :
		ur"""is cname feature set on vserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._iscname
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		ur"""State of the gslb vserver.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def svreffgslbstate(self) :
		ur"""Effective state of the gslb svc.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svreffgslbstate
		except Exception as e:
			raise e

	@property
	def thresholdvalue(self) :
		ur"""Tells whether threshold exceeded for this service participating in CUSTOMLB.
		"""
		try :
			return self._thresholdvalue
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""IP address.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbvserver_gslbservice_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbvserver_gslbservice_binding
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
				updateresource = gslbvserver_gslbservice_binding()
				updateresource.name = resource.name
				updateresource.servicename = resource.servicename
				updateresource.weight = resource.weight
				updateresource.domainname = resource.domainname
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [gslbvserver_gslbservice_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].servicename = resource[i].servicename
						updateresources[i].weight = resource[i].weight
						updateresources[i].domainname = resource[i].domainname
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = gslbvserver_gslbservice_binding()
				deleteresource.name = resource.name
				deleteresource.servicename = resource.servicename
				deleteresource.domainname = resource.domainname
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [gslbvserver_gslbservice_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].servicename = resource[i].servicename
						deleteresources[i].domainname = resource[i].domainname
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch gslbvserver_gslbservice_binding resources.
		"""
		try :
			obj = gslbvserver_gslbservice_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of gslbvserver_gslbservice_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbvserver_gslbservice_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count gslbvserver_gslbservice_binding resources configued on NetScaler.
		"""
		try :
			obj = gslbvserver_gslbservice_binding()
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
		ur""" Use this API to count the filtered set of gslbvserver_gslbservice_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbvserver_gslbservice_binding()
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

	class Svcsitepersistence:
		ConnectionProxy = "ConnectionProxy"
		HTTPRedirect = "HTTPRedirect"
		NONE = "NONE"

	class Svreffgslbstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Type:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"

	class Gslbboundsvctype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		NNTP = "NNTP"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		RADIUS = "RADIUS"
		RDP = "RDP"
		RTSP = "RTSP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"

	class Iscname:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Curstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

class gslbvserver_gslbservice_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbvserver_gslbservice_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbvserver_gslbservice_binding = [gslbvserver_gslbservice_binding() for _ in range(length)]

