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


class auditmessages_args :
	ur""" Provides additional arguments required for fetching the auditmessages resource.
	"""
	def __init__(self) :
		self._loglevel = []
		self._numofmesgs = 0

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
		ur"""Number of log messages to be displayed.<br/>Default value: 20<br/>Minimum value =  1<br/>Maximum value =  256.
		"""
		try :
			return self._numofmesgs
		except Exception as e:
			raise e

	@numofmesgs.setter
	def numofmesgs(self, numofmesgs) :
		ur"""Number of log messages to be displayed.<br/>Default value: 20<br/>Minimum value =  1<br/>Maximum value =  256
		"""
		try :
			self._numofmesgs = numofmesgs
		except Exception as e:
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

