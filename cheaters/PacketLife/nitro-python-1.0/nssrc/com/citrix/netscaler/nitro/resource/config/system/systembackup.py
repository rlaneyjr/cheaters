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

class systembackup(base_resource) :
	""" Configuration for Backup Data for ns backup and restore resource. """
	def __init__(self) :
		self._filename = ""
		self._level = ""
		self._comment = ""
		self._size = 0
		self._creationtime = ""
		self._version = ""
		self._createdby = ""
		self._ipaddress = ""
		self.___count = 0

	@property
	def filename(self) :
		ur"""Name of the backup file(*.tgz) to be restored.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		ur"""Name of the backup file(*.tgz) to be restored.
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def level(self) :
		ur"""Level of data to be backed up.<br/>Default value: basic<br/>Possible values = basic, full.
		"""
		try :
			return self._level
		except Exception as e:
			raise e

	@level.setter
	def level(self, level) :
		ur"""Level of data to be backed up.<br/>Default value: basic<br/>Possible values = basic, full
		"""
		try :
			self._level = level
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Comment specified at the time of creation of the backup file(*.tgz).
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Comment specified at the time of creation of the backup file(*.tgz).
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def size(self) :
		ur"""Size of the backup file(*.tgz) in KB.
		"""
		try :
			return self._size
		except Exception as e:
			raise e

	@property
	def creationtime(self) :
		ur"""Creation time of the backup file(*.tgz).
		"""
		try :
			return self._creationtime
		except Exception as e:
			raise e

	@property
	def version(self) :
		ur"""Build version of the backup file(*.tgz).
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@property
	def createdby(self) :
		ur"""Name of user who created the backup file(*.tgz).
		"""
		try :
			return self._createdby
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""Ip of Netscaler box where the backup file(*.tgz) was created.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systembackup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systembackup
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
	def create(cls, client, resource) :
		ur""" Use this API to create systembackup.
		"""
		try :
			if type(resource) is not list :
				createresource = systembackup()
				createresource.filename = resource.filename
				createresource.level = resource.level
				createresource.comment = resource.comment
				return createresource.perform_operation(client,"create")
			else :
				if (resource and len(resource) > 0) :
					createresources = [ systembackup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						createresources[i].filename = resource[i].filename
						createresources[i].level = resource[i].level
						createresources[i].comment = resource[i].comment
				result = cls.perform_operation_bulk_request(client, createresources,"create")
			return result
		except Exception as e :
			raise e

	@classmethod
	def restore(cls, client, resource) :
		ur""" Use this API to restore systembackup.
		"""
		try :
			if type(resource) is not list :
				restoreresource = systembackup()
				restoreresource.filename = resource.filename
				return restoreresource.perform_operation(client,"restore")
			else :
				if (resource and len(resource) > 0) :
					restoreresources = [ systembackup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						restoreresources[i].filename = resource[i].filename
				result = cls.perform_operation_bulk_request(client, restoreresources,"restore")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete systembackup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = systembackup()
				if type(resource) !=  type(deleteresource):
					deleteresource.filename = resource
				else :
					deleteresource.filename = resource.filename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ systembackup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].filename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ systembackup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].filename = resource[i].filename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systembackup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systembackup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = systembackup()
						obj.filename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [systembackup() for _ in range(len(name))]
							obj = [systembackup() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = systembackup()
								obj[i].filename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of systembackup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systembackup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the systembackup resources configured on NetScaler.
		"""
		try :
			obj = systembackup()
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
		ur""" Use this API to count filtered the set of systembackup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systembackup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Level:
		basic = "basic"
		full = "full"

class systembackup_response(base_response) :
	def __init__(self, length=1) :
		self.systembackup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systembackup = [systembackup() for _ in range(length)]

