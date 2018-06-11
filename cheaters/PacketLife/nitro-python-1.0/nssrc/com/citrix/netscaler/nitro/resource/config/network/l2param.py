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

class l2param(base_resource) :
	""" Configuration for Layer 2 related parameter resource. """
	def __init__(self) :
		self._mbfpeermacupdate = 0
		self._maxbridgecollision = 0
		self._bdggrpproxyarp = ""
		self._bdgsetting = ""
		self._garponvridintf = ""
		self._macmodefwdmypkt = ""
		self._usemymac = ""
		self._proxyarp = ""
		self._garpreply = ""
		self._mbfinstlearning = ""
		self._rstintfonhafo = ""
		self._skipproxyingbsdtraffic = ""
		self._returntoethernetsender = ""

	@property
	def mbfpeermacupdate(self) :
		ur"""When mbf_instant_learning is enabled, learn any changes in peer's MAC after this time interval, which is in 10ms ticks.<br/>Default value: 10.
		"""
		try :
			return self._mbfpeermacupdate
		except Exception as e:
			raise e

	@mbfpeermacupdate.setter
	def mbfpeermacupdate(self, mbfpeermacupdate) :
		ur"""When mbf_instant_learning is enabled, learn any changes in peer's MAC after this time interval, which is in 10ms ticks.<br/>Default value: 10
		"""
		try :
			self._mbfpeermacupdate = mbfpeermacupdate
		except Exception as e:
			raise e

	@property
	def maxbridgecollision(self) :
		ur"""Maximum bridge collision for loop detection .<br/>Default value: 20.
		"""
		try :
			return self._maxbridgecollision
		except Exception as e:
			raise e

	@maxbridgecollision.setter
	def maxbridgecollision(self, maxbridgecollision) :
		ur"""Maximum bridge collision for loop detection .<br/>Default value: 20
		"""
		try :
			self._maxbridgecollision = maxbridgecollision
		except Exception as e:
			raise e

	@property
	def bdggrpproxyarp(self) :
		ur"""Set/reset proxy ARP in bridge group deployment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._bdggrpproxyarp
		except Exception as e:
			raise e

	@bdggrpproxyarp.setter
	def bdggrpproxyarp(self, bdggrpproxyarp) :
		ur"""Set/reset proxy ARP in bridge group deployment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._bdggrpproxyarp = bdggrpproxyarp
		except Exception as e:
			raise e

	@property
	def bdgsetting(self) :
		ur"""Bridging settings for C2C behavior.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._bdgsetting
		except Exception as e:
			raise e

	@bdgsetting.setter
	def bdgsetting(self, bdgsetting) :
		ur"""Bridging settings for C2C behavior.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._bdgsetting = bdgsetting
		except Exception as e:
			raise e

	@property
	def garponvridintf(self) :
		ur"""Send GARP messagess on VRID-configured interfaces upon failover .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._garponvridintf
		except Exception as e:
			raise e

	@garponvridintf.setter
	def garponvridintf(self, garponvridintf) :
		ur"""Send GARP messagess on VRID-configured interfaces upon failover .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._garponvridintf = garponvridintf
		except Exception as e:
			raise e

	@property
	def macmodefwdmypkt(self) :
		ur""" MAC mode vserver forward packets destined to VIPs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._macmodefwdmypkt
		except Exception as e:
			raise e

	@macmodefwdmypkt.setter
	def macmodefwdmypkt(self, macmodefwdmypkt) :
		ur""" MAC mode vserver forward packets destined to VIPs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._macmodefwdmypkt = macmodefwdmypkt
		except Exception as e:
			raise e

	@property
	def usemymac(self) :
		ur"""Set/reset cfg_use_my_mac .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._usemymac
		except Exception as e:
			raise e

	@usemymac.setter
	def usemymac(self, usemymac) :
		ur"""Set/reset cfg_use_my_mac .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._usemymac = usemymac
		except Exception as e:
			raise e

	@property
	def proxyarp(self) :
		ur"""Set/reset cfg_proxy_arp_dr .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._proxyarp
		except Exception as e:
			raise e

	@proxyarp.setter
	def proxyarp(self, proxyarp) :
		ur"""Set/reset cfg_proxy_arp_dr .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._proxyarp = proxyarp
		except Exception as e:
			raise e

	@property
	def garpreply(self) :
		ur"""Set/reset REPLY form of GARP .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._garpreply
		except Exception as e:
			raise e

	@garpreply.setter
	def garpreply(self, garpreply) :
		ur"""Set/reset REPLY form of GARP .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._garpreply = garpreply
		except Exception as e:
			raise e

	@property
	def mbfinstlearning(self) :
		ur"""Enable instant learning of MAC changes in MBF mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mbfinstlearning
		except Exception as e:
			raise e

	@mbfinstlearning.setter
	def mbfinstlearning(self, mbfinstlearning) :
		ur"""Enable instant learning of MAC changes in MBF mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mbfinstlearning = mbfinstlearning
		except Exception as e:
			raise e

	@property
	def rstintfonhafo(self) :
		ur"""Enable the reset interface upon HA failover.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rstintfonhafo
		except Exception as e:
			raise e

	@rstintfonhafo.setter
	def rstintfonhafo(self, rstintfonhafo) :
		ur"""Enable the reset interface upon HA failover.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rstintfonhafo = rstintfonhafo
		except Exception as e:
			raise e

	@property
	def skipproxyingbsdtraffic(self) :
		ur"""Enable the proxying of FreeBSD traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skipproxyingbsdtraffic
		except Exception as e:
			raise e

	@skipproxyingbsdtraffic.setter
	def skipproxyingbsdtraffic(self, skipproxyingbsdtraffic) :
		ur"""Enable the proxying of FreeBSD traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skipproxyingbsdtraffic = skipproxyingbsdtraffic
		except Exception as e:
			raise e

	@property
	def returntoethernetsender(self) :
		ur""" Return to ethernet sender.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._returntoethernetsender
		except Exception as e:
			raise e

	@returntoethernetsender.setter
	def returntoethernetsender(self, returntoethernetsender) :
		ur""" Return to ethernet sender.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._returntoethernetsender = returntoethernetsender
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(l2param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.l2param
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
		ur""" Use this API to update l2param.
		"""
		try :
			if type(resource) is not list :
				updateresource = l2param()
				updateresource.mbfpeermacupdate = resource.mbfpeermacupdate
				updateresource.maxbridgecollision = resource.maxbridgecollision
				updateresource.bdggrpproxyarp = resource.bdggrpproxyarp
				updateresource.bdgsetting = resource.bdgsetting
				updateresource.garponvridintf = resource.garponvridintf
				updateresource.macmodefwdmypkt = resource.macmodefwdmypkt
				updateresource.usemymac = resource.usemymac
				updateresource.proxyarp = resource.proxyarp
				updateresource.garpreply = resource.garpreply
				updateresource.mbfinstlearning = resource.mbfinstlearning
				updateresource.rstintfonhafo = resource.rstintfonhafo
				updateresource.skipproxyingbsdtraffic = resource.skipproxyingbsdtraffic
				updateresource.returntoethernetsender = resource.returntoethernetsender
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of l2param resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = l2param()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the l2param resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = l2param()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Proxyarp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Usemymac:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Bdgsetting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Returntoethernetsender:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rstintfonhafo:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mbfinstlearning:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Macmodefwdmypkt:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Bdggrpproxyarp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Garponvridintf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Garpreply:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Skipproxyingbsdtraffic:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class l2param_response(base_response) :
	def __init__(self, length=1) :
		self.l2param = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.l2param = [l2param() for _ in range(length)]

