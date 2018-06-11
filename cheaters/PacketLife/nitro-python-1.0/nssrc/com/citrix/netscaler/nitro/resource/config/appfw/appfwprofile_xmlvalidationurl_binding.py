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

class appfwprofile_xmlvalidationurl_binding(base_resource) :
	""" Binding class showing the xmlvalidationurl that can be bound to appfwprofile.
	"""
	def __init__(self) :
		self._xmlvalidationurl = ""
		self._xmlvalidateresponse = ""
		self._xmlwsdl = ""
		self._xmladditionalsoapheaders = ""
		self._xmlendpointcheck = ""
		self._xmlrequestschema = ""
		self._xmlresponseschema = ""
		self._xmlvalidatesoapenvelope = ""
		self._state = ""
		self._comment = ""
		self._name = ""
		self.___count = 0

	@property
	def state(self) :
		ur"""Enabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Enabled.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def xmlwsdl(self) :
		ur"""WSDL object for soap request validation.
		"""
		try :
			return self._xmlwsdl
		except Exception as e:
			raise e

	@xmlwsdl.setter
	def xmlwsdl(self, xmlwsdl) :
		ur"""WSDL object for soap request validation.
		"""
		try :
			self._xmlwsdl = xmlwsdl
		except Exception as e:
			raise e

	@property
	def xmlendpointcheck(self) :
		ur"""Modifies the behaviour of the Request URL validation w.r.t. the Service URL.
		If set to ABSOLUTE, the entire request URL is validated with the entire URL mentioned in Service of the associated WSDL.
		eg: Service URL: http://example.org/ExampleService, Request URL: http//example.com/ExampleService would FAIL the validation.
		If set to RELAIVE, only the non-hostname part of the request URL is validated against the non-hostname part of the Service URL.
		eg: Service URL: http://example.org/ExampleService, Request URL: http//example.com/ExampleService would PASS the validation.<br/>Possible values = ABSOLUTE, RELATIVE.
		"""
		try :
			return self._xmlendpointcheck
		except Exception as e:
			raise e

	@xmlendpointcheck.setter
	def xmlendpointcheck(self, xmlendpointcheck) :
		ur"""Modifies the behaviour of the Request URL validation w.r.t. the Service URL.
		If set to ABSOLUTE, the entire request URL is validated with the entire URL mentioned in Service of the associated WSDL.
		eg: Service URL: http://example.org/ExampleService, Request URL: http//example.com/ExampleService would FAIL the validation.
		If set to RELAIVE, only the non-hostname part of the request URL is validated against the non-hostname part of the Service URL.
		eg: Service URL: http://example.org/ExampleService, Request URL: http//example.com/ExampleService would PASS the validation.<br/>Possible values = ABSOLUTE, RELATIVE
		"""
		try :
			self._xmlendpointcheck = xmlendpointcheck
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def xmlvalidateresponse(self) :
		ur"""Validate response message.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlvalidateresponse
		except Exception as e:
			raise e

	@xmlvalidateresponse.setter
	def xmlvalidateresponse(self, xmlvalidateresponse) :
		ur"""Validate response message.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlvalidateresponse = xmlvalidateresponse
		except Exception as e:
			raise e

	@property
	def xmlvalidationurl(self) :
		ur"""XML Validation URL regular expression.
		"""
		try :
			return self._xmlvalidationurl
		except Exception as e:
			raise e

	@xmlvalidationurl.setter
	def xmlvalidationurl(self, xmlvalidationurl) :
		ur"""XML Validation URL regular expression.
		"""
		try :
			self._xmlvalidationurl = xmlvalidationurl
		except Exception as e:
			raise e

	@property
	def xmlresponseschema(self) :
		ur"""XML Schema object for response validation.
		"""
		try :
			return self._xmlresponseschema
		except Exception as e:
			raise e

	@xmlresponseschema.setter
	def xmlresponseschema(self, xmlresponseschema) :
		ur"""XML Schema object for response validation.
		"""
		try :
			self._xmlresponseschema = xmlresponseschema
		except Exception as e:
			raise e

	@property
	def xmlvalidatesoapenvelope(self) :
		ur"""Validate SOAP Evelope only.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlvalidatesoapenvelope
		except Exception as e:
			raise e

	@xmlvalidatesoapenvelope.setter
	def xmlvalidatesoapenvelope(self, xmlvalidatesoapenvelope) :
		ur"""Validate SOAP Evelope only.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlvalidatesoapenvelope = xmlvalidatesoapenvelope
		except Exception as e:
			raise e

	@property
	def xmlrequestschema(self) :
		ur"""XML Schema object for request validation .
		"""
		try :
			return self._xmlrequestschema
		except Exception as e:
			raise e

	@xmlrequestschema.setter
	def xmlrequestschema(self, xmlrequestschema) :
		ur"""XML Schema object for request validation .
		"""
		try :
			self._xmlrequestschema = xmlrequestschema
		except Exception as e:
			raise e

	@property
	def xmladditionalsoapheaders(self) :
		ur"""Allow addtional soap headers.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmladditionalsoapheaders
		except Exception as e:
			raise e

	@xmladditionalsoapheaders.setter
	def xmladditionalsoapheaders(self, xmladditionalsoapheaders) :
		ur"""Allow addtional soap headers.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmladditionalsoapheaders = xmladditionalsoapheaders
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_xmlvalidationurl_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_xmlvalidationurl_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = appfwprofile_xmlvalidationurl_binding()
				updateresource.name = resource.name
				updateresource.comment = resource.comment
				updateresource.state = resource.state
				updateresource.xmlvalidationurl = resource.xmlvalidationurl
				updateresource.xmlrequestschema = resource.xmlrequestschema
				updateresource.xmlresponseschema = resource.xmlresponseschema
				updateresource.xmlwsdl = resource.xmlwsdl
				updateresource.xmladditionalsoapheaders = resource.xmladditionalsoapheaders
				updateresource.xmlendpointcheck = resource.xmlendpointcheck
				updateresource.xmlvalidatesoapenvelope = resource.xmlvalidatesoapenvelope
				updateresource.xmlvalidateresponse = resource.xmlvalidateresponse
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [appfwprofile_xmlvalidationurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].comment = resource[i].comment
						updateresources[i].state = resource[i].state
						updateresources[i].xmlvalidationurl = resource[i].xmlvalidationurl
						updateresources[i].xmlrequestschema = resource[i].xmlrequestschema
						updateresources[i].xmlresponseschema = resource[i].xmlresponseschema
						updateresources[i].xmlwsdl = resource[i].xmlwsdl
						updateresources[i].xmladditionalsoapheaders = resource[i].xmladditionalsoapheaders
						updateresources[i].xmlendpointcheck = resource[i].xmlendpointcheck
						updateresources[i].xmlvalidatesoapenvelope = resource[i].xmlvalidatesoapenvelope
						updateresources[i].xmlvalidateresponse = resource[i].xmlvalidateresponse
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = appfwprofile_xmlvalidationurl_binding()
				deleteresource.name = resource.name
				deleteresource.xmlvalidationurl = resource.xmlvalidationurl
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [appfwprofile_xmlvalidationurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].xmlvalidationurl = resource[i].xmlvalidationurl
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch appfwprofile_xmlvalidationurl_binding resources.
		"""
		try :
			obj = appfwprofile_xmlvalidationurl_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of appfwprofile_xmlvalidationurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmlvalidationurl_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count appfwprofile_xmlvalidationurl_binding resources configued on NetScaler.
		"""
		try :
			obj = appfwprofile_xmlvalidationurl_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of appfwprofile_xmlvalidationurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmlvalidationurl_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class As_scan_location_xmlsql:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Xmlmaxelementdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattachmentsizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlsoaparraycheck:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Xmlmaxelementnamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_ff:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxelementscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlendpointcheck:
		ABSOLUTE = "ABSOLUTE"
		RELATIVE = "RELATIVE"

	class Xmlmaxnamespacescheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributenamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlblockdtd:
		ON = "ON"
		OFF = "OFF"

	class Xmlblockpi:
		ON = "ON"
		OFF = "OFF"

	class Isregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxelementchildrencheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlvalidateresponse:
		ON = "ON"
		OFF = "OFF"

	class Isregex:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxentityexpansionscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnamespaceurilengthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xss:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Xmlmaxentityexpansiondepthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xmlxss:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Xmlmaxattributevaluelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_sql:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Isregex_ffc:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlattachmentcontenttypecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xmlsql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidatesoapenvelope:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxchardatalengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlminfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Isregex_xmlxss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmladditionalsoapheaders:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributescheck:
		ON = "ON"
		OFF = "OFF"

	class Action:
		none = "none"
		block = "block"
		log = "log"
		remove = "remove"
		stats = "stats"
		xout = "xout"

	class Xmlblockexternalentities:
		ON = "ON"
		OFF = "OFF"

class appfwprofile_xmlvalidationurl_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_xmlvalidationurl_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_xmlvalidationurl_binding = [appfwprofile_xmlvalidationurl_binding() for _ in range(length)]

