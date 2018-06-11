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

class authenticationnegotiateaction(base_resource) :
	""" Configuration for Negotiate action resource. """
	def __init__(self) :
		self._name = ""
		self._domain = ""
		self._domainuser = ""
		self._domainuserpasswd = ""
		self._ou = ""
		self._defaultauthenticationgroup = ""
		self._keytab = ""
		self._kcdspn = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the AD KDC server profile (negotiate action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after AD KDC server profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the AD KDC server profile (negotiate action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after AD KDC server profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""Domain name of the AD KDC server.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""Domain name of the AD KDC server.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def domainuser(self) :
		ur"""User name that the NetScaler appliance uses to join the AD KDC server domain. 
		The NetScaler appliance uses the domain user name to check the health of the AD KDC server.<br/>Minimum length =  1.
		"""
		try :
			return self._domainuser
		except Exception as e:
			raise e

	@domainuser.setter
	def domainuser(self, domainuser) :
		ur"""User name that the NetScaler appliance uses to join the AD KDC server domain. 
		The NetScaler appliance uses the domain user name to check the health of the AD KDC server.<br/>Minimum length =  1
		"""
		try :
			self._domainuser = domainuser
		except Exception as e:
			raise e

	@property
	def domainuserpasswd(self) :
		ur"""Password that the NetScaler appliance uses to join the AD KDC server domain.<br/>Minimum length =  1.
		"""
		try :
			return self._domainuserpasswd
		except Exception as e:
			raise e

	@domainuserpasswd.setter
	def domainuserpasswd(self, domainuserpasswd) :
		ur"""Password that the NetScaler appliance uses to join the AD KDC server domain.<br/>Minimum length =  1
		"""
		try :
			self._domainuserpasswd = domainuserpasswd
		except Exception as e:
			raise e

	@property
	def ou(self) :
		ur"""Active Directory organizational units (OU) attribute.<br/>Minimum length =  1.
		"""
		try :
			return self._ou
		except Exception as e:
			raise e

	@ou.setter
	def ou(self, ou) :
		ur"""Active Directory organizational units (OU) attribute.<br/>Minimum length =  1
		"""
		try :
			self._ou = ou
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

	@property
	def keytab(self) :
		ur"""The path to the keytab file.<br/>Minimum length =  1.
		"""
		try :
			return self._keytab
		except Exception as e:
			raise e

	@keytab.setter
	def keytab(self, keytab) :
		ur"""The path to the keytab file.<br/>Minimum length =  1
		"""
		try :
			self._keytab = keytab
		except Exception as e:
			raise e

	@property
	def kcdspn(self) :
		ur"""Host SPN extracted from keytab file.
		"""
		try :
			return self._kcdspn
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationnegotiateaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationnegotiateaction
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
		ur""" Use this API to add authenticationnegotiateaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationnegotiateaction()
				addresource.name = resource.name
				addresource.domain = resource.domain
				addresource.domainuser = resource.domainuser
				addresource.domainuserpasswd = resource.domainuserpasswd
				addresource.ou = resource.ou
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				addresource.keytab = resource.keytab
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationnegotiateaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].domain = resource[i].domain
						addresources[i].domainuser = resource[i].domainuser
						addresources[i].domainuserpasswd = resource[i].domainuserpasswd
						addresources[i].ou = resource[i].ou
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						addresources[i].keytab = resource[i].keytab
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete authenticationnegotiateaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationnegotiateaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationnegotiateaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationnegotiateaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update authenticationnegotiateaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationnegotiateaction()
				updateresource.name = resource.name
				updateresource.domain = resource.domain
				updateresource.domainuser = resource.domainuser
				updateresource.domainuserpasswd = resource.domainuserpasswd
				updateresource.ou = resource.ou
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.keytab = resource.keytab
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationnegotiateaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].domain = resource[i].domain
						updateresources[i].domainuser = resource[i].domainuser
						updateresources[i].domainuserpasswd = resource[i].domainuserpasswd
						updateresources[i].ou = resource[i].ou
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						updateresources[i].keytab = resource[i].keytab
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of authenticationnegotiateaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationnegotiateaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationnegotiateaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationnegotiateaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the authenticationnegotiateaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationnegotiateaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = authenticationnegotiateaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [authenticationnegotiateaction() for _ in range(len(name))]
							obj = [authenticationnegotiateaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = authenticationnegotiateaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of authenticationnegotiateaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationnegotiateaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the authenticationnegotiateaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationnegotiateaction()
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
		ur""" Use this API to count filtered the set of authenticationnegotiateaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationnegotiateaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class authenticationnegotiateaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationnegotiateaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationnegotiateaction = [authenticationnegotiateaction() for _ in range(length)]

