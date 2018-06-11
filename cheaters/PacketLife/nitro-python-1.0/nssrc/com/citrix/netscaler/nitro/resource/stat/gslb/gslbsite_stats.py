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

class gslbsite_stats(base_resource) :
	ur""" Statistics for GSLB site resource.
	"""
	def __init__(self) :
		self._sitename = ""
		self._clearstats = ""
		self._sitepublicip = ""
		self._siteip = ""
		self._sitemepstatus = ""
		self._persexchange = ""
		self._nwmetricexchange = ""
		self._sitemetricexchange = ""
		self._sitetype = ""
		self._siteipstr = ""
		self._sitepublicipstr = ""
		self._sitemetricmepstatus = ""
		self._nwmetricmepstatus = ""
		self._sitetotalrequestbytes = 0
		self._siterequestbytesrate = 0
		self._sitetotalresponsebytes = 0
		self._siteresponsebytesrate = 0
		self._sitetotalrequests = 0
		self._siterequestsrate = 0
		self._sitetotalresponses = 0
		self._siteresponsesrate = 0
		self._sitecurclntconnections = 0
		self._sitecursrvrconnections = 0

	@property
	def sitename(self) :
		ur"""Name of the GSLB site for which to display detailed statistics. If a name is not specified, basic information about all GSLB sites is displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@sitename.setter
	def sitename(self, sitename) :
		ur"""Name of the GSLB site for which to display detailed statistics. If a name is not specified, basic information about all GSLB sites is displayed.
		"""
		try :
			self._sitename = sitename
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
	def siteresponsesrate(self) :
		ur"""Rate (/s) counter for sitetotalresponses.
		"""
		try :
			return self._siteresponsesrate
		except Exception as e:
			raise e

	@property
	def siteipstr(self) :
		ur"""The private IP address of this GSLB site.
		"""
		try :
			return self._siteipstr
		except Exception as e:
			raise e

	@property
	def sitetotalrequests(self) :
		ur"""Total number of requests received by the virtual servers represented by all GSLB services associated with this GSLB site.
		"""
		try :
			return self._sitetotalrequests
		except Exception as e:
			raise e

	@property
	def siterequestsrate(self) :
		ur"""Rate (/s) counter for sitetotalrequests.
		"""
		try :
			return self._siterequestsrate
		except Exception as e:
			raise e

	@property
	def nwmetricmepstatus(self) :
		ur"""Indicates the status of the network metric Metric Exchange connection at this GSLB site. .
		"""
		try :
			return self._nwmetricmepstatus
		except Exception as e:
			raise e

	@property
	def sitemetricexchange(self) :
		ur"""Indicates whether metric exchange is enabled or disabled at this GSLB site.
		"""
		try :
			return self._sitemetricexchange
		except Exception as e:
			raise e

	@property
	def sitepublicip(self) :
		ur"""The public IP address of this GSLB site.
		"""
		try :
			return self._sitepublicip
		except Exception as e:
			raise e

	@property
	def sitetotalresponsebytes(self) :
		ur"""Number of response bytes received by the virtual servers represented by all GSLB services associated with this GSLB site.
		"""
		try :
			return self._sitetotalresponsebytes
		except Exception as e:
			raise e

	@property
	def sitecursrvrconnections(self) :
		ur"""Number of current connections to the real servers behind the virtual servers represented by all GSLB services associated with this GSLB site.
		"""
		try :
			return self._sitecursrvrconnections
		except Exception as e:
			raise e

	@property
	def sitepublicipstr(self) :
		ur"""The public IP address of this GSLB site.
		"""
		try :
			return self._sitepublicipstr
		except Exception as e:
			raise e

	@property
	def sitetotalrequestbytes(self) :
		ur"""Total number of request bytes received by the virtual servers represented by all GSLB services associated with this GSLB site.
		"""
		try :
			return self._sitetotalrequestbytes
		except Exception as e:
			raise e

	@property
	def siteip(self) :
		ur"""The private IP address of this GSLB site.
		"""
		try :
			return self._siteip
		except Exception as e:
			raise e

	@property
	def sitemepstatus(self) :
		ur"""Indicates the status of the Metric Exchange Policy at this GSLB site. .
		"""
		try :
			return self._sitemepstatus
		except Exception as e:
			raise e

	@property
	def sitecurclntconnections(self) :
		ur"""Number of current client connections to the virtual servers represented by all GSLB services associated with this GSLB site.
		"""
		try :
			return self._sitecurclntconnections
		except Exception as e:
			raise e

	@property
	def sitetype(self) :
		ur"""Indicates whether this GSLB site is local or remote.
		"""
		try :
			return self._sitetype
		except Exception as e:
			raise e

	@property
	def nwmetricexchange(self) :
		ur"""Indicates whether network metric exchange is enabled or disabled at this GSLB site.
		"""
		try :
			return self._nwmetricexchange
		except Exception as e:
			raise e

	@property
	def persexchange(self) :
		ur"""Indicates whether Persistence entries exchange is enabled or disabled at this GSLB site.
		"""
		try :
			return self._persexchange
		except Exception as e:
			raise e

	@property
	def siterequestbytesrate(self) :
		ur"""Rate (/s) counter for sitetotalrequestbytes.
		"""
		try :
			return self._siterequestbytesrate
		except Exception as e:
			raise e

	@property
	def siteresponsebytesrate(self) :
		ur"""Rate (/s) counter for sitetotalresponsebytes.
		"""
		try :
			return self._siteresponsebytesrate
		except Exception as e:
			raise e

	@property
	def sitetotalresponses(self) :
		ur"""Number of responses received by the virtual servers represented by all GSLB services associated with this GSLB site.
		"""
		try :
			return self._sitetotalresponses
		except Exception as e:
			raise e

	@property
	def sitemetricmepstatus(self) :
		ur"""Indicates the status of the site metric Metric Exchange connection at this GSLB site. .
		"""
		try :
			return self._sitemetricmepstatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbsite_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbsite
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.sitename is not None :
				return str(self.sitename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all gslbsite_stats resources that are configured on netscaler.
		"""
		try :
			obj = gslbsite_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.sitename = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class gslbsite_response(base_response) :
	def __init__(self, length=1) :
		self.gslbsite = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbsite = [gslbsite_stats() for _ in range(length)]

