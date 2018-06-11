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

class sslcipher_individualcipher_binding(base_resource) :
	""" Binding class showing the individualcipher that can be bound to sslcipher.
	"""
	def __init__(self) :
		self._ciphername = ""
		self._description = ""
		self._ciphergroupname = ""
		self._cipheroperation = ""
		self._ciphgrpals = ""
		self.___count = 0

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

	@property
	def ciphgrpals(self) :
		ur"""A cipher-suite can consist of an individual cipher name, the system predefined cipher-alias name, or user defined cipher-group name.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphgrpals
		except Exception as e:
			raise e

	@ciphgrpals.setter
	def ciphgrpals(self, ciphgrpals) :
		ur"""A cipher-suite can consist of an individual cipher name, the system predefined cipher-alias name, or user defined cipher-group name.<br/>Minimum length =  1
		"""
		try :
			self._ciphgrpals = ciphgrpals
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Cipher suite description.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@description.setter
	def description(self, description) :
		ur"""Cipher suite description.
		"""
		try :
			self._description = description
		except Exception as e:
			raise e

	@property
	def ciphergroupname(self) :
		ur"""Name of the user-defined cipher group.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphergroupname
		except Exception as e:
			raise e

	@ciphergroupname.setter
	def ciphergroupname(self, ciphergroupname) :
		ur"""Name of the user-defined cipher group.<br/>Minimum length =  1
		"""
		try :
			self._ciphergroupname = ciphergroupname
		except Exception as e:
			raise e

	@property
	def cipheroperation(self) :
		ur"""The operation that is performed when adding the cipher-suite.
		Possible cipher operations are:
		ADD - Appends the given cipher-suite to the existing one configured for the virtual server.
		REM - Removes the given cipher-suite from the existing one configured for the virtual server.
		ORD - Overrides the current configured cipher-suite for the virtual server with the given cipher-suite.<br/>Default value: 0<br/>Possible values = ADD, REM, ORD.
		"""
		try :
			return self._cipheroperation
		except Exception as e:
			raise e

	@cipheroperation.setter
	def cipheroperation(self, cipheroperation) :
		ur"""The operation that is performed when adding the cipher-suite.
		Possible cipher operations are:
		ADD - Appends the given cipher-suite to the existing one configured for the virtual server.
		REM - Removes the given cipher-suite from the existing one configured for the virtual server.
		ORD - Overrides the current configured cipher-suite for the virtual server with the given cipher-suite.<br/>Default value: 0<br/>Possible values = ADD, REM, ORD
		"""
		try :
			self._cipheroperation = cipheroperation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcipher_individualcipher_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcipher_individualcipher_binding
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
	def get(cls, service, ciphergroupname) :
		ur""" Use this API to fetch sslcipher_individualcipher_binding resources.
		"""
		try :
			obj = sslcipher_individualcipher_binding()
			obj.ciphergroupname = ciphergroupname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, ciphergroupname, filter_) :
		ur""" Use this API to fetch filtered set of sslcipher_individualcipher_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcipher_individualcipher_binding()
			obj.ciphergroupname = ciphergroupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, ciphergroupname) :
		ur""" Use this API to count sslcipher_individualcipher_binding resources configued on NetScaler.
		"""
		try :
			obj = sslcipher_individualcipher_binding()
			obj.ciphergroupname = ciphergroupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, ciphergroupname, filter_) :
		ur""" Use this API to count the filtered set of sslcipher_individualcipher_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcipher_individualcipher_binding()
			obj.ciphergroupname = ciphergroupname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Cipheroperation:
		ADD = "ADD"
		REM = "REM"
		ORD = "ORD"

class sslcipher_individualcipher_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcipher_individualcipher_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcipher_individualcipher_binding = [sslcipher_individualcipher_binding() for _ in range(length)]

