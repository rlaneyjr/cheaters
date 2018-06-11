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

class aaagroup(base_resource) :
	""" Configuration for AAA group resource. """
	def __init__(self) :
		self._groupname = ""
		self._loggedin = False
		self.___count = 0

	@property
	def groupname(self) :
		ur"""Name for the group. Must begin with a letter, number, or the underscore character (_), and must consist only of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore  characters. Cannot be changed after the group is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or
		single quotation marks (for example, "my aaa group" or 'my aaa
		group).<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		ur"""Name for the group. Must begin with a letter, number, or the underscore character (_), and must consist only of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore  characters. Cannot be changed after the group is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or
		single quotation marks (for example, "my aaa group" or 'my aaa
		group).<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def loggedin(self) :
		ur"""Display only the group members who are currently logged in.
		"""
		try :
			return self._loggedin
		except Exception as e:
			raise e

	@loggedin.setter
	def loggedin(self, loggedin) :
		ur"""Display only the group members who are currently logged in.
		"""
		try :
			self._loggedin = loggedin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaagroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaagroup
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
		ur""" Use this API to add aaagroup.
		"""
		try :
			if type(resource) is not list :
				addresource = aaagroup()
				addresource.groupname = resource.groupname
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ aaagroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].groupname = resource[i].groupname
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete aaagroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = aaagroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.groupname = resource
				else :
					deleteresource.groupname = resource.groupname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaagroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].groupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaagroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].groupname = resource[i].groupname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the aaagroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaagroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = aaagroup()
						obj.groupname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [aaagroup() for _ in range(len(name))]
							obj = [aaagroup() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = aaagroup()
								obj[i].groupname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the aaagroup resources that are configured on netscaler.
	# This uses aaagroup_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = aaagroup()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of aaagroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaagroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the aaagroup resources configured on NetScaler.
		"""
		try :
			obj = aaagroup()
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
		ur""" Use this API to count filtered the set of aaagroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaagroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class aaagroup_response(base_response) :
	def __init__(self, length=1) :
		self.aaagroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaagroup = [aaagroup() for _ in range(length)]

