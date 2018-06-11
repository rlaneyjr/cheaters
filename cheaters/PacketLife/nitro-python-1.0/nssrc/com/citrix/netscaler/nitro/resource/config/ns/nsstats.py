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

class nsstats(base_resource) :
	""" Configuration for stats resource. """
	def __init__(self) :
		self._cleanuplevel = ""

	@property
	def cleanuplevel(self) :
		ur"""The level of stats to be cleared. 'global' option will clear global counters only, 'all' option will clear all device counters also along with global counters. For both the cases only 'ever incrementing counters' i.e. total counters will be cleared.<br/>Possible values = global, all.
		"""
		try :
			return self._cleanuplevel
		except Exception as e:
			raise e

	@cleanuplevel.setter
	def cleanuplevel(self, cleanuplevel) :
		ur"""The level of stats to be cleared. 'global' option will clear global counters only, 'all' option will clear all device counters also along with global counters. For both the cases only 'ever incrementing counters' i.e. total counters will be cleared.<br/>Possible values = global, all
		"""
		try :
			self._cleanuplevel = cleanuplevel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsstats_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsstats
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
	def clear(cls, client, resource) :
		ur""" Use this API to clear nsstats.
		"""
		try :
			if type(resource) is not list :
				clearresource = nsstats()
				clearresource.cleanuplevel = resource.cleanuplevel
				return clearresource.perform_operation(client,"clear")
		except Exception as e :
			raise e

	class Cleanuplevel:
		GLOBAL = "global"
		all = "all"

class nsstats_response(base_response) :
	def __init__(self, length=1) :
		self.nsstats = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsstats = [nsstats() for _ in range(length)]

