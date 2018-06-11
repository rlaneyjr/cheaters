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

class arpparam(base_resource) :
	""" Configuration for Global arp parameters resource. """
	def __init__(self) :
		self._timeout = 0
		self._spoofvalidation = ""

	@property
	def timeout(self) :
		ur"""Time-out value (aging time) for the dynamically learned ARP entries, in seconds. The new value applies only to ARP entries that are dynamically learned after the new value is set. Previously existing ARP entries expire after the previously configured aging time.<br/>Default value: 1200<br/>Minimum length =  5<br/>Maximum length =  1200.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		ur"""Time-out value (aging time) for the dynamically learned ARP entries, in seconds. The new value applies only to ARP entries that are dynamically learned after the new value is set. Previously existing ARP entries expire after the previously configured aging time.<br/>Default value: 1200<br/>Minimum length =  5<br/>Maximum length =  1200
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def spoofvalidation(self) :
		ur"""enable/disable arp spoofing validation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._spoofvalidation
		except Exception as e:
			raise e

	@spoofvalidation.setter
	def spoofvalidation(self, spoofvalidation) :
		ur"""enable/disable arp spoofing validation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._spoofvalidation = spoofvalidation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(arpparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.arpparam
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
		ur""" Use this API to update arpparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = arpparam()
				updateresource.timeout = resource.timeout
				updateresource.spoofvalidation = resource.spoofvalidation
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of arpparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = arpparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the arpparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = arpparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Spoofvalidation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class arpparam_response(base_response) :
	def __init__(self, length=1) :
		self.arpparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.arpparam = [arpparam() for _ in range(length)]

