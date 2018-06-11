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

class nsassignment(base_resource) :
	""" Configuration for assignment resource. """
	def __init__(self) :
		self._name = ""
		self._variable = ""
		self._set = ""
		self._Add = ""
		self._sub = ""
		self._append = ""
		self._clear = False
		self._comment = ""
		self._newname = ""
		self._hits = 0
		self._undefhits = 0
		self._referencecount = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the assignment. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the assignment is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my assignment" or 'my assignment').
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the assignment. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the assignment is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my assignment" or 'my assignment').
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def variable(self) :
		ur"""Left hand side of the assigment, of the form $variable-name (for a singleton variabled) or $variable-name[key-expression], where key-expression is a default syntax expression that evaluates to a text string and provides the key to select a map entry.
		"""
		try :
			return self._variable
		except Exception as e:
			raise e

	@variable.setter
	def variable(self, variable) :
		ur"""Left hand side of the assigment, of the form $variable-name (for a singleton variabled) or $variable-name[key-expression], where key-expression is a default syntax expression that evaluates to a text string and provides the key to select a map entry.
		"""
		try :
			self._variable = variable
		except Exception as e:
			raise e

	@property
	def set(self) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and assigned to theleft hand variable.
		"""
		try :
			return self._set
		except Exception as e:
			raise e

	@set.setter
	def set(self, set) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and assigned to theleft hand variable.
		"""
		try :
			self._set = set
		except Exception as e:
			raise e

	@property
	def Add(self) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and added to the left hand variable.
		"""
		try :
			return self._Add
		except Exception as e:
			raise e

	@Add.setter
	def Add(self, Add) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and added to the left hand variable.
		"""
		try :
			self._Add = Add
		except Exception as e:
			raise e

	@property
	def sub(self) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and subtracted from the left hand variable.
		"""
		try :
			return self._sub
		except Exception as e:
			raise e

	@sub.setter
	def sub(self, sub) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and subtracted from the left hand variable.
		"""
		try :
			self._sub = sub
		except Exception as e:
			raise e

	@property
	def append(self) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and appended to the left hand variable.
		"""
		try :
			return self._append
		except Exception as e:
			raise e

	@append.setter
	def append(self, append) :
		ur"""Right hand side of the assignment. The default syntax expression is evaluated and appended to the left hand variable.
		"""
		try :
			self._append = append
		except Exception as e:
			raise e

	@property
	def clear(self) :
		ur"""Clear the variable value. Deallocates a text value, and for a map, the text key.
		"""
		try :
			return self._clear
		except Exception as e:
			raise e

	@clear.setter
	def clear(self, clear) :
		ur"""Clear the variable value. Deallocates a text value, and for a map, the text key.
		"""
		try :
			self._clear = clear
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
		ur"""New name for the assignment.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the rewrite policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my assignment" or 'my assignment').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the assignment.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the rewrite policy is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my assignment" or 'my assignment').<br/>Minimum length =  1
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

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsassignment_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsassignment
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
		ur""" Use this API to add nsassignment.
		"""
		try :
			if type(resource) is not list :
				addresource = nsassignment()
				addresource.name = resource.name
				addresource.variable = resource.variable
				addresource.set = resource.set
				addresource.Add = resource.Add
				addresource.sub = resource.sub
				addresource.append = resource.append
				addresource.clear = resource.clear
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsassignment() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].variable = resource[i].variable
						addresources[i].set = resource[i].set
						addresources[i].Add = resource[i].Add
						addresources[i].sub = resource[i].sub
						addresources[i].append = resource[i].append
						addresources[i].clear = resource[i].clear
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nsassignment.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsassignment()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsassignment() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsassignment() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		ur""" Use this API to rename a nsassignment resource.
		"""
		try :
			renameresource = nsassignment()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsassignment resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsassignment()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nsassignment()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nsassignment() for _ in range(len(name))]
							obj = [nsassignment() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nsassignment()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nsassignment resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsassignment()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nsassignment resources configured on NetScaler.
		"""
		try :
			obj = nsassignment()
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
		ur""" Use this API to count filtered the set of nsassignment resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsassignment()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nsassignment_response(base_response) :
	def __init__(self, length=1) :
		self.nsassignment = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsassignment = [nsassignment() for _ in range(length)]

