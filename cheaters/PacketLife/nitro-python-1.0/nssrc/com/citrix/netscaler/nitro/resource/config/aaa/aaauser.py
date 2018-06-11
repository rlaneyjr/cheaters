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

class aaauser(base_resource) :
	""" Configuration for AAA user resource. """
	def __init__(self) :
		self._username = ""
		self._password = ""
		self._loggedin = False
		self.___count = 0

	@property
	def username(self) :
		ur"""Name for the user. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the user is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or
		single quotation marks (for example, "my aaa user" or "my aaa user").<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Name for the user. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the user is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or
		single quotation marks (for example, "my aaa user" or "my aaa user").<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password with which the user logs on. Required for any user account that does not exist on an external authentication server. 
		If you are not using an external authentication server, all user accounts must have a password. If you are using an external authentication server, you must provide a password for local user accounts that do not exist on the authentication server.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password with which the user logs on. Required for any user account that does not exist on an external authentication server. 
		If you are not using an external authentication server, all user accounts must have a password. If you are using an external authentication server, you must provide a password for local user accounts that do not exist on the authentication server.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def loggedin(self) :
		ur"""Show whether the user is logged in or not.
		"""
		try :
			return self._loggedin
		except Exception as e:
			raise e

	@loggedin.setter
	def loggedin(self, loggedin) :
		ur"""Show whether the user is logged in or not.
		"""
		try :
			self._loggedin = loggedin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaauser_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaauser
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.username is not None :
				return str(self.username)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add aaauser.
		"""
		try :
			if type(resource) is not list :
				addresource = aaauser()
				addresource.username = resource.username
				addresource.password = resource.password
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ aaauser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].username = resource[i].username
						addresources[i].password = resource[i].password
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete aaauser.
		"""
		try :
			if type(resource) is not list :
				deleteresource = aaauser()
				if type(resource) !=  type(deleteresource):
					deleteresource.username = resource
				else :
					deleteresource.username = resource.username
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaauser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].username = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaauser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].username = resource[i].username
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update aaauser.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaauser()
				updateresource.username = resource.username
				updateresource.password = resource.password
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ aaauser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].username = resource[i].username
						updateresources[i].password = resource[i].password
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unlock(cls, client, resource) :
		ur""" Use this API to unlock aaauser.
		"""
		try :
			if type(resource) is not list :
				unlockresource = aaauser()
				unlockresource.username = resource.username
				return unlockresource.perform_operation(client,"unlock")
			else :
				if (resource and len(resource) > 0) :
					unlockresources = [ aaauser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						unlockresources[i].username = resource[i].username
				result = cls.perform_operation_bulk_request(client, unlockresources,"unlock")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the aaauser resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaauser()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = aaauser()
						obj.username = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [aaauser() for _ in range(len(name))]
							obj = [aaauser() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = aaauser()
								obj[i].username = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the aaauser resources that are configured on netscaler.
	# This uses aaauser_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = aaauser()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of aaauser resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaauser()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the aaauser resources configured on NetScaler.
		"""
		try :
			obj = aaauser()
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
		ur""" Use this API to count filtered the set of aaauser resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaauser()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class aaauser_response(base_response) :
	def __init__(self, length=1) :
		self.aaauser = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaauser = [aaauser() for _ in range(length)]

