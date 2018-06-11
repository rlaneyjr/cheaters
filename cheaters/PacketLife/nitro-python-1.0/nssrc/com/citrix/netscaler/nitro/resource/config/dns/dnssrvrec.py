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

class dnssrvrec(base_resource) :
	""" Configuration for server record resource. """
	def __init__(self) :
		self._domain = ""
		self._target = ""
		self._priority = 0
		self._weight = 0
		self._port = 0
		self._ttl = 0
		self._type = ""
		self._authtype = ""
		self.___count = 0

	@property
	def domain(self) :
		ur"""Domain name, which, by convention, is prefixed by the symbolic name of the desired service and the symbolic name of the desired protocol, each with an underscore (_) prepended. For example, if an SRV-aware client wants to discover a SIP service that is provided over UDP, in the domain example.com, the client performs a lookup for _sip._udp.example.com.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""Domain name, which, by convention, is prefixed by the symbolic name of the desired service and the symbolic name of the desired protocol, each with an underscore (_) prepended. For example, if an SRV-aware client wants to discover a SIP service that is provided over UDP, in the domain example.com, the client performs a lookup for _sip._udp.example.com.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def target(self) :
		ur"""Target host for the specified service.
		"""
		try :
			return self._target
		except Exception as e:
			raise e

	@target.setter
	def target(self, target) :
		ur"""Target host for the specified service.
		"""
		try :
			self._target = target
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Integer specifying the priority of the target host. The lower the number, the higher the priority. If multiple target hosts have the same priority, selection is based on the Weight parameter.<br/>Maximum length =  65535.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Integer specifying the priority of the target host. The lower the number, the higher the priority. If multiple target hosts have the same priority, selection is based on the Weight parameter.<br/>Maximum length =  65535
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Weight for the target host. Aids host selection when two or more hosts have the same priority. A larger number indicates greater weight.<br/>Maximum length =  65535.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur"""Weight for the target host. Aids host selection when two or more hosts have the same priority. A larger number indicates greater weight.<br/>Maximum length =  65535
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port on which the target host listens for client requests.<br/>Maximum length =  65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""Port on which the target host listens for client requests.<br/>Maximum length =  65535
		"""
		try :
			self._port = port
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
		ur"""Record type.<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._authtype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnssrvrec_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnssrvrec
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.domain is not None :
				return str(self.domain)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add dnssrvrec.
		"""
		try :
			if type(resource) is not list :
				addresource = dnssrvrec()
				addresource.domain = resource.domain
				addresource.target = resource.target
				addresource.priority = resource.priority
				addresource.weight = resource.weight
				addresource.port = resource.port
				addresource.ttl = resource.ttl
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnssrvrec() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].domain = resource[i].domain
						addresources[i].target = resource[i].target
						addresources[i].priority = resource[i].priority
						addresources[i].weight = resource[i].weight
						addresources[i].port = resource[i].port
						addresources[i].ttl = resource[i].ttl
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dnssrvrec.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnssrvrec()
				if type(resource) !=  type(deleteresource):
					deleteresource.domain = resource
				else :
					deleteresource.domain = resource.domain
					deleteresource.target = resource.target
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnssrvrec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].domain = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnssrvrec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].domain = resource[i].domain
							deleteresources[i].target = resource[i].target
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update dnssrvrec.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnssrvrec()
				updateresource.domain = resource.domain
				updateresource.target = resource.target
				updateresource.priority = resource.priority
				updateresource.weight = resource.weight
				updateresource.port = resource.port
				updateresource.ttl = resource.ttl
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnssrvrec() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].domain = resource[i].domain
						updateresources[i].target = resource[i].target
						updateresources[i].priority = resource[i].priority
						updateresources[i].weight = resource[i].weight
						updateresources[i].port = resource[i].port
						updateresources[i].ttl = resource[i].ttl
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of dnssrvrec resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnssrvrec()
				unsetresource.domain = resource.domain
				unsetresource.target = resource.target
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) == cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnssrvrec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].domain = resource[i].domain
							unsetresources[i].target = resource[i].target
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnssrvrec resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnssrvrec()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnssrvrec() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the dnssrvrec resources that are configured on netscaler.
	# This uses dnssrvrec_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnssrvrec()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnssrvrec resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnssrvrec()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnssrvrec resources configured on NetScaler.
		"""
		try :
			obj = dnssrvrec()
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
		ur""" Use this API to count filtered the set of dnssrvrec resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnssrvrec()
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

class dnssrvrec_response(base_response) :
	def __init__(self, length=1) :
		self.dnssrvrec = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnssrvrec = [dnssrvrec() for _ in range(length)]

