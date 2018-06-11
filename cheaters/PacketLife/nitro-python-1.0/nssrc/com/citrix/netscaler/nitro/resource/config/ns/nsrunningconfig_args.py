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


class nsrunningconfig_args :
	ur""" Provides additional arguments required for fetching the nsrunningconfig resource.
	"""
	def __init__(self) :
		self._withdefaults = False

	@property
	def withdefaults(self) :
		ur"""Include default values of parameters that have not been explicitly configured. If this argument is disabled, such parameters are not included.
		"""
		try :
			return self._withdefaults
		except Exception as e:
			raise e

	@withdefaults.setter
	def withdefaults(self, withdefaults) :
		ur"""Include default values of parameters that have not been explicitly configured. If this argument is disabled, such parameters are not included.
		"""
		try :
			self._withdefaults = withdefaults
		except Exception as e:
			raise e

