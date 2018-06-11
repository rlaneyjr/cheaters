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

class wipackage(base_resource) :
	""" Configuration for Web Interface resource. """
	def __init__(self) :
		self._jre = ""
		self._wi = ""
		self._maxsites = ""

	@property
	def jre(self) :
		ur"""Complete path to the JRE tar file. 
		You can use the Diablo Latte JRE version 1.6.0-7 for 64-bit FreeBSD 6.x/amd64 platform available on the FreeBSD Foundation web site.
		Alternatively, you can use OpenJDK6 package for FreeBSD 6.x/amd63.The Java package can be downloaded from http://ftp.riken.jp/pub/FreeBSD/ports/amd64/packages-6-stable/java/openjdk6-b17_2.tbz or http://www.freebsdfoundation.org/cgi-bin/download?download=diablo-jdk-freebsd6.amd64.1.6.0.07.02.tbz.<br/>Default value: "file://tmp/diablo-jdk-freebsd6.amd64.1.6.0.07.02.tbz"<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._jre
		except Exception as e:
			raise e

	@jre.setter
	def jre(self, jre) :
		ur"""Complete path to the JRE tar file. 
		You can use the Diablo Latte JRE version 1.6.0-7 for 64-bit FreeBSD 6.x/amd64 platform available on the FreeBSD Foundation web site.
		Alternatively, you can use OpenJDK6 package for FreeBSD 6.x/amd63.The Java package can be downloaded from http://ftp.riken.jp/pub/FreeBSD/ports/amd64/packages-6-stable/java/openjdk6-b17_2.tbz or http://www.freebsdfoundation.org/cgi-bin/download?download=diablo-jdk-freebsd6.amd64.1.6.0.07.02.tbz.<br/>Default value: "file://tmp/diablo-jdk-freebsd6.amd64.1.6.0.07.02.tbz"<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._jre = jre
		except Exception as e:
			raise e

	@property
	def wi(self) :
		ur"""Complete path to the Web Interface tar file for installing the Web Interface on the NetScaler appliance. This file includes Apache Tomcat Web server. The file name has the following format: nswi-<version number>.tgz (for example, nswi-1.5.tgz).<br/>Default value: "http://citrix.com/downloads/nswi-1.7.tgz"<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._wi
		except Exception as e:
			raise e

	@wi.setter
	def wi(self, wi) :
		ur"""Complete path to the Web Interface tar file for installing the Web Interface on the NetScaler appliance. This file includes Apache Tomcat Web server. The file name has the following format: nswi-<version number>.tgz (for example, nswi-1.5.tgz).<br/>Default value: "http://citrix.com/downloads/nswi-1.7.tgz"<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._wi = wi
		except Exception as e:
			raise e

	@property
	def maxsites(self) :
		ur"""Maximum number of Web Interface sites that can be created on the NetScaler appliance; changes the amount of RAM reserved for Web Interface usage; changing its value results in restart of Tomcat server and invalidates any existing Web Interface sessions.<br/>Possible values = 3, 25, 50, 100, 200, 500.
		"""
		try :
			return self._maxsites
		except Exception as e:
			raise e

	@maxsites.setter
	def maxsites(self, maxsites) :
		ur"""Maximum number of Web Interface sites that can be created on the NetScaler appliance; changes the amount of RAM reserved for Web Interface usage; changing its value results in restart of Tomcat server and invalidates any existing Web Interface sessions.<br/>Possible values = 3, 25, 50, 100, 200, 500
		"""
		try :
			self._maxsites = maxsites
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wipackage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wipackage
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
	def Install(cls, client, resource) :
		ur""" Use this API to Install wipackage.
		"""
		try :
			if type(resource) is not list :
				Installresource = wipackage()
				Installresource.jre = resource.jre
				Installresource.wi = resource.wi
				Installresource.maxsites = resource.maxsites
				return Installresource.perform_operation(client)
		except Exception as e :
			raise e

	class Maxsites:
		_3 = "3"
		_25 = "25"
		_50 = "50"
		_100 = "100"
		_200 = "200"
		_500 = "500"

class wipackage_response(base_response) :
	def __init__(self, length=1) :
		self.wipackage = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wipackage = [wipackage() for _ in range(length)]

