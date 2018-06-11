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

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class appfwcustomsettings(base_resource) :
	""" Configuration for application firewall custom settings XML configuration resource. """
	def __init__(self) :
		self._name = ""
		self._target = ""

	@property
	def name(self) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def target(self) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._target
		except Exception as e:
			raise e

	@target.setter
	def target(self, target) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._target = target
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwcustomsettings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwcustomsettings
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def export(cls, client, resource) :
		ur""" Use this API to export appfwcustomsettings.
		"""
		try :
			if type(resource) is not list :
				exportresource = appfwcustomsettings()
				exportresource.name = resource.name
				exportresource.target = resource.target
				return exportresource.perform_operation(client,"export")
		except Exception as e :
			raise e

class appfwcustomsettings_response(base_response) :
	def __init__(self, length=1) :
		self.appfwcustomsettings = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwcustomsettings = [appfwcustomsettings() for _ in range(length)]

