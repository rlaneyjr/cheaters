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

class sslcertkey_sslvserver_binding(base_resource) :
	""" Binding class showing the sslvserver that can be bound to sslcertkey.
	"""
	def __init__(self) :
		self._servername = ""
		self._data = 0
		self._version = 0
		self._certkey = ""
		self._vservername = ""
		self._vserver = False
		self._ca = False
		self._crlcheck = ""
		self.___count = 0

	@property
	def vserver(self) :
		ur"""Specify this option to bind the certificate to an SSL virtual server.
		Note: The default option is -vServer.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		ur"""Specify this option to bind the certificate to an SSL virtual server.
		Note: The default option is -vServer.
		"""
		try :
			self._vserver = vserver
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
	def vservername(self) :
		ur"""The name of the SSL virtual server name to which the certificate-key pair needs to be bound.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		ur"""The name of the SSL virtual server name to which the certificate-key pair needs to be bound.
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def servername(self) :
		ur"""Vserver name to which the certificate key pair is bound.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		ur"""Vserver name to which the certificate key pair is bound.
		"""
		try :
			self._servername = servername
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
	def version(self) :
		ur"""Version.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@property
	def data(self) :
		ur"""Vserver Id.
		"""
		try :
			return self._data
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcertkey_sslvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcertkey_sslvserver_binding
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
	def get(cls, service, certkey) :
		ur""" Use this API to fetch sslcertkey_sslvserver_binding resources.
		"""
		try :
			obj = sslcertkey_sslvserver_binding()
			obj.certkey = certkey
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, certkey, filter_) :
		ur""" Use this API to fetch filtered set of sslcertkey_sslvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey_sslvserver_binding()
			obj.certkey = certkey
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, certkey) :
		ur""" Use this API to count sslcertkey_sslvserver_binding resources configued on NetScaler.
		"""
		try :
			obj = sslcertkey_sslvserver_binding()
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
		ur""" Use this API to count the filtered set of sslcertkey_sslvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey_sslvserver_binding()
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

class sslcertkey_sslvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcertkey_sslvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcertkey_sslvserver_binding = [sslcertkey_sslvserver_binding() for _ in range(length)]

