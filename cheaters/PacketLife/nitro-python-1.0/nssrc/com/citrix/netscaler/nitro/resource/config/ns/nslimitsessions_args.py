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


class nslimitsessions_args :
	ur""" Provides additional arguments required for fetching the nslimitsessions resource.
	"""
	def __init__(self) :
		self._limitidentifier = ""
		self._detail = False

	@property
	def limitidentifier(self) :
		ur"""Name of the rate limit identifier for which to display the sessions.<br/>Minimum length =  1.
		"""
		try :
			return self._limitidentifier
		except Exception as e:
			raise e

	@limitidentifier.setter
	def limitidentifier(self, limitidentifier) :
		ur"""Name of the rate limit identifier for which to display the sessions.<br/>Minimum length =  1
		"""
		try :
			self._limitidentifier = limitidentifier
		except Exception as e:
			raise e

	@property
	def detail(self) :
		ur"""Show the individual hash values.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		ur"""Show the individual hash values.
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

