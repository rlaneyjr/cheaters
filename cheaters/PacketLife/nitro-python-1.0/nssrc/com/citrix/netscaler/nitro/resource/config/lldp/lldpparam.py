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

class lldpparam(base_resource) :
	""" Configuration for lldp params resource. """
	def __init__(self) :
		self._holdtimetxmult = 0
		self._timer = 0
		self._mode = ""

	@property
	def holdtimetxmult(self) :
		ur"""A multiplier for calculating the duration for which the receiving device stores the LLDP information in its database before discarding or removing it. The duration is calculated as the holdtimeTxMult (Holdtime Multiplier) parameter value multiplied by the timer (Timer) parameter value.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  20.
		"""
		try :
			return self._holdtimetxmult
		except Exception as e:
			raise e

	@holdtimetxmult.setter
	def holdtimetxmult(self, holdtimetxmult) :
		ur"""A multiplier for calculating the duration for which the receiving device stores the LLDP information in its database before discarding or removing it. The duration is calculated as the holdtimeTxMult (Holdtime Multiplier) parameter value multiplied by the timer (Timer) parameter value.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  20
		"""
		try :
			self._holdtimetxmult = holdtimetxmult
		except Exception as e:
			raise e

	@property
	def timer(self) :
		ur"""Interval, in seconds, between LLDP packet data units (LLDPDUs).  that the NetScaler ADC sends to a directly connected device.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  3000.
		"""
		try :
			return self._timer
		except Exception as e:
			raise e

	@timer.setter
	def timer(self, timer) :
		ur"""Interval, in seconds, between LLDP packet data units (LLDPDUs).  that the NetScaler ADC sends to a directly connected device.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  3000
		"""
		try :
			self._timer = timer
		except Exception as e:
			raise e

	@property
	def mode(self) :
		ur"""Global mode of Link Layer Discovery Protocol (LLDP) on the NetScaler ADC. The resultant LLDP mode of an interface depends on the LLDP mode configured at the global and the interface levels.<br/>Possible values = NONE, TRANSMITTER, RECEIVER, TRANSCEIVER.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		ur"""Global mode of Link Layer Discovery Protocol (LLDP) on the NetScaler ADC. The resultant LLDP mode of an interface depends on the LLDP mode configured at the global and the interface levels.<br/>Possible values = NONE, TRANSMITTER, RECEIVER, TRANSCEIVER
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lldpparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lldpparam
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
		ur""" Use this API to update lldpparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = lldpparam()
				updateresource.holdtimetxmult = resource.holdtimetxmult
				updateresource.timer = resource.timer
				updateresource.mode = resource.mode
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lldpparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lldpparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lldpparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lldpparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Mode:
		NONE = "NONE"
		TRANSMITTER = "TRANSMITTER"
		RECEIVER = "RECEIVER"
		TRANSCEIVER = "TRANSCEIVER"

class lldpparam_response(base_response) :
	def __init__(self, length=1) :
		self.lldpparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lldpparam = [lldpparam() for _ in range(length)]

