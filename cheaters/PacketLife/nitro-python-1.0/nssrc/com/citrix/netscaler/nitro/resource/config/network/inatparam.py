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

class inatparam(base_resource) :
	""" Configuration for INAT parameter resource. """
	def __init__(self) :
		self._nat46v6prefix = ""
		self._td = 0
		self._nat46ignoretos = ""
		self._nat46zerochecksum = ""
		self._nat46v6mtu = 0
		self._nat46fragheader = ""
		self.___count = 0

	@property
	def nat46v6prefix(self) :
		ur"""The prefix used for translating packets received from private IPv6 servers into IPv4 packets. This prefix has a length of 96 bits (128-32 = 96). The IPv6 servers embed the destination IP address of the IPv4 servers or hosts in the last 32 bits of the destination IP address field of the IPv6 packets. The first 96 bits of the destination IP address field are set as the IPv6 NAT prefix. IPv6 packets addressed to this prefix have to be routed to the NetScaler appliance to ensure that the IPv6-IPv4 translation is done by the appliance.
		"""
		try :
			return self._nat46v6prefix
		except Exception as e:
			raise e

	@nat46v6prefix.setter
	def nat46v6prefix(self, nat46v6prefix) :
		ur"""The prefix used for translating packets received from private IPv6 servers into IPv4 packets. This prefix has a length of 96 bits (128-32 = 96). The IPv6 servers embed the destination IP address of the IPv4 servers or hosts in the last 32 bits of the destination IP address field of the IPv6 packets. The first 96 bits of the destination IP address field are set as the IPv6 NAT prefix. IPv6 packets addressed to this prefix have to be routed to the NetScaler appliance to ensure that the IPv6-IPv4 translation is done by the appliance.
		"""
		try :
			self._nat46v6prefix = nat46v6prefix
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def nat46ignoretos(self) :
		ur"""Ignore TOS.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._nat46ignoretos
		except Exception as e:
			raise e

	@nat46ignoretos.setter
	def nat46ignoretos(self, nat46ignoretos) :
		ur"""Ignore TOS.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._nat46ignoretos = nat46ignoretos
		except Exception as e:
			raise e

	@property
	def nat46zerochecksum(self) :
		ur"""Calculate checksum for UDP packets with zero checksum.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nat46zerochecksum
		except Exception as e:
			raise e

	@nat46zerochecksum.setter
	def nat46zerochecksum(self, nat46zerochecksum) :
		ur"""Calculate checksum for UDP packets with zero checksum.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nat46zerochecksum = nat46zerochecksum
		except Exception as e:
			raise e

	@property
	def nat46v6mtu(self) :
		ur"""MTU setting for the IPv6 side. If the incoming IPv4 packet greater than this, either fragment or send icmp need fragmentation error.<br/>Default value: 1280<br/>Minimum length =  1280<br/>Maximum length =  9216.
		"""
		try :
			return self._nat46v6mtu
		except Exception as e:
			raise e

	@nat46v6mtu.setter
	def nat46v6mtu(self, nat46v6mtu) :
		ur"""MTU setting for the IPv6 side. If the incoming IPv4 packet greater than this, either fragment or send icmp need fragmentation error.<br/>Default value: 1280<br/>Minimum length =  1280<br/>Maximum length =  9216
		"""
		try :
			self._nat46v6mtu = nat46v6mtu
		except Exception as e:
			raise e

	@property
	def nat46fragheader(self) :
		ur"""When disabled, translator will not insert IPv6 fragmentation header for non fragmented IPv4 packets.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nat46fragheader
		except Exception as e:
			raise e

	@nat46fragheader.setter
	def nat46fragheader(self, nat46fragheader) :
		ur"""When disabled, translator will not insert IPv6 fragmentation header for non fragmented IPv4 packets.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nat46fragheader = nat46fragheader
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(inatparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.inatparam
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.td is not None :
				return str(self.td)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update inatparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = inatparam()
				updateresource.nat46v6prefix = resource.nat46v6prefix
				updateresource.td = resource.td
				updateresource.nat46ignoretos = resource.nat46ignoretos
				updateresource.nat46zerochecksum = resource.nat46zerochecksum
				updateresource.nat46v6mtu = resource.nat46v6mtu
				updateresource.nat46fragheader = resource.nat46fragheader
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ inatparam() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].nat46v6prefix = resource[i].nat46v6prefix
						updateresources[i].td = resource[i].td
						updateresources[i].nat46ignoretos = resource[i].nat46ignoretos
						updateresources[i].nat46zerochecksum = resource[i].nat46zerochecksum
						updateresources[i].nat46v6mtu = resource[i].nat46v6mtu
						updateresources[i].nat46fragheader = resource[i].nat46fragheader
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of inatparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = inatparam()
				if type(resource) !=  type(unsetresource):
					unsetresource.td = resource
				else :
					unsetresource.td = resource.td
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ inatparam() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].td = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ inatparam() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].td = resource[i].td
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the inatparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = inatparam()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = inatparam()
						obj.td = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [inatparam() for _ in range(len(name))]
							obj = [inatparam() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = inatparam()
								obj[i].td = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of inatparam resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = inatparam()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the inatparam resources configured on NetScaler.
		"""
		try :
			obj = inatparam()
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
		ur""" Use this API to count filtered the set of inatparam resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = inatparam()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Nat46zerochecksum:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nat46ignoretos:
		YES = "YES"
		NO = "NO"

	class Nat46fragheader:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class inatparam_response(base_response) :
	def __init__(self, length=1) :
		self.inatparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.inatparam = [inatparam() for _ in range(length)]

