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

class pqbinding(base_resource) :
	""" Configuration for PQ bindings resource. """
	def __init__(self) :
		self._vservername = ""
		self._policyname = ""
		self._rule = ""
		self._priority = 0
		self._weight = 0
		self._qdepth = 0
		self._polqdepth = 0
		self._hits = 0
		self.___count = 0

	@property
	def vservername(self) :
		ur"""Name of the load balancing virtual server for which to display the priority queuing policy.<br/>Minimum length =  1.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		ur"""Name of the load balancing virtual server for which to display the priority queuing policy.<br/>Minimum length =  1
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""The name of the priority queuing policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""The condition for applying the policy.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""The priority of queuing the request.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Weight.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@property
	def qdepth(self) :
		ur"""Queue Depth.
		"""
		try :
			return self._qdepth
		except Exception as e:
			raise e

	@property
	def polqdepth(self) :
		ur"""Policy Queue Depth.
		"""
		try :
			return self._polqdepth
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Total number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(pqbinding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pqbinding
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
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the pqbinding resources that are configured on netscaler.
		"""
		try :
			if type(name) == cls :
				if type(name) is not list :
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						response = [pqbinding() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the pqbinding resources that are configured on netscaler.
	# This uses pqbinding_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = pqbinding()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_, obj) :
		ur""" Use this API to fetch filtered set of pqbinding resources.
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
		ur""" Use this API to count the pqbinding resources configured on NetScaler.
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
		ur""" Use this API to count filtered the set of pqbinding resources.
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


class pqbinding_response(base_response) :
	def __init__(self, length=1) :
		self.pqbinding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.pqbinding = [pqbinding() for _ in range(length)]

