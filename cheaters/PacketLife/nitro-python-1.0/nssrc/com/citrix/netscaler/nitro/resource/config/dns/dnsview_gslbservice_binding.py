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

class dnsview_gslbservice_binding(base_resource) :
	""" Binding class showing the gslbservice that can be bound to dnsview.
	"""
	def __init__(self) :
		self._gslbservicename = ""
		self._ipaddress = ""
		self._viewname = ""
		self.___count = 0

	@property
	def viewname(self) :
		ur"""Name of the view to display.<br/>Minimum length =  1.
		"""
		try :
			return self._viewname
		except Exception as e:
			raise e

	@viewname.setter
	def viewname(self, viewname) :
		ur"""Name of the view to display.<br/>Minimum length =  1
		"""
		try :
			self._viewname = viewname
		except Exception as e:
			raise e

	@property
	def gslbservicename(self) :
		ur"""Service name of the service using this view.
		"""
		try :
			return self._gslbservicename
		except Exception as e:
			raise e

	@gslbservicename.setter
	def gslbservicename(self, gslbservicename) :
		ur"""Service name of the service using this view.
		"""
		try :
			self._gslbservicename = gslbservicename
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""IP of the service corresponding to the given view.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsview_gslbservice_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsview_gslbservice_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.viewname is not None :
				return str(self.viewname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, viewname) :
		ur""" Use this API to fetch dnsview_gslbservice_binding resources.
		"""
		try :
			obj = dnsview_gslbservice_binding()
			obj.viewname = viewname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, viewname, filter_) :
		ur""" Use this API to fetch filtered set of dnsview_gslbservice_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsview_gslbservice_binding()
			obj.viewname = viewname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, viewname) :
		ur""" Use this API to count dnsview_gslbservice_binding resources configued on NetScaler.
		"""
		try :
			obj = dnsview_gslbservice_binding()
			obj.viewname = viewname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, viewname, filter_) :
		ur""" Use this API to count the filtered set of dnsview_gslbservice_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsview_gslbservice_binding()
			obj.viewname = viewname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class dnsview_gslbservice_binding_response(base_response) :
	def __init__(self, length=1) :
		self.dnsview_gslbservice_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsview_gslbservice_binding = [dnsview_gslbservice_binding() for _ in range(length)]

