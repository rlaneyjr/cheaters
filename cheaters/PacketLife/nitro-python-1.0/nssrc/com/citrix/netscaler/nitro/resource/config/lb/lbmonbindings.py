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

class lbmonbindings(base_resource) :
	""" Configuration for monitro bindings resource. """
	def __init__(self) :
		self._monitorname = ""
		self._type = ""
		self._state = ""
		self.___count = 0

	@property
	def monitorname(self) :
		ur"""The name of the monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._monitorname
		except Exception as e:
			raise e

	@monitorname.setter
	def monitorname(self, monitorname) :
		ur"""The name of the monitor.<br/>Minimum length =  1
		"""
		try :
			self._monitorname = monitorname
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""The type of monitor.<br/>Possible values = PING, TCP, HTTP, TCP-ECV, HTTP-ECV, UDP-ECV, DNS, FTP, LDNS-PING, LDNS-TCP, LDNS-DNS, RADIUS, USER, HTTP-INLINE, SIP-UDP, LOAD, FTP-EXTENDED, SMTP, SNMP, NNTP, MYSQL, MYSQL-ECV, MSSQL-ECV, ORACLE-ECV, LDAP, POP3, CITRIX-XML-SERVICE, CITRIX-WEB-INTERFACE, DNS-TCP, RTSP, ARP, CITRIX-AG, CITRIX-AAC-LOGINPAGE, CITRIX-AAC-LAS, CITRIX-XD-DDC, ND6, CITRIX-WI-EXTENDED, DIAMETER, RADIUS_ACCOUNTING, STOREFRONT, APPC, CITRIX-XNC-ECV, CITRIX-XDM.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""The state of the monitor.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmonbindings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmonbindings
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.monitorname is not None :
				return str(self.monitorname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lbmonbindings resources that are configured on netscaler.
		"""
		try :
				if type(name) != cls :
					if type(name) is not list :
						obj = lbmonbindings()
						obj.monitorname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lbmonbindings() for _ in range(len(name))]
							obj = [lbmonbindings() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lbmonbindings()
								obj[i].monitorname = name[i]
								response[i] = obj[i].get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_, obj) :
		ur""" Use this API to fetch filtered set of lbmonbindings resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client, obj) :
		ur""" Use this API to count the lbmonbindings resources configured on NetScaler.
		"""
		try :
			option_ = options()
			option_.count = True
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_, obj) :
		ur""" Use this API to count filtered the set of lbmonbindings resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.count = True
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		PING = "PING"
		TCP = "TCP"
		HTTP = "HTTP"
		TCP_ECV = "TCP-ECV"
		HTTP_ECV = "HTTP-ECV"
		UDP_ECV = "UDP-ECV"
		DNS = "DNS"
		FTP = "FTP"
		LDNS_PING = "LDNS-PING"
		LDNS_TCP = "LDNS-TCP"
		LDNS_DNS = "LDNS-DNS"
		RADIUS = "RADIUS"
		USER = "USER"
		HTTP_INLINE = "HTTP-INLINE"
		SIP_UDP = "SIP-UDP"
		LOAD = "LOAD"
		FTP_EXTENDED = "FTP-EXTENDED"
		SMTP = "SMTP"
		SNMP = "SNMP"
		NNTP = "NNTP"
		MYSQL = "MYSQL"
		MYSQL_ECV = "MYSQL-ECV"
		MSSQL_ECV = "MSSQL-ECV"
		ORACLE_ECV = "ORACLE-ECV"
		LDAP = "LDAP"
		POP3 = "POP3"
		CITRIX_XML_SERVICE = "CITRIX-XML-SERVICE"
		CITRIX_WEB_INTERFACE = "CITRIX-WEB-INTERFACE"
		DNS_TCP = "DNS-TCP"
		RTSP = "RTSP"
		ARP = "ARP"
		CITRIX_AG = "CITRIX-AG"
		CITRIX_AAC_LOGINPAGE = "CITRIX-AAC-LOGINPAGE"
		CITRIX_AAC_LAS = "CITRIX-AAC-LAS"
		CITRIX_XD_DDC = "CITRIX-XD-DDC"
		ND6 = "ND6"
		CITRIX_WI_EXTENDED = "CITRIX-WI-EXTENDED"
		DIAMETER = "DIAMETER"
		RADIUS_ACCOUNTING = "RADIUS_ACCOUNTING"
		STOREFRONT = "STOREFRONT"
		APPC = "APPC"
		CITRIX_XNC_ECV = "CITRIX-XNC-ECV"
		CITRIX_XDM = "CITRIX-XDM"

class lbmonbindings_response(base_response) :
	def __init__(self, length=1) :
		self.lbmonbindings = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmonbindings = [lbmonbindings() for _ in range(length)]

