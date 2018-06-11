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


class aaasession_args :
	ur""" Provides additional arguments required for fetching the aaasession resource.
	"""
	def __init__(self) :
		self._username = ""
		self._groupname = ""
		self._iip = ""
		self._netmask = ""

	@property
	def username(self) :
		ur"""Name of the AAA user.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Name of the AAA user.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		ur"""Name of the AAA group.<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name of the AAA group.<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def iip(self) :
		ur"""IP address or the first address in the intranet IP range.<br/>Minimum length =  1.
		"""
		try :
			return self._iip
		except Exception as e:
			raise e

	@iip.setter
	def iip(self, iip) :
		ur"""IP address or the first address in the intranet IP range.<br/>Minimum length =  1
		"""
		try :
			self._iip = iip
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""Subnet mask for the intranet IP range.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""Subnet mask for the intranet IP range.<br/>Minimum length =  1
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

