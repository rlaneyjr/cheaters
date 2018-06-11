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

class lbparameter(base_resource) :
	""" Configuration for LB parameter resource. """
	def __init__(self) :
		self._httponlycookieflag = ""
		self._usesecuredpersistencecookie = ""
		self._cookiepassphrase = ""
		self._consolidatedlconn = ""
		self._useportforhashlb = ""
		self._preferdirectroute = ""
		self._startuprrfactor = 0
		self._monitorskipmaxclient = ""
		self._monitorconnectionclose = ""
		self._vserverspecificmac = ""
		self._sessionsthreshold = 0

	@property
	def httponlycookieflag(self) :
		ur"""Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute limits the scope of a cookie to HTTP requests and helps mitigate the risk of cross-site scripting attacks.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httponlycookieflag
		except Exception as e:
			raise e

	@httponlycookieflag.setter
	def httponlycookieflag(self, httponlycookieflag) :
		ur"""Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute limits the scope of a cookie to HTTP requests and helps mitigate the risk of cross-site scripting attacks.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httponlycookieflag = httponlycookieflag
		except Exception as e:
			raise e

	@property
	def usesecuredpersistencecookie(self) :
		ur"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._usesecuredpersistencecookie
		except Exception as e:
			raise e

	@usesecuredpersistencecookie.setter
	def usesecuredpersistencecookie(self, usesecuredpersistencecookie) :
		ur"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._usesecuredpersistencecookie = usesecuredpersistencecookie
		except Exception as e:
			raise e

	@property
	def cookiepassphrase(self) :
		ur"""Use this parameter to specify the passphrase used to generate secured persistence cookie value. It specifies the passphrase with a maximum of 31 characters.
		"""
		try :
			return self._cookiepassphrase
		except Exception as e:
			raise e

	@cookiepassphrase.setter
	def cookiepassphrase(self, cookiepassphrase) :
		ur"""Use this parameter to specify the passphrase used to generate secured persistence cookie value. It specifies the passphrase with a maximum of 31 characters.
		"""
		try :
			self._cookiepassphrase = cookiepassphrase
		except Exception as e:
			raise e

	@property
	def consolidatedlconn(self) :
		ur"""To find the service with the fewest connections, the virtual server uses the consolidated connection statistics from all the packet engines. The NO setting allows consideration of only the number of connections on the packet engine that received the new connection.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._consolidatedlconn
		except Exception as e:
			raise e

	@consolidatedlconn.setter
	def consolidatedlconn(self, consolidatedlconn) :
		ur"""To find the service with the fewest connections, the virtual server uses the consolidated connection statistics from all the packet engines. The NO setting allows consideration of only the number of connections on the packet engine that received the new connection.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._consolidatedlconn = consolidatedlconn
		except Exception as e:
			raise e

	@property
	def useportforhashlb(self) :
		ur"""Include the port number of the service when creating a hash for hash based load balancing methods. With the NO setting, only the IP address of the service is considered when creating a hash.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._useportforhashlb
		except Exception as e:
			raise e

	@useportforhashlb.setter
	def useportforhashlb(self, useportforhashlb) :
		ur"""Include the port number of the service when creating a hash for hash based load balancing methods. With the NO setting, only the IP address of the service is considered when creating a hash.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._useportforhashlb = useportforhashlb
		except Exception as e:
			raise e

	@property
	def preferdirectroute(self) :
		ur"""Perform route lookup for traffic received by the NetScaler appliance, and forward the traffic according to configured routes. Do not set this parameter if you want a wildcard virtual server to direct packets received by the appliance to an intermediary device, such as a firewall, even if their destination is directly connected to the appliance. Route lookup is performed after the packets have been processed and returned by the intermediary device.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._preferdirectroute
		except Exception as e:
			raise e

	@preferdirectroute.setter
	def preferdirectroute(self, preferdirectroute) :
		ur"""Perform route lookup for traffic received by the NetScaler appliance, and forward the traffic according to configured routes. Do not set this parameter if you want a wildcard virtual server to direct packets received by the appliance to an intermediary device, such as a firewall, even if their destination is directly connected to the appliance. Route lookup is performed after the packets have been processed and returned by the intermediary device.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._preferdirectroute = preferdirectroute
		except Exception as e:
			raise e

	@property
	def startuprrfactor(self) :
		ur"""Number of requests, per service, for which to apply the round robin load balancing method before switching to the configured load balancing method, thus allowing services to ramp up gradually to full load. Until the specified number of requests is distributed, the NetScaler appliance is said to be implementing the slow start mode (or startup round robin). Implemented for a virtual server when one of the following is true:
		* The virtual server is newly created.
		* One or more services are newly bound to the virtual server. 
		* One or more services bound to the virtual server are enabled.
		* The load balancing method is changed.
		This parameter applies to all the load balancing virtual servers configured on the NetScaler appliance, except for those virtual servers for which the virtual server-level slow start parameters (New Service Startup Request Rate and Increment Interval) are configured. If the global slow start parameter and the slow start parameters for a given virtual server are not set, the appliance implements a default slow start for the virtual server, as follows:
		* For a newly configured virtual server, the appliance implements slow start for the first 100 requests received by the virtual server.
		* For an existing virtual server, if one or more services are newly bound or newly enabled, or if the load balancing method is changed, the appliance dynamically computes the number of requests for which to implement startup round robin. It obtains this number by multiplying the request rate by the number of bound services (it includes services that are marked as DOWN). For example, if the current request rate is 20 requests/s and ten services are bound to the virtual server, the appliance performs startup round robin for 200 requests.
		Not applicable to a virtual server for which a hash based load balancing method is configured.
		"""
		try :
			return self._startuprrfactor
		except Exception as e:
			raise e

	@startuprrfactor.setter
	def startuprrfactor(self, startuprrfactor) :
		ur"""Number of requests, per service, for which to apply the round robin load balancing method before switching to the configured load balancing method, thus allowing services to ramp up gradually to full load. Until the specified number of requests is distributed, the NetScaler appliance is said to be implementing the slow start mode (or startup round robin). Implemented for a virtual server when one of the following is true:
		* The virtual server is newly created.
		* One or more services are newly bound to the virtual server. 
		* One or more services bound to the virtual server are enabled.
		* The load balancing method is changed.
		This parameter applies to all the load balancing virtual servers configured on the NetScaler appliance, except for those virtual servers for which the virtual server-level slow start parameters (New Service Startup Request Rate and Increment Interval) are configured. If the global slow start parameter and the slow start parameters for a given virtual server are not set, the appliance implements a default slow start for the virtual server, as follows:
		* For a newly configured virtual server, the appliance implements slow start for the first 100 requests received by the virtual server.
		* For an existing virtual server, if one or more services are newly bound or newly enabled, or if the load balancing method is changed, the appliance dynamically computes the number of requests for which to implement startup round robin. It obtains this number by multiplying the request rate by the number of bound services (it includes services that are marked as DOWN). For example, if the current request rate is 20 requests/s and ten services are bound to the virtual server, the appliance performs startup round robin for 200 requests.
		Not applicable to a virtual server for which a hash based load balancing method is configured.
		"""
		try :
			self._startuprrfactor = startuprrfactor
		except Exception as e:
			raise e

	@property
	def monitorskipmaxclient(self) :
		ur"""When a monitor initiates a connection to a service, do not check to determine whether the number of connections to the service has reached the limit specified by the service's Max Clients setting. Enables monitoring to continue even if the service has reached its connection limit.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._monitorskipmaxclient
		except Exception as e:
			raise e

	@monitorskipmaxclient.setter
	def monitorskipmaxclient(self, monitorskipmaxclient) :
		ur"""When a monitor initiates a connection to a service, do not check to determine whether the number of connections to the service has reached the limit specified by the service's Max Clients setting. Enables monitoring to continue even if the service has reached its connection limit.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._monitorskipmaxclient = monitorskipmaxclient
		except Exception as e:
			raise e

	@property
	def monitorconnectionclose(self) :
		ur"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: FIN<br/>Possible values = RESET, FIN.
		"""
		try :
			return self._monitorconnectionclose
		except Exception as e:
			raise e

	@monitorconnectionclose.setter
	def monitorconnectionclose(self, monitorconnectionclose) :
		ur"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: FIN<br/>Possible values = RESET, FIN
		"""
		try :
			self._monitorconnectionclose = monitorconnectionclose
		except Exception as e:
			raise e

	@property
	def vserverspecificmac(self) :
		ur"""Allow a MAC-mode virtual server to accept traffic returned by an intermediary device, such as a firewall, to which the traffic was previously forwarded by another MAC-mode virtual server. The second virtual server can then distribute that traffic across the destination server farm. Also useful when load balancing Branch Repeater appliances.
		Note: The second virtual server can also send the traffic to another set of intermediary devices, such as another set of firewalls. If necessary, you can configure multiple MAC-mode virtual servers to pass traffic successively through multiple sets of intermediary devices.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._vserverspecificmac
		except Exception as e:
			raise e

	@vserverspecificmac.setter
	def vserverspecificmac(self, vserverspecificmac) :
		ur"""Allow a MAC-mode virtual server to accept traffic returned by an intermediary device, such as a firewall, to which the traffic was previously forwarded by another MAC-mode virtual server. The second virtual server can then distribute that traffic across the destination server farm. Also useful when load balancing Branch Repeater appliances.
		Note: The second virtual server can also send the traffic to another set of intermediary devices, such as another set of firewalls. If necessary, you can configure multiple MAC-mode virtual servers to pass traffic successively through multiple sets of intermediary devices.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._vserverspecificmac = vserverspecificmac
		except Exception as e:
			raise e

	@property
	def sessionsthreshold(self) :
		ur"""This option is used to get the upper-limit on the number of persistent sessions set by the administrator for this system.<br/>Minimum value =  1.
		"""
		try :
			return self._sessionsthreshold
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbparameter
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
		ur""" Use this API to update lbparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = lbparameter()
				updateresource.httponlycookieflag = resource.httponlycookieflag
				updateresource.usesecuredpersistencecookie = resource.usesecuredpersistencecookie
				updateresource.cookiepassphrase = resource.cookiepassphrase
				updateresource.consolidatedlconn = resource.consolidatedlconn
				updateresource.useportforhashlb = resource.useportforhashlb
				updateresource.preferdirectroute = resource.preferdirectroute
				updateresource.startuprrfactor = resource.startuprrfactor
				updateresource.monitorskipmaxclient = resource.monitorskipmaxclient
				updateresource.monitorconnectionclose = resource.monitorconnectionclose
				updateresource.vserverspecificmac = resource.vserverspecificmac
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of lbparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lbparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Usesecuredpersistencecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httponlycookieflag:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Monitorconnectionclose:
		RESET = "RESET"
		FIN = "FIN"

	class Useportforhashlb:
		YES = "YES"
		NO = "NO"

	class Consolidatedlconn:
		YES = "YES"
		NO = "NO"

	class Vserverspecificmac:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Monitorskipmaxclient:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Preferdirectroute:
		YES = "YES"
		NO = "NO"

class lbparameter_response(base_response) :
	def __init__(self, length=1) :
		self.lbparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbparameter = [lbparameter() for _ in range(length)]

