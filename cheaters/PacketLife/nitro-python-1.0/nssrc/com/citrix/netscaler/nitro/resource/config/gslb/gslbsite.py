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

class gslbsite(base_resource) :
	""" Configuration for GSLB site resource. """
	def __init__(self) :
		self._sitename = ""
		self._sitetype = ""
		self._siteipaddress = ""
		self._publicip = ""
		self._metricexchange = ""
		self._nwmetricexchange = ""
		self._sessionexchange = ""
		self._triggermonitor = ""
		self._parentsite = ""
		self._clip = ""
		self._publicclip = ""
		self._status = ""
		self._persistencemepstatus = ""
		self._version = 0
		self.___count = 0

	@property
	def sitename(self) :
		ur"""Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my gslbsite" or 'my gslbsite').<br/>Minimum length =  1.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@sitename.setter
	def sitename(self, sitename) :
		ur"""Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my gslbsite" or 'my gslbsite').<br/>Minimum length =  1
		"""
		try :
			self._sitename = sitename
		except Exception as e:
			raise e

	@property
	def sitetype(self) :
		ur"""Type of site to create. If the type is not specified, the appliance automatically detects and sets the type on the basis of the IP address being assigned to the site. If the specified site IP address is owned by the appliance (for example, a MIP address or SNIP address), the site is a local site. Otherwise, it is a remote site.<br/>Default value: NONE<br/>Possible values = REMOTE, LOCAL.
		"""
		try :
			return self._sitetype
		except Exception as e:
			raise e

	@sitetype.setter
	def sitetype(self, sitetype) :
		ur"""Type of site to create. If the type is not specified, the appliance automatically detects and sets the type on the basis of the IP address being assigned to the site. If the specified site IP address is owned by the appliance (for example, a MIP address or SNIP address), the site is a local site. Otherwise, it is a remote site.<br/>Default value: NONE<br/>Possible values = REMOTE, LOCAL
		"""
		try :
			self._sitetype = sitetype
		except Exception as e:
			raise e

	@property
	def siteipaddress(self) :
		ur"""IP address for the GSLB site. The GSLB site uses this IP address to communicate with other GSLB sites. For a local site, use any IP address that is owned by the appliance (for example, a SNIP or MIP address, or the IP address of the ADNS service).<br/>Minimum length =  1.
		"""
		try :
			return self._siteipaddress
		except Exception as e:
			raise e

	@siteipaddress.setter
	def siteipaddress(self, siteipaddress) :
		ur"""IP address for the GSLB site. The GSLB site uses this IP address to communicate with other GSLB sites. For a local site, use any IP address that is owned by the appliance (for example, a SNIP or MIP address, or the IP address of the ADNS service).<br/>Minimum length =  1
		"""
		try :
			self._siteipaddress = siteipaddress
		except Exception as e:
			raise e

	@property
	def publicip(self) :
		ur"""Public IP address for the local site. Required only if the appliance is deployed in a private address space and the site has a public IP address hosted on an external firewall or a NAT device.<br/>Minimum length =  1.
		"""
		try :
			return self._publicip
		except Exception as e:
			raise e

	@publicip.setter
	def publicip(self, publicip) :
		ur"""Public IP address for the local site. Required only if the appliance is deployed in a private address space and the site has a public IP address hosted on an external firewall or a NAT device.<br/>Minimum length =  1
		"""
		try :
			self._publicip = publicip
		except Exception as e:
			raise e

	@property
	def metricexchange(self) :
		ur"""Exchange metrics with other sites. Metrics are exchanged by using Metric Exchange Protocol (MEP). The appliances in the GSLB setup exchange health information once every second. 
		If you disable metrics exchange, you can use only static load balancing methods (such as round robin, static proximity, or the hash-based methods), and if you disable metrics exchange when a dynamic load balancing method (such as least connection) is in operation, the appliance falls back to round robin. Also, if you disable metrics exchange, you must use a monitor to determine the state of GSLB services. Otherwise, the service is marked as DOWN.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._metricexchange
		except Exception as e:
			raise e

	@metricexchange.setter
	def metricexchange(self, metricexchange) :
		ur"""Exchange metrics with other sites. Metrics are exchanged by using Metric Exchange Protocol (MEP). The appliances in the GSLB setup exchange health information once every second. 
		If you disable metrics exchange, you can use only static load balancing methods (such as round robin, static proximity, or the hash-based methods), and if you disable metrics exchange when a dynamic load balancing method (such as least connection) is in operation, the appliance falls back to round robin. Also, if you disable metrics exchange, you must use a monitor to determine the state of GSLB services. Otherwise, the service is marked as DOWN.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._metricexchange = metricexchange
		except Exception as e:
			raise e

	@property
	def nwmetricexchange(self) :
		ur"""Exchange, with other GSLB sites, network metrics such as round-trip time (RTT), learned from communications with various local DNS (LDNS) servers used by clients. RTT information is used in the dynamic RTT load balancing method, and is exchanged every 5 seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nwmetricexchange
		except Exception as e:
			raise e

	@nwmetricexchange.setter
	def nwmetricexchange(self, nwmetricexchange) :
		ur"""Exchange, with other GSLB sites, network metrics such as round-trip time (RTT), learned from communications with various local DNS (LDNS) servers used by clients. RTT information is used in the dynamic RTT load balancing method, and is exchanged every 5 seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nwmetricexchange = nwmetricexchange
		except Exception as e:
			raise e

	@property
	def sessionexchange(self) :
		ur"""Exchange persistent session entries with other GSLB sites every five seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionexchange
		except Exception as e:
			raise e

	@sessionexchange.setter
	def sessionexchange(self, sessionexchange) :
		ur"""Exchange persistent session entries with other GSLB sites every five seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionexchange = sessionexchange
		except Exception as e:
			raise e

	@property
	def triggermonitor(self) :
		ur"""Specify the conditions under which the GSLB service must be monitored by a monitor, if one is bound. Available settings function as follows:
		* ALWAYS - Monitor the GSLB service at all times.
		* MEPDOWN - Monitor the GSLB service only when the exchange of metrics through the Metrics Exchange Protocol (MEP) is disabled.
		MEPDOWN_SVCDOWN - Monitor the service in either of the following situations: 
		* The exchange of metrics through MEP is disabled.
		* The exchange of metrics through MEP is enabled but the status of the service, learned through metrics exchange, is DOWN.<br/>Default value: ALWAYS<br/>Possible values = ALWAYS, MEPDOWN, MEPDOWN_SVCDOWN.
		"""
		try :
			return self._triggermonitor
		except Exception as e:
			raise e

	@triggermonitor.setter
	def triggermonitor(self, triggermonitor) :
		ur"""Specify the conditions under which the GSLB service must be monitored by a monitor, if one is bound. Available settings function as follows:
		* ALWAYS - Monitor the GSLB service at all times.
		* MEPDOWN - Monitor the GSLB service only when the exchange of metrics through the Metrics Exchange Protocol (MEP) is disabled.
		MEPDOWN_SVCDOWN - Monitor the service in either of the following situations: 
		* The exchange of metrics through MEP is disabled.
		* The exchange of metrics through MEP is enabled but the status of the service, learned through metrics exchange, is DOWN.<br/>Default value: ALWAYS<br/>Possible values = ALWAYS, MEPDOWN, MEPDOWN_SVCDOWN
		"""
		try :
			self._triggermonitor = triggermonitor
		except Exception as e:
			raise e

	@property
	def parentsite(self) :
		ur"""Parent site of the GSLB site, in a parent-child topology.
		"""
		try :
			return self._parentsite
		except Exception as e:
			raise e

	@parentsite.setter
	def parentsite(self, parentsite) :
		ur"""Parent site of the GSLB site, in a parent-child topology.
		"""
		try :
			self._parentsite = parentsite
		except Exception as e:
			raise e

	@property
	def clip(self) :
		ur"""Cluster IP used to connect to remote cluster site for GSLB autosync.
		"""
		try :
			return self._clip
		except Exception as e:
			raise e

	@clip.setter
	def clip(self, clip) :
		ur"""Cluster IP used to connect to remote cluster site for GSLB autosync.
		"""
		try :
			self._clip = clip
		except Exception as e:
			raise e

	@property
	def publicclip(self) :
		ur"""Public cluster IP used to connect to remote cluster site for GSLB autosync if the remote cluster is behind a NAT.
		"""
		try :
			return self._publicclip
		except Exception as e:
			raise e

	@publicclip.setter
	def publicclip(self, publicclip) :
		ur"""Public cluster IP used to connect to remote cluster site for GSLB autosync if the remote cluster is behind a NAT.
		"""
		try :
			self._publicclip = publicclip
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""Current metric exchange status.<br/>Possible values = ACTIVE, INACTIVE, DOWN.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def persistencemepstatus(self) :
		ur"""Network metric and persistence exchange MEP connection status.<br/>Possible values = ACTIVE, INACTIVE, DOWN.
		"""
		try :
			return self._persistencemepstatus
		except Exception as e:
			raise e

	@property
	def version(self) :
		ur"""will be true if the remote site's version is ncore compatible with the local site.(>= 9.2).
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbsite_response, response, self.__class__.__name__)
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
	def add(cls, client, resource) :
		ur""" Use this API to add gslbsite.
		"""
		try :
			if type(resource) is not list :
				addresource = gslbsite()
				addresource.sitename = resource.sitename
				addresource.sitetype = resource.sitetype
				addresource.siteipaddress = resource.siteipaddress
				addresource.publicip = resource.publicip
				addresource.metricexchange = resource.metricexchange
				addresource.nwmetricexchange = resource.nwmetricexchange
				addresource.sessionexchange = resource.sessionexchange
				addresource.triggermonitor = resource.triggermonitor
				addresource.parentsite = resource.parentsite
				addresource.clip = resource.clip
				addresource.publicclip = resource.publicclip
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ gslbsite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].sitename = resource[i].sitename
						addresources[i].sitetype = resource[i].sitetype
						addresources[i].siteipaddress = resource[i].siteipaddress
						addresources[i].publicip = resource[i].publicip
						addresources[i].metricexchange = resource[i].metricexchange
						addresources[i].nwmetricexchange = resource[i].nwmetricexchange
						addresources[i].sessionexchange = resource[i].sessionexchange
						addresources[i].triggermonitor = resource[i].triggermonitor
						addresources[i].parentsite = resource[i].parentsite
						addresources[i].clip = resource[i].clip
						addresources[i].publicclip = resource[i].publicclip
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete gslbsite.
		"""
		try :
			if type(resource) is not list :
				deleteresource = gslbsite()
				if type(resource) !=  type(deleteresource):
					deleteresource.sitename = resource
				else :
					deleteresource.sitename = resource.sitename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitename = resource[i].sitename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update gslbsite.
		"""
		try :
			if type(resource) is not list :
				updateresource = gslbsite()
				updateresource.sitename = resource.sitename
				updateresource.metricexchange = resource.metricexchange
				updateresource.nwmetricexchange = resource.nwmetricexchange
				updateresource.sessionexchange = resource.sessionexchange
				updateresource.triggermonitor = resource.triggermonitor
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ gslbsite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].sitename = resource[i].sitename
						updateresources[i].metricexchange = resource[i].metricexchange
						updateresources[i].nwmetricexchange = resource[i].nwmetricexchange
						updateresources[i].sessionexchange = resource[i].sessionexchange
						updateresources[i].triggermonitor = resource[i].triggermonitor
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of gslbsite resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = gslbsite()
				if type(resource) !=  type(unsetresource):
					unsetresource.sitename = resource
				else :
					unsetresource.sitename = resource.sitename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sitename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sitename = resource[i].sitename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the gslbsite resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbsite()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = gslbsite()
						obj.sitename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [gslbsite() for _ in range(len(name))]
							obj = [gslbsite() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = gslbsite()
								obj[i].sitename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of gslbsite resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbsite()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the gslbsite resources configured on NetScaler.
		"""
		try :
			obj = gslbsite()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		ur""" Use this API to count filtered the set of gslbsite resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbsite()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sessionexchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nwmetricexchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Status:
		ACTIVE = "ACTIVE"
		INACTIVE = "INACTIVE"
		DOWN = "DOWN"

	class Triggermonitor:
		ALWAYS = "ALWAYS"
		MEPDOWN = "MEPDOWN"
		MEPDOWN_SVCDOWN = "MEPDOWN_SVCDOWN"

	class Persistencemepstatus:
		ACTIVE = "ACTIVE"
		INACTIVE = "INACTIVE"
		DOWN = "DOWN"

	class Metricexchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sitetype:
		REMOTE = "REMOTE"
		LOCAL = "LOCAL"

class gslbsite_response(base_response) :
	def __init__(self, length=1) :
		self.gslbsite = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbsite = [gslbsite() for _ in range(length)]

