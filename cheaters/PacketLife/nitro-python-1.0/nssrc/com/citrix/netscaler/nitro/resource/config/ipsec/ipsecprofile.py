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

class ipsecprofile(base_resource) :
	""" Configuration for IPSEC profile resource. """
	def __init__(self) :
		self._name = ""
		self._ikeversion = ""
		self._encalgo = []
		self._hashalgo = []
		self._lifetime = 0
		self._psk = ""
		self._publickey = ""
		self._privatekey = ""
		self._peerpublickey = ""
		self._livenesscheckinterval = 0
		self._replaywindowsize = 0
		self._ikeretryinterval = 0
		self._retransmissiontime = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""The name of the ipsec profile.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""The name of the ipsec profile.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ikeversion(self) :
		ur"""IKE Protocol Version.<br/>Possible values = V1, V2.
		"""
		try :
			return self._ikeversion
		except Exception as e:
			raise e

	@ikeversion.setter
	def ikeversion(self, ikeversion) :
		ur"""IKE Protocol Version.<br/>Possible values = V1, V2
		"""
		try :
			self._ikeversion = ikeversion
		except Exception as e:
			raise e

	@property
	def encalgo(self) :
		ur"""Type of encryption algorithm.<br/>Possible values = AES, 3DES.
		"""
		try :
			return self._encalgo
		except Exception as e:
			raise e

	@encalgo.setter
	def encalgo(self, encalgo) :
		ur"""Type of encryption algorithm.<br/>Possible values = AES, 3DES
		"""
		try :
			self._encalgo = encalgo
		except Exception as e:
			raise e

	@property
	def hashalgo(self) :
		ur"""Type of hashing algorithm.<br/>Possible values = HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5.
		"""
		try :
			return self._hashalgo
		except Exception as e:
			raise e

	@hashalgo.setter
	def hashalgo(self, hashalgo) :
		ur"""Type of hashing algorithm.<br/>Possible values = HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5
		"""
		try :
			self._hashalgo = hashalgo
		except Exception as e:
			raise e

	@property
	def lifetime(self) :
		ur"""Lifetime of IKE SA in seconds. Lifetime of IPSec SA will be (lifetime of IKE SA/8).<br/>Minimum length =  480<br/>Maximum length =  31536000.
		"""
		try :
			return self._lifetime
		except Exception as e:
			raise e

	@lifetime.setter
	def lifetime(self, lifetime) :
		ur"""Lifetime of IKE SA in seconds. Lifetime of IPSec SA will be (lifetime of IKE SA/8).<br/>Minimum length =  480<br/>Maximum length =  31536000
		"""
		try :
			self._lifetime = lifetime
		except Exception as e:
			raise e

	@property
	def psk(self) :
		ur"""Pre shared key value.
		"""
		try :
			return self._psk
		except Exception as e:
			raise e

	@psk.setter
	def psk(self, psk) :
		ur"""Pre shared key value.
		"""
		try :
			self._psk = psk
		except Exception as e:
			raise e

	@property
	def publickey(self) :
		ur"""Public key file path.
		"""
		try :
			return self._publickey
		except Exception as e:
			raise e

	@publickey.setter
	def publickey(self, publickey) :
		ur"""Public key file path.
		"""
		try :
			self._publickey = publickey
		except Exception as e:
			raise e

	@property
	def privatekey(self) :
		ur"""Private key file path.
		"""
		try :
			return self._privatekey
		except Exception as e:
			raise e

	@privatekey.setter
	def privatekey(self, privatekey) :
		ur"""Private key file path.
		"""
		try :
			self._privatekey = privatekey
		except Exception as e:
			raise e

	@property
	def peerpublickey(self) :
		ur"""Peer public key file path.
		"""
		try :
			return self._peerpublickey
		except Exception as e:
			raise e

	@peerpublickey.setter
	def peerpublickey(self, peerpublickey) :
		ur"""Peer public key file path.
		"""
		try :
			self._peerpublickey = peerpublickey
		except Exception as e:
			raise e

	@property
	def livenesscheckinterval(self) :
		ur"""Number of seconds after which a notify payload is sent to check the liveliness of the peer. Additional retries are done as per retransmit interval setting. Zero value disables liveliness checks.<br/>Maximum length =  64999.
		"""
		try :
			return self._livenesscheckinterval
		except Exception as e:
			raise e

	@livenesscheckinterval.setter
	def livenesscheckinterval(self, livenesscheckinterval) :
		ur"""Number of seconds after which a notify payload is sent to check the liveliness of the peer. Additional retries are done as per retransmit interval setting. Zero value disables liveliness checks.<br/>Maximum length =  64999
		"""
		try :
			self._livenesscheckinterval = livenesscheckinterval
		except Exception as e:
			raise e

	@property
	def replaywindowsize(self) :
		ur"""IPSec Replay window size for the data traffic.<br/>Maximum length =  16384.
		"""
		try :
			return self._replaywindowsize
		except Exception as e:
			raise e

	@replaywindowsize.setter
	def replaywindowsize(self, replaywindowsize) :
		ur"""IPSec Replay window size for the data traffic.<br/>Maximum length =  16384
		"""
		try :
			self._replaywindowsize = replaywindowsize
		except Exception as e:
			raise e

	@property
	def ikeretryinterval(self) :
		ur"""IKE retry interval for bringing up the connection.<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._ikeretryinterval
		except Exception as e:
			raise e

	@ikeretryinterval.setter
	def ikeretryinterval(self, ikeretryinterval) :
		ur"""IKE retry interval for bringing up the connection.<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._ikeretryinterval = ikeretryinterval
		except Exception as e:
			raise e

	@property
	def retransmissiontime(self) :
		ur"""The interval in seconds to retry sending the IKE messages to peer, three consecutive attempts are done with doubled interval after every failure.<br/>Minimum length =  1<br/>Maximum length =  99.
		"""
		try :
			return self._retransmissiontime
		except Exception as e:
			raise e

	@retransmissiontime.setter
	def retransmissiontime(self, retransmissiontime) :
		ur"""The interval in seconds to retry sending the IKE messages to peer, three consecutive attempts are done with doubled interval after every failure.<br/>Minimum length =  1<br/>Maximum length =  99
		"""
		try :
			self._retransmissiontime = retransmissiontime
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ipsecprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipsecprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add ipsecprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = ipsecprofile()
				addresource.name = resource.name
				addresource.ikeversion = resource.ikeversion
				addresource.encalgo = resource.encalgo
				addresource.hashalgo = resource.hashalgo
				addresource.lifetime = resource.lifetime
				addresource.psk = resource.psk
				addresource.publickey = resource.publickey
				addresource.privatekey = resource.privatekey
				addresource.peerpublickey = resource.peerpublickey
				addresource.livenesscheckinterval = resource.livenesscheckinterval
				addresource.replaywindowsize = resource.replaywindowsize
				addresource.ikeretryinterval = resource.ikeretryinterval
				addresource.retransmissiontime = resource.retransmissiontime
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ ipsecprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].ikeversion = resource[i].ikeversion
						addresources[i].encalgo = resource[i].encalgo
						addresources[i].hashalgo = resource[i].hashalgo
						addresources[i].lifetime = resource[i].lifetime
						addresources[i].psk = resource[i].psk
						addresources[i].publickey = resource[i].publickey
						addresources[i].privatekey = resource[i].privatekey
						addresources[i].peerpublickey = resource[i].peerpublickey
						addresources[i].livenesscheckinterval = resource[i].livenesscheckinterval
						addresources[i].replaywindowsize = resource[i].replaywindowsize
						addresources[i].ikeretryinterval = resource[i].ikeretryinterval
						addresources[i].retransmissiontime = resource[i].retransmissiontime
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete ipsecprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ipsecprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ ipsecprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ ipsecprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the ipsecprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ipsecprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = ipsecprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [ipsecprofile() for _ in range(len(name))]
							obj = [ipsecprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = ipsecprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of ipsecprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipsecprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the ipsecprofile resources configured on NetScaler.
		"""
		try :
			obj = ipsecprofile()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of ipsecprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ipsecprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

	class Encalgo:
		AES = "AES"
		_3DES = "3DES"

	class Ikeversion:
		V1 = "V1"
		V2 = "V2"

	class Hashalgo:
		HMAC_SHA1 = "HMAC_SHA1"
		HMAC_SHA256 = "HMAC_SHA256"
		HMAC_SHA384 = "HMAC_SHA384"
		HMAC_SHA512 = "HMAC_SHA512"
		HMAC_MD5 = "HMAC_MD5"

class ipsecprofile_response(base_response) :
	def __init__(self, length=1) :
		self.ipsecprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ipsecprofile = [ipsecprofile() for _ in range(length)]

