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

class nshostname(base_resource) :
	""" Configuration for host name resource. """
	def __init__(self) :
		self._hostname = ""
		self._ownernode = 0
		self.___count = 0

	@property
	def hostname(self) :
		ur"""Host name for the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._hostname
		except Exception as e:
			raise e

	@hostname.setter
	def hostname(self, hostname) :
		ur"""Host name for the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._hostname = hostname
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		ur"""ID of the cluster node for which you are setting the hostname. Can be configured only through the cluster IP address.<br/>Default value: 255<br/>Maximum length =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		ur"""ID of the cluster node for which you are setting the hostname. Can be configured only through the cluster IP address.<br/>Default value: 255<br/>Maximum length =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nshostname_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nshostname
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ownernode is not None :
				return str(self.ownernode)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nshostname.
		"""
		try :
			if type(resource) is not list :
				updateresource = nshostname()
				updateresource.hostname = resource.hostname
				updateresource.ownernode = resource.ownernode
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nshostname() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].hostname = resource[i].hostname
						updateresources[i].ownernode = resource[i].ownernode
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nshostname resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nshostname()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nshostname resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshostname()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nshostname resources configured on NetScaler.
		"""
		try :
			obj = nshostname()
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
		ur""" Use this API to count filtered the set of nshostname resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshostname()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nshostname_response(base_response) :
	def __init__(self, length=1) :
		self.nshostname = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nshostname = [nshostname() for _ in range(length)]

