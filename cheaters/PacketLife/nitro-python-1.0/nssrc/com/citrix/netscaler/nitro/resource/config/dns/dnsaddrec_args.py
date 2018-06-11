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


class dnsaddrec_args :
	ur""" Provides additional arguments required for fetching the dnsaddrec resource.
	"""
	def __init__(self) :
		self._type = ""

	@property
	def type(self) :
		ur"""The address record type. The type can take 3 values:
		ADNS -  If this is specified, all of the authoritative address records will be displayed.
		PROXY - If this is specified, all of the proxy address records will be displayed.
		ALL  -  If this is specified, all of the address records will be displayed.<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""The address record type. The type can take 3 values:
		ADNS -  If this is specified, all of the authoritative address records will be displayed.
		PROXY - If this is specified, all of the proxy address records will be displayed.
		ALL  -  If this is specified, all of the address records will be displayed.<br/>Possible values = ALL, ADNS, PROXY
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	class Type:
		ALL = "ALL"
		ADNS = "ADNS"
		PROXY = "PROXY"

