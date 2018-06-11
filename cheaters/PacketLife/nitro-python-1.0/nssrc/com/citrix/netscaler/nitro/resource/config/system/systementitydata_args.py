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


class systementitydata_args :
	ur""" Provides additional arguments required for fetching the systementitydata resource.
	"""
	def __init__(self) :
		self._type = ""
		self._name = ""
		self._counters = ""
		self._starttime = ""
		self._endtime = ""
		self._last = 0
		self._unit = ""
		self._datasource = ""
		self._core = 0

	@property
	def type(self) :
		ur"""Specify the entity type.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Specify the entity type.
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Specify the entity name.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Specify the entity name.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def counters(self) :
		ur"""Specify the counters to be collected.
		"""
		try :
			return self._counters
		except Exception as e:
			raise e

	@counters.setter
	def counters(self, counters) :
		ur"""Specify the counters to be collected.
		"""
		try :
			self._counters = counters
		except Exception as e:
			raise e

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
	def core(self) :
		ur"""Specify core ID of the PE in nCore.
		"""
		try :
			return self._core
		except Exception as e:
			raise e

	@core.setter
	def core(self, core) :
		ur"""Specify core ID of the PE in nCore.
		"""
		try :
			self._core = core
		except Exception as e:
			raise e

	class Unit:
		HOURS = "HOURS"
		DAYS = "DAYS"
		MONTHS = "MONTHS"

