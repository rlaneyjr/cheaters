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

class sslservicegroup_sslcertkey_binding(base_resource) :
	""" Binding class showing the sslcertkey that can be bound to sslservicegroup.
	"""
	def __init__(self) :
		self._certkeyname = ""
		self._crlcheck = ""
		self._ocspcheck = ""
		self._ca = False
		self._snicert = False
		self._servicegroupname = ""
		self.___count = 0

	@property
	def servicegroupname(self) :
		ur"""The name of the SSL service to which the SSL policy needs to be bound.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		ur"""The name of the SSL service to which the SSL policy needs to be bound.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def ca(self) :
		ur"""CA certificate.
		"""
		try :
			return self._ca
		except Exception as e:
			raise e

	@ca.setter
	def ca(self, ca) :
		ur"""CA certificate.
		"""
		try :
			self._ca = ca
		except Exception as e:
			raise e

	@property
	def crlcheck(self) :
		ur"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@crlcheck.setter
	def crlcheck(self, crlcheck) :
		ur"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._crlcheck = crlcheck
		except Exception as e:
			raise e

	@property
	def certkeyname(self) :
		ur"""The name of the certificate bound to the SSL service group.
		"""
		try :
			return self._certkeyname
		except Exception as e:
			raise e

	@certkeyname.setter
	def certkeyname(self, certkeyname) :
		ur"""The name of the certificate bound to the SSL service group.
		"""
		try :
			self._certkeyname = certkeyname
		except Exception as e:
			raise e

	@property
	def snicert(self) :
		ur"""The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing.
		"""
		try :
			return self._snicert
		except Exception as e:
			raise e

	@snicert.setter
	def snicert(self, snicert) :
		ur"""The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing.
		"""
		try :
			self._snicert = snicert
		except Exception as e:
			raise e

	@property
	def ocspcheck(self) :
		ur"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._ocspcheck
		except Exception as e:
			raise e

	@ocspcheck.setter
	def ocspcheck(self, ocspcheck) :
		ur"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._ocspcheck = ocspcheck
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslservicegroup_sslcertkey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslservicegroup_sslcertkey_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = sslservicegroup_sslcertkey_binding()
				updateresource.servicegroupname = resource.servicegroupname
				updateresource.certkeyname = resource.certkeyname
				updateresource.ca = resource.ca
				updateresource.crlcheck = resource.crlcheck
				updateresource.snicert = resource.snicert
				updateresource.ocspcheck = resource.ocspcheck
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslservicegroup_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicegroupname = resource[i].servicegroupname
						updateresources[i].certkeyname = resource[i].certkeyname
						updateresources[i].ca = resource[i].ca
						updateresources[i].crlcheck = resource[i].crlcheck
						updateresources[i].snicert = resource[i].snicert
						updateresources[i].ocspcheck = resource[i].ocspcheck
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslservicegroup_sslcertkey_binding()
				deleteresource.servicegroupname = resource.servicegroupname
				deleteresource.certkeyname = resource.certkeyname
				deleteresource.ca = resource.ca
				deleteresource.crlcheck = resource.crlcheck
				deleteresource.snicert = resource.snicert
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslservicegroup_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].servicegroupname = resource[i].servicegroupname
						deleteresources[i].certkeyname = resource[i].certkeyname
						deleteresources[i].ca = resource[i].ca
						deleteresources[i].crlcheck = resource[i].crlcheck
						deleteresources[i].snicert = resource[i].snicert
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, servicegroupname) :
		ur""" Use this API to fetch sslservicegroup_sslcertkey_binding resources.
		"""
		try :
			obj = sslservicegroup_sslcertkey_binding()
			obj.servicegroupname = servicegroupname
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicegroupname, filter_) :
		ur""" Use this API to fetch filtered set of sslservicegroup_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup_sslcertkey_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicegroupname) :
		ur""" Use this API to count sslservicegroup_sslcertkey_binding resources configued on NetScaler.
		"""
		try :
			obj = sslservicegroup_sslcertkey_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, servicegroupname, filter_) :
		ur""" Use this API to count the filtered set of sslservicegroup_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup_sslcertkey_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

class sslservicegroup_sslcertkey_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslservicegroup_sslcertkey_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslservicegroup_sslcertkey_binding = [sslservicegroup_sslcertkey_binding() for _ in range(length)]

