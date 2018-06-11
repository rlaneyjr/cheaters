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

class dnsnsecrec(base_resource) :
	def __init__(self) :
		self._hostname = ""
		self._type = ""
		self._nextnsec = ""
		self._nextrecs = []
		self._ttl = 0
		self.___count = 0

	@property
	def hostname(self) :
		ur"""Name of the domain.<br/>Minimum length =  1.
		"""
		try :
			return self._hostname
		except Exception as e:
			raise e

	@hostname.setter
	def hostname(self, hostname) :
		ur"""Name of the domain.<br/>Minimum length =  1
		"""
		try :
			self._hostname = hostname
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
	def nextnsec(self) :
		ur"""Next nsec record in the chain.
		"""
		try :
			return self._nextnsec
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

	@property
	def ttl(self) :
		ur"""Time to Live (TTL), in seconds, for the record.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsnsecrec_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsnsecrec
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
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnsnsecrec resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsnsecrec()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = dnsnsecrec()
						obj.hostname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnsnsecrec() for _ in range(len(name))]
							obj = [dnsnsecrec() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = dnsnsecrec()
								obj[i].hostname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the dnsnsecrec resources that are configured on netscaler.
	# This uses dnsnsecrec_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnsnsecrec()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnsnsecrec resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsnsecrec()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnsnsecrec resources configured on NetScaler.
		"""
		try :
			obj = dnsnsecrec()
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
		ur""" Use this API to count filtered the set of dnsnsecrec resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsnsecrec()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		ALL = "ALL"
		ADNS = "ADNS"
		PROXY = "PROXY"

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

class dnsnsecrec_response(base_response) :
	def __init__(self, length=1) :
		self.dnsnsecrec = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsnsecrec = [dnsnsecrec() for _ in range(length)]

