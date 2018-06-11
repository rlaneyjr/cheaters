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

class caaction(base_resource) :
	""" Configuration for ca action resource. """
	def __init__(self) :
		self._name = ""
		self._accumressize = 0
		self._lbvserver = ""
		self._comment = ""
		self._type = ""
		self._newname = ""
		self._isdefault = False
		self._hits = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the content adaptation action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the content adaptation action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def accumressize(self) :
		ur"""Size of the data, in KB, that the server must respond with. The NetScaler uses this data to compute a hash which is then used to lookup within the T2100 appliance.
		"""
		try :
			return self._accumressize
		except Exception as e:
			raise e

	@accumressize.setter
	def accumressize(self, accumressize) :
		ur"""Size of the data, in KB, that the server must respond with. The NetScaler uses this data to compute a hash which is then used to lookup within the T2100 appliance.
		"""
		try :
			self._accumressize = accumressize
		except Exception as e:
			raise e

	@property
	def lbvserver(self) :
		ur"""Name of the load balancing virtual server that has the T2100 appliances as services.
		"""
		try :
			return self._lbvserver
		except Exception as e:
			raise e

	@lbvserver.setter
	def lbvserver(self, lbvserver) :
		ur"""Name of the load balancing virtual server that has the T2100 appliances as services.
		"""
		try :
			self._lbvserver = lbvserver
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Information about the content adaptation action.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Information about the content adaptation action.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Specifies whether the NetScaler must lookup for the response on the T2100 appliance or serve the response directly from the server.<br/>Possible values = nolookup, lookup, noop.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Specifies whether the NetScaler must lookup for the response on the T2100 appliance or serve the response directly from the server.<br/>Possible values = nolookup, lookup, noop
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the ContentAdaptation action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the ContentAdaptation policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ContentAdaptation action" or 'my ContentAdaptation action').!,.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the ContentAdaptation action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the ContentAdaptation policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ContentAdaptation action" or 'my ContentAdaptation action').!,.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		ur"""A value of true is returned if it is a default content accelerator action.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The number of times the action has been taken.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine whether content accelerator action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(caaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.caaction
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
		ur""" Use this API to add caaction.
		"""
		try :
			if type(resource) is not list :
				addresource = caaction()
				addresource.name = resource.name
				addresource.accumressize = resource.accumressize
				addresource.lbvserver = resource.lbvserver
				addresource.comment = resource.comment
				addresource.type = resource.type
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ caaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].accumressize = resource[i].accumressize
						addresources[i].lbvserver = resource[i].lbvserver
						addresources[i].comment = resource[i].comment
						addresources[i].type = resource[i].type
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update caaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = caaction()
				updateresource.name = resource.name
				updateresource.accumressize = resource.accumressize
				updateresource.type = resource.type
				updateresource.lbvserver = resource.lbvserver
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ caaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].accumressize = resource[i].accumressize
						updateresources[i].type = resource[i].type
						updateresources[i].lbvserver = resource[i].lbvserver
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of caaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = caaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ caaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ caaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete caaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = caaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ caaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ caaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a caaction resource.
		"""
		try :
			renameresource = caaction()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the caaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = caaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = caaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [caaction() for _ in range(len(name))]
							obj = [caaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = caaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of caaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = caaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the caaction resources configured on NetScaler.
		"""
		try :
			obj = caaction()
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
		ur""" Use this API to count filtered the set of caaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = caaction()
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

	class Type:
		nolookup = "nolookup"
		lookup = "lookup"
		noop = "noop"

class caaction_response(base_response) :
	def __init__(self, length=1) :
		self.caaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.caaction = [caaction() for _ in range(length)]

