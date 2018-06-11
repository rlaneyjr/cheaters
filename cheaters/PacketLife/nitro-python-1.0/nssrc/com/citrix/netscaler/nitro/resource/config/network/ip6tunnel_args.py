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


class ip6tunnel_args :
	ur""" Provides additional arguments required for fetching the ip6tunnel resource.
	"""
	def __init__(self) :
		self._remote = ""

	@property
	def remote(self) :
		ur"""The IPv6 address at which the remote NetScaler appliance connects to the tunnel.<br/>Minimum length =  1.
		"""
		try :
			return self._remote
		except Exception as e:
			raise e

	@remote.setter
	def remote(self, remote) :
		ur"""The IPv6 address at which the remote NetScaler appliance connects to the tunnel.<br/>Minimum length =  1
		"""
		try :
			self._remote = remote
		except Exception as e:
			raise e

