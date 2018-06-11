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

class cmppolicy(base_resource) :
	""" Configuration for compression policy resource. """
	def __init__(self) :
		self._name = ""
		self._rule = ""
		self._resaction = ""
		self._newname = ""
		self._expressiontype = ""
		self._reqaction = ""
		self._hits = 0
		self._txbytes = 0
		self._rxbytes = 0
		self._clientttlb = 0
		self._clienttransactions = 0
		self._serverttlb = 0
		self._servertransactions = 0
		self._description = ""
		self._builtin = []
		self._isdefault = False
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the HTTP compression policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		Can be changed after the policy is created. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp policy" or 'my cmp policy').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the HTTP compression policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		Can be changed after the policy is created. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp policy" or 'my cmp policy').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Expression that determines which HTTP requests or responses match the compression policy. Can be a classic expression or a default-syntax expression.  
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Expression that determines which HTTP requests or responses match the compression policy. Can be a classic expression or a default-syntax expression.  
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def resaction(self) :
		ur"""The built-in or user-defined compression action to apply to the response when the policy matches a request or response.<br/>Minimum length =  1.
		"""
		try :
			return self._resaction
		except Exception as e:
			raise e

	@resaction.setter
	def resaction(self, resaction) :
		ur"""The built-in or user-defined compression action to apply to the response when the policy matches a request or response.<br/>Minimum length =  1
		"""
		try :
			self._resaction = resaction
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the compression policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		Choose a name that reflects the function that the policy performs. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp policy" or 'my cmp policy').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the compression policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		Choose a name that reflects the function that the policy performs. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cmp policy" or 'my cmp policy').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def expressiontype(self) :
		ur"""Type of policy (Classic/Advanced) .<br/>Possible values = Classic Policy, Advanced Policy.
		"""
		try :
			return self._expressiontype
		except Exception as e:
			raise e

	@property
	def reqaction(self) :
		ur"""The compression action to be performed on requests.
		"""
		try :
			return self._reqaction
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def txbytes(self) :
		ur"""Number of bytes transferred.
		"""
		try :
			return self._txbytes
		except Exception as e:
			raise e

	@property
	def rxbytes(self) :
		ur"""Number of bytes received.
		"""
		try :
			return self._rxbytes
		except Exception as e:
			raise e

	@property
	def clientttlb(self) :
		ur"""Total client TTLB value.
		"""
		try :
			return self._clientttlb
		except Exception as e:
			raise e

	@property
	def clienttransactions(self) :
		ur"""Number of client transactions.
		"""
		try :
			return self._clienttransactions
		except Exception as e:
			raise e

	@property
	def serverttlb(self) :
		ur"""Total server TTLB value.
		"""
		try :
			return self._serverttlb
		except Exception as e:
			raise e

	@property
	def servertransactions(self) :
		ur"""Number of server transactions.
		"""
		try :
			return self._servertransactions
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Description of the policy.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine if compression policy is builtin or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		ur"""A value of true is returned if it is a default policy.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cmppolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cmppolicy
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
		ur""" Use this API to add cmppolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = cmppolicy()
				addresource.name = resource.name
				addresource.rule = resource.rule
				addresource.resaction = resource.resaction
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cmppolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].rule = resource[i].rule
						addresources[i].resaction = resource[i].resaction
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete cmppolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cmppolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cmppolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cmppolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update cmppolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = cmppolicy()
				updateresource.name = resource.name
				updateresource.rule = resource.rule
				updateresource.resaction = resource.resaction
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ cmppolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].rule = resource[i].rule
						updateresources[i].resaction = resource[i].resaction
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a cmppolicy resource.
		"""
		try :
			renameresource = cmppolicy()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cmppolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cmppolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = cmppolicy()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [cmppolicy() for _ in range(len(name))]
							obj = [cmppolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = cmppolicy()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of cmppolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cmppolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the cmppolicy resources configured on NetScaler.
		"""
		try :
			obj = cmppolicy()
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
		ur""" Use this API to count filtered the set of cmppolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cmppolicy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Expressiontype:
		Classic_Policy = "Classic Policy"
		Advanced_Policy = "Advanced Policy"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

class cmppolicy_response(base_response) :
	def __init__(self, length=1) :
		self.cmppolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cmppolicy = [cmppolicy() for _ in range(length)]

