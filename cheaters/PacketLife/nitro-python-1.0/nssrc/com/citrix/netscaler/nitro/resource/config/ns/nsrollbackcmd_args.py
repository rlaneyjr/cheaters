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


class nsrollbackcmd_args :
	ur""" Provides additional arguments required for fetching the nsrollbackcmd resource.
	"""
	def __init__(self) :
		self._filename = ""
		self._outtype = ""

	@property
	def filename(self) :
		ur"""File that contains the commands for which the rollback commands must be generated. Specify the full path of the file name.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		ur"""File that contains the commands for which the rollback commands must be generated. Specify the full path of the file name.
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def outtype(self) :
		ur"""Format in which the rollback commands must be generated.<br/>Possible values = cli, xml.
		"""
		try :
			return self._outtype
		except Exception as e:
			raise e

	@outtype.setter
	def outtype(self, outtype) :
		ur"""Format in which the rollback commands must be generated.<br/>Possible values = cli, xml
		"""
		try :
			self._outtype = outtype
		except Exception as e:
			raise e

	class Outtype:
		cli = "cli"
		xml = "xml"

