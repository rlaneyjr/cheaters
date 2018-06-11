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

class dnsaaaarec(base_resource) :
	""" Configuration for IPv6 address type record resource. """
	def __init__(self) :
		self._hostname = ""
		self._ipv6address = ""
		self._ttl = 0
		self._type = ""
		self._vservername = ""
		self._authtype = ""
		self.___count = 0

	@property
	def hostname(self) :
		ur"""Domain name.<br/>Minimum length =  1.
		"""
		try :
			return self._hostname
		except Exception as e:
			raise e

	@hostname.setter
	def hostname(self, hostname) :
		ur"""Domain name.<br/>Minimum length =  1
		"""
		try :
			self._hostname = hostname
		except Exception as e:
			raise e

	@property
	def ipv6address(self) :
		ur"""One or more IPv6 addresses to assign to the domain name.<br/>Minimum length =  1.
		"""
		try :
			return self._ipv6address
		except Exception as e:
			raise e

	@ipv6address.setter
	def ipv6address(self, ipv6address) :
		ur"""One or more IPv6 addresses to assign to the domain name.<br/>Minimum length =  1
		"""
		try :
			self._ipv6address = ipv6address
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
	def vservername(self) :
		ur"""Vitual server name.
		"""
		try :
			return self._vservername
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
			result = service.payload_formatter.string_to_resource(dnsaaaarec_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsaaaarec
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.hostname is not None :
				return str(self.hostname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add dnsaaaarec.
		"""
		try :
			if type(resource) is not list :
				addresource = dnsaaaarec()
				addresource.hostname = resource.hostname
				addresource.ipv6address = resource.ipv6address
				addresource.ttl = resource.ttl
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnsaaaarec() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].hostname = resource[i].hostname
						addresources[i].ipv6address = resource[i].ipv6address
						addresources[i].ttl = resource[i].ttl
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dnsaaaarec.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnsaaaarec()
				if type(resource) !=  type(deleteresource):
					deleteresource.hostname = resource
				else :
					deleteresource.hostname = resource.hostname
					deleteresource.ipv6address = resource.ipv6address
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsaaaarec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].hostname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsaaaarec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].hostname = resource[i].hostname
							deleteresources[i].ipv6address = resource[i].ipv6address
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnsaaaarec resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsaaaarec()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnsaaaarec() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the dnsaaaarec resources that are configured on netscaler.
	# This uses dnsaaaarec_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnsaaaarec()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnsaaaarec resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsaaaarec()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnsaaaarec resources configured on NetScaler.
		"""
		try :
			obj = dnsaaaarec()
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
		ur""" Use this API to count filtered the set of dnsaaaarec resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsaaaarec()
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

class dnsaaaarec_response(base_response) :
	def __init__(self, length=1) :
		self.dnsaaaarec = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsaaaarec = [dnsaaaarec() for _ in range(length)]

