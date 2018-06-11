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


class systementity_args :
	ur""" Provides additional arguments required for fetching the systementity resource.
	"""
	def __init__(self) :
		self._type = ""
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

