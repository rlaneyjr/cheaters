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

class hasync(base_resource) :
	""" Configuration for sync resource. """
	def __init__(self) :
		self._force = False
		self._save = ""

	@property
	def force(self) :
		ur"""Force synchronization regardless of the state of HA propagation and HA synchronization on either node.
		"""
		try :
			return self._force
		except Exception as e:
			raise e

	@force.setter
	def force(self, force) :
		ur"""Force synchronization regardless of the state of HA propagation and HA synchronization on either node.
		"""
		try :
			self._force = force
		except Exception as e:
			raise e

	@property
	def save(self) :
		ur"""After synchronization, automatically save the configuration in the secondary node configuration file (ns.conf) without prompting for confirmation.<br/>Possible values = YES, NO.
		"""
		try :
			return self._save
		except Exception as e:
			raise e

	@save.setter
	def save(self, save) :
		ur"""After synchronization, automatically save the configuration in the secondary node configuration file (ns.conf) without prompting for confirmation.<br/>Possible values = YES, NO
		"""
		try :
			self._save = save
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(hasync_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.hasync
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
	def Force(cls, client, resource) :
		ur""" Use this API to Force hasync.
		"""
		try :
			if type(resource) is not list :
				Forceresource = hasync()
				Forceresource.force = resource.force
				Forceresource.save = resource.save
				return Forceresource.perform_operation(client,"Force")
		except Exception as e :
			raise e

	class Save:
		YES = "YES"
		NO = "NO"

class hasync_response(base_response) :
	def __init__(self, length=1) :
		self.hasync = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.hasync = [hasync() for _ in range(length)]

