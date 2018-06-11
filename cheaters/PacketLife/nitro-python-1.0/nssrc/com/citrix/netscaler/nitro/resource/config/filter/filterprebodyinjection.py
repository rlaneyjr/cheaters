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

class filterprebodyinjection(base_resource) :
	""" Configuration for HTML Injection prebody resource. """
	def __init__(self) :
		self._prebody = ""
		self._systemiid = ""

	@property
	def prebody(self) :
		ur"""Name of file whose contents are to be inserted before the response body.<br/>Minimum length =  1.
		"""
		try :
			return self._prebody
		except Exception as e:
			raise e

	@prebody.setter
	def prebody(self, prebody) :
		ur"""Name of file whose contents are to be inserted before the response body.<br/>Minimum length =  1
		"""
		try :
			self._prebody = prebody
		except Exception as e:
			raise e

	@property
	def systemiid(self) :
		ur"""The system IID of the current NetScaler system.
		"""
		try :
			return self._systemiid
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(filterprebodyinjection_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filterprebodyinjection
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
		ur""" Use this API to update filterprebodyinjection.
		"""
		try :
			if type(resource) is not list :
				updateresource = filterprebodyinjection()
				updateresource.prebody = resource.prebody
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of filterprebodyinjection resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = filterprebodyinjection()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the filterprebodyinjection resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = filterprebodyinjection()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class filterprebodyinjection_response(base_response) :
	def __init__(self, length=1) :
		self.filterprebodyinjection = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.filterprebodyinjection = [filterprebodyinjection() for _ in range(length)]

