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

class cspolicylabel(base_resource) :
	""" Configuration for CS policy label resource. """
	def __init__(self) :
		self._labelname = ""
		self._cspolicylabeltype = ""
		self._newname = ""
		self._numpol = 0
		self._hits = 0
		self._policyname = ""
		self._priority = 0
		self._targetvserver = ""
		self._gotopriorityexpression = ""
		self._labeltype = ""
		self._invoke_labelname = ""
		self.___count = 0

	@property
	def labelname(self) :
		ur"""Name for the policy label. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		The label name must be unique within the list of policy labels for content switching.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, \"my label\" or \'my policylabel\').
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name for the policy label. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		The label name must be unique within the list of policy labels for content switching.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, \"my label\" or \'my policylabel\').
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def cspolicylabeltype(self) :
		ur"""Protocol supported by the policy label. All policies bound to the policy label must either match the specified protocol or be a subtype of that protocol. Available settings function as follows:
		* HTTP - Supports policies that process HTTP traffic. Used to access unencrypted Web sites. (The default.)
		* SSL - Supports policies that process HTTPS/SSL encrypted traffic. Used to access encrypted Web sites.
		* TCP - Supports policies that process any type of TCP traffic, including HTTP.
		* SSL_TCP - Supports policies that process SSL-encrypted TCP traffic, including SSL.
		* UDP - Supports policies that process any type of UDP-based traffic, including DNS.
		* DNS - Supports policies that process DNS traffic.
		* ANY - Supports all types of policies except HTTP, SSL, and TCP.             
		* SIP_UDP - Supports policies that process UDP based Session Initiation Protocol (SIP) traffic. SIP initiates, manages, and terminates multimedia communications sessions, and has emerged as the standard for Internet telephony (VoIP).
		* RTSP - Supports policies that process Real Time Streaming Protocol (RTSP) traffic. RTSP provides delivery of multimedia and other streaming data, such as audio, video, and other types of streamed media.
		* RADIUS - Supports policies that process Remote Authentication Dial In User Service (RADIUS) traffic. RADIUS supports combined authentication, authorization, and auditing services for network management.
		* MYSQL - Supports policies that process MYSQL traffic.
		* MSSQL - Supports policies that process Microsoft SQL traffic.<br/>Possible values = HTTP, TCP, RTSP, SSL, SSL_TCP, UDP, DNS, SIP_UDP, ANY, RADIUS, RDP, MYSQL, MSSQL, ORACLE, DIAMETER, SSL_DIAMETER, FTP, DNS_TCP.
		"""
		try :
			return self._cspolicylabeltype
		except Exception as e:
			raise e

	@cspolicylabeltype.setter
	def cspolicylabeltype(self, cspolicylabeltype) :
		ur"""Protocol supported by the policy label. All policies bound to the policy label must either match the specified protocol or be a subtype of that protocol. Available settings function as follows:
		* HTTP - Supports policies that process HTTP traffic. Used to access unencrypted Web sites. (The default.)
		* SSL - Supports policies that process HTTPS/SSL encrypted traffic. Used to access encrypted Web sites.
		* TCP - Supports policies that process any type of TCP traffic, including HTTP.
		* SSL_TCP - Supports policies that process SSL-encrypted TCP traffic, including SSL.
		* UDP - Supports policies that process any type of UDP-based traffic, including DNS.
		* DNS - Supports policies that process DNS traffic.
		* ANY - Supports all types of policies except HTTP, SSL, and TCP.             
		* SIP_UDP - Supports policies that process UDP based Session Initiation Protocol (SIP) traffic. SIP initiates, manages, and terminates multimedia communications sessions, and has emerged as the standard for Internet telephony (VoIP).
		* RTSP - Supports policies that process Real Time Streaming Protocol (RTSP) traffic. RTSP provides delivery of multimedia and other streaming data, such as audio, video, and other types of streamed media.
		* RADIUS - Supports policies that process Remote Authentication Dial In User Service (RADIUS) traffic. RADIUS supports combined authentication, authorization, and auditing services for network management.
		* MYSQL - Supports policies that process MYSQL traffic.
		* MSSQL - Supports policies that process Microsoft SQL traffic.<br/>Possible values = HTTP, TCP, RTSP, SSL, SSL_TCP, UDP, DNS, SIP_UDP, ANY, RADIUS, RDP, MYSQL, MSSQL, ORACLE, DIAMETER, SSL_DIAMETER, FTP, DNS_TCP
		"""
		try :
			self._cspolicylabeltype = cspolicylabeltype
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""The new name of the content switching policylabel.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""The new name of the content switching policylabel.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		ur"""number of polices bound to label.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Number of times policy label was invoked.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		ur"""Name of the content switching policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Specifies the priority of the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def targetvserver(self) :
		ur"""Name of the virtual server to which to forward requests that match the policy.
		"""
		try :
			return self._targetvserver
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of policy label invocation.<br/>Possible values = policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def invoke_labelname(self) :
		ur"""Name of the label to invoke if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._invoke_labelname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cspolicylabel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cspolicylabel
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.labelname is not None :
				return str(self.labelname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add cspolicylabel.
		"""
		try :
			if type(resource) is not list :
				addresource = cspolicylabel()
				addresource.labelname = resource.labelname
				addresource.cspolicylabeltype = resource.cspolicylabeltype
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ cspolicylabel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].labelname = resource[i].labelname
						addresources[i].cspolicylabeltype = resource[i].cspolicylabeltype
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete cspolicylabel.
		"""
		try :
			if type(resource) is not list :
				deleteresource = cspolicylabel()
				if type(resource) !=  type(deleteresource):
					deleteresource.labelname = resource
				else :
					deleteresource.labelname = resource.labelname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ cspolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ cspolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i].labelname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_labelname) :
		ur""" Use this API to rename a cspolicylabel resource.
		"""
		try :
			renameresource = cspolicylabel()
			if type(resource) == cls :
				renameresource.labelname = resource.labelname
			else :
				renameresource.labelname = resource
			return renameresource.rename_resource(client,new_labelname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the cspolicylabel resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cspolicylabel()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = cspolicylabel()
						obj.labelname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [cspolicylabel() for _ in range(len(name))]
							obj = [cspolicylabel() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = cspolicylabel()
								obj[i].labelname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of cspolicylabel resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicylabel()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the cspolicylabel resources configured on NetScaler.
		"""
		try :
			obj = cspolicylabel()
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
		ur""" Use this API to count filtered the set of cspolicylabel resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cspolicylabel()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Cspolicylabeltype:
		HTTP = "HTTP"
		TCP = "TCP"
		RTSP = "RTSP"
		SSL = "SSL"
		SSL_TCP = "SSL_TCP"
		UDP = "UDP"
		DNS = "DNS"
		SIP_UDP = "SIP_UDP"
		ANY = "ANY"
		RADIUS = "RADIUS"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		FTP = "FTP"
		DNS_TCP = "DNS_TCP"

	class Labeltype:
		policylabel = "policylabel"

class cspolicylabel_response(base_response) :
	def __init__(self, length=1) :
		self.cspolicylabel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cspolicylabel = [cspolicylabel() for _ in range(length)]

