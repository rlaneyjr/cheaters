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

class cluster(base_resource) :
	def __init__(self) :
		self._clip = ""
		self._password = ""

	@property
	def clip(self) :
		ur"""Cluster IP address to which to add the node.
		"""
		try :
			return self._clip
		except Exception as e:
			raise e

	@clip.setter
	def clip(self, clip) :
		ur"""Cluster IP address to which to add the node.
		"""
		try :
			self._clip = clip
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password for the nsroot account of the configuration coordinator (CCO).
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password for the nsroot account of the configuration coordinator (CCO).
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cluster_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cluster
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.clip is not None :
				return str(self.clip)
			return None
		except Exception as e :
			raise e



	@classmethod
	def join(cls, client, resource) :
		ur""" Use this API to join cluster.
		"""
		try :
			if type(resource) is not list :
				joinresource = cluster()
				joinresource.clip = resource.clip
				joinresource.password = resource.password
				return joinresource.perform_operation(client,"join")
		except Exception as e :
			raise e

class cluster_response(base_response) :
	def __init__(self, length=1) :
		self.cluster = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cluster = [cluster() for _ in range(length)]

