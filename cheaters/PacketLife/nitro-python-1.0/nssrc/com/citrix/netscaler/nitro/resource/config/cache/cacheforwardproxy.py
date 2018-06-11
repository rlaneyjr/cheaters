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

class cacheforwardproxy(base_resource) :
	""" Configuration for forward proxy resource. """
	def __init__(self) :
		self._ipaddress = ""
		self._port = 0
		self.___count = 0

	@property
	def ipaddress(self) :
		ur"""IP address of the NetScaler appliance or a cache server for which the cache acts as a proxy. Requests coming to the NetScaler with the configured IP address are forwarded to the particular address, without involving the Integrated Cache in any way.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""IP address of the NetScaler appliance or a cache server for which the cache acts as a proxy. Requests coming to the NetScaler with the configured IP address are forwarded to the particular address, without involving the Integrated Cache in any way.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port on the NetScaler appliance or a server for which the cache acts as a proxy.<br/>Minimum length =  1<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""Port on the NetScaler appliance or a server for which the cache acts as a proxy.<br/>Minimum length =  1<br/>Range 1 - 65535
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cacheforwardproxy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cacheforwardproxy
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ipaddress is not None :
				return str(self.ipaddress)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add cacheforwardproxy.
		"""
		try :
			if type(resource) is not list :
				addresource = cacheforwardproxy()
				addresource.ipaddress = resource.ipaddress
				addresource.port = resource.port
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cacheforwardproxy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].port = resource[i].port
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete cacheforwardproxy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cacheforwardproxy()
				if type(resource) !=  type(deleteresource):
					deleteresource.ipaddress = resource
				else :
					deleteresource.ipaddress = resource.ipaddress
					deleteresource.port = resource.port
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cacheforwardproxy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipaddress = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cacheforwardproxy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipaddress = resource[i].ipaddress
							deleteresources[i].port = resource[i].port
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cacheforwardproxy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cacheforwardproxy()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of cacheforwardproxy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheforwardproxy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the cacheforwardproxy resources configured on NetScaler.
		"""
		try :
			obj = cacheforwardproxy()
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
		ur""" Use this API to count filtered the set of cacheforwardproxy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheforwardproxy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class cacheforwardproxy_response(base_response) :
	def __init__(self, length=1) :
		self.cacheforwardproxy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cacheforwardproxy = [cacheforwardproxy() for _ in range(length)]

