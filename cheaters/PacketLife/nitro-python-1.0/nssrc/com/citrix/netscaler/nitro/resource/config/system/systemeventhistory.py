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

class systemeventhistory(base_resource) :
	""" Configuration for event history resource. """
	def __init__(self) :
		self._starttime = ""
		self._endtime = ""
		self._last = 0
		self._unit = ""
		self._datasource = ""
		self._response = ""

	@property
	def starttime(self) :
		ur"""Specify start time in mmddyyyyhhmm to start collecting values from that timestamp.
		"""
		try :
			return self._starttime
		except Exception as e:
			raise e

	@starttime.setter
	def starttime(self, starttime) :
		ur"""Specify start time in mmddyyyyhhmm to start collecting values from that timestamp.
		"""
		try :
			self._starttime = starttime
		except Exception as e:
			raise e

	@property
	def endtime(self) :
		ur"""Specify end time in mmddyyyyhhmm upto which values have to be collected.
		"""
		try :
			return self._endtime
		except Exception as e:
			raise e

	@endtime.setter
	def endtime(self, endtime) :
		ur"""Specify end time in mmddyyyyhhmm upto which values have to be collected.
		"""
		try :
			self._endtime = endtime
		except Exception as e:
			raise e

	@property
	def last(self) :
		ur"""Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1.
		"""
		try :
			return self._last
		except Exception as e:
			raise e

	@last.setter
	def last(self, last) :
		ur"""Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1
		"""
		try :
			self._last = last
		except Exception as e:
			raise e

	@property
	def unit(self) :
		ur"""Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS.
		"""
		try :
			return self._unit
		except Exception as e:
			raise e

	@unit.setter
	def unit(self, unit) :
		ur"""Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS
		"""
		try :
			self._unit = unit
		except Exception as e:
			raise e

	@property
	def datasource(self) :
		ur"""Specifies the source which contains all the stored counter values.
		"""
		try :
			return self._datasource
		except Exception as e:
			raise e

	@datasource.setter
	def datasource(self, datasource) :
		ur"""Specifies the source which contains all the stored counter values.
		"""
		try :
			self._datasource = datasource
		except Exception as e:
			raise e

	@property
	def response(self) :
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemeventhistory_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemeventhistory
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
		ur""" Use this API to fetch all the systemeventhistory resources that are configured on netscaler.
		"""
		try :
			if type(name) == cls :
				if type(name) is not list :
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the systemeventhistory resources that are configured on netscaler.
	# This uses systemeventhistory_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = systemeventhistory()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Unit:
		HOURS = "HOURS"
		DAYS = "DAYS"
		MONTHS = "MONTHS"

class systemeventhistory_response(base_response) :
	def __init__(self, length=1) :
		self.systemeventhistory = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemeventhistory = [systemeventhistory() for _ in range(length)]

