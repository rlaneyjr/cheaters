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

class cachepolicylabel(base_resource) :
	""" Configuration for cache policy label resource. """
	def __init__(self) :
		self._labelname = ""
		self._evaluates = ""
		self._newname = ""
		self._numpol = 0
		self._hits = 0
		self._priority = 0
		self._gotopriorityexpression = ""
		self._labeltype = ""
		self._invoke_labelname = ""
		self._flowtype = 0
		self._builtin = []
		self.___count = 0

	@property
	def labelname(self) :
		ur"""Name for the label. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the label is created.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name for the label. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the label is created.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def evaluates(self) :
		ur"""When to evaluate policies bound to this label: request-time or response-time.<br/>Possible values = REQ, RES, MSSQL_REQ, MSSQL_RES, MYSQL_REQ, MYSQL_RES.
		"""
		try :
			return self._evaluates
		except Exception as e:
			raise e

	@evaluates.setter
	def evaluates(self, evaluates) :
		ur"""When to evaluate policies bound to this label: request-time or response-time.<br/>Possible values = REQ, RES, MSSQL_REQ, MSSQL_RES, MYSQL_REQ, MYSQL_RES
		"""
		try :
			self._evaluates = evaluates
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the cache-policy label. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the cache-policy label. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		ur"""Number of polices bound to label.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Number of times policy label was invoked.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Specifies the priority of the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of policy label to invoke: an unnamed label associated with a virtual server, or user-defined policy label.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def invoke_labelname(self) :
		ur"""Name of the policy label to invoke if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._invoke_labelname
		except Exception as e:
			raise e

	@property
	def flowtype(self) :
		ur"""Flowtype of the bound cache policy.
		"""
		try :
			return self._flowtype
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
			result = service.payload_formatter.string_to_resource(cachepolicylabel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cachepolicylabel
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.labelname is not None :
				return str(self.labelname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add cachepolicylabel.
		"""
		try :
			if type(resource) is not list :
				addresource = cachepolicylabel()
				addresource.labelname = resource.labelname
				addresource.evaluates = resource.evaluates
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cachepolicylabel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].labelname = resource[i].labelname
						addresources[i].evaluates = resource[i].evaluates
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete cachepolicylabel.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cachepolicylabel()
				if type(resource) !=  type(deleteresource):
					deleteresource.labelname = resource
				else :
					deleteresource.labelname = resource.labelname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cachepolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cachepolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i].labelname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_labelname) :
		ur""" Use this API to rename a cachepolicylabel resource.
		"""
		try :
			renameresource = cachepolicylabel()
			if type(resource) == cls :
				renameresource.labelname = resource.labelname
			else :
				renameresource.labelname = resource
			return renameresource.rename_resource(client,new_labelname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cachepolicylabel resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cachepolicylabel()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = cachepolicylabel()
						obj.labelname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [cachepolicylabel() for _ in range(len(name))]
							obj = [cachepolicylabel() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = cachepolicylabel()
								obj[i].labelname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of cachepolicylabel resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cachepolicylabel()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the cachepolicylabel resources configured on NetScaler.
		"""
		try :
			obj = cachepolicylabel()
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
		ur""" Use this API to count filtered the set of cachepolicylabel resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cachepolicylabel()
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

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

	class Evaluates:
		REQ = "REQ"
		RES = "RES"
		MSSQL_REQ = "MSSQL_REQ"
		MSSQL_RES = "MSSQL_RES"
		MYSQL_REQ = "MYSQL_REQ"
		MYSQL_RES = "MYSQL_RES"

class cachepolicylabel_response(base_response) :
	def __init__(self, length=1) :
		self.cachepolicylabel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cachepolicylabel = [cachepolicylabel() for _ in range(length)]

