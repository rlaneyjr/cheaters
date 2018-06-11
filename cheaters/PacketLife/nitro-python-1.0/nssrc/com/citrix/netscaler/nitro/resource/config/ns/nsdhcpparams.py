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

class nsdhcpparams(base_resource) :
	""" Configuration for DHCP parameters resource. """
	def __init__(self) :
		self._dhcpclient = ""
		self._saveroute = ""
		self._ipaddress = ""
		self._netmask = ""
		self._hostrtgw = ""
		self._running = False

	@property
	def dhcpclient(self) :
		ur"""Enables DHCP client to acquire IP address from the DHCP server in the next boot. When set to OFF, disables the DHCP client in the next boot.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._dhcpclient
		except Exception as e:
			raise e

	@dhcpclient.setter
	def dhcpclient(self, dhcpclient) :
		ur"""Enables DHCP client to acquire IP address from the DHCP server in the next boot. When set to OFF, disables the DHCP client in the next boot.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._dhcpclient = dhcpclient
		except Exception as e:
			raise e

	@property
	def saveroute(self) :
		ur"""DHCP acquired routes are saved on the NetScaler appliance.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._saveroute
		except Exception as e:
			raise e

	@saveroute.setter
	def saveroute(self, saveroute) :
		ur"""DHCP acquired routes are saved on the NetScaler appliance.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._saveroute = saveroute
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""DHCP acquired IP.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""DHCP acquired Netmask.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@property
	def hostrtgw(self) :
		ur"""DHCP acquired Gateway.
		"""
		try :
			return self._hostrtgw
		except Exception as e:
			raise e

	@property
	def running(self) :
		ur"""DHCP mode.
		"""
		try :
			return self._running
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsdhcpparams_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsdhcpparams
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
		ur""" Use this API to update nsdhcpparams.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsdhcpparams()
				updateresource.dhcpclient = resource.dhcpclient
				updateresource.saveroute = resource.saveroute
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nsdhcpparams resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsdhcpparams()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsdhcpparams resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsdhcpparams()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Dhcpclient:
		ON = "ON"
		OFF = "OFF"

	class Saveroute:
		ON = "ON"
		OFF = "OFF"

class nsdhcpparams_response(base_response) :
	def __init__(self, length=1) :
		self.nsdhcpparams = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsdhcpparams = [nsdhcpparams() for _ in range(length)]

