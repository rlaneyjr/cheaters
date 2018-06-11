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

class nsfeature(base_resource) :
	""" Configuration for feature resource. """
	def __init__(self) :
		self._feature = []
		self._wl = False
		self._sp = False
		self._lb = False
		self._cs = False
		self._cr = False
		self._sc = False
		self._cmp = False
		self._pq = False
		self._ssl = False
		self._gslb = False
		self._hdosp = False
		self._cf = False
		self._ic = False
		self._sslvpn = False
		self._aaa = False
		self._ospf = False
		self._rip = False
		self._bgp = False
		self._rewrite = False
		self._ipv6pt = False
		self._appfw = False
		self._responder = False
		self._htmlinjection = False
		self._push = False
		self._appflow = False
		self._cloudbridge = False
		self._isis = False
		self._ch = False
		self._appqoe = False
		self._vpath = False
		self._contentaccelerator = False
		self._rise = False
		self._feo = False

	@property
	def feature(self) :
		ur"""Feature to be enabled. Multiple features can be specified by providing a blank space between each feature.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	@feature.setter
	def feature(self, feature) :
		ur"""Feature to be enabled. Multiple features can be specified by providing a blank space between each feature.
		"""
		try :
			self._feature = feature
		except Exception as e:
			raise e

	@property
	def wl(self) :
		ur"""Web Logging.
		"""
		try :
			return self._wl
		except Exception as e:
			raise e

	@property
	def sp(self) :
		ur"""Surge Protection.
		"""
		try :
			return self._sp
		except Exception as e:
			raise e

	@property
	def lb(self) :
		ur"""Load Balancing.
		"""
		try :
			return self._lb
		except Exception as e:
			raise e

	@property
	def cs(self) :
		ur"""Content Switching.
		"""
		try :
			return self._cs
		except Exception as e:
			raise e

	@property
	def cr(self) :
		ur"""Cache Redirect.
		"""
		try :
			return self._cr
		except Exception as e:
			raise e

	@property
	def sc(self) :
		ur"""Sure Connect.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@property
	def cmp(self) :
		ur"""Compression.
		"""
		try :
			return self._cmp
		except Exception as e:
			raise e

	@property
	def pq(self) :
		ur"""Priority Queuing.
		"""
		try :
			return self._pq
		except Exception as e:
			raise e

	@property
	def ssl(self) :
		ur"""Secure Sockets Layer.
		"""
		try :
			return self._ssl
		except Exception as e:
			raise e

	@property
	def gslb(self) :
		ur"""Global Server Load Balancing.
		"""
		try :
			return self._gslb
		except Exception as e:
			raise e

	@property
	def hdosp(self) :
		ur"""DOS Protection.
		"""
		try :
			return self._hdosp
		except Exception as e:
			raise e

	@property
	def cf(self) :
		ur"""Content Filter.
		"""
		try :
			return self._cf
		except Exception as e:
			raise e

	@property
	def ic(self) :
		ur"""Integrated Caching.
		"""
		try :
			return self._ic
		except Exception as e:
			raise e

	@property
	def sslvpn(self) :
		ur"""SSL VPN.
		"""
		try :
			return self._sslvpn
		except Exception as e:
			raise e

	@property
	def aaa(self) :
		ur"""AAA.
		"""
		try :
			return self._aaa
		except Exception as e:
			raise e

	@property
	def ospf(self) :
		ur"""OSPF Routing.
		"""
		try :
			return self._ospf
		except Exception as e:
			raise e

	@property
	def rip(self) :
		ur"""RIP Routing.
		"""
		try :
			return self._rip
		except Exception as e:
			raise e

	@property
	def bgp(self) :
		ur"""BGP Routing.
		"""
		try :
			return self._bgp
		except Exception as e:
			raise e

	@property
	def rewrite(self) :
		ur"""Rewrite.
		"""
		try :
			return self._rewrite
		except Exception as e:
			raise e

	@property
	def ipv6pt(self) :
		ur"""IPv6 protocol translation.
		"""
		try :
			return self._ipv6pt
		except Exception as e:
			raise e

	@property
	def appfw(self) :
		ur"""Application Firewall.
		"""
		try :
			return self._appfw
		except Exception as e:
			raise e

	@property
	def responder(self) :
		ur"""Responder.
		"""
		try :
			return self._responder
		except Exception as e:
			raise e

	@property
	def htmlinjection(self) :
		ur"""HTML Injection.
		"""
		try :
			return self._htmlinjection
		except Exception as e:
			raise e

	@property
	def push(self) :
		ur"""NetScaler Push.
		"""
		try :
			return self._push
		except Exception as e:
			raise e

	@property
	def appflow(self) :
		ur"""AppFlow.
		"""
		try :
			return self._appflow
		except Exception as e:
			raise e

	@property
	def cloudbridge(self) :
		ur"""CloudBridge.
		"""
		try :
			return self._cloudbridge
		except Exception as e:
			raise e

	@property
	def isis(self) :
		ur"""ISIS Routing.
		"""
		try :
			return self._isis
		except Exception as e:
			raise e

	@property
	def ch(self) :
		ur"""Call Home.
		"""
		try :
			return self._ch
		except Exception as e:
			raise e

	@property
	def appqoe(self) :
		ur"""AppQoS.
		"""
		try :
			return self._appqoe
		except Exception as e:
			raise e

	@property
	def vpath(self) :
		ur"""Vpath.
		"""
		try :
			return self._vpath
		except Exception as e:
			raise e

	@property
	def contentaccelerator(self) :
		ur"""Transparent Integrated Caching.
		"""
		try :
			return self._contentaccelerator
		except Exception as e:
			raise e

	@property
	def rise(self) :
		ur"""RISE.
		"""
		try :
			return self._rise
		except Exception as e:
			raise e

	@property
	def feo(self) :
		ur"""Optimize Web content (HTML, CSS, JavaScript, images).
		"""
		try :
			return self._feo
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsfeature_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsfeature
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
	def enable(cls, client, resource) :
		ur""" Use this API to enable nsfeature.
		"""
		try :
			if type(resource) is not list :
				enableresource = nsfeature()
				enableresource.feature = resource.feature
				return enableresource.perform_operation(client,"enable")
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable nsfeature.
		"""
		try :
			if type(resource) is not list :
				disableresource = nsfeature()
				disableresource.feature = resource.feature
				return disableresource.perform_operation(client,"disable")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsfeature resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsfeature()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		vPath = "vPath"
		ContentAccelerator = "ContentAccelerator"
		RISE = "RISE"
		FEO = "FEO"

class nsfeature_response(base_response) :
	def __init__(self, length=1) :
		self.nsfeature = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsfeature = [nsfeature() for _ in range(length)]

