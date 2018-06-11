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

class nslimitidentifier_stats(base_resource) :
	ur""" Statistics for limit Indetifier resource.
	"""
	def __init__(self) :
		self._name = ""
		self._pattern = []
		self._clearstats = ""
		self._sortby = ""
		self._sortorder = ""
		self._ratelmtobjhits = 0
		self._ratelmtobjdrops = 0
		self._ratelmtsessionobjhits = 0

	@property
	def name(self) :
		ur"""The name of the identifier.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of the identifier.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def pattern(self) :
		ur"""Pattern for the selector field, ? means field is required, * means field value does not matter, anything else is a regular pattern.
		"""
		try :
			return self._pattern
		except Exception as e:
			raise e

	@pattern.setter
	def pattern(self, pattern) :
		ur"""Pattern for the selector field, ? means field is required, * means field value does not matter, anything else is a regular pattern
		"""
		try :
			self._pattern = pattern
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
	def sortby(self) :
		ur"""use this argument to sort by specific key.<br/>Possible values = .
		"""
		try :
			return self._sortby
		except Exception as e:
			raise e

	@sortby.setter
	def sortby(self, sortby) :
		ur"""use this argument to sort by specific key
		"""
		try :
			self._sortby = sortby
		except Exception as e:
			raise e

	@property
	def sortorder(self) :
		ur"""use this argument to specify sort order.<br/>Default value: SORT_DESCENDING<br/>Possible values = ascending, descending.
		"""
		try :
			return self._sortorder
		except Exception as e:
			raise e

	@sortorder.setter
	def sortorder(self, sortorder) :
		ur"""use this argument to specify sort order
		"""
		try :
			self._sortorder = sortorder
		except Exception as e:
			raise e

	@property
	def ratelmtobjhits(self) :
		ur"""Total hits.
		"""
		try :
			return self._ratelmtobjhits
		except Exception as e:
			raise e

	@property
	def ratelmtsessionobjhits(self) :
		ur"""Total hits.
		"""
		try :
			return self._ratelmtsessionobjhits
		except Exception as e:
			raise e

	@property
	def ratelmtobjdrops(self) :
		ur"""Total drops.
		"""
		try :
			return self._ratelmtobjdrops
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslimitidentifier_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslimitidentifier
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
		ur""" Use this API to fetch the statistics of all nslimitidentifier_stats resources that are configured on netscaler.
		"""
		try :
			obj = nslimitidentifier_stats()
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

	class Sortorder:
		ascending = "ascending"
		descending = "descending"

class nslimitidentifier_response(base_response) :
	def __init__(self, length=1) :
		self.nslimitidentifier = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslimitidentifier = [nslimitidentifier_stats() for _ in range(length)]

