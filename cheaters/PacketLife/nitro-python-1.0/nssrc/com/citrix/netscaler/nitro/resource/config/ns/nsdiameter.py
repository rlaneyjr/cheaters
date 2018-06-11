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

class nsdiameter(base_resource) :
	""" Configuration for Diameter Parameters resource. """
	def __init__(self) :
		self._identity = ""
		self._realm = ""
		self._serverclosepropagation = ""

	@property
	def identity(self) :
		ur"""DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Netscaler (as a Diameter node) MUST be assigned a unique DiameterIdentity.
		example =>
		set ns diameter -identity netscaler.com
		Now whenever Netscaler system needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._identity
		except Exception as e:
			raise e

	@identity.setter
	def identity(self, identity) :
		ur"""DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Netscaler (as a Diameter node) MUST be assigned a unique DiameterIdentity.
		example =>
		set ns diameter -identity netscaler.com
		Now whenever Netscaler system needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
		.<br/>Minimum length =  1
		"""
		try :
			self._identity = identity
		except Exception as e:
			raise e

	@property
	def realm(self) :
		ur"""Diameter Realm to be used by NS.
		example =>
		set ns diameter -realm com
		Now whenever Netscaler system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._realm
		except Exception as e:
			raise e

	@realm.setter
	def realm(self, realm) :
		ur"""Diameter Realm to be used by NS.
		example =>
		set ns diameter -realm com
		Now whenever Netscaler system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
		.<br/>Minimum length =  1
		"""
		try :
			self._realm = realm
		except Exception as e:
			raise e

	@property
	def serverclosepropagation(self) :
		ur"""when a Server connection goes down, whether to close the corresponding client connection if there were requests pending on the server.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._serverclosepropagation
		except Exception as e:
			raise e

	@serverclosepropagation.setter
	def serverclosepropagation(self, serverclosepropagation) :
		ur"""when a Server connection goes down, whether to close the corresponding client connection if there were requests pending on the server.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._serverclosepropagation = serverclosepropagation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsdiameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsdiameter
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nsdiameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsdiameter()
				updateresource.identity = resource.identity
				updateresource.realm = resource.realm
				updateresource.serverclosepropagation = resource.serverclosepropagation
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nsdiameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsdiameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsdiameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsdiameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Serverclosepropagation:
		YES = "YES"
		NO = "NO"

class nsdiameter_response(base_response) :
	def __init__(self, length=1) :
		self.nsdiameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsdiameter = [nsdiameter() for _ in range(length)]

