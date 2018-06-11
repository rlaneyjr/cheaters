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

class authenticationwebauthaction(base_resource) :
	""" Configuration for Web authentication action resource. """
	def __init__(self) :
		self._name = ""
		self._serverip = ""
		self._serverport = 0
		self._fullreqexpr = ""
		self._scheme = ""
		self._successrule = ""
		self._defaultauthenticationgroup = ""
		self._attribute1 = ""
		self._attribute2 = ""
		self._attribute3 = ""
		self._attribute4 = ""
		self._attribute5 = ""
		self._attribute6 = ""
		self._attribute7 = ""
		self._attribute8 = ""
		self._attribute9 = ""
		self._attribute10 = ""
		self._attribute11 = ""
		self._attribute12 = ""
		self._attribute13 = ""
		self._attribute14 = ""
		self._attribute15 = ""
		self._attribute16 = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the Web Authentication action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the Web Authentication action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		ur"""IP address of the web server to be used for authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		ur"""IP address of the web server to be used for authentication.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		ur"""Port on which the web server accepts connections.<br/>Minimum length =  1<br/>Range 1 - 65535.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		ur"""Port on which the web server accepts connections.<br/>Minimum length =  1<br/>Range 1 - 65535
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def fullreqexpr(self) :
		ur"""Exact HTTP request, in the form of a default syntax expression, which the NetScaler appliance sends to the authentication server.
		The NetScaler appliance does not check the validity of this request. One must manually validate the request.
		"""
		try :
			return self._fullreqexpr
		except Exception as e:
			raise e

	@fullreqexpr.setter
	def fullreqexpr(self, fullreqexpr) :
		ur"""Exact HTTP request, in the form of a default syntax expression, which the NetScaler appliance sends to the authentication server.
		The NetScaler appliance does not check the validity of this request. One must manually validate the request.
		"""
		try :
			self._fullreqexpr = fullreqexpr
		except Exception as e:
			raise e

	@property
	def scheme(self) :
		ur"""Type of scheme for the web server.<br/>Possible values = http, https.
		"""
		try :
			return self._scheme
		except Exception as e:
			raise e

	@scheme.setter
	def scheme(self, scheme) :
		ur"""Type of scheme for the web server.<br/>Possible values = http, https
		"""
		try :
			self._scheme = scheme
		except Exception as e:
			raise e

	@property
	def successrule(self) :
		ur"""Expression, that checks to see if authentication is successful.
		"""
		try :
			return self._successrule
		except Exception as e:
			raise e

	@successrule.setter
	def successrule(self, successrule) :
		ur"""Expression, that checks to see if authentication is successful.
		"""
		try :
			self._successrule = successrule
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
	def attribute1(self) :
		ur"""Expression that would be evaluated to extract attribute1 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute1
		except Exception as e:
			raise e

	@attribute1.setter
	def attribute1(self, attribute1) :
		ur"""Expression that would be evaluated to extract attribute1 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute1 = attribute1
		except Exception as e:
			raise e

	@property
	def attribute2(self) :
		ur"""Expression that would be evaluated to extract attribute2 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute2
		except Exception as e:
			raise e

	@attribute2.setter
	def attribute2(self, attribute2) :
		ur"""Expression that would be evaluated to extract attribute2 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute2 = attribute2
		except Exception as e:
			raise e

	@property
	def attribute3(self) :
		ur"""Expression that would be evaluated to extract attribute3 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute3
		except Exception as e:
			raise e

	@attribute3.setter
	def attribute3(self, attribute3) :
		ur"""Expression that would be evaluated to extract attribute3 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute3 = attribute3
		except Exception as e:
			raise e

	@property
	def attribute4(self) :
		ur"""Expression that would be evaluated to extract attribute4 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute4
		except Exception as e:
			raise e

	@attribute4.setter
	def attribute4(self, attribute4) :
		ur"""Expression that would be evaluated to extract attribute4 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute4 = attribute4
		except Exception as e:
			raise e

	@property
	def attribute5(self) :
		ur"""Expression that would be evaluated to extract attribute5 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute5
		except Exception as e:
			raise e

	@attribute5.setter
	def attribute5(self, attribute5) :
		ur"""Expression that would be evaluated to extract attribute5 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute5 = attribute5
		except Exception as e:
			raise e

	@property
	def attribute6(self) :
		ur"""Expression that would be evaluated to extract attribute6 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute6
		except Exception as e:
			raise e

	@attribute6.setter
	def attribute6(self, attribute6) :
		ur"""Expression that would be evaluated to extract attribute6 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute6 = attribute6
		except Exception as e:
			raise e

	@property
	def attribute7(self) :
		ur"""Expression that would be evaluated to extract attribute7 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute7
		except Exception as e:
			raise e

	@attribute7.setter
	def attribute7(self, attribute7) :
		ur"""Expression that would be evaluated to extract attribute7 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute7 = attribute7
		except Exception as e:
			raise e

	@property
	def attribute8(self) :
		ur"""Expression that would be evaluated to extract attribute8 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute8
		except Exception as e:
			raise e

	@attribute8.setter
	def attribute8(self, attribute8) :
		ur"""Expression that would be evaluated to extract attribute8 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute8 = attribute8
		except Exception as e:
			raise e

	@property
	def attribute9(self) :
		ur"""Expression that would be evaluated to extract attribute9 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute9
		except Exception as e:
			raise e

	@attribute9.setter
	def attribute9(self, attribute9) :
		ur"""Expression that would be evaluated to extract attribute9 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute9 = attribute9
		except Exception as e:
			raise e

	@property
	def attribute10(self) :
		ur"""Expression that would be evaluated to extract attribute10 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute10
		except Exception as e:
			raise e

	@attribute10.setter
	def attribute10(self, attribute10) :
		ur"""Expression that would be evaluated to extract attribute10 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute10 = attribute10
		except Exception as e:
			raise e

	@property
	def attribute11(self) :
		ur"""Expression that would be evaluated to extract attribute11 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute11
		except Exception as e:
			raise e

	@attribute11.setter
	def attribute11(self, attribute11) :
		ur"""Expression that would be evaluated to extract attribute11 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute11 = attribute11
		except Exception as e:
			raise e

	@property
	def attribute12(self) :
		ur"""Expression that would be evaluated to extract attribute12 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute12
		except Exception as e:
			raise e

	@attribute12.setter
	def attribute12(self, attribute12) :
		ur"""Expression that would be evaluated to extract attribute12 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute12 = attribute12
		except Exception as e:
			raise e

	@property
	def attribute13(self) :
		ur"""Expression that would be evaluated to extract attribute13 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute13
		except Exception as e:
			raise e

	@attribute13.setter
	def attribute13(self, attribute13) :
		ur"""Expression that would be evaluated to extract attribute13 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute13 = attribute13
		except Exception as e:
			raise e

	@property
	def attribute14(self) :
		ur"""Expression that would be evaluated to extract attribute14 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute14
		except Exception as e:
			raise e

	@attribute14.setter
	def attribute14(self, attribute14) :
		ur"""Expression that would be evaluated to extract attribute14 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute14 = attribute14
		except Exception as e:
			raise e

	@property
	def attribute15(self) :
		ur"""Expression that would be evaluated to extract attribute15 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute15
		except Exception as e:
			raise e

	@attribute15.setter
	def attribute15(self, attribute15) :
		ur"""Expression that would be evaluated to extract attribute15 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute15 = attribute15
		except Exception as e:
			raise e

	@property
	def attribute16(self) :
		ur"""Expression that would be evaluated to extract attribute16 from the webauth response.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute16
		except Exception as e:
			raise e

	@attribute16.setter
	def attribute16(self, attribute16) :
		ur"""Expression that would be evaluated to extract attribute16 from the webauth response.<br/>Maximum length =  128
		"""
		try :
			self._attribute16 = attribute16
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationwebauthaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationwebauthaction
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
		ur""" Use this API to add authenticationwebauthaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationwebauthaction()
				addresource.name = resource.name
				addresource.serverip = resource.serverip
				addresource.serverport = resource.serverport
				addresource.fullreqexpr = resource.fullreqexpr
				addresource.scheme = resource.scheme
				addresource.successrule = resource.successrule
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				addresource.attribute1 = resource.attribute1
				addresource.attribute2 = resource.attribute2
				addresource.attribute3 = resource.attribute3
				addresource.attribute4 = resource.attribute4
				addresource.attribute5 = resource.attribute5
				addresource.attribute6 = resource.attribute6
				addresource.attribute7 = resource.attribute7
				addresource.attribute8 = resource.attribute8
				addresource.attribute9 = resource.attribute9
				addresource.attribute10 = resource.attribute10
				addresource.attribute11 = resource.attribute11
				addresource.attribute12 = resource.attribute12
				addresource.attribute13 = resource.attribute13
				addresource.attribute14 = resource.attribute14
				addresource.attribute15 = resource.attribute15
				addresource.attribute16 = resource.attribute16
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationwebauthaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].serverip = resource[i].serverip
						addresources[i].serverport = resource[i].serverport
						addresources[i].fullreqexpr = resource[i].fullreqexpr
						addresources[i].scheme = resource[i].scheme
						addresources[i].successrule = resource[i].successrule
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						addresources[i].attribute1 = resource[i].attribute1
						addresources[i].attribute2 = resource[i].attribute2
						addresources[i].attribute3 = resource[i].attribute3
						addresources[i].attribute4 = resource[i].attribute4
						addresources[i].attribute5 = resource[i].attribute5
						addresources[i].attribute6 = resource[i].attribute6
						addresources[i].attribute7 = resource[i].attribute7
						addresources[i].attribute8 = resource[i].attribute8
						addresources[i].attribute9 = resource[i].attribute9
						addresources[i].attribute10 = resource[i].attribute10
						addresources[i].attribute11 = resource[i].attribute11
						addresources[i].attribute12 = resource[i].attribute12
						addresources[i].attribute13 = resource[i].attribute13
						addresources[i].attribute14 = resource[i].attribute14
						addresources[i].attribute15 = resource[i].attribute15
						addresources[i].attribute16 = resource[i].attribute16
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete authenticationwebauthaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationwebauthaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationwebauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationwebauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update authenticationwebauthaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationwebauthaction()
				updateresource.name = resource.name
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.fullreqexpr = resource.fullreqexpr
				updateresource.scheme = resource.scheme
				updateresource.successrule = resource.successrule
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.attribute1 = resource.attribute1
				updateresource.attribute2 = resource.attribute2
				updateresource.attribute3 = resource.attribute3
				updateresource.attribute4 = resource.attribute4
				updateresource.attribute5 = resource.attribute5
				updateresource.attribute6 = resource.attribute6
				updateresource.attribute7 = resource.attribute7
				updateresource.attribute8 = resource.attribute8
				updateresource.attribute9 = resource.attribute9
				updateresource.attribute10 = resource.attribute10
				updateresource.attribute11 = resource.attribute11
				updateresource.attribute12 = resource.attribute12
				updateresource.attribute13 = resource.attribute13
				updateresource.attribute14 = resource.attribute14
				updateresource.attribute15 = resource.attribute15
				updateresource.attribute16 = resource.attribute16
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationwebauthaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].serverip = resource[i].serverip
						updateresources[i].serverport = resource[i].serverport
						updateresources[i].fullreqexpr = resource[i].fullreqexpr
						updateresources[i].scheme = resource[i].scheme
						updateresources[i].successrule = resource[i].successrule
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						updateresources[i].attribute1 = resource[i].attribute1
						updateresources[i].attribute2 = resource[i].attribute2
						updateresources[i].attribute3 = resource[i].attribute3
						updateresources[i].attribute4 = resource[i].attribute4
						updateresources[i].attribute5 = resource[i].attribute5
						updateresources[i].attribute6 = resource[i].attribute6
						updateresources[i].attribute7 = resource[i].attribute7
						updateresources[i].attribute8 = resource[i].attribute8
						updateresources[i].attribute9 = resource[i].attribute9
						updateresources[i].attribute10 = resource[i].attribute10
						updateresources[i].attribute11 = resource[i].attribute11
						updateresources[i].attribute12 = resource[i].attribute12
						updateresources[i].attribute13 = resource[i].attribute13
						updateresources[i].attribute14 = resource[i].attribute14
						updateresources[i].attribute15 = resource[i].attribute15
						updateresources[i].attribute16 = resource[i].attribute16
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of authenticationwebauthaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationwebauthaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationwebauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationwebauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the authenticationwebauthaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationwebauthaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = authenticationwebauthaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [authenticationwebauthaction() for _ in range(len(name))]
							obj = [authenticationwebauthaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = authenticationwebauthaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of authenticationwebauthaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationwebauthaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the authenticationwebauthaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationwebauthaction()
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
		ur""" Use this API to count filtered the set of authenticationwebauthaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationwebauthaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Scheme:
		http = "http"
		https = "https"

class authenticationwebauthaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationwebauthaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationwebauthaction = [authenticationwebauthaction() for _ in range(length)]

