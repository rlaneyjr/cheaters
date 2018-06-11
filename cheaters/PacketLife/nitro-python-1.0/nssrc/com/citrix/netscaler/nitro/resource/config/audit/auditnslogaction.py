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

class auditnslogaction(base_resource) :
	""" Configuration for ns log action resource. """
	def __init__(self) :
		self._name = ""
		self._serverip = ""
		self._serverport = 0
		self._loglevel = []
		self._dateformat = ""
		self._logfacility = ""
		self._tcp = ""
		self._acl = ""
		self._timezone = ""
		self._userdefinedauditlog = ""
		self._appflowexport = ""
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the nslog action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the nslog action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my nslog action" or 'my nslog action).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the nslog action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the nslog action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my nslog action" or 'my nslog action).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		ur"""IP address of the nslog server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		ur"""IP address of the nslog server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		ur"""Port on which the nslog server accepts connections.<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		ur"""Port on which the nslog server accepts connections.<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def loglevel(self) :
		ur"""Audit log level, which specifies the types of events to log. 
		Available settings function as follows: 
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.
		* NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE.
		"""
		try :
			return self._loglevel
		except Exception as e:
			raise e

	@loglevel.setter
	def loglevel(self, loglevel) :
		ur"""Audit log level, which specifies the types of events to log. 
		Available settings function as follows: 
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.
		* NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE
		"""
		try :
			self._loglevel = loglevel
		except Exception as e:
			raise e

	@property
	def dateformat(self) :
		ur"""Format of dates in the logs.
		Supported formats are: 
		* MMDDYYYY - U.S. style month/date/year format.
		* DDMMYYYY - European style date/month/year format.
		* YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD.
		"""
		try :
			return self._dateformat
		except Exception as e:
			raise e

	@dateformat.setter
	def dateformat(self, dateformat) :
		ur"""Format of dates in the logs.
		Supported formats are: 
		* MMDDYYYY - U.S. style month/date/year format.
		* DDMMYYYY - European style date/month/year format.
		* YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD
		"""
		try :
			self._dateformat = dateformat
		except Exception as e:
			raise e

	@property
	def logfacility(self) :
		ur"""Facility value, as defined in RFC 3164, assigned to the log message. 
		Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the NetScaler appliance itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7.
		"""
		try :
			return self._logfacility
		except Exception as e:
			raise e

	@logfacility.setter
	def logfacility(self, logfacility) :
		ur"""Facility value, as defined in RFC 3164, assigned to the log message. 
		Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the NetScaler appliance itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7
		"""
		try :
			self._logfacility = logfacility
		except Exception as e:
			raise e

	@property
	def tcp(self) :
		ur"""Log TCP messages.<br/>Possible values = NONE, ALL.
		"""
		try :
			return self._tcp
		except Exception as e:
			raise e

	@tcp.setter
	def tcp(self, tcp) :
		ur"""Log TCP messages.<br/>Possible values = NONE, ALL
		"""
		try :
			self._tcp = tcp
		except Exception as e:
			raise e

	@property
	def acl(self) :
		ur"""Log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._acl
		except Exception as e:
			raise e

	@acl.setter
	def acl(self, acl) :
		ur"""Log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._acl = acl
		except Exception as e:
			raise e

	@property
	def timezone(self) :
		ur"""Time zone used for date and timestamps in the logs. 
		Available settings function as follows: 
		* GMT_TIME. Coordinated Universal Time.
		* LOCAL_TIME. The server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME.
		"""
		try :
			return self._timezone
		except Exception as e:
			raise e

	@timezone.setter
	def timezone(self, timezone) :
		ur"""Time zone used for date and timestamps in the logs. 
		Available settings function as follows: 
		* GMT_TIME. Coordinated Universal Time.
		* LOCAL_TIME. The server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME
		"""
		try :
			self._timezone = timezone
		except Exception as e:
			raise e

	@property
	def userdefinedauditlog(self) :
		ur"""Log user-configurable log messages to nslog.
		Setting this parameter to NO causes auditing to ignore all user-configured message actions. Setting this parameter to YES causes auditing to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO.
		"""
		try :
			return self._userdefinedauditlog
		except Exception as e:
			raise e

	@userdefinedauditlog.setter
	def userdefinedauditlog(self, userdefinedauditlog) :
		ur"""Log user-configurable log messages to nslog.
		Setting this parameter to NO causes auditing to ignore all user-configured message actions. Setting this parameter to YES causes auditing to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO
		"""
		try :
			self._userdefinedauditlog = userdefinedauditlog
		except Exception as e:
			raise e

	@property
	def appflowexport(self) :
		ur"""Export log messages to AppFlow collectors.
		Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowexport
		except Exception as e:
			raise e

	@appflowexport.setter
	def appflowexport(self, appflowexport) :
		ur"""Export log messages to AppFlow collectors.
		Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowexport = appflowexport
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(auditnslogaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.auditnslogaction
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add auditnslogaction.
		"""
		try :
			if type(resource) is not list :
				addresource = auditnslogaction()
				addresource.name = resource.name
				addresource.serverip = resource.serverip
				addresource.serverport = resource.serverport
				addresource.loglevel = resource.loglevel
				addresource.dateformat = resource.dateformat
				addresource.logfacility = resource.logfacility
				addresource.tcp = resource.tcp
				addresource.acl = resource.acl
				addresource.timezone = resource.timezone
				addresource.userdefinedauditlog = resource.userdefinedauditlog
				addresource.appflowexport = resource.appflowexport
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ auditnslogaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].serverip = resource[i].serverip
						addresources[i].serverport = resource[i].serverport
						addresources[i].loglevel = resource[i].loglevel
						addresources[i].dateformat = resource[i].dateformat
						addresources[i].logfacility = resource[i].logfacility
						addresources[i].tcp = resource[i].tcp
						addresources[i].acl = resource[i].acl
						addresources[i].timezone = resource[i].timezone
						addresources[i].userdefinedauditlog = resource[i].userdefinedauditlog
						addresources[i].appflowexport = resource[i].appflowexport
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete auditnslogaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = auditnslogaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ auditnslogaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ auditnslogaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update auditnslogaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = auditnslogaction()
				updateresource.name = resource.name
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.loglevel = resource.loglevel
				updateresource.dateformat = resource.dateformat
				updateresource.logfacility = resource.logfacility
				updateresource.tcp = resource.tcp
				updateresource.acl = resource.acl
				updateresource.timezone = resource.timezone
				updateresource.userdefinedauditlog = resource.userdefinedauditlog
				updateresource.appflowexport = resource.appflowexport
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ auditnslogaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].serverip = resource[i].serverip
						updateresources[i].serverport = resource[i].serverport
						updateresources[i].loglevel = resource[i].loglevel
						updateresources[i].dateformat = resource[i].dateformat
						updateresources[i].logfacility = resource[i].logfacility
						updateresources[i].tcp = resource[i].tcp
						updateresources[i].acl = resource[i].acl
						updateresources[i].timezone = resource[i].timezone
						updateresources[i].userdefinedauditlog = resource[i].userdefinedauditlog
						updateresources[i].appflowexport = resource[i].appflowexport
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of auditnslogaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = auditnslogaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ auditnslogaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ auditnslogaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the auditnslogaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = auditnslogaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = auditnslogaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [auditnslogaction() for _ in range(len(name))]
							obj = [auditnslogaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = auditnslogaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of auditnslogaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditnslogaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the auditnslogaction resources configured on NetScaler.
		"""
		try :
			obj = auditnslogaction()
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
		ur""" Use this API to count filtered the set of auditnslogaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditnslogaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Userdefinedauditlog:
		YES = "YES"
		NO = "NO"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

	class Timezone:
		GMT_TIME = "GMT_TIME"
		LOCAL_TIME = "LOCAL_TIME"

	class Dateformat:
		MMDDYYYY = "MMDDYYYY"
		DDMMYYYY = "DDMMYYYY"
		YYYYMMDD = "YYYYMMDD"

	class Acl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logfacility:
		LOCAL0 = "LOCAL0"
		LOCAL1 = "LOCAL1"
		LOCAL2 = "LOCAL2"
		LOCAL3 = "LOCAL3"
		LOCAL4 = "LOCAL4"
		LOCAL5 = "LOCAL5"
		LOCAL6 = "LOCAL6"
		LOCAL7 = "LOCAL7"

	class Loglevel:
		ALL = "ALL"
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"
		NONE = "NONE"

	class Tcp:
		NONE = "NONE"
		ALL = "ALL"

	class Appflowexport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class auditnslogaction_response(base_response) :
	def __init__(self, length=1) :
		self.auditnslogaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.auditnslogaction = [auditnslogaction() for _ in range(length)]

