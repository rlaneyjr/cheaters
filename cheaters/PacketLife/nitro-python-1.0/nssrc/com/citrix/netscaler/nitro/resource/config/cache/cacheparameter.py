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

class cacheparameter(base_resource) :
	""" Configuration for cache parameter resource. """
	def __init__(self) :
		self._memlimit = 0
		self._via = ""
		self._verifyusing = ""
		self._maxpostlen = 0
		self._prefetchmaxpending = 0
		self._enablebypass = ""
		self._undefaction = ""
		self._enablehaobjpersist = ""
		self._disklimit = 0
		self._maxdisklimit = 0
		self._memlimitactive = 0
		self._maxmemlimit = 0
		self._prefetchcur = 0

	@property
	def memlimit(self) :
		ur"""Amount of memory available for storing the cache objects. In practice, the amount of memory available for caching can be less than half the total memory of the NetScaler appliance.
		"""
		try :
			return self._memlimit
		except Exception as e:
			raise e

	@memlimit.setter
	def memlimit(self, memlimit) :
		ur"""Amount of memory available for storing the cache objects. In practice, the amount of memory available for caching can be less than half the total memory of the NetScaler appliance.
		"""
		try :
			self._memlimit = memlimit
		except Exception as e:
			raise e

	@property
	def via(self) :
		ur"""String to include in the Via header. A Via header is inserted into all responses served from a content group if its Insert Via flag is set.<br/>Minimum length =  1.
		"""
		try :
			return self._via
		except Exception as e:
			raise e

	@via.setter
	def via(self, via) :
		ur"""String to include in the Via header. A Via header is inserted into all responses served from a content group if its Insert Via flag is set.<br/>Minimum length =  1
		"""
		try :
			self._via = via
		except Exception as e:
			raise e

	@property
	def verifyusing(self) :
		ur"""Criteria for deciding whether a cached object can be served for an incoming HTTP request. Available settings function as follows:
		HOSTNAME - The URL, host name, and host port values in the incoming HTTP request header must match the cache policy. The IP address and the TCP port of the destination host are not evaluated. Do not use the HOSTNAME setting unless you are certain that no rogue client can access a rogue server through the cache. 
		HOSTNAME_AND_IP - The URL, host name, host port in the incoming HTTP request header, and the IP address and TCP port of
		the destination server, must match the cache policy.
		DNS - The URL, host name and host port in the incoming HTTP request, and the TCP port must match the cache policy. The host name is used for DNS lookup of the destination server's IP address, and is compared with the set of addresses returned by the DNS lookup.<br/>Possible values = HOSTNAME, HOSTNAME_AND_IP, DNS.
		"""
		try :
			return self._verifyusing
		except Exception as e:
			raise e

	@verifyusing.setter
	def verifyusing(self, verifyusing) :
		ur"""Criteria for deciding whether a cached object can be served for an incoming HTTP request. Available settings function as follows:
		HOSTNAME - The URL, host name, and host port values in the incoming HTTP request header must match the cache policy. The IP address and the TCP port of the destination host are not evaluated. Do not use the HOSTNAME setting unless you are certain that no rogue client can access a rogue server through the cache. 
		HOSTNAME_AND_IP - The URL, host name, host port in the incoming HTTP request header, and the IP address and TCP port of
		the destination server, must match the cache policy.
		DNS - The URL, host name and host port in the incoming HTTP request, and the TCP port must match the cache policy. The host name is used for DNS lookup of the destination server's IP address, and is compared with the set of addresses returned by the DNS lookup.<br/>Possible values = HOSTNAME, HOSTNAME_AND_IP, DNS
		"""
		try :
			self._verifyusing = verifyusing
		except Exception as e:
			raise e

	@property
	def maxpostlen(self) :
		ur"""Maximum number of POST body bytes to consider when evaluating parameters for a content group for which you have configured hit parameters and invalidation parameters.<br/>Default value: 4096<br/>Maximum length =  131072.
		"""
		try :
			return self._maxpostlen
		except Exception as e:
			raise e

	@maxpostlen.setter
	def maxpostlen(self, maxpostlen) :
		ur"""Maximum number of POST body bytes to consider when evaluating parameters for a content group for which you have configured hit parameters and invalidation parameters.<br/>Default value: 4096<br/>Maximum length =  131072
		"""
		try :
			self._maxpostlen = maxpostlen
		except Exception as e:
			raise e

	@property
	def prefetchmaxpending(self) :
		ur"""Maximum number of outstanding prefetches in the Integrated Cache.
		"""
		try :
			return self._prefetchmaxpending
		except Exception as e:
			raise e

	@prefetchmaxpending.setter
	def prefetchmaxpending(self, prefetchmaxpending) :
		ur"""Maximum number of outstanding prefetches in the Integrated Cache.
		"""
		try :
			self._prefetchmaxpending = prefetchmaxpending
		except Exception as e:
			raise e

	@property
	def enablebypass(self) :
		ur"""Evaluate the request-time policies before attempting hit selection. If set to NO, an incoming request for which a matching object is found in cache storage results in a response regardless of the policy configuration.
		If the request matches a policy with a NOCACHE action, the request bypasses all cache processing. 
		This parameter does not affect processing of requests that match any invalidation policy.<br/>Possible values = YES, NO.
		"""
		try :
			return self._enablebypass
		except Exception as e:
			raise e

	@enablebypass.setter
	def enablebypass(self, enablebypass) :
		ur"""Evaluate the request-time policies before attempting hit selection. If set to NO, an incoming request for which a matching object is found in cache storage results in a response regardless of the policy configuration.
		If the request matches a policy with a NOCACHE action, the request bypasses all cache processing. 
		This parameter does not affect processing of requests that match any invalidation policy.<br/>Possible values = YES, NO
		"""
		try :
			self._enablebypass = enablebypass
		except Exception as e:
			raise e

	@property
	def undefaction(self) :
		ur"""Action to take when a policy cannot be evaluated.<br/>Possible values = NOCACHE, RESET.
		"""
		try :
			return self._undefaction
		except Exception as e:
			raise e

	@undefaction.setter
	def undefaction(self, undefaction) :
		ur"""Action to take when a policy cannot be evaluated.<br/>Possible values = NOCACHE, RESET
		"""
		try :
			self._undefaction = undefaction
		except Exception as e:
			raise e

	@property
	def enablehaobjpersist(self) :
		ur"""The HA object persisting parameter. When this value is set to YES, cache objects can be synced to Secondary in a HA deployment.  If set to NO, objects will never be synced to Secondary node.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._enablehaobjpersist
		except Exception as e:
			raise e

	@enablehaobjpersist.setter
	def enablehaobjpersist(self, enablehaobjpersist) :
		ur"""The HA object persisting parameter. When this value is set to YES, cache objects can be synced to Secondary in a HA deployment.  If set to NO, objects will never be synced to Secondary node.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._enablehaobjpersist = enablehaobjpersist
		except Exception as e:
			raise e

	@property
	def disklimit(self) :
		ur"""The disk limit for the Integrated Cache.
		"""
		try :
			return self._disklimit
		except Exception as e:
			raise e

	@property
	def maxdisklimit(self) :
		ur"""The maximum value of the memory limit for the Integrated Cache.
		"""
		try :
			return self._maxdisklimit
		except Exception as e:
			raise e

	@property
	def memlimitactive(self) :
		ur"""Active value of the memory limit for the Integrated Cache.
		"""
		try :
			return self._memlimitactive
		except Exception as e:
			raise e

	@property
	def maxmemlimit(self) :
		ur"""The maximum value of the memory limit for the Integrated Cache.
		"""
		try :
			return self._maxmemlimit
		except Exception as e:
			raise e

	@property
	def prefetchcur(self) :
		ur"""Number of current outstanding prefetches in the IC.
		"""
		try :
			return self._prefetchcur
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cacheparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cacheparameter
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
		ur""" Use this API to update cacheparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cacheparameter()
				updateresource.memlimit = resource.memlimit
				updateresource.via = resource.via
				updateresource.verifyusing = resource.verifyusing
				updateresource.maxpostlen = resource.maxpostlen
				updateresource.prefetchmaxpending = resource.prefetchmaxpending
				updateresource.enablebypass = resource.enablebypass
				updateresource.undefaction = resource.undefaction
				updateresource.enablehaobjpersist = resource.enablehaobjpersist
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of cacheparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cacheparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cacheparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cacheparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Verifyusing:
		HOSTNAME = "HOSTNAME"
		HOSTNAME_AND_IP = "HOSTNAME_AND_IP"
		DNS = "DNS"

	class Enablehaobjpersist:
		YES = "YES"
		NO = "NO"

	class Undefaction:
		NOCACHE = "NOCACHE"
		RESET = "RESET"

	class Enablebypass:
		YES = "YES"
		NO = "NO"

class cacheparameter_response(base_response) :
	def __init__(self, length=1) :
		self.cacheparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cacheparameter = [cacheparameter() for _ in range(length)]

