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

class dnszone_dnskey_binding(base_resource) :
	""" Binding class showing the dnskey that can be bound to dnszone.
	"""
	def __init__(self) :
		self._keyname = []
		self._siginceptiontime = []
		self._signed = 0
		self._expires = 0
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
	def siginceptiontime(self) :
		ur"""The time when sign was done with this key.<br/>Minimum value =  1.
		"""
		try :
			return self._siginceptiontime
		except Exception as e:
			raise e

	@property
	def signed(self) :
		ur"""Integer which denote status of keys.
		"""
		try :
			return self._signed
		except Exception as e:
			raise e

	@property
	def expires(self) :
		ur"""Time period for which to consider the key valid, after the key is used to sign a zone.
		"""
		try :
			return self._expires
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnszone_dnskey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnszone_dnskey_binding
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
		ur""" Use this API to fetch dnszone_dnskey_binding resources.
		"""
		try :
			obj = dnszone_dnskey_binding()
			obj.zonename = zonename
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, zonename, filter_) :
		ur""" Use this API to fetch filtered set of dnszone_dnskey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnszone_dnskey_binding()
			obj.zonename = zonename
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, zonename) :
		ur""" Use this API to count dnszone_dnskey_binding resources configued on NetScaler.
		"""
		try :
			obj = dnszone_dnskey_binding()
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
		ur""" Use this API to count the filtered set of dnszone_dnskey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnszone_dnskey_binding()
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

class dnszone_dnskey_binding_response(base_response) :
	def __init__(self, length=1) :
		self.dnszone_dnskey_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnszone_dnskey_binding = [dnszone_dnskey_binding() for _ in range(length)]

