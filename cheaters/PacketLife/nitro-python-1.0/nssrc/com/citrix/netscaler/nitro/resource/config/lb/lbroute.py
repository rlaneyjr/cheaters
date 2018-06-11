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

class lbroute(base_resource) :
	""" Configuration for LB route resource. """
	def __init__(self) :
		self._network = ""
		self._netmask = ""
		self._gatewayname = ""
		self._td = 0
		self._flags = ""
		self.___count = 0

	@property
	def network(self) :
		ur"""The IP address of the network to which the route belongs.
		"""
		try :
			return self._network
		except Exception as e:
			raise e

	@network.setter
	def network(self, network) :
		ur"""The IP address of the network to which the route belongs.
		"""
		try :
			self._network = network
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""The netmask to which the route belongs.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""The netmask to which the route belongs.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def gatewayname(self) :
		ur"""The name of the route.<br/>Minimum length =  1.
		"""
		try :
			return self._gatewayname
		except Exception as e:
			raise e

	@gatewayname.setter
	def gatewayname(self, gatewayname) :
		ur"""The name of the route.<br/>Minimum length =  1
		"""
		try :
			self._gatewayname = gatewayname
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""State of the configured gateway.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbroute_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbroute
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.network is not None :
				return str(self.network)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lbroute.
		"""
		try :
			if type(resource) is not list :
				addresource = lbroute()
				addresource.network = resource.network
				addresource.netmask = resource.netmask
				addresource.gatewayname = resource.gatewayname
				addresource.td = resource.td
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbroute() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].network = resource[i].network
						addresources[i].netmask = resource[i].netmask
						addresources[i].gatewayname = resource[i].gatewayname
						addresources[i].td = resource[i].td
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lbroute.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbroute()
				if type(resource) !=  type(deleteresource):
					deleteresource.network = resource
				else :
					deleteresource.network = resource.network
					deleteresource.netmask = resource.netmask
					deleteresource.td = resource.td
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbroute() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].network = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbroute() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].network = resource[i].network
							deleteresources[i].netmask = resource[i].netmask
							deleteresources[i].td = resource[i].td
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lbroute resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbroute()
				response = obj.get_resources(client, option_)
			else :
				if type(name) == cls :
					if type(name) is not list :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name)
						response = name.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lbroute() for _ in range(len(name))]
							for i in range(len(name)) :
								option_ = options()
								option_.args = nitro_util.object_to_string_withoutquotes(name[i])
								response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lbroute resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbroute()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lbroute resources configured on NetScaler.
		"""
		try :
			obj = lbroute()
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
		ur""" Use this API to count filtered the set of lbroute resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbroute()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Flags:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

class lbroute_response(base_response) :
	def __init__(self, length=1) :
		self.lbroute = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbroute = [lbroute() for _ in range(length)]

