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

class rewriteparam(base_resource) :
	""" Configuration for rewrite parameter resource. """
	def __init__(self) :
		self._undefaction = ""

	@property
	def undefaction(self) :
		ur"""Action to perform if the result of policy evaluation is undefined (UNDEF). An UNDEF event indicates an internal error condition.
		Available settings function as follows:
		* NOOP - Send the request to the protected server instead of responding to it.
		* RESET - Reset the request and notify the user's browser, so that the user can resend the request.
		* DROP - Drop the request without sending a response to the user.<br/>Default value: "NOREWRITE".
		"""
		try :
			return self._undefaction
		except Exception as e:
			raise e

	@undefaction.setter
	def undefaction(self, undefaction) :
		ur"""Action to perform if the result of policy evaluation is undefined (UNDEF). An UNDEF event indicates an internal error condition.
		Available settings function as follows:
		* NOOP - Send the request to the protected server instead of responding to it.
		* RESET - Reset the request and notify the user's browser, so that the user can resend the request.
		* DROP - Drop the request without sending a response to the user.<br/>Default value: "NOREWRITE"
		"""
		try :
			self._undefaction = undefaction
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rewriteparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rewriteparam
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
		ur""" Use this API to update rewriteparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = rewriteparam()
				updateresource.undefaction = resource.undefaction
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of rewriteparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = rewriteparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the rewriteparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rewriteparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class rewriteparam_response(base_response) :
	def __init__(self, length=1) :
		self.rewriteparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rewriteparam = [rewriteparam() for _ in range(length)]

