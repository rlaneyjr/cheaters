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

class snmpmib(base_resource) :
	""" Configuration for SNMP mib resource. """
	def __init__(self) :
		self._contact = ""
		self._name = ""
		self._location = ""
		self._customid = ""
		self._sysdesc = ""
		self._sysuptime = 0
		self._sysservices = 0
		self._sysoid = ""

	@property
	def contact(self) :
		ur"""Name of the administrator for this NetScaler appliance. Along with the name, you can include information on how to contact this person, such as a phone number or an email address. Can consist of 1 to 127 characters that include uppercase and  lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the information includes one or more spaces, enclose it in double or single quotation marks (for example, "my contact" or 'my contact').<br/>Default value: "WebMaster (default)"<br/>Minimum length =  1.
		"""
		try :
			return self._contact
		except Exception as e:
			raise e

	@contact.setter
	def contact(self, contact) :
		ur"""Name of the administrator for this NetScaler appliance. Along with the name, you can include information on how to contact this person, such as a phone number or an email address. Can consist of 1 to 127 characters that include uppercase and  lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the information includes one or more spaces, enclose it in double or single quotation marks (for example, "my contact" or 'my contact').<br/>Default value: "WebMaster (default)"<br/>Minimum length =  1
		"""
		try :
			self._contact = contact
		except Exception as e:
			raise e

	@property
	def name(self) :
		ur"""Name for this NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You should choose a name that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my name" or 'my name').<br/>Default value: "NetScaler"<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for this NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You should choose a name that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose it in double or single quotation marks (for example, "my name" or 'my name').<br/>Default value: "NetScaler"<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def location(self) :
		ur"""Physical location of the NetScaler appliance. For example, you can specify building name, lab number, and rack number. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the location includes one or more spaces, enclose it in double or single quotation marks (for example, "my location" or 'my location').<br/>Default value: "POP (default)"<br/>Minimum length =  1.
		"""
		try :
			return self._location
		except Exception as e:
			raise e

	@location.setter
	def location(self, location) :
		ur"""Physical location of the NetScaler appliance. For example, you can specify building name, lab number, and rack number. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
		The following requirement applies only to the NetScaler CLI:
		If the location includes one or more spaces, enclose it in double or single quotation marks (for example, "my location" or 'my location').<br/>Default value: "POP (default)"<br/>Minimum length =  1
		"""
		try :
			self._location = location
		except Exception as e:
			raise e

	@property
	def customid(self) :
		ur"""Custom identification number for the NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a custom identification that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the ID includes one or more spaces, enclose it in double or single quotation marks (for example, "my ID" or 'my ID').<br/>Default value: "Default"<br/>Minimum length =  1.
		"""
		try :
			return self._customid
		except Exception as e:
			raise e

	@customid.setter
	def customid(self, customid) :
		ur"""Custom identification number for the NetScaler appliance. Can consist of 1 to 127 characters that include uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters. You should choose a custom identification that helps identify the NetScaler appliance.
		The following requirement applies only to the NetScaler CLI:
		If the ID includes one or more spaces, enclose it in double or single quotation marks (for example, "my ID" or 'my ID').<br/>Default value: "Default"<br/>Minimum length =  1
		"""
		try :
			self._customid = customid
		except Exception as e:
			raise e

	@property
	def sysdesc(self) :
		ur"""The description of the system.
		"""
		try :
			return self._sysdesc
		except Exception as e:
			raise e

	@property
	def sysuptime(self) :
		ur"""The UP time of the system in 100th of a second.
		"""
		try :
			return self._sysuptime
		except Exception as e:
			raise e

	@property
	def sysservices(self) :
		ur"""The services offered by the system.
		"""
		try :
			return self._sysservices
		except Exception as e:
			raise e

	@property
	def sysoid(self) :
		ur"""The OID of the system's management system.
		"""
		try :
			return self._sysoid
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmpmib_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmpmib
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update snmpmib.
		"""
		try :
			if type(resource) is not list :
				updateresource = snmpmib()
				updateresource.contact = resource.contact
				updateresource.name = resource.name
				updateresource.location = resource.location
				updateresource.customid = resource.customid
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of snmpmib resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = snmpmib()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the snmpmib resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = snmpmib()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class snmpmib_response(base_response) :
	def __init__(self, length=1) :
		self.snmpmib = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmpmib = [snmpmib() for _ in range(length)]

