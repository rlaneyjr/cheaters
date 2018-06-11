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

class gslbsite_gslbservice_binding(base_resource) :
	""" Binding class showing the gslbservice that can be bound to gslbsite.
	"""
	def __init__(self) :
		self._servicename = ""
		self._cnameentry = ""
		self._ipaddress = ""
		self._port = 0
		self._servicetype = ""
		self._state = ""
		self._sitename = ""
		self.___count = 0

	@property
	def servicename(self) :
		ur"""Service name.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""Service name.
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def sitename(self) :
		ur"""Name of the GSLB site. If you specify a site name, details of all the site's constituent services are also displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@sitename.setter
	def sitename(self, sitename) :
		ur"""Name of the GSLB site. If you specify a site name, details of all the site's constituent services are also displayed.<br/>Minimum length =  1
		"""
		try :
			self._sitename = sitename
		except Exception as e:
			raise e

	@property
	def cnameentry(self) :
		ur"""The cname of the gslb service.<br/>Minimum length =  1.
		"""
		try :
			return self._cnameentry
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of the gslb service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		ur"""Service type.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, DNS, DHCPRA, ANY, SIP_UDP, DNS_TCP, RTSP, PUSH, SSL_PUSH, RADIUS, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port number of the gslb service.<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""IP Address of the gslb service.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbsite_gslbservice_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbsite_gslbservice_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sitename is not None :
				return str(self.sitename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, sitename) :
		ur""" Use this API to fetch gslbsite_gslbservice_binding resources.
		"""
		try :
			obj = gslbsite_gslbservice_binding()
			obj.sitename = sitename
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, sitename, filter_) :
		ur""" Use this API to fetch filtered set of gslbsite_gslbservice_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbsite_gslbservice_binding()
			obj.sitename = sitename
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, sitename) :
		ur""" Use this API to count gslbsite_gslbservice_binding resources configued on NetScaler.
		"""
		try :
			obj = gslbsite_gslbservice_binding()
			obj.sitename = sitename
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, sitename, filter_) :
		ur""" Use this API to count the filtered set of gslbsite_gslbservice_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbsite_gslbservice_binding()
			obj.sitename = sitename
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class State:
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

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		DTLS = "DTLS"
		NNTP = "NNTP"
		DNS = "DNS"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		DNS_TCP = "DNS_TCP"
		RTSP = "RTSP"
		PUSH = "PUSH"
		SSL_PUSH = "SSL_PUSH"
		RADIUS = "RADIUS"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"

class gslbsite_gslbservice_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbsite_gslbservice_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbsite_gslbservice_binding = [gslbsite_gslbservice_binding() for _ in range(length)]

