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

class ssldhfile(base_resource) :
	""" Configuration for dh imported file resource. """
	def __init__(self) :
		self._name = ""
		self._src = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name to assign to the imported DH file.  Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my file" or 'my file').<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name to assign to the imported DH file.  Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my file" or 'my file').<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def src(self) :
		ur"""URL specifying the protocol, host, and path, including file name, to the DH file to be imported. For example, http://www.example.com/dh_file.  
		NOTE: The import fails if the file is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._src
		except Exception as e:
			raise e

	@src.setter
	def src(self, src) :
		ur"""URL specifying the protocol, host, and path, including file name, to the DH file to be imported. For example, http://www.example.com/dh_file.  
		NOTE: The import fails if the file is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._src = src
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ssldhfile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssldhfile
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
		ur""" Use this API to Import ssldhfile.
		"""
		try :
			if type(resource) is not list :
				Importresource = ssldhfile()
				Importresource.name = resource.name
				Importresource.src = resource.src
				return Importresource.perform_operation(client,"Import")
			else :
				if (resource and len(resource) > 0) :
					Importresources = [ ssldhfile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						Importresources[i].name = resource[i].name
						Importresources[i].src = resource[i].src
				result = cls.perform_operation_bulk_request(client, Importresources,"Import")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete ssldhfile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ssldhfile()
				deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if (resource and len(resource) > 0) :
					deleteresources = [ ssldhfile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the ssldhfile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ssldhfile()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of ssldhfile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssldhfile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the ssldhfile resources configured on NetScaler.
		"""
		try :
			obj = ssldhfile()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of ssldhfile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssldhfile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class ssldhfile_response(base_response) :
	def __init__(self, length=1) :
		self.ssldhfile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ssldhfile = [ssldhfile() for _ in range(length)]

