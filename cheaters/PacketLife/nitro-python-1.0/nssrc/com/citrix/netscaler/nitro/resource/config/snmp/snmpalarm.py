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

class snmpalarm(base_resource) :
	""" Configuration for alarm resource. """
	def __init__(self) :
		self._trapname = ""
		self._thresholdvalue = 0
		self._normalvalue = 0
		self._time = 0
		self._state = ""
		self._severity = ""
		self._logging = ""
		self._timeout = 0
		self.___count = 0

	@property
	def trapname(self) :
		ur"""Name of the SNMP alarm. This parameter is required for identifying the SNMP alarm and cannot be modified.<br/>Possible values = CPU-USAGE, AVERAGE-CPU, MEMORY, MGMT-CPU-USAGE, SYNFLOOD, VSERVER-REQRATE, SERVICE-REQRATE, ENTITY-RXRATE, ENTITY-TXRATE, ENTITY-SYNFLOOD, SERVICE-MAXCLIENTS, HA-STATE-CHANGE, ENTITY-STATE, CONFIG-CHANGE, CONFIG-SAVE, SERVICEGROUP-MEMBER-REQRATE, SERVICEGROUP-MEMBER-MAXCLIENTS, MONITOR-RTO-THRESHOLD, LOGIN-FAILURE, SSL-CERT-EXPIRY, FAN-SPEED-LOW, VOLTAGE-LOW, VOLTAGE-HIGH, TEMPERATURE-HIGH, CPU-TEMPERATURE-HIGH, POWER-SUPPLY-FAILURE, DISK-USAGE-HIGH, INTERFACE-THROUGHPUT-LOW, MON_PROBE_FAILED, HA-VERSION-MISMATCH, HA-SYNC-FAILURE, HA-NO-HEARTBEATS, HA-BAD-SECONDARY-STATE, INTERFACE-BW-USAGE, RATE-LIMIT-THRESHOLD-EXCEEDED, ENTITY-NAME-CHANGE, HA-PROP-FAILURE, IP-CONFLICT, PF-RL-RATE-THRESHOLD, PF-RL-PPS-THRESHOLD, PF-RL-RATE-PKTS-DROPPED, PF-RL-PPS-PKTS-DROPPED, APPFW-START-URL, APPFW-DENY-URL, APPFW-VIOLATIONS-TYPE, APPFW-REFERER-HEADER, APPFW-CSRF-TAG, APPFW-COOKIE, APPFW-FIELD-CONSISTENCY, APPFW-BUFFER-OVERFLOW, APPFW-FIELD-FORMAT, APPFW-SAFE-COMMERCE, APPFW-SAFE-OBJECT, APPFW-POLICY-HIT, APPFW-XSS, APPFW-XML-XSS, APPFW-SQL, APPFW-XML-SQL, APPFW-XML-ATTACHMENT, APPFW-XML-DOS, APPFW-XML-VALIDATION, APPFW-XML-WSI, APPFW-XML-SCHEMA-COMPILE, APPFW-XML-SOAP-FAULT, DNSKEY-EXPIRY, HA-LICENSE-MISMATCH, SSL-CARD-FAILED, SSL-CARD-NORMAL, WARM-RESTART-EVENT, HARD-DISK-DRIVE-ERRORS, COMPACT-FLASH-ERRORS, CALLHOME-UPLOAD-EVENT, 1024KEY-EXCHANGE-RATE, 2048KEY-EXCHANGE-RATE, 4096KEY-EXCHANGE-RATE, SSL-CUR-SESSION-INUSE, CLUSTER-NODE-HEALTH, CLUSTER-NODE-QUORUM, CLUSTER-VERSION-MISMATCH, CLUSTER-CCO-CHANGE, CLUSTER-OVS-CHANGE, CLUSTER-SYNC-FAILURE, CLUSTER-PROP-FAILURE, HA-STICKY-PRIMARY, INBAND-PROTOCOL-VERSION-MISMATCH, SSL-CHIP-REINIT, VRID-STATE-CHANGE, PORT-ALLOC-FAILED, LLDP-REMOTE-CHANGE, DUPLICATE-IPV6.
		"""
		try :
			return self._trapname
		except Exception as e:
			raise e

	@trapname.setter
	def trapname(self, trapname) :
		ur"""Name of the SNMP alarm. This parameter is required for identifying the SNMP alarm and cannot be modified.<br/>Possible values = CPU-USAGE, AVERAGE-CPU, MEMORY, MGMT-CPU-USAGE, SYNFLOOD, VSERVER-REQRATE, SERVICE-REQRATE, ENTITY-RXRATE, ENTITY-TXRATE, ENTITY-SYNFLOOD, SERVICE-MAXCLIENTS, HA-STATE-CHANGE, ENTITY-STATE, CONFIG-CHANGE, CONFIG-SAVE, SERVICEGROUP-MEMBER-REQRATE, SERVICEGROUP-MEMBER-MAXCLIENTS, MONITOR-RTO-THRESHOLD, LOGIN-FAILURE, SSL-CERT-EXPIRY, FAN-SPEED-LOW, VOLTAGE-LOW, VOLTAGE-HIGH, TEMPERATURE-HIGH, CPU-TEMPERATURE-HIGH, POWER-SUPPLY-FAILURE, DISK-USAGE-HIGH, INTERFACE-THROUGHPUT-LOW, MON_PROBE_FAILED, HA-VERSION-MISMATCH, HA-SYNC-FAILURE, HA-NO-HEARTBEATS, HA-BAD-SECONDARY-STATE, INTERFACE-BW-USAGE, RATE-LIMIT-THRESHOLD-EXCEEDED, ENTITY-NAME-CHANGE, HA-PROP-FAILURE, IP-CONFLICT, PF-RL-RATE-THRESHOLD, PF-RL-PPS-THRESHOLD, PF-RL-RATE-PKTS-DROPPED, PF-RL-PPS-PKTS-DROPPED, APPFW-START-URL, APPFW-DENY-URL, APPFW-VIOLATIONS-TYPE, APPFW-REFERER-HEADER, APPFW-CSRF-TAG, APPFW-COOKIE, APPFW-FIELD-CONSISTENCY, APPFW-BUFFER-OVERFLOW, APPFW-FIELD-FORMAT, APPFW-SAFE-COMMERCE, APPFW-SAFE-OBJECT, APPFW-POLICY-HIT, APPFW-XSS, APPFW-XML-XSS, APPFW-SQL, APPFW-XML-SQL, APPFW-XML-ATTACHMENT, APPFW-XML-DOS, APPFW-XML-VALIDATION, APPFW-XML-WSI, APPFW-XML-SCHEMA-COMPILE, APPFW-XML-SOAP-FAULT, DNSKEY-EXPIRY, HA-LICENSE-MISMATCH, SSL-CARD-FAILED, SSL-CARD-NORMAL, WARM-RESTART-EVENT, HARD-DISK-DRIVE-ERRORS, COMPACT-FLASH-ERRORS, CALLHOME-UPLOAD-EVENT, 1024KEY-EXCHANGE-RATE, 2048KEY-EXCHANGE-RATE, 4096KEY-EXCHANGE-RATE, SSL-CUR-SESSION-INUSE, CLUSTER-NODE-HEALTH, CLUSTER-NODE-QUORUM, CLUSTER-VERSION-MISMATCH, CLUSTER-CCO-CHANGE, CLUSTER-OVS-CHANGE, CLUSTER-SYNC-FAILURE, CLUSTER-PROP-FAILURE, HA-STICKY-PRIMARY, INBAND-PROTOCOL-VERSION-MISMATCH, SSL-CHIP-REINIT, VRID-STATE-CHANGE, PORT-ALLOC-FAILED, LLDP-REMOTE-CHANGE, DUPLICATE-IPV6
		"""
		try :
			self._trapname = trapname
		except Exception as e:
			raise e

	@property
	def thresholdvalue(self) :
		ur"""Value for the high threshold. The NetScaler appliance generates an SNMP trap message when the value of the attribute associated with the alarm is greater than or equal to the specified high threshold value.<br/>Minimum length =  1.
		"""
		try :
			return self._thresholdvalue
		except Exception as e:
			raise e

	@thresholdvalue.setter
	def thresholdvalue(self, thresholdvalue) :
		ur"""Value for the high threshold. The NetScaler appliance generates an SNMP trap message when the value of the attribute associated with the alarm is greater than or equal to the specified high threshold value.<br/>Minimum length =  1
		"""
		try :
			self._thresholdvalue = thresholdvalue
		except Exception as e:
			raise e

	@property
	def normalvalue(self) :
		ur"""Value for the normal threshold. A trap message is generated if the value of the respective attribute falls to or below this value after exceeding the high threshold.<br/>Minimum length =  1.
		"""
		try :
			return self._normalvalue
		except Exception as e:
			raise e

	@normalvalue.setter
	def normalvalue(self, normalvalue) :
		ur"""Value for the normal threshold. A trap message is generated if the value of the respective attribute falls to or below this value after exceeding the high threshold.<br/>Minimum length =  1
		"""
		try :
			self._normalvalue = normalvalue
		except Exception as e:
			raise e

	@property
	def time(self) :
		ur"""Interval, in seconds, at which the NetScaler appliance generates SNMP trap messages when the conditions specified in the SNMP alarm are met.Can be specified for the following alarms: SYNFLOOD, HA-VERSION-MISMATCH, HA-SYNC-FAILURE, HA-NO-HEARTBEATS,HA-BAD-SECONDARY-STATE, CLUSTER-NODE-HEALTH, CLUSTER-NODE-QUORUM, CLUSTER-VERSION-MISMATCH, PORT-ALLOC-FAILED and APPFW traps. Default trap time intervals: SYNFLOOD and APPFW traps = 1sec, PORT-ALLOC-FAILED = 3600sec(1 hour), Other Traps = 86400sec(1 day).<br/>Default value: 1.
		"""
		try :
			return self._time
		except Exception as e:
			raise e

	@time.setter
	def time(self, time) :
		ur"""Interval, in seconds, at which the NetScaler appliance generates SNMP trap messages when the conditions specified in the SNMP alarm are met.Can be specified for the following alarms: SYNFLOOD, HA-VERSION-MISMATCH, HA-SYNC-FAILURE, HA-NO-HEARTBEATS,HA-BAD-SECONDARY-STATE, CLUSTER-NODE-HEALTH, CLUSTER-NODE-QUORUM, CLUSTER-VERSION-MISMATCH, PORT-ALLOC-FAILED and APPFW traps. Default trap time intervals: SYNFLOOD and APPFW traps = 1sec, PORT-ALLOC-FAILED = 3600sec(1 hour), Other Traps = 86400sec(1 day).<br/>Default value: 1
		"""
		try :
			self._time = time
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Current state of the SNMP alarm. The NetScaler appliance generates trap messages only for SNMP alarms that are enabled. Some alarms are enabled by default, but you can disable them.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		ur"""Current state of the SNMP alarm. The NetScaler appliance generates trap messages only for SNMP alarms that are enabled. Some alarms are enabled by default, but you can disable them.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def severity(self) :
		ur"""Severity level assigned to trap messages generated by this alarm. The severity levels are, in increasing order of severity, Informational, Warning, Minor, Major, and Critical.
		This parameter is useful when you want the NetScaler appliance to send trap messages to a trap listener on the basis of severity level. Trap messages with a severity level lower than the specified level (in the trap listener entry) are not sent.<br/>Default value: Unknown<br/>Possible values = Critical, Major, Minor, Warning, Informational.
		"""
		try :
			return self._severity
		except Exception as e:
			raise e

	@severity.setter
	def severity(self, severity) :
		ur"""Severity level assigned to trap messages generated by this alarm. The severity levels are, in increasing order of severity, Informational, Warning, Minor, Major, and Critical.
		This parameter is useful when you want the NetScaler appliance to send trap messages to a trap listener on the basis of severity level. Trap messages with a severity level lower than the specified level (in the trap listener entry) are not sent.<br/>Default value: Unknown<br/>Possible values = Critical, Major, Minor, Warning, Informational
		"""
		try :
			self._severity = severity
		except Exception as e:
			raise e

	@property
	def logging(self) :
		ur"""Logging status of the alarm. When logging is enabled, the NetScaler appliance logs every trap message that is generated for this alarm.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._logging
		except Exception as e:
			raise e

	@logging.setter
	def logging(self, logging) :
		ur"""Logging status of the alarm. When logging is enabled, the NetScaler appliance logs every trap message that is generated for this alarm.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._logging = logging
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		ur"""If DB is enabled and clear config is fired, then to reset timeinterval of alarm, corresponding default time value is needed. This hidden argument holds the default time value for the corresponding alarm.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmpalarm_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmpalarm
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.trapname is not None :
				return str(self.trapname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update snmpalarm.
		"""
		try :
			if type(resource) is not list :
				updateresource = snmpalarm()
				updateresource.trapname = resource.trapname
				updateresource.thresholdvalue = resource.thresholdvalue
				updateresource.normalvalue = resource.normalvalue
				updateresource.time = resource.time
				updateresource.state = resource.state
				updateresource.severity = resource.severity
				updateresource.logging = resource.logging
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ snmpalarm() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].trapname = resource[i].trapname
						updateresources[i].thresholdvalue = resource[i].thresholdvalue
						updateresources[i].normalvalue = resource[i].normalvalue
						updateresources[i].time = resource[i].time
						updateresources[i].state = resource[i].state
						updateresources[i].severity = resource[i].severity
						updateresources[i].logging = resource[i].logging
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of snmpalarm resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = snmpalarm()
				if type(resource) !=  type(unsetresource):
					unsetresource.trapname = resource
				else :
					unsetresource.trapname = resource.trapname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ snmpalarm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].trapname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ snmpalarm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].trapname = resource[i].trapname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		ur""" Use this API to enable snmpalarm.
		"""
		try :
			if type(resource) is not list :
				enableresource = snmpalarm()
				if type(resource) !=  type(enableresource):
					enableresource.trapname = resource
				else :
					enableresource.trapname = resource.trapname
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ snmpalarm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].trapname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ snmpalarm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].trapname = resource[i].trapname
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		ur""" Use this API to disable snmpalarm.
		"""
		try :
			if type(resource) is not list :
				disableresource = snmpalarm()
				if type(resource) !=  type(disableresource):
					disableresource.trapname = resource
				else :
					disableresource.trapname = resource.trapname
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ snmpalarm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].trapname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ snmpalarm() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].trapname = resource[i].trapname
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the snmpalarm resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = snmpalarm()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = snmpalarm()
						obj.trapname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [snmpalarm() for _ in range(len(name))]
							obj = [snmpalarm() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = snmpalarm()
								obj[i].trapname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of snmpalarm resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpalarm()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the snmpalarm resources configured on NetScaler.
		"""
		try :
			obj = snmpalarm()
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
		ur""" Use this API to count filtered the set of snmpalarm resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = snmpalarm()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Trapname:
		CPU_USAGE = "CPU-USAGE"
		AVERAGE_CPU = "AVERAGE-CPU"
		MEMORY = "MEMORY"
		MGMT_CPU_USAGE = "MGMT-CPU-USAGE"
		SYNFLOOD = "SYNFLOOD"
		VSERVER_REQRATE = "VSERVER-REQRATE"
		SERVICE_REQRATE = "SERVICE-REQRATE"
		ENTITY_RXRATE = "ENTITY-RXRATE"
		ENTITY_TXRATE = "ENTITY-TXRATE"
		ENTITY_SYNFLOOD = "ENTITY-SYNFLOOD"
		SERVICE_MAXCLIENTS = "SERVICE-MAXCLIENTS"
		HA_STATE_CHANGE = "HA-STATE-CHANGE"
		ENTITY_STATE = "ENTITY-STATE"
		CONFIG_CHANGE = "CONFIG-CHANGE"
		CONFIG_SAVE = "CONFIG-SAVE"
		SERVICEGROUP_MEMBER_REQRATE = "SERVICEGROUP-MEMBER-REQRATE"
		SERVICEGROUP_MEMBER_MAXCLIENTS = "SERVICEGROUP-MEMBER-MAXCLIENTS"
		MONITOR_RTO_THRESHOLD = "MONITOR-RTO-THRESHOLD"
		LOGIN_FAILURE = "LOGIN-FAILURE"
		SSL_CERT_EXPIRY = "SSL-CERT-EXPIRY"
		FAN_SPEED_LOW = "FAN-SPEED-LOW"
		VOLTAGE_LOW = "VOLTAGE-LOW"
		VOLTAGE_HIGH = "VOLTAGE-HIGH"
		TEMPERATURE_HIGH = "TEMPERATURE-HIGH"
		CPU_TEMPERATURE_HIGH = "CPU-TEMPERATURE-HIGH"
		POWER_SUPPLY_FAILURE = "POWER-SUPPLY-FAILURE"
		DISK_USAGE_HIGH = "DISK-USAGE-HIGH"
		INTERFACE_THROUGHPUT_LOW = "INTERFACE-THROUGHPUT-LOW"
		MON_PROBE_FAILED = "MON_PROBE_FAILED"
		HA_VERSION_MISMATCH = "HA-VERSION-MISMATCH"
		HA_SYNC_FAILURE = "HA-SYNC-FAILURE"
		HA_NO_HEARTBEATS = "HA-NO-HEARTBEATS"
		HA_BAD_SECONDARY_STATE = "HA-BAD-SECONDARY-STATE"
		INTERFACE_BW_USAGE = "INTERFACE-BW-USAGE"
		RATE_LIMIT_THRESHOLD_EXCEEDED = "RATE-LIMIT-THRESHOLD-EXCEEDED"
		ENTITY_NAME_CHANGE = "ENTITY-NAME-CHANGE"
		HA_PROP_FAILURE = "HA-PROP-FAILURE"
		IP_CONFLICT = "IP-CONFLICT"
		PF_RL_RATE_THRESHOLD = "PF-RL-RATE-THRESHOLD"
		PF_RL_PPS_THRESHOLD = "PF-RL-PPS-THRESHOLD"
		PF_RL_RATE_PKTS_DROPPED = "PF-RL-RATE-PKTS-DROPPED"
		PF_RL_PPS_PKTS_DROPPED = "PF-RL-PPS-PKTS-DROPPED"
		APPFW_START_URL = "APPFW-START-URL"
		APPFW_DENY_URL = "APPFW-DENY-URL"
		APPFW_VIOLATIONS_TYPE = "APPFW-VIOLATIONS-TYPE"
		APPFW_REFERER_HEADER = "APPFW-REFERER-HEADER"
		APPFW_CSRF_TAG = "APPFW-CSRF-TAG"
		APPFW_COOKIE = "APPFW-COOKIE"
		APPFW_FIELD_CONSISTENCY = "APPFW-FIELD-CONSISTENCY"
		APPFW_BUFFER_OVERFLOW = "APPFW-BUFFER-OVERFLOW"
		APPFW_FIELD_FORMAT = "APPFW-FIELD-FORMAT"
		APPFW_SAFE_COMMERCE = "APPFW-SAFE-COMMERCE"
		APPFW_SAFE_OBJECT = "APPFW-SAFE-OBJECT"
		APPFW_POLICY_HIT = "APPFW-POLICY-HIT"
		APPFW_XSS = "APPFW-XSS"
		APPFW_XML_XSS = "APPFW-XML-XSS"
		APPFW_SQL = "APPFW-SQL"
		APPFW_XML_SQL = "APPFW-XML-SQL"
		APPFW_XML_ATTACHMENT = "APPFW-XML-ATTACHMENT"
		APPFW_XML_DOS = "APPFW-XML-DOS"
		APPFW_XML_VALIDATION = "APPFW-XML-VALIDATION"
		APPFW_XML_WSI = "APPFW-XML-WSI"
		APPFW_XML_SCHEMA_COMPILE = "APPFW-XML-SCHEMA-COMPILE"
		APPFW_XML_SOAP_FAULT = "APPFW-XML-SOAP-FAULT"
		DNSKEY_EXPIRY = "DNSKEY-EXPIRY"
		HA_LICENSE_MISMATCH = "HA-LICENSE-MISMATCH"
		SSL_CARD_FAILED = "SSL-CARD-FAILED"
		SSL_CARD_NORMAL = "SSL-CARD-NORMAL"
		WARM_RESTART_EVENT = "WARM-RESTART-EVENT"
		HARD_DISK_DRIVE_ERRORS = "HARD-DISK-DRIVE-ERRORS"
		COMPACT_FLASH_ERRORS = "COMPACT-FLASH-ERRORS"
		CALLHOME_UPLOAD_EVENT = "CALLHOME-UPLOAD-EVENT"
		_1024KEY_EXCHANGE_RATE = "1024KEY-EXCHANGE-RATE"
		_2048KEY_EXCHANGE_RATE = "2048KEY-EXCHANGE-RATE"
		_4096KEY_EXCHANGE_RATE = "4096KEY-EXCHANGE-RATE"
		SSL_CUR_SESSION_INUSE = "SSL-CUR-SESSION-INUSE"
		CLUSTER_NODE_HEALTH = "CLUSTER-NODE-HEALTH"
		CLUSTER_NODE_QUORUM = "CLUSTER-NODE-QUORUM"
		CLUSTER_VERSION_MISMATCH = "CLUSTER-VERSION-MISMATCH"
		CLUSTER_CCO_CHANGE = "CLUSTER-CCO-CHANGE"
		CLUSTER_OVS_CHANGE = "CLUSTER-OVS-CHANGE"
		CLUSTER_SYNC_FAILURE = "CLUSTER-SYNC-FAILURE"
		CLUSTER_PROP_FAILURE = "CLUSTER-PROP-FAILURE"
		HA_STICKY_PRIMARY = "HA-STICKY-PRIMARY"
		INBAND_PROTOCOL_VERSION_MISMATCH = "INBAND-PROTOCOL-VERSION-MISMATCH"
		SSL_CHIP_REINIT = "SSL-CHIP-REINIT"
		VRID_STATE_CHANGE = "VRID-STATE-CHANGE"
		PORT_ALLOC_FAILED = "PORT-ALLOC-FAILED"
		LLDP_REMOTE_CHANGE = "LLDP-REMOTE-CHANGE"
		DUPLICATE_IPV6 = "DUPLICATE-IPV6"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Severity:
		Critical = "Critical"
		Major = "Major"
		Minor = "Minor"
		Warning = "Warning"
		Informational = "Informational"

	class Logging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class snmpalarm_response(base_response) :
	def __init__(self, length=1) :
		self.snmpalarm = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmpalarm = [snmpalarm() for _ in range(length)]

