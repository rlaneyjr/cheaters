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

class appflow_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._appflowtotaltxoctets = 0
		self._appflowtxoctetsrate = 0
		self._appflowtotalflows = 0
		self._appflowflowsrate = 0
		self._appflowtotaltxmessagess = 0
		self._appflowtxmessagessrate = 0
		self._appflowtotalignoctets = 0
		self._appflowignoctetsrate = 0
		self._appflowtotalignpacketss = 0
		self._appflowignpacketssrate = 0
		self._appflowtotalnotxoctets = 0
		self._appflownotxoctetsrate = 0
		self._appflowtotalnotxflows = 0
		self._appflownotxflowsrate = 0
		self._appflowtotalnotxpackets = 0
		self._appflownotxpacketsrate = 0

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
	def appflowtxoctetsrate(self) :
		ur"""Rate (/s) counter for appflowtotaltxoctets.
		"""
		try :
			return self._appflowtxoctetsrate
		except Exception as e:
			raise e

	@property
	def appflowtxmessagessrate(self) :
		ur"""Rate (/s) counter for appflowtotaltxmessagess.
		"""
		try :
			return self._appflowtxmessagessrate
		except Exception as e:
			raise e

	@property
	def appflowtotalnotxoctets(self) :
		ur"""The total number of AppFlow (IPFIX) octets that the NetScaler has not transmitted.
		"""
		try :
			return self._appflowtotalnotxoctets
		except Exception as e:
			raise e

	@property
	def appflowtotaltxmessagess(self) :
		ur"""The total number of AppFlow (IPFIX) messages that the NetScaler has transmitted.
		"""
		try :
			return self._appflowtotaltxmessagess
		except Exception as e:
			raise e

	@property
	def appflowtotalignpacketss(self) :
		ur"""The total number of packets that the NetScaler has ignored for AppFlow (IPFIX).
		"""
		try :
			return self._appflowtotalignpacketss
		except Exception as e:
			raise e

	@property
	def appflowtotalflows(self) :
		ur"""The total number of AppFlow (IPFIX) flows that the NetScaler has transmitted.
		"""
		try :
			return self._appflowtotalflows
		except Exception as e:
			raise e

	@property
	def appflowtotalnotxflows(self) :
		ur"""The total number of AppFlow (IPFIX) flows that the NetScaler has not transmitted.
		"""
		try :
			return self._appflowtotalnotxflows
		except Exception as e:
			raise e

	@property
	def appflownotxflowsrate(self) :
		ur"""Rate (/s) counter for appflowtotalnotxflows.
		"""
		try :
			return self._appflownotxflowsrate
		except Exception as e:
			raise e

	@property
	def appflowignoctetsrate(self) :
		ur"""Rate (/s) counter for appflowtotalignoctets.
		"""
		try :
			return self._appflowignoctetsrate
		except Exception as e:
			raise e

	@property
	def appflowtotalignoctets(self) :
		ur"""The total number of octets that the NetScaler has ignored for AppFlow (IPFIX).
		"""
		try :
			return self._appflowtotalignoctets
		except Exception as e:
			raise e

	@property
	def appflowtotaltxoctets(self) :
		ur"""The total number of AppFlow (IPFIX) octets that the NetScaler has transmitted.
		"""
		try :
			return self._appflowtotaltxoctets
		except Exception as e:
			raise e

	@property
	def appflowtotalnotxpackets(self) :
		ur"""The total number of AppFlow (IPFIX) packets that the NetScaler has not transmitted.
		"""
		try :
			return self._appflowtotalnotxpackets
		except Exception as e:
			raise e

	@property
	def appflownotxpacketsrate(self) :
		ur"""Rate (/s) counter for appflowtotalnotxpackets.
		"""
		try :
			return self._appflownotxpacketsrate
		except Exception as e:
			raise e

	@property
	def appflowflowsrate(self) :
		ur"""Rate (/s) counter for appflowtotalflows.
		"""
		try :
			return self._appflowflowsrate
		except Exception as e:
			raise e

	@property
	def appflownotxoctetsrate(self) :
		ur"""Rate (/s) counter for appflowtotalnotxoctets.
		"""
		try :
			return self._appflownotxoctetsrate
		except Exception as e:
			raise e

	@property
	def appflowignpacketssrate(self) :
		ur"""Rate (/s) counter for appflowtotalignpacketss.
		"""
		try :
			return self._appflowignpacketssrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appflow_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appflow
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all appflow_stats resources that are configured on netscaler.
		"""
		try :
			obj = appflow_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class appflow_response(base_response) :
	def __init__(self, length=1) :
		self.appflow = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appflow = [appflow_stats() for _ in range(length)]

