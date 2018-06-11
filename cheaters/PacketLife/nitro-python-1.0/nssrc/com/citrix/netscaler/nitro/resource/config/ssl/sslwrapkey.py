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

class sslwrapkey(base_resource) :
	""" Configuration for WRAP key resource. """
	def __init__(self) :
		self._wrapkeyname = ""
		self._password = ""
		self._salt = ""
		self.___count = 0

	@property
	def wrapkeyname(self) :
		ur"""Name for the wrap key. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the wrap key is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my key" or 'my key').<br/>Minimum length =  1.
		"""
		try :
			return self._wrapkeyname
		except Exception as e:
			raise e

	@wrapkeyname.setter
	def wrapkeyname(self, wrapkeyname) :
		ur"""Name for the wrap key. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the wrap key is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my key" or 'my key').<br/>Minimum length =  1
		"""
		try :
			self._wrapkeyname = wrapkeyname
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password string for the wrap key.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password string for the wrap key.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def salt(self) :
		ur"""Salt string for the wrap key.<br/>Minimum length =  1.
		"""
		try :
			return self._salt
		except Exception as e:
			raise e

	@salt.setter
	def salt(self, salt) :
		ur"""Salt string for the wrap key.<br/>Minimum length =  1
		"""
		try :
			self._salt = salt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslwrapkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslwrapkey
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.wrapkeyname is not None :
				return str(self.wrapkeyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def create(cls, client, resource) :
		ur""" Use this API to create sslwrapkey.
		"""
		try :
			if type(resource) is not list :
				createresource = sslwrapkey()
				createresource.wrapkeyname = resource.wrapkeyname
				createresource.password = resource.password
				createresource.salt = resource.salt
				return createresource.perform_operation(client,"create")
			else :
				if (resource and len(resource) > 0) :
					createresources = [ sslwrapkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						createresources[i].wrapkeyname = resource[i].wrapkeyname
						createresources[i].password = resource[i].password
						createresources[i].salt = resource[i].salt
				result = cls.perform_operation_bulk_request(client, createresources,"create")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete sslwrapkey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslwrapkey()
				if type(resource) !=  type(deleteresource):
					deleteresource.wrapkeyname = resource
				else :
					deleteresource.wrapkeyname = resource.wrapkeyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslwrapkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].wrapkeyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslwrapkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].wrapkeyname = resource[i].wrapkeyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslwrapkey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslwrapkey()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of sslwrapkey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslwrapkey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the sslwrapkey resources configured on NetScaler.
		"""
		try :
			obj = sslwrapkey()
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
		ur""" Use this API to count filtered the set of sslwrapkey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslwrapkey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class sslwrapkey_response(base_response) :
	def __init__(self, length=1) :
		self.sslwrapkey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslwrapkey = [sslwrapkey() for _ in range(length)]

