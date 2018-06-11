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

class sslparameter(base_resource) :
	""" Configuration for SSL parameter resource. """
	def __init__(self) :
		self._quantumsize = ""
		self._crlmemorysizemb = 0
		self._strictcachecks = ""
		self._ssltriggertimeout = 0
		self._sendclosenotify = ""
		self._encrypttriggerpktcount = 0
		self._denysslreneg = ""
		self._insertionencoding = ""
		self._ocspcachesize = 0
		self._pushflag = 0
		self._dropreqwithnohostheader = ""
		self._pushenctriggertimeout = 0
		self._cryptodevdisablelimit = 0
		self._undefactioncontrol = ""
		self._undefactiondata = ""

	@property
	def quantumsize(self) :
		ur"""Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384.
		"""
		try :
			return self._quantumsize
		except Exception as e:
			raise e

	@quantumsize.setter
	def quantumsize(self, quantumsize) :
		ur"""Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384
		"""
		try :
			self._quantumsize = quantumsize
		except Exception as e:
			raise e

	@property
	def crlmemorysizemb(self) :
		ur"""Maximum memory size to use for certificate revocation lists (CRLs). This parameter reserves memory for a CRL but sets a limit to the maximum memory that the CRLs loaded on the appliance can consume.<br/>Default value: 256<br/>Minimum length =  10<br/>Maximum length =  1024.
		"""
		try :
			return self._crlmemorysizemb
		except Exception as e:
			raise e

	@crlmemorysizemb.setter
	def crlmemorysizemb(self, crlmemorysizemb) :
		ur"""Maximum memory size to use for certificate revocation lists (CRLs). This parameter reserves memory for a CRL but sets a limit to the maximum memory that the CRLs loaded on the appliance can consume.<br/>Default value: 256<br/>Minimum length =  10<br/>Maximum length =  1024
		"""
		try :
			self._crlmemorysizemb = crlmemorysizemb
		except Exception as e:
			raise e

	@property
	def strictcachecks(self) :
		ur"""Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._strictcachecks
		except Exception as e:
			raise e

	@strictcachecks.setter
	def strictcachecks(self, strictcachecks) :
		ur"""Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._strictcachecks = strictcachecks
		except Exception as e:
			raise e

	@property
	def ssltriggertimeout(self) :
		ur"""Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the NetScaler appliance because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200.
		"""
		try :
			return self._ssltriggertimeout
		except Exception as e:
			raise e

	@ssltriggertimeout.setter
	def ssltriggertimeout(self, ssltriggertimeout) :
		ur"""Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the NetScaler appliance because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200
		"""
		try :
			self._ssltriggertimeout = ssltriggertimeout
		except Exception as e:
			raise e

	@property
	def sendclosenotify(self) :
		ur"""Send an SSL Close-Notify message to the client at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._sendclosenotify
		except Exception as e:
			raise e

	@sendclosenotify.setter
	def sendclosenotify(self, sendclosenotify) :
		ur"""Send an SSL Close-Notify message to the client at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._sendclosenotify = sendclosenotify
		except Exception as e:
			raise e

	@property
	def encrypttriggerpktcount(self) :
		ur"""Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to NetScaler.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50.
		"""
		try :
			return self._encrypttriggerpktcount
		except Exception as e:
			raise e

	@encrypttriggerpktcount.setter
	def encrypttriggerpktcount(self, encrypttriggerpktcount) :
		ur"""Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to NetScaler.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50
		"""
		try :
			self._encrypttriggerpktcount = encrypttriggerpktcount
		except Exception as e:
			raise e

	@property
	def denysslreneg(self) :
		ur"""Deny renegotiation in specified circumstances. Available settings function as follows:
		* NO - Allow SSL renegotiation.
		* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
		* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the NetScaler during policy-based client authentication. 
		* ALL - Deny all secure and nonsecure SSL renegotiation.
		* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE.
		"""
		try :
			return self._denysslreneg
		except Exception as e:
			raise e

	@denysslreneg.setter
	def denysslreneg(self, denysslreneg) :
		ur"""Deny renegotiation in specified circumstances. Available settings function as follows:
		* NO - Allow SSL renegotiation.
		* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
		* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the NetScaler during policy-based client authentication. 
		* ALL - Deny all secure and nonsecure SSL renegotiation.
		* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE
		"""
		try :
			self._denysslreneg = denysslreneg
		except Exception as e:
			raise e

	@property
	def insertionencoding(self) :
		ur"""Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8.
		"""
		try :
			return self._insertionencoding
		except Exception as e:
			raise e

	@insertionencoding.setter
	def insertionencoding(self, insertionencoding) :
		ur"""Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8
		"""
		try :
			self._insertionencoding = insertionencoding
		except Exception as e:
			raise e

	@property
	def ocspcachesize(self) :
		ur"""Size, per packet engine, in megabytes, of the OCSP cache. A maximum of 10% of the packet engine memory can be assigned. Because the maximum allowed packet engine memory is 4GB, the maximum value that can be assigned to the OCSP cache is approximately 410 MB.<br/>Default value: 10<br/>Maximum length =  512.
		"""
		try :
			return self._ocspcachesize
		except Exception as e:
			raise e

	@ocspcachesize.setter
	def ocspcachesize(self, ocspcachesize) :
		ur"""Size, per packet engine, in megabytes, of the OCSP cache. A maximum of 10% of the packet engine memory can be assigned. Because the maximum allowed packet engine memory is 4GB, the maximum value that can be assigned to the OCSP cache is approximately 410 MB.<br/>Default value: 10<br/>Maximum length =  512
		"""
		try :
			self._ocspcachesize = ocspcachesize
		except Exception as e:
			raise e

	@property
	def pushflag(self) :
		ur"""Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
		0 - Auto (PUSH flag is not set.)
		1 - Insert PUSH flag into every decrypted record.
		2 -Insert PUSH flag into every encrypted record.
		3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3.
		"""
		try :
			return self._pushflag
		except Exception as e:
			raise e

	@pushflag.setter
	def pushflag(self, pushflag) :
		ur"""Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
		0 - Auto (PUSH flag is not set.)
		1 - Insert PUSH flag into every decrypted record.
		2 -Insert PUSH flag into every encrypted record.
		3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3
		"""
		try :
			self._pushflag = pushflag
		except Exception as e:
			raise e

	@property
	def dropreqwithnohostheader(self) :
		ur"""Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._dropreqwithnohostheader
		except Exception as e:
			raise e

	@dropreqwithnohostheader.setter
	def dropreqwithnohostheader(self, dropreqwithnohostheader) :
		ur"""Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._dropreqwithnohostheader = dropreqwithnohostheader
		except Exception as e:
			raise e

	@property
	def pushenctriggertimeout(self) :
		ur"""PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200.
		"""
		try :
			return self._pushenctriggertimeout
		except Exception as e:
			raise e

	@pushenctriggertimeout.setter
	def pushenctriggertimeout(self, pushenctriggertimeout) :
		ur"""PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200
		"""
		try :
			self._pushenctriggertimeout = pushenctriggertimeout
		except Exception as e:
			raise e

	@property
	def cryptodevdisablelimit(self) :
		ur"""Disabled Crypto Device Limit reboots the system once reached.  A value of zero(0) implies no reboot. .<br/>Default value: 0.
		"""
		try :
			return self._cryptodevdisablelimit
		except Exception as e:
			raise e

	@cryptodevdisablelimit.setter
	def cryptodevdisablelimit(self, cryptodevdisablelimit) :
		ur"""Disabled Crypto Device Limit reboots the system once reached.  A value of zero(0) implies no reboot. .<br/>Default value: 0
		"""
		try :
			self._cryptodevdisablelimit = cryptodevdisablelimit
		except Exception as e:
			raise e

	@property
	def undefactioncontrol(self) :
		ur"""Name of the undefined built-in control action: CLIENTAUTH, NOCLIENTAUTH, NOOP, RESET, or DROP.<br/>Default value: "CLIENTAUTH".
		"""
		try :
			return self._undefactioncontrol
		except Exception as e:
			raise e

	@undefactioncontrol.setter
	def undefactioncontrol(self, undefactioncontrol) :
		ur"""Name of the undefined built-in control action: CLIENTAUTH, NOCLIENTAUTH, NOOP, RESET, or DROP.<br/>Default value: "CLIENTAUTH"
		"""
		try :
			self._undefactioncontrol = undefactioncontrol
		except Exception as e:
			raise e

	@property
	def undefactiondata(self) :
		ur"""Name of the undefined built-in data action: NOOP, RESET or DROP.<br/>Default value: "NOOP".
		"""
		try :
			return self._undefactiondata
		except Exception as e:
			raise e

	@undefactiondata.setter
	def undefactiondata(self, undefactiondata) :
		ur"""Name of the undefined built-in data action: NOOP, RESET or DROP.<br/>Default value: "NOOP"
		"""
		try :
			self._undefactiondata = undefactiondata
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslparameter
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
	def update(cls, client, resource) :
		ur""" Use this API to update sslparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslparameter()
				updateresource.quantumsize = resource.quantumsize
				updateresource.crlmemorysizemb = resource.crlmemorysizemb
				updateresource.strictcachecks = resource.strictcachecks
				updateresource.ssltriggertimeout = resource.ssltriggertimeout
				updateresource.sendclosenotify = resource.sendclosenotify
				updateresource.encrypttriggerpktcount = resource.encrypttriggerpktcount
				updateresource.denysslreneg = resource.denysslreneg
				updateresource.insertionencoding = resource.insertionencoding
				updateresource.ocspcachesize = resource.ocspcachesize
				updateresource.pushflag = resource.pushflag
				updateresource.dropreqwithnohostheader = resource.dropreqwithnohostheader
				updateresource.pushenctriggertimeout = resource.pushenctriggertimeout
				updateresource.cryptodevdisablelimit = resource.cryptodevdisablelimit
				updateresource.undefactioncontrol = resource.undefactioncontrol
				updateresource.undefactiondata = resource.undefactiondata
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of sslparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Denysslreneg:
		NO = "NO"
		FRONTEND_CLIENT = "FRONTEND_CLIENT"
		FRONTEND_CLIENTSERVER = "FRONTEND_CLIENTSERVER"
		ALL = "ALL"
		NONSECURE = "NONSECURE"

	class Insertionencoding:
		Unicode = "Unicode"
		UTF_8 = "UTF-8"

	class Strictcachecks:
		YES = "YES"
		NO = "NO"

	class Quantumsize:
		_4096 = "4096"
		_8192 = "8192"
		_16384 = "16384"

	class Sendclosenotify:
		YES = "YES"
		NO = "NO"

	class Dropreqwithnohostheader:
		YES = "YES"
		NO = "NO"

class sslparameter_response(base_response) :
	def __init__(self, length=1) :
		self.sslparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslparameter = [sslparameter() for _ in range(length)]

