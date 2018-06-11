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

class nsrunningconfig(base_resource) :
	""" Configuration for running configuration resource. """
	def __init__(self) :
		self._withdefaults = False
		self._response = ""

	@property
	def withdefaults(self) :
		ur"""Include default values of parameters that have not been explicitly configured. If this argument is disabled, such parameters are not included.
		"""
		try :
			return self._withdefaults
		except Exception as e:
			raise e

	@withdefaults.setter
	def withdefaults(self, withdefaults) :
		ur"""Include default values of parameters that have not been explicitly configured. If this argument is disabled, such parameters are not included.
		"""
		try :
			self._withdefaults = withdefaults
		except Exception as e:
			raise e

	@property
	def response(self) :
		ur"""running config data as text blob.
		"""
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsrunningconfig_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsrunningconfig
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
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsrunningconfig resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsrunningconfig()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the nsrunningconfig resources that are configured on netscaler.
	# This uses nsrunningconfig_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nsrunningconfig()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nsrunningconfig_response(base_response) :
	def __init__(self, length=1) :
		self.nsrunningconfig = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsrunningconfig = [nsrunningconfig() for _ in range(length)]

