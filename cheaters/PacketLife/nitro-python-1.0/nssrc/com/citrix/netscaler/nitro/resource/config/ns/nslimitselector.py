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

class nslimitselector(base_resource) :
	""" Configuration for limit selector resource. """
	def __init__(self) :
		self._selectorname = ""
		self._rule = []
		self.___count = 0

	@property
	def selectorname(self) :
		try :
			return self._selectorname
		except Exception as e:
			raise e

	@selectorname.setter
	def selectorname(self, selectorname) :
		try :
			self._selectorname = selectorname
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur""".<br/>Minimum length =  1.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur""".<br/>Minimum length =  1
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslimitselector_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslimitselector
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
		ur""" Use this API to add nslimitselector.
		"""
		try :
			if type(resource) is not list :
				addresource = nslimitselector()
				addresource.selectorname = resource.selectorname
				addresource.rule = resource.rule
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nslimitselector() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].selectorname = resource[i].selectorname
						addresources[i].rule = resource[i].rule
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nslimitselector.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nslimitselector()
				if type(resource) !=  type(deleteresource):
					deleteresource.selectorname = resource
				else :
					deleteresource.selectorname = resource.selectorname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslimitselector() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].selectorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslimitselector() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].selectorname = resource[i].selectorname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nslimitselector.
		"""
		try :
			if type(resource) is not list :
				updateresource = nslimitselector()
				updateresource.selectorname = resource.selectorname
				updateresource.rule = resource.rule
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nslimitselector() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].selectorname = resource[i].selectorname
						updateresources[i].rule = resource[i].rule
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nslimitselector resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nslimitselector()
				if type(resource) !=  type(unsetresource):
					unsetresource.selectorname = resource
				else :
					unsetresource.selectorname = resource.selectorname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nslimitselector() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].selectorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nslimitselector() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].selectorname = resource[i].selectorname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nslimitselector resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nslimitselector()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nslimitselector()
						obj.selectorname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nslimitselector() for _ in range(len(name))]
							obj = [nslimitselector() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nslimitselector()
								obj[i].selectorname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nslimitselector resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslimitselector()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nslimitselector resources configured on NetScaler.
		"""
		try :
			obj = nslimitselector()
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
		ur""" Use this API to count filtered the set of nslimitselector resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslimitselector()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nslimitselector_response(base_response) :
	def __init__(self, length=1) :
		self.nslimitselector = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslimitselector = [nslimitselector() for _ in range(length)]

