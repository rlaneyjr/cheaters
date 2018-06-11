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

class cspolicy(base_resource) :
	""" Configuration for content-switching policy resource. """
	def __init__(self) :
		self._policyname = ""
		self._url = ""
		self._rule = ""
		self._domain = ""
		self._action = ""
		self._logaction = ""
		self._newname = ""
		self._vstype = 0
		self._hits = 0
		self._bindhits = 0
		self._labelname = ""
		self._labeltype = ""
		self._priority = 0
		self._activepolicy = False
		self._cspolicytype = ""
		self.___count = 0

	@property
	def policyname(self) :
		ur"""Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after a policy is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after a policy is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def url(self) :
		ur"""URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: [[prefix] [*]] [.suffix].<br/>Minimum length =  1<br/>Maximum length =  208.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		ur"""URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: [[prefix] [*]] [.suffix].<br/>Minimum length =  1<br/>Maximum length =  208
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax. 
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		*  If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		*  If the expression itself includes double quotation marks, escape the quotations by using the  character. 
		*  Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax. 
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		*  If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		*  If the expression itself includes double quotation marks, escape the quotations by using the  character. 
		*  Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""The domain name. The string value can range to 63 characters.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""The domain name. The string value can range to 63 characters.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def action(self) :
		ur"""Content switching action that names the target load balancing virtual server to which the traffic is switched.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		ur"""Content switching action that names the target load balancing virtual server to which the traffic is switched.
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def logaction(self) :
		ur"""The log action associated with the content switching policy.
		"""
		try :
			return self._logaction
		except Exception as e:
			raise e

	@logaction.setter
	def logaction(self, logaction) :
		ur"""The log action associated with the content switching policy.
		"""
		try :
			self._logaction = logaction
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""The new name of the content switching policy.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""The new name of the content switching policy.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
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
	def hits(self) :
		ur"""Total number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def bindhits(self) :
		ur"""Total number of hits.
		"""
		try :
			return self._bindhits
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the label invoked.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""The invocation type.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""priority of bound policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def activepolicy(self) :
		ur"""Indicates whether policy is bound or not.
		"""
		try :
			return self._activepolicy
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

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cspolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cspolicy
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
		ur""" Use this API to add cspolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = cspolicy()
				addresource.policyname = resource.policyname
				addresource.url = resource.url
				addresource.rule = resource.rule
				addresource.domain = resource.domain
				addresource.action = resource.action
				addresource.logaction = resource.logaction
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cspolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].policyname = resource[i].policyname
						addresources[i].url = resource[i].url
						addresources[i].rule = resource[i].rule
						addresources[i].domain = resource[i].domain
						addresources[i].action = resource[i].action
						addresources[i].logaction = resource[i].logaction
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete cspolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cspolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.policyname = resource
				else :
					deleteresource.policyname = resource.policyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i].policyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update cspolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = cspolicy()
				updateresource.policyname = resource.policyname
				updateresource.url = resource.url
				updateresource.rule = resource.rule
				updateresource.domain = resource.domain
				updateresource.action = resource.action
				updateresource.logaction = resource.logaction
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ cspolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].url = resource[i].url
						updateresources[i].rule = resource[i].rule
						updateresources[i].domain = resource[i].domain
						updateresources[i].action = resource[i].action
						updateresources[i].logaction = resource[i].logaction
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of cspolicy resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cspolicy()
				if type(resource) !=  type(unsetresource):
					unsetresource.policyname = resource
				else :
					unsetresource.policyname = resource.policyname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ cspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ cspolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].policyname = resource[i].policyname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_policyname) :
		ur""" Use this API to rename a cspolicy resource.
		"""
		try :
			renameresource = cspolicy()
			if type(resource) == cls :
				renameresource.policyname = resource.policyname
			else :
				renameresource.policyname = resource
			return renameresource.rename_resource(client,new_policyname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cspolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cspolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = cspolicy()
						obj.policyname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [cspolicy() for _ in range(len(name))]
							obj = [cspolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = cspolicy()
								obj[i].policyname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of cspolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the cspolicy resources configured on NetScaler.
		"""
		try :
			obj = cspolicy()
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
		ur""" Use this API to count filtered the set of cspolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Cspolicytype:
		Classic_Policy = "Classic Policy"
		Advanced_Policy = "Advanced Policy"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

class cspolicy_response(base_response) :
	def __init__(self, length=1) :
		self.cspolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cspolicy = [cspolicy() for _ in range(length)]

