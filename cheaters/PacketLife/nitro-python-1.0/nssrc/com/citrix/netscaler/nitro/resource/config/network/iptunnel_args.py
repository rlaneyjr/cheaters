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


class iptunnel_args :
	ur""" Provides additional arguments required for fetching the iptunnel resource.
	"""
	def __init__(self) :
		self._remote = ""
		self._remotesubnetmask = ""

	@property
	def remote(self) :
		ur"""Public IPv4 address, of the remote device, used to set up the tunnel. For this parameter, you can alternatively specify a network address.<br/>Minimum length =  1.
		"""
		try :
			return self._remote
		except Exception as e:
			raise e

	@remote.setter
	def remote(self, remote) :
		ur"""Public IPv4 address, of the remote device, used to set up the tunnel. For this parameter, you can alternatively specify a network address.<br/>Minimum length =  1
		"""
		try :
			self._remote = remote
		except Exception as e:
			raise e

	@property
	def remotesubnetmask(self) :
		ur"""Subnet mask of the remote IP address of the tunnel.
		"""
		try :
			return self._remotesubnetmask
		except Exception as e:
			raise e

	@remotesubnetmask.setter
	def remotesubnetmask(self, remotesubnetmask) :
		ur"""Subnet mask of the remote IP address of the tunnel.
		"""
		try :
			self._remotesubnetmask = remotesubnetmask
		except Exception as e:
			raise e

