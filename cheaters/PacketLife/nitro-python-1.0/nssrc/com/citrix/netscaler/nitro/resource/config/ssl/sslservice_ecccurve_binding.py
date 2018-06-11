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

class sslservice_ecccurve_binding(base_resource) :
	""" Binding class showing the ecccurve that can be bound to sslservice.
	"""
	def __init__(self) :
		self._ecccurvename = ""
		self._servicename = ""
		self.___count = 0

	@property
	def servicename(self) :
		ur"""Name of the SSL service for which to set advanced configuration.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		ur"""Name of the SSL service for which to set advanced configuration.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def ecccurvename(self) :
		ur"""Named ECC curve bound to service/vserver.<br/>Possible values = ALL, P_224, P_256, P_384, P_521.
		"""
		try :
			return self._ecccurvename
		except Exception as e:
			raise e

	@ecccurvename.setter
	def ecccurvename(self, ecccurvename) :
		ur"""Named ECC curve bound to service/vserver.<br/>Possible values = ALL, P_224, P_256, P_384, P_521
		"""
		try :
			self._ecccurvename = ecccurvename
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslservice_ecccurve_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslservice_ecccurve_binding
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
				updateresource = sslservice_ecccurve_binding()
				updateresource.servicename = resource.servicename
				updateresource.ecccurvename = resource.ecccurvename
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslservice_ecccurve_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicename = resource[i].servicename
						updateresources[i].ecccurvename = resource[i].ecccurvename
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslservice_ecccurve_binding()
				deleteresource.servicename = resource.servicename
				deleteresource.ecccurvename = resource.ecccurvename
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslservice_ecccurve_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].servicename = resource[i].servicename
						deleteresources[i].ecccurvename = resource[i].ecccurvename
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, servicename) :
		ur""" Use this API to fetch sslservice_ecccurve_binding resources.
		"""
		try :
			obj = sslservice_ecccurve_binding()
			obj.servicename = servicename
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicename, filter_) :
		ur""" Use this API to fetch filtered set of sslservice_ecccurve_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservice_ecccurve_binding()
			obj.servicename = servicename
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicename) :
		ur""" Use this API to count sslservice_ecccurve_binding resources configued on NetScaler.
		"""
		try :
			obj = sslservice_ecccurve_binding()
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
		ur""" Use this API to count the filtered set of sslservice_ecccurve_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservice_ecccurve_binding()
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

	class Ecccurvename:
		ALL = "ALL"
		P_224 = "P_224"
		P_256 = "P_256"
		P_384 = "P_384"
		P_521 = "P_521"

	class Labeltype:
		vserver = "vserver"
		service = "service"
		policylabel = "policylabel"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

class sslservice_ecccurve_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslservice_ecccurve_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslservice_ecccurve_binding = [sslservice_ecccurve_binding() for _ in range(length)]

