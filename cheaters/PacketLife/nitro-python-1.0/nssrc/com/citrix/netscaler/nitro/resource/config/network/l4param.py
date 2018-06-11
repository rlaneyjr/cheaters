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

class l4param(base_resource) :
	""" Configuration for Layer 4 related parameter resource. """
	def __init__(self) :
		self._l2connmethod = ""
		self._l4switch = ""

	@property
	def l2connmethod(self) :
		ur"""Layer 2 connection method based on the combination of  channel number, MAC address and VLAN. It is tuned with l2conn param of lb vserver. If l2conn of lb vserver is ON then method specified here will be used to identify a connection in addition to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>).<br/>Default value: MacVlanChannel<br/>Possible values = Channel, Vlan, VlanChannel, Mac, MacChannel, MacVlan, MacVlanChannel.
		"""
		try :
			return self._l2connmethod
		except Exception as e:
			raise e

	@l2connmethod.setter
	def l2connmethod(self, l2connmethod) :
		ur"""Layer 2 connection method based on the combination of  channel number, MAC address and VLAN. It is tuned with l2conn param of lb vserver. If l2conn of lb vserver is ON then method specified here will be used to identify a connection in addition to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>).<br/>Default value: MacVlanChannel<br/>Possible values = Channel, Vlan, VlanChannel, Mac, MacChannel, MacVlan, MacVlanChannel
		"""
		try :
			self._l2connmethod = l2connmethod
		except Exception as e:
			raise e

	@property
	def l4switch(self) :
		ur"""In L4 switch topology, always clients and servers are on the same side. Enable l4switch to allow such connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._l4switch
		except Exception as e:
			raise e

	@l4switch.setter
	def l4switch(self, l4switch) :
		ur"""In L4 switch topology, always clients and servers are on the same side. Enable l4switch to allow such connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._l4switch = l4switch
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(l4param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.l4param
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
		ur""" Use this API to update l4param.
		"""
		try :
			if type(resource) is not list :
				updateresource = l4param()
				updateresource.l2connmethod = resource.l2connmethod
				updateresource.l4switch = resource.l4switch
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of l4param resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = l4param()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the l4param resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = l4param()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class L4switch:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class L2connmethod:
		Channel = "Channel"
		Vlan = "Vlan"
		VlanChannel = "VlanChannel"
		Mac = "Mac"
		MacChannel = "MacChannel"
		MacVlan = "MacVlan"
		MacVlanChannel = "MacVlanChannel"

class l4param_response(base_response) :
	def __init__(self, length=1) :
		self.l4param = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.l4param = [l4param() for _ in range(length)]

