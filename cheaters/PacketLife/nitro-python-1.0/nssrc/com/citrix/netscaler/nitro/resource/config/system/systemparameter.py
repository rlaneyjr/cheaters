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

class systemparameter(base_resource) :
	""" Configuration for system parameter resource. """
	def __init__(self) :
		self._rbaonresponse = ""
		self._promptstring = ""
		self._natpcbforceflushlimit = 0
		self._natpcbrstontimeout = ""
		self._timeout = 0
		self._localauth = ""
		self._restrictedtimeout = ""
		self._maxclient = 0

	@property
	def rbaonresponse(self) :
		ur"""Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rbaonresponse
		except Exception as e:
			raise e

	@rbaonresponse.setter
	def rbaonresponse(self, rbaonresponse) :
		ur"""Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rbaonresponse = rbaonresponse
		except Exception as e:
			raise e

	@property
	def promptstring(self) :
		ur"""String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables: 
		* %u - Will be replaced by the user name.
		* %h - Will be replaced by the hostname of the NetScaler appliance.
		* %t - Will be replaced by the current time in 12-hour format.
		* %T - Will be replaced by the current time in 24-hour format.
		* %d - Will be replaced by the current date.
		* %s - Will be replaced by the state of the NetScaler appliance.
		Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1.
		"""
		try :
			return self._promptstring
		except Exception as e:
			raise e

	@promptstring.setter
	def promptstring(self, promptstring) :
		ur"""String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables: 
		* %u - Will be replaced by the user name.
		* %h - Will be replaced by the hostname of the NetScaler appliance.
		* %t - Will be replaced by the current time in 12-hour format.
		* %T - Will be replaced by the current time in 24-hour format.
		* %d - Will be replaced by the current date.
		* %s - Will be replaced by the state of the NetScaler appliance.
		Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1
		"""
		try :
			self._promptstring = promptstring
		except Exception as e:
			raise e

	@property
	def natpcbforceflushlimit(self) :
		ur"""Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000.
		"""
		try :
			return self._natpcbforceflushlimit
		except Exception as e:
			raise e

	@natpcbforceflushlimit.setter
	def natpcbforceflushlimit(self, natpcbforceflushlimit) :
		ur"""Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000
		"""
		try :
			self._natpcbforceflushlimit = natpcbforceflushlimit
		except Exception as e:
			raise e

	@property
	def natpcbrstontimeout(self) :
		ur"""Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._natpcbrstontimeout
		except Exception as e:
			raise e

	@natpcbrstontimeout.setter
	def natpcbrstontimeout(self, natpcbrstontimeout) :
		ur"""Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._natpcbrstontimeout = natpcbrstontimeout
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		ur"""CLI session inactivity timeout, in seconds. If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds. If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		ur"""CLI session inactivity timeout, in seconds. If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds. If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def localauth(self) :
		ur"""When enabled, local users can access NetScaler even when external authentication is configured. When disabled, local users are not allowed to access the NetScaler, Local users can access the NetScaler only when the configured external authentication servers are unavailable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._localauth
		except Exception as e:
			raise e

	@localauth.setter
	def localauth(self, localauth) :
		ur"""When enabled, local users can access NetScaler even when external authentication is configured. When disabled, local users are not allowed to access the NetScaler, Local users can access the NetScaler only when the configured external authentication servers are unavailable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._localauth = localauth
		except Exception as e:
			raise e

	@property
	def restrictedtimeout(self) :
		ur"""Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout and also it will have\
		the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._restrictedtimeout
		except Exception as e:
			raise e

	@restrictedtimeout.setter
	def restrictedtimeout(self, restrictedtimeout) :
		ur"""Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout and also it will have\
		the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._restrictedtimeout = restrictedtimeout
		except Exception as e:
			raise e

	@property
	def maxclient(self) :
		ur"""Maximum number of client connection allowed by the system.<br/>Minimum value =  20<br/>Maximum value =  40.
		"""
		try :
			return self._maxclient
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemparameter
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
		ur""" Use this API to update systemparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = systemparameter()
				updateresource.rbaonresponse = resource.rbaonresponse
				updateresource.promptstring = resource.promptstring
				updateresource.natpcbforceflushlimit = resource.natpcbforceflushlimit
				updateresource.natpcbrstontimeout = resource.natpcbrstontimeout
				updateresource.timeout = resource.timeout
				updateresource.localauth = resource.localauth
				updateresource.restrictedtimeout = resource.restrictedtimeout
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of systemparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = systemparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systemparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Localauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Restrictedtimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rbaonresponse:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Natpcbrstontimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class systemparameter_response(base_response) :
	def __init__(self, length=1) :
		self.systemparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemparameter = [systemparameter() for _ in range(length)]

