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

class ntpparam(base_resource) :
	""" Configuration for NTP parameter resource. """
	def __init__(self) :
		self._authentication = ""
		self._trustedkey = []
		self._autokeylogsec = 0
		self._revokelogsec = 0

	@property
	def authentication(self) :
		ur"""Apply NTP authentication, which enables the NTP client (NetScaler) to verify that the server is in fact known and trusted.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		ur"""Apply NTP authentication, which enables the NTP client (NetScaler) to verify that the server is in fact known and trusted.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	@property
	def trustedkey(self) :
		ur"""Key identifiers that are trusted for server authentication with symmetric key cryptography in the keys file.<br/>Minimum length =  1<br/>Maximum length =  65534.
		"""
		try :
			return self._trustedkey
		except Exception as e:
			raise e

	@trustedkey.setter
	def trustedkey(self, trustedkey) :
		ur"""Key identifiers that are trusted for server authentication with symmetric key cryptography in the keys file.<br/>Minimum length =  1<br/>Maximum length =  65534
		"""
		try :
			self._trustedkey = trustedkey
		except Exception as e:
			raise e

	@property
	def autokeylogsec(self) :
		ur"""Autokey protocol requires the keys to be refreshed periodically. This parameter specifies the interval between regenerations of new session keys. In seconds, expressed as a power of 2.<br/>Default value: 12<br/>Maximum length =  32.
		"""
		try :
			return self._autokeylogsec
		except Exception as e:
			raise e

	@autokeylogsec.setter
	def autokeylogsec(self, autokeylogsec) :
		ur"""Autokey protocol requires the keys to be refreshed periodically. This parameter specifies the interval between regenerations of new session keys. In seconds, expressed as a power of 2.<br/>Default value: 12<br/>Maximum length =  32
		"""
		try :
			self._autokeylogsec = autokeylogsec
		except Exception as e:
			raise e

	@property
	def revokelogsec(self) :
		ur"""Interval between re-randomizations of the autokey seeds to prevent brute-force attacks on the autokey algorithms.<br/>Default value: 16<br/>Maximum length =  32.
		"""
		try :
			return self._revokelogsec
		except Exception as e:
			raise e

	@revokelogsec.setter
	def revokelogsec(self, revokelogsec) :
		ur"""Interval between re-randomizations of the autokey seeds to prevent brute-force attacks on the autokey algorithms.<br/>Default value: 16<br/>Maximum length =  32
		"""
		try :
			self._revokelogsec = revokelogsec
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ntpparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ntpparam
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
		ur""" Use this API to update ntpparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = ntpparam()
				updateresource.authentication = resource.authentication
				updateresource.trustedkey = resource.trustedkey
				updateresource.autokeylogsec = resource.autokeylogsec
				updateresource.revokelogsec = resource.revokelogsec
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of ntpparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ntpparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the ntpparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ntpparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Authentication:
		YES = "YES"
		NO = "NO"

class ntpparam_response(base_response) :
	def __init__(self, length=1) :
		self.ntpparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ntpparam = [ntpparam() for _ in range(length)]

