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

class systemcmdpolicy(base_resource) :
	""" Configuration for command policy resource. """
	def __init__(self) :
		self._policyname = ""
		self._action = ""
		self._cmdspec = ""
		self._builtin = []
		self.___count = 0

	@property
	def policyname(self) :
		ur"""Name for a command policy. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the policy is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name for a command policy. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the policy is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def action(self) :
		ur"""Action to perform when a request matches the policy.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		ur"""Action to perform when a request matches the policy.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def cmdspec(self) :
		ur"""Regular expression specifying the data that matches the policy.<br/>Minimum length =  1.
		"""
		try :
			return self._cmdspec
		except Exception as e:
			raise e

	@cmdspec.setter
	def cmdspec(self, cmdspec) :
		ur"""Regular expression specifying the data that matches the policy.<br/>Minimum length =  1
		"""
		try :
			self._cmdspec = cmdspec
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur""".<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemcmdpolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemcmdpolicy
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add systemcmdpolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = systemcmdpolicy()
				addresource.policyname = resource.policyname
				addresource.action = resource.action
				addresource.cmdspec = resource.cmdspec
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ systemcmdpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].policyname = resource[i].policyname
						addresources[i].action = resource[i].action
						addresources[i].cmdspec = resource[i].cmdspec
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete systemcmdpolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = systemcmdpolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.policyname = resource
				else :
					deleteresource.policyname = resource.policyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemcmdpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemcmdpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i].policyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update systemcmdpolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = systemcmdpolicy()
				updateresource.policyname = resource.policyname
				updateresource.action = resource.action
				updateresource.cmdspec = resource.cmdspec
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ systemcmdpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].action = resource[i].action
						updateresources[i].cmdspec = resource[i].cmdspec
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systemcmdpolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemcmdpolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = systemcmdpolicy()
						obj.policyname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [systemcmdpolicy() for _ in range(len(name))]
							obj = [systemcmdpolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = systemcmdpolicy()
								obj[i].policyname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of systemcmdpolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemcmdpolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the systemcmdpolicy resources configured on NetScaler.
		"""
		try :
			obj = systemcmdpolicy()
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
		ur""" Use this API to count filtered the set of systemcmdpolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemcmdpolicy()
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

	class Action:
		ALLOW = "ALLOW"
		DENY = "DENY"

class systemcmdpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.systemcmdpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemcmdpolicy = [systemcmdpolicy() for _ in range(length)]

