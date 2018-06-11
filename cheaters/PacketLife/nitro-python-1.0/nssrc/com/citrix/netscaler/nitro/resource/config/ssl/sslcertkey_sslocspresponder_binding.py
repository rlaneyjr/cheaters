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

class sslcertkey_sslocspresponder_binding(base_resource) :
	""" Binding class showing the sslocspresponder that can be bound to sslcertkey.
	"""
	def __init__(self) :
		self._ocspresponder = ""
		self._priority = 0
		self._certkey = ""
		self._ca = False
		self._crlcheck = ""
		self.___count = 0

	@property
	def priority(self) :
		ur"""ocsp priority.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""ocsp priority.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def crlcheck(self) :
		ur"""The rule for use of CRL corresponding to this CA certificate during client authentication. If crlCheck is set to Mandatory, the system will deny all SSL clients if the CRL is missing, expired - NextUpdate date is in the past, or is incomplete with remote CRL refresh enabled. If crlCheck is set to optional, the system will allow SSL clients in the above error cases.However, in any case if the client certificate is revoked in the CRL, the SSL client will be denied access.<br/>Default value: CRLCHECK_OPTIONAL<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@crlcheck.setter
	def crlcheck(self, crlcheck) :
		ur"""The rule for use of CRL corresponding to this CA certificate during client authentication. If crlCheck is set to Mandatory, the system will deny all SSL clients if the CRL is missing, expired - NextUpdate date is in the past, or is incomplete with remote CRL refresh enabled. If crlCheck is set to optional, the system will allow SSL clients in the above error cases.However, in any case if the client certificate is revoked in the CRL, the SSL client will be denied access.<br/>Default value: CRLCHECK_OPTIONAL<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._crlcheck = crlcheck
		except Exception as e:
			raise e

	@property
	def ca(self) :
		ur"""If this option is specified, it indicates that the certificate-key pair being bound to the SSL virtual server is a CA certificate. If this option is not specified, the certificate-key pair is bound as a normal server certificate.
		Note: In case of a normal server certificate, the certificate-key pair should consist of both the certificate and the private-key.
		"""
		try :
			return self._ca
		except Exception as e:
			raise e

	@ca.setter
	def ca(self, ca) :
		ur"""If this option is specified, it indicates that the certificate-key pair being bound to the SSL virtual server is a CA certificate. If this option is not specified, the certificate-key pair is bound as a normal server certificate.
		Note: In case of a normal server certificate, the certificate-key pair should consist of both the certificate and the private-key.
		"""
		try :
			self._ca = ca
		except Exception as e:
			raise e

	@property
	def certkey(self) :
		ur"""Name of the certificate-key pair.<br/>Minimum length =  1.
		"""
		try :
			return self._certkey
		except Exception as e:
			raise e

	@certkey.setter
	def certkey(self, certkey) :
		ur"""Name of the certificate-key pair.<br/>Minimum length =  1
		"""
		try :
			self._certkey = certkey
		except Exception as e:
			raise e

	@property
	def ocspresponder(self) :
		ur"""OCSP responders bound to this certkey.
		"""
		try :
			return self._ocspresponder
		except Exception as e:
			raise e

	@ocspresponder.setter
	def ocspresponder(self, ocspresponder) :
		ur"""OCSP responders bound to this certkey.
		"""
		try :
			self._ocspresponder = ocspresponder
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcertkey_sslocspresponder_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcertkey_sslocspresponder_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.certkey is not None :
				return str(self.certkey)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = sslcertkey_sslocspresponder_binding()
				updateresource.certkey = resource.certkey
				updateresource.ocspresponder = resource.ocspresponder
				updateresource.priority = resource.priority
				updateresource.ca = resource.ca
				updateresource.crlcheck = resource.crlcheck
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslcertkey_sslocspresponder_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].certkey = resource[i].certkey
						updateresources[i].ocspresponder = resource[i].ocspresponder
						updateresources[i].priority = resource[i].priority
						updateresources[i].ca = resource[i].ca
						updateresources[i].crlcheck = resource[i].crlcheck
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = sslcertkey_sslocspresponder_binding()
				deleteresource.certkey = resource.certkey
				deleteresource.ocspresponder = resource.ocspresponder
				deleteresource.ca = resource.ca
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslcertkey_sslocspresponder_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].certkey = resource[i].certkey
						deleteresources[i].ocspresponder = resource[i].ocspresponder
						deleteresources[i].ca = resource[i].ca
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, certkey) :
		ur""" Use this API to fetch sslcertkey_sslocspresponder_binding resources.
		"""
		try :
			obj = sslcertkey_sslocspresponder_binding()
			obj.certkey = certkey
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, certkey, filter_) :
		ur""" Use this API to fetch filtered set of sslcertkey_sslocspresponder_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey_sslocspresponder_binding()
			obj.certkey = certkey
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, certkey) :
		ur""" Use this API to count sslcertkey_sslocspresponder_binding resources configued on NetScaler.
		"""
		try :
			obj = sslcertkey_sslocspresponder_binding()
			obj.certkey = certkey
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, certkey, filter_) :
		ur""" Use this API to count the filtered set of sslcertkey_sslocspresponder_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey_sslocspresponder_binding()
			obj.certkey = certkey
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

class sslcertkey_sslocspresponder_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcertkey_sslocspresponder_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcertkey_sslocspresponder_binding = [sslcertkey_sslocspresponder_binding() for _ in range(length)]

