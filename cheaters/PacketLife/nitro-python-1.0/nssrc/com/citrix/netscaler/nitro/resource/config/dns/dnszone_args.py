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


class dnszone_args :
	ur""" Provides additional arguments required for fetching the dnszone resource.
	"""
	def __init__(self) :
		self._type = ""

	@property
	def type(self) :
		ur"""Type of zone to display. Mutually exclusive with the DNS Zone (zoneName) parameter. Available settings function as follows:
		* ADNS - Display all the zones for which the NetScaler appliance is authoritative.
		* PROXY - Display all the zones for which the NetScaler appliance is functioning as a proxy server.
		* ALL - Display all the zones configured on the appliance.<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of zone to display. Mutually exclusive with the DNS Zone (zoneName) parameter. Available settings function as follows:
		* ADNS - Display all the zones for which the NetScaler appliance is authoritative.
		* PROXY - Display all the zones for which the NetScaler appliance is functioning as a proxy server.
		* ALL - Display all the zones configured on the appliance.<br/>Possible values = ALL, ADNS, PROXY
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	class Type:
		ALL = "ALL"
		ADNS = "ADNS"
		PROXY = "PROXY"

