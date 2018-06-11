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

class systemcollectionparam(base_resource) :
	""" Configuration for collection parameter resource. """
	def __init__(self) :
		self._communityname = ""
		self._loglevel = ""
		self._datapath = ""

	@property
	def communityname(self) :
		ur"""SNMPv1 community name for authentication.
		"""
		try :
			return self._communityname
		except Exception as e:
			raise e

	@communityname.setter
	def communityname(self, communityname) :
		ur"""SNMPv1 community name for authentication.
		"""
		try :
			self._communityname = communityname
		except Exception as e:
			raise e

	@property
	def loglevel(self) :
		ur"""specify the log level. Possible values CRITICAL,WARNING,INFO,DEBUG1,DEBUG2.<br/>Minimum length =  1.
		"""
		try :
			return self._loglevel
		except Exception as e:
			raise e

	@loglevel.setter
	def loglevel(self, loglevel) :
		ur"""specify the log level. Possible values CRITICAL,WARNING,INFO,DEBUG1,DEBUG2.<br/>Minimum length =  1
		"""
		try :
			self._loglevel = loglevel
		except Exception as e:
			raise e

	@property
	def datapath(self) :
		ur"""specify the data path to the database.<br/>Minimum length =  1.
		"""
		try :
			return self._datapath
		except Exception as e:
			raise e

	@datapath.setter
	def datapath(self, datapath) :
		ur"""specify the data path to the database.<br/>Minimum length =  1
		"""
		try :
			self._datapath = datapath
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemcollectionparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemcollectionparam
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
		ur""" Use this API to update systemcollectionparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = systemcollectionparam()
				updateresource.communityname = resource.communityname
				updateresource.loglevel = resource.loglevel
				updateresource.datapath = resource.datapath
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of systemcollectionparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = systemcollectionparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systemcollectionparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemcollectionparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class systemcollectionparam_response(base_response) :
	def __init__(self, length=1) :
		self.systemcollectionparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemcollectionparam = [systemcollectionparam() for _ in range(length)]

