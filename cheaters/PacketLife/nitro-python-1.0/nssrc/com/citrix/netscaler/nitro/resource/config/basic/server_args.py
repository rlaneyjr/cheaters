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


class server_args :
	ur""" Provides additional arguments required for fetching the server resource.
	"""
	def __init__(self) :
		self._Internal = False

	@property
	def Internal(self) :
		ur"""Display names of the servers that have been created for internal use.
		"""
		try :
			return self._Internal
		except Exception as e:
			raise e

	@Internal.setter
	def Internal(self, Internal) :
		ur"""Display names of the servers that have been created for internal use.
		"""
		try :
			self._Internal = Internal
		except Exception as e:
			raise e

