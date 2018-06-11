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

class scpolicy(base_resource) :
	""" Configuration for SureConnect policy resource. """
	def __init__(self) :
		self._name = ""
		self._url = ""
		self._rule = ""
		self._delay = 0
		self._maxconn = 0
		self._action = ""
		self._altcontentsvcname = ""
		self._altcontentpath = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the policy. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def url(self) :
		ur"""URL against which to match incoming client request.<br/>Maximum length =  127.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		ur"""URL against which to match incoming client request.<br/>Maximum length =  127
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Expression against which the traffic is evaluated. 
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the  character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Maximum length =  1499.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Expression against which the traffic is evaluated. 
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the  character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Maximum length =  1499
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def delay(self) :
		ur"""Delay threshold, in microseconds, for requests that match the policy's URL or rule. If the delay statistics gathered for the matching request exceed the specified delay, SureConnect is triggered for that request.<br/>Minimum length =  1<br/>Maximum length =  599999999.
		"""
		try :
			return self._delay
		except Exception as e:
			raise e

	@delay.setter
	def delay(self, delay) :
		ur"""Delay threshold, in microseconds, for requests that match the policy's URL or rule. If the delay statistics gathered for the matching request exceed the specified delay, SureConnect is triggered for that request.<br/>Minimum length =  1<br/>Maximum length =  599999999
		"""
		try :
			self._delay = delay
		except Exception as e:
			raise e

	@property
	def maxconn(self) :
		ur"""Maximum number of concurrent connections that can be open for requests that match the policy's URL or rule.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._maxconn
		except Exception as e:
			raise e

	@maxconn.setter
	def maxconn(self, maxconn) :
		ur"""Maximum number of concurrent connections that can be open for requests that match the policy's URL or rule.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._maxconn = maxconn
		except Exception as e:
			raise e

	@property
	def action(self) :
		ur"""Action to be taken when the delay or maximum-connections threshold is reached. Available settings function as follows:
		ACS - Serve content from an alternative content service.
		NS - Serve alternative content from the NetScaler appliance.
		NO ACTION - Serve no alternative content. However, delay statistics are still collected for the configured URLs, and, if the Maximum Client Connections parameter is set, the number of connections is limited to the value specified by that parameter. (However, alternative content is not served even if the maxConn threshold is met).<br/>Possible values = ACS, NS, NOACTION.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		ur"""Action to be taken when the delay or maximum-connections threshold is reached. Available settings function as follows:
		ACS - Serve content from an alternative content service.
		NS - Serve alternative content from the NetScaler appliance.
		NO ACTION - Serve no alternative content. However, delay statistics are still collected for the configured URLs, and, if the Maximum Client Connections parameter is set, the number of connections is limited to the value specified by that parameter. (However, alternative content is not served even if the maxConn threshold is met).<br/>Possible values = ACS, NS, NOACTION
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def altcontentsvcname(self) :
		ur"""Name of the alternative content service to be used in the ACS action.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._altcontentsvcname
		except Exception as e:
			raise e

	@altcontentsvcname.setter
	def altcontentsvcname(self, altcontentsvcname) :
		ur"""Name of the alternative content service to be used in the ACS action.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._altcontentsvcname = altcontentsvcname
		except Exception as e:
			raise e

	@property
	def altcontentpath(self) :
		ur"""Path to the alternative content service to be used in the ACS action.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._altcontentpath
		except Exception as e:
			raise e

	@altcontentpath.setter
	def altcontentpath(self, altcontentpath) :
		ur"""Path to the alternative content service to be used in the ACS action.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._altcontentpath = altcontentpath
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(scpolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.scpolicy
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
		ur""" Use this API to add scpolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = scpolicy()
				addresource.name = resource.name
				addresource.url = resource.url
				addresource.rule = resource.rule
				addresource.delay = resource.delay
				addresource.maxconn = resource.maxconn
				addresource.action = resource.action
				addresource.altcontentsvcname = resource.altcontentsvcname
				addresource.altcontentpath = resource.altcontentpath
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ scpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].url = resource[i].url
						addresources[i].rule = resource[i].rule
						addresources[i].delay = resource[i].delay
						addresources[i].maxconn = resource[i].maxconn
						addresources[i].action = resource[i].action
						addresources[i].altcontentsvcname = resource[i].altcontentsvcname
						addresources[i].altcontentpath = resource[i].altcontentpath
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete scpolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = scpolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ scpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ scpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update scpolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = scpolicy()
				updateresource.name = resource.name
				updateresource.url = resource.url
				updateresource.rule = resource.rule
				updateresource.delay = resource.delay
				updateresource.maxconn = resource.maxconn
				updateresource.action = resource.action
				updateresource.altcontentsvcname = resource.altcontentsvcname
				updateresource.altcontentpath = resource.altcontentpath
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ scpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].url = resource[i].url
						updateresources[i].rule = resource[i].rule
						updateresources[i].delay = resource[i].delay
						updateresources[i].maxconn = resource[i].maxconn
						updateresources[i].action = resource[i].action
						updateresources[i].altcontentsvcname = resource[i].altcontentsvcname
						updateresources[i].altcontentpath = resource[i].altcontentpath
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of scpolicy resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = scpolicy()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ scpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ scpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the scpolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = scpolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = scpolicy()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [scpolicy() for _ in range(len(name))]
							obj = [scpolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = scpolicy()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of scpolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = scpolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the scpolicy resources configured on NetScaler.
		"""
		try :
			obj = scpolicy()
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
		ur""" Use this API to count filtered the set of scpolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = scpolicy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Action:
		ACS = "ACS"
		NS = "NS"
		NOACTION = "NOACTION"

class scpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.scpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.scpolicy = [scpolicy() for _ in range(length)]

