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

class systemuser(base_resource) :
	""" Configuration for system user resource. """
	def __init__(self) :
		self._username = ""
		self._password = ""
		self._externalauth = ""
		self._promptstring = ""
		self._timeout = 0
		self._logging = ""
		self._encrypted = False
		self._promptinheritedfrom = ""
		self._timeoutkind = ""
		self.___count = 0

	@property
	def username(self) :
		ur"""Name for a user. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the user is added.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my user" or 'my user').<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		ur"""Name for a user. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the user is added.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my user" or 'my user').<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password for the system user. Can include any ASCII character.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password for the system user. Can include any ASCII character.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def externalauth(self) :
		ur"""Whether to use external authentication servers for the system user authentication or not.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._externalauth
		except Exception as e:
			raise e

	@externalauth.setter
	def externalauth(self, externalauth) :
		ur"""Whether to use external authentication servers for the system user authentication or not.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._externalauth = externalauth
		except Exception as e:
			raise e

	@property
	def promptstring(self) :
		ur"""String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables: 
		* %u - Will be replaced by the user name.
		* %h - Will be replaced by the hostname of the NetScaler appliance.
		* %t - Will be replaced by the current time in 12-hour format.
		* %T - Will be replaced by the current time in 24-hour format.
		* %d - Will be replaced by the current date.
		* %s - Will be replaced by the state of the NetScaler appliance.
		Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1.
		"""
		try :
			return self._promptstring
		except Exception as e:
			raise e

	@promptstring.setter
	def promptstring(self, promptstring) :
		ur"""String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables: 
		* %u - Will be replaced by the user name.
		* %h - Will be replaced by the hostname of the NetScaler appliance.
		* %t - Will be replaced by the current time in 12-hour format.
		* %T - Will be replaced by the current time in 24-hour format.
		* %d - Will be replaced by the current date.
		* %s - Will be replaced by the state of the NetScaler appliance.
		Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1
		"""
		try :
			self._promptstring = promptstring
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		ur"""CLI session inactivity timeout, in seconds. If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds. If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		ur"""CLI session inactivity timeout, in seconds. If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds. If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def logging(self) :
		ur"""Users logging privilege.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logging
		except Exception as e:
			raise e

	@logging.setter
	def logging(self, logging) :
		ur"""Users logging privilege.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logging = logging
		except Exception as e:
			raise e

	@property
	def encrypted(self) :
		try :
			return self._encrypted
		except Exception as e:
			raise e

	@property
	def promptinheritedfrom(self) :
		ur"""From where the prompt has been inherited.<br/>Possible values = User, Group, Global, Climode.
		"""
		try :
			return self._promptinheritedfrom
		except Exception as e:
			raise e

	@property
	def timeoutkind(self) :
		ur"""From where the timeout has been inherited.<br/>Possible values = User, Group, Global, Climode.
		"""
		try :
			return self._timeoutkind
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemuser_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemuser
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
		ur""" Use this API to add systemuser.
		"""
		try :
			if type(resource) is not list :
				addresource = systemuser()
				addresource.username = resource.username
				addresource.password = resource.password
				addresource.externalauth = resource.externalauth
				addresource.promptstring = resource.promptstring
				addresource.timeout = resource.timeout
				addresource.logging = resource.logging
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ systemuser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].username = resource[i].username
						addresources[i].password = resource[i].password
						addresources[i].externalauth = resource[i].externalauth
						addresources[i].promptstring = resource[i].promptstring
						addresources[i].timeout = resource[i].timeout
						addresources[i].logging = resource[i].logging
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete systemuser.
		"""
		try :
			if type(resource) is not list :
				deleteresource = systemuser()
				if type(resource) !=  type(deleteresource):
					deleteresource.username = resource
				else :
					deleteresource.username = resource.username
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].username = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].username = resource[i].username
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update systemuser.
		"""
		try :
			if type(resource) is not list :
				updateresource = systemuser()
				updateresource.username = resource.username
				updateresource.password = resource.password
				updateresource.externalauth = resource.externalauth
				updateresource.promptstring = resource.promptstring
				updateresource.timeout = resource.timeout
				updateresource.logging = resource.logging
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ systemuser() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].username = resource[i].username
						updateresources[i].password = resource[i].password
						updateresources[i].externalauth = resource[i].externalauth
						updateresources[i].promptstring = resource[i].promptstring
						updateresources[i].timeout = resource[i].timeout
						updateresources[i].logging = resource[i].logging
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of systemuser resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = systemuser()
				if type(resource) !=  type(unsetresource):
					unsetresource.username = resource
				else :
					unsetresource.username = resource.username
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ systemuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].username = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ systemuser() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].username = resource[i].username
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systemuser resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemuser()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = systemuser()
						obj.username = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [systemuser() for _ in range(len(name))]
							obj = [systemuser() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = systemuser()
								obj[i].username = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of systemuser resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemuser()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the systemuser resources configured on NetScaler.
		"""
		try :
			obj = systemuser()
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
		ur""" Use this API to count filtered the set of systemuser resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemuser()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Timeoutkind:
		User = "User"
		Group = "Group"
		Global = "Global"
		Climode = "Climode"

	class Promptinheritedfrom:
		User = "User"
		Group = "Group"
		Global = "Global"
		Climode = "Climode"

	class Logging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Externalauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class systemuser_response(base_response) :
	def __init__(self, length=1) :
		self.systemuser = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemuser = [systemuser() for _ in range(length)]

