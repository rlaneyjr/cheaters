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

class lldp_stats(base_resource) :
	def __init__(self) :
		self._ifnum = ""
		self._clearstats = ""
		self._rxportframestotal = 0
		self._rxportframesrate = 0
		self._rxportbytestotal = 0
		self._rxportbytesrate = 0
		self._txportframestotal = 0
		self._txportframesrate = 0
		self._txportbytestotal = 0
		self._txportbytesrate = 0
		self._rxportframeserrors = 0
		self._rxportframeserrorsrate = 0
		self._rxporttlvsdiscardedtotal = 0
		self._rxporttlvsdiscardedrate = 0
		self._rxporttlvsunrecognizedtotal = 0
		self._rxporttlvsunrecognizedrate = 0

	@property
	def ifnum(self) :
		ur"""LLDP Statistics per interfaces.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		ur"""LLDP Statistics per interfaces
		"""
		try :
			self._ifnum = ifnum
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
	def rxporttlvsdiscardedtotal(self) :
		ur"""Total discarded LLDP packets.
		"""
		try :
			return self._rxporttlvsdiscardedtotal
		except Exception as e:
			raise e

	@property
	def rxportframeserrors(self) :
		ur"""Total errors in LLDP packets.
		"""
		try :
			return self._rxportframeserrors
		except Exception as e:
			raise e

	@property
	def rxportframeserrorsrate(self) :
		ur"""Rate (/s) counter for rxportframeserrors.
		"""
		try :
			return self._rxportframeserrorsrate
		except Exception as e:
			raise e

	@property
	def rxportframestotal(self) :
		ur"""Total LLDP Packets received.
		"""
		try :
			return self._rxportframestotal
		except Exception as e:
			raise e

	@property
	def txportbytestotal(self) :
		ur"""Total LLDP bytes transmitted.
		"""
		try :
			return self._txportbytestotal
		except Exception as e:
			raise e

	@property
	def txportframestotal(self) :
		ur"""Total LLDP Packets transmitted.
		"""
		try :
			return self._txportframestotal
		except Exception as e:
			raise e

	@property
	def rxporttlvsunrecognizedtotal(self) :
		ur"""Total TLVs not Recognised.
		"""
		try :
			return self._rxporttlvsunrecognizedtotal
		except Exception as e:
			raise e

	@property
	def rxportbytesrate(self) :
		ur"""Rate (/s) counter for rxportbytestotal.
		"""
		try :
			return self._rxportbytesrate
		except Exception as e:
			raise e

	@property
	def rxportbytestotal(self) :
		ur"""Total LLDP bytes received.
		"""
		try :
			return self._rxportbytestotal
		except Exception as e:
			raise e

	@property
	def rxporttlvsdiscardedrate(self) :
		ur"""Rate (/s) counter for rxporttlvsdiscardedtotal.
		"""
		try :
			return self._rxporttlvsdiscardedrate
		except Exception as e:
			raise e

	@property
	def txportbytesrate(self) :
		ur"""Rate (/s) counter for txportbytestotal.
		"""
		try :
			return self._txportbytesrate
		except Exception as e:
			raise e

	@property
	def rxporttlvsunrecognizedrate(self) :
		ur"""Rate (/s) counter for rxporttlvsunrecognizedtotal.
		"""
		try :
			return self._rxporttlvsunrecognizedrate
		except Exception as e:
			raise e

	@property
	def rxportframesrate(self) :
		ur"""Rate (/s) counter for rxportframestotal.
		"""
		try :
			return self._rxportframesrate
		except Exception as e:
			raise e

	@property
	def txportframesrate(self) :
		ur"""Rate (/s) counter for txportframestotal.
		"""
		try :
			return self._txportframesrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lldp_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lldp
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ifnum is not None :
				return str(self.ifnum)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all lldp_stats resources that are configured on netscaler.
		"""
		try :
			obj = lldp_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.ifnum = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class lldp_response(base_response) :
	def __init__(self, length=1) :
		self.lldp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lldp = [lldp_stats() for _ in range(length)]

