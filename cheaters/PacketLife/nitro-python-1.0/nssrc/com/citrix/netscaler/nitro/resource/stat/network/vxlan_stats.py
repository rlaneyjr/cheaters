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

class vxlan_stats(base_resource) :
	ur""" Statistics for "VXLAN" resource.
	"""
	def __init__(self) :
		self._id = 0
		self._clearstats = ""
		self._vxlantotrxpkts = 0
		self._vxlanrxpktsrate = 0
		self._vxlantotrxbytes = 0
		self._vxlanrxbytesrate = 0
		self._vxlantottxpkts = 0
		self._vxlantxpktsrate = 0
		self._vxlantottxbytes = 0
		self._vxlantxbytesrate = 0

	@property
	def id(self) :
		ur"""An integer specifying the VXLAN identification number (VNID).<br/>Minimum value =  1<br/>Maximum value =  16777215.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		ur"""An integer specifying the VXLAN identification number (VNID).
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
	def vxlanrxbytesrate(self) :
		ur"""Rate (/s) counter for vxlantotrxbytes.
		"""
		try :
			return self._vxlanrxbytesrate
		except Exception as e:
			raise e

	@property
	def vxlantottxpkts(self) :
		ur"""Packets transmitted on the VXLAN.
		"""
		try :
			return self._vxlantottxpkts
		except Exception as e:
			raise e

	@property
	def vxlanrxpktsrate(self) :
		ur"""Rate (/s) counter for vxlantotrxpkts.
		"""
		try :
			return self._vxlanrxpktsrate
		except Exception as e:
			raise e

	@property
	def vxlantotrxbytes(self) :
		ur"""Bytes of data received on the VXLAN.
		"""
		try :
			return self._vxlantotrxbytes
		except Exception as e:
			raise e

	@property
	def vxlantxbytesrate(self) :
		ur"""Rate (/s) counter for vxlantottxbytes.
		"""
		try :
			return self._vxlantxbytesrate
		except Exception as e:
			raise e

	@property
	def vxlantxpktsrate(self) :
		ur"""Rate (/s) counter for vxlantottxpkts.
		"""
		try :
			return self._vxlantxpktsrate
		except Exception as e:
			raise e

	@property
	def vxlantottxbytes(self) :
		ur"""Bytes of data transmitted on the VXLAN.
		"""
		try :
			return self._vxlantottxbytes
		except Exception as e:
			raise e

	@property
	def vxlantotrxpkts(self) :
		ur"""Packets received on the VXLAN.
		"""
		try :
			return self._vxlantotrxpkts
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vxlan_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vxlan
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
		ur""" Use this API to fetch the statistics of all vxlan_stats resources that are configured on netscaler.
		"""
		try :
			obj = vxlan_stats()
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

class vxlan_response(base_response) :
	def __init__(self, length=1) :
		self.vxlan = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vxlan = [vxlan_stats() for _ in range(length)]

