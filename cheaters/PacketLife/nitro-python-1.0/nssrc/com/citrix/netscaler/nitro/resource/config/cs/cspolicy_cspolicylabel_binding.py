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

class cspolicy_cspolicylabel_binding(base_resource) :
	""" Binding class showing the cspolicylabel that can be bound to cspolicy.
	"""
	def __init__(self) :
		self._domain = ""
		self._url = ""
		self._priority = 0
		self._hits = 0
		self._labeltype = ""
		self._labelname = ""
		self._policyname = ""
		self.___count = 0

	@property
	def policyname(self) :
		ur"""Name of the content switching policy to display. If this parameter is omitted, details of all the policies are displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name of the content switching policy to display. If this parameter is omitted, details of all the policies are displayed.<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def domain(self) :
		ur"""The domain name. The string value can range to 63 characters.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		ur"""The domain name. The string value can range to 63 characters.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""priority of bound policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Total number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def url(self) :
		ur"""URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: [[prefix] [*]] [.suffix].<br/>Minimum length =  1<br/>Maximum length =  208.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""The invocation type.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		ur"""Name of the label invoked.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cspolicy_cspolicylabel_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cspolicy_cspolicylabel_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, policyname) :
		ur""" Use this API to fetch cspolicy_cspolicylabel_binding resources.
		"""
		try :
			obj = cspolicy_cspolicylabel_binding()
			obj.policyname = policyname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, policyname, filter_) :
		ur""" Use this API to fetch filtered set of cspolicy_cspolicylabel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicy_cspolicylabel_binding()
			obj.policyname = policyname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, policyname) :
		ur""" Use this API to count cspolicy_cspolicylabel_binding resources configued on NetScaler.
		"""
		try :
			obj = cspolicy_cspolicylabel_binding()
			obj.policyname = policyname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, policyname, filter_) :
		ur""" Use this API to count the filtered set of cspolicy_cspolicylabel_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicy_cspolicylabel_binding()
			obj.policyname = policyname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

class cspolicy_cspolicylabel_binding_response(base_response) :
	def __init__(self, length=1) :
		self.cspolicy_cspolicylabel_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cspolicy_cspolicylabel_binding = [cspolicy_cspolicylabel_binding() for _ in range(length)]

