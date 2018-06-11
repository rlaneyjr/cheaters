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

class dnsptrrec(base_resource) :
	""" Configuration for PTR record resource. """
	def __init__(self) :
		self._reversedomain = ""
		self._domain = ""
		self._ttl = 0
		self._type = ""
		self._authtype = ""
		self.___count = 0

	@property
	def reversedomain(self) :
		ur"""Reversed domain name representation of the IPv4 or IPv6 address for which to create the PTR record. Use the "in-addr.arpa." suffix for IPv4 addresses and the "ip6.arpa." suffix for IPv6 addresses.<br/>Minimum length =  1.
		"""
		try :
			return self._reversedomain
		except Exception as e:
			raise e

	@reversedomain.setter
	def reversedomain(self, reversedomain) :
		ur"""Reversed domain name representation of the IPv4 or IPv6 address for which to create the PTR record. Use the "in-addr.arpa." suffix for IPv4 addresses and the "ip6.arpa." suffix for IPv6 addresses.<br/>Minimum length =  1
		"""
		try :
			self._reversedomain = reversedomain
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""Domain name for which to configure reverse mapping.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""Domain name for which to configure reverse mapping.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		ur"""Time to Live (TTL), in seconds, for the record. TTL is the time for which the record must be cached by DNS proxies. The specified TTL is applied to all the resource records that are of the same record type and belong to the specified domain name. For example, if you add an address record, with a TTL of 36000, to the domain name example.com, the TTLs of all the address records of example.com are changed to 36000. If the TTL is not specified, the NetScaler appliance uses either the DNS zone's minimum TTL or, if the SOA record is not available on the appliance, the default value of 3600.<br/>Default value: 3600<br/>Maximum length =  2147483647.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		ur"""Time to Live (TTL), in seconds, for the record. TTL is the time for which the record must be cached by DNS proxies. The specified TTL is applied to all the resource records that are of the same record type and belong to the specified domain name. For example, if you add an address record, with a TTL of 36000, to the domain name example.com, the TTLs of all the address records of example.com are changed to 36000. If the TTL is not specified, the NetScaler appliance uses either the DNS zone's minimum TTL or, if the SOA record is not available on the appliance, the default value of 3600.<br/>Default value: 3600<br/>Maximum length =  2147483647
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of records to display. Available settings function as follows:
		* ADNS - Display all authoritative address records.
		* PROXY - Display all proxy address records.
		* ALL - Display all address records.<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of records to display. Available settings function as follows:
		* ADNS - Display all authoritative address records.
		* PROXY - Display all proxy address records.
		* ALL - Display all address records.<br/>Possible values = ALL, ADNS, PROXY
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def authtype(self) :
		ur"""Authentication type.<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._authtype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsptrrec_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsptrrec
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.reversedomain is not None :
				return str(self.reversedomain)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add dnsptrrec.
		"""
		try :
			if type(resource) is not list :
				addresource = dnsptrrec()
				addresource.reversedomain = resource.reversedomain
				addresource.domain = resource.domain
				addresource.ttl = resource.ttl
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnsptrrec() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].reversedomain = resource[i].reversedomain
						addresources[i].domain = resource[i].domain
						addresources[i].ttl = resource[i].ttl
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dnsptrrec.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnsptrrec()
				if type(resource) !=  type(deleteresource):
					deleteresource.reversedomain = resource
				else :
					deleteresource.reversedomain = resource.reversedomain
					deleteresource.domain = resource.domain
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsptrrec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].reversedomain = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsptrrec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].reversedomain = resource[i].reversedomain
							deleteresources[i].domain = resource[i].domain
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnsptrrec resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsptrrec()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = dnsptrrec()
						obj.reversedomain = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnsptrrec() for _ in range(len(name))]
							obj = [dnsptrrec() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = dnsptrrec()
								obj[i].reversedomain = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the dnsptrrec resources that are configured on netscaler.
	# This uses dnsptrrec_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnsptrrec()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnsptrrec resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsptrrec()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnsptrrec resources configured on NetScaler.
		"""
		try :
			obj = dnsptrrec()
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
		ur""" Use this API to count filtered the set of dnsptrrec resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsptrrec()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Authtype:
		ALL = "ALL"
		ADNS = "ADNS"
		PROXY = "PROXY"

	class Type:
		ALL = "ALL"
		ADNS = "ADNS"
		PROXY = "PROXY"

class dnsptrrec_response(base_response) :
	def __init__(self, length=1) :
		self.dnsptrrec = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsptrrec = [dnsptrrec() for _ in range(length)]

