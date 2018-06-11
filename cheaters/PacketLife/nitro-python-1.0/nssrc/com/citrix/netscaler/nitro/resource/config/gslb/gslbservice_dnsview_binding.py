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

class gslbservice_dnsview_binding(base_resource) :
	""" Binding class showing the dnsview that can be bound to gslbservice.
	"""
	def __init__(self) :
		self._viewname = ""
		self._viewip = ""
		self._servicename = ""
		self.___count = 0

	@property
	def viewname(self) :
		ur"""Name of the DNS view of the service. A DNS view is used in global server load balancing (GSLB) to return a predetermined IP address to a specific group of clients, which are identified by using a DNS policy.<br/>Minimum length =  1.
		"""
		try :
			return self._viewname
		except Exception as e:
			raise e

	@viewname.setter
	def viewname(self, viewname) :
		ur"""Name of the DNS view of the service. A DNS view is used in global server load balancing (GSLB) to return a predetermined IP address to a specific group of clients, which are identified by using a DNS policy.<br/>Minimum length =  1
		"""
		try :
			self._viewname = viewname
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""Name of the GSLB service.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""Name of the GSLB service.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def viewip(self) :
		ur"""IP address to be used for the given view.
		"""
		try :
			return self._viewip
		except Exception as e:
			raise e

	@viewip.setter
	def viewip(self, viewip) :
		ur"""IP address to be used for the given view.
		"""
		try :
			self._viewip = viewip
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbservice_dnsview_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbservice_dnsview_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicename is not None :
				return str(self.servicename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = gslbservice_dnsview_binding()
				updateresource.servicename = resource.servicename
				updateresource.viewname = resource.viewname
				updateresource.viewip = resource.viewip
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [gslbservice_dnsview_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicename = resource[i].servicename
						updateresources[i].viewname = resource[i].viewname
						updateresources[i].viewip = resource[i].viewip
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = gslbservice_dnsview_binding()
				deleteresource.servicename = resource.servicename
				deleteresource.viewname = resource.viewname
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [gslbservice_dnsview_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].servicename = resource[i].servicename
						deleteresources[i].viewname = resource[i].viewname
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, servicename) :
		ur""" Use this API to fetch gslbservice_dnsview_binding resources.
		"""
		try :
			obj = gslbservice_dnsview_binding()
			obj.servicename = servicename
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicename, filter_) :
		ur""" Use this API to fetch filtered set of gslbservice_dnsview_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbservice_dnsview_binding()
			obj.servicename = servicename
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicename) :
		ur""" Use this API to count gslbservice_dnsview_binding resources configued on NetScaler.
		"""
		try :
			obj = gslbservice_dnsview_binding()
			obj.servicename = servicename
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, servicename, filter_) :
		ur""" Use this API to count the filtered set of gslbservice_dnsview_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbservice_dnsview_binding()
			obj.servicename = servicename
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Monstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class gslbservice_dnsview_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbservice_dnsview_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbservice_dnsview_binding = [gslbservice_dnsview_binding() for _ in range(length)]

