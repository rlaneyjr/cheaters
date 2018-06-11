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

class systemfile(base_resource) :
	""" Configuration for file resource. """
	def __init__(self) :
		self._filename = ""
		self._filecontent = ""
		self._filelocation = ""
		self._fileencoding = ""
		self._fileaccesstime = ""
		self._filemodifiedtime = ""
		self._filemode = []
		self.___count = 0

	@property
	def filename(self) :
		ur"""Name of the file. It should not include filepath.<br/>Maximum length =  63.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		ur"""Name of the file. It should not include filepath.<br/>Maximum length =  63
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def filecontent(self) :
		ur"""file content in Base64 format.
		"""
		try :
			return self._filecontent
		except Exception as e:
			raise e

	@filecontent.setter
	def filecontent(self, filecontent) :
		ur"""file content in Base64 format.
		"""
		try :
			self._filecontent = filecontent
		except Exception as e:
			raise e

	@property
	def filelocation(self) :
		ur"""location of the file on NetScaler.<br/>Maximum length =  127.
		"""
		try :
			return self._filelocation
		except Exception as e:
			raise e

	@filelocation.setter
	def filelocation(self, filelocation) :
		ur"""location of the file on NetScaler.<br/>Maximum length =  127
		"""
		try :
			self._filelocation = filelocation
		except Exception as e:
			raise e

	@property
	def fileencoding(self) :
		ur"""encoding type of the file content.<br/>Default value: "BASE64".
		"""
		try :
			return self._fileencoding
		except Exception as e:
			raise e

	@fileencoding.setter
	def fileencoding(self, fileencoding) :
		ur"""encoding type of the file content.<br/>Default value: "BASE64"
		"""
		try :
			self._fileencoding = fileencoding
		except Exception as e:
			raise e

	@property
	def fileaccesstime(self) :
		ur"""Last access time of the file.
		"""
		try :
			return self._fileaccesstime
		except Exception as e:
			raise e

	@property
	def filemodifiedtime(self) :
		ur"""last modified time of the file.
		"""
		try :
			return self._filemodifiedtime
		except Exception as e:
			raise e

	@property
	def filemode(self) :
		ur"""file mode.<br/>Possible values = DIRECTORY.
		"""
		try :
			return self._filemode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemfile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemfile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.filename is not None :
				return str(self.filename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add systemfile.
		"""
		try :
			if type(resource) is not list :
				addresource = systemfile()
				addresource.filename = resource.filename
				addresource.filecontent = resource.filecontent
				addresource.filelocation = resource.filelocation
				addresource.fileencoding = resource.fileencoding
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ systemfile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].filename = resource[i].filename
						addresources[i].filecontent = resource[i].filecontent
						addresources[i].filelocation = resource[i].filelocation
						addresources[i].fileencoding = resource[i].fileencoding
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete systemfile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = systemfile()
				if type(resource) !=  type(deleteresource):
					deleteresource.filename = resource
				else :
					deleteresource.filename = resource.filename
					deleteresource.filelocation = resource.filelocation
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemfile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].filename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemfile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].filename = resource[i].filename
							deleteresources[i].filelocation = resource[i].filelocation
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systemfile resources that are configured on netscaler.
		"""
		try :
			if type(name) == cls :
				if type(name) is not list :
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						response = [systemfile() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the systemfile resources that are configured on netscaler.
	# This uses systemfile_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = systemfile()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Filemode:
		DIRECTORY = "DIRECTORY"

class systemfile_response(base_response) :
	def __init__(self, length=1) :
		self.systemfile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemfile = [systemfile() for _ in range(length)]

