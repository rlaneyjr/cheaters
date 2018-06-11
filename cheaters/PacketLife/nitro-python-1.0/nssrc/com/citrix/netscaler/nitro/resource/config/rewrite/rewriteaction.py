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

class rewriteaction(base_resource) :
	""" Configuration for rewrite action resource. """
	def __init__(self) :
		self._name = ""
		self._type = ""
		self._target = ""
		self._stringbuilderexpr = ""
		self._pattern = ""
		self._search = ""
		self._bypasssafetycheck = ""
		self._refinesearch = ""
		self._comment = ""
		self._newname = ""
		self._hits = 0
		self._undefhits = 0
		self._referencecount = 0
		self._description = ""
		self._isdefault = False
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the user-defined rewrite action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the rewrite policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rewrite action" or 'my rewrite action').
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the user-defined rewrite action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the rewrite policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rewrite action" or 'my rewrite action').
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of user-defined rewrite action. The information that you provide for, and the effect of, each type are as follows:: 
		* REPLACE <target> <string_builder_expr>. Replaces the string with the string-builder expression.
		* REPLACE_ALL <target> <string_builder_expr1> -(pattern|search) <string_builder_expr2>. In the request or response specified by <target>, replaces all occurrences of the string defined by <string_builder_expr1> with the string defined by <string_builder_expr2>. You can use a PCRE-format pattern or the search facility to find the strings to be replaced.
		* REPLACE_HTTP_RES <string_builder_expr>. Replaces the complete HTTP response with the string defined by the string-builder expression.
		* REPLACE_SIP_RES <target> - Replaces the complete SIP response with the string specified by <target>.
		* INSERT_HTTP_HEADER <header_string_builder_expr> <contents_string_builder_expr>. Inserts the HTTP header specified by <header_string_builder_expr> and header contents specified by <contents_string_builder_expr>.
		* DELETE_HTTP_HEADER <target>. Deletes the HTTP header specified by <target>.
		* CORRUPT_HTTP_HEADER <target>. Replaces the header name of all occurrences of the HTTP header specified by <target> with a corrupted name, so that it will not be recognized by the receiver  Example: MY_HEADER is changed to MHEY_ADER.
		* INSERT_BEFORE <string_builder_expr1> <string_builder_expr1>. Finds the string specified in <string_builder_expr1> and inserts the string in <string_builder_expr2> before it.
		* INSERT_BEFORE_ALL <target> <string_builder_expr1> -(pattern|search) <string_builder_expr2>. In the request or response specified by <target>, locates all occurrences of the string specified in <string_builder_expr1> and inserts the string specified in <string_builder_expr2> before each. You can use a PCRE-format pattern or the search facility to find the strings.
		* INSERT_AFTER <string_builder_expr1> <string_builder_expr2>. Finds the string specified in <string_builder_expr1>, and inserts the string specified in <string_builder_expr2> after it.
		* INSERT_AFTER_ALL <target> <string_builder_expr1> -(pattern|search) <string_builder_expr>. In the request or response specified by <target>, locates all occurrences of the string specified by <string_builder_expr1> and inserts the string specified by <string_builder_expr2> after each. You can use a PCRE-format pattern or the search facility to find the strings.
		* DELETE <target>. Finds and deletes the specified target.
		* DELETE_ALL <target> -(pattern|search) <string_builder_expr>. In the request or response specified by <target>, locates and deletes all occurrences of the string specified by <string_builder_expr>. You can use a PCRE-format pattern or the search facility to find the strings.
		* REPLACE_DIAMETER_HEADER_FIELD <target> <field value>. In the request or response modify the header field specified by <target>. Use Diameter.req.flags.SET(<flag>) or Diameter.req.flags.UNSET<flag> as 'stringbuilderexpression' to set or unset flags.<br/>Possible values = noop, delete, insert_http_header, delete_http_header, corrupt_http_header, insert_before, insert_after, replace, replace_http_res, delete_all, replace_all, insert_before_all, insert_after_all, clientless_vpn_encode, clientless_vpn_encode_all, clientless_vpn_decode, clientless_vpn_decode_all, insert_sip_header, delete_sip_header, corrupt_sip_header, replace_sip_res, replace_diameter_header_field.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of user-defined rewrite action. The information that you provide for, and the effect of, each type are as follows:: 
		* REPLACE <target> <string_builder_expr>. Replaces the string with the string-builder expression.
		* REPLACE_ALL <target> <string_builder_expr1> -(pattern|search) <string_builder_expr2>. In the request or response specified by <target>, replaces all occurrences of the string defined by <string_builder_expr1> with the string defined by <string_builder_expr2>. You can use a PCRE-format pattern or the search facility to find the strings to be replaced.
		* REPLACE_HTTP_RES <string_builder_expr>. Replaces the complete HTTP response with the string defined by the string-builder expression.
		* REPLACE_SIP_RES <target> - Replaces the complete SIP response with the string specified by <target>.
		* INSERT_HTTP_HEADER <header_string_builder_expr> <contents_string_builder_expr>. Inserts the HTTP header specified by <header_string_builder_expr> and header contents specified by <contents_string_builder_expr>.
		* DELETE_HTTP_HEADER <target>. Deletes the HTTP header specified by <target>.
		* CORRUPT_HTTP_HEADER <target>. Replaces the header name of all occurrences of the HTTP header specified by <target> with a corrupted name, so that it will not be recognized by the receiver  Example: MY_HEADER is changed to MHEY_ADER.
		* INSERT_BEFORE <string_builder_expr1> <string_builder_expr1>. Finds the string specified in <string_builder_expr1> and inserts the string in <string_builder_expr2> before it.
		* INSERT_BEFORE_ALL <target> <string_builder_expr1> -(pattern|search) <string_builder_expr2>. In the request or response specified by <target>, locates all occurrences of the string specified in <string_builder_expr1> and inserts the string specified in <string_builder_expr2> before each. You can use a PCRE-format pattern or the search facility to find the strings.
		* INSERT_AFTER <string_builder_expr1> <string_builder_expr2>. Finds the string specified in <string_builder_expr1>, and inserts the string specified in <string_builder_expr2> after it.
		* INSERT_AFTER_ALL <target> <string_builder_expr1> -(pattern|search) <string_builder_expr>. In the request or response specified by <target>, locates all occurrences of the string specified by <string_builder_expr1> and inserts the string specified by <string_builder_expr2> after each. You can use a PCRE-format pattern or the search facility to find the strings.
		* DELETE <target>. Finds and deletes the specified target.
		* DELETE_ALL <target> -(pattern|search) <string_builder_expr>. In the request or response specified by <target>, locates and deletes all occurrences of the string specified by <string_builder_expr>. You can use a PCRE-format pattern or the search facility to find the strings.
		* REPLACE_DIAMETER_HEADER_FIELD <target> <field value>. In the request or response modify the header field specified by <target>. Use Diameter.req.flags.SET(<flag>) or Diameter.req.flags.UNSET<flag> as 'stringbuilderexpression' to set or unset flags.<br/>Possible values = noop, delete, insert_http_header, delete_http_header, corrupt_http_header, insert_before, insert_after, replace, replace_http_res, delete_all, replace_all, insert_before_all, insert_after_all, clientless_vpn_encode, clientless_vpn_encode_all, clientless_vpn_decode, clientless_vpn_decode_all, insert_sip_header, delete_sip_header, corrupt_sip_header, replace_sip_res, replace_diameter_header_field
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def target(self) :
		ur"""Default syntax expression that specifies which part of the request or response to rewrite.<br/>Minimum length =  1.
		"""
		try :
			return self._target
		except Exception as e:
			raise e

	@target.setter
	def target(self, target) :
		ur"""Default syntax expression that specifies which part of the request or response to rewrite.<br/>Minimum length =  1
		"""
		try :
			self._target = target
		except Exception as e:
			raise e

	@property
	def stringbuilderexpr(self) :
		ur"""Default syntax expression that specifies the content to insert into the request or response at the specified location, or that replaces the specified string.
		"""
		try :
			return self._stringbuilderexpr
		except Exception as e:
			raise e

	@stringbuilderexpr.setter
	def stringbuilderexpr(self, stringbuilderexpr) :
		ur"""Default syntax expression that specifies the content to insert into the request or response at the specified location, or that replaces the specified string.
		"""
		try :
			self._stringbuilderexpr = stringbuilderexpr
		except Exception as e:
			raise e

	@property
	def pattern(self) :
		ur"""Pattern that is used to match multiple strings in the request or response. The pattern may be a string literal (without quotes) or a PCRE-format regular expression with a delimiter that consists of any printable ASCII non-alphanumeric character except for the underscore (_) and space ( ) that is not otherwise used in the expression. Example: re~https?://|HTTPS?://~ The preceding regular expression can use the tilde (~) as the delimiter because that character does not appear in the regular expression itself. Used in the INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types.
		"""
		try :
			return self._pattern
		except Exception as e:
			raise e

	@pattern.setter
	def pattern(self, pattern) :
		ur"""Pattern that is used to match multiple strings in the request or response. The pattern may be a string literal (without quotes) or a PCRE-format regular expression with a delimiter that consists of any printable ASCII non-alphanumeric character except for the underscore (_) and space ( ) that is not otherwise used in the expression. Example: re~https?://|HTTPS?://~ The preceding regular expression can use the tilde (~) as the delimiter because that character does not appear in the regular expression itself. Used in the INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types.
		"""
		try :
			self._pattern = pattern
		except Exception as e:
			raise e

	@property
	def search(self) :
		ur"""Search facility that is used to match multiple strings in the request or response. Used in the INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types. The following search types are supported:
		* Text ("text(string)") - A literal string. Example: -search text("hello")
		* Regular expression ("regex(re<delimiter>regular exp<delimiter>)") - Pattern that is used to match multiple strings in the request or response. The pattern may be a string literal (without quotes) or a PCRE-format regular expression with a delimiter that consists of any printable ASCII non-alphanumeric character except for the underscore (_) and space ( ) that is not otherwise used in the expression. Example: -search regex(re~^hello~) The preceding regular expression can use the tilde (~) as the delimiter because that character does not appear in the regular expression itself.
		* XPath ("xpath(xp<delimiter>xpath expression<delimiter>)") - An XPath expression. Example: -search xpath(xp%/a/b%)
		* JSON ("xpath_json(xp<delimiter>xpath expression<delimiter>)") - An XPath JSON expression. Example: -search xpath_json(xp%/a/b%)
		NOTE: JSON searches use the same syntax as XPath searches, but operate on JSON files instead of standard XML files.
		* Patset ("patset(patset)") - A predefined pattern set. Example: -search patset("patset1").
		* Datset ("dataset(dataset)") - A predefined dataset. Example: -search dataset("dataset1").
		* AVP ("avp(avp number)") - AVP number that is used to match multiple AVPs in a Diameter Message. Example: -search avp(999).
		"""
		try :
			return self._search
		except Exception as e:
			raise e

	@search.setter
	def search(self, search) :
		ur"""Search facility that is used to match multiple strings in the request or response. Used in the INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types. The following search types are supported:
		* Text ("text(string)") - A literal string. Example: -search text("hello")
		* Regular expression ("regex(re<delimiter>regular exp<delimiter>)") - Pattern that is used to match multiple strings in the request or response. The pattern may be a string literal (without quotes) or a PCRE-format regular expression with a delimiter that consists of any printable ASCII non-alphanumeric character except for the underscore (_) and space ( ) that is not otherwise used in the expression. Example: -search regex(re~^hello~) The preceding regular expression can use the tilde (~) as the delimiter because that character does not appear in the regular expression itself.
		* XPath ("xpath(xp<delimiter>xpath expression<delimiter>)") - An XPath expression. Example: -search xpath(xp%/a/b%)
		* JSON ("xpath_json(xp<delimiter>xpath expression<delimiter>)") - An XPath JSON expression. Example: -search xpath_json(xp%/a/b%)
		NOTE: JSON searches use the same syntax as XPath searches, but operate on JSON files instead of standard XML files.
		* Patset ("patset(patset)") - A predefined pattern set. Example: -search patset("patset1").
		* Datset ("dataset(dataset)") - A predefined dataset. Example: -search dataset("dataset1").
		* AVP ("avp(avp number)") - AVP number that is used to match multiple AVPs in a Diameter Message. Example: -search avp(999).
		"""
		try :
			self._search = search
		except Exception as e:
			raise e

	@property
	def bypasssafetycheck(self) :
		ur"""Bypass the safety check and allow unsafe expressions. An unsafe expression is one that contains references to message elements that might not be present in all messages. If an expression refers to a missing request element, an empty string is used instead.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._bypasssafetycheck
		except Exception as e:
			raise e

	@bypasssafetycheck.setter
	def bypasssafetycheck(self, bypasssafetycheck) :
		ur"""Bypass the safety check and allow unsafe expressions. An unsafe expression is one that contains references to message elements that might not be present in all messages. If an expression refers to a missing request element, an empty string is used instead.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._bypasssafetycheck = bypasssafetycheck
		except Exception as e:
			raise e

	@property
	def refinesearch(self) :
		ur"""Specify additional criteria to refine the results of the search. 
		Always starts with the "extend(m,n)" operation, where 'm' specifies number of bytes to the left of selected data and 'n' specifies number of bytes to the right of selected data.
		You can use refineSearch only on body expressions, and for the INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types.
		"""
		try :
			return self._refinesearch
		except Exception as e:
			raise e

	@refinesearch.setter
	def refinesearch(self, refinesearch) :
		ur"""Specify additional criteria to refine the results of the search. 
		Always starts with the "extend(m,n)" operation, where 'm' specifies number of bytes to the left of selected data and 'n' specifies number of bytes to the right of selected data.
		You can use refineSearch only on body expressions, and for the INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types.
		"""
		try :
			self._refinesearch = refinesearch
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Comment. Can be used to preserve information about this rewrite action.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Comment. Can be used to preserve information about this rewrite action.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the rewrite action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the rewrite policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rewrite action" or 'my rewrite action').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the rewrite action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the rewrite policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rewrite action" or 'my rewrite action').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The number of times the action has been taken.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		ur"""The number of times the action resulted in UNDEF.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		ur"""The number of references to the action.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Description of the action.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		ur"""A value of true is returned if it is a default rewriteaction.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine whether rewrite action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rewriteaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rewriteaction
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
		ur""" Use this API to add rewriteaction.
		"""
		try :
			if type(resource) is not list :
				addresource = rewriteaction()
				addresource.name = resource.name
				addresource.type = resource.type
				addresource.target = resource.target
				addresource.stringbuilderexpr = resource.stringbuilderexpr
				addresource.pattern = resource.pattern
				addresource.search = resource.search
				addresource.bypasssafetycheck = resource.bypasssafetycheck
				addresource.refinesearch = resource.refinesearch
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ rewriteaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].type = resource[i].type
						addresources[i].target = resource[i].target
						addresources[i].stringbuilderexpr = resource[i].stringbuilderexpr
						addresources[i].pattern = resource[i].pattern
						addresources[i].search = resource[i].search
						addresources[i].bypasssafetycheck = resource[i].bypasssafetycheck
						addresources[i].refinesearch = resource[i].refinesearch
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete rewriteaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = rewriteaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ rewriteaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ rewriteaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update rewriteaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = rewriteaction()
				updateresource.name = resource.name
				updateresource.target = resource.target
				updateresource.stringbuilderexpr = resource.stringbuilderexpr
				updateresource.bypasssafetycheck = resource.bypasssafetycheck
				updateresource.pattern = resource.pattern
				updateresource.search = resource.search
				updateresource.bypasssafetycheck = resource.bypasssafetycheck
				updateresource.refinesearch = resource.refinesearch
				updateresource.comment = resource.comment
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ rewriteaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].target = resource[i].target
						updateresources[i].stringbuilderexpr = resource[i].stringbuilderexpr
						updateresources[i].bypasssafetycheck = resource[i].bypasssafetycheck
						updateresources[i].pattern = resource[i].pattern
						updateresources[i].search = resource[i].search
						updateresources[i].bypasssafetycheck = resource[i].bypasssafetycheck
						updateresources[i].refinesearch = resource[i].refinesearch
						updateresources[i].comment = resource[i].comment
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of rewriteaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = rewriteaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ rewriteaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ rewriteaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a rewriteaction resource.
		"""
		try :
			renameresource = rewriteaction()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the rewriteaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rewriteaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = rewriteaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [rewriteaction() for _ in range(len(name))]
							obj = [rewriteaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = rewriteaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of rewriteaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rewriteaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the rewriteaction resources configured on NetScaler.
		"""
		try :
			obj = rewriteaction()
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
		ur""" Use this API to count filtered the set of rewriteaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rewriteaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

	class Type:
		noop = "noop"
		delete = "delete"
		insert_http_header = "insert_http_header"
		delete_http_header = "delete_http_header"
		corrupt_http_header = "corrupt_http_header"
		insert_before = "insert_before"
		insert_after = "insert_after"
		replace = "replace"
		replace_http_res = "replace_http_res"
		delete_all = "delete_all"
		replace_all = "replace_all"
		insert_before_all = "insert_before_all"
		insert_after_all = "insert_after_all"
		clientless_vpn_encode = "clientless_vpn_encode"
		clientless_vpn_encode_all = "clientless_vpn_encode_all"
		clientless_vpn_decode = "clientless_vpn_decode"
		clientless_vpn_decode_all = "clientless_vpn_decode_all"
		insert_sip_header = "insert_sip_header"
		delete_sip_header = "delete_sip_header"
		corrupt_sip_header = "corrupt_sip_header"
		replace_sip_res = "replace_sip_res"
		replace_diameter_header_field = "replace_diameter_header_field"

	class Bypasssafetycheck:
		YES = "YES"
		NO = "NO"

class rewriteaction_response(base_response) :
	def __init__(self, length=1) :
		self.rewriteaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rewriteaction = [rewriteaction() for _ in range(length)]

