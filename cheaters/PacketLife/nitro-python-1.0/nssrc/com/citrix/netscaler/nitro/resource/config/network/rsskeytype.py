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

class rsskeytype(base_resource) :
	""" Configuration for RSS key type resource. """
	def __init__(self) :
		self._rsstype = ""

	@property
	def rsstype(self) :
		ur"""Type of RSS key, possible values ASYMMETRIC and SYMMETRIC. .<br/>Default value: ASYMMETRIC<br/>Possible values = ASYMMETRIC, SYMMETRIC.
		"""
		try :
			return self._rsstype
		except Exception as e:
			raise e

	@rsstype.setter
	def rsstype(self, rsstype) :
		ur"""Type of RSS key, possible values ASYMMETRIC and SYMMETRIC. .<br/>Default value: ASYMMETRIC<br/>Possible values = ASYMMETRIC, SYMMETRIC
		"""
		try :
			self._rsstype = rsstype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rsskeytype_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rsskeytype
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
		ur""" Use this API to update rsskeytype.
		"""
		try :
			if type(resource) is not list :
				updateresource = rsskeytype()
				updateresource.rsstype = resource.rsstype
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the rsskeytype resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rsskeytype()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Rsstype:
		ASYMMETRIC = "ASYMMETRIC"
		SYMMETRIC = "SYMMETRIC"

class rsskeytype_response(base_response) :
	def __init__(self, length=1) :
		self.rsskeytype = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rsskeytype = [rsskeytype() for _ in range(length)]

