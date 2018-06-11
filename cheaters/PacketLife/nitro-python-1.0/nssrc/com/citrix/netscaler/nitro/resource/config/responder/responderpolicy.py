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

class responderpolicy(base_resource) :
	""" Configuration for responder policy resource. """
	def __init__(self) :
		self._name = ""
		self._rule = ""
		self._action = ""
		self._undefaction = ""
		self._comment = ""
		self._logaction = ""
		self._appflowaction = ""
		self._newname = ""
		self._hits = 0
		self._undefhits = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the responder policy.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the responder policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder policy" or 'my responder policy').
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the responder policy.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the responder policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder policy" or 'my responder policy').
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Default syntax expression that the policy uses to determine whether to respond to the specified request.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Default syntax expression that the policy uses to determine whether to respond to the specified request.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def action(self) :
		ur"""Name of the responder action to perform if the request matches this responder policy. There are also some built-in actions which can be used. These are:
		* NOOP - Send the request to the protected server instead of responding to it.
		* RESET - Reset the client connection by closing it. The client program, such as a browser, will handle this and may inform the user. The client may then resend the request if desired.
		* DROP - Drop the request without sending a response to the user.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		ur"""Name of the responder action to perform if the request matches this responder policy. There are also some built-in actions which can be used. These are:
		* NOOP - Send the request to the protected server instead of responding to it.
		* RESET - Reset the client connection by closing it. The client program, such as a browser, will handle this and may inform the user. The client may then resend the request if desired.
		* DROP - Drop the request without sending a response to the user.
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def undefaction(self) :
		ur"""Action to perform if the result of policy evaluation is undefined (UNDEF). An UNDEF event indicates an internal error condition. Only the above built-in actions can be used.
		"""
		try :
			return self._undefaction
		except Exception as e:
			raise e

	@undefaction.setter
	def undefaction(self, undefaction) :
		ur"""Action to perform if the result of policy evaluation is undefined (UNDEF). An UNDEF event indicates an internal error condition. Only the above built-in actions can be used.
		"""
		try :
			self._undefaction = undefaction
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any type of information about this responder policy.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any type of information about this responder policy.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def logaction(self) :
		ur"""Name of the messagelog action to use for requests that match this policy.
		"""
		try :
			return self._logaction
		except Exception as e:
			raise e

	@logaction.setter
	def logaction(self, logaction) :
		ur"""Name of the messagelog action to use for requests that match this policy.
		"""
		try :
			self._logaction = logaction
		except Exception as e:
			raise e

	@property
	def appflowaction(self) :
		ur"""AppFlow action to invoke for requests that match this policy.
		"""
		try :
			return self._appflowaction
		except Exception as e:
			raise e

	@appflowaction.setter
	def appflowaction(self, appflowaction) :
		ur"""AppFlow action to invoke for requests that match this policy.
		"""
		try :
			self._appflowaction = appflowaction
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the responder policy. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder policy" or 'my responder policy').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the responder policy. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. 
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder policy" or 'my responder policy').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
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
	def undefhits(self) :
		ur"""Number of policy UNDEF hits.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine if responder policy is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(responderpolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.responderpolicy
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
		ur""" Use this API to add responderpolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = responderpolicy()
				addresource.name = resource.name
				addresource.rule = resource.rule
				addresource.action = resource.action
				addresource.undefaction = resource.undefaction
				addresource.comment = resource.comment
				addresource.logaction = resource.logaction
				addresource.appflowaction = resource.appflowaction
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ responderpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].rule = resource[i].rule
						addresources[i].action = resource[i].action
						addresources[i].undefaction = resource[i].undefaction
						addresources[i].comment = resource[i].comment
						addresources[i].logaction = resource[i].logaction
						addresources[i].appflowaction = resource[i].appflowaction
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete responderpolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = responderpolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ responderpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ responderpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update responderpolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = responderpolicy()
				updateresource.name = resource.name
				updateresource.rule = resource.rule
				updateresource.action = resource.action
				updateresource.undefaction = resource.undefaction
				updateresource.comment = resource.comment
				updateresource.logaction = resource.logaction
				updateresource.appflowaction = resource.appflowaction
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ responderpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].rule = resource[i].rule
						updateresources[i].action = resource[i].action
						updateresources[i].undefaction = resource[i].undefaction
						updateresources[i].comment = resource[i].comment
						updateresources[i].logaction = resource[i].logaction
						updateresources[i].appflowaction = resource[i].appflowaction
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of responderpolicy resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = responderpolicy()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ responderpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ responderpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a responderpolicy resource.
		"""
		try :
			renameresource = responderpolicy()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the responderpolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = responderpolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = responderpolicy()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [responderpolicy() for _ in range(len(name))]
							obj = [responderpolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = responderpolicy()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of responderpolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = responderpolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the responderpolicy resources configured on NetScaler.
		"""
		try :
			obj = responderpolicy()
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
		ur""" Use this API to count filtered the set of responderpolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = responderpolicy()
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

class responderpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.responderpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.responderpolicy = [responderpolicy() for _ in range(length)]

