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

class vpnintranetapplication(base_resource) :
	""" Configuration for SSLVPN intranet application resource. """
	def __init__(self) :
		self._intranetapplication = ""
		self._protocol = ""
		self._destip = ""
		self._netmask = ""
		self._iprange = ""
		self._hostname = ""
		self._clientapplication = []
		self._spoofiip = ""
		self._destport = ""
		self._interception = ""
		self._srcip = ""
		self._srcport = 0
		self._ipaddress = ""
		self.___count = 0

	@property
	def intranetapplication(self) :
		ur"""Name of the intranet application.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._intranetapplication
		except Exception as e:
			raise e

	@intranetapplication.setter
	def intranetapplication(self, intranetapplication) :
		ur"""Name of the intranet application.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._intranetapplication = intranetapplication
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		ur"""Protocol used by the intranet application. If protocol is set to BOTH, TCP and UDP traffic is allowed.<br/>Possible values = TCP, UDP, ANY.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		ur"""Protocol used by the intranet application. If protocol is set to BOTH, TCP and UDP traffic is allowed.<br/>Possible values = TCP, UDP, ANY
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def destip(self) :
		ur"""Destination IP address, IP range, or host name of the intranet application. This address is the server IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		ur"""Destination IP address, IP range, or host name of the intranet application. This address is the server IP address.<br/>Minimum length =  1
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""Destination subnet mask for the intranet application.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""Destination subnet mask for the intranet application.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def iprange(self) :
		ur"""If you have multiple servers in your network, such as web, email, and file shares, configure an intranet application that includes the IP range for all the network applications. This allows users to access all the intranet applications contained in the IP address range.<br/>Minimum length =  1.
		"""
		try :
			return self._iprange
		except Exception as e:
			raise e

	@iprange.setter
	def iprange(self, iprange) :
		ur"""If you have multiple servers in your network, such as web, email, and file shares, configure an intranet application that includes the IP range for all the network applications. This allows users to access all the intranet applications contained in the IP address range.<br/>Minimum length =  1
		"""
		try :
			self._iprange = iprange
		except Exception as e:
			raise e

	@property
	def hostname(self) :
		ur"""Name of the host for which to configure interception. The names are resolved during interception when users log on with the NetScaler Gateway Plug-in.<br/>Minimum length =  1.
		"""
		try :
			return self._hostname
		except Exception as e:
			raise e

	@hostname.setter
	def hostname(self, hostname) :
		ur"""Name of the host for which to configure interception. The names are resolved during interception when users log on with the NetScaler Gateway Plug-in.<br/>Minimum length =  1
		"""
		try :
			self._hostname = hostname
		except Exception as e:
			raise e

	@property
	def clientapplication(self) :
		ur"""Names of the client applications, such as PuTTY and Xshell.<br/>Minimum length =  1.
		"""
		try :
			return self._clientapplication
		except Exception as e:
			raise e

	@clientapplication.setter
	def clientapplication(self, clientapplication) :
		ur"""Names of the client applications, such as PuTTY and Xshell.<br/>Minimum length =  1
		"""
		try :
			self._clientapplication = clientapplication
		except Exception as e:
			raise e

	@property
	def spoofiip(self) :
		ur"""IP address that the intranet application will use to route the connection through the virtual adapter.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._spoofiip
		except Exception as e:
			raise e

	@spoofiip.setter
	def spoofiip(self, spoofiip) :
		ur"""IP address that the intranet application will use to route the connection through the virtual adapter.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._spoofiip = spoofiip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		ur"""Destination TCP or UDP port number for the intranet application. Use a hyphen to specify a range of port numbers, for example 90-95.<br/>Minimum length =  1.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		ur"""Destination TCP or UDP port number for the intranet application. Use a hyphen to specify a range of port numbers, for example 90-95.<br/>Minimum length =  1
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def interception(self) :
		ur"""Interception mode for the intranet application or resource. Correct value depends on the type of client software used to make connections. If the interception mode is set to TRANSPARENT, users connect with the NetScaler Gateway Plug-in for Windows. With the PROXY setting, users connect with the NetScaler Gateway Plug-in for Java.<br/>Possible values = PROXY, TRANSPARENT.
		"""
		try :
			return self._interception
		except Exception as e:
			raise e

	@interception.setter
	def interception(self, interception) :
		ur"""Interception mode for the intranet application or resource. Correct value depends on the type of client software used to make connections. If the interception mode is set to TRANSPARENT, users connect with the NetScaler Gateway Plug-in for Windows. With the PROXY setting, users connect with the NetScaler Gateway Plug-in for Java.<br/>Possible values = PROXY, TRANSPARENT
		"""
		try :
			self._interception = interception
		except Exception as e:
			raise e

	@property
	def srcip(self) :
		ur"""Source IP address. Required if interception mode is set to PROXY. Default is the loopback address, 127.0.0.1.<br/>Minimum length =  1.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		ur"""Source IP address. Required if interception mode is set to PROXY. Default is the loopback address, 127.0.0.1.<br/>Minimum length =  1
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		ur"""Source port for the application for which the NetScaler Gateway virtual server proxies the traffic. If users are connecting from a device that uses the NetScaler Gateway Plug-in for Java, applications must be configured manually by using the source IP address and TCP port values specified in the intranet application profile. If a port value is not set, the destination port value is used.<br/>Minimum length =  1.
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@srcport.setter
	def srcport(self, srcport) :
		ur"""Source port for the application for which the NetScaler Gateway virtual server proxies the traffic. If users are connecting from a device that uses the NetScaler Gateway Plug-in for Java, applications must be configured manually by using the source IP address and TCP port values specified in the intranet application profile. If a port value is not set, the destination port value is used.<br/>Minimum length =  1
		"""
		try :
			self._srcport = srcport
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""The IP address for the application. This address is the real application server IP address.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnintranetapplication_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnintranetapplication
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.intranetapplication is not None :
				return str(self.intranetapplication)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add vpnintranetapplication.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnintranetapplication()
				addresource.intranetapplication = resource.intranetapplication
				addresource.protocol = resource.protocol
				addresource.destip = resource.destip
				addresource.netmask = resource.netmask
				addresource.iprange = resource.iprange
				addresource.hostname = resource.hostname
				addresource.clientapplication = resource.clientapplication
				addresource.spoofiip = resource.spoofiip
				addresource.destport = resource.destport
				addresource.interception = resource.interception
				addresource.srcip = resource.srcip
				addresource.srcport = resource.srcport
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnintranetapplication() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].intranetapplication = resource[i].intranetapplication
						addresources[i].protocol = resource[i].protocol
						addresources[i].destip = resource[i].destip
						addresources[i].netmask = resource[i].netmask
						addresources[i].iprange = resource[i].iprange
						addresources[i].hostname = resource[i].hostname
						addresources[i].clientapplication = resource[i].clientapplication
						addresources[i].spoofiip = resource[i].spoofiip
						addresources[i].destport = resource[i].destport
						addresources[i].interception = resource[i].interception
						addresources[i].srcip = resource[i].srcip
						addresources[i].srcport = resource[i].srcport
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete vpnintranetapplication.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnintranetapplication()
				if type(resource) !=  type(deleteresource):
					deleteresource.intranetapplication = resource
				else :
					deleteresource.intranetapplication = resource.intranetapplication
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnintranetapplication() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].intranetapplication = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnintranetapplication() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].intranetapplication = resource[i].intranetapplication
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the vpnintranetapplication resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnintranetapplication()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = vpnintranetapplication()
						obj.intranetapplication = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [vpnintranetapplication() for _ in range(len(name))]
							obj = [vpnintranetapplication() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = vpnintranetapplication()
								obj[i].intranetapplication = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of vpnintranetapplication resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnintranetapplication()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the vpnintranetapplication resources configured on NetScaler.
		"""
		try :
			obj = vpnintranetapplication()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of vpnintranetapplication resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnintranetapplication()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Spoofiip:
		ON = "ON"
		OFF = "OFF"

	class Protocol:
		TCP = "TCP"
		UDP = "UDP"
		ANY = "ANY"

	class Interception:
		PROXY = "PROXY"
		TRANSPARENT = "TRANSPARENT"

class vpnintranetapplication_response(base_response) :
	def __init__(self, length=1) :
		self.vpnintranetapplication = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnintranetapplication = [vpnintranetapplication() for _ in range(length)]

