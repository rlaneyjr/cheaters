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

class aaapreauthenticationaction(base_resource) :
	""" Configuration for pre authentication action resource. """
	def __init__(self) :
		self._name = ""
		self._preauthenticationaction = ""
		self._killprocess = ""
		self._deletefiles = ""
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the preauthentication action. Must begin with a letter, number, or the underscore character (_), and must consist only of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after preauthentication action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my aaa action" or 'my aaa action).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the preauthentication action. Must begin with a letter, number, or the underscore character (_), and must consist only of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after preauthentication action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my aaa action" or 'my aaa action).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def preauthenticationaction(self) :
		ur"""Allow or deny logon after endpoint analysis (EPA) results.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._preauthenticationaction
		except Exception as e:
			raise e

	@preauthenticationaction.setter
	def preauthenticationaction(self, preauthenticationaction) :
		ur"""Allow or deny logon after endpoint analysis (EPA) results.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._preauthenticationaction = preauthenticationaction
		except Exception as e:
			raise e

	@property
	def killprocess(self) :
		ur"""String specifying the name of a process to be terminated by the endpoint analysis (EPA) tool.
		"""
		try :
			return self._killprocess
		except Exception as e:
			raise e

	@killprocess.setter
	def killprocess(self, killprocess) :
		ur"""String specifying the name of a process to be terminated by the endpoint analysis (EPA) tool.
		"""
		try :
			self._killprocess = killprocess
		except Exception as e:
			raise e

	@property
	def deletefiles(self) :
		ur"""String specifying the path(s) and name(s) of the files to be deleted by the endpoint analysis (EPA) tool.
		"""
		try :
			return self._deletefiles
		except Exception as e:
			raise e

	@deletefiles.setter
	def deletefiles(self, deletefiles) :
		ur"""String specifying the path(s) and name(s) of the files to be deleted by the endpoint analysis (EPA) tool.
		"""
		try :
			self._deletefiles = deletefiles
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaapreauthenticationaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaapreauthenticationaction
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
	def add(cls, client, resource) :
		ur""" Use this API to add aaapreauthenticationaction.
		"""
		try :
			if type(resource) is not list :
				addresource = aaapreauthenticationaction()
				addresource.name = resource.name
				addresource.preauthenticationaction = resource.preauthenticationaction
				addresource.killprocess = resource.killprocess
				addresource.deletefiles = resource.deletefiles
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ aaapreauthenticationaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].preauthenticationaction = resource[i].preauthenticationaction
						addresources[i].killprocess = resource[i].killprocess
						addresources[i].deletefiles = resource[i].deletefiles
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete aaapreauthenticationaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = aaapreauthenticationaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaapreauthenticationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaapreauthenticationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update aaapreauthenticationaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaapreauthenticationaction()
				updateresource.name = resource.name
				updateresource.preauthenticationaction = resource.preauthenticationaction
				updateresource.killprocess = resource.killprocess
				updateresource.deletefiles = resource.deletefiles
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ aaapreauthenticationaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].preauthenticationaction = resource[i].preauthenticationaction
						updateresources[i].killprocess = resource[i].killprocess
						updateresources[i].deletefiles = resource[i].deletefiles
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of aaapreauthenticationaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaapreauthenticationaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ aaapreauthenticationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ aaapreauthenticationaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the aaapreauthenticationaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaapreauthenticationaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = aaapreauthenticationaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [aaapreauthenticationaction() for _ in range(len(name))]
							obj = [aaapreauthenticationaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = aaapreauthenticationaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of aaapreauthenticationaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaapreauthenticationaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the aaapreauthenticationaction resources configured on NetScaler.
		"""
		try :
			obj = aaapreauthenticationaction()
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
		ur""" Use this API to count filtered the set of aaapreauthenticationaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaapreauthenticationaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

	class Preauthenticationaction:
		ALLOW = "ALLOW"
		DENY = "DENY"

class aaapreauthenticationaction_response(base_response) :
	def __init__(self, length=1) :
		self.aaapreauthenticationaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaapreauthenticationaction = [aaapreauthenticationaction() for _ in range(length)]

