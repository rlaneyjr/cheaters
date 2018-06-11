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

class hafiles(base_resource) :
	""" Configuration for files resource. """
	def __init__(self) :
		self._mode = []

	@property
	def mode(self) :
		ur"""Specify one of the following modes of synchronization.
		* all - Synchronize files related to system configuration, Access Gateway bookmarks, SSL certificates, SSL CRL lists, HTML injection scripts, and Application Firewall XML objects. 
		* bookmarks - Synchronize all Access Gateway bookmarks.
		* ssl - Synchronize all certificates, keys, and CRLs for the SSL feature. 
		* htmlinjection. Synchronize all scripts configured for the HTML injection feature. 
		* imports. Synchronize all XML objects (for example, WSDLs, schemas, error pages) configured for the application firewall. 
		* misc - Synchronize all license files and the rc.conf file. 
		* all_plus_misc - Synchronize files related to system configuration, Access Gateway bookmarks, SSL certificates, SSL CRL lists, HTML injection scripts, application firewall XML objects, licenses, and the rc.conf file.<br/>Possible values = all, bookmarks, ssl, htmlinjection, imports, misc, dns, krb, all_plus_misc, all_minus_misc.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		ur"""Specify one of the following modes of synchronization.
		* all - Synchronize files related to system configuration, Access Gateway bookmarks, SSL certificates, SSL CRL lists, HTML injection scripts, and Application Firewall XML objects. 
		* bookmarks - Synchronize all Access Gateway bookmarks.
		* ssl - Synchronize all certificates, keys, and CRLs for the SSL feature. 
		* htmlinjection. Synchronize all scripts configured for the HTML injection feature. 
		* imports. Synchronize all XML objects (for example, WSDLs, schemas, error pages) configured for the application firewall. 
		* misc - Synchronize all license files and the rc.conf file. 
		* all_plus_misc - Synchronize files related to system configuration, Access Gateway bookmarks, SSL certificates, SSL CRL lists, HTML injection scripts, application firewall XML objects, licenses, and the rc.conf file.<br/>Possible values = all, bookmarks, ssl, htmlinjection, imports, misc, dns, krb, all_plus_misc, all_minus_misc
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(hafiles_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.hafiles
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
	def sync(cls, client, resource) :
		ur""" Use this API to sync hafiles.
		"""
		try :
			if type(resource) is not list :
				syncresource = hafiles()
				syncresource.mode = resource.mode
				return syncresource.perform_operation(client,"sync")
		except Exception as e :
			raise e

	class Mode:
		all = "all"
		bookmarks = "bookmarks"
		ssl = "ssl"
		htmlinjection = "htmlinjection"
		imports = "imports"
		misc = "misc"
		dns = "dns"
		krb = "krb"
		all_plus_misc = "all_plus_misc"
		all_minus_misc = "all_minus_misc"

class hafiles_response(base_response) :
	def __init__(self, length=1) :
		self.hafiles = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.hafiles = [hafiles() for _ in range(length)]

