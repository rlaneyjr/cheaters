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


class techsupport_args :
	ur""" Provides additional arguments required for fetching the techsupport resource.
	"""
	def __init__(self) :
		self._scope = ""

	@property
	def scope(self) :
		ur"""Use this option to run showtechsupport on present node or all cluster nodes.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER.
		"""
		try :
			return self._scope
		except Exception as e:
			raise e

	@scope.setter
	def scope(self, scope) :
		ur"""Use this option to run showtechsupport on present node or all cluster nodes.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER
		"""
		try :
			self._scope = scope
		except Exception as e:
			raise e

	class Scope:
		NODE = "NODE"
		CLUSTER = "CLUSTER"

