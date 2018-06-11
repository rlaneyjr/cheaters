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

class application(base_resource) :
	""" Configuration for application resource. """
	def __init__(self) :
		self._apptemplatefilename = ""
		self._appname = ""
		self._deploymentfilename = ""

	@property
	def apptemplatefilename(self) :
		ur"""Name of the AppExpert application template file.
		"""
		try :
			return self._apptemplatefilename
		except Exception as e:
			raise e

	@apptemplatefilename.setter
	def apptemplatefilename(self, apptemplatefilename) :
		ur"""Name of the AppExpert application template file.
		"""
		try :
			self._apptemplatefilename = apptemplatefilename
		except Exception as e:
			raise e

	@property
	def appname(self) :
		ur"""Name to assign to the application on the NetScaler appliance. If you do not provide a name, the appliance assigns the application the name of the template file.
		"""
		try :
			return self._appname
		except Exception as e:
			raise e

	@appname.setter
	def appname(self, appname) :
		ur"""Name to assign to the application on the NetScaler appliance. If you do not provide a name, the appliance assigns the application the name of the template file.
		"""
		try :
			self._appname = appname
		except Exception as e:
			raise e

	@property
	def deploymentfilename(self) :
		ur"""Name of the deployment file.
		"""
		try :
			return self._deploymentfilename
		except Exception as e:
			raise e

	@deploymentfilename.setter
	def deploymentfilename(self, deploymentfilename) :
		ur"""Name of the deployment file.
		"""
		try :
			self._deploymentfilename = deploymentfilename
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(application_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.application
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def Import(cls, client, resource) :
		ur""" Use this API to Import application.
		"""
		try :
			if type(resource) is not list :
				Importresource = application()
				Importresource.apptemplatefilename = resource.apptemplatefilename
				Importresource.appname = resource.appname
				Importresource.deploymentfilename = resource.deploymentfilename
				return Importresource.perform_operation(client,"Import")
		except Exception as e :
			raise e

	@classmethod
	def export(cls, client, resource) :
		ur""" Use this API to export application.
		"""
		try :
			if type(resource) is not list :
				exportresource = application()
				exportresource.appname = resource.appname
				exportresource.apptemplatefilename = resource.apptemplatefilename
				exportresource.deploymentfilename = resource.deploymentfilename
				return exportresource.perform_operation(client,"export")
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete application.
		"""
		try :
			if type(resource) is not list :
				deleteresource = application()
				deleteresource.appname = resource.appname
				return deleteresource.delete_resource(client)
		except Exception as e :
			raise e

class application_response(base_response) :
	def __init__(self, length=1) :
		self.application = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.application = [application() for _ in range(length)]

