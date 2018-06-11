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

class authenticationcertaction(base_resource) :
	""" Configuration for CERT action resource. """
	def __init__(self) :
		self._name = ""
		self._twofactor = ""
		self._usernamefield = ""
		self._groupnamefield = ""
		self._defaultauthenticationgroup = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the client cert authentication server profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after certifcate action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the client cert authentication server profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after certifcate action is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def twofactor(self) :
		ur"""Enables or disables two-factor authentication. 
		Two factor authentication is client cert authentication followed by password authentication.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._twofactor
		except Exception as e:
			raise e

	@twofactor.setter
	def twofactor(self, twofactor) :
		ur"""Enables or disables two-factor authentication. 
		Two factor authentication is client cert authentication followed by password authentication.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._twofactor = twofactor
		except Exception as e:
			raise e

	@property
	def usernamefield(self) :
		ur"""Client-cert field from which the username is extracted. Must be set to either ""Subject"" and ""Issuer"" (include both sets of double quotation marks).
		Format: <field>:<subfield>.<br/>Minimum length =  1.
		"""
		try :
			return self._usernamefield
		except Exception as e:
			raise e

	@usernamefield.setter
	def usernamefield(self, usernamefield) :
		ur"""Client-cert field from which the username is extracted. Must be set to either ""Subject"" and ""Issuer"" (include both sets of double quotation marks).
		Format: <field>:<subfield>.<br/>Minimum length =  1
		"""
		try :
			self._usernamefield = usernamefield
		except Exception as e:
			raise e

	@property
	def groupnamefield(self) :
		ur"""Client-cert field from which the group is extracted.  Must be set to either ""Subject"" and ""Issuer"" (include both sets of double quotation marks).
		Format: <field>:<subfield>.<br/>Minimum length =  1.
		"""
		try :
			return self._groupnamefield
		except Exception as e:
			raise e

	@groupnamefield.setter
	def groupnamefield(self, groupnamefield) :
		ur"""Client-cert field from which the group is extracted.  Must be set to either ""Subject"" and ""Issuer"" (include both sets of double quotation marks).
		Format: <field>:<subfield>.<br/>Minimum length =  1
		"""
		try :
			self._groupnamefield = groupnamefield
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		ur"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		ur"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationcertaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationcertaction
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
		ur""" Use this API to add authenticationcertaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationcertaction()
				addresource.name = resource.name
				addresource.twofactor = resource.twofactor
				addresource.usernamefield = resource.usernamefield
				addresource.groupnamefield = resource.groupnamefield
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationcertaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].twofactor = resource[i].twofactor
						addresources[i].usernamefield = resource[i].usernamefield
						addresources[i].groupnamefield = resource[i].groupnamefield
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete authenticationcertaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationcertaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationcertaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationcertaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update authenticationcertaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationcertaction()
				updateresource.name = resource.name
				updateresource.twofactor = resource.twofactor
				updateresource.usernamefield = resource.usernamefield
				updateresource.groupnamefield = resource.groupnamefield
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationcertaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].twofactor = resource[i].twofactor
						updateresources[i].usernamefield = resource[i].usernamefield
						updateresources[i].groupnamefield = resource[i].groupnamefield
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of authenticationcertaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationcertaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationcertaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationcertaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the authenticationcertaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationcertaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = authenticationcertaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [authenticationcertaction() for _ in range(len(name))]
							obj = [authenticationcertaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = authenticationcertaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of authenticationcertaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationcertaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the authenticationcertaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationcertaction()
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
		ur""" Use this API to count filtered the set of authenticationcertaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationcertaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Twofactor:
		ON = "ON"
		OFF = "OFF"

class authenticationcertaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationcertaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationcertaction = [authenticationcertaction() for _ in range(length)]

