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

class inatsession_stats(base_resource) :
	ur""" Statistics for stateful INAT resource.
	"""
	def __init__(self) :
		self._name = ""
		self._clearstats = ""
		self._inattothits = 0
		self._inathitsrate = 0
		self._inatcursessions = 0
		self._inatcursessionsrate = 0
		self._inattotreceivebytes = 0
		self._inatreceivebytesrate = 0
		self._inattotsentbytes = 0
		self._inatsentbytesrate = 0
		self._inattotpktreceived = 0
		self._inatpktreceivedrate = 0
		self._inattotpktsent = 0
		self._inatpktsentrate = 0

	@property
	def name(self) :
		ur"""INAT name.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""INAT name
		"""
		try :
			self._name = name
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
	def inattotsentbytes(self) :
		ur"""INAT total Sent Bytes.
		"""
		try :
			return self._inattotsentbytes
		except Exception as e:
			raise e

	@property
	def inatreceivebytesrate(self) :
		ur"""Rate (/s) counter for inattotreceivebytes.
		"""
		try :
			return self._inatreceivebytesrate
		except Exception as e:
			raise e

	@property
	def inathitsrate(self) :
		ur"""Rate (/s) counter for inattothits.
		"""
		try :
			return self._inathitsrate
		except Exception as e:
			raise e

	@property
	def inattotreceivebytes(self) :
		ur"""INAT total Received Bytes.
		"""
		try :
			return self._inattotreceivebytes
		except Exception as e:
			raise e

	@property
	def inatcursessionsrate(self) :
		ur"""Rate (/s) counter for inatcursessions.
		"""
		try :
			return self._inatcursessionsrate
		except Exception as e:
			raise e

	@property
	def inatcursessions(self) :
		ur"""INAT current sessions.
		"""
		try :
			return self._inatcursessions
		except Exception as e:
			raise e

	@property
	def inatsentbytesrate(self) :
		ur"""Rate (/s) counter for inattotsentbytes.
		"""
		try :
			return self._inatsentbytesrate
		except Exception as e:
			raise e

	@property
	def inatpktsentrate(self) :
		ur"""Rate (/s) counter for inattotpktsent.
		"""
		try :
			return self._inatpktsentrate
		except Exception as e:
			raise e

	@property
	def inattotpktreceived(self) :
		ur"""INAT total Packets Received.
		"""
		try :
			return self._inattotpktreceived
		except Exception as e:
			raise e

	@property
	def inattothits(self) :
		ur"""INAT total sessions.
		"""
		try :
			return self._inattothits
		except Exception as e:
			raise e

	@property
	def inattotpktsent(self) :
		ur"""INAT total Packets Sent.
		"""
		try :
			return self._inattotpktsent
		except Exception as e:
			raise e

	@property
	def inatpktreceivedrate(self) :
		ur"""Rate (/s) counter for inattotpktreceived.
		"""
		try :
			return self._inatpktreceivedrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(inatsession_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.inatsession
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all inatsession_stats resources that are configured on netscaler.
		"""
		try :
			obj = inatsession_stats()
			if name :
				obj.name = name
				response = obj.stat_resource(service, option_)
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(name)
			response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class inatsession_response(base_response) :
	def __init__(self, length=1) :
		self.inatsession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.inatsession = [inatsession_stats() for _ in range(length)]

