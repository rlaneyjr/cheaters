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

class autoscaleprofile(base_resource) :
	""" Configuration for autoscale profile resource. """
	def __init__(self) :
		self._name = ""
		self._type = ""
		self._url = ""
		self._apikey = ""
		self._sharedsecret = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""AutoScale profile name.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""AutoScale profile name.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""The type of profile.<br/>Possible values = CLOUDSTACK.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""The type of profile.<br/>Possible values = CLOUDSTACK
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def url(self) :
		ur"""URL providing the service.<br/>Minimum length =  1.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		ur"""URL providing the service.<br/>Minimum length =  1
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def apikey(self) :
		ur"""api key for authentication with service.<br/>Minimum length =  1.
		"""
		try :
			return self._apikey
		except Exception as e:
			raise e

	@apikey.setter
	def apikey(self, apikey) :
		ur"""api key for authentication with service.<br/>Minimum length =  1
		"""
		try :
			self._apikey = apikey
		except Exception as e:
			raise e

	@property
	def sharedsecret(self) :
		ur"""shared secret for authentication with service.<br/>Minimum length =  1.
		"""
		try :
			return self._sharedsecret
		except Exception as e:
			raise e

	@sharedsecret.setter
	def sharedsecret(self, sharedsecret) :
		ur"""shared secret for authentication with service.<br/>Minimum length =  1
		"""
		try :
			self._sharedsecret = sharedsecret
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(autoscaleprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscaleprofile
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
		ur""" Use this API to add autoscaleprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = autoscaleprofile()
				addresource.name = resource.name
				addresource.type = resource.type
				addresource.url = resource.url
				addresource.apikey = resource.apikey
				addresource.sharedsecret = resource.sharedsecret
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ autoscaleprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].type = resource[i].type
						addresources[i].url = resource[i].url
						addresources[i].apikey = resource[i].apikey
						addresources[i].sharedsecret = resource[i].sharedsecret
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete autoscaleprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = autoscaleprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ autoscaleprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ autoscaleprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update autoscaleprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = autoscaleprofile()
				updateresource.name = resource.name
				updateresource.url = resource.url
				updateresource.apikey = resource.apikey
				updateresource.sharedsecret = resource.sharedsecret
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ autoscaleprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].url = resource[i].url
						updateresources[i].apikey = resource[i].apikey
						updateresources[i].sharedsecret = resource[i].sharedsecret
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the autoscaleprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = autoscaleprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = autoscaleprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [autoscaleprofile() for _ in range(len(name))]
							obj = [autoscaleprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = autoscaleprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of autoscaleprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = autoscaleprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the autoscaleprofile resources configured on NetScaler.
		"""
		try :
			obj = autoscaleprofile()
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
		ur""" Use this API to count filtered the set of autoscaleprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = autoscaleprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		CLOUDSTACK = "CLOUDSTACK"

class autoscaleprofile_response(base_response) :
	def __init__(self, length=1) :
		self.autoscaleprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.autoscaleprofile = [autoscaleprofile() for _ in range(length)]

