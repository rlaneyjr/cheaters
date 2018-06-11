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

class clusterfiles(base_resource) :
	""" Configuration for files resource. """
	def __init__(self) :
		self._mode = []

	@property
	def mode(self) :
		ur"""The directories and files to be synchronized. The available settings function as follows:
		Mode    Paths
		all           /nsconfig/ssl/
		/var/netscaler/ssl/
		/var/vpn/bookmark/
		/nsconfig/dns/
		/nsconfig/htmlinjection/
		/netscaler/htmlinjection/ens/
		/nsconfig/monitors/
		/nsconfig/nstemplates/
		/nsconfig/ssh/
		/nsconfig/rc.netscaler
		/nsconfig/resolv.conf
		/nsconfig/inetd.conf
		/nsconfig/syslog.conf
		/nsconfig/snmpd.conf
		/nsconfig/ntp.conf
		/nsconfig/httpd.conf
		/nsconfig/sshd_config
		/nsconfig/hosts
		/nsconfig/enckey
		/var/nslw.bin/etc/krb5.conf
		/var/nslw.bin/etc/krb5.keytab
		/var/lib/likewise/db/
		/var/download/
		/var/wi/tomcat/webapps/
		/var/wi/tomcat/conf/Catalina/localhost/
		/var/wi/java_home/lib/security/cacerts
		/var/wi/java_home/jre/lib/security/cacerts
		/var/netscaler/locdb/
		ssl            /nsconfig/ssl/
		/var/netscaler/ssl/
		bookmarks     /var/vpn/bookmark/
		dns                  /nsconfig/dns/
		htmlinjection    /nsconfig/htmlinjection/
		imports          /var/download/
		misc               /nsconfig/license/
		/nsconfig/rc.conf
		all_plus_misc    Includes *all* files and /nsconfig/license/ and /nsconfig/rc.conf.
		Default value: all.<br/>Possible values = all, bookmarks, ssl, htmlinjection, imports, misc, dns, krb, all_plus_misc, all_minus_misc.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		ur"""The directories and files to be synchronized. The available settings function as follows:
		Mode    Paths
		all           /nsconfig/ssl/
		/var/netscaler/ssl/
		/var/vpn/bookmark/
		/nsconfig/dns/
		/nsconfig/htmlinjection/
		/netscaler/htmlinjection/ens/
		/nsconfig/monitors/
		/nsconfig/nstemplates/
		/nsconfig/ssh/
		/nsconfig/rc.netscaler
		/nsconfig/resolv.conf
		/nsconfig/inetd.conf
		/nsconfig/syslog.conf
		/nsconfig/snmpd.conf
		/nsconfig/ntp.conf
		/nsconfig/httpd.conf
		/nsconfig/sshd_config
		/nsconfig/hosts
		/nsconfig/enckey
		/var/nslw.bin/etc/krb5.conf
		/var/nslw.bin/etc/krb5.keytab
		/var/lib/likewise/db/
		/var/download/
		/var/wi/tomcat/webapps/
		/var/wi/tomcat/conf/Catalina/localhost/
		/var/wi/java_home/lib/security/cacerts
		/var/wi/java_home/jre/lib/security/cacerts
		/var/netscaler/locdb/
		ssl            /nsconfig/ssl/
		/var/netscaler/ssl/
		bookmarks     /var/vpn/bookmark/
		dns                  /nsconfig/dns/
		htmlinjection    /nsconfig/htmlinjection/
		imports          /var/download/
		misc               /nsconfig/license/
		/nsconfig/rc.conf
		all_plus_misc    Includes *all* files and /nsconfig/license/ and /nsconfig/rc.conf.
		Default value: all.<br/>Possible values = all, bookmarks, ssl, htmlinjection, imports, misc, dns, krb, all_plus_misc, all_minus_misc
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusterfiles_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusterfiles
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
		ur""" Use this API to sync clusterfiles.
		"""
		try :
			if type(resource) is not list :
				syncresource = clusterfiles()
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

class clusterfiles_response(base_response) :
	def __init__(self, length=1) :
		self.clusterfiles = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusterfiles = [clusterfiles() for _ in range(length)]

