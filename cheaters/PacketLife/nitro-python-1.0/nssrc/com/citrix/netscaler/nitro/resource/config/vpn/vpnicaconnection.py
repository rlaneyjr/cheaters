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

class vpnicaconnection(base_resource) :
	""" Configuration for active ica connections resource. """
	def __init__(self) :
		self._username = ""
		self._domain = ""
		self._srcip = ""
		self._srcport = 0
		self._destip = ""
		self._destport = 0
		self._peid = 0
		self.___count = 0

	@property
	def username(self) :
		ur"""User name for which to display connections.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""User name for which to display connections.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""The domain name.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@property
	def srcip(self) :
		ur"""The client IP address.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		ur"""The client port.<br/>Range 1 - 65535.
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@property
	def destip(self) :
		ur"""The CPS server IP address.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		ur"""The CPS server port.<br/>Range 1 - 65535.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@property
	def peid(self) :
		ur"""Core id of the session owner.
		"""
		try :
			return self._peid
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnicaconnection_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnicaconnection
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
		ur""" Use this API to fetch all the vpnicaconnection resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnicaconnection()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the vpnicaconnection resources that are configured on netscaler.
	# This uses vpnicaconnection_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = vpnicaconnection()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of vpnicaconnection resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnicaconnection()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the vpnicaconnection resources configured on NetScaler.
		"""
		try :
			obj = vpnicaconnection()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of vpnicaconnection resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnicaconnection()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class vpnicaconnection_response(base_response) :
	def __init__(self, length=1) :
		self.vpnicaconnection = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnicaconnection = [vpnicaconnection() for _ in range(length)]

