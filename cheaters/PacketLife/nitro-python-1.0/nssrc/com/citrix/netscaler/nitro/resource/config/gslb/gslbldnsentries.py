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

class gslbldnsentries(base_resource) :
	""" Configuration for LDAP entries resource. """

		#------- Read only Parameter ---------

	def __init__(self) :
		self._sitename = ""
		self._numsites = 0
		self._ipaddress = ""
		self._ttl = 0
		self._name = ""
		self._rtt = []
		self.___count = 0

	@property
	def sitename(self) :
		ur"""The GSLB site name.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@property
	def numsites(self) :
		ur"""Specifies the number of gslb sites.
		"""
		try :
			return self._numsites
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""IP address of the LDNS server.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		ur"""TTL value of the LDNS entry.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Monitor that is currently being used to monitor the LDNS ip..
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@property
	def rtt(self) :
		ur"""RTT value of the LDNS entry for all gslb sites.
		"""
		try :
			return self._rtt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbldnsentries_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbldnsentries
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
		ur""" Use this API to clear gslbldnsentries.
		"""
		try :
			if type(resource) is not list :
				clearresource = gslbldnsentries()
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ gslbldnsentries() for _ in range(len(resource))]
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the gslbldnsentries resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbldnsentries()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of gslbldnsentries resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbldnsentries()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the gslbldnsentries resources configured on NetScaler.
		"""
		try :
			obj = gslbldnsentries()
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
		ur""" Use this API to count filtered the set of gslbldnsentries resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbldnsentries()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class gslbldnsentries_response(base_response) :
	def __init__(self, length=1) :
		self.gslbldnsentries = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbldnsentries = [gslbldnsentries() for _ in range(length)]

