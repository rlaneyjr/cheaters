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

class capolicy(base_resource) :
	""" Configuration for contentadaptation policy resource. """
	def __init__(self) :
		self._name = ""
		self._rule = ""
		self._action = ""
		self._undefaction = ""
		self._comment = ""
		self._logaction = ""
		self._newname = ""
		self._hits = 0
		self._undefhits = 0
		self._isdefault = False
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the content adaptation policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the policy is created.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the content adaptation policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the policy is created.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Expression that determines which requests or responses match the content adaptation policy. When specifying the rule in the CLI, the description must be enclosed within double quotes.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Expression that determines which requests or responses match the content adaptation policy. When specifying the rule in the CLI, the description must be enclosed within double quotes.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def action(self) :
		ur"""Name of content adaptation action to be executed when the rule is evaluated to true.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		ur"""Name of content adaptation action to be executed when the rule is evaluated to true.
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def undefaction(self) :
		try :
			return self._undefaction
		except Exception as e:
			raise e

	@undefaction.setter
	def undefaction(self, undefaction) :
		try :
			self._undefaction = undefaction
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Information about the content adaptation policy.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Information about the content adaptation policy.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def logaction(self) :
		ur"""Name of messagelog action to use when a request matches this policy.
		"""
		try :
			return self._logaction
		except Exception as e:
			raise e

	@logaction.setter
	def logaction(self, logaction) :
		ur"""Name of messagelog action to use when a request matches this policy.
		"""
		try :
			self._logaction = logaction
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the content accelerator policy.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the content accelerator policy.<br/>Minimum length =  1
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
		ur"""Number of Undef hits.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		ur"""A value of true is returned if it is a default ContentAdaptationpolicy.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(capolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.capolicy
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
		ur""" Use this API to add capolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = capolicy()
				addresource.name = resource.name
				addresource.rule = resource.rule
				addresource.action = resource.action
				addresource.undefaction = resource.undefaction
				addresource.comment = resource.comment
				addresource.logaction = resource.logaction
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ capolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].rule = resource[i].rule
						addresources[i].action = resource[i].action
						addresources[i].undefaction = resource[i].undefaction
						addresources[i].comment = resource[i].comment
						addresources[i].logaction = resource[i].logaction
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete capolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = capolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ capolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ capolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update capolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = capolicy()
				updateresource.name = resource.name
				updateresource.rule = resource.rule
				updateresource.action = resource.action
				updateresource.comment = resource.comment
				updateresource.logaction = resource.logaction
				updateresource.undefaction = resource.undefaction
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ capolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].rule = resource[i].rule
						updateresources[i].action = resource[i].action
						updateresources[i].comment = resource[i].comment
						updateresources[i].logaction = resource[i].logaction
						updateresources[i].undefaction = resource[i].undefaction
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of capolicy resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = capolicy()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ capolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ capolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a capolicy resource.
		"""
		try :
			renameresource = capolicy()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the capolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = capolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = capolicy()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [capolicy() for _ in range(len(name))]
							obj = [capolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = capolicy()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of capolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = capolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the capolicy resources configured on NetScaler.
		"""
		try :
			obj = capolicy()
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
		ur""" Use this API to count filtered the set of capolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = capolicy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class capolicy_response(base_response) :
	def __init__(self, length=1) :
		self.capolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.capolicy = [capolicy() for _ in range(length)]

