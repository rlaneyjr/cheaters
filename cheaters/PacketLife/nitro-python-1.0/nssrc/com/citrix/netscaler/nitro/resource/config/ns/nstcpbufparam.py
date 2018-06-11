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

class nstcpbufparam(base_resource) :
	""" Configuration for tcp buffer parameter resource. """
	def __init__(self) :
		self._size = 0
		self._memlimit = 0

	@property
	def size(self) :
		ur"""TCP buffering size per connection, in kilobytes.<br/>Default value: 64<br/>Minimum length =  4<br/>Maximum length =  20480.
		"""
		try :
			return self._size
		except Exception as e:
			raise e

	@size.setter
	def size(self, size) :
		ur"""TCP buffering size per connection, in kilobytes.<br/>Default value: 64<br/>Minimum length =  4<br/>Maximum length =  20480
		"""
		try :
			self._size = size
		except Exception as e:
			raise e

	@property
	def memlimit(self) :
		ur"""Maximum memory, in megabytes, that can be used for buffering.<br/>Default value: 64.
		"""
		try :
			return self._memlimit
		except Exception as e:
			raise e

	@memlimit.setter
	def memlimit(self, memlimit) :
		ur"""Maximum memory, in megabytes, that can be used for buffering.<br/>Default value: 64
		"""
		try :
			self._memlimit = memlimit
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstcpbufparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstcpbufparam
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
		ur""" Use this API to update nstcpbufparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = nstcpbufparam()
				updateresource.size = resource.size
				updateresource.memlimit = resource.memlimit
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nstcpbufparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nstcpbufparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nstcpbufparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nstcpbufparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nstcpbufparam_response(base_response) :
	def __init__(self, length=1) :
		self.nstcpbufparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstcpbufparam = [nstcpbufparam() for _ in range(length)]

