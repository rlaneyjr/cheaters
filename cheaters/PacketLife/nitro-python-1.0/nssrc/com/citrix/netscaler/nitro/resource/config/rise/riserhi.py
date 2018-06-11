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

class riserhi(base_resource) :
	""" Configuration for RISE RHI rules resource. """

		#------- Read only Parameter ---------

	def __init__(self) :
		self._ipaddress = ""
		self._prefixlen = 0
		self._hostrtgw = ""
		self._nexthopvlan = 0
		self._weight = 0
		self._vserverrhilevel = ""
		self.___count = 0

	@property
	def ipaddress(self) :
		ur"""(V)IP advertised.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@property
	def prefixlen(self) :
		ur"""Prefix Length.
		"""
		try :
			return self._prefixlen
		except Exception as e:
			raise e

	@property
	def hostrtgw(self) :
		ur"""Gateway for the advertised IP.
		"""
		try :
			return self._hostrtgw
		except Exception as e:
			raise e

	@property
	def nexthopvlan(self) :
		ur"""Vlan id on which the gateway is present.
		"""
		try :
			return self._nexthopvlan
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Cost of the route.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@property
	def vserverrhilevel(self) :
		ur"""Advertisement level.<br/>Default value: ONE_VSERVER<br/>Possible values = ONE_VSERVER, ALL_VSERVERS, NONE, VSVR_CNTRLD.
		"""
		try :
			return self._vserverrhilevel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(riserhi_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.riserhi
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
		ur""" Use this API to fetch all the riserhi resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = riserhi()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of riserhi resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = riserhi()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the riserhi resources configured on NetScaler.
		"""
		try :
			obj = riserhi()
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
		ur""" Use this API to count filtered the set of riserhi resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = riserhi()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Vserverrhilevel:
		ONE_VSERVER = "ONE_VSERVER"
		ALL_VSERVERS = "ALL_VSERVERS"
		NONE = "NONE"
		VSVR_CNTRLD = "VSVR_CNTRLD"

class riserhi_response(base_response) :
	def __init__(self, length=1) :
		self.riserhi = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.riserhi = [riserhi() for _ in range(length)]

