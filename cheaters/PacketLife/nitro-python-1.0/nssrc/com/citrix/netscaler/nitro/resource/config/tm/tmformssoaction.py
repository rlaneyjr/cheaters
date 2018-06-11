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

class tmformssoaction(base_resource) :
	""" Configuration for Form sso action resource. """
	def __init__(self) :
		self._name = ""
		self._actionurl = ""
		self._userfield = ""
		self._passwdfield = ""
		self._ssosuccessrule = ""
		self._namevaluepair = ""
		self._responsesize = 0
		self._nvtype = ""
		self._submitmethod = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the new form-based single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an SSO action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the new form-based single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an SSO action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def actionurl(self) :
		ur"""URL to which the completed form is submitted.<br/>Minimum length =  1.
		"""
		try :
			return self._actionurl
		except Exception as e:
			raise e

	@actionurl.setter
	def actionurl(self, actionurl) :
		ur"""URL to which the completed form is submitted.<br/>Minimum length =  1
		"""
		try :
			self._actionurl = actionurl
		except Exception as e:
			raise e

	@property
	def userfield(self) :
		ur"""Name of the form field in which the user types in the user ID.<br/>Minimum length =  1.
		"""
		try :
			return self._userfield
		except Exception as e:
			raise e

	@userfield.setter
	def userfield(self, userfield) :
		ur"""Name of the form field in which the user types in the user ID.<br/>Minimum length =  1
		"""
		try :
			self._userfield = userfield
		except Exception as e:
			raise e

	@property
	def passwdfield(self) :
		ur"""Name of the form field in which the user types in the password.<br/>Minimum length =  1.
		"""
		try :
			return self._passwdfield
		except Exception as e:
			raise e

	@passwdfield.setter
	def passwdfield(self, passwdfield) :
		ur"""Name of the form field in which the user types in the password.<br/>Minimum length =  1
		"""
		try :
			self._passwdfield = passwdfield
		except Exception as e:
			raise e

	@property
	def ssosuccessrule(self) :
		ur"""Expression, that checks to see if single sign-on is successful.
		"""
		try :
			return self._ssosuccessrule
		except Exception as e:
			raise e

	@ssosuccessrule.setter
	def ssosuccessrule(self, ssosuccessrule) :
		ur"""Expression, that checks to see if single sign-on is successful.
		"""
		try :
			self._ssosuccessrule = ssosuccessrule
		except Exception as e:
			raise e

	@property
	def namevaluepair(self) :
		ur"""Name-value pair attributes to send to the server in addition to sending the username and password. Value names are separated by an ampersand (&) (for example, name1=value1&name2=value2).
		"""
		try :
			return self._namevaluepair
		except Exception as e:
			raise e

	@namevaluepair.setter
	def namevaluepair(self, namevaluepair) :
		ur"""Name-value pair attributes to send to the server in addition to sending the username and password. Value names are separated by an ampersand (&) (for example, name1=value1&name2=value2).
		"""
		try :
			self._namevaluepair = namevaluepair
		except Exception as e:
			raise e

	@property
	def responsesize(self) :
		ur"""Number of bytes, in the response, to parse for extracting the forms.<br/>Default value: 8096.
		"""
		try :
			return self._responsesize
		except Exception as e:
			raise e

	@responsesize.setter
	def responsesize(self, responsesize) :
		ur"""Number of bytes, in the response, to parse for extracting the forms.<br/>Default value: 8096
		"""
		try :
			self._responsesize = responsesize
		except Exception as e:
			raise e

	@property
	def nvtype(self) :
		ur"""Type of processing of the name-value pair. If you specify STATIC, the values configured by the administrator are used. For DYNAMIC, the response is parsed, and the form is extracted and then submitted.<br/>Default value: DYNAMIC<br/>Possible values = STATIC, DYNAMIC.
		"""
		try :
			return self._nvtype
		except Exception as e:
			raise e

	@nvtype.setter
	def nvtype(self, nvtype) :
		ur"""Type of processing of the name-value pair. If you specify STATIC, the values configured by the administrator are used. For DYNAMIC, the response is parsed, and the form is extracted and then submitted.<br/>Default value: DYNAMIC<br/>Possible values = STATIC, DYNAMIC
		"""
		try :
			self._nvtype = nvtype
		except Exception as e:
			raise e

	@property
	def submitmethod(self) :
		ur"""HTTP method used by the single sign-on form to send the logon credentials to the logon server. Applies only to STATIC name-value type.<br/>Default value: GET<br/>Possible values = GET, POST.
		"""
		try :
			return self._submitmethod
		except Exception as e:
			raise e

	@submitmethod.setter
	def submitmethod(self, submitmethod) :
		ur"""HTTP method used by the single sign-on form to send the logon credentials to the logon server. Applies only to STATIC name-value type.<br/>Default value: GET<br/>Possible values = GET, POST
		"""
		try :
			self._submitmethod = submitmethod
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(tmformssoaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tmformssoaction
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
		ur""" Use this API to add tmformssoaction.
		"""
		try :
			if type(resource) is not list :
				addresource = tmformssoaction()
				addresource.name = resource.name
				addresource.actionurl = resource.actionurl
				addresource.userfield = resource.userfield
				addresource.passwdfield = resource.passwdfield
				addresource.ssosuccessrule = resource.ssosuccessrule
				addresource.namevaluepair = resource.namevaluepair
				addresource.responsesize = resource.responsesize
				addresource.nvtype = resource.nvtype
				addresource.submitmethod = resource.submitmethod
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ tmformssoaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].actionurl = resource[i].actionurl
						addresources[i].userfield = resource[i].userfield
						addresources[i].passwdfield = resource[i].passwdfield
						addresources[i].ssosuccessrule = resource[i].ssosuccessrule
						addresources[i].namevaluepair = resource[i].namevaluepair
						addresources[i].responsesize = resource[i].responsesize
						addresources[i].nvtype = resource[i].nvtype
						addresources[i].submitmethod = resource[i].submitmethod
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete tmformssoaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = tmformssoaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ tmformssoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ tmformssoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update tmformssoaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = tmformssoaction()
				updateresource.name = resource.name
				updateresource.actionurl = resource.actionurl
				updateresource.userfield = resource.userfield
				updateresource.passwdfield = resource.passwdfield
				updateresource.ssosuccessrule = resource.ssosuccessrule
				updateresource.responsesize = resource.responsesize
				updateresource.namevaluepair = resource.namevaluepair
				updateresource.nvtype = resource.nvtype
				updateresource.submitmethod = resource.submitmethod
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ tmformssoaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].actionurl = resource[i].actionurl
						updateresources[i].userfield = resource[i].userfield
						updateresources[i].passwdfield = resource[i].passwdfield
						updateresources[i].ssosuccessrule = resource[i].ssosuccessrule
						updateresources[i].responsesize = resource[i].responsesize
						updateresources[i].namevaluepair = resource[i].namevaluepair
						updateresources[i].nvtype = resource[i].nvtype
						updateresources[i].submitmethod = resource[i].submitmethod
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of tmformssoaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = tmformssoaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ tmformssoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ tmformssoaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the tmformssoaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = tmformssoaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = tmformssoaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [tmformssoaction() for _ in range(len(name))]
							obj = [tmformssoaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = tmformssoaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of tmformssoaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tmformssoaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the tmformssoaction resources configured on NetScaler.
		"""
		try :
			obj = tmformssoaction()
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
		ur""" Use this API to count filtered the set of tmformssoaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = tmformssoaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Nvtype:
		STATIC = "STATIC"
		DYNAMIC = "DYNAMIC"

	class Submitmethod:
		GET = "GET"
		POST = "POST"

class tmformssoaction_response(base_response) :
	def __init__(self, length=1) :
		self.tmformssoaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.tmformssoaction = [tmformssoaction() for _ in range(length)]

