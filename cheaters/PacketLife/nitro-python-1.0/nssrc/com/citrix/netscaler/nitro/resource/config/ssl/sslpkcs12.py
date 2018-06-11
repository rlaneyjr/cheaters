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

class sslpkcs12(base_resource) :
	""" Configuration for pkcs12 resource. """
	def __init__(self) :
		self._outfile = ""
		self._Import = False
		self._pkcs12file = ""
		self._des = False
		self._des3 = False
		self._export = False
		self._certfile = ""
		self._keyfile = ""
		self._password = ""
		self._pempassphrase = ""

	@property
	def outfile(self) :
		ur"""Name for and, optionally, path to, the output file that contains the certificate and the private key after converting from PKCS#12 to PEM format. /nsconfig/ssl/ is the default path.
		If importing, the certificate-key pair is stored in PEM format. If exporting, the certificate-key pair is stored in PKCS#12 format.<br/>Maximum length =  63.
		"""
		try :
			return self._outfile
		except Exception as e:
			raise e

	@outfile.setter
	def outfile(self, outfile) :
		ur"""Name for and, optionally, path to, the output file that contains the certificate and the private key after converting from PKCS#12 to PEM format. /nsconfig/ssl/ is the default path.
		If importing, the certificate-key pair is stored in PEM format. If exporting, the certificate-key pair is stored in PKCS#12 format.<br/>Maximum length =  63
		"""
		try :
			self._outfile = outfile
		except Exception as e:
			raise e

	@property
	def Import(self) :
		ur"""Convert the certificate and private-key from PKCS#12 format to PEM format.
		"""
		try :
			return self._Import
		except Exception as e:
			raise e

	@Import.setter
	def Import(self, Import) :
		ur"""Convert the certificate and private-key from PKCS#12 format to PEM format.
		"""
		try :
			self._Import = Import
		except Exception as e:
			raise e

	@property
	def pkcs12file(self) :
		ur"""Name for and, optionally, path to, the PKCS#12 file. If importing, specify the input file name that contains the certificate and the private key in PKCS#12 format. If exporting, specify the output file name that contains the certificate and the private key after converting from PEM to
		PKCS#12 format. /nsconfig/ssl/ is the default path.
		During the import operation, if the key is encrypted, you are prompted to enter the pass phrase used for encrypting the key.<br/>Maximum length =  63.
		"""
		try :
			return self._pkcs12file
		except Exception as e:
			raise e

	@pkcs12file.setter
	def pkcs12file(self, pkcs12file) :
		ur"""Name for and, optionally, path to, the PKCS#12 file. If importing, specify the input file name that contains the certificate and the private key in PKCS#12 format. If exporting, specify the output file name that contains the certificate and the private key after converting from PEM to
		PKCS#12 format. /nsconfig/ssl/ is the default path.
		During the import operation, if the key is encrypted, you are prompted to enter the pass phrase used for encrypting the key.<br/>Maximum length =  63
		"""
		try :
			self._pkcs12file = pkcs12file
		except Exception as e:
			raise e

	@property
	def des(self) :
		ur"""Encrypt the private key by using the DES algorithm in CBC mode during the import operation. On the command line, you are prompted to enter the pass phrase.
		"""
		try :
			return self._des
		except Exception as e:
			raise e

	@des.setter
	def des(self, des) :
		ur"""Encrypt the private key by using the DES algorithm in CBC mode during the import operation. On the command line, you are prompted to enter the pass phrase.
		"""
		try :
			self._des = des
		except Exception as e:
			raise e

	@property
	def des3(self) :
		ur"""Encrypt the private key by using the Triple-DES algorithm in EDE CBC mode (168-bit key) during the import operation. On the command line, you are prompted to enter the pass phrase.
		"""
		try :
			return self._des3
		except Exception as e:
			raise e

	@des3.setter
	def des3(self, des3) :
		ur"""Encrypt the private key by using the Triple-DES algorithm in EDE CBC mode (168-bit key) during the import operation. On the command line, you are prompted to enter the pass phrase.
		"""
		try :
			self._des3 = des3
		except Exception as e:
			raise e

	@property
	def export(self) :
		ur"""Convert the certificate and private key from PEM format to PKCS#12 format. On the command line, you are prompted to enter the pass phrase.
		"""
		try :
			return self._export
		except Exception as e:
			raise e

	@export.setter
	def export(self, export) :
		ur"""Convert the certificate and private key from PEM format to PKCS#12 format. On the command line, you are prompted to enter the pass phrase.
		"""
		try :
			self._export = export
		except Exception as e:
			raise e

	@property
	def certfile(self) :
		ur"""Certificate file to be converted from PEM to PKCS#12 format.<br/>Maximum length =  63.
		"""
		try :
			return self._certfile
		except Exception as e:
			raise e

	@certfile.setter
	def certfile(self, certfile) :
		ur"""Certificate file to be converted from PEM to PKCS#12 format.<br/>Maximum length =  63
		"""
		try :
			self._certfile = certfile
		except Exception as e:
			raise e

	@property
	def keyfile(self) :
		ur"""Name of the private key file to be converted from PEM to PKCS#12 format. If the key file is encrypted, you are prompted to enter the pass phrase used for encrypting the key.<br/>Maximum length =  63.
		"""
		try :
			return self._keyfile
		except Exception as e:
			raise e

	@keyfile.setter
	def keyfile(self, keyfile) :
		ur"""Name of the private key file to be converted from PEM to PKCS#12 format. If the key file is encrypted, you are prompted to enter the pass phrase used for encrypting the key.<br/>Maximum length =  63
		"""
		try :
			self._keyfile = keyfile
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def pempassphrase(self) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._pempassphrase
		except Exception as e:
			raise e

	@pempassphrase.setter
	def pempassphrase(self, pempassphrase) :
		ur""".<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._pempassphrase = pempassphrase
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslpkcs12_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslpkcs12
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def convert(cls, client, resource) :
		ur""" Use this API to convert sslpkcs12.
		"""
		try :
			if type(resource) is not list :
				convertresource = sslpkcs12()
				convertresource.outfile = resource.outfile
				convertresource.Import = resource.Import
				convertresource.pkcs12file = resource.pkcs12file
				convertresource.des = resource.des
				convertresource.des3 = resource.des3
				convertresource.export = resource.export
				convertresource.certfile = resource.certfile
				convertresource.keyfile = resource.keyfile
				convertresource.password = resource.password
				convertresource.pempassphrase = resource.pempassphrase
				return convertresource.perform_operation(client,"convert")
		except Exception as e :
			raise e

class sslpkcs12_response(base_response) :
	def __init__(self, length=1) :
		self.sslpkcs12 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslpkcs12 = [sslpkcs12() for _ in range(length)]

