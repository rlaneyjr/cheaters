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

class auditmessages(base_resource) :
	""" Configuration for audit message resource. """
	def __init__(self) :
		self._loglevel = []
		self._numofmesgs = 0
		self._value = ""
		self.___count = 0

	@property
	def loglevel(self) :
		ur"""Audit log level filter, which specifies the types of events to display. 
		The following loglevels are valid:
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG.
		"""
		try :
			return self._loglevel
		except Exception as e:
			raise e

	@loglevel.setter
	def loglevel(self, loglevel) :
		ur"""Audit log level filter, which specifies the types of events to display. 
		The following loglevels are valid:
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG
		"""
		try :
			self._loglevel = loglevel
		except Exception as e:
			raise e

	@property
	def numofmesgs(self) :
		ur"""Number of log messages to be displayed.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  256.
		"""
		try :
			return self._numofmesgs
		except Exception as e:
			raise e

	@numofmesgs.setter
	def numofmesgs(self, numofmesgs) :
		ur"""Number of log messages to be displayed.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  256
		"""
		try :
			self._numofmesgs = numofmesgs
		except Exception as e:
			raise e

	@property
	def value(self) :
		ur"""The Audit message.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(auditmessages_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.auditmessages
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
		ur""" Use this API to fetch all the auditmessages resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = auditmessages()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the auditmessages resources that are configured on netscaler.
	# This uses auditmessages_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = auditmessages()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of auditmessages resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditmessages()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the auditmessages resources configured on NetScaler.
		"""
		try :
			obj = auditmessages()
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
		ur""" Use this API to count filtered the set of auditmessages resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditmessages()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Loglevel:
		ALL = "ALL"
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"

class auditmessages_response(base_response) :
	def __init__(self, length=1) :
		self.auditmessages = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.auditmessages = [auditmessages() for _ in range(length)]

