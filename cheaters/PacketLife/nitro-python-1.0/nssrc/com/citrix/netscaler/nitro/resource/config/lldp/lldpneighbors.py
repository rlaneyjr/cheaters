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

class lldpneighbors(base_resource) :
	""" Configuration for lldp neighbors resource. """
	def __init__(self) :
		self._ifnum = ""
		self._chassisidsubtype = ""
		self._chassisid = ""
		self._portidsubtype = ""
		self._portid = ""
		self._ttl = 0
		self._portdescription = ""
		self._sys = ""
		self._sysdesc = ""
		self._mgmtaddresssubtype = ""
		self._mgmtaddress = ""
		self._iftype = ""
		self._ifnumber = 0
		self._vlan = ""
		self._vlanid = 0
		self._portprotosupported = 0
		self._portprotoenabled = 0
		self._portprotoid = 0
		self._portvlanid = 0
		self._protocolid = ""
		self._linkaggrcapable = ""
		self._linkaggrenabled = ""
		self._linkaggrid = 0
		self._flag = 0
		self._syscapabilities = ""
		self._syscapenabled = ""
		self._autonegsupport = ""
		self._autonegenabled = ""
		self._autonegadvertised = ""
		self._autonegmautype = ""
		self._mtu = 0
		self.___count = 0

	@property
	def ifnum(self) :
		ur"""Interface Name.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		ur"""Interface Name.
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def chassisidsubtype(self) :
		ur"""Chassis id sub type.<br/>Possible values = NONE, Component, Interface Alias, Port Component, MAC Address, Network Address, Interface Name, Locally Assigned.
		"""
		try :
			return self._chassisidsubtype
		except Exception as e:
			raise e

	@property
	def chassisid(self) :
		ur"""Chassis Id.
		"""
		try :
			return self._chassisid
		except Exception as e:
			raise e

	@property
	def portidsubtype(self) :
		ur"""Port id subtype.<br/>Possible values = NONE, Interface Alias, Port Component, MAC Address, Network Address, Interface Name, Agent Circuit ID, Locally Assigned.
		"""
		try :
			return self._portidsubtype
		except Exception as e:
			raise e

	@property
	def portid(self) :
		ur"""Port Id.
		"""
		try :
			return self._portid
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		ur"""Time to Live.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@property
	def portdescription(self) :
		ur"""Port Description.
		"""
		try :
			return self._portdescription
		except Exception as e:
			raise e

	@property
	def sys(self) :
		ur"""System Name.
		"""
		try :
			return self._sys
		except Exception as e:
			raise e

	@property
	def sysdesc(self) :
		ur"""System Description.
		"""
		try :
			return self._sysdesc
		except Exception as e:
			raise e

	@property
	def mgmtaddresssubtype(self) :
		ur"""Management Address Type.<br/>Possible values = OTHER, IPv4, IPv6.
		"""
		try :
			return self._mgmtaddresssubtype
		except Exception as e:
			raise e

	@property
	def mgmtaddress(self) :
		ur"""Management Address.
		"""
		try :
			return self._mgmtaddress
		except Exception as e:
			raise e

	@property
	def iftype(self) :
		ur"""Interface subtype.<br/>Possible values = UNKNOWN, ifIndex, system port number.
		"""
		try :
			return self._iftype
		except Exception as e:
			raise e

	@property
	def ifnumber(self) :
		ur"""Interface Number.
		"""
		try :
			return self._ifnumber
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		ur"""vlan name.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@property
	def vlanid(self) :
		ur"""Vlan Id.
		"""
		try :
			return self._vlanid
		except Exception as e:
			raise e

	@property
	def portprotosupported(self) :
		ur"""Flag to show Port Protocol Support.
		"""
		try :
			return self._portprotosupported
		except Exception as e:
			raise e

	@property
	def portprotoenabled(self) :
		ur"""Flag to show Port Protocol support enabled.
		"""
		try :
			return self._portprotoenabled
		except Exception as e:
			raise e

	@property
	def portprotoid(self) :
		ur"""Port Protocol ID.
		"""
		try :
			return self._portprotoid
		except Exception as e:
			raise e

	@property
	def portvlanid(self) :
		ur"""Port Vlan Id.
		"""
		try :
			return self._portvlanid
		except Exception as e:
			raise e

	@property
	def protocolid(self) :
		ur"""port vlan id name.
		"""
		try :
			return self._protocolid
		except Exception as e:
			raise e

	@property
	def linkaggrcapable(self) :
		ur"""Is neighbor Link Aggregation Capable.<br/>Possible values = NO, YES.
		"""
		try :
			return self._linkaggrcapable
		except Exception as e:
			raise e

	@property
	def linkaggrenabled(self) :
		ur"""Is link aggregation Enabled.<br/>Possible values = NO, YES.
		"""
		try :
			return self._linkaggrenabled
		except Exception as e:
			raise e

	@property
	def linkaggrid(self) :
		ur"""Link Aggregation Id.
		"""
		try :
			return self._linkaggrid
		except Exception as e:
			raise e

	@property
	def flag(self) :
		try :
			return self._flag
		except Exception as e:
			raise e

	@property
	def syscapabilities(self) :
		ur"""Acronyms for remote system capabilities:
		OT : Other.
		RE : Repeater(IETF RFC 2108).
		BR : MAC Bridge(IEEE Std 802.1D).
		WL : WLAN Access Point(IEEE Std 802.11 MIB).
		RO : ROuter(IETF RFC 1812).
		TE : Telephone(IETF RFC 4293).
		DO : DOCSIS cable device(IETF RFC 4639 and IETF RFC 4546).
		ST : STation only(IETF RFC 4293).
		CV : C-VLAN component of a VLAN Bridge(IEEE Std 802.1Q).
		SV : S-VLAN component of a VLAN Bridge(IEEE Std 802.1Q).
		MR : Two port MAC Relay(IEEE Std 802.1Q).
		"""
		try :
			return self._syscapabilities
		except Exception as e:
			raise e

	@property
	def syscapenabled(self) :
		ur"""Acronyms for remote system enabled capabilities:
		OT : Other.
		RE : Repeater(IETF RFC 2108).
		BR : MAC Bridge(IEEE Std 802.1D).
		WL : WLAN Access Point(IEEE Std 802.11 MIB).
		RO : ROuter(IETF RFC 1812).
		TE : Telephone(IETF RFC 4293).
		DO : DOCSIS cable device(IETF RFC 4639 and IETF RFC 4546).
		ST : STation only(IETF RFC 4293).
		CV : C-VLAN component of a VLAN Bridge(IEEE Std 802.1Q).
		SV : S-VLAN component of a VLAN Bridge(IEEE Std 802.1Q).
		MR : Two port MAC Relay(IEEE Std 802.1Q).
		"""
		try :
			return self._syscapenabled
		except Exception as e:
			raise e

	@property
	def autonegsupport(self) :
		ur"""MAC/PHY autonegotiation support.<br/>Possible values = NO, YES.
		"""
		try :
			return self._autonegsupport
		except Exception as e:
			raise e

	@property
	def autonegenabled(self) :
		ur"""MAC/PHY autonegotiation enabled.<br/>Possible values = NO, YES.
		"""
		try :
			return self._autonegenabled
		except Exception as e:
			raise e

	@property
	def autonegadvertised(self) :
		ur"""MAC/PHY autonegotiation advetised.
		"""
		try :
			return self._autonegadvertised
		except Exception as e:
			raise e

	@property
	def autonegmautype(self) :
		ur"""MAC/PHY Medium Attachment Unit (MAU) type of the port. Description listed below:
		AUI           - no internal MAU, view from AUI
		10Base5       - thick coax MAU
		Foirl         - FOIRL MAU
		10Base2       - thin coax MAU
		10BaseT       - UTP MAU
		10BaseFP      - passive fiber MAU
		10BaseFB      - sync fiber MAU
		10BaseFL      - async fiber MAU
		10Broad36     - broadband DTE MAU
		10BaseTHD     - UTP MAU, half duplex mode
		10BaseTFD     - UTP MAU, full duplex mode
		10BaseFLHD    - async fiber MAU, half duplex mode
		10BaseFLDF    - async fiber MAU, full duplex mode
		10BaseT4      - 4 pair category 3 UTP
		100BaseTXHD   - 2 pair category 5 UTP, half duplex mode
		100BaseTXFD   - 2 pair category 5 UTP, full duplex mode
		100BaseFXHD   - X fiber over PMT, half duplex mode
		100BaseFXFD   - X fiber over PMT, full duplex mode
		100BaseT2HD   - 2 pair category 3 UTP, half duplex mode
		100BaseT2DF   - 2 pair category 3 UTP, full duplex mode
		1000BaseXHD   - PCS/PMA, unknown PMD, half duplex mode
		1000BaseXFD   - PCS/PMA, unknown PMD, full duplex mode
		1000BaseLXHD  - Fiber over long-wavelength laser, half duplex mode
		1000BaseLXFD  - Fiber over long-wavelength laser, full duplex mode
		1000BaseSXHD  - Fiber over short-wavelength laser, half duplex mode
		1000BaseSXFD  - Fiber over short-wavelength laser, full duplex mode
		1000BaseCXHD  - Copper over 150-Ohm balanced cable, half duplex mode
		1000BaseCXFD  - Copper over 150-Ohm balanced cable, full duplex mode
		1000BaseTHD   - Four-pair Category 5 UTP, half duplex mode
		1000BaseTFD   - Four-pair Category 5 UTP, full duplex mode
		10GigBaseX    - X PCS/PMA, unknown PMD
		10GigBaseLX4  - X fiber over WWDM optics
		10GigBaseR    - R PCS/PMA, unknown PMD
		10GigBaseER   - R fiber over 1550 nm optics
		10GigBaseLR   - R fiber over 1310 nm optics
		10GigBaseSR   - R fiber over 850 nm optics
		10GigBaseW    - W PCS/PMA, unknown PMD
		10GigBaseEW   - W fiber over 1550 nm optics
		10GigBaseLW   - W fiber over 1310 nm optics
		10GigBaseSW   - W fiber over 850 nm optics.<br/>Possible values = Not Recieved, AUI, 10Base5, Foirl, 10Base2, 10BaseT, 10BaseFP, 10BaseFB, 10BaseFL, 10Broad36, 10BaseTHD, 10BaseTFD, 10BaseFLHD, 10BaseFLDF, 10BaseT4, 100BaseTXHD, 100BaseTXFD, 100BaseFXHD, 100BaseFXFD, 100BaseT2HD, 100BaseT2DF, 1000BaseXHD, 1000BaseXFD, 1000BaseLXHD, 1000BaseLXFD, 1000BaseSXHD, 1000BaseSXFD, 1000BaseCXHD, 1000BaseCXFD, 1000BaseTHD, 1000BaseTFD, 10GigBaseX, 10GigBaseLX4, 10GigBaseR, 10GigBaseER, 10GigBaseLR, 10GigBaseSR, 10GigBaseW, 10GigBaseEW, 10GigBaseLW, 10GigBaseSW.
		"""
		try :
			return self._autonegmautype
		except Exception as e:
			raise e

	@property
	def mtu(self) :
		ur"""MTU of Remote Device.
		"""
		try :
			return self._mtu
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lldpneighbors_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lldpneighbors
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ifnum is not None :
				return str(self.ifnum)
			return None
		except Exception as e :
			raise e



	@classmethod
	def clear(cls, client, resource="") :
		ur""" Use this API to clear lldpneighbors.
		"""
		try :
			if type(resource) is not list :
				clearresource = lldpneighbors()
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ lldpneighbors() for _ in range(len(resource))]
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lldpneighbors resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lldpneighbors()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lldpneighbors()
						obj.ifnum = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lldpneighbors() for _ in range(len(name))]
							obj = [lldpneighbors() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lldpneighbors()
								obj[i].ifnum = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lldpneighbors resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lldpneighbors()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lldpneighbors resources configured on NetScaler.
		"""
		try :
			obj = lldpneighbors()
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
		ur""" Use this API to count filtered the set of lldpneighbors resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lldpneighbors()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Mgmtaddresssubtype:
		OTHER = "OTHER"
		IPv4 = "IPv4"
		IPv6 = "IPv6"

	class Autonegmautype:
		Not_Recieved = "Not Recieved"
		AUI = "AUI"
		_10Base5 = "10Base5"
		Foirl = "Foirl"
		_10Base2 = "10Base2"
		_10BaseT = "10BaseT"
		_10BaseFP = "10BaseFP"
		_10BaseFB = "10BaseFB"
		_10BaseFL = "10BaseFL"
		_10Broad36 = "10Broad36"
		_10BaseTHD = "10BaseTHD"
		_10BaseTFD = "10BaseTFD"
		_10BaseFLHD = "10BaseFLHD"
		_10BaseFLDF = "10BaseFLDF"
		_10BaseT4 = "10BaseT4"
		_100BaseTXHD = "100BaseTXHD"
		_100BaseTXFD = "100BaseTXFD"
		_100BaseFXHD = "100BaseFXHD"
		_100BaseFXFD = "100BaseFXFD"
		_100BaseT2HD = "100BaseT2HD"
		_100BaseT2DF = "100BaseT2DF"
		_1000BaseXHD = "1000BaseXHD"
		_1000BaseXFD = "1000BaseXFD"
		_1000BaseLXHD = "1000BaseLXHD"
		_1000BaseLXFD = "1000BaseLXFD"
		_1000BaseSXHD = "1000BaseSXHD"
		_1000BaseSXFD = "1000BaseSXFD"
		_1000BaseCXHD = "1000BaseCXHD"
		_1000BaseCXFD = "1000BaseCXFD"
		_1000BaseTHD = "1000BaseTHD"
		_1000BaseTFD = "1000BaseTFD"
		_10GigBaseX = "10GigBaseX"
		_10GigBaseLX4 = "10GigBaseLX4"
		_10GigBaseR = "10GigBaseR"
		_10GigBaseER = "10GigBaseER"
		_10GigBaseLR = "10GigBaseLR"
		_10GigBaseSR = "10GigBaseSR"
		_10GigBaseW = "10GigBaseW"
		_10GigBaseEW = "10GigBaseEW"
		_10GigBaseLW = "10GigBaseLW"
		_10GigBaseSW = "10GigBaseSW"

	class Linkaggrcapable:
		NO = "NO"
		YES = "YES"

	class Autonegsupport:
		NO = "NO"
		YES = "YES"

	class Chassisidsubtype:
		NONE = "NONE"
		Component = "Component"
		Interface_Alias = "Interface Alias"
		Port_Component = "Port Component"
		MAC_Address = "MAC Address"
		Network_Address = "Network Address"
		Interface_Name = "Interface Name"
		Locally_Assigned = "Locally Assigned"

	class Portidsubtype:
		NONE = "NONE"
		Interface_Alias = "Interface Alias"
		Port_Component = "Port Component"
		MAC_Address = "MAC Address"
		Network_Address = "Network Address"
		Interface_Name = "Interface Name"
		Agent_Circuit_ID = "Agent Circuit ID"
		Locally_Assigned = "Locally Assigned"

	class Autonegenabled:
		NO = "NO"
		YES = "YES"

	class Iftype:
		UNKNOWN = "UNKNOWN"
		ifIndex = "ifIndex"
		system_port_number = "system port number"

	class Linkaggrenabled:
		NO = "NO"
		YES = "YES"

class lldpneighbors_response(base_response) :
	def __init__(self, length=1) :
		self.lldpneighbors = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lldpneighbors = [lldpneighbors() for _ in range(length)]

