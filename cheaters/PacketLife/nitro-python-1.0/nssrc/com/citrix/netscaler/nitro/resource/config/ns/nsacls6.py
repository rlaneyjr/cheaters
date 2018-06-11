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

class nsacls6(base_resource) :
	""" Configuration for ACL6 entry resource. """

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsacls6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsacls6
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
	def clear(cls, client, resource="") :
		ur""" Use this API to clear nsacls6.
		"""
		try :
			if type(resource) is not list :
				clearresource = nsacls6()
				return clearresource.perform_operation(client,"clear")
		except Exception as e :
			raise e

	@classmethod
	def apply(cls, client, resource="") :
		ur""" Use this API to apply nsacls6.
		"""
		try :
			if type(resource) is not list :
				applyresource = nsacls6()
				return applyresource.perform_operation(client,"apply")
		except Exception as e :
			raise e

	@classmethod
	def renumber(cls, client, resource="") :
		ur""" Use this API to renumber nsacls6.
		"""
		try :
			if type(resource) is not list :
				renumberresource = nsacls6()
				return renumberresource.perform_operation(client,"renumber")
		except Exception as e :
			raise e

class nsacls6_response(base_response) :
	def __init__(self, length=1) :
		self.nsacls6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsacls6 = [nsacls6() for _ in range(length)]

