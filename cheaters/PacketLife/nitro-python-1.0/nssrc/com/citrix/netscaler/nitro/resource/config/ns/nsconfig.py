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

class nsconfig(base_resource) :
	""" Configuration for system config resource. """
	def __init__(self) :
		self._force = False
		self._level = ""
		self._ipaddress = ""
		self._netmask = ""
		self._nsvlan = 0
		self._ifnum = []
		self._tagged = ""
		self._httpport = []
		self._maxconn = 0
		self._maxreq = 0
		self._cip = ""
		self._cipheader = ""
		self._cookieversion = ""
		self._securecookie = ""
		self._pmtumin = 0
		self._pmtutimeout = 0
		self._ftpportrange = ""
		self._crportrange = ""
		self._timezone = ""
		self._grantquotamaxclient = 0
		self._exclusivequotamaxclient = 0
		self._grantquotaspillover = 0
		self._exclusivequotaspillover = 0
		self._nwfwmode = ""
		self._config1 = ""
		self._config2 = ""
		self._outtype = ""
		self._template = False
		self._ignoredevicespecific = False
		self._message = ""
		self._mappedip = ""
		self._range = 0
		self._systemtype = ""
		self._primaryip = ""
		self._flags = 0
		self._lastconfigchangedtime = ""
		self._lastconfigsavetime = ""
		self._currentsytemtime = ""
		self._systemtime = 0
		self._response = ""

	@property
	def force(self) :
		ur"""Configurations will be cleared without prompting for confirmation.
		"""
		try :
			return self._force
		except Exception as e:
			raise e

	@force.setter
	def force(self, force) :
		ur"""Configurations will be cleared without prompting for confirmation.
		"""
		try :
			self._force = force
		except Exception as e:
			raise e

	@property
	def level(self) :
		ur"""Types of configurations to be cleared.
		* basic: Clears all configurations except the following:
		- NSIP, default route (gateway), MIPs, and SNIPs
		- Network settings (DG, VLAN, RHI, NTP and DNS settings)
		- Cluster settings
		- HA node definitions
		- Feature and mode settings
		- nsroot password
		* extended: Clears the same configurations as the 'basic' option. In addition, it clears the nsroot password and feature and mode settings.
		* full: Clears all configurations except NSIP, default route, and interface settings.
		Note: When you clear the configurations through the cluster IP address, by specifying the level as 'full', the cluster is deleted and all cluster nodes become standalone appliances. The 'basic' and 'extended' levels are propagated to the cluster nodes.<br/>Possible values = basic, extended, full.
		"""
		try :
			return self._level
		except Exception as e:
			raise e

	@level.setter
	def level(self, level) :
		ur"""Types of configurations to be cleared.
		* basic: Clears all configurations except the following:
		- NSIP, default route (gateway), MIPs, and SNIPs
		- Network settings (DG, VLAN, RHI, NTP and DNS settings)
		- Cluster settings
		- HA node definitions
		- Feature and mode settings
		- nsroot password
		* extended: Clears the same configurations as the 'basic' option. In addition, it clears the nsroot password and feature and mode settings.
		* full: Clears all configurations except NSIP, default route, and interface settings.
		Note: When you clear the configurations through the cluster IP address, by specifying the level as 'full', the cluster is deleted and all cluster nodes become standalone appliances. The 'basic' and 'extended' levels are propagated to the cluster nodes.<br/>Possible values = basic, extended, full
		"""
		try :
			self._level = level
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""IP address of the NetScaler appliance. Commonly referred to as NSIP address. This parameter is mandatory to bring up the appliance.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		ur"""IP address of the NetScaler appliance. Commonly referred to as NSIP address. This parameter is mandatory to bring up the appliance.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		ur"""Netmask corresponding to the IP address. This parameter is mandatory to bring up the appliance.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		ur"""Netmask corresponding to the IP address. This parameter is mandatory to bring up the appliance.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def nsvlan(self) :
		ur"""VLAN (NSVLAN) for the subnet on which the IP address resides.<br/>Minimum length =  2<br/>Maximum length =  4094.
		"""
		try :
			return self._nsvlan
		except Exception as e:
			raise e

	@nsvlan.setter
	def nsvlan(self, nsvlan) :
		ur"""VLAN (NSVLAN) for the subnet on which the IP address resides.<br/>Minimum length =  2<br/>Maximum length =  4094
		"""
		try :
			self._nsvlan = nsvlan
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		ur"""Interfaces of the appliances that must be bound to the NSVLAN.<br/>Minimum length =  1.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		ur"""Interfaces of the appliances that must be bound to the NSVLAN.<br/>Minimum length =  1
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def tagged(self) :
		ur"""Specifies that the interfaces will be added as 802.1q tagged interfaces. Packets sent on these interface on this VLAN will have an additional 4-byte 802.1q tag which identifies the VLAN.
		To use 802.1q tagging, the switch connected to the appliance's interfaces must also be configured for tagging.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._tagged
		except Exception as e:
			raise e

	@tagged.setter
	def tagged(self, tagged) :
		ur"""Specifies that the interfaces will be added as 802.1q tagged interfaces. Packets sent on these interface on this VLAN will have an additional 4-byte 802.1q tag which identifies the VLAN.
		To use 802.1q tagging, the switch connected to the appliance's interfaces must also be configured for tagging.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._tagged = tagged
		except Exception as e:
			raise e

	@property
	def httpport(self) :
		ur"""The HTTP ports on the Web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1.
		"""
		try :
			return self._httpport
		except Exception as e:
			raise e

	@httpport.setter
	def httpport(self, httpport) :
		ur"""The HTTP ports on the Web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1
		"""
		try :
			self._httpport = httpport
		except Exception as e:
			raise e

	@property
	def maxconn(self) :
		ur"""The maximum number of connections that will be made from the system to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Maximum length =  4294967294.
		"""
		try :
			return self._maxconn
		except Exception as e:
			raise e

	@maxconn.setter
	def maxconn(self, maxconn) :
		ur"""The maximum number of connections that will be made from the system to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Maximum length =  4294967294
		"""
		try :
			self._maxconn = maxconn
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		ur"""The maximum number of requests that the system can pass on a particular connection between the system and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed.<br/>Maximum length =  65535.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		ur"""The maximum number of requests that the system can pass on a particular connection between the system and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed.<br/>Maximum length =  65535
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def cip(self) :
		ur"""The option to control (enable or disable) the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system.
		The passed address can then be accessed through a minor modification to the server.
		l	If cipHeader is specified, it will be used as the client IP header.
		l	If it is not specified, then the value that has been set by the set ns config CLI command will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@cip.setter
	def cip(self, cip) :
		ur"""The option to control (enable or disable) the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system.
		The passed address can then be accessed through a minor modification to the server.
		l	If cipHeader is specified, it will be used as the client IP header.
		l	If it is not specified, then the value that has been set by the set ns config CLI command will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cip = cip
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		ur"""The text that will be used as the client IP header.<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@cipheader.setter
	def cipheader(self, cipheader) :
		ur"""The text that will be used as the client IP header.<br/>Minimum length =  1
		"""
		try :
			self._cipheader = cipheader
		except Exception as e:
			raise e

	@property
	def cookieversion(self) :
		ur"""The version of the cookie inserted by system.<br/>Possible values = 0, 1.
		"""
		try :
			return self._cookieversion
		except Exception as e:
			raise e

	@cookieversion.setter
	def cookieversion(self, cookieversion) :
		ur"""The version of the cookie inserted by system.<br/>Possible values = 0, 1
		"""
		try :
			self._cookieversion = cookieversion
		except Exception as e:
			raise e

	@property
	def securecookie(self) :
		ur"""enable/disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._securecookie
		except Exception as e:
			raise e

	@securecookie.setter
	def securecookie(self, securecookie) :
		ur"""enable/disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._securecookie = securecookie
		except Exception as e:
			raise e

	@property
	def pmtumin(self) :
		ur"""The minimum Path MTU.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500.
		"""
		try :
			return self._pmtumin
		except Exception as e:
			raise e

	@pmtumin.setter
	def pmtumin(self, pmtumin) :
		ur"""The minimum Path MTU.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500
		"""
		try :
			self._pmtumin = pmtumin
		except Exception as e:
			raise e

	@property
	def pmtutimeout(self) :
		ur"""The timeout value in minutes.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._pmtutimeout
		except Exception as e:
			raise e

	@pmtutimeout.setter
	def pmtutimeout(self, pmtutimeout) :
		ur"""The timeout value in minutes.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._pmtutimeout = pmtutimeout
		except Exception as e:
			raise e

	@property
	def ftpportrange(self) :
		ur"""Port range configured for FTP services.<br/>Minimum length =  1024<br/>Maximum length =  64000.
		"""
		try :
			return self._ftpportrange
		except Exception as e:
			raise e

	@ftpportrange.setter
	def ftpportrange(self, ftpportrange) :
		ur"""Port range configured for FTP services.<br/>Minimum length =  1024<br/>Maximum length =  64000
		"""
		try :
			self._ftpportrange = ftpportrange
		except Exception as e:
			raise e

	@property
	def crportrange(self) :
		ur"""Port range for cache redirection services.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._crportrange
		except Exception as e:
			raise e

	@crportrange.setter
	def crportrange(self, crportrange) :
		ur"""Port range for cache redirection services.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._crportrange = crportrange
		except Exception as e:
			raise e

	@property
	def timezone(self) :
		ur"""Name of the timezone.<br/>Possible values = CoordinatedUniversalTime, GMT+01:00-CET-Europe/Andorra, GMT+04:00-GST-Asia/Dubai, GMT+04:30-AFT-Asia/Kabul, GMT-04:00-AST-America/Antigua, GMT-04:00-AST-America/Anguilla, GMT+01:00-CET-Europe/Tirane, GMT+04:00-AMT-Asia/Yerevan, GMT+01:00-WAT-Africa/Luanda, GMT+13:00-NZDT-Antarctica/McMurdo, GMT+13:00-NZDT-Antarctica/South_Pole, GMT-03:00-ROTT-Antarctica/Rothera, GMT-04:00-CLT-Antarctica/Palmer, GMT+05:00-MAWT-Antarctica/Mawson, GMT+07:00-DAVT-Antarctica/Davis, GMT+08:00-WST-Antarctica/Casey, GMT+06:00-VOST-Antarctica/Vostok, GMT+10:00-DDUT-Antarctica/DumontDUrville, GMT+03:00-SYOT-Antarctica/Syowa, GMT+11:00-MIST-Antarctica/Macquarie, GMT-03:00-ART-America/Argentina/Buenos_Aires, GMT-03:00-ART-America/Argentina/Cordoba, GMT-03:00-ART-America/Argentina/Salta, GMT-03:00-ART-America/Argentina/Jujuy, GMT-03:00-ART-America/Argentina/Tucuman, GMT-03:00-ART-America/Argentina/Catamarca, GMT-03:00-ART-America/Argentina/La_Rioja, GMT-03:00-ART-America/Argentina/San_Juan, GMT-03:00-ART-America/Argentina/Mendoza, GMT-03:00-WARST-America/Argentina/San_Luis, GMT-03:00-ART-America/Argentina/Rio_Gallegos, GMT-03:00-ART-America/Argentina/Ushuaia, GMT-11:00-SST-Pacific/Pago_Pago, GMT+01:00-CET-Europe/Vienna, GMT+11:00-LHST-Australia/Lord_Howe, GMT+11:00-EST-Australia/Hobart, GMT+11:00-EST-Australia/Currie, GMT+11:00-EST-Australia/Melbourne, GMT+11:00-EST-Australia/Sydney, GMT+10:30-CST-Australia/Broken_Hill, GMT+10:00-EST-Australia/Brisbane, GMT+10:00-EST-Australia/Lindeman, GMT+10:30-CST-Australia/Adelaide, GMT+09:30-CST-Australia/Darwin, GMT+08:00-WST-Australia/Perth, GMT+08:45-CWST-Australia/Eucla, GMT-04:00-AST-America/Aruba, GMT+02:00-EET-Europe/Mariehamn, GMT+04:00-AZT-Asia/Baku, GMT+01:00-CET-Europe/Sarajevo, GMT-04:00-AST-America/Barbados, GMT+06:00-BDT-Asia/Dhaka, GMT+01:00-CET-Europe/Brussels, GMT+00:00-GMT-Africa/Ouagadougou, GMT+02:00-EET-Europe/Sofia, GMT+03:00-AST-Asia/Bahrain, GMT+02:00-CAT-Africa/Bujumbura, GMT+01:00-WAT-Africa/Porto-Novo, GMT-04:00-AST-America/St_Barthelemy, GMT-03:00-ADT-Atlantic/Bermuda, GMT+08:00-BNT-Asia/Brunei, GMT-04:00-BOT-America/La_Paz, GMT-02:00-FNT-America/Noronha, GMT-03:00-BRT-America/Belem, GMT-03:00-BRT-America/Fortaleza, GMT-03:00-BRT-America/Recife, GMT-03:00-BRT-America/Araguaina, GMT-03:00-BRT-America/Maceio, GMT-03:00-BRT-America/Bahia, GMT-03:00-BRT-America/Sao_Paulo, GMT-04:00-AMT-America/Campo_Grande, GMT-04:00-AMT-America/Cuiaba, GMT-03:00-BRT-America/Santarem, GMT-04:00-AMT-America/Porto_Velho, GMT-04:00-AMT-America/Boa_Vista, GMT-04:00-AMT-America/Manaus, GMT-04:00-AMT-America/Eirunepe, GMT-04:00-AMT-America/Rio_Branco, GMT-04:00-EDT-America/Nassau, GMT+06:00-BTT-Asia/Thimphu, GMT+02:00-CAT-Africa/Gaborone, GMT+03:00-FET-Europe/Minsk, GMT-06:00-CST-America/Belize, GMT-02:30-NDT-America/St_Johns, GMT-03:00-ADT-America/Halifax, GMT-03:00-ADT-America/Glace_Bay, GMT-03:00-ADT-America/Moncton, GMT-03:00-ADT-America/Goose_Bay, GMT-04:00-AST-America/Blanc-Sablon, GMT-04:00-EDT-America/Montreal, GMT-04:00-EDT-America/Toronto, GMT-04:00-EDT-America/Nipigon, GMT-04:00-EDT-America/Thunder_Bay, GMT-04:00-EDT-America/Iqaluit, GMT-04:00-EDT-America/Pangnirtung, GMT-05:00-CDT-America/Resolute, GMT-05:00-EST-America/Atikokan, GMT-05:00-CDT-America/Rankin_Inlet, GMT-05:00-CDT-America/Winnipeg, GMT-05:00-CDT-America/Rainy_River, GMT-06:00-CST-America/Regina, GMT-06:00-CST-America/Swift_Current, GMT-06:00-MDT-America/Edmonton, GMT-06:00-MDT-America/Cambridge_Bay, GMT-06:00-MDT-America/Yellowknife, GMT-06:00-MDT-America/Inuvik, GMT-07:00-MST-America/Dawson_Creek, GMT-07:00-PDT-America/Vancouver, GMT-07:00-PDT-America/Whitehorse, GMT-07:00-PDT-America/Dawson, GMT+06:30-CCT-Indian/Cocos, GMT+01:00-WAT-Africa/Kinshasa, GMT+02:00-CAT-Africa/Lubumbashi, GMT+01:00-WAT-Africa/Bangui, GMT+01:00-WAT-Africa/Brazzaville, GMT+01:00-CET-Europe/Zurich, GMT+00:00-GMT-Africa/Abidjan, GMT-10:00-CKT-Pacific/Rarotonga, GMT-04:00-CLT-America/Santiago, GMT-06:00-EAST-Pacific/Easter, GMT+01:00-WAT-Africa/Douala, GMT+08:00-CST-Asia/Shanghai, GMT+08:00-CST-Asia/Harbin, GMT+08:00-CST-Asia/Chongqing, GMT+08:00-CST-Asia/Urumqi, GMT+08:00-CST-Asia/Kashgar, GMT-05:00-COT-America/Bogota, GMT-06:00-CST-America/Costa_Rica, GMT-04:00-CDT-America/Havana, GMT-01:00-CVT-Atlantic/Cape_Verde, GMT+07:00-CXT-Indian/Christmas, GMT+02:00-EET-Asia/Nicosia, GMT+01:00-CET-Europe/Prague, GMT+01:00-CET-Europe/Berlin, GMT+03:00-EAT-Africa/Djibouti, GMT+01:00-CET-Europe/Copenhagen, GMT-04:00-AST-America/Dominica, GMT-04:00-AST-America/Santo_Domingo, GMT+01:00-CET-Africa/Algiers, GMT-05:00-ECT-America/Guayaquil, GMT-06:00-GALT-Pacific/Galapagos, GMT+02:00-EET-Europe/Tallinn, GMT+02:00-EET-Africa/Cairo, GMT+00:00-WET-Africa/El_Aaiun, GMT+03:00-EAT-Africa/Asmara, GMT+01:00-CET-Europe/Madrid, GMT+01:00-CET-Africa/Ceuta, GMT+00:00-WET-Atlantic/Canary, GMT+03:00-EAT-Africa/Addis_Ababa, GMT+02:00-EET-Europe/Helsinki, GMT+12:00-FJT-Pacific/Fiji, GMT-03:00-FKST-Atlantic/Stanley, GMT+10:00-CHUT-Pacific/Chuuk, GMT+11:00-PONT-Pacific/Pohnpei, GMT+11:00-KOST-Pacific/Kosrae, GMT+00:00-WET-Atlantic/Faroe, GMT+01:00-CET-Europe/Paris, GMT+01:00-WAT-Africa/Libreville, GMT+00:00-GMT-Europe/London, GMT-04:00-AST-America/Grenada, GMT+04:00-GET-Asia/Tbilisi, GMT-03:00-GFT-America/Cayenne, GMT+00:00-GMT-Europe/Guernsey, GMT+00:00-GMT-Africa/Accra, GMT+01:00-CET-Europe/Gibraltar, GMT-03:00-WGT-America/Godthab, GMT+00:00-GMT-America/Danmarkshavn, GMT-01:00-EGT-America/Scoresbysund, GMT-03:00-ADT-America/Thule, GMT+00:00-GMT-Africa/Banjul, GMT+00:00-GMT-Africa/Conakry, GMT-04:00-AST-America/Guadeloupe, GMT+01:00-WAT-Africa/Malabo, GMT+02:00-EET-Europe/Athens, GMT-02:00-GST-Atlantic/South_Georgia, GMT-06:00-CST-America/Guatemala, GMT+10:00-ChST-Pacific/Guam, GMT+00:00-GMT-Africa/Bissau, GMT-04:00-GYT-America/Guyana, GMT+08:00-HKT-Asia/Hong_Kong, GMT-06:00-CST-America/Tegucigalpa, GMT+01:00-CET-Europe/Zagreb, GMT-05:00-EST-America/Port-au-Prince, GMT+01:00-CET-Europe/Budapest, GMT+07:00-WIT-Asia/Jakarta, GMT+07:00-WIT-Asia/Pontianak, GMT+08:00-CIT-Asia/Makassar, GMT+09:00-EIT-Asia/Jayapura, GMT+00:00-GMT-Europe/Dublin, GMT+02:00-IST-Asia/Jerusalem, GMT+00:00-GMT-Europe/Isle_of_Man, GMT+05:30-IST-Asia/Kolkata, GMT+06:00-IOT-Indian/Chagos, GMT+03:00-AST-Asia/Baghdad, GMT+03:30-IRST-Asia/Tehran, GMT+00:00-GMT-Atlantic/Reykjavik, GMT+01:00-CET-Europe/Rome, GMT+00:00-GMT-Europe/Jersey, GMT-05:00-EST-America/Jamaica, GMT+02:00-EET-Asia/Amman, GMT+09:00-JST-Asia/Tokyo, GMT+03:00-EAT-Africa/Nairobi, GMT+06:00-KGT-Asia/Bishkek, GMT+07:00-ICT-Asia/Phnom_Penh, GMT+12:00-GILT-Pacific/Tarawa, GMT+13:00-PHOT-Pacific/Enderbury, GMT+14:00-LINT-Pacific/Kiritimati, GMT+03:00-EAT-Indian/Comoro, GMT-04:00-AST-America/St_Kitts, GMT+09:00-KST-Asia/Pyongyang, GMT+09:00-KST-Asia/Seoul, GMT+03:00-AST-Asia/Kuwait, GMT-05:00-EST-America/Cayman, GMT+06:00-ALMT-Asia/Almaty, GMT+06:00-QYZT-Asia/Qyzylorda, GMT+05:00-AQTT-Asia/Aqtobe, GMT+05:00-AQTT-Asia/Aqtau, GMT+05:00-ORAT-Asia/Oral, GMT+07:00-ICT-Asia/Vientiane, GMT+02:00-EET-Asia/Beirut, GMT-04:00-AST-America/St_Lucia, GMT+01:00-CET-Europe/Vaduz, GMT+05:30-IST-Asia/Colombo, GMT+00:00-GMT-Africa/Monrovia, GMT+02:00-SAST-Africa/Maseru, GMT+02:00-EET-Europe/Vilnius, GMT+01:00-CET-Europe/Luxembourg, GMT+02:00-EET-Europe/Riga, GMT+02:00-EET-Africa/Tripoli, GMT+00:00-WET-Africa/Casablanca, GMT+01:00-CET-Europe/Monaco, GMT+02:00-EET-Europe/Chisinau, GMT+01:00-CET-Europe/Podgorica, GMT-04:00-AST-America/Marigot, GMT+03:00-EAT-Indian/Antananarivo, GMT+12:00-MHT-Pacific/Majuro, GMT+12:00-MHT-Pacific/Kwajalein, GMT+01:00-CET-Europe/Skopje, GMT+00:00-GMT-Africa/Bamako, GMT+06:30-MMT-Asia/Rangoon, GMT+08:00-ULAT-Asia/Ulaanbaatar, GMT+07:00-HOVT-Asia/Hovd, GMT+08:00-CHOT-Asia/Choibalsan, GMT+08:00-CST-Asia/Macau, GMT+10:00-ChST-Pacific/Saipan, GMT-04:00-AST-America/Martinique, GMT+00:00-GMT-Africa/Nouakchott, GMT-04:00-AST-America/Montserrat, GMT+01:00-CET-Europe/Malta, GMT+04:00-MUT-Indian/Mauritius, GMT+05:00-MVT-Indian/Maldives, GMT+02:00-CAT-Africa/Blantyre, GMT-06:00-CST-America/Mexico_City, GMT-06:00-CST-America/Cancun, GMT-06:00-CST-America/Merida, GMT-06:00-CST-America/Monterrey, GMT-05:00-CDT-America/Matamoros, GMT-07:00-MST-America/Mazatlan, GMT-07:00-MST-America/Chihuahua, GMT-06:00-MDT-America/Ojinaga, GMT-07:00-MST-America/Hermosillo, GMT-07:00-PDT-America/Tijuana, GMT-08:00-PST-America/Santa_Isabel, GMT-06:00-CST-America/Bahia_Banderas, GMT+08:00-MYT-Asia/Kuala_Lumpur, GMT+08:00-MYT-Asia/Kuching, GMT+02:00-CAT-Africa/Maputo, GMT+02:00-WAST-Africa/Windhoek, GMT+11:00-NCT-Pacific/Noumea, GMT+01:00-WAT-Africa/Niamey, GMT+11:30-NFT-Pacific/Norfolk, GMT+01:00-WAT-Africa/Lagos, GMT-06:00-CST-America/Managua, GMT+01:00-CET-Europe/Amsterdam, GMT+01:00-CET-Europe/Oslo, GMT+05:45-NPT-Asia/Kathmandu, GMT+12:00-NRT-Pacific/Nauru, GMT-11:00-NUT-Pacific/Niue, GMT+13:00-NZDT-Pacific/Auckland, GMT+13:45-CHADT-Pacific/Chatham, GMT+04:00-GST-Asia/Muscat, GMT-05:00-EST-America/Panama, GMT-05:00-PET-America/Lima, GMT-10:00-TAHT-Pacific/Tahiti, GMT-09:30-MART-Pacific/Marquesas, GMT-09:00-GAMT-Pacific/Gambier, GMT+10:00-PGT-Pacific/Port_Moresby, GMT+08:00-PHT-Asia/Manila, GMT+05:00-PKT-Asia/Karachi, GMT+01:00-CET-Europe/Warsaw, GMT-02:00-PMDT-America/Miquelon, GMT-08:00-PST-Pacific/Pitcairn, GMT-04:00-AST-America/Puerto_Rico, GMT+02:00-EET-Asia/Gaza, GMT+02:00-EET-Asia/Hebron, GMT+00:00-WET-Europe/Lisbon, GMT+00:00-WET-Atlantic/Madeira, GMT-01:00-AZOT-Atlantic/Azores, GMT+09:00-PWT-Pacific/Palau, GMT-03:00-PYST-America/Asuncion, GMT+03:00-AST-Asia/Qatar, GMT+04:00-RET-Indian/Reunion, GMT+02:00-EET-Europe/Bucharest, GMT+01:00-CET-Europe/Belgrade, GMT+03:00-FET-Europe/Kaliningrad, GMT+04:00-MSK-Europe/Moscow, GMT+04:00-VOLT-Europe/Volgograd, GMT+04:00-SAMT-Europe/Samara, GMT+06:00-YEKT-Asia/Yekaterinburg, GMT+07:00-OMST-Asia/Omsk, GMT+07:00-NOVT-Asia/Novosibirsk, GMT+07:00-NOVT-Asia/Novokuznetsk, GMT+08:00-KRAT-Asia/Krasnoyarsk, GMT+09:00-IRKT-Asia/Irkutsk, GMT+10:00-YAKT-Asia/Yakutsk, GMT+11:00-VLAT-Asia/Vladivostok, GMT+11:00-SAKT-Asia/Sakhalin, GMT+12:00-MAGT-Asia/Magadan, GMT+12:00-PETT-Asia/Kamchatka, GMT+12:00-ANAT-Asia/Anadyr, GMT+02:00-CAT-Africa/Kigali, GMT+03:00-AST-Asia/Riyadh, GMT+11:00-SBT-Pacific/Guadalcanal, GMT+04:00-SCT-Indian/Mahe, GMT+03:00-EAT-Africa/Khartoum, GMT+01:00-CET-Europe/Stockholm, GMT+08:00-SGT-Asia/Singapore, GMT+00:00-GMT-Atlantic/St_Helena, GMT+01:00-CET-Europe/Ljubljana, GMT+01:00-CET-Arctic/Longyearbyen, GMT+01:00-CET-Europe/Bratislava, GMT+00:00-GMT-Africa/Freetown, GMT+01:00-CET-Europe/San_Marino, GMT+00:00-GMT-Africa/Dakar, GMT+03:00-EAT-Africa/Mogadishu, GMT-03:00-SRT-America/Paramaribo, GMT+00:00-GMT-Africa/Sao_Tome, GMT-06:00-CST-America/El_Salvador, GMT+02:00-EET-Asia/Damascus, GMT+02:00-SAST-Africa/Mbabane, GMT-04:00-EDT-America/Grand_Turk, GMT+01:00-WAT-Africa/Ndjamena, GMT+05:00-TFT-Indian/Kerguelen, GMT+00:00-GMT-Africa/Lome, GMT+07:00-ICT-Asia/Bangkok, GMT+05:00-TJT-Asia/Dushanbe, GMT-10:00-TKT-Pacific/Fakaofo, GMT+09:00-TLT-Asia/Dili, GMT+05:00-TMT-Asia/Ashgabat, GMT+01:00-CET-Africa/Tunis, GMT+13:00-TOT-Pacific/Tongatapu, GMT+02:00-EET-Europe/Istanbul, GMT-04:00-AST-America/Port_of_Spain, GMT+12:00-TVT-Pacific/Funafuti, GMT+08:00-CST-Asia/Taipei, GMT+03:00-EAT-Africa/Dar_es_Salaam, GMT+02:00-EET-Europe/Kiev, GMT+02:00-EET-Europe/Uzhgorod, GMT+02:00-EET-Europe/Zaporozhye, GMT+02:00-EET-Europe/Simferopol, GMT+03:00-EAT-Africa/Kampala, GMT-10:00-HST-Pacific/Johnston, GMT-11:00-SST-Pacific/Midway, GMT+12:00-WAKT-Pacific/Wake, GMT-04:00-EDT-America/New_York, GMT-04:00-EDT-America/Detroit, GMT-04:00-EDT-America/Kentucky/Louisville, GMT-04:00-EDT-America/Kentucky/Monticello, GMT-04:00-EDT-America/Indiana/Indianapolis, GMT-04:00-EDT-America/Indiana/Vincennes, GMT-04:00-EDT-America/Indiana/Winamac, GMT-04:00-EDT-America/Indiana/Marengo, GMT-04:00-EDT-America/Indiana/Petersburg, GMT-04:00-EDT-America/Indiana/Vevay, GMT-05:00-CDT-America/Chicago, GMT-05:00-CDT-America/Indiana/Tell_City, GMT-05:00-CDT-America/Indiana/Knox, GMT-05:00-CDT-America/Menominee, GMT-05:00-CDT-America/North_Dakota/Center, GMT-05:00-CDT-America/North_Dakota/New_Salem, GMT-05:00-CDT-America/North_Dakota/Beulah, GMT-06:00-MDT-America/Denver, GMT-06:00-MDT-America/Boise, GMT-06:00-MDT-America/Shiprock, GMT-07:00-MST-America/Phoenix, GMT-07:00-PDT-America/Los_Angeles, GMT-08:00-AKDT-America/Anchorage, GMT-08:00-AKDT-America/Juneau, GMT-08:00-AKDT-America/Sitka, GMT-08:00-AKDT-America/Yakutat, GMT-08:00-AKDT-America/Nome, GMT-09:00-HADT-America/Adak, GMT-08:00-MeST-America/Metlakatla, GMT-10:00-HST-Pacific/Honolulu, GMT-03:00-UYT-America/Montevideo, GMT+05:00-UZT-Asia/Samarkand, GMT+05:00-UZT-Asia/Tashkent, GMT+01:00-CET-Europe/Vatican, GMT-04:00-AST-America/St_Vincent, GMT-04:30-VET-America/Caracas, GMT-04:00-AST-America/Tortola, GMT-04:00-AST-America/St_Thomas, GMT+07:00-ICT-Asia/Ho_Chi_Minh, GMT+11:00-VUT-Pacific/Efate, GMT+12:00-WFT-Pacific/Wallis, GMT+14:00-WSDT-Pacific/Apia, GMT+03:00-AST-Asia/Aden, GMT+03:00-EAT-Indian/Mayotte, GMT+02:00-SAST-Africa/Johannesburg, GMT+02:00-CAT-Africa/Lusaka, GMT+02:00-CAT-Africa/Harare.
		"""
		try :
			return self._timezone
		except Exception as e:
			raise e

	@timezone.setter
	def timezone(self, timezone) :
		ur"""Name of the timezone.<br/>Possible values = CoordinatedUniversalTime, GMT+01:00-CET-Europe/Andorra, GMT+04:00-GST-Asia/Dubai, GMT+04:30-AFT-Asia/Kabul, GMT-04:00-AST-America/Antigua, GMT-04:00-AST-America/Anguilla, GMT+01:00-CET-Europe/Tirane, GMT+04:00-AMT-Asia/Yerevan, GMT+01:00-WAT-Africa/Luanda, GMT+13:00-NZDT-Antarctica/McMurdo, GMT+13:00-NZDT-Antarctica/South_Pole, GMT-03:00-ROTT-Antarctica/Rothera, GMT-04:00-CLT-Antarctica/Palmer, GMT+05:00-MAWT-Antarctica/Mawson, GMT+07:00-DAVT-Antarctica/Davis, GMT+08:00-WST-Antarctica/Casey, GMT+06:00-VOST-Antarctica/Vostok, GMT+10:00-DDUT-Antarctica/DumontDUrville, GMT+03:00-SYOT-Antarctica/Syowa, GMT+11:00-MIST-Antarctica/Macquarie, GMT-03:00-ART-America/Argentina/Buenos_Aires, GMT-03:00-ART-America/Argentina/Cordoba, GMT-03:00-ART-America/Argentina/Salta, GMT-03:00-ART-America/Argentina/Jujuy, GMT-03:00-ART-America/Argentina/Tucuman, GMT-03:00-ART-America/Argentina/Catamarca, GMT-03:00-ART-America/Argentina/La_Rioja, GMT-03:00-ART-America/Argentina/San_Juan, GMT-03:00-ART-America/Argentina/Mendoza, GMT-03:00-WARST-America/Argentina/San_Luis, GMT-03:00-ART-America/Argentina/Rio_Gallegos, GMT-03:00-ART-America/Argentina/Ushuaia, GMT-11:00-SST-Pacific/Pago_Pago, GMT+01:00-CET-Europe/Vienna, GMT+11:00-LHST-Australia/Lord_Howe, GMT+11:00-EST-Australia/Hobart, GMT+11:00-EST-Australia/Currie, GMT+11:00-EST-Australia/Melbourne, GMT+11:00-EST-Australia/Sydney, GMT+10:30-CST-Australia/Broken_Hill, GMT+10:00-EST-Australia/Brisbane, GMT+10:00-EST-Australia/Lindeman, GMT+10:30-CST-Australia/Adelaide, GMT+09:30-CST-Australia/Darwin, GMT+08:00-WST-Australia/Perth, GMT+08:45-CWST-Australia/Eucla, GMT-04:00-AST-America/Aruba, GMT+02:00-EET-Europe/Mariehamn, GMT+04:00-AZT-Asia/Baku, GMT+01:00-CET-Europe/Sarajevo, GMT-04:00-AST-America/Barbados, GMT+06:00-BDT-Asia/Dhaka, GMT+01:00-CET-Europe/Brussels, GMT+00:00-GMT-Africa/Ouagadougou, GMT+02:00-EET-Europe/Sofia, GMT+03:00-AST-Asia/Bahrain, GMT+02:00-CAT-Africa/Bujumbura, GMT+01:00-WAT-Africa/Porto-Novo, GMT-04:00-AST-America/St_Barthelemy, GMT-03:00-ADT-Atlantic/Bermuda, GMT+08:00-BNT-Asia/Brunei, GMT-04:00-BOT-America/La_Paz, GMT-02:00-FNT-America/Noronha, GMT-03:00-BRT-America/Belem, GMT-03:00-BRT-America/Fortaleza, GMT-03:00-BRT-America/Recife, GMT-03:00-BRT-America/Araguaina, GMT-03:00-BRT-America/Maceio, GMT-03:00-BRT-America/Bahia, GMT-03:00-BRT-America/Sao_Paulo, GMT-04:00-AMT-America/Campo_Grande, GMT-04:00-AMT-America/Cuiaba, GMT-03:00-BRT-America/Santarem, GMT-04:00-AMT-America/Porto_Velho, GMT-04:00-AMT-America/Boa_Vista, GMT-04:00-AMT-America/Manaus, GMT-04:00-AMT-America/Eirunepe, GMT-04:00-AMT-America/Rio_Branco, GMT-04:00-EDT-America/Nassau, GMT+06:00-BTT-Asia/Thimphu, GMT+02:00-CAT-Africa/Gaborone, GMT+03:00-FET-Europe/Minsk, GMT-06:00-CST-America/Belize, GMT-02:30-NDT-America/St_Johns, GMT-03:00-ADT-America/Halifax, GMT-03:00-ADT-America/Glace_Bay, GMT-03:00-ADT-America/Moncton, GMT-03:00-ADT-America/Goose_Bay, GMT-04:00-AST-America/Blanc-Sablon, GMT-04:00-EDT-America/Montreal, GMT-04:00-EDT-America/Toronto, GMT-04:00-EDT-America/Nipigon, GMT-04:00-EDT-America/Thunder_Bay, GMT-04:00-EDT-America/Iqaluit, GMT-04:00-EDT-America/Pangnirtung, GMT-05:00-CDT-America/Resolute, GMT-05:00-EST-America/Atikokan, GMT-05:00-CDT-America/Rankin_Inlet, GMT-05:00-CDT-America/Winnipeg, GMT-05:00-CDT-America/Rainy_River, GMT-06:00-CST-America/Regina, GMT-06:00-CST-America/Swift_Current, GMT-06:00-MDT-America/Edmonton, GMT-06:00-MDT-America/Cambridge_Bay, GMT-06:00-MDT-America/Yellowknife, GMT-06:00-MDT-America/Inuvik, GMT-07:00-MST-America/Dawson_Creek, GMT-07:00-PDT-America/Vancouver, GMT-07:00-PDT-America/Whitehorse, GMT-07:00-PDT-America/Dawson, GMT+06:30-CCT-Indian/Cocos, GMT+01:00-WAT-Africa/Kinshasa, GMT+02:00-CAT-Africa/Lubumbashi, GMT+01:00-WAT-Africa/Bangui, GMT+01:00-WAT-Africa/Brazzaville, GMT+01:00-CET-Europe/Zurich, GMT+00:00-GMT-Africa/Abidjan, GMT-10:00-CKT-Pacific/Rarotonga, GMT-04:00-CLT-America/Santiago, GMT-06:00-EAST-Pacific/Easter, GMT+01:00-WAT-Africa/Douala, GMT+08:00-CST-Asia/Shanghai, GMT+08:00-CST-Asia/Harbin, GMT+08:00-CST-Asia/Chongqing, GMT+08:00-CST-Asia/Urumqi, GMT+08:00-CST-Asia/Kashgar, GMT-05:00-COT-America/Bogota, GMT-06:00-CST-America/Costa_Rica, GMT-04:00-CDT-America/Havana, GMT-01:00-CVT-Atlantic/Cape_Verde, GMT+07:00-CXT-Indian/Christmas, GMT+02:00-EET-Asia/Nicosia, GMT+01:00-CET-Europe/Prague, GMT+01:00-CET-Europe/Berlin, GMT+03:00-EAT-Africa/Djibouti, GMT+01:00-CET-Europe/Copenhagen, GMT-04:00-AST-America/Dominica, GMT-04:00-AST-America/Santo_Domingo, GMT+01:00-CET-Africa/Algiers, GMT-05:00-ECT-America/Guayaquil, GMT-06:00-GALT-Pacific/Galapagos, GMT+02:00-EET-Europe/Tallinn, GMT+02:00-EET-Africa/Cairo, GMT+00:00-WET-Africa/El_Aaiun, GMT+03:00-EAT-Africa/Asmara, GMT+01:00-CET-Europe/Madrid, GMT+01:00-CET-Africa/Ceuta, GMT+00:00-WET-Atlantic/Canary, GMT+03:00-EAT-Africa/Addis_Ababa, GMT+02:00-EET-Europe/Helsinki, GMT+12:00-FJT-Pacific/Fiji, GMT-03:00-FKST-Atlantic/Stanley, GMT+10:00-CHUT-Pacific/Chuuk, GMT+11:00-PONT-Pacific/Pohnpei, GMT+11:00-KOST-Pacific/Kosrae, GMT+00:00-WET-Atlantic/Faroe, GMT+01:00-CET-Europe/Paris, GMT+01:00-WAT-Africa/Libreville, GMT+00:00-GMT-Europe/London, GMT-04:00-AST-America/Grenada, GMT+04:00-GET-Asia/Tbilisi, GMT-03:00-GFT-America/Cayenne, GMT+00:00-GMT-Europe/Guernsey, GMT+00:00-GMT-Africa/Accra, GMT+01:00-CET-Europe/Gibraltar, GMT-03:00-WGT-America/Godthab, GMT+00:00-GMT-America/Danmarkshavn, GMT-01:00-EGT-America/Scoresbysund, GMT-03:00-ADT-America/Thule, GMT+00:00-GMT-Africa/Banjul, GMT+00:00-GMT-Africa/Conakry, GMT-04:00-AST-America/Guadeloupe, GMT+01:00-WAT-Africa/Malabo, GMT+02:00-EET-Europe/Athens, GMT-02:00-GST-Atlantic/South_Georgia, GMT-06:00-CST-America/Guatemala, GMT+10:00-ChST-Pacific/Guam, GMT+00:00-GMT-Africa/Bissau, GMT-04:00-GYT-America/Guyana, GMT+08:00-HKT-Asia/Hong_Kong, GMT-06:00-CST-America/Tegucigalpa, GMT+01:00-CET-Europe/Zagreb, GMT-05:00-EST-America/Port-au-Prince, GMT+01:00-CET-Europe/Budapest, GMT+07:00-WIT-Asia/Jakarta, GMT+07:00-WIT-Asia/Pontianak, GMT+08:00-CIT-Asia/Makassar, GMT+09:00-EIT-Asia/Jayapura, GMT+00:00-GMT-Europe/Dublin, GMT+02:00-IST-Asia/Jerusalem, GMT+00:00-GMT-Europe/Isle_of_Man, GMT+05:30-IST-Asia/Kolkata, GMT+06:00-IOT-Indian/Chagos, GMT+03:00-AST-Asia/Baghdad, GMT+03:30-IRST-Asia/Tehran, GMT+00:00-GMT-Atlantic/Reykjavik, GMT+01:00-CET-Europe/Rome, GMT+00:00-GMT-Europe/Jersey, GMT-05:00-EST-America/Jamaica, GMT+02:00-EET-Asia/Amman, GMT+09:00-JST-Asia/Tokyo, GMT+03:00-EAT-Africa/Nairobi, GMT+06:00-KGT-Asia/Bishkek, GMT+07:00-ICT-Asia/Phnom_Penh, GMT+12:00-GILT-Pacific/Tarawa, GMT+13:00-PHOT-Pacific/Enderbury, GMT+14:00-LINT-Pacific/Kiritimati, GMT+03:00-EAT-Indian/Comoro, GMT-04:00-AST-America/St_Kitts, GMT+09:00-KST-Asia/Pyongyang, GMT+09:00-KST-Asia/Seoul, GMT+03:00-AST-Asia/Kuwait, GMT-05:00-EST-America/Cayman, GMT+06:00-ALMT-Asia/Almaty, GMT+06:00-QYZT-Asia/Qyzylorda, GMT+05:00-AQTT-Asia/Aqtobe, GMT+05:00-AQTT-Asia/Aqtau, GMT+05:00-ORAT-Asia/Oral, GMT+07:00-ICT-Asia/Vientiane, GMT+02:00-EET-Asia/Beirut, GMT-04:00-AST-America/St_Lucia, GMT+01:00-CET-Europe/Vaduz, GMT+05:30-IST-Asia/Colombo, GMT+00:00-GMT-Africa/Monrovia, GMT+02:00-SAST-Africa/Maseru, GMT+02:00-EET-Europe/Vilnius, GMT+01:00-CET-Europe/Luxembourg, GMT+02:00-EET-Europe/Riga, GMT+02:00-EET-Africa/Tripoli, GMT+00:00-WET-Africa/Casablanca, GMT+01:00-CET-Europe/Monaco, GMT+02:00-EET-Europe/Chisinau, GMT+01:00-CET-Europe/Podgorica, GMT-04:00-AST-America/Marigot, GMT+03:00-EAT-Indian/Antananarivo, GMT+12:00-MHT-Pacific/Majuro, GMT+12:00-MHT-Pacific/Kwajalein, GMT+01:00-CET-Europe/Skopje, GMT+00:00-GMT-Africa/Bamako, GMT+06:30-MMT-Asia/Rangoon, GMT+08:00-ULAT-Asia/Ulaanbaatar, GMT+07:00-HOVT-Asia/Hovd, GMT+08:00-CHOT-Asia/Choibalsan, GMT+08:00-CST-Asia/Macau, GMT+10:00-ChST-Pacific/Saipan, GMT-04:00-AST-America/Martinique, GMT+00:00-GMT-Africa/Nouakchott, GMT-04:00-AST-America/Montserrat, GMT+01:00-CET-Europe/Malta, GMT+04:00-MUT-Indian/Mauritius, GMT+05:00-MVT-Indian/Maldives, GMT+02:00-CAT-Africa/Blantyre, GMT-06:00-CST-America/Mexico_City, GMT-06:00-CST-America/Cancun, GMT-06:00-CST-America/Merida, GMT-06:00-CST-America/Monterrey, GMT-05:00-CDT-America/Matamoros, GMT-07:00-MST-America/Mazatlan, GMT-07:00-MST-America/Chihuahua, GMT-06:00-MDT-America/Ojinaga, GMT-07:00-MST-America/Hermosillo, GMT-07:00-PDT-America/Tijuana, GMT-08:00-PST-America/Santa_Isabel, GMT-06:00-CST-America/Bahia_Banderas, GMT+08:00-MYT-Asia/Kuala_Lumpur, GMT+08:00-MYT-Asia/Kuching, GMT+02:00-CAT-Africa/Maputo, GMT+02:00-WAST-Africa/Windhoek, GMT+11:00-NCT-Pacific/Noumea, GMT+01:00-WAT-Africa/Niamey, GMT+11:30-NFT-Pacific/Norfolk, GMT+01:00-WAT-Africa/Lagos, GMT-06:00-CST-America/Managua, GMT+01:00-CET-Europe/Amsterdam, GMT+01:00-CET-Europe/Oslo, GMT+05:45-NPT-Asia/Kathmandu, GMT+12:00-NRT-Pacific/Nauru, GMT-11:00-NUT-Pacific/Niue, GMT+13:00-NZDT-Pacific/Auckland, GMT+13:45-CHADT-Pacific/Chatham, GMT+04:00-GST-Asia/Muscat, GMT-05:00-EST-America/Panama, GMT-05:00-PET-America/Lima, GMT-10:00-TAHT-Pacific/Tahiti, GMT-09:30-MART-Pacific/Marquesas, GMT-09:00-GAMT-Pacific/Gambier, GMT+10:00-PGT-Pacific/Port_Moresby, GMT+08:00-PHT-Asia/Manila, GMT+05:00-PKT-Asia/Karachi, GMT+01:00-CET-Europe/Warsaw, GMT-02:00-PMDT-America/Miquelon, GMT-08:00-PST-Pacific/Pitcairn, GMT-04:00-AST-America/Puerto_Rico, GMT+02:00-EET-Asia/Gaza, GMT+02:00-EET-Asia/Hebron, GMT+00:00-WET-Europe/Lisbon, GMT+00:00-WET-Atlantic/Madeira, GMT-01:00-AZOT-Atlantic/Azores, GMT+09:00-PWT-Pacific/Palau, GMT-03:00-PYST-America/Asuncion, GMT+03:00-AST-Asia/Qatar, GMT+04:00-RET-Indian/Reunion, GMT+02:00-EET-Europe/Bucharest, GMT+01:00-CET-Europe/Belgrade, GMT+03:00-FET-Europe/Kaliningrad, GMT+04:00-MSK-Europe/Moscow, GMT+04:00-VOLT-Europe/Volgograd, GMT+04:00-SAMT-Europe/Samara, GMT+06:00-YEKT-Asia/Yekaterinburg, GMT+07:00-OMST-Asia/Omsk, GMT+07:00-NOVT-Asia/Novosibirsk, GMT+07:00-NOVT-Asia/Novokuznetsk, GMT+08:00-KRAT-Asia/Krasnoyarsk, GMT+09:00-IRKT-Asia/Irkutsk, GMT+10:00-YAKT-Asia/Yakutsk, GMT+11:00-VLAT-Asia/Vladivostok, GMT+11:00-SAKT-Asia/Sakhalin, GMT+12:00-MAGT-Asia/Magadan, GMT+12:00-PETT-Asia/Kamchatka, GMT+12:00-ANAT-Asia/Anadyr, GMT+02:00-CAT-Africa/Kigali, GMT+03:00-AST-Asia/Riyadh, GMT+11:00-SBT-Pacific/Guadalcanal, GMT+04:00-SCT-Indian/Mahe, GMT+03:00-EAT-Africa/Khartoum, GMT+01:00-CET-Europe/Stockholm, GMT+08:00-SGT-Asia/Singapore, GMT+00:00-GMT-Atlantic/St_Helena, GMT+01:00-CET-Europe/Ljubljana, GMT+01:00-CET-Arctic/Longyearbyen, GMT+01:00-CET-Europe/Bratislava, GMT+00:00-GMT-Africa/Freetown, GMT+01:00-CET-Europe/San_Marino, GMT+00:00-GMT-Africa/Dakar, GMT+03:00-EAT-Africa/Mogadishu, GMT-03:00-SRT-America/Paramaribo, GMT+00:00-GMT-Africa/Sao_Tome, GMT-06:00-CST-America/El_Salvador, GMT+02:00-EET-Asia/Damascus, GMT+02:00-SAST-Africa/Mbabane, GMT-04:00-EDT-America/Grand_Turk, GMT+01:00-WAT-Africa/Ndjamena, GMT+05:00-TFT-Indian/Kerguelen, GMT+00:00-GMT-Africa/Lome, GMT+07:00-ICT-Asia/Bangkok, GMT+05:00-TJT-Asia/Dushanbe, GMT-10:00-TKT-Pacific/Fakaofo, GMT+09:00-TLT-Asia/Dili, GMT+05:00-TMT-Asia/Ashgabat, GMT+01:00-CET-Africa/Tunis, GMT+13:00-TOT-Pacific/Tongatapu, GMT+02:00-EET-Europe/Istanbul, GMT-04:00-AST-America/Port_of_Spain, GMT+12:00-TVT-Pacific/Funafuti, GMT+08:00-CST-Asia/Taipei, GMT+03:00-EAT-Africa/Dar_es_Salaam, GMT+02:00-EET-Europe/Kiev, GMT+02:00-EET-Europe/Uzhgorod, GMT+02:00-EET-Europe/Zaporozhye, GMT+02:00-EET-Europe/Simferopol, GMT+03:00-EAT-Africa/Kampala, GMT-10:00-HST-Pacific/Johnston, GMT-11:00-SST-Pacific/Midway, GMT+12:00-WAKT-Pacific/Wake, GMT-04:00-EDT-America/New_York, GMT-04:00-EDT-America/Detroit, GMT-04:00-EDT-America/Kentucky/Louisville, GMT-04:00-EDT-America/Kentucky/Monticello, GMT-04:00-EDT-America/Indiana/Indianapolis, GMT-04:00-EDT-America/Indiana/Vincennes, GMT-04:00-EDT-America/Indiana/Winamac, GMT-04:00-EDT-America/Indiana/Marengo, GMT-04:00-EDT-America/Indiana/Petersburg, GMT-04:00-EDT-America/Indiana/Vevay, GMT-05:00-CDT-America/Chicago, GMT-05:00-CDT-America/Indiana/Tell_City, GMT-05:00-CDT-America/Indiana/Knox, GMT-05:00-CDT-America/Menominee, GMT-05:00-CDT-America/North_Dakota/Center, GMT-05:00-CDT-America/North_Dakota/New_Salem, GMT-05:00-CDT-America/North_Dakota/Beulah, GMT-06:00-MDT-America/Denver, GMT-06:00-MDT-America/Boise, GMT-06:00-MDT-America/Shiprock, GMT-07:00-MST-America/Phoenix, GMT-07:00-PDT-America/Los_Angeles, GMT-08:00-AKDT-America/Anchorage, GMT-08:00-AKDT-America/Juneau, GMT-08:00-AKDT-America/Sitka, GMT-08:00-AKDT-America/Yakutat, GMT-08:00-AKDT-America/Nome, GMT-09:00-HADT-America/Adak, GMT-08:00-MeST-America/Metlakatla, GMT-10:00-HST-Pacific/Honolulu, GMT-03:00-UYT-America/Montevideo, GMT+05:00-UZT-Asia/Samarkand, GMT+05:00-UZT-Asia/Tashkent, GMT+01:00-CET-Europe/Vatican, GMT-04:00-AST-America/St_Vincent, GMT-04:30-VET-America/Caracas, GMT-04:00-AST-America/Tortola, GMT-04:00-AST-America/St_Thomas, GMT+07:00-ICT-Asia/Ho_Chi_Minh, GMT+11:00-VUT-Pacific/Efate, GMT+12:00-WFT-Pacific/Wallis, GMT+14:00-WSDT-Pacific/Apia, GMT+03:00-AST-Asia/Aden, GMT+03:00-EAT-Indian/Mayotte, GMT+02:00-SAST-Africa/Johannesburg, GMT+02:00-CAT-Africa/Lusaka, GMT+02:00-CAT-Africa/Harare
		"""
		try :
			self._timezone = timezone
		except Exception as e:
			raise e

	@property
	def grantquotamaxclient(self) :
		ur"""The percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotamaxclient
		except Exception as e:
			raise e

	@grantquotamaxclient.setter
	def grantquotamaxclient(self, grantquotamaxclient) :
		ur"""The percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotamaxclient = grantquotamaxclient
		except Exception as e:
			raise e

	@property
	def exclusivequotamaxclient(self) :
		ur"""The percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotamaxclient
		except Exception as e:
			raise e

	@exclusivequotamaxclient.setter
	def exclusivequotamaxclient(self, exclusivequotamaxclient) :
		ur"""The percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotamaxclient = exclusivequotamaxclient
		except Exception as e:
			raise e

	@property
	def grantquotaspillover(self) :
		ur"""The percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotaspillover
		except Exception as e:
			raise e

	@grantquotaspillover.setter
	def grantquotaspillover(self, grantquotaspillover) :
		ur"""The percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotaspillover = grantquotaspillover
		except Exception as e:
			raise e

	@property
	def exclusivequotaspillover(self) :
		ur"""The percentage of max limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotaspillover
		except Exception as e:
			raise e

	@exclusivequotaspillover.setter
	def exclusivequotaspillover(self, exclusivequotaspillover) :
		ur"""The percentage of max limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotaspillover = exclusivequotaspillover
		except Exception as e:
			raise e

	@property
	def nwfwmode(self) :
		ur"""Network Firewall mode to be used.
		NOFIREWALL   - No Network firewall setting
		BASIC 	     - DENY-ALL behavior and DENY-ALL AT BOOTUP
		EXTENDED     - NS_NWFWMODE_BASIC + drop IP fragments + TCP and ACL logging + packet drop on closed port
		EXTENDEDPLUS - NS_NWFWMODE_EXTENDED + block traffic on 3008-3011 + drop non-session packets
		FULL         - NS_NWFWMODE_EXTENDEDPLUS + drop  non-ip packets.<br/>Default value: NOFIREWALL<br/>Possible values = NOFIREWALL, BASIC, EXTENDED, EXTENDEDPLUS, FULL.
		"""
		try :
			return self._nwfwmode
		except Exception as e:
			raise e

	@nwfwmode.setter
	def nwfwmode(self, nwfwmode) :
		ur"""Network Firewall mode to be used.
		NOFIREWALL   - No Network firewall setting
		BASIC 	     - DENY-ALL behavior and DENY-ALL AT BOOTUP
		EXTENDED     - NS_NWFWMODE_BASIC + drop IP fragments + TCP and ACL logging + packet drop on closed port
		EXTENDEDPLUS - NS_NWFWMODE_EXTENDED + block traffic on 3008-3011 + drop non-session packets
		FULL         - NS_NWFWMODE_EXTENDEDPLUS + drop  non-ip packets.<br/>Default value: NOFIREWALL<br/>Possible values = NOFIREWALL, BASIC, EXTENDED, EXTENDEDPLUS, FULL
		"""
		try :
			self._nwfwmode = nwfwmode
		except Exception as e:
			raise e

	@property
	def config1(self) :
		ur"""Location of the configurations.
		"""
		try :
			return self._config1
		except Exception as e:
			raise e

	@config1.setter
	def config1(self, config1) :
		ur"""Location of the configurations.
		"""
		try :
			self._config1 = config1
		except Exception as e:
			raise e

	@property
	def config2(self) :
		ur"""Location of the configurations.
		"""
		try :
			return self._config2
		except Exception as e:
			raise e

	@config2.setter
	def config2(self, config2) :
		ur"""Location of the configurations.
		"""
		try :
			self._config2 = config2
		except Exception as e:
			raise e

	@property
	def outtype(self) :
		ur"""Format to display the difference in configurations.<br/>Possible values = cli, xml.
		"""
		try :
			return self._outtype
		except Exception as e:
			raise e

	@outtype.setter
	def outtype(self, outtype) :
		ur"""Format to display the difference in configurations.<br/>Possible values = cli, xml
		"""
		try :
			self._outtype = outtype
		except Exception as e:
			raise e

	@property
	def template(self) :
		ur"""File that contains the commands to be compared.
		"""
		try :
			return self._template
		except Exception as e:
			raise e

	@template.setter
	def template(self, template) :
		ur"""File that contains the commands to be compared.
		"""
		try :
			self._template = template
		except Exception as e:
			raise e

	@property
	def ignoredevicespecific(self) :
		ur"""Suppress device specific differences.
		"""
		try :
			return self._ignoredevicespecific
		except Exception as e:
			raise e

	@ignoredevicespecific.setter
	def ignoredevicespecific(self, ignoredevicespecific) :
		ur"""Suppress device specific differences.
		"""
		try :
			self._ignoredevicespecific = ignoredevicespecific
		except Exception as e:
			raise e

	@property
	def message(self) :
		try :
			return self._message
		except Exception as e:
			raise e

	@property
	def mappedip(self) :
		ur"""Mapped IP Address of the System.<br/>Minimum length =  1.
		"""
		try :
			return self._mappedip
		except Exception as e:
			raise e

	@property
	def range(self) :
		ur"""The range of Mapped IP addresses to be configured.<br/>Minimum value =  1.
		"""
		try :
			return self._range
		except Exception as e:
			raise e

	@property
	def systemtype(self) :
		ur"""The type of the System. Possible Values: Standalone, HA, Cluster.<br/>Possible values = Stand-alone, HA, Cluster.
		"""
		try :
			return self._systemtype
		except Exception as e:
			raise e

	@property
	def primaryip(self) :
		ur"""HA Master Node IP address.
		"""
		try :
			return self._primaryip
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""The flags for this entry.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def lastconfigchangedtime(self) :
		ur"""Time when the configuration was last modified.
		"""
		try :
			return self._lastconfigchangedtime
		except Exception as e:
			raise e

	@property
	def lastconfigsavetime(self) :
		ur"""Time when the configuration was last saved through savensconfig.
		"""
		try :
			return self._lastconfigsavetime
		except Exception as e:
			raise e

	@property
	def currentsytemtime(self) :
		ur"""current system time in date format.
		"""
		try :
			return self._currentsytemtime
		except Exception as e:
			raise e

	@property
	def systemtime(self) :
		ur"""current system time.
		"""
		try :
			return self._systemtime
		except Exception as e:
			raise e

	@property
	def response(self) :
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsconfig_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsconfig
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
	def clear(cls, client, resource) :
		ur""" Use this API to clear nsconfig.
		"""
		try :
			if type(resource) is not list :
				clearresource = nsconfig()
				clearresource.force = resource.force
				clearresource.level = resource.level
				return clearresource.perform_operation(client,"clear")
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nsconfig.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsconfig()
				updateresource.ipaddress = resource.ipaddress
				updateresource.netmask = resource.netmask
				updateresource.nsvlan = resource.nsvlan
				updateresource.ifnum = resource.ifnum
				updateresource.tagged = resource.tagged
				updateresource.httpport = resource.httpport
				updateresource.maxconn = resource.maxconn
				updateresource.maxreq = resource.maxreq
				updateresource.cip = resource.cip
				updateresource.cipheader = resource.cipheader
				updateresource.cookieversion = resource.cookieversion
				updateresource.securecookie = resource.securecookie
				updateresource.pmtumin = resource.pmtumin
				updateresource.pmtutimeout = resource.pmtutimeout
				updateresource.ftpportrange = resource.ftpportrange
				updateresource.crportrange = resource.crportrange
				updateresource.timezone = resource.timezone
				updateresource.grantquotamaxclient = resource.grantquotamaxclient
				updateresource.exclusivequotamaxclient = resource.exclusivequotamaxclient
				updateresource.grantquotaspillover = resource.grantquotaspillover
				updateresource.exclusivequotaspillover = resource.exclusivequotaspillover
				updateresource.nwfwmode = resource.nwfwmode
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nsconfig resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsconfig()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def save(cls, client, resource="") :
		ur""" Use this API to save nsconfig.
		"""
		try :
			if type(resource) is not list :
				saveresource = nsconfig()
				return saveresource.perform_operation(client,"save")
		except Exception as e :
			raise e

	@classmethod
	def diff(cls, client, resource) :
		ur""" Use this API to diff nsconfig.
		"""
		try :
			if type(resource) is not list :
				diffresource = nsconfig()
				diffresource.config1 = resource.config1
				diffresource.config2 = resource.config2
				diffresource.outtype = resource.outtype
				diffresource.template = resource.template
				diffresource.ignoredevicespecific = resource.ignoredevicespecific
				return diffresource.perform_operation(client,"diff")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsconfig resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsconfig()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Nwfwmode:
		NOFIREWALL = "NOFIREWALL"
		BASIC = "BASIC"
		EXTENDED = "EXTENDED"
		EXTENDEDPLUS = "EXTENDEDPLUS"
		FULL = "FULL"

	class Outtype:
		cli = "cli"
		xml = "xml"

	class Timezone:
		CoordinatedUniversalTime = "CoordinatedUniversalTime"
		GMT_01_00_CET_Europe_Andorra = "GMT+01:00-CET-Europe/Andorra"
		GMT_04_00_GST_Asia_Dubai = "GMT+04:00-GST-Asia/Dubai"
		GMT_04_30_AFT_Asia_Kabul = "GMT+04:30-AFT-Asia/Kabul"
		GMT_04_00_AST_America_Antigua = "GMT-04:00-AST-America/Antigua"
		GMT_04_00_AST_America_Anguilla = "GMT-04:00-AST-America/Anguilla"
		GMT_01_00_CET_Europe_Tirane = "GMT+01:00-CET-Europe/Tirane"
		GMT_04_00_AMT_Asia_Yerevan = "GMT+04:00-AMT-Asia/Yerevan"
		GMT_01_00_WAT_Africa_Luanda = "GMT+01:00-WAT-Africa/Luanda"
		GMT_13_00_NZDT_Antarctica_McMurdo = "GMT+13:00-NZDT-Antarctica/McMurdo"
		GMT_13_00_NZDT_Antarctica_South_Pole = "GMT+13:00-NZDT-Antarctica/South_Pole"
		GMT_03_00_ROTT_Antarctica_Rothera = "GMT-03:00-ROTT-Antarctica/Rothera"
		GMT_04_00_CLT_Antarctica_Palmer = "GMT-04:00-CLT-Antarctica/Palmer"
		GMT_05_00_MAWT_Antarctica_Mawson = "GMT+05:00-MAWT-Antarctica/Mawson"
		GMT_07_00_DAVT_Antarctica_Davis = "GMT+07:00-DAVT-Antarctica/Davis"
		GMT_08_00_WST_Antarctica_Casey = "GMT+08:00-WST-Antarctica/Casey"
		GMT_06_00_VOST_Antarctica_Vostok = "GMT+06:00-VOST-Antarctica/Vostok"
		GMT_10_00_DDUT_Antarctica_DumontDUrville = "GMT+10:00-DDUT-Antarctica/DumontDUrville"
		GMT_03_00_SYOT_Antarctica_Syowa = "GMT+03:00-SYOT-Antarctica/Syowa"
		GMT_11_00_MIST_Antarctica_Macquarie = "GMT+11:00-MIST-Antarctica/Macquarie"
		GMT_03_00_ART_America_Argentina_Buenos_Aires = "GMT-03:00-ART-America/Argentina/Buenos_Aires"
		GMT_03_00_ART_America_Argentina_Cordoba = "GMT-03:00-ART-America/Argentina/Cordoba"
		GMT_03_00_ART_America_Argentina_Salta = "GMT-03:00-ART-America/Argentina/Salta"
		GMT_03_00_ART_America_Argentina_Jujuy = "GMT-03:00-ART-America/Argentina/Jujuy"
		GMT_03_00_ART_America_Argentina_Tucuman = "GMT-03:00-ART-America/Argentina/Tucuman"
		GMT_03_00_ART_America_Argentina_Catamarca = "GMT-03:00-ART-America/Argentina/Catamarca"
		GMT_03_00_ART_America_Argentina_La_Rioja = "GMT-03:00-ART-America/Argentina/La_Rioja"
		GMT_03_00_ART_America_Argentina_San_Juan = "GMT-03:00-ART-America/Argentina/San_Juan"
		GMT_03_00_ART_America_Argentina_Mendoza = "GMT-03:00-ART-America/Argentina/Mendoza"
		GMT_03_00_WARST_America_Argentina_San_Luis = "GMT-03:00-WARST-America/Argentina/San_Luis"
		GMT_03_00_ART_America_Argentina_Rio_Gallegos = "GMT-03:00-ART-America/Argentina/Rio_Gallegos"
		GMT_03_00_ART_America_Argentina_Ushuaia = "GMT-03:00-ART-America/Argentina/Ushuaia"
		GMT_11_00_SST_Pacific_Pago_Pago = "GMT-11:00-SST-Pacific/Pago_Pago"
		GMT_01_00_CET_Europe_Vienna = "GMT+01:00-CET-Europe/Vienna"
		GMT_11_00_LHST_Australia_Lord_Howe = "GMT+11:00-LHST-Australia/Lord_Howe"
		GMT_11_00_EST_Australia_Hobart = "GMT+11:00-EST-Australia/Hobart"
		GMT_11_00_EST_Australia_Currie = "GMT+11:00-EST-Australia/Currie"
		GMT_11_00_EST_Australia_Melbourne = "GMT+11:00-EST-Australia/Melbourne"
		GMT_11_00_EST_Australia_Sydney = "GMT+11:00-EST-Australia/Sydney"
		GMT_10_30_CST_Australia_Broken_Hill = "GMT+10:30-CST-Australia/Broken_Hill"
		GMT_10_00_EST_Australia_Brisbane = "GMT+10:00-EST-Australia/Brisbane"
		GMT_10_00_EST_Australia_Lindeman = "GMT+10:00-EST-Australia/Lindeman"
		GMT_10_30_CST_Australia_Adelaide = "GMT+10:30-CST-Australia/Adelaide"
		GMT_09_30_CST_Australia_Darwin = "GMT+09:30-CST-Australia/Darwin"
		GMT_08_00_WST_Australia_Perth = "GMT+08:00-WST-Australia/Perth"
		GMT_08_45_CWST_Australia_Eucla = "GMT+08:45-CWST-Australia/Eucla"
		GMT_04_00_AST_America_Aruba = "GMT-04:00-AST-America/Aruba"
		GMT_02_00_EET_Europe_Mariehamn = "GMT+02:00-EET-Europe/Mariehamn"
		GMT_04_00_AZT_Asia_Baku = "GMT+04:00-AZT-Asia/Baku"
		GMT_01_00_CET_Europe_Sarajevo = "GMT+01:00-CET-Europe/Sarajevo"
		GMT_04_00_AST_America_Barbados = "GMT-04:00-AST-America/Barbados"
		GMT_06_00_BDT_Asia_Dhaka = "GMT+06:00-BDT-Asia/Dhaka"
		GMT_01_00_CET_Europe_Brussels = "GMT+01:00-CET-Europe/Brussels"
		GMT_00_00_GMT_Africa_Ouagadougou = "GMT+00:00-GMT-Africa/Ouagadougou"
		GMT_02_00_EET_Europe_Sofia = "GMT+02:00-EET-Europe/Sofia"
		GMT_03_00_AST_Asia_Bahrain = "GMT+03:00-AST-Asia/Bahrain"
		GMT_02_00_CAT_Africa_Bujumbura = "GMT+02:00-CAT-Africa/Bujumbura"
		GMT_01_00_WAT_Africa_Porto_Novo = "GMT+01:00-WAT-Africa/Porto-Novo"
		GMT_04_00_AST_America_St_Barthelemy = "GMT-04:00-AST-America/St_Barthelemy"
		GMT_03_00_ADT_Atlantic_Bermuda = "GMT-03:00-ADT-Atlantic/Bermuda"
		GMT_08_00_BNT_Asia_Brunei = "GMT+08:00-BNT-Asia/Brunei"
		GMT_04_00_BOT_America_La_Paz = "GMT-04:00-BOT-America/La_Paz"
		GMT_02_00_FNT_America_Noronha = "GMT-02:00-FNT-America/Noronha"
		GMT_03_00_BRT_America_Belem = "GMT-03:00-BRT-America/Belem"
		GMT_03_00_BRT_America_Fortaleza = "GMT-03:00-BRT-America/Fortaleza"
		GMT_03_00_BRT_America_Recife = "GMT-03:00-BRT-America/Recife"
		GMT_03_00_BRT_America_Araguaina = "GMT-03:00-BRT-America/Araguaina"
		GMT_03_00_BRT_America_Maceio = "GMT-03:00-BRT-America/Maceio"
		GMT_03_00_BRT_America_Bahia = "GMT-03:00-BRT-America/Bahia"
		GMT_03_00_BRT_America_Sao_Paulo = "GMT-03:00-BRT-America/Sao_Paulo"
		GMT_04_00_AMT_America_Campo_Grande = "GMT-04:00-AMT-America/Campo_Grande"
		GMT_04_00_AMT_America_Cuiaba = "GMT-04:00-AMT-America/Cuiaba"
		GMT_03_00_BRT_America_Santarem = "GMT-03:00-BRT-America/Santarem"
		GMT_04_00_AMT_America_Porto_Velho = "GMT-04:00-AMT-America/Porto_Velho"
		GMT_04_00_AMT_America_Boa_Vista = "GMT-04:00-AMT-America/Boa_Vista"
		GMT_04_00_AMT_America_Manaus = "GMT-04:00-AMT-America/Manaus"
		GMT_04_00_AMT_America_Eirunepe = "GMT-04:00-AMT-America/Eirunepe"
		GMT_04_00_AMT_America_Rio_Branco = "GMT-04:00-AMT-America/Rio_Branco"
		GMT_04_00_EDT_America_Nassau = "GMT-04:00-EDT-America/Nassau"
		GMT_06_00_BTT_Asia_Thimphu = "GMT+06:00-BTT-Asia/Thimphu"
		GMT_02_00_CAT_Africa_Gaborone = "GMT+02:00-CAT-Africa/Gaborone"
		GMT_03_00_FET_Europe_Minsk = "GMT+03:00-FET-Europe/Minsk"
		GMT_06_00_CST_America_Belize = "GMT-06:00-CST-America/Belize"
		GMT_02_30_NDT_America_St_Johns = "GMT-02:30-NDT-America/St_Johns"
		GMT_03_00_ADT_America_Halifax = "GMT-03:00-ADT-America/Halifax"
		GMT_03_00_ADT_America_Glace_Bay = "GMT-03:00-ADT-America/Glace_Bay"
		GMT_03_00_ADT_America_Moncton = "GMT-03:00-ADT-America/Moncton"
		GMT_03_00_ADT_America_Goose_Bay = "GMT-03:00-ADT-America/Goose_Bay"
		GMT_04_00_AST_America_Blanc_Sablon = "GMT-04:00-AST-America/Blanc-Sablon"
		GMT_04_00_EDT_America_Montreal = "GMT-04:00-EDT-America/Montreal"
		GMT_04_00_EDT_America_Toronto = "GMT-04:00-EDT-America/Toronto"
		GMT_04_00_EDT_America_Nipigon = "GMT-04:00-EDT-America/Nipigon"
		GMT_04_00_EDT_America_Thunder_Bay = "GMT-04:00-EDT-America/Thunder_Bay"
		GMT_04_00_EDT_America_Iqaluit = "GMT-04:00-EDT-America/Iqaluit"
		GMT_04_00_EDT_America_Pangnirtung = "GMT-04:00-EDT-America/Pangnirtung"
		GMT_05_00_CDT_America_Resolute = "GMT-05:00-CDT-America/Resolute"
		GMT_05_00_EST_America_Atikokan = "GMT-05:00-EST-America/Atikokan"
		GMT_05_00_CDT_America_Rankin_Inlet = "GMT-05:00-CDT-America/Rankin_Inlet"
		GMT_05_00_CDT_America_Winnipeg = "GMT-05:00-CDT-America/Winnipeg"
		GMT_05_00_CDT_America_Rainy_River = "GMT-05:00-CDT-America/Rainy_River"
		GMT_06_00_CST_America_Regina = "GMT-06:00-CST-America/Regina"
		GMT_06_00_CST_America_Swift_Current = "GMT-06:00-CST-America/Swift_Current"
		GMT_06_00_MDT_America_Edmonton = "GMT-06:00-MDT-America/Edmonton"
		GMT_06_00_MDT_America_Cambridge_Bay = "GMT-06:00-MDT-America/Cambridge_Bay"
		GMT_06_00_MDT_America_Yellowknife = "GMT-06:00-MDT-America/Yellowknife"
		GMT_06_00_MDT_America_Inuvik = "GMT-06:00-MDT-America/Inuvik"
		GMT_07_00_MST_America_Dawson_Creek = "GMT-07:00-MST-America/Dawson_Creek"
		GMT_07_00_PDT_America_Vancouver = "GMT-07:00-PDT-America/Vancouver"
		GMT_07_00_PDT_America_Whitehorse = "GMT-07:00-PDT-America/Whitehorse"
		GMT_07_00_PDT_America_Dawson = "GMT-07:00-PDT-America/Dawson"
		GMT_06_30_CCT_Indian_Cocos = "GMT+06:30-CCT-Indian/Cocos"
		GMT_01_00_WAT_Africa_Kinshasa = "GMT+01:00-WAT-Africa/Kinshasa"
		GMT_02_00_CAT_Africa_Lubumbashi = "GMT+02:00-CAT-Africa/Lubumbashi"
		GMT_01_00_WAT_Africa_Bangui = "GMT+01:00-WAT-Africa/Bangui"
		GMT_01_00_WAT_Africa_Brazzaville = "GMT+01:00-WAT-Africa/Brazzaville"
		GMT_01_00_CET_Europe_Zurich = "GMT+01:00-CET-Europe/Zurich"
		GMT_00_00_GMT_Africa_Abidjan = "GMT+00:00-GMT-Africa/Abidjan"
		GMT_10_00_CKT_Pacific_Rarotonga = "GMT-10:00-CKT-Pacific/Rarotonga"
		GMT_04_00_CLT_America_Santiago = "GMT-04:00-CLT-America/Santiago"
		GMT_06_00_EAST_Pacific_Easter = "GMT-06:00-EAST-Pacific/Easter"
		GMT_01_00_WAT_Africa_Douala = "GMT+01:00-WAT-Africa/Douala"
		GMT_08_00_CST_Asia_Shanghai = "GMT+08:00-CST-Asia/Shanghai"
		GMT_08_00_CST_Asia_Harbin = "GMT+08:00-CST-Asia/Harbin"
		GMT_08_00_CST_Asia_Chongqing = "GMT+08:00-CST-Asia/Chongqing"
		GMT_08_00_CST_Asia_Urumqi = "GMT+08:00-CST-Asia/Urumqi"
		GMT_08_00_CST_Asia_Kashgar = "GMT+08:00-CST-Asia/Kashgar"
		GMT_05_00_COT_America_Bogota = "GMT-05:00-COT-America/Bogota"
		GMT_06_00_CST_America_Costa_Rica = "GMT-06:00-CST-America/Costa_Rica"
		GMT_04_00_CDT_America_Havana = "GMT-04:00-CDT-America/Havana"
		GMT_01_00_CVT_Atlantic_Cape_Verde = "GMT-01:00-CVT-Atlantic/Cape_Verde"
		GMT_07_00_CXT_Indian_Christmas = "GMT+07:00-CXT-Indian/Christmas"
		GMT_02_00_EET_Asia_Nicosia = "GMT+02:00-EET-Asia/Nicosia"
		GMT_01_00_CET_Europe_Prague = "GMT+01:00-CET-Europe/Prague"
		GMT_01_00_CET_Europe_Berlin = "GMT+01:00-CET-Europe/Berlin"
		GMT_03_00_EAT_Africa_Djibouti = "GMT+03:00-EAT-Africa/Djibouti"
		GMT_01_00_CET_Europe_Copenhagen = "GMT+01:00-CET-Europe/Copenhagen"
		GMT_04_00_AST_America_Dominica = "GMT-04:00-AST-America/Dominica"
		GMT_04_00_AST_America_Santo_Domingo = "GMT-04:00-AST-America/Santo_Domingo"
		GMT_01_00_CET_Africa_Algiers = "GMT+01:00-CET-Africa/Algiers"
		GMT_05_00_ECT_America_Guayaquil = "GMT-05:00-ECT-America/Guayaquil"
		GMT_06_00_GALT_Pacific_Galapagos = "GMT-06:00-GALT-Pacific/Galapagos"
		GMT_02_00_EET_Europe_Tallinn = "GMT+02:00-EET-Europe/Tallinn"
		GMT_02_00_EET_Africa_Cairo = "GMT+02:00-EET-Africa/Cairo"
		GMT_00_00_WET_Africa_El_Aaiun = "GMT+00:00-WET-Africa/El_Aaiun"
		GMT_03_00_EAT_Africa_Asmara = "GMT+03:00-EAT-Africa/Asmara"
		GMT_01_00_CET_Europe_Madrid = "GMT+01:00-CET-Europe/Madrid"
		GMT_01_00_CET_Africa_Ceuta = "GMT+01:00-CET-Africa/Ceuta"
		GMT_00_00_WET_Atlantic_Canary = "GMT+00:00-WET-Atlantic/Canary"
		GMT_03_00_EAT_Africa_Addis_Ababa = "GMT+03:00-EAT-Africa/Addis_Ababa"
		GMT_02_00_EET_Europe_Helsinki = "GMT+02:00-EET-Europe/Helsinki"
		GMT_12_00_FJT_Pacific_Fiji = "GMT+12:00-FJT-Pacific/Fiji"
		GMT_03_00_FKST_Atlantic_Stanley = "GMT-03:00-FKST-Atlantic/Stanley"
		GMT_10_00_CHUT_Pacific_Chuuk = "GMT+10:00-CHUT-Pacific/Chuuk"
		GMT_11_00_PONT_Pacific_Pohnpei = "GMT+11:00-PONT-Pacific/Pohnpei"
		GMT_11_00_KOST_Pacific_Kosrae = "GMT+11:00-KOST-Pacific/Kosrae"
		GMT_00_00_WET_Atlantic_Faroe = "GMT+00:00-WET-Atlantic/Faroe"
		GMT_01_00_CET_Europe_Paris = "GMT+01:00-CET-Europe/Paris"
		GMT_01_00_WAT_Africa_Libreville = "GMT+01:00-WAT-Africa/Libreville"
		GMT_00_00_GMT_Europe_London = "GMT+00:00-GMT-Europe/London"
		GMT_04_00_AST_America_Grenada = "GMT-04:00-AST-America/Grenada"
		GMT_04_00_GET_Asia_Tbilisi = "GMT+04:00-GET-Asia/Tbilisi"
		GMT_03_00_GFT_America_Cayenne = "GMT-03:00-GFT-America/Cayenne"
		GMT_00_00_GMT_Europe_Guernsey = "GMT+00:00-GMT-Europe/Guernsey"
		GMT_00_00_GMT_Africa_Accra = "GMT+00:00-GMT-Africa/Accra"
		GMT_01_00_CET_Europe_Gibraltar = "GMT+01:00-CET-Europe/Gibraltar"
		GMT_03_00_WGT_America_Godthab = "GMT-03:00-WGT-America/Godthab"
		GMT_00_00_GMT_America_Danmarkshavn = "GMT+00:00-GMT-America/Danmarkshavn"
		GMT_01_00_EGT_America_Scoresbysund = "GMT-01:00-EGT-America/Scoresbysund"
		GMT_03_00_ADT_America_Thule = "GMT-03:00-ADT-America/Thule"
		GMT_00_00_GMT_Africa_Banjul = "GMT+00:00-GMT-Africa/Banjul"
		GMT_00_00_GMT_Africa_Conakry = "GMT+00:00-GMT-Africa/Conakry"
		GMT_04_00_AST_America_Guadeloupe = "GMT-04:00-AST-America/Guadeloupe"
		GMT_01_00_WAT_Africa_Malabo = "GMT+01:00-WAT-Africa/Malabo"
		GMT_02_00_EET_Europe_Athens = "GMT+02:00-EET-Europe/Athens"
		GMT_02_00_GST_Atlantic_South_Georgia = "GMT-02:00-GST-Atlantic/South_Georgia"
		GMT_06_00_CST_America_Guatemala = "GMT-06:00-CST-America/Guatemala"
		GMT_10_00_ChST_Pacific_Guam = "GMT+10:00-ChST-Pacific/Guam"
		GMT_00_00_GMT_Africa_Bissau = "GMT+00:00-GMT-Africa/Bissau"
		GMT_04_00_GYT_America_Guyana = "GMT-04:00-GYT-America/Guyana"
		GMT_08_00_HKT_Asia_Hong_Kong = "GMT+08:00-HKT-Asia/Hong_Kong"
		GMT_06_00_CST_America_Tegucigalpa = "GMT-06:00-CST-America/Tegucigalpa"
		GMT_01_00_CET_Europe_Zagreb = "GMT+01:00-CET-Europe/Zagreb"
		GMT_05_00_EST_America_Port_au_Prince = "GMT-05:00-EST-America/Port-au-Prince"
		GMT_01_00_CET_Europe_Budapest = "GMT+01:00-CET-Europe/Budapest"
		GMT_07_00_WIT_Asia_Jakarta = "GMT+07:00-WIT-Asia/Jakarta"
		GMT_07_00_WIT_Asia_Pontianak = "GMT+07:00-WIT-Asia/Pontianak"
		GMT_08_00_CIT_Asia_Makassar = "GMT+08:00-CIT-Asia/Makassar"
		GMT_09_00_EIT_Asia_Jayapura = "GMT+09:00-EIT-Asia/Jayapura"
		GMT_00_00_GMT_Europe_Dublin = "GMT+00:00-GMT-Europe/Dublin"
		GMT_02_00_IST_Asia_Jerusalem = "GMT+02:00-IST-Asia/Jerusalem"
		GMT_00_00_GMT_Europe_Isle_of_Man = "GMT+00:00-GMT-Europe/Isle_of_Man"
		GMT_05_30_IST_Asia_Kolkata = "GMT+05:30-IST-Asia/Kolkata"
		GMT_06_00_IOT_Indian_Chagos = "GMT+06:00-IOT-Indian/Chagos"
		GMT_03_00_AST_Asia_Baghdad = "GMT+03:00-AST-Asia/Baghdad"
		GMT_03_30_IRST_Asia_Tehran = "GMT+03:30-IRST-Asia/Tehran"
		GMT_00_00_GMT_Atlantic_Reykjavik = "GMT+00:00-GMT-Atlantic/Reykjavik"
		GMT_01_00_CET_Europe_Rome = "GMT+01:00-CET-Europe/Rome"
		GMT_00_00_GMT_Europe_Jersey = "GMT+00:00-GMT-Europe/Jersey"
		GMT_05_00_EST_America_Jamaica = "GMT-05:00-EST-America/Jamaica"
		GMT_02_00_EET_Asia_Amman = "GMT+02:00-EET-Asia/Amman"
		GMT_09_00_JST_Asia_Tokyo = "GMT+09:00-JST-Asia/Tokyo"
		GMT_03_00_EAT_Africa_Nairobi = "GMT+03:00-EAT-Africa/Nairobi"
		GMT_06_00_KGT_Asia_Bishkek = "GMT+06:00-KGT-Asia/Bishkek"
		GMT_07_00_ICT_Asia_Phnom_Penh = "GMT+07:00-ICT-Asia/Phnom_Penh"
		GMT_12_00_GILT_Pacific_Tarawa = "GMT+12:00-GILT-Pacific/Tarawa"
		GMT_13_00_PHOT_Pacific_Enderbury = "GMT+13:00-PHOT-Pacific/Enderbury"
		GMT_14_00_LINT_Pacific_Kiritimati = "GMT+14:00-LINT-Pacific/Kiritimati"
		GMT_03_00_EAT_Indian_Comoro = "GMT+03:00-EAT-Indian/Comoro"
		GMT_04_00_AST_America_St_Kitts = "GMT-04:00-AST-America/St_Kitts"
		GMT_09_00_KST_Asia_Pyongyang = "GMT+09:00-KST-Asia/Pyongyang"
		GMT_09_00_KST_Asia_Seoul = "GMT+09:00-KST-Asia/Seoul"
		GMT_03_00_AST_Asia_Kuwait = "GMT+03:00-AST-Asia/Kuwait"
		GMT_05_00_EST_America_Cayman = "GMT-05:00-EST-America/Cayman"
		GMT_06_00_ALMT_Asia_Almaty = "GMT+06:00-ALMT-Asia/Almaty"
		GMT_06_00_QYZT_Asia_Qyzylorda = "GMT+06:00-QYZT-Asia/Qyzylorda"
		GMT_05_00_AQTT_Asia_Aqtobe = "GMT+05:00-AQTT-Asia/Aqtobe"
		GMT_05_00_AQTT_Asia_Aqtau = "GMT+05:00-AQTT-Asia/Aqtau"
		GMT_05_00_ORAT_Asia_Oral = "GMT+05:00-ORAT-Asia/Oral"
		GMT_07_00_ICT_Asia_Vientiane = "GMT+07:00-ICT-Asia/Vientiane"
		GMT_02_00_EET_Asia_Beirut = "GMT+02:00-EET-Asia/Beirut"
		GMT_04_00_AST_America_St_Lucia = "GMT-04:00-AST-America/St_Lucia"
		GMT_01_00_CET_Europe_Vaduz = "GMT+01:00-CET-Europe/Vaduz"
		GMT_05_30_IST_Asia_Colombo = "GMT+05:30-IST-Asia/Colombo"
		GMT_00_00_GMT_Africa_Monrovia = "GMT+00:00-GMT-Africa/Monrovia"
		GMT_02_00_SAST_Africa_Maseru = "GMT+02:00-SAST-Africa/Maseru"
		GMT_02_00_EET_Europe_Vilnius = "GMT+02:00-EET-Europe/Vilnius"
		GMT_01_00_CET_Europe_Luxembourg = "GMT+01:00-CET-Europe/Luxembourg"
		GMT_02_00_EET_Europe_Riga = "GMT+02:00-EET-Europe/Riga"
		GMT_02_00_EET_Africa_Tripoli = "GMT+02:00-EET-Africa/Tripoli"
		GMT_00_00_WET_Africa_Casablanca = "GMT+00:00-WET-Africa/Casablanca"
		GMT_01_00_CET_Europe_Monaco = "GMT+01:00-CET-Europe/Monaco"
		GMT_02_00_EET_Europe_Chisinau = "GMT+02:00-EET-Europe/Chisinau"
		GMT_01_00_CET_Europe_Podgorica = "GMT+01:00-CET-Europe/Podgorica"
		GMT_04_00_AST_America_Marigot = "GMT-04:00-AST-America/Marigot"
		GMT_03_00_EAT_Indian_Antananarivo = "GMT+03:00-EAT-Indian/Antananarivo"
		GMT_12_00_MHT_Pacific_Majuro = "GMT+12:00-MHT-Pacific/Majuro"
		GMT_12_00_MHT_Pacific_Kwajalein = "GMT+12:00-MHT-Pacific/Kwajalein"
		GMT_01_00_CET_Europe_Skopje = "GMT+01:00-CET-Europe/Skopje"
		GMT_00_00_GMT_Africa_Bamako = "GMT+00:00-GMT-Africa/Bamako"
		GMT_06_30_MMT_Asia_Rangoon = "GMT+06:30-MMT-Asia/Rangoon"
		GMT_08_00_ULAT_Asia_Ulaanbaatar = "GMT+08:00-ULAT-Asia/Ulaanbaatar"
		GMT_07_00_HOVT_Asia_Hovd = "GMT+07:00-HOVT-Asia/Hovd"
		GMT_08_00_CHOT_Asia_Choibalsan = "GMT+08:00-CHOT-Asia/Choibalsan"
		GMT_08_00_CST_Asia_Macau = "GMT+08:00-CST-Asia/Macau"
		GMT_10_00_ChST_Pacific_Saipan = "GMT+10:00-ChST-Pacific/Saipan"
		GMT_04_00_AST_America_Martinique = "GMT-04:00-AST-America/Martinique"
		GMT_00_00_GMT_Africa_Nouakchott = "GMT+00:00-GMT-Africa/Nouakchott"
		GMT_04_00_AST_America_Montserrat = "GMT-04:00-AST-America/Montserrat"
		GMT_01_00_CET_Europe_Malta = "GMT+01:00-CET-Europe/Malta"
		GMT_04_00_MUT_Indian_Mauritius = "GMT+04:00-MUT-Indian/Mauritius"
		GMT_05_00_MVT_Indian_Maldives = "GMT+05:00-MVT-Indian/Maldives"
		GMT_02_00_CAT_Africa_Blantyre = "GMT+02:00-CAT-Africa/Blantyre"
		GMT_06_00_CST_America_Mexico_City = "GMT-06:00-CST-America/Mexico_City"
		GMT_06_00_CST_America_Cancun = "GMT-06:00-CST-America/Cancun"
		GMT_06_00_CST_America_Merida = "GMT-06:00-CST-America/Merida"
		GMT_06_00_CST_America_Monterrey = "GMT-06:00-CST-America/Monterrey"
		GMT_05_00_CDT_America_Matamoros = "GMT-05:00-CDT-America/Matamoros"
		GMT_07_00_MST_America_Mazatlan = "GMT-07:00-MST-America/Mazatlan"
		GMT_07_00_MST_America_Chihuahua = "GMT-07:00-MST-America/Chihuahua"
		GMT_06_00_MDT_America_Ojinaga = "GMT-06:00-MDT-America/Ojinaga"
		GMT_07_00_MST_America_Hermosillo = "GMT-07:00-MST-America/Hermosillo"
		GMT_07_00_PDT_America_Tijuana = "GMT-07:00-PDT-America/Tijuana"
		GMT_08_00_PST_America_Santa_Isabel = "GMT-08:00-PST-America/Santa_Isabel"
		GMT_06_00_CST_America_Bahia_Banderas = "GMT-06:00-CST-America/Bahia_Banderas"
		GMT_08_00_MYT_Asia_Kuala_Lumpur = "GMT+08:00-MYT-Asia/Kuala_Lumpur"
		GMT_08_00_MYT_Asia_Kuching = "GMT+08:00-MYT-Asia/Kuching"
		GMT_02_00_CAT_Africa_Maputo = "GMT+02:00-CAT-Africa/Maputo"
		GMT_02_00_WAST_Africa_Windhoek = "GMT+02:00-WAST-Africa/Windhoek"
		GMT_11_00_NCT_Pacific_Noumea = "GMT+11:00-NCT-Pacific/Noumea"
		GMT_01_00_WAT_Africa_Niamey = "GMT+01:00-WAT-Africa/Niamey"
		GMT_11_30_NFT_Pacific_Norfolk = "GMT+11:30-NFT-Pacific/Norfolk"
		GMT_01_00_WAT_Africa_Lagos = "GMT+01:00-WAT-Africa/Lagos"
		GMT_06_00_CST_America_Managua = "GMT-06:00-CST-America/Managua"
		GMT_01_00_CET_Europe_Amsterdam = "GMT+01:00-CET-Europe/Amsterdam"
		GMT_01_00_CET_Europe_Oslo = "GMT+01:00-CET-Europe/Oslo"
		GMT_05_45_NPT_Asia_Kathmandu = "GMT+05:45-NPT-Asia/Kathmandu"
		GMT_12_00_NRT_Pacific_Nauru = "GMT+12:00-NRT-Pacific/Nauru"
		GMT_11_00_NUT_Pacific_Niue = "GMT-11:00-NUT-Pacific/Niue"
		GMT_13_00_NZDT_Pacific_Auckland = "GMT+13:00-NZDT-Pacific/Auckland"
		GMT_13_45_CHADT_Pacific_Chatham = "GMT+13:45-CHADT-Pacific/Chatham"
		GMT_04_00_GST_Asia_Muscat = "GMT+04:00-GST-Asia/Muscat"
		GMT_05_00_EST_America_Panama = "GMT-05:00-EST-America/Panama"
		GMT_05_00_PET_America_Lima = "GMT-05:00-PET-America/Lima"
		GMT_10_00_TAHT_Pacific_Tahiti = "GMT-10:00-TAHT-Pacific/Tahiti"
		GMT_09_30_MART_Pacific_Marquesas = "GMT-09:30-MART-Pacific/Marquesas"
		GMT_09_00_GAMT_Pacific_Gambier = "GMT-09:00-GAMT-Pacific/Gambier"
		GMT_10_00_PGT_Pacific_Port_Moresby = "GMT+10:00-PGT-Pacific/Port_Moresby"
		GMT_08_00_PHT_Asia_Manila = "GMT+08:00-PHT-Asia/Manila"
		GMT_05_00_PKT_Asia_Karachi = "GMT+05:00-PKT-Asia/Karachi"
		GMT_01_00_CET_Europe_Warsaw = "GMT+01:00-CET-Europe/Warsaw"
		GMT_02_00_PMDT_America_Miquelon = "GMT-02:00-PMDT-America/Miquelon"
		GMT_08_00_PST_Pacific_Pitcairn = "GMT-08:00-PST-Pacific/Pitcairn"
		GMT_04_00_AST_America_Puerto_Rico = "GMT-04:00-AST-America/Puerto_Rico"
		GMT_02_00_EET_Asia_Gaza = "GMT+02:00-EET-Asia/Gaza"
		GMT_02_00_EET_Asia_Hebron = "GMT+02:00-EET-Asia/Hebron"
		GMT_00_00_WET_Europe_Lisbon = "GMT+00:00-WET-Europe/Lisbon"
		GMT_00_00_WET_Atlantic_Madeira = "GMT+00:00-WET-Atlantic/Madeira"
		GMT_01_00_AZOT_Atlantic_Azores = "GMT-01:00-AZOT-Atlantic/Azores"
		GMT_09_00_PWT_Pacific_Palau = "GMT+09:00-PWT-Pacific/Palau"
		GMT_03_00_PYST_America_Asuncion = "GMT-03:00-PYST-America/Asuncion"
		GMT_03_00_AST_Asia_Qatar = "GMT+03:00-AST-Asia/Qatar"
		GMT_04_00_RET_Indian_Reunion = "GMT+04:00-RET-Indian/Reunion"
		GMT_02_00_EET_Europe_Bucharest = "GMT+02:00-EET-Europe/Bucharest"
		GMT_01_00_CET_Europe_Belgrade = "GMT+01:00-CET-Europe/Belgrade"
		GMT_03_00_FET_Europe_Kaliningrad = "GMT+03:00-FET-Europe/Kaliningrad"
		GMT_04_00_MSK_Europe_Moscow = "GMT+04:00-MSK-Europe/Moscow"
		GMT_04_00_VOLT_Europe_Volgograd = "GMT+04:00-VOLT-Europe/Volgograd"
		GMT_04_00_SAMT_Europe_Samara = "GMT+04:00-SAMT-Europe/Samara"
		GMT_06_00_YEKT_Asia_Yekaterinburg = "GMT+06:00-YEKT-Asia/Yekaterinburg"
		GMT_07_00_OMST_Asia_Omsk = "GMT+07:00-OMST-Asia/Omsk"
		GMT_07_00_NOVT_Asia_Novosibirsk = "GMT+07:00-NOVT-Asia/Novosibirsk"
		GMT_07_00_NOVT_Asia_Novokuznetsk = "GMT+07:00-NOVT-Asia/Novokuznetsk"
		GMT_08_00_KRAT_Asia_Krasnoyarsk = "GMT+08:00-KRAT-Asia/Krasnoyarsk"
		GMT_09_00_IRKT_Asia_Irkutsk = "GMT+09:00-IRKT-Asia/Irkutsk"
		GMT_10_00_YAKT_Asia_Yakutsk = "GMT+10:00-YAKT-Asia/Yakutsk"
		GMT_11_00_VLAT_Asia_Vladivostok = "GMT+11:00-VLAT-Asia/Vladivostok"
		GMT_11_00_SAKT_Asia_Sakhalin = "GMT+11:00-SAKT-Asia/Sakhalin"
		GMT_12_00_MAGT_Asia_Magadan = "GMT+12:00-MAGT-Asia/Magadan"
		GMT_12_00_PETT_Asia_Kamchatka = "GMT+12:00-PETT-Asia/Kamchatka"
		GMT_12_00_ANAT_Asia_Anadyr = "GMT+12:00-ANAT-Asia/Anadyr"
		GMT_02_00_CAT_Africa_Kigali = "GMT+02:00-CAT-Africa/Kigali"
		GMT_03_00_AST_Asia_Riyadh = "GMT+03:00-AST-Asia/Riyadh"
		GMT_11_00_SBT_Pacific_Guadalcanal = "GMT+11:00-SBT-Pacific/Guadalcanal"
		GMT_04_00_SCT_Indian_Mahe = "GMT+04:00-SCT-Indian/Mahe"
		GMT_03_00_EAT_Africa_Khartoum = "GMT+03:00-EAT-Africa/Khartoum"
		GMT_01_00_CET_Europe_Stockholm = "GMT+01:00-CET-Europe/Stockholm"
		GMT_08_00_SGT_Asia_Singapore = "GMT+08:00-SGT-Asia/Singapore"
		GMT_00_00_GMT_Atlantic_St_Helena = "GMT+00:00-GMT-Atlantic/St_Helena"
		GMT_01_00_CET_Europe_Ljubljana = "GMT+01:00-CET-Europe/Ljubljana"
		GMT_01_00_CET_Arctic_Longyearbyen = "GMT+01:00-CET-Arctic/Longyearbyen"
		GMT_01_00_CET_Europe_Bratislava = "GMT+01:00-CET-Europe/Bratislava"
		GMT_00_00_GMT_Africa_Freetown = "GMT+00:00-GMT-Africa/Freetown"
		GMT_01_00_CET_Europe_San_Marino = "GMT+01:00-CET-Europe/San_Marino"
		GMT_00_00_GMT_Africa_Dakar = "GMT+00:00-GMT-Africa/Dakar"
		GMT_03_00_EAT_Africa_Mogadishu = "GMT+03:00-EAT-Africa/Mogadishu"
		GMT_03_00_SRT_America_Paramaribo = "GMT-03:00-SRT-America/Paramaribo"
		GMT_00_00_GMT_Africa_Sao_Tome = "GMT+00:00-GMT-Africa/Sao_Tome"
		GMT_06_00_CST_America_El_Salvador = "GMT-06:00-CST-America/El_Salvador"
		GMT_02_00_EET_Asia_Damascus = "GMT+02:00-EET-Asia/Damascus"
		GMT_02_00_SAST_Africa_Mbabane = "GMT+02:00-SAST-Africa/Mbabane"
		GMT_04_00_EDT_America_Grand_Turk = "GMT-04:00-EDT-America/Grand_Turk"
		GMT_01_00_WAT_Africa_Ndjamena = "GMT+01:00-WAT-Africa/Ndjamena"
		GMT_05_00_TFT_Indian_Kerguelen = "GMT+05:00-TFT-Indian/Kerguelen"
		GMT_00_00_GMT_Africa_Lome = "GMT+00:00-GMT-Africa/Lome"
		GMT_07_00_ICT_Asia_Bangkok = "GMT+07:00-ICT-Asia/Bangkok"
		GMT_05_00_TJT_Asia_Dushanbe = "GMT+05:00-TJT-Asia/Dushanbe"
		GMT_10_00_TKT_Pacific_Fakaofo = "GMT-10:00-TKT-Pacific/Fakaofo"
		GMT_09_00_TLT_Asia_Dili = "GMT+09:00-TLT-Asia/Dili"
		GMT_05_00_TMT_Asia_Ashgabat = "GMT+05:00-TMT-Asia/Ashgabat"
		GMT_01_00_CET_Africa_Tunis = "GMT+01:00-CET-Africa/Tunis"
		GMT_13_00_TOT_Pacific_Tongatapu = "GMT+13:00-TOT-Pacific/Tongatapu"
		GMT_02_00_EET_Europe_Istanbul = "GMT+02:00-EET-Europe/Istanbul"
		GMT_04_00_AST_America_Port_of_Spain = "GMT-04:00-AST-America/Port_of_Spain"
		GMT_12_00_TVT_Pacific_Funafuti = "GMT+12:00-TVT-Pacific/Funafuti"
		GMT_08_00_CST_Asia_Taipei = "GMT+08:00-CST-Asia/Taipei"
		GMT_03_00_EAT_Africa_Dar_es_Salaam = "GMT+03:00-EAT-Africa/Dar_es_Salaam"
		GMT_02_00_EET_Europe_Kiev = "GMT+02:00-EET-Europe/Kiev"
		GMT_02_00_EET_Europe_Uzhgorod = "GMT+02:00-EET-Europe/Uzhgorod"
		GMT_02_00_EET_Europe_Zaporozhye = "GMT+02:00-EET-Europe/Zaporozhye"
		GMT_02_00_EET_Europe_Simferopol = "GMT+02:00-EET-Europe/Simferopol"
		GMT_03_00_EAT_Africa_Kampala = "GMT+03:00-EAT-Africa/Kampala"
		GMT_10_00_HST_Pacific_Johnston = "GMT-10:00-HST-Pacific/Johnston"
		GMT_11_00_SST_Pacific_Midway = "GMT-11:00-SST-Pacific/Midway"
		GMT_12_00_WAKT_Pacific_Wake = "GMT+12:00-WAKT-Pacific/Wake"
		GMT_04_00_EDT_America_New_York = "GMT-04:00-EDT-America/New_York"
		GMT_04_00_EDT_America_Detroit = "GMT-04:00-EDT-America/Detroit"
		GMT_04_00_EDT_America_Kentucky_Louisville = "GMT-04:00-EDT-America/Kentucky/Louisville"
		GMT_04_00_EDT_America_Kentucky_Monticello = "GMT-04:00-EDT-America/Kentucky/Monticello"
		GMT_04_00_EDT_America_Indiana_Indianapolis = "GMT-04:00-EDT-America/Indiana/Indianapolis"
		GMT_04_00_EDT_America_Indiana_Vincennes = "GMT-04:00-EDT-America/Indiana/Vincennes"
		GMT_04_00_EDT_America_Indiana_Winamac = "GMT-04:00-EDT-America/Indiana/Winamac"
		GMT_04_00_EDT_America_Indiana_Marengo = "GMT-04:00-EDT-America/Indiana/Marengo"
		GMT_04_00_EDT_America_Indiana_Petersburg = "GMT-04:00-EDT-America/Indiana/Petersburg"
		GMT_04_00_EDT_America_Indiana_Vevay = "GMT-04:00-EDT-America/Indiana/Vevay"
		GMT_05_00_CDT_America_Chicago = "GMT-05:00-CDT-America/Chicago"
		GMT_05_00_CDT_America_Indiana_Tell_City = "GMT-05:00-CDT-America/Indiana/Tell_City"
		GMT_05_00_CDT_America_Indiana_Knox = "GMT-05:00-CDT-America/Indiana/Knox"
		GMT_05_00_CDT_America_Menominee = "GMT-05:00-CDT-America/Menominee"
		GMT_05_00_CDT_America_North_Dakota_Center = "GMT-05:00-CDT-America/North_Dakota/Center"
		GMT_05_00_CDT_America_North_Dakota_New_Salem = "GMT-05:00-CDT-America/North_Dakota/New_Salem"
		GMT_05_00_CDT_America_North_Dakota_Beulah = "GMT-05:00-CDT-America/North_Dakota/Beulah"
		GMT_06_00_MDT_America_Denver = "GMT-06:00-MDT-America/Denver"
		GMT_06_00_MDT_America_Boise = "GMT-06:00-MDT-America/Boise"
		GMT_06_00_MDT_America_Shiprock = "GMT-06:00-MDT-America/Shiprock"
		GMT_07_00_MST_America_Phoenix = "GMT-07:00-MST-America/Phoenix"
		GMT_07_00_PDT_America_Los_Angeles = "GMT-07:00-PDT-America/Los_Angeles"
		GMT_08_00_AKDT_America_Anchorage = "GMT-08:00-AKDT-America/Anchorage"
		GMT_08_00_AKDT_America_Juneau = "GMT-08:00-AKDT-America/Juneau"
		GMT_08_00_AKDT_America_Sitka = "GMT-08:00-AKDT-America/Sitka"
		GMT_08_00_AKDT_America_Yakutat = "GMT-08:00-AKDT-America/Yakutat"
		GMT_08_00_AKDT_America_Nome = "GMT-08:00-AKDT-America/Nome"
		GMT_09_00_HADT_America_Adak = "GMT-09:00-HADT-America/Adak"
		GMT_08_00_MeST_America_Metlakatla = "GMT-08:00-MeST-America/Metlakatla"
		GMT_10_00_HST_Pacific_Honolulu = "GMT-10:00-HST-Pacific/Honolulu"
		GMT_03_00_UYT_America_Montevideo = "GMT-03:00-UYT-America/Montevideo"
		GMT_05_00_UZT_Asia_Samarkand = "GMT+05:00-UZT-Asia/Samarkand"
		GMT_05_00_UZT_Asia_Tashkent = "GMT+05:00-UZT-Asia/Tashkent"
		GMT_01_00_CET_Europe_Vatican = "GMT+01:00-CET-Europe/Vatican"
		GMT_04_00_AST_America_St_Vincent = "GMT-04:00-AST-America/St_Vincent"
		GMT_04_30_VET_America_Caracas = "GMT-04:30-VET-America/Caracas"
		GMT_04_00_AST_America_Tortola = "GMT-04:00-AST-America/Tortola"
		GMT_04_00_AST_America_St_Thomas = "GMT-04:00-AST-America/St_Thomas"
		GMT_07_00_ICT_Asia_Ho_Chi_Minh = "GMT+07:00-ICT-Asia/Ho_Chi_Minh"
		GMT_11_00_VUT_Pacific_Efate = "GMT+11:00-VUT-Pacific/Efate"
		GMT_12_00_WFT_Pacific_Wallis = "GMT+12:00-WFT-Pacific/Wallis"
		GMT_14_00_WSDT_Pacific_Apia = "GMT+14:00-WSDT-Pacific/Apia"
		GMT_03_00_AST_Asia_Aden = "GMT+03:00-AST-Asia/Aden"
		GMT_03_00_EAT_Indian_Mayotte = "GMT+03:00-EAT-Indian/Mayotte"
		GMT_02_00_SAST_Africa_Johannesburg = "GMT+02:00-SAST-Africa/Johannesburg"
		GMT_02_00_CAT_Africa_Lusaka = "GMT+02:00-CAT-Africa/Lusaka"
		GMT_02_00_CAT_Africa_Harare = "GMT+02:00-CAT-Africa/Harare"

	class Systemtype:
		Stand_alone = "Stand-alone"
		HA = "HA"
		Cluster = "Cluster"

	class Securecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Level:
		basic = "basic"
		extended = "extended"
		full = "full"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tagged:
		YES = "YES"
		NO = "NO"

	class Cookieversion:
		_0 = "0"
		_1 = "1"

class nsconfig_response(base_response) :
	def __init__(self, length=1) :
		self.nsconfig = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsconfig = [nsconfig() for _ in range(length)]

