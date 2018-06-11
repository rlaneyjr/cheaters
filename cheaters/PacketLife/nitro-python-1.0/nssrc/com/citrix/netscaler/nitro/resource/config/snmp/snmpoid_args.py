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


class snmpoid_args :
	ur""" Provides additional arguments required for fetching the snmpoid resource.
	"""
	def __init__(self) :
		self._entitytype = ""

	@property
	def entitytype(self) :
		ur"""The type of entity whose SNMP OIDs you want to displayType of entity whose SNMP OIDs you want the NetScaler appliance to display.<br/>Possible values = VSERVER, SERVICE, SERVICEGROUP.
		"""
		try :
			return self._entitytype
		except Exception as e:
			raise e

	@entitytype.setter
	def entitytype(self, entitytype) :
		ur"""The type of entity whose SNMP OIDs you want to displayType of entity whose SNMP OIDs you want the NetScaler appliance to display.<br/>Possible values = VSERVER, SERVICE, SERVICEGROUP
		"""
		try :
			self._entitytype = entitytype
		except Exception as e:
			raise e

	class Entitytype:
		VSERVER = "VSERVER"
		SERVICE = "SERVICE"
		SERVICEGROUP = "SERVICEGROUP"

