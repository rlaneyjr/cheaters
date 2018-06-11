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

class ip6tunnel(base_resource) :
	""" Configuration for ip6 Tunnel resource. """
	def __init__(self) :
		self._name = ""
		self._remote = ""
		self._local = ""
		self._remoteip = ""
		self._type = 0
		self._encapip = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the IPv6 Tunnel. Cannot be changed after the service group is created. Must begin with a number or letter, and can consist of letters, numbers, and the @ _ - . (period) : (colon) # and space ( ) characters.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the IPv6 Tunnel. Cannot be changed after the service group is created. Must begin with a number or letter, and can consist of letters, numbers, and the @ _ - . (period) : (colon) # and space ( ) characters.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def remote(self) :
		ur"""An IPv6 address of the remote NetScaler appliance used to set up the tunnel.<br/>Minimum length =  1.
		"""
		try :
			return self._remote
		except Exception as e:
			raise e

	@remote.setter
	def remote(self, remote) :
		ur"""An IPv6 address of the remote NetScaler appliance used to set up the tunnel.<br/>Minimum length =  1
		"""
		try :
			self._remote = remote
		except Exception as e:
			raise e

	@property
	def local(self) :
		ur"""An IPv6 address of the local NetScaler appliance used to set up the tunnel.
		"""
		try :
			return self._local
		except Exception as e:
			raise e

	@local.setter
	def local(self, local) :
		ur"""An IPv6 address of the local NetScaler appliance used to set up the tunnel.
		"""
		try :
			self._local = local
		except Exception as e:
			raise e

	@property
	def remoteip(self) :
		ur"""The remote IP address or subnet of the tunnel.
		"""
		try :
			return self._remoteip
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""The type of this tunnel.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def encapip(self) :
		ur"""The effective local IP address of the tunnel. Used as the source of the encapsulated packets.
		"""
		try :
			return self._encapip
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ip6tunnel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ip6tunnel
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add ip6tunnel.
		"""
		try :
			if type(resource) is not list :
				addresource = ip6tunnel()
				addresource.name = resource.name
				addresource.remote = resource.remote
				addresource.local = resource.local
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ ip6tunnel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].remote = resource[i].remote
						addresources[i].local = resource[i].local
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete ip6tunnel.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ip6tunnel()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ ip6tunnel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ ip6tunnel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the ip6tunnel resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ip6tunnel()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = ip6tunnel()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [ip6tunnel() for _ in range(len(name))]
							obj = [ip6tunnel() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = ip6tunnel()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the ip6tunnel resources that are configured on netscaler.
	# This uses ip6tunnel_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = ip6tunnel()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of ip6tunnel resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ip6tunnel()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the ip6tunnel resources configured on NetScaler.
		"""
		try :
			obj = ip6tunnel()
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
		ur""" Use this API to count filtered the set of ip6tunnel resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ip6tunnel()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class ip6tunnel_response(base_response) :
	def __init__(self, length=1) :
		self.ip6tunnel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ip6tunnel = [ip6tunnel() for _ in range(length)]

