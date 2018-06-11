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

class cacheselector(base_resource) :
	""" Configuration for cache selector resource. """
	def __init__(self) :
		self._selectorname = ""
		self._rule = []
		self._flags = 0
		self.___count = 0

	@property
	def selectorname(self) :
		ur"""Name for the selector.  Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			return self._selectorname
		except Exception as e:
			raise e

	@selectorname.setter
	def selectorname(self, selectorname) :
		ur"""Name for the selector.  Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			self._selectorname = selectorname
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""One or multiple PIXL expressions for evaluating an HTTP request or response.<br/>Minimum length =  1.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""One or multiple PIXL expressions for evaluating an HTTP request or response.<br/>Minimum length =  1
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""Flags.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cacheselector_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cacheselector
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.selectorname is not None :
				return str(self.selectorname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add cacheselector.
		"""
		try :
			if type(resource) is not list :
				addresource = cacheselector()
				addresource.selectorname = resource.selectorname
				addresource.rule = resource.rule
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cacheselector() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].selectorname = resource[i].selectorname
						addresources[i].rule = resource[i].rule
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete cacheselector.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cacheselector()
				if type(resource) !=  type(deleteresource):
					deleteresource.selectorname = resource
				else :
					deleteresource.selectorname = resource.selectorname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cacheselector() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].selectorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cacheselector() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].selectorname = resource[i].selectorname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update cacheselector.
		"""
		try :
			if type(resource) is not list :
				updateresource = cacheselector()
				updateresource.selectorname = resource.selectorname
				updateresource.rule = resource.rule
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ cacheselector() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].selectorname = resource[i].selectorname
						updateresources[i].rule = resource[i].rule
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cacheselector resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cacheselector()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = cacheselector()
						obj.selectorname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [cacheselector() for _ in range(len(name))]
							obj = [cacheselector() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = cacheselector()
								obj[i].selectorname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of cacheselector resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheselector()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the cacheselector resources configured on NetScaler.
		"""
		try :
			obj = cacheselector()
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
		ur""" Use this API to count filtered the set of cacheselector resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cacheselector()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class cacheselector_response(base_response) :
	def __init__(self, length=1) :
		self.cacheselector = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cacheselector = [cacheselector() for _ in range(length)]

