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

class dnszone_domain_binding(base_resource) :
	""" Binding class showing the domain that can be bound to dnszone.
	"""
	def __init__(self) :
		self._domain = ""
		self._nextrecs = []
		self._zonename = ""
		self.___count = 0

	@property
	def zonename(self) :
		ur"""Name of the zone. Mutually exclusive with the type parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._zonename
		except Exception as e:
			raise e

	@zonename.setter
	def zonename(self, zonename) :
		ur"""Name of the zone. Mutually exclusive with the type parameter.<br/>Minimum length =  1
		"""
		try :
			self._zonename = zonename
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""Domain name that belongs to the given zone.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""Domain name that belongs to the given zone.
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def nextrecs(self) :
		ur"""An array of record types associated with the nsec record.<br/>Possible values = A, NS, CNAME, SOA, MX, AAAA, SRV, RRSIG, NSEC, DNSKEY, PTR, TXT, NAPTR.
		"""
		try :
			return self._nextrecs
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnszone_domain_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnszone_domain_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.zonename is not None :
				return str(self.zonename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, zonename) :
		ur""" Use this API to fetch dnszone_domain_binding resources.
		"""
		try :
			obj = dnszone_domain_binding()
			obj.zonename = zonename
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, zonename, filter_) :
		ur""" Use this API to fetch filtered set of dnszone_domain_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnszone_domain_binding()
			obj.zonename = zonename
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, zonename) :
		ur""" Use this API to count dnszone_domain_binding resources configued on NetScaler.
		"""
		try :
			obj = dnszone_domain_binding()
			obj.zonename = zonename
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, zonename, filter_) :
		ur""" Use this API to count the filtered set of dnszone_domain_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnszone_domain_binding()
			obj.zonename = zonename
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Nextrecs:
		A = "A"
		NS = "NS"
		CNAME = "CNAME"
		SOA = "SOA"
		MX = "MX"
		AAAA = "AAAA"
		SRV = "SRV"
		RRSIG = "RRSIG"
		NSEC = "NSEC"
		DNSKEY = "DNSKEY"
		PTR = "PTR"
		TXT = "TXT"
		NAPTR = "NAPTR"

class dnszone_domain_binding_response(base_response) :
	def __init__(self, length=1) :
		self.dnszone_domain_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnszone_domain_binding = [dnszone_domain_binding() for _ in range(length)]

