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

class dnszone(base_resource) :
	""" Configuration for DNS zone resource. """
	def __init__(self) :
		self._zonename = ""
		self._proxymode = ""
		self._dnssecoffload = ""
		self._nsec = ""
		self._keyname = []
		self._type = ""
		self._flags = 0
		self.___count = 0

	@property
	def zonename(self) :
		ur"""Name of the zone to create.<br/>Minimum length =  1.
		"""
		try :
			return self._zonename
		except Exception as e:
			raise e

	@zonename.setter
	def zonename(self, zonename) :
		ur"""Name of the zone to create.<br/>Minimum length =  1
		"""
		try :
			self._zonename = zonename
		except Exception as e:
			raise e

	@property
	def proxymode(self) :
		ur"""Deploy the zone in proxy mode. Enable in the following scenarios:
		* The load balanced DNS servers are authoritative for the zone and all resource records that are part of the zone. 
		* The load balanced DNS servers are authoritative for the zone, but the NetScaler appliance owns a subset of the resource records that belong to the zone (partial zone ownership configuration). Typically seen in global server load balancing (GSLB) configurations, in which the appliance responds authoritatively to queries for GSLB domain names but forwards queries for other domain names in the zone to the load balanced servers.
		In either scenario, do not create the zone's Start of Authority (SOA) and name server (NS) resource records on the appliance. 
		Disable if the appliance is authoritative for the zone, but make sure that you have created the SOA and NS records on the appliance before you create the zone.<br/>Default value: ENABLED<br/>Possible values = YES, NO.
		"""
		try :
			return self._proxymode
		except Exception as e:
			raise e

	@proxymode.setter
	def proxymode(self, proxymode) :
		ur"""Deploy the zone in proxy mode. Enable in the following scenarios:
		* The load balanced DNS servers are authoritative for the zone and all resource records that are part of the zone. 
		* The load balanced DNS servers are authoritative for the zone, but the NetScaler appliance owns a subset of the resource records that belong to the zone (partial zone ownership configuration). Typically seen in global server load balancing (GSLB) configurations, in which the appliance responds authoritatively to queries for GSLB domain names but forwards queries for other domain names in the zone to the load balanced servers.
		In either scenario, do not create the zone's Start of Authority (SOA) and name server (NS) resource records on the appliance. 
		Disable if the appliance is authoritative for the zone, but make sure that you have created the SOA and NS records on the appliance before you create the zone.<br/>Default value: ENABLED<br/>Possible values = YES, NO
		"""
		try :
			self._proxymode = proxymode
		except Exception as e:
			raise e

	@property
	def dnssecoffload(self) :
		ur"""Enable dnssec offload for this zone.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnssecoffload
		except Exception as e:
			raise e

	@dnssecoffload.setter
	def dnssecoffload(self, dnssecoffload) :
		ur"""Enable dnssec offload for this zone.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnssecoffload = dnssecoffload
		except Exception as e:
			raise e

	@property
	def nsec(self) :
		ur"""Enable nsec generation for dnssec offload.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nsec
		except Exception as e:
			raise e

	@nsec.setter
	def nsec(self, nsec) :
		ur"""Enable nsec generation for dnssec offload.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nsec = nsec
		except Exception as e:
			raise e

	@property
	def keyname(self) :
		ur"""Name of the public/private DNS key pair with which to sign the zone. You can sign a zone with up to four keys.<br/>Minimum length =  1.
		"""
		try :
			return self._keyname
		except Exception as e:
			raise e

	@keyname.setter
	def keyname(self, keyname) :
		ur"""Name of the public/private DNS key pair with which to sign the zone. You can sign a zone with up to four keys.<br/>Minimum length =  1
		"""
		try :
			self._keyname = keyname
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of zone to display. Mutually exclusive with the DNS Zone (zoneName) parameter. Available settings function as follows:
		* ADNS - Display all the zones for which the NetScaler appliance is authoritative.
		* PROXY - Display all the zones for which the NetScaler appliance is functioning as a proxy server.
		* ALL - Display all the zones configured on the appliance.<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of zone to display. Mutually exclusive with the DNS Zone (zoneName) parameter. Available settings function as follows:
		* ADNS - Display all the zones for which the NetScaler appliance is authoritative.
		* PROXY - Display all the zones for which the NetScaler appliance is functioning as a proxy server.
		* ALL - Display all the zones configured on the appliance.<br/>Possible values = ALL, ADNS, PROXY
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""Flags controlling display.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnszone_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnszone
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
	def add(cls, client, resource) :
		ur""" Use this API to add dnszone.
		"""
		try :
			if type(resource) is not list :
				addresource = dnszone()
				addresource.zonename = resource.zonename
				addresource.proxymode = resource.proxymode
				addresource.dnssecoffload = resource.dnssecoffload
				addresource.nsec = resource.nsec
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnszone() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].zonename = resource[i].zonename
						addresources[i].proxymode = resource[i].proxymode
						addresources[i].dnssecoffload = resource[i].dnssecoffload
						addresources[i].nsec = resource[i].nsec
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update dnszone.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnszone()
				updateresource.zonename = resource.zonename
				updateresource.proxymode = resource.proxymode
				updateresource.dnssecoffload = resource.dnssecoffload
				updateresource.nsec = resource.nsec
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnszone() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].zonename = resource[i].zonename
						updateresources[i].proxymode = resource[i].proxymode
						updateresources[i].dnssecoffload = resource[i].dnssecoffload
						updateresources[i].nsec = resource[i].nsec
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of dnszone resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnszone()
				if type(resource) !=  type(unsetresource):
					unsetresource.zonename = resource
				else :
					unsetresource.zonename = resource.zonename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnszone() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].zonename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnszone() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].zonename = resource[i].zonename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dnszone.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnszone()
				if type(resource) !=  type(deleteresource):
					deleteresource.zonename = resource
				else :
					deleteresource.zonename = resource.zonename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnszone() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].zonename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnszone() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].zonename = resource[i].zonename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def sign(cls, client, resource) :
		ur""" Use this API to sign dnszone.
		"""
		try :
			if type(resource) is not list :
				signresource = dnszone()
				signresource.zonename = resource.zonename
				signresource.keyname = resource.keyname
				return signresource.perform_operation(client,"sign")
			else :
				if (resource and len(resource) > 0) :
					signresources = [ dnszone() for _ in range(len(resource))]
					for i in range(len(resource)) :
						signresources[i].zonename = resource[i].zonename
						signresources[i].keyname = resource[i].keyname
				result = cls.perform_operation_bulk_request(client, signresources,"sign")
			return result
		except Exception as e :
			raise e

	@classmethod
	def unsign(cls, client, resource) :
		ur""" Use this API to unsign dnszone.
		"""
		try :
			if type(resource) is not list :
				unsignresource = dnszone()
				unsignresource.zonename = resource.zonename
				unsignresource.keyname = resource.keyname
				return unsignresource.perform_operation(client,"unsign")
			else :
				if (resource and len(resource) > 0) :
					unsignresources = [ dnszone() for _ in range(len(resource))]
					for i in range(len(resource)) :
						unsignresources[i].zonename = resource[i].zonename
						unsignresources[i].keyname = resource[i].keyname
				result = cls.perform_operation_bulk_request(client, unsignresources,"unsign")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnszone resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnszone()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = dnszone()
						obj.zonename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnszone() for _ in range(len(name))]
							obj = [dnszone() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = dnszone()
								obj[i].zonename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the dnszone resources that are configured on netscaler.
	# This uses dnszone_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnszone()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnszone resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnszone()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnszone resources configured on NetScaler.
		"""
		try :
			obj = dnszone()
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
		ur""" Use this API to count filtered the set of dnszone resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnszone()
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

	class Proxymode:
		YES = "YES"
		NO = "NO"

	class Nsec:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dnssecoffload:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class dnszone_response(base_response) :
	def __init__(self, length=1) :
		self.dnszone = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnszone = [dnszone() for _ in range(length)]

