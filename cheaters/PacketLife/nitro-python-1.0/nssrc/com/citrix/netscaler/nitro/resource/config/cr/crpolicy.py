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

class crpolicy(base_resource) :
	""" Configuration for cache redirection policy resource. """
	def __init__(self) :
		self._policyname = ""
		self._rule = ""
		self._domain = ""
		self._vstype = 0
		self._cspolicytype = ""
		self._builtin = []
		self.___count = 0

	@property
	def policyname(self) :
		ur"""Name for the cache redirection policy. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after the policy is created.
		The following requirement applies only to the NetScaler CLI: 
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name for the cache redirection policy. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after the policy is created.
		The following requirement applies only to the NetScaler CLI: 
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic syntax.
		Note:Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: "<string of 255 characters>" + "<string of 245 characters>"
		The following requirements apply only to the NetScaler CLI:
		*  If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		*  If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		*  Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic syntax.
		Note:Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: "<string of 255 characters>" + "<string of 245 characters>"
		The following requirements apply only to the NetScaler CLI:
		*  If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		*  If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		*  Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""Domain name.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@property
	def vstype(self) :
		ur"""Virtual server type.
		"""
		try :
			return self._vstype
		except Exception as e:
			raise e

	@property
	def cspolicytype(self) :
		ur"""Indicates whether policy is PI or not.(used only during display).<br/>Possible values = Classic Policy, Advanced Policy.
		"""
		try :
			return self._cspolicytype
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
			result = service.payload_formatter.string_to_resource(crpolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.crpolicy
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
		ur""" Use this API to add crpolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = crpolicy()
				addresource.policyname = resource.policyname
				addresource.rule = resource.rule
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ crpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].policyname = resource[i].policyname
						addresources[i].rule = resource[i].rule
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete crpolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = crpolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.policyname = resource
				else :
					deleteresource.policyname = resource.policyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ crpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ crpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i].policyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update crpolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = crpolicy()
				updateresource.policyname = resource.policyname
				updateresource.rule = resource.rule
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ crpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].rule = resource[i].rule
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the crpolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = crpolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = crpolicy()
						obj.policyname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [crpolicy() for _ in range(len(name))]
							obj = [crpolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = crpolicy()
								obj[i].policyname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of crpolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = crpolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the crpolicy resources configured on NetScaler.
		"""
		try :
			obj = crpolicy()
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
		ur""" Use this API to count filtered the set of crpolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = crpolicy()
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

	class Cspolicytype:
		Classic_Policy = "Classic Policy"
		Advanced_Policy = "Advanced Policy"

class crpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.crpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.crpolicy = [crpolicy() for _ in range(length)]

