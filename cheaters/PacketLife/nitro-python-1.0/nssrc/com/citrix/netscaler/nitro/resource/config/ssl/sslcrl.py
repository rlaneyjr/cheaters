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

class sslcrl(base_resource) :
	""" Configuration for Certificate Revocation List resource. """
	def __init__(self) :
		self._crlname = ""
		self._crlpath = ""
		self._inform = ""
		self._refresh = ""
		self._cacert = ""
		self._method = ""
		self._server = ""
		self._url = ""
		self._port = 0
		self._basedn = ""
		self._scope = ""
		self._interval = ""
		self._day = 0
		self._time = ""
		self._binddn = ""
		self._password = ""
		self._binary = ""
		self._cacertfile = ""
		self._cakeyfile = ""
		self._indexfile = ""
		self._revoke = ""
		self._gencrl = ""
		self._flags = 0
		self._lastupdatetime = 0
		self._version = 0
		self._signaturealgo = ""
		self._issuer = ""
		self._lastupdate = ""
		self._nextupdate = ""
		self._daystoexpiration = 0
		self.___count = 0

	@property
	def crlname(self) :
		ur"""Name for the Certificate Revocation List (CRL). Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the CRL is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my crl" or 'my crl').<br/>Minimum length =  1.
		"""
		try :
			return self._crlname
		except Exception as e:
			raise e

	@crlname.setter
	def crlname(self, crlname) :
		ur"""Name for the Certificate Revocation List (CRL). Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the CRL is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my crl" or 'my crl').<br/>Minimum length =  1
		"""
		try :
			self._crlname = crlname
		except Exception as e:
			raise e

	@property
	def crlpath(self) :
		ur"""Path to the CRL file. /var/netscaler/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._crlpath
		except Exception as e:
			raise e

	@crlpath.setter
	def crlpath(self, crlpath) :
		ur"""Path to the CRL file. /var/netscaler/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._crlpath = crlpath
		except Exception as e:
			raise e

	@property
	def inform(self) :
		ur"""Input format of the CRL file. The two formats supported on the appliance are:
		PEM - Privacy Enhanced Mail.
		DER - Distinguished Encoding Rule.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._inform
		except Exception as e:
			raise e

	@inform.setter
	def inform(self, inform) :
		ur"""Input format of the CRL file. The two formats supported on the appliance are:
		PEM - Privacy Enhanced Mail.
		DER - Distinguished Encoding Rule.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._inform = inform
		except Exception as e:
			raise e

	@property
	def refresh(self) :
		ur"""Set CRL auto refresh.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._refresh
		except Exception as e:
			raise e

	@refresh.setter
	def refresh(self, refresh) :
		ur"""Set CRL auto refresh.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._refresh = refresh
		except Exception as e:
			raise e

	@property
	def cacert(self) :
		ur"""CA certificate that has issued the CRL. Required if CRL Auto Refresh is selected. Install the CA certificate on the appliance before adding the CRL.<br/>Minimum length =  1.
		"""
		try :
			return self._cacert
		except Exception as e:
			raise e

	@cacert.setter
	def cacert(self, cacert) :
		ur"""CA certificate that has issued the CRL. Required if CRL Auto Refresh is selected. Install the CA certificate on the appliance before adding the CRL.<br/>Minimum length =  1
		"""
		try :
			self._cacert = cacert
		except Exception as e:
			raise e

	@property
	def method(self) :
		ur"""Method for CRL refresh. If LDAP is selected, specify the method, CA certificate, base DN, port, and LDAP server name. If HTTP is selected, specify the CA certificate, method, URL, and port. Cannot be changed after a CRL is added.<br/>Possible values = HTTP, LDAP.
		"""
		try :
			return self._method
		except Exception as e:
			raise e

	@method.setter
	def method(self, method) :
		ur"""Method for CRL refresh. If LDAP is selected, specify the method, CA certificate, base DN, port, and LDAP server name. If HTTP is selected, specify the CA certificate, method, URL, and port. Cannot be changed after a CRL is added.<br/>Possible values = HTTP, LDAP
		"""
		try :
			self._method = method
		except Exception as e:
			raise e

	@property
	def server(self) :
		ur"""IP address of the LDAP server from which to fetch the CRLs.<br/>Minimum length =  1.
		"""
		try :
			return self._server
		except Exception as e:
			raise e

	@server.setter
	def server(self, server) :
		ur"""IP address of the LDAP server from which to fetch the CRLs.<br/>Minimum length =  1
		"""
		try :
			self._server = server
		except Exception as e:
			raise e

	@property
	def url(self) :
		ur"""URL of the CRL distribution point.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		ur"""URL of the CRL distribution point.
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def port(self) :
		ur"""Port for the LDAP server.<br/>Minimum length =  1.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		ur"""Port for the LDAP server.<br/>Minimum length =  1
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def basedn(self) :
		ur"""Base distinguished name (DN), which is used in an LDAP search to search for a CRL. Citrix recommends searching for the Base DN instead of the Issuer Name from the CA certificate, because the Issuer Name field might not exactly match the LDAP directory structure's DN.<br/>Minimum length =  1.
		"""
		try :
			return self._basedn
		except Exception as e:
			raise e

	@basedn.setter
	def basedn(self, basedn) :
		ur"""Base distinguished name (DN), which is used in an LDAP search to search for a CRL. Citrix recommends searching for the Base DN instead of the Issuer Name from the CA certificate, because the Issuer Name field might not exactly match the LDAP directory structure's DN.<br/>Minimum length =  1
		"""
		try :
			self._basedn = basedn
		except Exception as e:
			raise e

	@property
	def scope(self) :
		ur"""Extent of the search operation on the LDAP server. Available settings function as follows:
		One - One level below Base DN.
		Base - Exactly the same level as Base DN.<br/>Default value: One<br/>Possible values = Base, One.
		"""
		try :
			return self._scope
		except Exception as e:
			raise e

	@scope.setter
	def scope(self, scope) :
		ur"""Extent of the search operation on the LDAP server. Available settings function as follows:
		One - One level below Base DN.
		Base - Exactly the same level as Base DN.<br/>Default value: One<br/>Possible values = Base, One
		"""
		try :
			self._scope = scope
		except Exception as e:
			raise e

	@property
	def interval(self) :
		ur"""CRL refresh interval. Use the NONE setting to unset this parameter.<br/>Possible values = MONTHLY, WEEKLY, DAILY, NONE.
		"""
		try :
			return self._interval
		except Exception as e:
			raise e

	@interval.setter
	def interval(self, interval) :
		ur"""CRL refresh interval. Use the NONE setting to unset this parameter.<br/>Possible values = MONTHLY, WEEKLY, DAILY, NONE
		"""
		try :
			self._interval = interval
		except Exception as e:
			raise e

	@property
	def day(self) :
		ur"""Day on which to refresh the CRL, or, if the Interval parameter is not set, the number of days after which to refresh the CRL. If Interval is set to MONTHLY, specify the date. If Interval is set to WEEKLY, specify the day of the week (for example, Sun=0 and Sat=6). This parameter is not applicable if the Interval is set to DAILY.<br/>Maximum length =  0x1F.
		"""
		try :
			return self._day
		except Exception as e:
			raise e

	@day.setter
	def day(self, day) :
		ur"""Day on which to refresh the CRL, or, if the Interval parameter is not set, the number of days after which to refresh the CRL. If Interval is set to MONTHLY, specify the date. If Interval is set to WEEKLY, specify the day of the week (for example, Sun=0 and Sat=6). This parameter is not applicable if the Interval is set to DAILY.<br/>Maximum length =  0x1F
		"""
		try :
			self._day = day
		except Exception as e:
			raise e

	@property
	def time(self) :
		ur"""Time, in hours (1-24) and minutes (1-60), at which to refresh the CRL.
		"""
		try :
			return self._time
		except Exception as e:
			raise e

	@time.setter
	def time(self, time) :
		ur"""Time, in hours (1-24) and minutes (1-60), at which to refresh the CRL.
		"""
		try :
			self._time = time
		except Exception as e:
			raise e

	@property
	def binddn(self) :
		ur"""Bind distinguished name (DN) to be used to access the CRL object in the LDAP repository if access to the LDAP repository is restricted or anonymous access is not allowed.<br/>Minimum length =  1.
		"""
		try :
			return self._binddn
		except Exception as e:
			raise e

	@binddn.setter
	def binddn(self, binddn) :
		ur"""Bind distinguished name (DN) to be used to access the CRL object in the LDAP repository if access to the LDAP repository is restricted or anonymous access is not allowed.<br/>Minimum length =  1
		"""
		try :
			self._binddn = binddn
		except Exception as e:
			raise e

	@property
	def password(self) :
		ur"""Password to access the CRL in the LDAP repository if access to the LDAP repository is restricted or anonymous access is not allowed.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		ur"""Password to access the CRL in the LDAP repository if access to the LDAP repository is restricted or anonymous access is not allowed.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def binary(self) :
		ur"""Set the LDAP-based CRL retrieval mode to binary.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._binary
		except Exception as e:
			raise e

	@binary.setter
	def binary(self, binary) :
		ur"""Set the LDAP-based CRL retrieval mode to binary.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._binary = binary
		except Exception as e:
			raise e

	@property
	def cacertfile(self) :
		ur"""Name of and, optionally, path to the CA certificate file.
		/nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._cacertfile
		except Exception as e:
			raise e

	@cacertfile.setter
	def cacertfile(self, cacertfile) :
		ur"""Name of and, optionally, path to the CA certificate file.
		/nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._cacertfile = cacertfile
		except Exception as e:
			raise e

	@property
	def cakeyfile(self) :
		ur"""Name of and, optionally, path to the CA key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._cakeyfile
		except Exception as e:
			raise e

	@cakeyfile.setter
	def cakeyfile(self, cakeyfile) :
		ur"""Name of and, optionally, path to the CA key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._cakeyfile = cakeyfile
		except Exception as e:
			raise e

	@property
	def indexfile(self) :
		ur"""Name of and, optionally, path to the file containing the serial numbers of all the certificates that are revoked. Revoked certificates are appended to the file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._indexfile
		except Exception as e:
			raise e

	@indexfile.setter
	def indexfile(self, indexfile) :
		ur"""Name of and, optionally, path to the file containing the serial numbers of all the certificates that are revoked. Revoked certificates are appended to the file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._indexfile = indexfile
		except Exception as e:
			raise e

	@property
	def revoke(self) :
		ur"""Name of and, optionally, path to the certificate to be revoked. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._revoke
		except Exception as e:
			raise e

	@revoke.setter
	def revoke(self, revoke) :
		ur"""Name of and, optionally, path to the certificate to be revoked. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._revoke = revoke
		except Exception as e:
			raise e

	@property
	def gencrl(self) :
		ur"""Name of and, optionally, path to the CRL file to be generated. The list of certificates that have been revoked is obtained from the index file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._gencrl
		except Exception as e:
			raise e

	@gencrl.setter
	def gencrl(self, gencrl) :
		ur"""Name of and, optionally, path to the CRL file to be generated. The list of certificates that have been revoked is obtained from the index file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._gencrl = gencrl
		except Exception as e:
			raise e

	@property
	def flags(self) :
		ur"""CRL status flag.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def lastupdatetime(self) :
		ur"""Last CRL refresh time.
		"""
		try :
			return self._lastupdatetime
		except Exception as e:
			raise e

	@property
	def version(self) :
		ur"""CRL version.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@property
	def signaturealgo(self) :
		ur"""Signature algorithm.
		"""
		try :
			return self._signaturealgo
		except Exception as e:
			raise e

	@property
	def issuer(self) :
		ur"""Issuer name.
		"""
		try :
			return self._issuer
		except Exception as e:
			raise e

	@property
	def lastupdate(self) :
		ur"""Last update time.
		"""
		try :
			return self._lastupdate
		except Exception as e:
			raise e

	@property
	def nextupdate(self) :
		ur"""Next update time.
		"""
		try :
			return self._nextupdate
		except Exception as e:
			raise e

	@property
	def daystoexpiration(self) :
		ur"""Number of days remaining for the CRL to expire.
		"""
		try :
			return self._daystoexpiration
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcrl_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcrl
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.crlname is not None :
				return str(self.crlname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add sslcrl.
		"""
		try :
			if type(resource) is not list :
				addresource = sslcrl()
				addresource.crlname = resource.crlname
				addresource.crlpath = resource.crlpath
				addresource.inform = resource.inform
				addresource.refresh = resource.refresh
				addresource.cacert = resource.cacert
				addresource.method = resource.method
				addresource.server = resource.server
				addresource.url = resource.url
				addresource.port = resource.port
				addresource.basedn = resource.basedn
				addresource.scope = resource.scope
				addresource.interval = resource.interval
				addresource.day = resource.day
				addresource.time = resource.time
				addresource.binddn = resource.binddn
				addresource.password = resource.password
				addresource.binary = resource.binary
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslcrl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].crlname = resource[i].crlname
						addresources[i].crlpath = resource[i].crlpath
						addresources[i].inform = resource[i].inform
						addresources[i].refresh = resource[i].refresh
						addresources[i].cacert = resource[i].cacert
						addresources[i].method = resource[i].method
						addresources[i].server = resource[i].server
						addresources[i].url = resource[i].url
						addresources[i].port = resource[i].port
						addresources[i].basedn = resource[i].basedn
						addresources[i].scope = resource[i].scope
						addresources[i].interval = resource[i].interval
						addresources[i].day = resource[i].day
						addresources[i].time = resource[i].time
						addresources[i].binddn = resource[i].binddn
						addresources[i].password = resource[i].password
						addresources[i].binary = resource[i].binary
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def create(cls, client, resource) :
		ur""" Use this API to create sslcrl.
		"""
		try :
			if type(resource) is not list :
				createresource = sslcrl()
				createresource.cacertfile = resource.cacertfile
				createresource.cakeyfile = resource.cakeyfile
				createresource.indexfile = resource.indexfile
				createresource.revoke = resource.revoke
				createresource.gencrl = resource.gencrl
				createresource.password = resource.password
				return createresource.perform_operation(client,"create")
			else :
				if (resource and len(resource) > 0) :
					createresources = [ sslcrl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						createresources[i].cacertfile = resource[i].cacertfile
						createresources[i].cakeyfile = resource[i].cakeyfile
						createresources[i].indexfile = resource[i].indexfile
						createresources[i].revoke = resource[i].revoke
						createresources[i].gencrl = resource[i].gencrl
						createresources[i].password = resource[i].password
				result = cls.perform_operation_bulk_request(client, createresources,"create")
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete sslcrl.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslcrl()
				if type(resource) !=  type(deleteresource):
					deleteresource.crlname = resource
				else :
					deleteresource.crlname = resource.crlname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslcrl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].crlname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslcrl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].crlname = resource[i].crlname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update sslcrl.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslcrl()
				updateresource.crlname = resource.crlname
				updateresource.refresh = resource.refresh
				updateresource.cacert = resource.cacert
				updateresource.server = resource.server
				updateresource.method = resource.method
				updateresource.url = resource.url
				updateresource.port = resource.port
				updateresource.basedn = resource.basedn
				updateresource.scope = resource.scope
				updateresource.interval = resource.interval
				updateresource.day = resource.day
				updateresource.time = resource.time
				updateresource.binddn = resource.binddn
				updateresource.password = resource.password
				updateresource.binary = resource.binary
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslcrl() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].crlname = resource[i].crlname
						updateresources[i].refresh = resource[i].refresh
						updateresources[i].cacert = resource[i].cacert
						updateresources[i].server = resource[i].server
						updateresources[i].method = resource[i].method
						updateresources[i].url = resource[i].url
						updateresources[i].port = resource[i].port
						updateresources[i].basedn = resource[i].basedn
						updateresources[i].scope = resource[i].scope
						updateresources[i].interval = resource[i].interval
						updateresources[i].day = resource[i].day
						updateresources[i].time = resource[i].time
						updateresources[i].binddn = resource[i].binddn
						updateresources[i].password = resource[i].password
						updateresources[i].binary = resource[i].binary
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of sslcrl resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslcrl()
				if type(resource) !=  type(unsetresource):
					unsetresource.crlname = resource
				else :
					unsetresource.crlname = resource.crlname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslcrl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].crlname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslcrl() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].crlname = resource[i].crlname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslcrl resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslcrl()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = sslcrl()
						obj.crlname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [sslcrl() for _ in range(len(name))]
							obj = [sslcrl() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = sslcrl()
								obj[i].crlname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of sslcrl resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcrl()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the sslcrl resources configured on NetScaler.
		"""
		try :
			obj = sslcrl()
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
		ur""" Use this API to count filtered the set of sslcrl resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcrl()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Refresh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Scope:
		Base = "Base"
		One = "One"

	class Binary:
		YES = "YES"
		NO = "NO"

	class Interval:
		MONTHLY = "MONTHLY"
		WEEKLY = "WEEKLY"
		DAILY = "DAILY"
		NONE = "NONE"

	class Method:
		HTTP = "HTTP"
		LDAP = "LDAP"

	class Inform:
		DER = "DER"
		PEM = "PEM"

class sslcrl_response(base_response) :
	def __init__(self, length=1) :
		self.sslcrl = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcrl = [sslcrl() for _ in range(length)]

