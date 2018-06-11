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

class sslcipher(base_resource) :
	""" Configuration for cipher resource. """
	def __init__(self) :
		self._ciphergroupname = ""
		self._ciphgrpalias = ""
		self._ciphername = ""
		self.___count = 0

	@property
	def ciphergroupname(self) :
		ur"""Name for the user-defined cipher group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the cipher group is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ciphergroup" or 'my ciphergroup').<br/>Minimum length =  1.
		"""
		try :
			return self._ciphergroupname
		except Exception as e:
			raise e

	@ciphergroupname.setter
	def ciphergroupname(self, ciphergroupname) :
		ur"""Name for the user-defined cipher group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the cipher group is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my ciphergroup" or 'my ciphergroup').<br/>Minimum length =  1
		"""
		try :
			self._ciphergroupname = ciphergroupname
		except Exception as e:
			raise e

	@property
	def ciphgrpalias(self) :
		ur"""The individual cipher name(s), a user-defined cipher group, or a system predefined cipher alias that will be added to the  predefined cipher alias that will be added to the group cipherGroupName.
		If a cipher alias or a cipher group is specified, all the individual ciphers in the cipher alias or group will be added to the user-defined cipher group.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphgrpalias
		except Exception as e:
			raise e

	@ciphgrpalias.setter
	def ciphgrpalias(self, ciphgrpalias) :
		ur"""The individual cipher name(s), a user-defined cipher group, or a system predefined cipher alias that will be added to the  predefined cipher alias that will be added to the group cipherGroupName.
		If a cipher alias or a cipher group is specified, all the individual ciphers in the cipher alias or group will be added to the user-defined cipher group.<br/>Minimum length =  1
		"""
		try :
			self._ciphgrpalias = ciphgrpalias
		except Exception as e:
			raise e

	@property
	def ciphername(self) :
		ur"""The cipher(s) to be removed from the cipher group.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphername
		except Exception as e:
			raise e

	@ciphername.setter
	def ciphername(self, ciphername) :
		ur"""The cipher(s) to be removed from the cipher group.<br/>Minimum length =  1
		"""
		try :
			self._ciphername = ciphername
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcipher_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcipher
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ciphergroupname is not None :
				return str(self.ciphergroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add sslcipher.
		"""
		try :
			if type(resource) is not list :
				addresource = sslcipher()
				addresource.ciphergroupname = resource.ciphergroupname
				addresource.ciphgrpalias = resource.ciphgrpalias
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslcipher() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ciphergroupname = resource[i].ciphergroupname
						addresources[i].ciphgrpalias = resource[i].ciphgrpalias
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete sslcipher.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslcipher()
				if type(resource) !=  type(deleteresource):
					deleteresource.ciphergroupname = resource
				else :
					deleteresource.ciphergroupname = resource.ciphergroupname
					deleteresource.ciphername = resource.ciphername
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslcipher() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ciphergroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslcipher() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ciphergroupname = resource[i].ciphergroupname
							deleteresources[i].ciphername = resource[i].ciphername
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslcipher resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslcipher()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = sslcipher()
						obj.ciphergroupname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [sslcipher() for _ in range(len(name))]
							obj = [sslcipher() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = sslcipher()
								obj[i].ciphergroupname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of sslcipher resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcipher()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the sslcipher resources configured on NetScaler.
		"""
		try :
			obj = sslcipher()
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
		ur""" Use this API to count filtered the set of sslcipher resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcipher()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class sslcipher_response(base_response) :
	def __init__(self, length=1) :
		self.sslcipher = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcipher = [sslcipher() for _ in range(length)]

