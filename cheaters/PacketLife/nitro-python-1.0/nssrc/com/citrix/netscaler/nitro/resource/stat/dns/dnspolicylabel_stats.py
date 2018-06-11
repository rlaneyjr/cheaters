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

class dnspolicylabel_stats(base_resource) :
	ur""" Statistics for dns policy label resource.
	"""
	def __init__(self) :
		self._labelname = ""
		self._clearstats = ""
		self._pipolicylabelhits = 0
		self._pipolicylabelhitsrate = 0

	@property
	def labelname(self) :
		ur"""The name of the dns policy label for which statistics will be displayed.  If not given statistics are shown for all dns policylabels.<br/>Minimum length =  1.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""The name of the dns policy label for which statistics will be displayed.  If not given statistics are shown for all dns policylabels.
		"""
		try :
			self._labelname = labelname
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
	def pipolicylabelhitsrate(self) :
		ur"""Rate (/s) counter for pipolicylabelhits.
		"""
		try :
			return self._pipolicylabelhitsrate
		except Exception as e:
			raise e

	@property
	def pipolicylabelhits(self) :
		ur"""Number of times policy label was invoked. .
		"""
		try :
			return self._pipolicylabelhits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnspolicylabel_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnspolicylabel
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.labelname is not None :
				return str(self.labelname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all dnspolicylabel_stats resources that are configured on netscaler.
		"""
		try :
			obj = dnspolicylabel_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.labelname = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class dnspolicylabel_response(base_response) :
	def __init__(self, length=1) :
		self.dnspolicylabel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnspolicylabel = [dnspolicylabel_stats() for _ in range(length)]

