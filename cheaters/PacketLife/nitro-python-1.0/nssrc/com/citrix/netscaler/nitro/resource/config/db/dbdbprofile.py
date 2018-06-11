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

class dbdbprofile(base_resource) :
	""" Configuration for DB profile resource. """
	def __init__(self) :
		self._name = ""
		self._interpretquery = ""
		self._stickiness = ""
		self._kcdaccount = ""
		self._conmultiplex = ""
		self._enablecachingconmuxoff = ""
		self._refcnt = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the database profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile'). .<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the database profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile'). .<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def interpretquery(self) :
		ur"""If ENABLED, inspect the query and update the connection information, if required. If DISABLED, forward the query to the server.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._interpretquery
		except Exception as e:
			raise e

	@interpretquery.setter
	def interpretquery(self, interpretquery) :
		ur"""If ENABLED, inspect the query and update the connection information, if required. If DISABLED, forward the query to the server.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._interpretquery = interpretquery
		except Exception as e:
			raise e

	@property
	def stickiness(self) :
		ur"""If the queries are related to each other, forward to the same backend server.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._stickiness
		except Exception as e:
			raise e

	@stickiness.setter
	def stickiness(self, stickiness) :
		ur"""If the queries are related to each other, forward to the same backend server.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._stickiness = stickiness
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		ur"""Name of the KCD account that is used for Windows authentication.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		ur"""Name of the KCD account that is used for Windows authentication.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def conmultiplex(self) :
		ur"""Use the same server-side connection for multiple client-side requests. Default is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._conmultiplex
		except Exception as e:
			raise e

	@conmultiplex.setter
	def conmultiplex(self, conmultiplex) :
		ur"""Use the same server-side connection for multiple client-side requests. Default is enabled.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._conmultiplex = conmultiplex
		except Exception as e:
			raise e

	@property
	def enablecachingconmuxoff(self) :
		ur"""Enable caching when connection multiplexing is OFF.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._enablecachingconmuxoff
		except Exception as e:
			raise e

	@enablecachingconmuxoff.setter
	def enablecachingconmuxoff(self, enablecachingconmuxoff) :
		ur"""Enable caching when connection multiplexing is OFF.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._enablecachingconmuxoff = enablecachingconmuxoff
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		ur"""Profile Reference Count.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dbdbprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dbdbprofile
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
		ur""" Use this API to add dbdbprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = dbdbprofile()
				addresource.name = resource.name
				addresource.interpretquery = resource.interpretquery
				addresource.stickiness = resource.stickiness
				addresource.kcdaccount = resource.kcdaccount
				addresource.conmultiplex = resource.conmultiplex
				addresource.enablecachingconmuxoff = resource.enablecachingconmuxoff
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dbdbprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].interpretquery = resource[i].interpretquery
						addresources[i].stickiness = resource[i].stickiness
						addresources[i].kcdaccount = resource[i].kcdaccount
						addresources[i].conmultiplex = resource[i].conmultiplex
						addresources[i].enablecachingconmuxoff = resource[i].enablecachingconmuxoff
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete dbdbprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dbdbprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dbdbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dbdbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update dbdbprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = dbdbprofile()
				updateresource.name = resource.name
				updateresource.interpretquery = resource.interpretquery
				updateresource.stickiness = resource.stickiness
				updateresource.kcdaccount = resource.kcdaccount
				updateresource.conmultiplex = resource.conmultiplex
				updateresource.enablecachingconmuxoff = resource.enablecachingconmuxoff
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dbdbprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].interpretquery = resource[i].interpretquery
						updateresources[i].stickiness = resource[i].stickiness
						updateresources[i].kcdaccount = resource[i].kcdaccount
						updateresources[i].conmultiplex = resource[i].conmultiplex
						updateresources[i].enablecachingconmuxoff = resource[i].enablecachingconmuxoff
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of dbdbprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dbdbprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dbdbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dbdbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the dbdbprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dbdbprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = dbdbprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [dbdbprofile() for _ in range(len(name))]
							obj = [dbdbprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = dbdbprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of dbdbprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dbdbprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the dbdbprofile resources configured on NetScaler.
		"""
		try :
			obj = dbdbprofile()
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
		ur""" Use this API to count filtered the set of dbdbprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dbdbprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Conmultiplex:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Enablecachingconmuxoff:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Stickiness:
		YES = "YES"
		NO = "NO"

	class Interpretquery:
		YES = "YES"
		NO = "NO"

class dbdbprofile_response(base_response) :
	def __init__(self, length=1) :
		self.dbdbprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dbdbprofile = [dbdbprofile() for _ in range(length)]

