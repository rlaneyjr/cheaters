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

class sslcertchain_sslcertkey_binding(base_resource) :
	""" Binding class showing the sslcertkey that can be bound to sslcertchain.
	"""
	def __init__(self) :
		self._linkcertkeyname = ""
		self._islinked = False
		self._isca = False
		self._addsubject = False
		self._certkeyname = ""
		self.___count = 0

	@property
	def linkcertkeyname(self) :
		ur"""Name of the Linked Certificate.<br/>Minimum length =  1.
		"""
		try :
			return self._linkcertkeyname
		except Exception as e:
			raise e

	@linkcertkeyname.setter
	def linkcertkeyname(self, linkcertkeyname) :
		ur"""Name of the Linked Certificate.<br/>Minimum length =  1
		"""
		try :
			self._linkcertkeyname = linkcertkeyname
		except Exception as e:
			raise e

	@property
	def certkeyname(self) :
		ur"""Name of the Certificate.<br/>Minimum length =  1.
		"""
		try :
			return self._certkeyname
		except Exception as e:
			raise e

	@certkeyname.setter
	def certkeyname(self, certkeyname) :
		ur"""Name of the Certificate.<br/>Minimum length =  1
		"""
		try :
			self._certkeyname = certkeyname
		except Exception as e:
			raise e

	@property
	def isca(self) :
		ur"""Used to find if certificate is a CA.
		"""
		try :
			return self._isca
		except Exception as e:
			raise e

	@property
	def islinked(self) :
		ur"""Used to find if certificate is linked.
		"""
		try :
			return self._islinked
		except Exception as e:
			raise e

	@property
	def addsubject(self) :
		ur"""Used to find if certificate is linked.
		"""
		try :
			return self._addsubject
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcertchain_sslcertkey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcertchain_sslcertkey_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.certkeyname is not None :
				return str(self.certkeyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, certkeyname) :
		ur""" Use this API to fetch sslcertchain_sslcertkey_binding resources.
		"""
		try :
			obj = sslcertchain_sslcertkey_binding()
			obj.certkeyname = certkeyname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, certkeyname, filter_) :
		ur""" Use this API to fetch filtered set of sslcertchain_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertchain_sslcertkey_binding()
			obj.certkeyname = certkeyname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, certkeyname) :
		ur""" Use this API to count sslcertchain_sslcertkey_binding resources configued on NetScaler.
		"""
		try :
			obj = sslcertchain_sslcertkey_binding()
			obj.certkeyname = certkeyname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, certkeyname, filter_) :
		ur""" Use this API to count the filtered set of sslcertchain_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertchain_sslcertkey_binding()
			obj.certkeyname = certkeyname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class sslcertchain_sslcertkey_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcertchain_sslcertkey_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcertchain_sslcertkey_binding = [sslcertchain_sslcertkey_binding() for _ in range(length)]

