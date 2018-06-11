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

class lbwlm(base_resource) :
	""" Configuration for web log manager resource. """
	def __init__(self) :
		self._wlmname = ""
		self._ipaddress = ""
		self._port = 0
		self._lbuid = ""
		self._katimeout = 0
		self._secure = ""
		self._state = ""
		self.___count = 0

	@property
	def wlmname(self) :
		ur"""The name of the Work Load Manager.<br/>Minimum length =  1.
		"""
		try :
			return self._wlmname
		except Exception as e:
			raise e

	@wlmname.setter
	def wlmname(self, wlmname) :
		ur"""The name of the Work Load Manager.<br/>Minimum length =  1
		"""
		try :
			self._wlmname = wlmname
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""The IP address of the WLM.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""The IP address of the WLM.
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""The port of the WLM.<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""The port of the WLM.<br/>Range 1 - 65535
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def lbuid(self) :
		ur"""The LBUID for the Load Balancer to communicate to the Work Load Manager.
		"""
		try :
			return self._lbuid
		except Exception as e:
			raise e

	@lbuid.setter
	def lbuid(self, lbuid) :
		ur"""The LBUID for the Load Balancer to communicate to the Work Load Manager.
		"""
		try :
			self._lbuid = lbuid
		except Exception as e:
			raise e

	@property
	def katimeout(self) :
		ur"""The idle time period after which NS would probe the WLM. The value ranges from 1 to 1440 minutes.<br/>Default value: 2<br/>Maximum length =  1440.
		"""
		try :
			return self._katimeout
		except Exception as e:
			raise e

	@katimeout.setter
	def katimeout(self, katimeout) :
		ur"""The idle time period after which NS would probe the WLM. The value ranges from 1 to 1440 minutes.<br/>Default value: 2<br/>Maximum length =  1440
		"""
		try :
			self._katimeout = katimeout
		except Exception as e:
			raise e

	@property
	def secure(self) :
		ur"""Use this parameter to enable secure mode of communication with WLM.<br/>Possible values = YES, NO.
		"""
		try :
			return self._secure
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""State of the WLM.<br/>Possible values = ACTIVE, INACTIVE, UNKNOWN.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbwlm_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbwlm
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.wlmname is not None :
				return str(self.wlmname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lbwlm.
		"""
		try :
			if type(resource) is not list :
				addresource = lbwlm()
				addresource.wlmname = resource.wlmname
				addresource.ipaddress = resource.ipaddress
				addresource.port = resource.port
				addresource.lbuid = resource.lbuid
				addresource.katimeout = resource.katimeout
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbwlm() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].wlmname = resource[i].wlmname
						addresources[i].ipaddress = resource[i].ipaddress
						addresources[i].port = resource[i].port
						addresources[i].lbuid = resource[i].lbuid
						addresources[i].katimeout = resource[i].katimeout
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lbwlm.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbwlm()
				if type(resource) !=  type(deleteresource):
					deleteresource.wlmname = resource
				else :
					deleteresource.wlmname = resource.wlmname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbwlm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].wlmname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbwlm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].wlmname = resource[i].wlmname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lbwlm.
		"""
		try :
			if type(resource) is not list :
				updateresource = lbwlm()
				updateresource.wlmname = resource.wlmname
				updateresource.katimeout = resource.katimeout
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lbwlm() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].wlmname = resource[i].wlmname
						updateresources[i].katimeout = resource[i].katimeout
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lbwlm resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbwlm()
				if type(resource) !=  type(unsetresource):
					unsetresource.wlmname = resource
				else :
					unsetresource.wlmname = resource.wlmname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbwlm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].wlmname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbwlm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].wlmname = resource[i].wlmname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lbwlm resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbwlm()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lbwlm()
						obj.wlmname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lbwlm() for _ in range(len(name))]
							obj = [lbwlm() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lbwlm()
								obj[i].wlmname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lbwlm resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbwlm()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lbwlm resources configured on NetScaler.
		"""
		try :
			obj = lbwlm()
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
		ur""" Use this API to count filtered the set of lbwlm resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbwlm()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Secure:
		YES = "YES"
		NO = "NO"

	class State:
		ACTIVE = "ACTIVE"
		INACTIVE = "INACTIVE"
		UNKNOWN = "UNKNOWN"

class lbwlm_response(base_response) :
	def __init__(self, length=1) :
		self.lbwlm = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbwlm = [lbwlm() for _ in range(length)]

