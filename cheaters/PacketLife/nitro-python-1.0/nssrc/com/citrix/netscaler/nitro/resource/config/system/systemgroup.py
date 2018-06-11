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

class systemgroup(base_resource) :
	""" Configuration for system group resource. """
	def __init__(self) :
		self._groupname = ""
		self._promptstring = ""
		self._timeout = 0
		self.___count = 0

	@property
	def groupname(self) :
		ur"""Name for the group. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the group is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my group" or 'my group').<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name for the group. Must begin with a letter, number, or the underscore (_) character, and must contain only alphanumeric, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed after the group is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my group" or 'my group').<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
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
		ur"""CLI session inactivity timeout, in seconds.If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds. If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		ur"""CLI session inactivity timeout, in seconds.If Restrictedtimeout argument of system parameter is enabled, Timeout can have values in the range [300-86400] seconds. If Restrictedtimeout argument of system parameter is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemgroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemgroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.groupname is not None :
				return str(self.groupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add systemgroup.
		"""
		try :
			if type(resource) is not list :
				addresource = systemgroup()
				addresource.groupname = resource.groupname
				addresource.promptstring = resource.promptstring
				addresource.timeout = resource.timeout
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ systemgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].groupname = resource[i].groupname
						addresources[i].promptstring = resource[i].promptstring
						addresources[i].timeout = resource[i].timeout
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete systemgroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = systemgroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.groupname = resource
				else :
					deleteresource.groupname = resource.groupname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].groupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].groupname = resource[i].groupname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update systemgroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = systemgroup()
				updateresource.groupname = resource.groupname
				updateresource.promptstring = resource.promptstring
				updateresource.timeout = resource.timeout
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ systemgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].groupname = resource[i].groupname
						updateresources[i].promptstring = resource[i].promptstring
						updateresources[i].timeout = resource[i].timeout
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of systemgroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = systemgroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.groupname = resource
				else :
					unsetresource.groupname = resource.groupname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ systemgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].groupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ systemgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].groupname = resource[i].groupname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the systemgroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemgroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = systemgroup()
						obj.groupname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [systemgroup() for _ in range(len(name))]
							obj = [systemgroup() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = systemgroup()
								obj[i].groupname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of systemgroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemgroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the systemgroup resources configured on NetScaler.
		"""
		try :
			obj = systemgroup()
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
		ur""" Use this API to count filtered the set of systemgroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemgroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class systemgroup_response(base_response) :
	def __init__(self, length=1) :
		self.systemgroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemgroup = [systemgroup() for _ in range(length)]

