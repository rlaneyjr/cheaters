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

class systembw_stats(base_resource) :
	ur""" Statistics for bw resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._httpcltpoolinactive = 0
		self._httpcltpooloutactive = 0
		self._httpsvr200okresp = 0
		self._httpsvr200okresprate = 0
		self._httpsvr404notfound = 0
		self._httpsvr404notfoundrate = 0
		self._httpclterrstray = 0
		self._httpclterrstrayrate = 0
		self._httpcltttfplwm = 0
		self._httpcltttfplwmrate = 0
		self._httpcltttfp_0 = 0
		self._httpcltttfp_0rate = 0
		self._httpcltttfp_1 = 0
		self._httpcltttfp_1rate = 0
		self._httpcltttfp_2 = 0
		self._httpcltttfp_2rate = 0
		self._httpcltttfp_3 = 0
		self._httpcltttfp_3rate = 0
		self._httpcltttfp_4 = 0
		self._httpcltttfp_4rate = 0
		self._httpcltttfp_5 = 0
		self._httpcltttfp_5rate = 0
		self._httpcltttfp_6 = 0
		self._httpcltttfp_6rate = 0
		self._httpcltttfp_7 = 0
		self._httpcltttfp_7rate = 0
		self._httpcltttfphwm = 0
		self._httpcltttfphwmrate = 0
		self._httpcltttfpmax = 0
		self._httpcltttlplwm = 0
		self._httpcltttlplwmrate = 0
		self._httpcltttlp_0 = 0
		self._httpcltttlp_0rate = 0
		self._httpcltttlp_1 = 0
		self._httpcltttlp_1rate = 0
		self._httpcltttlp_2 = 0
		self._httpcltttlp_2rate = 0
		self._httpcltttlp_3 = 0
		self._httpcltttlp_3rate = 0
		self._httpcltttlp_4 = 0
		self._httpcltttlp_4rate = 0
		self._httpcltttlp_5 = 0
		self._httpcltttlp_5rate = 0
		self._httpcltttlp_6 = 0
		self._httpcltttlp_6rate = 0
		self._httpcltttlp_7 = 0
		self._httpcltttlp_7rate = 0
		self._httpcltttlphwm = 0
		self._httpcltttlphwmrate = 0
		self._httpcltttlpmax = 0

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
	def httpcltttfp_4rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_4.
		"""
		try :
			return self._httpcltttfp_4rate
		except Exception as e:
			raise e

	@property
	def httpcltttlp_5rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_5.
		"""
		try :
			return self._httpcltttlp_5rate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_2rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_2.
		"""
		try :
			return self._httpcltttfp_2rate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_7rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_7.
		"""
		try :
			return self._httpcltttfp_7rate
		except Exception as e:
			raise e

	@property
	def httpcltttlphwmrate(self) :
		ur"""Rate (/s) counter for httpcltttlphwm.
		"""
		try :
			return self._httpcltttlphwmrate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_0rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_0.
		"""
		try :
			return self._httpcltttfp_0rate
		except Exception as e:
			raise e

	@property
	def httpcltttlplwmrate(self) :
		ur"""Rate (/s) counter for httpcltttlplwm.
		"""
		try :
			return self._httpcltttlplwmrate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_4(self) :
		ur"""Number of Responses Falling on Band-4 for TTFP.
		"""
		try :
			return self._httpcltttfp_4
		except Exception as e:
			raise e

	@property
	def httpcltpooloutactive(self) :
		ur"""No of responses Received.
		"""
		try :
			return self._httpcltpooloutactive
		except Exception as e:
			raise e

	@property
	def httpcltttlplwm(self) :
		ur"""Number of Responses Falling on LWM for TTLP.
		"""
		try :
			return self._httpcltttlplwm
		except Exception as e:
			raise e

	@property
	def httpcltttlp_1(self) :
		ur"""Number of Responses Falling on Band-1 for TTLP.
		"""
		try :
			return self._httpcltttlp_1
		except Exception as e:
			raise e

	@property
	def httpsvr404notfoundrate(self) :
		ur"""Rate (/s) counter for httpsvr404notfound.
		"""
		try :
			return self._httpsvr404notfoundrate
		except Exception as e:
			raise e

	@property
	def httpcltttlp_6(self) :
		ur"""Number of Responses Falling on Band-6 for TTLP.
		"""
		try :
			return self._httpcltttlp_6
		except Exception as e:
			raise e

	@property
	def httpcltttlphwm(self) :
		ur"""Number of Responses Falling on HWM for TTLP.
		"""
		try :
			return self._httpcltttlphwm
		except Exception as e:
			raise e

	@property
	def httpcltttlp_1rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_1.
		"""
		try :
			return self._httpcltttlp_1rate
		except Exception as e:
			raise e

	@property
	def httpcltpoolinactive(self) :
		ur"""No of requests sent from BW client.
		"""
		try :
			return self._httpcltpoolinactive
		except Exception as e:
			raise e

	@property
	def httpcltttlp_3(self) :
		ur"""Number of Responses Falling on Band-3 for TTLP.
		"""
		try :
			return self._httpcltttlp_3
		except Exception as e:
			raise e

	@property
	def httpcltttlp_5(self) :
		ur"""Number of Responses Falling on Band-5 for TTLP.
		"""
		try :
			return self._httpcltttlp_5
		except Exception as e:
			raise e

	@property
	def httpcltttlp_6rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_6.
		"""
		try :
			return self._httpcltttlp_6rate
		except Exception as e:
			raise e

	@property
	def httpsvr200okresprate(self) :
		ur"""Rate (/s) counter for httpsvr200okresp.
		"""
		try :
			return self._httpsvr200okresprate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_1rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_1.
		"""
		try :
			return self._httpcltttfp_1rate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_1(self) :
		ur"""Number of Responses Falling on Band-1 for TTFP.
		"""
		try :
			return self._httpcltttfp_1
		except Exception as e:
			raise e

	@property
	def httpcltttfphwmrate(self) :
		ur"""Rate (/s) counter for httpcltttfphwm.
		"""
		try :
			return self._httpcltttfphwmrate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_6(self) :
		ur"""Number of Responses Falling on Band-6 for TTFP.
		"""
		try :
			return self._httpcltttfp_6
		except Exception as e:
			raise e

	@property
	def httpcltttfpmax(self) :
		ur"""Peak RTT observed for Time to First response packet.
		"""
		try :
			return self._httpcltttfpmax
		except Exception as e:
			raise e

	@property
	def httpcltttfp_5(self) :
		ur"""Number of Responses Falling on Band-5 for TTFP.
		"""
		try :
			return self._httpcltttfp_5
		except Exception as e:
			raise e

	@property
	def httpcltttlpmax(self) :
		ur"""Peak RTT observed for Time to Last response packet.
		"""
		try :
			return self._httpcltttlpmax
		except Exception as e:
			raise e

	@property
	def httpcltttlp_4rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_4.
		"""
		try :
			return self._httpcltttlp_4rate
		except Exception as e:
			raise e

	@property
	def httpcltttlp_7rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_7.
		"""
		try :
			return self._httpcltttlp_7rate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_0(self) :
		ur"""Number of Responses Falling on Band-0 for TTFP.
		"""
		try :
			return self._httpcltttfp_0
		except Exception as e:
			raise e

	@property
	def httpcltttfp_3(self) :
		ur"""Number of Responses Falling on Band-3 for TTFP.
		"""
		try :
			return self._httpcltttfp_3
		except Exception as e:
			raise e

	@property
	def httpcltttfphwm(self) :
		ur"""Number of Responses Falling on HWM for TTFP.
		"""
		try :
			return self._httpcltttfphwm
		except Exception as e:
			raise e

	@property
	def httpclterrstray(self) :
		ur"""Number of stray packets received from server without HTTP request.
		"""
		try :
			return self._httpclterrstray
		except Exception as e:
			raise e

	@property
	def httpcltttlp_0rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_0.
		"""
		try :
			return self._httpcltttlp_0rate
		except Exception as e:
			raise e

	@property
	def httpcltttfplwm(self) :
		ur"""Number of Responses Falling on LWM for TTFP.
		"""
		try :
			return self._httpcltttfplwm
		except Exception as e:
			raise e

	@property
	def httpcltttlp_0(self) :
		ur"""Number of Responses Falling on Band-0 for TTLP.
		"""
		try :
			return self._httpcltttlp_0
		except Exception as e:
			raise e

	@property
	def httpclterrstrayrate(self) :
		ur"""Rate (/s) counter for httpclterrstray.
		"""
		try :
			return self._httpclterrstrayrate
		except Exception as e:
			raise e

	@property
	def httpcltttfplwmrate(self) :
		ur"""Rate (/s) counter for httpcltttfplwm.
		"""
		try :
			return self._httpcltttfplwmrate
		except Exception as e:
			raise e

	@property
	def httpcltttlp_2(self) :
		ur"""Number of Responses Falling on Band-2 for TTLP.
		"""
		try :
			return self._httpcltttlp_2
		except Exception as e:
			raise e

	@property
	def httpcltttfp_2(self) :
		ur"""Number of Responses Falling on Band-2 for TTFP.
		"""
		try :
			return self._httpcltttfp_2
		except Exception as e:
			raise e

	@property
	def httpcltttlp_2rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_2.
		"""
		try :
			return self._httpcltttlp_2rate
		except Exception as e:
			raise e

	@property
	def httpcltttlp_4(self) :
		ur"""Number of Responses Falling on Band-4 for TTLP.
		"""
		try :
			return self._httpcltttlp_4
		except Exception as e:
			raise e

	@property
	def httpcltttfp_7(self) :
		ur"""Number of Responses Falling on Band-7 for TTFP.
		"""
		try :
			return self._httpcltttfp_7
		except Exception as e:
			raise e

	@property
	def httpsvr200okresp(self) :
		ur"""Number of 200 Ok response sent from the BW appliance.
		"""
		try :
			return self._httpsvr200okresp
		except Exception as e:
			raise e

	@property
	def httpsvr404notfound(self) :
		ur"""Number of 404 Not Found responses sent.
		"""
		try :
			return self._httpsvr404notfound
		except Exception as e:
			raise e

	@property
	def httpcltttlp_3rate(self) :
		ur"""Rate (/s) counter for httpcltttlp_3.
		"""
		try :
			return self._httpcltttlp_3rate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_6rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_6.
		"""
		try :
			return self._httpcltttfp_6rate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_5rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_5.
		"""
		try :
			return self._httpcltttfp_5rate
		except Exception as e:
			raise e

	@property
	def httpcltttfp_3rate(self) :
		ur"""Rate (/s) counter for httpcltttfp_3.
		"""
		try :
			return self._httpcltttfp_3rate
		except Exception as e:
			raise e

	@property
	def httpcltttlp_7(self) :
		ur"""Number of Responses Falling on Band-7 for TTLP.
		"""
		try :
			return self._httpcltttlp_7
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systembw_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systembw
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
		ur""" Use this API to fetch the statistics of all systembw_stats resources that are configured on netscaler.
		"""
		try :
			obj = systembw_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class systembw_response(base_response) :
	def __init__(self, length=1) :
		self.systembw = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systembw = [systembw_stats() for _ in range(length)]

