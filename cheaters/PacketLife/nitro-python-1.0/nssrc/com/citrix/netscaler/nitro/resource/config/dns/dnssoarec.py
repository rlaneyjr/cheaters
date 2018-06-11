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

class dnssoarec(base_resource) :
	""" Configuration for SOA record resource. """
	def __init__(self) :
		self._domain = ""
		self._originserver = ""
		self._contact = ""
		self._serial = 0
		self._refresh = 0
		self._retry = 0
		self._expire = 0
		self._minimum = 0
		self._ttl = 0
		self._type = ""
		self._authtype = ""
		self.___count = 0

	@property
	def domain(self) :
		ur"""Domain name for which to add the SOA record.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""Domain name for which to add the SOA record.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def originserver(self) :
		ur"""Domain name of the name server that responds authoritatively for the domain.<br/>Minimum length =  1.
		"""
		try :
			return self._originserver
		except Exception as e:
			raise e

	@originserver.setter
	def originserver(self, originserver) :
		ur"""Domain name of the name server that responds authoritatively for the domain.<br/>Minimum length =  1
		"""
		try :
			self._originserver = originserver
		except Exception as e:
			raise e

	@property
	def contact(self) :
		ur"""Email address of the contact to whom domain issues can be addressed. In the email address, replace the @ sign with a period (.). For example, enter domainadmin.example.com instead of domainadmin@example.com.<br/>Minimum length =  1.
		"""
		try :
			return self._contact
		except Exception as e:
			raise e

	@contact.setter
	def contact(self, contact) :
		ur"""Email address of the contact to whom domain issues can be addressed. In the email address, replace the @ sign with a period (.). For example, enter domainadmin.example.com instead of domainadmin@example.com.<br/>Minimum length =  1
		"""
		try :
			self._contact = contact
		except Exception as e:
			raise e

	@property
	def serial(self) :
		ur"""The secondary server uses this parameter to determine whether it requires a zone transfer from the primary server.<br/>Default value: 100<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._serial
		except Exception as e:
			raise e

	@serial.setter
	def serial(self, serial) :
		ur"""The secondary server uses this parameter to determine whether it requires a zone transfer from the primary server.<br/>Default value: 100<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._serial = serial
		except Exception as e:
			raise e

	@property
	def refresh(self) :
		ur"""Time, in seconds, for which a secondary server must wait between successive checks on the value of the serial number.<br/>Default value: 3600<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._refresh
		except Exception as e:
			raise e

	@refresh.setter
	def refresh(self, refresh) :
		ur"""Time, in seconds, for which a secondary server must wait between successive checks on the value of the serial number.<br/>Default value: 3600<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._refresh = refresh
		except Exception as e:
			raise e

	@property
	def retry(self) :
		ur"""Time, in seconds, between retries if a secondary server's attempt to contact the primary server for a zone refresh fails.<br/>Default value: 3<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._retry
		except Exception as e:
			raise e

	@retry.setter
	def retry(self, retry) :
		ur"""Time, in seconds, between retries if a secondary server's attempt to contact the primary server for a zone refresh fails.<br/>Default value: 3<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._retry = retry
		except Exception as e:
			raise e

	@property
	def expire(self) :
		ur"""Time, in seconds, after which the zone data on a secondary name server can no longer be considered authoritative because all refresh and retry attempts made during the period have failed. After the expiry period, the secondary server stops serving the zone. Typically one week. Not used by the primary server.<br/>Default value: 3600<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._expire
		except Exception as e:
			raise e

	@expire.setter
	def expire(self, expire) :
		ur"""Time, in seconds, after which the zone data on a secondary name server can no longer be considered authoritative because all refresh and retry attempts made during the period have failed. After the expiry period, the secondary server stops serving the zone. Typically one week. Not used by the primary server.<br/>Default value: 3600<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._expire = expire
		except Exception as e:
			raise e

	@property
	def minimum(self) :
		ur"""Default time to live (TTL) for all records in the zone. Can be overridden for individual records.<br/>Default value: 5<br/>Maximum length =  2147483647.
		"""
		try :
			return self._minimum
		except Exception as e:
			raise e

	@minimum.setter
	def minimum(self, minimum) :
		ur"""Default time to live (TTL) for all records in the zone. Can be overridden for individual records.<br/>Default value: 5<br/>Maximum length =  2147483647
		"""
		try :
			self._minimum = minimum
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
			result = service.payload_formatter.string_to_resource(dnssoarec_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnssoarec
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
		ur""" Use this API to add dnssoarec.
		"""
		try :
			if type(resource) is not list :
				addresource = dnssoarec()
				addresource.domain = resource.domain
				addresource.originserver = resource.originserver
				addresource.contact = resource.contact
				addresource.serial = resource.serial
				addresource.refresh = resource.refresh
				addresource.retry = resource.retry
				addresource.expire = resource.expire
				addresource.minimum = resource.minimum
				addresource.ttl = resource.ttl
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnssoarec() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].domain = resource[i].domain
						addresources[i].originserver = resource[i].originserver
						addresources[i].contact = resource[i].contact
						addresources[i].serial = resource[i].serial
						addresources[i].refresh = resource[i].refresh
						addresources[i].retry = resource[i].retry
						addresources[i].expire = resource[i].expire
						addresources[i].minimum = resource[i].minimum
						addresources[i].ttl = resource[i].ttl
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dnssoarec.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnssoarec()
				if type(resource) !=  type(deleteresource):
					deleteresource.domain = resource
				else :
					deleteresource.domain = resource.domain
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnssoarec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].domain = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnssoarec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].domain = resource[i].domain
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update dnssoarec.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnssoarec()
				updateresource.domain = resource.domain
				updateresource.originserver = resource.originserver
				updateresource.contact = resource.contact
				updateresource.serial = resource.serial
				updateresource.refresh = resource.refresh
				updateresource.retry = resource.retry
				updateresource.expire = resource.expire
				updateresource.minimum = resource.minimum
				updateresource.ttl = resource.ttl
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnssoarec() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].domain = resource[i].domain
						updateresources[i].originserver = resource[i].originserver
						updateresources[i].contact = resource[i].contact
						updateresources[i].serial = resource[i].serial
						updateresources[i].refresh = resource[i].refresh
						updateresources[i].retry = resource[i].retry
						updateresources[i].expire = resource[i].expire
						updateresources[i].minimum = resource[i].minimum
						updateresources[i].ttl = resource[i].ttl
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of dnssoarec resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnssoarec()
				if type(resource) !=  type(unsetresource):
					unsetresource.domain = resource
				else :
					unsetresource.domain = resource.domain
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnssoarec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].domain = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnssoarec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].domain = resource[i].domain
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnssoarec resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnssoarec()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = dnssoarec()
						obj.domain = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnssoarec() for _ in range(len(name))]
							obj = [dnssoarec() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = dnssoarec()
								obj[i].domain = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the dnssoarec resources that are configured on netscaler.
	# This uses dnssoarec_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnssoarec()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnssoarec resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnssoarec()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnssoarec resources configured on NetScaler.
		"""
		try :
			obj = dnssoarec()
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
		ur""" Use this API to count filtered the set of dnssoarec resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnssoarec()
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

class dnssoarec_response(base_response) :
	def __init__(self, length=1) :
		self.dnssoarec = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnssoarec = [dnssoarec() for _ in range(length)]

