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

class dnskey(base_resource) :
	def __init__(self) :
		self._keyname = ""
		self._publickey = ""
		self._privatekey = ""
		self._expires = 0
		self._units1 = ""
		self._notificationperiod = 0
		self._units2 = ""
		self._ttl = 0
		self._zonename = ""
		self._keytype = ""
		self._algorithm = ""
		self._keysize = 0
		self._filenameprefix = ""
		self.___count = 0

	@property
	def keyname(self) :
		ur"""Name of the public-private key pair to publish in the zone.<br/>Minimum length =  1.
		"""
		try :
			return self._keyname
		except Exception as e:
			raise e

	@keyname.setter
	def keyname(self, keyname) :
		ur"""Name of the public-private key pair to publish in the zone.<br/>Minimum length =  1
		"""
		try :
			self._keyname = keyname
		except Exception as e:
			raise e

	@property
	def publickey(self) :
		ur"""File name of the public key.
		"""
		try :
			return self._publickey
		except Exception as e:
			raise e

	@publickey.setter
	def publickey(self, publickey) :
		ur"""File name of the public key.
		"""
		try :
			self._publickey = publickey
		except Exception as e:
			raise e

	@property
	def privatekey(self) :
		ur"""File name of the private key.
		"""
		try :
			return self._privatekey
		except Exception as e:
			raise e

	@privatekey.setter
	def privatekey(self, privatekey) :
		ur"""File name of the private key.
		"""
		try :
			self._privatekey = privatekey
		except Exception as e:
			raise e

	@property
	def expires(self) :
		ur"""Time period for which to consider the key valid, after the key is used to sign a zone.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  32767.
		"""
		try :
			return self._expires
		except Exception as e:
			raise e

	@expires.setter
	def expires(self, expires) :
		ur"""Time period for which to consider the key valid, after the key is used to sign a zone.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  32767
		"""
		try :
			self._expires = expires
		except Exception as e:
			raise e

	@property
	def units1(self) :
		ur"""Units for the expiry period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS.
		"""
		try :
			return self._units1
		except Exception as e:
			raise e

	@units1.setter
	def units1(self, units1) :
		ur"""Units for the expiry period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS
		"""
		try :
			self._units1 = units1
		except Exception as e:
			raise e

	@property
	def notificationperiod(self) :
		ur"""Time at which to generate notification of key expiration, specified as number of days, hours, or minutes before expiry. Must be less than the expiry period. The notification is an SNMP trap sent to an SNMP manager. To enable the appliance to send the trap, enable the DNSKEY-EXPIRY SNMP alarm.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  32767.
		"""
		try :
			return self._notificationperiod
		except Exception as e:
			raise e

	@notificationperiod.setter
	def notificationperiod(self, notificationperiod) :
		ur"""Time at which to generate notification of key expiration, specified as number of days, hours, or minutes before expiry. Must be less than the expiry period. The notification is an SNMP trap sent to an SNMP manager. To enable the appliance to send the trap, enable the DNSKEY-EXPIRY SNMP alarm.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  32767
		"""
		try :
			self._notificationperiod = notificationperiod
		except Exception as e:
			raise e

	@property
	def units2(self) :
		ur"""Units for the notification period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS.
		"""
		try :
			return self._units2
		except Exception as e:
			raise e

	@units2.setter
	def units2(self, units2) :
		ur"""Units for the notification period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS
		"""
		try :
			self._units2 = units2
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		ur"""Time to Live (TTL), in seconds, for the DNSKEY resource record created in the zone. TTL is the time for which the record must be cached by the DNS proxies. If the TTL is not specified, either the DNS zone's minimum TTL or the default value of 3600 is used.<br/>Default value: 3600<br/>Maximum length =  2147483647.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		ur"""Time to Live (TTL), in seconds, for the DNSKEY resource record created in the zone. TTL is the time for which the record must be cached by the DNS proxies. If the TTL is not specified, either the DNS zone's minimum TTL or the default value of 3600 is used.<br/>Default value: 3600<br/>Maximum length =  2147483647
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def zonename(self) :
		ur"""Name of the zone for which to create a key.<br/>Minimum length =  1.
		"""
		try :
			return self._zonename
		except Exception as e:
			raise e

	@zonename.setter
	def zonename(self, zonename) :
		ur"""Name of the zone for which to create a key.<br/>Minimum length =  1
		"""
		try :
			self._zonename = zonename
		except Exception as e:
			raise e

	@property
	def keytype(self) :
		ur"""Type of key to create.<br/>Default value: NS_DNSKEY_ZSK<br/>Possible values = KSK, KeySigningKey, ZSK, ZoneSigningKey.
		"""
		try :
			return self._keytype
		except Exception as e:
			raise e

	@keytype.setter
	def keytype(self, keytype) :
		ur"""Type of key to create.<br/>Default value: NS_DNSKEY_ZSK<br/>Possible values = KSK, KeySigningKey, ZSK, ZoneSigningKey
		"""
		try :
			self._keytype = keytype
		except Exception as e:
			raise e

	@property
	def algorithm(self) :
		ur"""Algorithm to generate for zone signing.<br/>Default value: NS_DNSKEYALGO_RSASHA1<br/>Possible values = RSASHA1.
		"""
		try :
			return self._algorithm
		except Exception as e:
			raise e

	@algorithm.setter
	def algorithm(self, algorithm) :
		ur"""Algorithm to generate for zone signing.<br/>Default value: NS_DNSKEYALGO_RSASHA1<br/>Possible values = RSASHA1
		"""
		try :
			self._algorithm = algorithm
		except Exception as e:
			raise e

	@property
	def keysize(self) :
		ur"""Size of the key, in bits.<br/>Default value: 512.
		"""
		try :
			return self._keysize
		except Exception as e:
			raise e

	@keysize.setter
	def keysize(self, keysize) :
		ur"""Size of the key, in bits.<br/>Default value: 512
		"""
		try :
			self._keysize = keysize
		except Exception as e:
			raise e

	@property
	def filenameprefix(self) :
		ur"""Common prefix for the names of the generated public and private key files and the Delegation Signer (DS) resource record. During key generation, the .key, .private, and .ds suffixes are appended automatically to the file name prefix to produce the names of the public key, the private key, and the DS record, respectively.
		"""
		try :
			return self._filenameprefix
		except Exception as e:
			raise e

	@filenameprefix.setter
	def filenameprefix(self, filenameprefix) :
		ur"""Common prefix for the names of the generated public and private key files and the Delegation Signer (DS) resource record. During key generation, the .key, .private, and .ds suffixes are appended automatically to the file name prefix to produce the names of the public key, the private key, and the DS record, respectively.
		"""
		try :
			self._filenameprefix = filenameprefix
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnskey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnskey
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.keyname is not None :
				return str(self.keyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add dnskey.
		"""
		try :
			if type(resource) is not list :
				addresource = dnskey()
				addresource.keyname = resource.keyname
				addresource.publickey = resource.publickey
				addresource.privatekey = resource.privatekey
				addresource.expires = resource.expires
				addresource.units1 = resource.units1
				addresource.notificationperiod = resource.notificationperiod
				addresource.units2 = resource.units2
				addresource.ttl = resource.ttl
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].keyname = resource[i].keyname
						addresources[i].publickey = resource[i].publickey
						addresources[i].privatekey = resource[i].privatekey
						addresources[i].expires = resource[i].expires
						addresources[i].units1 = resource[i].units1
						addresources[i].notificationperiod = resource[i].notificationperiod
						addresources[i].units2 = resource[i].units2
						addresources[i].ttl = resource[i].ttl
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def create(cls, client, resource) :
		ur""" Use this API to create dnskey.
		"""
		try :
			if type(resource) is not list :
				createresource = dnskey()
				createresource.zonename = resource.zonename
				createresource.keytype = resource.keytype
				createresource.algorithm = resource.algorithm
				createresource.keysize = resource.keysize
				createresource.filenameprefix = resource.filenameprefix
				return createresource.perform_operation(client,"create")
			else :
				if (resource and len(resource) > 0) :
					createresources = [ dnskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						createresources[i].zonename = resource[i].zonename
						createresources[i].keytype = resource[i].keytype
						createresources[i].algorithm = resource[i].algorithm
						createresources[i].keysize = resource[i].keysize
						createresources[i].filenameprefix = resource[i].filenameprefix
				result = cls.perform_operation_bulk_request(client, createresources,"create")
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update dnskey.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnskey()
				updateresource.keyname = resource.keyname
				updateresource.expires = resource.expires
				updateresource.units1 = resource.units1
				updateresource.notificationperiod = resource.notificationperiod
				updateresource.units2 = resource.units2
				updateresource.ttl = resource.ttl
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].keyname = resource[i].keyname
						updateresources[i].expires = resource[i].expires
						updateresources[i].units1 = resource[i].units1
						updateresources[i].notificationperiod = resource[i].notificationperiod
						updateresources[i].units2 = resource[i].units2
						updateresources[i].ttl = resource[i].ttl
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of dnskey resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnskey()
				if type(resource) !=  type(unsetresource):
					unsetresource.keyname = resource
				else :
					unsetresource.keyname = resource.keyname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].keyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].keyname = resource[i].keyname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dnskey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnskey()
				if type(resource) !=  type(deleteresource):
					deleteresource.keyname = resource
				else :
					deleteresource.keyname = resource.keyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].keyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].keyname = resource[i].keyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dnskey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnskey()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = dnskey()
						obj.keyname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dnskey() for _ in range(len(name))]
							obj = [dnskey() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = dnskey()
								obj[i].keyname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dnskey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnskey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dnskey resources configured on NetScaler.
		"""
		try :
			obj = dnskey()
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
		ur""" Use this API to count filtered the set of dnskey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnskey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Algorithm:
		RSASHA1 = "RSASHA1"

	class Keytype:
		KSK = "KSK"
		KeySigningKey = "KeySigningKey"
		ZSK = "ZSK"
		ZoneSigningKey = "ZoneSigningKey"

	class Units1:
		MINUTES = "MINUTES"
		HOURS = "HOURS"
		DAYS = "DAYS"

	class Units2:
		MINUTES = "MINUTES"
		HOURS = "HOURS"
		DAYS = "DAYS"

class dnskey_response(base_response) :
	def __init__(self, length=1) :
		self.dnskey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnskey = [dnskey() for _ in range(length)]

