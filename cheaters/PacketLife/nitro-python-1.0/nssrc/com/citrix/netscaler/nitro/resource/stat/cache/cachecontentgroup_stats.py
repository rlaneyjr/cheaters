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

class cachecontentgroup_stats(base_resource) :
	ur""" Statistics for Integrated Cache content group resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._groupnon304hit = 0
		self._group304hit = 0
		self._totcell = 0
		self._totmarkercell = 0
		self._timesflushed = 0
		self._totmemory = 0
		self._maxmemory = 0

	@property
	def name(self) :
		ur"""Name of the cache contentgroup for which to display statistics. If you do not set this parameter, statistics are shown for all cache contentgroups.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the cache contentgroup for which to display statistics. If you do not set this parameter, statistics are shown for all cache contentgroups.
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
	def group304hit(self) :
		ur"""304 hits for ContentGroup.
		"""
		try :
			return self._group304hit
		except Exception as e:
			raise e

	@property
	def totmarkercell(self) :
		ur"""Number of marker objects in contentgroup.
		"""
		try :
			return self._totmarkercell
		except Exception as e:
			raise e

	@property
	def timesflushed(self) :
		ur"""Number of times contentgroup is flushed.
		"""
		try :
			return self._timesflushed
		except Exception as e:
			raise e

	@property
	def totmemory(self) :
		ur"""current memory usage.
		"""
		try :
			return self._totmemory
		except Exception as e:
			raise e

	@property
	def totcell(self) :
		ur"""Number of objects in contentgroup.
		"""
		try :
			return self._totcell
		except Exception as e:
			raise e

	@property
	def groupnon304hit(self) :
		ur"""Non304 hits for ContentGroup.
		"""
		try :
			return self._groupnon304hit
		except Exception as e:
			raise e

	@property
	def maxmemory(self) :
		ur"""maximum memory usage limit.
		"""
		try :
			return self._maxmemory
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cachecontentgroup_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cachecontentgroup
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
		ur""" Use this API to fetch the statistics of all cachecontentgroup_stats resources that are configured on netscaler.
		"""
		try :
			obj = cachecontentgroup_stats()
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

class cachecontentgroup_response(base_response) :
	def __init__(self, length=1) :
		self.cachecontentgroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cachecontentgroup = [cachecontentgroup_stats() for _ in range(length)]

