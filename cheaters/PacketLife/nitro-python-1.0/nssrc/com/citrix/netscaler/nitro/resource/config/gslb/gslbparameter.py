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

class gslbparameter(base_resource) :
	""" Configuration for GSLB parameter resource. """
	def __init__(self) :
		self._ldnsentrytimeout = 0
		self._rtttolerance = 0
		self._ldnsmask = ""
		self._v6ldnsmasklen = 0
		self._ldnsprobeorder = []
		self._dropldnsreq = ""
		self._flags = 0

	@property
	def ldnsentrytimeout(self) :
		ur"""Time, in seconds, after which an inactive LDNS entry is removed.<br/>Default value: 180<br/>Minimum length =  30<br/>Maximum length =  65534.
		"""
		try :
			return self._ldnsentrytimeout
		except Exception as e:
			raise e

	@ldnsentrytimeout.setter
	def ldnsentrytimeout(self, ldnsentrytimeout) :
		ur"""Time, in seconds, after which an inactive LDNS entry is removed.<br/>Default value: 180<br/>Minimum length =  30<br/>Maximum length =  65534
		"""
		try :
			self._ldnsentrytimeout = ldnsentrytimeout
		except Exception as e:
			raise e

	@property
	def rtttolerance(self) :
		ur"""Tolerance, in milliseconds, for newly learned round-trip time (RTT) values. If the difference between the old RTT value and the newly computed RTT value is less than or equal to the specified tolerance value, the LDNS entry in the network metric table is not updated with the new RTT value. Prevents the exchange of metrics when variations in RTT values are negligible.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._rtttolerance
		except Exception as e:
			raise e

	@rtttolerance.setter
	def rtttolerance(self, rtttolerance) :
		ur"""Tolerance, in milliseconds, for newly learned round-trip time (RTT) values. If the difference between the old RTT value and the newly computed RTT value is less than or equal to the specified tolerance value, the LDNS entry in the network metric table is not updated with the new RTT value. Prevents the exchange of metrics when variations in RTT values are negligible.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._rtttolerance = rtttolerance
		except Exception as e:
			raise e

	@property
	def ldnsmask(self) :
		ur"""The IPv4 network mask with which to create LDNS entries.<br/>Minimum length =  1.
		"""
		try :
			return self._ldnsmask
		except Exception as e:
			raise e

	@ldnsmask.setter
	def ldnsmask(self, ldnsmask) :
		ur"""The IPv4 network mask with which to create LDNS entries.<br/>Minimum length =  1
		"""
		try :
			self._ldnsmask = ldnsmask
		except Exception as e:
			raise e

	@property
	def v6ldnsmasklen(self) :
		ur"""Mask for creating LDNS entries for IPv6 source addresses. The mask is defined as the number of leading bits to consider, in the source IP address, when creating an LDNS entry.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6ldnsmasklen
		except Exception as e:
			raise e

	@v6ldnsmasklen.setter
	def v6ldnsmasklen(self, v6ldnsmasklen) :
		ur"""Mask for creating LDNS entries for IPv6 source addresses. The mask is defined as the number of leading bits to consider, in the source IP address, when creating an LDNS entry.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6ldnsmasklen = v6ldnsmasklen
		except Exception as e:
			raise e

	@property
	def ldnsprobeorder(self) :
		ur"""Order in which monitors should be initiated to calculate RTT.<br/>Possible values = PING, DNS, TCP.
		"""
		try :
			return self._ldnsprobeorder
		except Exception as e:
			raise e

	@ldnsprobeorder.setter
	def ldnsprobeorder(self, ldnsprobeorder) :
		ur"""Order in which monitors should be initiated to calculate RTT.<br/>Possible values = PING, DNS, TCP
		"""
		try :
			self._ldnsprobeorder = ldnsprobeorder
		except Exception as e:
			raise e

	@property
	def dropldnsreq(self) :
		ur"""Drop LDNS requests if round-trip time (RTT) information is not available.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropldnsreq
		except Exception as e:
			raise e

	@dropldnsreq.setter
	def dropldnsreq(self, dropldnsreq) :
		ur"""Drop LDNS requests if round-trip time (RTT) information is not available.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropldnsreq = dropldnsreq
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""State of the GSLB parameter.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbparameter
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
		ur""" Use this API to update gslbparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = gslbparameter()
				updateresource.ldnsentrytimeout = resource.ldnsentrytimeout
				updateresource.rtttolerance = resource.rtttolerance
				updateresource.ldnsmask = resource.ldnsmask
				updateresource.v6ldnsmasklen = resource.v6ldnsmasklen
				updateresource.ldnsprobeorder = resource.ldnsprobeorder
				updateresource.dropldnsreq = resource.dropldnsreq
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of gslbparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = gslbparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the gslbparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Ldnsprobeorder:
		PING = "PING"
		DNS = "DNS"
		TCP = "TCP"

	class Dropldnsreq:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class gslbparameter_response(base_response) :
	def __init__(self, length=1) :
		self.gslbparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbparameter = [gslbparameter() for _ in range(length)]

