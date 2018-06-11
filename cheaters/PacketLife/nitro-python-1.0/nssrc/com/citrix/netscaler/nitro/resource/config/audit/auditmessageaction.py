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

class auditmessageaction(base_resource) :
	""" Configuration for message action resource. """
	def __init__(self) :
		self._name = ""
		self._loglevel = ""
		self._stringbuilderexpr = ""
		self._logtonewnslog = ""
		self._bypasssafetycheck = ""
		self._loglevel1 = ""
		self._hits = 0
		self._undefhits = 0
		self._referencecount = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the audit message action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the message action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my message action" or 'my message action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the audit message action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the message action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my message action" or 'my message action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def loglevel(self) :
		ur"""Audit log level, which specifies the severity level of the log message being generated.. 
		The following loglevels are valid: 
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG.
		"""
		try :
			return self._loglevel
		except Exception as e:
			raise e

	@loglevel.setter
	def loglevel(self, loglevel) :
		ur"""Audit log level, which specifies the severity level of the log message being generated.. 
		The following loglevels are valid: 
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG
		"""
		try :
			self._loglevel = loglevel
		except Exception as e:
			raise e

	@property
	def stringbuilderexpr(self) :
		ur"""Default-syntax expression that defines the format and content of the log message.
		"""
		try :
			return self._stringbuilderexpr
		except Exception as e:
			raise e

	@stringbuilderexpr.setter
	def stringbuilderexpr(self, stringbuilderexpr) :
		ur"""Default-syntax expression that defines the format and content of the log message.
		"""
		try :
			self._stringbuilderexpr = stringbuilderexpr
		except Exception as e:
			raise e

	@property
	def logtonewnslog(self) :
		ur"""Send the message to the new nslog.<br/>Possible values = YES, NO.
		"""
		try :
			return self._logtonewnslog
		except Exception as e:
			raise e

	@logtonewnslog.setter
	def logtonewnslog(self, logtonewnslog) :
		ur"""Send the message to the new nslog.<br/>Possible values = YES, NO
		"""
		try :
			self._logtonewnslog = logtonewnslog
		except Exception as e:
			raise e

	@property
	def bypasssafetycheck(self) :
		ur"""Bypass the safety check and allow unsafe expressions.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._bypasssafetycheck
		except Exception as e:
			raise e

	@bypasssafetycheck.setter
	def bypasssafetycheck(self, bypasssafetycheck) :
		ur"""Bypass the safety check and allow unsafe expressions.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._bypasssafetycheck = bypasssafetycheck
		except Exception as e:
			raise e

	@property
	def loglevel1(self) :
		ur""".<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE.
		"""
		try :
			return self._loglevel1
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The number of times the action has been taken.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		ur"""The number of times the action resulted in UNDEF.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		ur"""The number of references to the action.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(auditmessageaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.auditmessageaction
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
		ur""" Use this API to add auditmessageaction.
		"""
		try :
			if type(resource) is not list :
				addresource = auditmessageaction()
				addresource.name = resource.name
				addresource.loglevel = resource.loglevel
				addresource.stringbuilderexpr = resource.stringbuilderexpr
				addresource.logtonewnslog = resource.logtonewnslog
				addresource.bypasssafetycheck = resource.bypasssafetycheck
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ auditmessageaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].loglevel = resource[i].loglevel
						addresources[i].stringbuilderexpr = resource[i].stringbuilderexpr
						addresources[i].logtonewnslog = resource[i].logtonewnslog
						addresources[i].bypasssafetycheck = resource[i].bypasssafetycheck
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete auditmessageaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = auditmessageaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ auditmessageaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ auditmessageaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update auditmessageaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = auditmessageaction()
				updateresource.name = resource.name
				updateresource.loglevel = resource.loglevel
				updateresource.stringbuilderexpr = resource.stringbuilderexpr
				updateresource.logtonewnslog = resource.logtonewnslog
				updateresource.bypasssafetycheck = resource.bypasssafetycheck
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ auditmessageaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].loglevel = resource[i].loglevel
						updateresources[i].stringbuilderexpr = resource[i].stringbuilderexpr
						updateresources[i].logtonewnslog = resource[i].logtonewnslog
						updateresources[i].bypasssafetycheck = resource[i].bypasssafetycheck
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of auditmessageaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = auditmessageaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ auditmessageaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ auditmessageaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the auditmessageaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = auditmessageaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = auditmessageaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [auditmessageaction() for _ in range(len(name))]
							obj = [auditmessageaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = auditmessageaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of auditmessageaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditmessageaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the auditmessageaction resources configured on NetScaler.
		"""
		try :
			obj = auditmessageaction()
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
		ur""" Use this API to count filtered the set of auditmessageaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditmessageaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Loglevel1:
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

	class Logtonewnslog:
		YES = "YES"
		NO = "NO"

	class Loglevel:
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"

	class Bypasssafetycheck:
		YES = "YES"
		NO = "NO"

class auditmessageaction_response(base_response) :
	def __init__(self, length=1) :
		self.auditmessageaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.auditmessageaction = [auditmessageaction() for _ in range(length)]

