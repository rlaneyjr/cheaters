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

class aaakcdaccount(base_resource) :
	""" Configuration for Kerberos constrained delegation account resource. """
	def __init__(self) :
		self._kcdaccount = ""
		self._keytab = ""
		self._realmstr = ""
		self._delegateduser = ""
		self._kcdpassword = ""
		self._usercert = ""
		self._cacert = ""
		self._userrealm = ""
		self._enterpriserealm = ""
		self._servicespn = ""
		self._principle = ""
		self._kcdspn = ""
		self.___count = 0

	@property
	def kcdaccount(self) :
		ur"""The name of the KCD account.<br/>Minimum length =  1.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		ur"""The name of the KCD account.<br/>Minimum length =  1
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def keytab(self) :
		ur"""The path to the keytab file. If specified other parameters in this command need not be given.
		"""
		try :
			return self._keytab
		except Exception as e:
			raise e

	@keytab.setter
	def keytab(self, keytab) :
		ur"""The path to the keytab file. If specified other parameters in this command need not be given.
		"""
		try :
			self._keytab = keytab
		except Exception as e:
			raise e

	@property
	def realmstr(self) :
		ur"""Kerberos Realm.
		"""
		try :
			return self._realmstr
		except Exception as e:
			raise e

	@realmstr.setter
	def realmstr(self, realmstr) :
		ur"""Kerberos Realm.
		"""
		try :
			self._realmstr = realmstr
		except Exception as e:
			raise e

	@property
	def delegateduser(self) :
		ur"""Username that can perform kerberos constrained delegation.
		"""
		try :
			return self._delegateduser
		except Exception as e:
			raise e

	@delegateduser.setter
	def delegateduser(self, delegateduser) :
		ur"""Username that can perform kerberos constrained delegation.
		"""
		try :
			self._delegateduser = delegateduser
		except Exception as e:
			raise e

	@property
	def kcdpassword(self) :
		ur"""Password for Delegated User.
		"""
		try :
			return self._kcdpassword
		except Exception as e:
			raise e

	@kcdpassword.setter
	def kcdpassword(self, kcdpassword) :
		ur"""Password for Delegated User.
		"""
		try :
			self._kcdpassword = kcdpassword
		except Exception as e:
			raise e

	@property
	def usercert(self) :
		ur"""SSL Cert (including private key) for Delegated User.
		"""
		try :
			return self._usercert
		except Exception as e:
			raise e

	@usercert.setter
	def usercert(self, usercert) :
		ur"""SSL Cert (including private key) for Delegated User.
		"""
		try :
			self._usercert = usercert
		except Exception as e:
			raise e

	@property
	def cacert(self) :
		ur"""CA Cert for UserCert or when doing PKINIT backchannel.
		"""
		try :
			return self._cacert
		except Exception as e:
			raise e

	@cacert.setter
	def cacert(self, cacert) :
		ur"""CA Cert for UserCert or when doing PKINIT backchannel.
		"""
		try :
			self._cacert = cacert
		except Exception as e:
			raise e

	@property
	def userrealm(self) :
		ur"""Realm of the user.
		"""
		try :
			return self._userrealm
		except Exception as e:
			raise e

	@userrealm.setter
	def userrealm(self, userrealm) :
		ur"""Realm of the user.
		"""
		try :
			self._userrealm = userrealm
		except Exception as e:
			raise e

	@property
	def enterpriserealm(self) :
		ur"""Enterprise Realm of the user. This should be given only in certain KDC deployments where KDC expects Enterprise username instead of Principal Name.
		"""
		try :
			return self._enterpriserealm
		except Exception as e:
			raise e

	@enterpriserealm.setter
	def enterpriserealm(self, enterpriserealm) :
		ur"""Enterprise Realm of the user. This should be given only in certain KDC deployments where KDC expects Enterprise username instead of Principal Name.
		"""
		try :
			self._enterpriserealm = enterpriserealm
		except Exception as e:
			raise e

	@property
	def servicespn(self) :
		ur"""Service SPN. When specified, this will be used to fetch kerberos tickets. If not specified, Netscaler will construct SPN using service fqdn.
		"""
		try :
			return self._servicespn
		except Exception as e:
			raise e

	@servicespn.setter
	def servicespn(self, servicespn) :
		ur"""Service SPN. When specified, this will be used to fetch kerberos tickets. If not specified, Netscaler will construct SPN using service fqdn.
		"""
		try :
			self._servicespn = servicespn
		except Exception as e:
			raise e

	@property
	def principle(self) :
		ur"""SPN extracted from keytab file.
		"""
		try :
			return self._principle
		except Exception as e:
			raise e

	@property
	def kcdspn(self) :
		ur"""Host SPN extracted from keytab file.
		"""
		try :
			return self._kcdspn
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaakcdaccount_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaakcdaccount
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.kcdaccount is not None :
				return str(self.kcdaccount)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add aaakcdaccount.
		"""
		try :
			if type(resource) is not list :
				addresource = aaakcdaccount()
				addresource.kcdaccount = resource.kcdaccount
				addresource.keytab = resource.keytab
				addresource.realmstr = resource.realmstr
				addresource.delegateduser = resource.delegateduser
				addresource.kcdpassword = resource.kcdpassword
				addresource.usercert = resource.usercert
				addresource.cacert = resource.cacert
				addresource.userrealm = resource.userrealm
				addresource.enterpriserealm = resource.enterpriserealm
				addresource.servicespn = resource.servicespn
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ aaakcdaccount() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].kcdaccount = resource[i].kcdaccount
						addresources[i].keytab = resource[i].keytab
						addresources[i].realmstr = resource[i].realmstr
						addresources[i].delegateduser = resource[i].delegateduser
						addresources[i].kcdpassword = resource[i].kcdpassword
						addresources[i].usercert = resource[i].usercert
						addresources[i].cacert = resource[i].cacert
						addresources[i].userrealm = resource[i].userrealm
						addresources[i].enterpriserealm = resource[i].enterpriserealm
						addresources[i].servicespn = resource[i].servicespn
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete aaakcdaccount.
		"""
		try :
			if type(resource) is not list :
				deleteresource = aaakcdaccount()
				if type(resource) !=  type(deleteresource):
					deleteresource.kcdaccount = resource
				else :
					deleteresource.kcdaccount = resource.kcdaccount
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].kcdaccount = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].kcdaccount = resource[i].kcdaccount
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update aaakcdaccount.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaakcdaccount()
				updateresource.kcdaccount = resource.kcdaccount
				updateresource.keytab = resource.keytab
				updateresource.realmstr = resource.realmstr
				updateresource.delegateduser = resource.delegateduser
				updateresource.kcdpassword = resource.kcdpassword
				updateresource.usercert = resource.usercert
				updateresource.cacert = resource.cacert
				updateresource.userrealm = resource.userrealm
				updateresource.enterpriserealm = resource.enterpriserealm
				updateresource.servicespn = resource.servicespn
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ aaakcdaccount() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].kcdaccount = resource[i].kcdaccount
						updateresources[i].keytab = resource[i].keytab
						updateresources[i].realmstr = resource[i].realmstr
						updateresources[i].delegateduser = resource[i].delegateduser
						updateresources[i].kcdpassword = resource[i].kcdpassword
						updateresources[i].usercert = resource[i].usercert
						updateresources[i].cacert = resource[i].cacert
						updateresources[i].userrealm = resource[i].userrealm
						updateresources[i].enterpriserealm = resource[i].enterpriserealm
						updateresources[i].servicespn = resource[i].servicespn
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of aaakcdaccount resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaakcdaccount()
				if type(resource) !=  type(unsetresource):
					unsetresource.kcdaccount = resource
				else :
					unsetresource.kcdaccount = resource.kcdaccount
					unsetresource.keytab = resource.keytab
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].kcdaccount = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].kcdaccount = resource[i].kcdaccount
							unsetresources[i].keytab = resource[i].keytab
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the aaakcdaccount resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaakcdaccount()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = aaakcdaccount()
						obj.kcdaccount = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [aaakcdaccount() for _ in range(len(name))]
							obj = [aaakcdaccount() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = aaakcdaccount()
								obj[i].kcdaccount = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of aaakcdaccount resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaakcdaccount()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the aaakcdaccount resources configured on NetScaler.
		"""
		try :
			obj = aaakcdaccount()
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
		ur""" Use this API to count filtered the set of aaakcdaccount resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaakcdaccount()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class aaakcdaccount_response(base_response) :
	def __init__(self, length=1) :
		self.aaakcdaccount = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaakcdaccount = [aaakcdaccount() for _ in range(length)]

