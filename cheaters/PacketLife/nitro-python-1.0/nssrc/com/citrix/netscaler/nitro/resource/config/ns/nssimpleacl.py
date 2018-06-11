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

class nssimpleacl(base_resource) :
	""" Configuration for simple ACL resource. """
	def __init__(self) :
		self._aclname = ""
		self._aclaction = ""
		self._td = 0
		self._srcip = ""
		self._destport = 0
		self._protocol = ""
		self._ttl = 0
		self._estsessions = False
		self._hits = 0
		self.___count = 0

	@property
	def aclname(self) :
		ur"""Name for the simple ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the simple ACL rule is created.<br/>Minimum length =  1.
		"""
		try :
			return self._aclname
		except Exception as e:
			raise e

	@aclname.setter
	def aclname(self, aclname) :
		ur"""Name for the simple ACL rule. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the simple ACL rule is created.<br/>Minimum length =  1
		"""
		try :
			self._aclname = aclname
		except Exception as e:
			raise e

	@property
	def aclaction(self) :
		ur"""Drop incoming IPv4 packets that match the simple ACL rule.<br/>Possible values = DENY.
		"""
		try :
			return self._aclaction
		except Exception as e:
			raise e

	@aclaction.setter
	def aclaction(self, aclaction) :
		ur"""Drop incoming IPv4 packets that match the simple ACL rule.<br/>Possible values = DENY
		"""
		try :
			self._aclaction = aclaction
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
	def srcip(self) :
		ur"""IP address to match against the source IP address of an incoming IPv4 packet.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		ur"""IP address to match against the source IP address of an incoming IPv4 packet.
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		ur"""Port number to match against the destination port number of an incoming IPv4 packet.
		Omitting the port number creates an all-ports simple ACL rule, which matches any port. In that case, you cannot create another simple ACL rule specifying a specific port and the same source IPv4 address.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		ur"""Port number to match against the destination port number of an incoming IPv4 packet.
		Omitting the port number creates an all-ports simple ACL rule, which matches any port. In that case, you cannot create another simple ACL rule specifying a specific port and the same source IPv4 address.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		ur"""Protocol to match against the protocol of an incoming IPv4 packet. You must set this parameter if you have set the Destination Port parameter.<br/>Possible values = TCP, UDP.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		ur"""Protocol to match against the protocol of an incoming IPv4 packet. You must set this parameter if you have set the Destination Port parameter.<br/>Possible values = TCP, UDP
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		ur"""Number of seconds, in multiples of four, after which the simple ACL rule expires. If you do not want the simple ACL rule to expire, do not specify a TTL value.<br/>Minimum length =  4<br/>Maximum length =  0x7FFFFFFF.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		ur"""Number of seconds, in multiples of four, after which the simple ACL rule expires. If you do not want the simple ACL rule to expire, do not specify a TTL value.<br/>Minimum length =  4<br/>Maximum length =  0x7FFFFFFF
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def estsessions(self) :
		try :
			return self._estsessions
		except Exception as e:
			raise e

	@estsessions.setter
	def estsessions(self, estsessions) :
		try :
			self._estsessions = estsessions
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Number of hits for this ACL rule.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nssimpleacl_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nssimpleacl
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.aclname is not None :
				return str(self.aclname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add nssimpleacl.
		"""
		try :
			if type(resource) is not list :
				addresource = nssimpleacl()
				addresource.aclname = resource.aclname
				addresource.aclaction = resource.aclaction
				addresource.td = resource.td
				addresource.srcip = resource.srcip
				addresource.destport = resource.destport
				addresource.protocol = resource.protocol
				addresource.ttl = resource.ttl
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nssimpleacl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].aclname = resource[i].aclname
						addresources[i].aclaction = resource[i].aclaction
						addresources[i].td = resource[i].td
						addresources[i].srcip = resource[i].srcip
						addresources[i].destport = resource[i].destport
						addresources[i].protocol = resource[i].protocol
						addresources[i].ttl = resource[i].ttl
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource="") :
		ur""" Use this API to clear nssimpleacl.
		"""
		try :
			if type(resource) is not list :
				clearresource = nssimpleacl()
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ nssimpleacl() for _ in range(len(resource))]
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nssimpleacl.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nssimpleacl()
				if type(resource) !=  type(deleteresource):
					deleteresource.aclname = resource
				else :
					deleteresource.aclname = resource.aclname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nssimpleacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nssimpleacl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].aclname = resource[i].aclname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def flush(cls, client, resource) :
		ur""" Use this API to flush nssimpleacl.
		"""
		try :
			if type(resource) is not list :
				flushresource = nssimpleacl()
				flushresource.estsessions = resource.estsessions
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ nssimpleacl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						flushresources[i].estsessions = resource[i].estsessions
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nssimpleacl resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nssimpleacl()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nssimpleacl()
						obj.aclname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nssimpleacl() for _ in range(len(name))]
							obj = [nssimpleacl() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nssimpleacl()
								obj[i].aclname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nssimpleacl resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nssimpleacl()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nssimpleacl resources configured on NetScaler.
		"""
		try :
			obj = nssimpleacl()
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
		ur""" Use this API to count filtered the set of nssimpleacl resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nssimpleacl()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Protocol:
		TCP = "TCP"
		UDP = "UDP"

	class Aclaction:
		DENY = "DENY"

class nssimpleacl_response(base_response) :
	def __init__(self, length=1) :
		self.nssimpleacl = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nssimpleacl = [nssimpleacl() for _ in range(length)]

