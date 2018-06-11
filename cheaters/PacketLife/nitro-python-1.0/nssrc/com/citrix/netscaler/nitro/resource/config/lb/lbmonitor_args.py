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


class lbmonitor_args :
	ur""" Provides additional arguments required for fetching the lbmonitor resource.
	"""
	def __init__(self) :
		self._type = ""

	@property
	def type(self) :
		ur"""Type of monitor that you want to create.<br/>Possible values = PING, TCP, HTTP, TCP-ECV, HTTP-ECV, UDP-ECV, DNS, FTP, LDNS-PING, LDNS-TCP, LDNS-DNS, RADIUS, USER, HTTP-INLINE, SIP-UDP, LOAD, FTP-EXTENDED, SMTP, SNMP, NNTP, MYSQL, MYSQL-ECV, MSSQL-ECV, ORACLE-ECV, LDAP, POP3, CITRIX-XML-SERVICE, CITRIX-WEB-INTERFACE, DNS-TCP, RTSP, ARP, CITRIX-AG, CITRIX-AAC-LOGINPAGE, CITRIX-AAC-LAS, CITRIX-XD-DDC, ND6, CITRIX-WI-EXTENDED, DIAMETER, RADIUS_ACCOUNTING, STOREFRONT, APPC, CITRIX-XNC-ECV, CITRIX-XDM.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of monitor that you want to create.<br/>Possible values = PING, TCP, HTTP, TCP-ECV, HTTP-ECV, UDP-ECV, DNS, FTP, LDNS-PING, LDNS-TCP, LDNS-DNS, RADIUS, USER, HTTP-INLINE, SIP-UDP, LOAD, FTP-EXTENDED, SMTP, SNMP, NNTP, MYSQL, MYSQL-ECV, MSSQL-ECV, ORACLE-ECV, LDAP, POP3, CITRIX-XML-SERVICE, CITRIX-WEB-INTERFACE, DNS-TCP, RTSP, ARP, CITRIX-AG, CITRIX-AAC-LOGINPAGE, CITRIX-AAC-LAS, CITRIX-XD-DDC, ND6, CITRIX-WI-EXTENDED, DIAMETER, RADIUS_ACCOUNTING, STOREFRONT, APPC, CITRIX-XNC-ECV, CITRIX-XDM
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

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

