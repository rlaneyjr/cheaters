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

class appfwprofile_fieldformat_binding(base_resource) :
	""" Binding class showing the fieldformat that can be bound to appfwprofile.
	"""
	def __init__(self) :
		self._fieldformat = ""
		self._isregex_ff = ""
		self._formactionurl_ff = ""
		self._fieldtype = ""
		self._fieldformatminlength = 0
		self._fieldformatmaxlength = 0
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
	def fieldformatmaxlength(self) :
		ur"""The maximum allowed length for data in this form field.
		"""
		try :
			return self._fieldformatmaxlength
		except Exception as e:
			raise e

	@fieldformatmaxlength.setter
	def fieldformatmaxlength(self, fieldformatmaxlength) :
		ur"""The maximum allowed length for data in this form field.
		"""
		try :
			self._fieldformatmaxlength = fieldformatmaxlength
		except Exception as e:
			raise e

	@property
	def isregex_ff(self) :
		ur"""Is the form field name a regular expression?.<br/>Possible values = REGEX, NOTREGEX.
		"""
		try :
			return self._isregex_ff
		except Exception as e:
			raise e

	@isregex_ff.setter
	def isregex_ff(self, isregex_ff) :
		ur"""Is the form field name a regular expression?.<br/>Possible values = REGEX, NOTREGEX
		"""
		try :
			self._isregex_ff = isregex_ff
		except Exception as e:
			raise e

	@property
	def fieldtype(self) :
		ur"""The field type you are assigning to this form field.
		"""
		try :
			return self._fieldtype
		except Exception as e:
			raise e

	@fieldtype.setter
	def fieldtype(self, fieldtype) :
		ur"""The field type you are assigning to this form field.
		"""
		try :
			self._fieldtype = fieldtype
		except Exception as e:
			raise e

	@property
	def formactionurl_ff(self) :
		ur"""Action URL of the form field to which a field format will be assigned.
		"""
		try :
			return self._formactionurl_ff
		except Exception as e:
			raise e

	@formactionurl_ff.setter
	def formactionurl_ff(self, formactionurl_ff) :
		ur"""Action URL of the form field to which a field format will be assigned.
		"""
		try :
			self._formactionurl_ff = formactionurl_ff
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
	def fieldformatminlength(self) :
		ur"""The minimum allowed length for data in this form field.
		"""
		try :
			return self._fieldformatminlength
		except Exception as e:
			raise e

	@fieldformatminlength.setter
	def fieldformatminlength(self, fieldformatminlength) :
		ur"""The minimum allowed length for data in this form field.
		"""
		try :
			self._fieldformatminlength = fieldformatminlength
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

	@property
	def fieldformat(self) :
		ur"""Name of the form field to which a field format will be assigned.
		"""
		try :
			return self._fieldformat
		except Exception as e:
			raise e

	@fieldformat.setter
	def fieldformat(self, fieldformat) :
		ur"""Name of the form field to which a field format will be assigned.
		"""
		try :
			self._fieldformat = fieldformat
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_fieldformat_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_fieldformat_binding
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
				updateresource = appfwprofile_fieldformat_binding()
				updateresource.name = resource.name
				updateresource.fieldformat = resource.fieldformat
				updateresource.formactionurl_ff = resource.formactionurl_ff
				updateresource.fieldtype = resource.fieldtype
				updateresource.fieldformatminlength = resource.fieldformatminlength
				updateresource.fieldformatmaxlength = resource.fieldformatmaxlength
				updateresource.isregex_ff = resource.isregex_ff
				updateresource.comment = resource.comment
				updateresource.state = resource.state
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [appfwprofile_fieldformat_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].fieldformat = resource[i].fieldformat
						updateresources[i].formactionurl_ff = resource[i].formactionurl_ff
						updateresources[i].fieldtype = resource[i].fieldtype
						updateresources[i].fieldformatminlength = resource[i].fieldformatminlength
						updateresources[i].fieldformatmaxlength = resource[i].fieldformatmaxlength
						updateresources[i].isregex_ff = resource[i].isregex_ff
						updateresources[i].comment = resource[i].comment
						updateresources[i].state = resource[i].state
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = appfwprofile_fieldformat_binding()
				deleteresource.name = resource.name
				deleteresource.fieldformat = resource.fieldformat
				deleteresource.formactionurl_ff = resource.formactionurl_ff
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [appfwprofile_fieldformat_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].fieldformat = resource[i].fieldformat
						deleteresources[i].formactionurl_ff = resource[i].formactionurl_ff
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch appfwprofile_fieldformat_binding resources.
		"""
		try :
			obj = appfwprofile_fieldformat_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of appfwprofile_fieldformat_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_fieldformat_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count appfwprofile_fieldformat_binding resources configued on NetScaler.
		"""
		try :
			obj = appfwprofile_fieldformat_binding()
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
		ur""" Use this API to count the filtered set of appfwprofile_fieldformat_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_fieldformat_binding()
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

	class Xmlvalidateresponse:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementchildrencheck:
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

class appfwprofile_fieldformat_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_fieldformat_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_fieldformat_binding = [appfwprofile_fieldformat_binding() for _ in range(length)]

