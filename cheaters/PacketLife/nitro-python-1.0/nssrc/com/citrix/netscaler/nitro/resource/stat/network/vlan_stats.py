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

class vlan_stats(base_resource) :
	ur""" Statistics for "VLAN" resource.
	"""
	def __init__(self) :
		self._id = 0
		self._clearstats = ""
		self._vlantotrxpkts = 0
		self._vlanrxpktsrate = 0
		self._vlantotrxbytes = 0
		self._vlanrxbytesrate = 0
		self._vlantottxpkts = 0
		self._vlantxpktsrate = 0
		self._vlantottxbytes = 0
		self._vlantxbytesrate = 0
		self._vlantotdroppedpkts = 0
		self._vlantotbroadcastpkts = 0

	@property
	def id(self) :
		ur"""An integer specifying the VLAN identification number (VID). Possible values: 1 through 4094.<br/>Minimum value =  1<br/>Maximum value =  4094.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""An integer specifying the VLAN identification number (VID). Possible values: 1 through 4094.
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		ur"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		ur"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def vlanrxbytesrate(self) :
		ur"""Rate (/s) counter for vlantotrxbytes.
		"""
		try :
			return self._vlanrxbytesrate
		except Exception as e:
			raise e

	@property
	def vlantottxpkts(self) :
		ur"""Packets transmitted on the VLAN.
		"""
		try :
			return self._vlantottxpkts
		except Exception as e:
			raise e

	@property
	def vlantotdroppedpkts(self) :
		ur"""Inbound packets dropped by the VLAN upon reception.
		"""
		try :
			return self._vlantotdroppedpkts
		except Exception as e:
			raise e

	@property
	def vlanrxpktsrate(self) :
		ur"""Rate (/s) counter for vlantotrxpkts.
		"""
		try :
			return self._vlanrxpktsrate
		except Exception as e:
			raise e

	@property
	def vlantotrxpkts(self) :
		ur"""Packets received on the VLAN.
		"""
		try :
			return self._vlantotrxpkts
		except Exception as e:
			raise e

	@property
	def vlantxpktsrate(self) :
		ur"""Rate (/s) counter for vlantottxpkts.
		"""
		try :
			return self._vlantxpktsrate
		except Exception as e:
			raise e

	@property
	def vlantotbroadcastpkts(self) :
		ur"""Broadcast packets sent and received on the VLAN.
		"""
		try :
			return self._vlantotbroadcastpkts
		except Exception as e:
			raise e

	@property
	def vlantxbytesrate(self) :
		ur"""Rate (/s) counter for vlantottxbytes.
		"""
		try :
			return self._vlantxbytesrate
		except Exception as e:
			raise e

	@property
	def vlantotrxbytes(self) :
		ur"""Bytes of data received on the VLAN.
		"""
		try :
			return self._vlantotrxbytes
		except Exception as e:
			raise e

	@property
	def vlantottxbytes(self) :
		ur"""Bytes of data transmitted on the VLAN.
		"""
		try :
			return self._vlantottxbytes
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vlan_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vlan
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all vlan_stats resources that are configured on netscaler.
		"""
		try :
			obj = vlan_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.id = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class vlan_response(base_response) :
	def __init__(self, length=1) :
		self.vlan = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vlan = [vlan_stats() for _ in range(length)]

