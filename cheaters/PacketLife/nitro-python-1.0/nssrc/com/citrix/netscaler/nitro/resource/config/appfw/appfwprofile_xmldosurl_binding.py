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

class appfwprofile_xmldosurl_binding(base_resource) :
	""" Binding class showing the xmldosurl that can be bound to appfwprofile.
	"""
	def __init__(self) :
		self._xmldosurl = ""
		self._xmlmaxelementdepthcheck = ""
		self._xmlmaxelementdepth = 0
		self._xmlmaxelementnamelengthcheck = ""
		self._xmlmaxelementnamelength = 0
		self._xmlmaxelementscheck = ""
		self._xmlmaxelements = 0
		self._xmlmaxelementchildrencheck = ""
		self._xmlmaxelementchildren = 0
		self._xmlmaxelementchildren = 0
		self._xmlmaxnodescheck = ""
		self._xmlmaxnodes = 0
		self._xmlmaxentityexpansionscheck = ""
		self._xmlmaxentityexpansions = 0
		self._xmlmaxentityexpansiondepthcheck = ""
		self._xmlmaxentityexpansiondepth = 0
		self._xmlmaxattributescheck = ""
		self._xmlmaxattributes = 0
		self._xmlmaxattributenamelengthcheck = ""
		self._xmlmaxattributenamelength = 0
		self._xmlmaxattributevaluelengthcheck = ""
		self._xmlmaxattributevaluelength = 0
		self._xmlmaxnamespacescheck = ""
		self._xmlmaxnamespaces = 0
		self._xmlmaxnamespaceurilengthcheck = ""
		self._xmlmaxnamespaceurilength = 0
		self._xmlmaxchardatalengthcheck = ""
		self._xmlmaxchardatalength = 0
		self._xmlmaxfilesizecheck = ""
		self._xmlmaxfilesize = 0
		self._xmlminfilesizecheck = ""
		self._xmlminfilesize = 0
		self._xmlblockpi = ""
		self._xmlblockdtd = ""
		self._xmlblockexternalentities = ""
		self._xmlsoaparraycheck = ""
		self._xmlmaxsoaparraysize = 0
		self._xmlmaxsoaparrayrank = 0
		self._state = ""
		self._comment = ""
		self._name = ""
		self.___count = 0

	@property
	def xmlmaxelementdepthcheck(self) :
		ur"""State if XML Max element depth check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementdepthcheck
		except Exception as e:
			raise e

	@xmlmaxelementdepthcheck.setter
	def xmlmaxelementdepthcheck(self, xmlmaxelementdepthcheck) :
		ur"""State if XML Max element depth check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementdepthcheck = xmlmaxelementdepthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxfilesize(self) :
		ur"""Specify the maximum size of XML messages. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxfilesize
		except Exception as e:
			raise e

	@xmlmaxfilesize.setter
	def xmlmaxfilesize(self, xmlmaxfilesize) :
		ur"""Specify the maximum size of XML messages. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxfilesize = xmlmaxfilesize
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespaceurilength(self) :
		ur"""Specify the longest URI of any XML namespace. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxnamespaceurilength
		except Exception as e:
			raise e

	@xmlmaxnamespaceurilength.setter
	def xmlmaxnamespaceurilength(self, xmlmaxnamespaceurilength) :
		ur"""Specify the longest URI of any XML namespace. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxnamespaceurilength = xmlmaxnamespaceurilength
		except Exception as e:
			raise e

	@property
	def xmldosurl(self) :
		ur"""XML DoS URL regular expression length.
		"""
		try :
			return self._xmldosurl
		except Exception as e:
			raise e

	@xmldosurl.setter
	def xmldosurl(self, xmldosurl) :
		ur"""XML DoS URL regular expression length.
		"""
		try :
			self._xmldosurl = xmldosurl
		except Exception as e:
			raise e

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
	def xmlsoaparraycheck(self) :
		ur"""State if XML SOAP Array check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlsoaparraycheck
		except Exception as e:
			raise e

	@xmlsoaparraycheck.setter
	def xmlsoaparraycheck(self, xmlsoaparraycheck) :
		ur"""State if XML SOAP Array check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlsoaparraycheck = xmlsoaparraycheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelementnamelengthcheck(self) :
		ur"""State if XML Max element name length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementnamelengthcheck
		except Exception as e:
			raise e

	@xmlmaxelementnamelengthcheck.setter
	def xmlmaxelementnamelengthcheck(self, xmlmaxelementnamelengthcheck) :
		ur"""State if XML Max element name length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementnamelengthcheck = xmlmaxelementnamelengthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelementscheck(self) :
		ur"""State if XML Max elements check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementscheck
		except Exception as e:
			raise e

	@xmlmaxelementscheck.setter
	def xmlmaxelementscheck(self, xmlmaxelementscheck) :
		ur"""State if XML Max elements check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementscheck = xmlmaxelementscheck
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansions(self) :
		ur"""Specify maximum allowed number of entity expansions. Protects aganist Entity Expansion Attack.
		"""
		try :
			return self._xmlmaxentityexpansions
		except Exception as e:
			raise e

	@xmlmaxentityexpansions.setter
	def xmlmaxentityexpansions(self, xmlmaxentityexpansions) :
		ur"""Specify maximum allowed number of entity expansions. Protects aganist Entity Expansion Attack.
		"""
		try :
			self._xmlmaxentityexpansions = xmlmaxentityexpansions
		except Exception as e:
			raise e

	@property
	def xmlmaxattributes(self) :
		ur"""Specify maximum number of attributes per XML element. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxattributes
		except Exception as e:
			raise e

	@xmlmaxattributes.setter
	def xmlmaxattributes(self, xmlmaxattributes) :
		ur"""Specify maximum number of attributes per XML element. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxattributes = xmlmaxattributes
		except Exception as e:
			raise e

	@property
	def xmlmaxfilesizecheck(self) :
		ur"""State if XML Max file size check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxfilesizecheck
		except Exception as e:
			raise e

	@xmlmaxfilesizecheck.setter
	def xmlmaxfilesizecheck(self, xmlmaxfilesizecheck) :
		ur"""State if XML Max file size check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxfilesizecheck = xmlmaxfilesizecheck
		except Exception as e:
			raise e

	@property
	def xmlmaxchardatalength(self) :
		ur"""Specify the maximum size of CDATA. Protects against overflow attacks and large quantities of unparsed data within XML messages.
		"""
		try :
			return self._xmlmaxchardatalength
		except Exception as e:
			raise e

	@xmlmaxchardatalength.setter
	def xmlmaxchardatalength(self, xmlmaxchardatalength) :
		ur"""Specify the maximum size of CDATA. Protects against overflow attacks and large quantities of unparsed data within XML messages.
		"""
		try :
			self._xmlmaxchardatalength = xmlmaxchardatalength
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespacescheck(self) :
		ur"""State if XML Max namespaces check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxnamespacescheck
		except Exception as e:
			raise e

	@xmlmaxnamespacescheck.setter
	def xmlmaxnamespacescheck(self, xmlmaxnamespacescheck) :
		ur"""State if XML Max namespaces check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxnamespacescheck = xmlmaxnamespacescheck
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespaces(self) :
		ur"""Specify maximum number of active namespaces. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxnamespaces
		except Exception as e:
			raise e

	@xmlmaxnamespaces.setter
	def xmlmaxnamespaces(self, xmlmaxnamespaces) :
		ur"""Specify maximum number of active namespaces. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxnamespaces = xmlmaxnamespaces
		except Exception as e:
			raise e

	@property
	def xmlmaxattributenamelengthcheck(self) :
		ur"""State if XML Max attribute name length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxattributenamelengthcheck
		except Exception as e:
			raise e

	@xmlmaxattributenamelengthcheck.setter
	def xmlmaxattributenamelengthcheck(self, xmlmaxattributenamelengthcheck) :
		ur"""State if XML Max attribute name length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxattributenamelengthcheck = xmlmaxattributenamelengthcheck
		except Exception as e:
			raise e

	@property
	def xmlblockdtd(self) :
		ur"""State if XML DTD is ON or OFF. Protects against recursive Document Type Declaration (DTD) entity expansion attacks. Also, SOAP messages cannot have DTDs in messages. .<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlblockdtd
		except Exception as e:
			raise e

	@xmlblockdtd.setter
	def xmlblockdtd(self, xmlblockdtd) :
		ur"""State if XML DTD is ON or OFF. Protects against recursive Document Type Declaration (DTD) entity expansion attacks. Also, SOAP messages cannot have DTDs in messages. .<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlblockdtd = xmlblockdtd
		except Exception as e:
			raise e

	@property
	def xmlmaxattributevaluelength(self) :
		ur"""Specify the longest value of any XML attribute. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxattributevaluelength
		except Exception as e:
			raise e

	@xmlmaxattributevaluelength.setter
	def xmlmaxattributevaluelength(self, xmlmaxattributevaluelength) :
		ur"""Specify the longest value of any XML attribute. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxattributevaluelength = xmlmaxattributevaluelength
		except Exception as e:
			raise e

	@property
	def xmlmaxelementdepth(self) :
		ur"""Maximum nesting (depth) of XML elements. This check protects against documents that have excessive hierarchy depths.
		"""
		try :
			return self._xmlmaxelementdepth
		except Exception as e:
			raise e

	@xmlmaxelementdepth.setter
	def xmlmaxelementdepth(self, xmlmaxelementdepth) :
		ur"""Maximum nesting (depth) of XML elements. This check protects against documents that have excessive hierarchy depths.
		"""
		try :
			self._xmlmaxelementdepth = xmlmaxelementdepth
		except Exception as e:
			raise e

	@property
	def xmlmaxelementnamelength(self) :
		ur"""Specify the longest name of any element (including the expanded namespace) to protect against overflow attacks.
		"""
		try :
			return self._xmlmaxelementnamelength
		except Exception as e:
			raise e

	@xmlmaxelementnamelength.setter
	def xmlmaxelementnamelength(self, xmlmaxelementnamelength) :
		ur"""Specify the longest name of any element (including the expanded namespace) to protect against overflow attacks.
		"""
		try :
			self._xmlmaxelementnamelength = xmlmaxelementnamelength
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
	def xmlblockpi(self) :
		ur"""State if XML Block PI is ON or OFF. Protects resources from denial of service attacks as SOAP messages cannot have processing instructions (PI) in messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlblockpi
		except Exception as e:
			raise e

	@xmlblockpi.setter
	def xmlblockpi(self, xmlblockpi) :
		ur"""State if XML Block PI is ON or OFF. Protects resources from denial of service attacks as SOAP messages cannot have processing instructions (PI) in messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlblockpi = xmlblockpi
		except Exception as e:
			raise e

	@property
	def xmlmaxelementchildrencheck(self) :
		ur"""State if XML Max element children check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementchildrencheck
		except Exception as e:
			raise e

	@xmlmaxelementchildrencheck.setter
	def xmlmaxelementchildrencheck(self, xmlmaxelementchildrencheck) :
		ur"""State if XML Max element children check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementchildrencheck = xmlmaxelementchildrencheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelements(self) :
		ur"""Specify the maximum number of XML elements allowed. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxelements
		except Exception as e:
			raise e

	@xmlmaxelements.setter
	def xmlmaxelements(self, xmlmaxelements) :
		ur"""Specify the maximum number of XML elements allowed. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxelements = xmlmaxelements
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansionscheck(self) :
		ur"""State if XML Max Entity Expansions Check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxentityexpansionscheck
		except Exception as e:
			raise e

	@xmlmaxentityexpansionscheck.setter
	def xmlmaxentityexpansionscheck(self, xmlmaxentityexpansionscheck) :
		ur"""State if XML Max Entity Expansions Check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxentityexpansionscheck = xmlmaxentityexpansionscheck
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespaceurilengthcheck(self) :
		ur"""State if XML Max namespace URI length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxnamespaceurilengthcheck
		except Exception as e:
			raise e

	@xmlmaxnamespaceurilengthcheck.setter
	def xmlmaxnamespaceurilengthcheck(self, xmlmaxnamespaceurilengthcheck) :
		ur"""State if XML Max namespace URI length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxnamespaceurilengthcheck = xmlmaxnamespaceurilengthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansiondepthcheck(self) :
		ur"""State if XML Max Entity Expansions Depth Check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxentityexpansiondepthcheck
		except Exception as e:
			raise e

	@xmlmaxentityexpansiondepthcheck.setter
	def xmlmaxentityexpansiondepthcheck(self, xmlmaxentityexpansiondepthcheck) :
		ur"""State if XML Max Entity Expansions Depth Check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxentityexpansiondepthcheck = xmlmaxentityexpansiondepthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxattributevaluelengthcheck(self) :
		ur"""State if XML Max atribute value length is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxattributevaluelengthcheck
		except Exception as e:
			raise e

	@xmlmaxattributevaluelengthcheck.setter
	def xmlmaxattributevaluelengthcheck(self, xmlmaxattributevaluelengthcheck) :
		ur"""State if XML Max atribute value length is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxattributevaluelengthcheck = xmlmaxattributevaluelengthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxsoaparraysize(self) :
		ur"""XML Max Total SOAP Array Size. Protects against SOAP Array Abuse attack.
		"""
		try :
			return self._xmlmaxsoaparraysize
		except Exception as e:
			raise e

	@xmlmaxsoaparraysize.setter
	def xmlmaxsoaparraysize(self, xmlmaxsoaparraysize) :
		ur"""XML Max Total SOAP Array Size. Protects against SOAP Array Abuse attack.
		"""
		try :
			self._xmlmaxsoaparraysize = xmlmaxsoaparraysize
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansiondepth(self) :
		ur"""Specify maximum entity expansion depth. Protects aganist Entity Expansion Attack.
		"""
		try :
			return self._xmlmaxentityexpansiondepth
		except Exception as e:
			raise e

	@xmlmaxentityexpansiondepth.setter
	def xmlmaxentityexpansiondepth(self, xmlmaxentityexpansiondepth) :
		ur"""Specify maximum entity expansion depth. Protects aganist Entity Expansion Attack.
		"""
		try :
			self._xmlmaxentityexpansiondepth = xmlmaxentityexpansiondepth
		except Exception as e:
			raise e

	@property
	def xmlmaxnodescheck(self) :
		ur"""State if XML Max nodes check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxnodescheck
		except Exception as e:
			raise e

	@xmlmaxnodescheck.setter
	def xmlmaxnodescheck(self, xmlmaxnodescheck) :
		ur"""State if XML Max nodes check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxnodescheck = xmlmaxnodescheck
		except Exception as e:
			raise e

	@property
	def xmlmaxattributenamelength(self) :
		ur"""Specify the longest name of any XML attribute. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxattributenamelength
		except Exception as e:
			raise e

	@xmlmaxattributenamelength.setter
	def xmlmaxattributenamelength(self, xmlmaxattributenamelength) :
		ur"""Specify the longest name of any XML attribute. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxattributenamelength = xmlmaxattributenamelength
		except Exception as e:
			raise e

	@property
	def xmlmaxchardatalengthcheck(self) :
		ur"""State if XML Max CDATA length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxchardatalengthcheck
		except Exception as e:
			raise e

	@xmlmaxchardatalengthcheck.setter
	def xmlmaxchardatalengthcheck(self, xmlmaxchardatalengthcheck) :
		ur"""State if XML Max CDATA length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxchardatalengthcheck = xmlmaxchardatalengthcheck
		except Exception as e:
			raise e

	@property
	def xmlminfilesizecheck(self) :
		ur"""State if XML Min file size check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlminfilesizecheck
		except Exception as e:
			raise e

	@xmlminfilesizecheck.setter
	def xmlminfilesizecheck(self, xmlminfilesizecheck) :
		ur"""State if XML Min file size check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlminfilesizecheck = xmlminfilesizecheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelementchildren(self) :
		ur"""Specify the maximum number of children allowed per XML element. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxelementchildren
		except Exception as e:
			raise e

	@xmlmaxelementchildren.setter
	def xmlmaxelementchildren(self, xmlmaxelementchildren) :
		ur"""Specify the maximum number of children allowed per XML element. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxelementchildren = xmlmaxelementchildren
		except Exception as e:
			raise e

	@property
	def xmlminfilesize(self) :
		ur"""Enforces minimum message size.
		"""
		try :
			return self._xmlminfilesize
		except Exception as e:
			raise e

	@xmlminfilesize.setter
	def xmlminfilesize(self, xmlminfilesize) :
		ur"""Enforces minimum message size.
		"""
		try :
			self._xmlminfilesize = xmlminfilesize
		except Exception as e:
			raise e

	@property
	def xmlmaxnodes(self) :
		ur"""Specify the maximum number of XML nodes. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxnodes
		except Exception as e:
			raise e

	@xmlmaxnodes.setter
	def xmlmaxnodes(self, xmlmaxnodes) :
		ur"""Specify the maximum number of XML nodes. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxnodes = xmlmaxnodes
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
	def xmlmaxattributescheck(self) :
		ur"""State if XML Max attributes check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxattributescheck
		except Exception as e:
			raise e

	@xmlmaxattributescheck.setter
	def xmlmaxattributescheck(self, xmlmaxattributescheck) :
		ur"""State if XML Max attributes check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxattributescheck = xmlmaxattributescheck
		except Exception as e:
			raise e

	@property
	def xmlmaxsoaparrayrank(self) :
		ur"""XML Max Individual SOAP Array Rank. This is the dimension of the SOAP array.
		"""
		try :
			return self._xmlmaxsoaparrayrank
		except Exception as e:
			raise e

	@xmlmaxsoaparrayrank.setter
	def xmlmaxsoaparrayrank(self, xmlmaxsoaparrayrank) :
		ur"""XML Max Individual SOAP Array Rank. This is the dimension of the SOAP array.
		"""
		try :
			self._xmlmaxsoaparrayrank = xmlmaxsoaparrayrank
		except Exception as e:
			raise e

	@property
	def xmlblockexternalentities(self) :
		ur"""State if XML Block External Entities Check is ON or OFF. Protects against XML External Entity (XXE) attacks that force applications to parse untrusted external entities (sources) in XML documents.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlblockexternalentities
		except Exception as e:
			raise e

	@xmlblockexternalentities.setter
	def xmlblockexternalentities(self, xmlblockexternalentities) :
		ur"""State if XML Block External Entities Check is ON or OFF. Protects against XML External Entity (XXE) attacks that force applications to parse untrusted external entities (sources) in XML documents.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlblockexternalentities = xmlblockexternalentities
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_xmldosurl_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_xmldosurl_binding
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
				updateresource = appfwprofile_xmldosurl_binding()
				updateresource.name = resource.name
				updateresource.comment = resource.comment
				updateresource.state = resource.state
				updateresource.xmldosurl = resource.xmldosurl
				updateresource.xmlmaxelementdepthcheck = resource.xmlmaxelementdepthcheck
				updateresource.xmlmaxelementdepth = resource.xmlmaxelementdepth
				updateresource.xmlmaxelementnamelengthcheck = resource.xmlmaxelementnamelengthcheck
				updateresource.xmlmaxelementnamelength = resource.xmlmaxelementnamelength
				updateresource.xmlmaxelementscheck = resource.xmlmaxelementscheck
				updateresource.xmlmaxelements = resource.xmlmaxelements
				updateresource.xmlmaxelementchildrencheck = resource.xmlmaxelementchildrencheck
				updateresource.xmlmaxelementchildren = resource.xmlmaxelementchildren
				updateresource.xmlmaxattributescheck = resource.xmlmaxattributescheck
				updateresource.xmlmaxattributes = resource.xmlmaxattributes
				updateresource.xmlmaxattributenamelengthcheck = resource.xmlmaxattributenamelengthcheck
				updateresource.xmlmaxattributenamelength = resource.xmlmaxattributenamelength
				updateresource.xmlmaxattributevaluelengthcheck = resource.xmlmaxattributevaluelengthcheck
				updateresource.xmlmaxattributevaluelength = resource.xmlmaxattributevaluelength
				updateresource.xmlmaxchardatalengthcheck = resource.xmlmaxchardatalengthcheck
				updateresource.xmlmaxchardatalength = resource.xmlmaxchardatalength
				updateresource.xmlmaxfilesizecheck = resource.xmlmaxfilesizecheck
				updateresource.xmlmaxfilesize = resource.xmlmaxfilesize
				updateresource.xmlminfilesizecheck = resource.xmlminfilesizecheck
				updateresource.xmlminfilesize = resource.xmlminfilesize
				updateresource.xmlblockpi = resource.xmlblockpi
				updateresource.xmlblockdtd = resource.xmlblockdtd
				updateresource.xmlblockexternalentities = resource.xmlblockexternalentities
				updateresource.xmlmaxentityexpansionscheck = resource.xmlmaxentityexpansionscheck
				updateresource.xmlmaxentityexpansions = resource.xmlmaxentityexpansions
				updateresource.xmlmaxentityexpansiondepthcheck = resource.xmlmaxentityexpansiondepthcheck
				updateresource.xmlmaxentityexpansiondepth = resource.xmlmaxentityexpansiondepth
				updateresource.xmlmaxnamespacescheck = resource.xmlmaxnamespacescheck
				updateresource.xmlmaxnamespaces = resource.xmlmaxnamespaces
				updateresource.xmlmaxnamespaceurilengthcheck = resource.xmlmaxnamespaceurilengthcheck
				updateresource.xmlmaxnamespaceurilength = resource.xmlmaxnamespaceurilength
				updateresource.xmlsoaparraycheck = resource.xmlsoaparraycheck
				updateresource.xmlmaxsoaparraysize = resource.xmlmaxsoaparraysize
				updateresource.xmlmaxsoaparrayrank = resource.xmlmaxsoaparrayrank
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [appfwprofile_xmldosurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].comment = resource[i].comment
						updateresources[i].state = resource[i].state
						updateresources[i].xmldosurl = resource[i].xmldosurl
						updateresources[i].xmlmaxelementdepthcheck = resource[i].xmlmaxelementdepthcheck
						updateresources[i].xmlmaxelementdepth = resource[i].xmlmaxelementdepth
						updateresources[i].xmlmaxelementnamelengthcheck = resource[i].xmlmaxelementnamelengthcheck
						updateresources[i].xmlmaxelementnamelength = resource[i].xmlmaxelementnamelength
						updateresources[i].xmlmaxelementscheck = resource[i].xmlmaxelementscheck
						updateresources[i].xmlmaxelements = resource[i].xmlmaxelements
						updateresources[i].xmlmaxelementchildrencheck = resource[i].xmlmaxelementchildrencheck
						updateresources[i].xmlmaxelementchildren = resource[i].xmlmaxelementchildren
						updateresources[i].xmlmaxattributescheck = resource[i].xmlmaxattributescheck
						updateresources[i].xmlmaxattributes = resource[i].xmlmaxattributes
						updateresources[i].xmlmaxattributenamelengthcheck = resource[i].xmlmaxattributenamelengthcheck
						updateresources[i].xmlmaxattributenamelength = resource[i].xmlmaxattributenamelength
						updateresources[i].xmlmaxattributevaluelengthcheck = resource[i].xmlmaxattributevaluelengthcheck
						updateresources[i].xmlmaxattributevaluelength = resource[i].xmlmaxattributevaluelength
						updateresources[i].xmlmaxchardatalengthcheck = resource[i].xmlmaxchardatalengthcheck
						updateresources[i].xmlmaxchardatalength = resource[i].xmlmaxchardatalength
						updateresources[i].xmlmaxfilesizecheck = resource[i].xmlmaxfilesizecheck
						updateresources[i].xmlmaxfilesize = resource[i].xmlmaxfilesize
						updateresources[i].xmlminfilesizecheck = resource[i].xmlminfilesizecheck
						updateresources[i].xmlminfilesize = resource[i].xmlminfilesize
						updateresources[i].xmlblockpi = resource[i].xmlblockpi
						updateresources[i].xmlblockdtd = resource[i].xmlblockdtd
						updateresources[i].xmlblockexternalentities = resource[i].xmlblockexternalentities
						updateresources[i].xmlmaxentityexpansionscheck = resource[i].xmlmaxentityexpansionscheck
						updateresources[i].xmlmaxentityexpansions = resource[i].xmlmaxentityexpansions
						updateresources[i].xmlmaxentityexpansiondepthcheck = resource[i].xmlmaxentityexpansiondepthcheck
						updateresources[i].xmlmaxentityexpansiondepth = resource[i].xmlmaxentityexpansiondepth
						updateresources[i].xmlmaxnamespacescheck = resource[i].xmlmaxnamespacescheck
						updateresources[i].xmlmaxnamespaces = resource[i].xmlmaxnamespaces
						updateresources[i].xmlmaxnamespaceurilengthcheck = resource[i].xmlmaxnamespaceurilengthcheck
						updateresources[i].xmlmaxnamespaceurilength = resource[i].xmlmaxnamespaceurilength
						updateresources[i].xmlsoaparraycheck = resource[i].xmlsoaparraycheck
						updateresources[i].xmlmaxsoaparraysize = resource[i].xmlmaxsoaparraysize
						updateresources[i].xmlmaxsoaparrayrank = resource[i].xmlmaxsoaparrayrank
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = appfwprofile_xmldosurl_binding()
				deleteresource.name = resource.name
				deleteresource.xmldosurl = resource.xmldosurl
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [appfwprofile_xmldosurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].name = resource[i].name
						deleteresources[i].xmldosurl = resource[i].xmldosurl
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name) :
		ur""" Use this API to fetch appfwprofile_xmldosurl_binding resources.
		"""
		try :
			obj = appfwprofile_xmldosurl_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of appfwprofile_xmldosurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmldosurl_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count appfwprofile_xmldosurl_binding resources configued on NetScaler.
		"""
		try :
			obj = appfwprofile_xmldosurl_binding()
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
		ur""" Use this API to count the filtered set of appfwprofile_xmldosurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmldosurl_binding()
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

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Xmlsoaparraycheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_ff:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxelementnamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlendpointcheck:
		ABSOLUTE = "ABSOLUTE"
		RELATIVE = "RELATIVE"

	class Xmlmaxfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnamespacescheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributenamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlblockdtd:
		ON = "ON"
		OFF = "OFF"

	class Isregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlblockpi:
		ON = "ON"
		OFF = "OFF"

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

	class As_scan_location_xss:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Xmlmaxnamespaceurilengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxentityexpansiondepthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xmlxss:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class As_scan_location_sql:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Isregex_ffc:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxattributevaluelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlattachmentcontenttypecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xmlsql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidatesoapenvelope:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnodescheck:
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

class appfwprofile_xmldosurl_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_xmldosurl_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_xmldosurl_binding = [appfwprofile_xmldosurl_binding() for _ in range(length)]

