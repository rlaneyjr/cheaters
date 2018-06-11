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

class sslcrl_serialnumber_binding(base_resource) :
	""" Binding class showing the serialnumber that can be bound to sslcrl.
	"""
	def __init__(self) :
		self._number = ""
		self._date = ""
		self._crlname = ""
		self.___count = 0

	@property
	def number(self) :
		ur"""Certificate Serial number.
		"""
		try :
			return self._number
		except Exception as e:
			raise e

	@number.setter
	def number(self, number) :
		ur"""Certificate Serial number.
		"""
		try :
			self._number = number
		except Exception as e:
			raise e

	@property
	def crlname(self) :
		ur"""Name of the CRL for which to show detailed information.<br/>Minimum length =  1.
		"""
		try :
			return self._crlname
		except Exception as e:
			raise e

	@crlname.setter
	def crlname(self, crlname) :
		ur"""Name of the CRL for which to show detailed information.<br/>Minimum length =  1
		"""
		try :
			self._crlname = crlname
		except Exception as e:
			raise e

	@property
	def date(self) :
		ur"""Certificate Revocation date.
		"""
		try :
			return self._date
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcrl_serialnumber_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcrl_serialnumber_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.crlname is not None :
				return str(self.crlname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, crlname) :
		ur""" Use this API to fetch sslcrl_serialnumber_binding resources.
		"""
		try :
			obj = sslcrl_serialnumber_binding()
			obj.crlname = crlname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, crlname, filter_) :
		ur""" Use this API to fetch filtered set of sslcrl_serialnumber_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcrl_serialnumber_binding()
			obj.crlname = crlname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, crlname) :
		ur""" Use this API to count sslcrl_serialnumber_binding resources configued on NetScaler.
		"""
		try :
			obj = sslcrl_serialnumber_binding()
			obj.crlname = crlname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, crlname, filter_) :
		ur""" Use this API to count the filtered set of sslcrl_serialnumber_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcrl_serialnumber_binding()
			obj.crlname = crlname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class sslcrl_serialnumber_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcrl_serialnumber_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcrl_serialnumber_binding = [sslcrl_serialnumber_binding() for _ in range(length)]

