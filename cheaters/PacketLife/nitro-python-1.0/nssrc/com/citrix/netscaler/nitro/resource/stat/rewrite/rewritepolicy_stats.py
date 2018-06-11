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

class rewritepolicy_stats(base_resource) :
	ur""" Statistics for rewrite policy resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._pipolicyhits = 0
		self._pipolicyhitsrate = 0
		self._pipolicyundefhits = 0
		self._pipolicyundefhitsrate = 0

	@property
	def name(self) :
		ur"""Name of the rewrite policy.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the rewrite policy.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		ur"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		ur"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def pipolicyhitsrate(self) :
		ur"""Rate (/s) counter for pipolicyhits.
		"""
		try :
			return self._pipolicyhitsrate
		except Exception as e:
			raise e

	@property
	def pipolicyundefhitsrate(self) :
		ur"""Rate (/s) counter for pipolicyundefhits.
		"""
		try :
			return self._pipolicyundefhitsrate
		except Exception as e:
			raise e

	@property
	def pipolicyhits(self) :
		ur"""Number of hits on the policy.
		"""
		try :
			return self._pipolicyhits
		except Exception as e:
			raise e

	@property
	def pipolicyundefhits(self) :
		ur"""Number of undef hits on the policy.
		"""
		try :
			return self._pipolicyundefhits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rewritepolicy_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rewritepolicy
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all rewritepolicy_stats resources that are configured on netscaler.
		"""
		try :
			obj = rewritepolicy_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class rewritepolicy_response(base_response) :
	def __init__(self, length=1) :
		self.rewritepolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rewritepolicy = [rewritepolicy_stats() for _ in range(length)]

