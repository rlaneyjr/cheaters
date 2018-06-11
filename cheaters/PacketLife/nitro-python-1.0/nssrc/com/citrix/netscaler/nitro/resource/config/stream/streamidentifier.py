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

class streamidentifier(base_resource) :
	""" Configuration for identifier resource. """
	def __init__(self) :
		self._name = ""
		self._selectorname = ""
		self._interval = 0
		self._samplecount = 0
		self._sort = ""
		self._rule = []
		self.___count = 0

	@property
	def name(self) :
		ur"""The name of stream identifier.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of stream identifier.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def selectorname(self) :
		ur"""Name of the selector to use with the stream identifier.<br/>Minimum length =  1.
		"""
		try :
			return self._selectorname
		except Exception as e:
			raise e

	@selectorname.setter
	def selectorname(self, selectorname) :
		ur"""Name of the selector to use with the stream identifier.<br/>Minimum length =  1
		"""
		try :
			self._selectorname = selectorname
		except Exception as e:
			raise e

	@property
	def interval(self) :
		ur"""Number of minutes of data to use when calculating session statistics (number of requests, bandwidth, and response times). The interval is a moving window that keeps the most recently collected data. Older data is discarded at regular intervals.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._interval
		except Exception as e:
			raise e

	@interval.setter
	def interval(self, interval) :
		ur"""Number of minutes of data to use when calculating session statistics (number of requests, bandwidth, and response times). The interval is a moving window that keeps the most recently collected data. Older data is discarded at regular intervals.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._interval = interval
		except Exception as e:
			raise e

	@property
	def samplecount(self) :
		ur"""Size of the sample from which to select a request for evaluation. The smaller the sample count, the more accurate is the statistical data. To evaluate all requests, set the sample count to 1. However, such a low setting can result in excessive consumption of memory and processing resources.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._samplecount
		except Exception as e:
			raise e

	@samplecount.setter
	def samplecount(self, samplecount) :
		ur"""Size of the sample from which to select a request for evaluation. The smaller the sample count, the more accurate is the statistical data. To evaluate all requests, set the sample count to 1. However, such a low setting can result in excessive consumption of memory and processing resources.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._samplecount = samplecount
		except Exception as e:
			raise e

	@property
	def sort(self) :
		ur"""Sort stored records by the specified statistics column, in descending order. Performed during data collection, the sorting enables real-time data evaluation through NetScaler policies (for example, compression and caching policies) that use functions such as IS_TOP(n).<br/>Default value: REQUESTS<br/>Possible values = REQUESTS, CONNECTIONS, RESPTIME, BANDWIDTH, NONE.
		"""
		try :
			return self._sort
		except Exception as e:
			raise e

	@sort.setter
	def sort(self, sort) :
		ur"""Sort stored records by the specified statistics column, in descending order. Performed during data collection, the sorting enables real-time data evaluation through NetScaler policies (for example, compression and caching policies) that use functions such as IS_TOP(n).<br/>Default value: REQUESTS<br/>Possible values = REQUESTS, CONNECTIONS, RESPTIME, BANDWIDTH, NONE
		"""
		try :
			self._sort = sort
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Rule.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(streamidentifier_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.streamidentifier
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
		ur""" Use this API to add streamidentifier.
		"""
		try :
			if type(resource) is not list :
				addresource = streamidentifier()
				addresource.name = resource.name
				addresource.selectorname = resource.selectorname
				addresource.interval = resource.interval
				addresource.samplecount = resource.samplecount
				addresource.sort = resource.sort
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ streamidentifier() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].selectorname = resource[i].selectorname
						addresources[i].interval = resource[i].interval
						addresources[i].samplecount = resource[i].samplecount
						addresources[i].sort = resource[i].sort
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update streamidentifier.
		"""
		try :
			if type(resource) is not list :
				updateresource = streamidentifier()
				updateresource.name = resource.name
				updateresource.selectorname = resource.selectorname
				updateresource.interval = resource.interval
				updateresource.samplecount = resource.samplecount
				updateresource.sort = resource.sort
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ streamidentifier() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].selectorname = resource[i].selectorname
						updateresources[i].interval = resource[i].interval
						updateresources[i].samplecount = resource[i].samplecount
						updateresources[i].sort = resource[i].sort
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of streamidentifier resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = streamidentifier()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete streamidentifier.
		"""
		try :
			if type(resource) is not list :
				deleteresource = streamidentifier()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ streamidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the streamidentifier resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = streamidentifier()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = streamidentifier()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [streamidentifier() for _ in range(len(name))]
							obj = [streamidentifier() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = streamidentifier()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of streamidentifier resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = streamidentifier()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the streamidentifier resources configured on NetScaler.
		"""
		try :
			obj = streamidentifier()
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
		ur""" Use this API to count filtered the set of streamidentifier resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = streamidentifier()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sort:
		REQUESTS = "REQUESTS"
		CONNECTIONS = "CONNECTIONS"
		RESPTIME = "RESPTIME"
		BANDWIDTH = "BANDWIDTH"
		NONE = "NONE"

class streamidentifier_response(base_response) :
	def __init__(self, length=1) :
		self.streamidentifier = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.streamidentifier = [streamidentifier() for _ in range(length)]

