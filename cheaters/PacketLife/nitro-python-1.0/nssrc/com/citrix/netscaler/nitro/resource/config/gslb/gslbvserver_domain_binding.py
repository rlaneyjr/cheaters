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

class gslbvserver_domain_binding(base_resource) :
	""" Binding class showing the domain that can be bound to gslbvserver.
	"""
	def __init__(self) :
		self._domainname = ""
		self._ttl = 0
		self._backupip = ""
		self._cookie_domain = ""
		self._cookietimeout = 0
		self._sitedomainttl = 0
		self._name = ""
		self._backupipflag = False
		self._cookie_domainflag = False
		self.___count = 0

	@property
	def backupipflag(self) :
		ur"""The IP address of the backup service for the specified domain name. Used when all the services bound to the domain are down, or when the backup chain of virtual servers is down.
		"""
		try :
			return self._backupipflag
		except Exception as e:
			raise e

	@backupipflag.setter
	def backupipflag(self, backupipflag) :
		ur"""The IP address of the backup service for the specified domain name. Used when all the services bound to the domain are down, or when the backup chain of virtual servers is down.
		"""
		try :
			self._backupipflag = backupipflag
		except Exception as e:
			raise e

	@property
	def cookietimeout(self) :
		ur"""Timeout, in minutes, for the GSLB site cookie.<br/>Minimum value =  0<br/>Maximum value =  1440.
		"""
		try :
			return self._cookietimeout
		except Exception as e:
			raise e

	@cookietimeout.setter
	def cookietimeout(self, cookietimeout) :
		ur"""Timeout, in minutes, for the GSLB site cookie.<br/>Minimum value =  0<br/>Maximum value =  1440
		"""
		try :
			self._cookietimeout = cookietimeout
		except Exception as e:
			raise e

	@property
	def backupip(self) :
		ur"""The IP address of the backup service for the specified domain name. Used when all the services bound to the domain are down, or when the backup chain of virtual servers is down.<br/>Minimum length =  1.
		"""
		try :
			return self._backupip
		except Exception as e:
			raise e

	@backupip.setter
	def backupip(self, backupip) :
		ur"""The IP address of the backup service for the specified domain name. Used when all the services bound to the domain are down, or when the backup chain of virtual servers is down.<br/>Minimum length =  1
		"""
		try :
			self._backupip = backupip
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name of the virtual server on which to perform the binding operation.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the virtual server on which to perform the binding operation.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		ur"""Time to live (TTL) for the domain.<br/>Minimum value =  1.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		ur"""Time to live (TTL) for the domain.<br/>Minimum value =  1
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def domainname(self) :
		ur"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._domainname
		except Exception as e:
			raise e

	@domainname.setter
	def domainname(self, domainname) :
		ur"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1
		"""
		try :
			self._domainname = domainname
		except Exception as e:
			raise e

	@property
	def sitedomainttl(self) :
		ur"""TTL, in seconds, for all internally created site domains (created when a site prefix is configured on a GSLB service) that are associated with this virtual server.<br/>Minimum value =  1.
		"""
		try :
			return self._sitedomainttl
		except Exception as e:
			raise e

	@sitedomainttl.setter
	def sitedomainttl(self, sitedomainttl) :
		ur"""TTL, in seconds, for all internally created site domains (created when a site prefix is configured on a GSLB service) that are associated with this virtual server.<br/>Minimum value =  1
		"""
		try :
			self._sitedomainttl = sitedomainttl
		except Exception as e:
			raise e

	@property
	def cookie_domainflag(self) :
		ur"""The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response.
		"""
		try :
			return self._cookie_domainflag
		except Exception as e:
			raise e

	@cookie_domainflag.setter
	def cookie_domainflag(self, cookie_domainflag) :
		ur"""The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response.
		"""
		try :
			self._cookie_domainflag = cookie_domainflag
		except Exception as e:
			raise e

	@property
	def cookie_domain(self) :
		ur"""The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response.<br/>Minimum length =  1.
		"""
		try :
			return self._cookie_domain
		except Exception as e:
			raise e

	@cookie_domain.setter
	def cookie_domain(self, cookie_domain) :
		ur"""The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response.<br/>Minimum length =  1
		"""
		try :
			self._cookie_domain = cookie_domain
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbvserver_domain_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbvserver_domain_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = gslbvserver_domain_binding()
				updateresource.name = resource.name
				updateresource.domainname = resource.domainname
				updateresource.ttl = resource.ttl
				updateresource.backupip = resource.backupip
				updateresource.cookie_domain = resource.cookie_domain
				updateresource.cookietimeout = resource.cookietimeout
				updateresource.sitedomainttl = resource.sitedomainttl
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [gslbvserver_domain_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].domainname = resource[i].domainname
						updateresources[i].ttl = resource[i].ttl
						updateresources[i].backupip = resource[i].backupip
						updateresources[i].cookie_domain = resource[i].cookie_domain
						updateresources[i].cookietimeout = resource[i].cookietimeout
						updateresources[i].sitedomainttl = resource[i].sitedomainttl
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = gslbvserver_domain_binding()
				deleteresource.name = resource.name
				deleteresource.domainname = resource.domainname
				deleteresource.backupipflag = resource.backupipflag
				deleteresource.cookie_domainflag = resource.cookie_domainflag
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [gslbvserver_domain_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].domainname = resource[i].domainname
						deleteresources[i].backupipflag = resource[i].backupipflag
						deleteresources[i].cookie_domainflag = resource[i].cookie_domainflag
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch gslbvserver_domain_binding resources.
		"""
		try :
			obj = gslbvserver_domain_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of gslbvserver_domain_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbvserver_domain_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count gslbvserver_domain_binding resources configued on NetScaler.
		"""
		try :
			obj = gslbvserver_domain_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of gslbvserver_domain_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbvserver_domain_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Type:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"

class gslbvserver_domain_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbvserver_domain_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbvserver_domain_binding = [gslbvserver_domain_binding() for _ in range(length)]

