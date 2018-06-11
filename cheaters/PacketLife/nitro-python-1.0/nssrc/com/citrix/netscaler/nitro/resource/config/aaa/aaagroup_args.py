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


class aaagroup_args :
	ur""" Provides additional arguments required for fetching the aaagroup resource.
	"""
	def __init__(self) :
		self._loggedin = False

	@property
	def loggedin(self) :
		ur"""Display only the group members who are currently logged in.
		"""
		try :
			return self._loggedin
		except Exception as e:
			raise e

	@loggedin.setter
	def loggedin(self, loggedin) :
		ur"""Display only the group members who are currently logged in.
		"""
		try :
			self._loggedin = loggedin
		except Exception as e:
			raise e

