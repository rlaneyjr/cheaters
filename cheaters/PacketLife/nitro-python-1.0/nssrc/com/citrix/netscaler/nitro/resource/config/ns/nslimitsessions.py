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

class nslimitsessions(base_resource) :
	""" Configuration for limit sessions resource. """
	def __init__(self) :
		self._limitidentifier = ""
		self._detail = False
		self._timeout = 0
		self._hits = 0
		self._drop = 0
		self._number = []
		self._name = ""
		self._unit = 0
		self._flags = 0
		self._referencecount = 0
		self._maxbandwidth = 0
		self._selectoripv61 = ""
		self._selectoripv62 = ""
		self._flag = 0
		self.___count = 0

	@property
	def limitidentifier(self) :
		ur"""Name of the rate limit identifier for which to display the sessions.<br/>Minimum length =  1.
		"""
		try :
			return self._limitidentifier
		except Exception as e:
			raise e

	@limitidentifier.setter
	def limitidentifier(self, limitidentifier) :
		ur"""Name of the rate limit identifier for which to display the sessions.<br/>Minimum length =  1
		"""
		try :
			self._limitidentifier = limitidentifier
		except Exception as e:
			raise e

	@property
	def detail(self) :
		ur"""Show the individual hash values.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		ur"""Show the individual hash values.
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		ur"""The time remaining on the session before a flush can be attempted. If active transactions are present the session will not be flushed.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The number of times this entry was hit.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def drop(self) :
		ur"""The number of times action was taken.
		"""
		try :
			return self._drop
		except Exception as e:
			raise e

	@property
	def number(self) :
		ur"""The hash of the matched selectlets.
		"""
		try :
			return self._number
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""The string formed by gathering selectlet values.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@property
	def unit(self) :
		ur"""Total computed hash of the matched selectlets.
		"""
		try :
			return self._unit
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""Used internally to identify ip addresses.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		ur"""Total number of transactions pointing to this entry. Its the sum total of the connection and bandwidth references.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	@property
	def maxbandwidth(self) :
		ur"""The current bandwidth.
		"""
		try :
			return self._maxbandwidth
		except Exception as e:
			raise e

	@property
	def selectoripv61(self) :
		ur"""First IPV6 address gathered.
		"""
		try :
			return self._selectoripv61
		except Exception as e:
			raise e

	@property
	def selectoripv62(self) :
		ur"""Second IPV6 address gathered.
		"""
		try :
			return self._selectoripv62
		except Exception as e:
			raise e

	@property
	def flag(self) :
		ur"""Used internally to identify ipv6 addresses.
		"""
		try :
			return self._flag
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslimitsessions_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslimitsessions
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
	def clear(cls, client, resource) :
		ur""" Use this API to clear nslimitsessions.
		"""
		try :
			if type(resource) is not list :
				clearresource = nslimitsessions()
				clearresource.limitidentifier = resource.limitidentifier
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ nslimitsessions() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].limitidentifier = resource[i].limitidentifier
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nslimitsessions resources that are configured on netscaler.
		"""
		try :
			if type(name) == cls :
				if type(name) is not list :
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						response = [nslimitsessions() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the nslimitsessions resources that are configured on netscaler.
	# This uses nslimitsessions_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nslimitsessions()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_, obj) :
		ur""" Use this API to fetch filtered set of nslimitsessions resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client, obj) :
		ur""" Use this API to count the nslimitsessions resources configured on NetScaler.
		"""
		try :
			option_ = options()
			option_.count = True
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_, obj) :
		ur""" Use this API to count filtered the set of nslimitsessions resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.count = True
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nslimitsessions_response(base_response) :
	def __init__(self, length=1) :
		self.nslimitsessions = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslimitsessions = [nslimitsessions() for _ in range(length)]

