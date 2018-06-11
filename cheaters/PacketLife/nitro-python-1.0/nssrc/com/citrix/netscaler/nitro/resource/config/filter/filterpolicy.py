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

class filterpolicy(base_resource) :
	""" Configuration for filter policy resource. """
	def __init__(self) :
		self._name = ""
		self._rule = ""
		self._reqaction = ""
		self._resaction = ""
		self._hits = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the filtering action. Must begin with a letter, number, or the underscore character (_). Other characters allowed, after the first character, are the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), and colon (:) characters. Choose a name that helps identify the type of action. The name cannot be updated after the policy is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the filtering action. Must begin with a letter, number, or the underscore character (_). Other characters allowed, after the first character, are the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), and colon (:) characters. Choose a name that helps identify the type of action. The name cannot be updated after the policy is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy" or 'my policy').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""NetScaler classic expression specifying the type of connections that match this policy.<br/>Minimum length =  1.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""NetScaler classic expression specifying the type of connections that match this policy.<br/>Minimum length =  1
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def reqaction(self) :
		ur"""Name of the action to be performed on requests that match the policy. Cannot be specified if the rule includes condition to be evaluated for responses.<br/>Minimum length =  1.
		"""
		try :
			return self._reqaction
		except Exception as e:
			raise e

	@reqaction.setter
	def reqaction(self, reqaction) :
		ur"""Name of the action to be performed on requests that match the policy. Cannot be specified if the rule includes condition to be evaluated for responses.<br/>Minimum length =  1
		"""
		try :
			self._reqaction = reqaction
		except Exception as e:
			raise e

	@property
	def resaction(self) :
		ur"""The action to be performed on the response. The string value can be a filter action created filter action or a built-in action.<br/>Minimum length =  1.
		"""
		try :
			return self._resaction
		except Exception as e:
			raise e

	@resaction.setter
	def resaction(self, resaction) :
		ur"""The action to be performed on the response. The string value can be a filter action created filter action or a built-in action.<br/>Minimum length =  1
		"""
		try :
			self._resaction = resaction
		except Exception as e:
			raise e

	@property
	def hits(self) :
		try :
			return self._hits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(filterpolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filterpolicy
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
		ur""" Use this API to add filterpolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = filterpolicy()
				addresource.name = resource.name
				addresource.rule = resource.rule
				addresource.reqaction = resource.reqaction
				addresource.resaction = resource.resaction
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ filterpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].rule = resource[i].rule
						addresources[i].reqaction = resource[i].reqaction
						addresources[i].resaction = resource[i].resaction
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete filterpolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = filterpolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ filterpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ filterpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update filterpolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = filterpolicy()
				updateresource.name = resource.name
				updateresource.rule = resource.rule
				updateresource.reqaction = resource.reqaction
				updateresource.resaction = resource.resaction
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ filterpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].rule = resource[i].rule
						updateresources[i].reqaction = resource[i].reqaction
						updateresources[i].resaction = resource[i].resaction
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the filterpolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = filterpolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = filterpolicy()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [filterpolicy() for _ in range(len(name))]
							obj = [filterpolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = filterpolicy()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of filterpolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = filterpolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the filterpolicy resources configured on NetScaler.
		"""
		try :
			obj = filterpolicy()
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
		ur""" Use this API to count filtered the set of filterpolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = filterpolicy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class filterpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.filterpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.filterpolicy = [filterpolicy() for _ in range(length)]

