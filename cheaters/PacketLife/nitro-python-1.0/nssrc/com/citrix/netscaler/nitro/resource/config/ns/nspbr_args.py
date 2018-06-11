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


class nspbr_args :
	ur""" Provides additional arguments required for fetching the nspbr resource.
	"""
	def __init__(self) :
		self._detail = False

	@property
	def detail(self) :
		ur"""To get a detailed view.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		ur"""To get a detailed view.
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

