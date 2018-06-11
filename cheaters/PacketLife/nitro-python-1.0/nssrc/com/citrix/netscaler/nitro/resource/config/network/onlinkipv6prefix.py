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

class onlinkipv6prefix(base_resource) :
	""" Configuration for on-link IPv6 global prefixes for Router Advertisment resource. """
	def __init__(self) :
		self._ipv6prefix = ""
		self._onlinkprefix = ""
		self._autonomusprefix = ""
		self._depricateprefix = ""
		self._decrementprefixlifetimes = ""
		self._prefixvalidelifetime = 0
		self._prefixpreferredlifetime = 0
		self._prefixcurrvalidelft = 0
		self._prefixcurrpreferredlft = 0
		self.___count = 0

	@property
	def ipv6prefix(self) :
		ur"""Onlink prefixes for RA messages.
		"""
		try :
			return self._ipv6prefix
		except Exception as e:
			raise e

	@ipv6prefix.setter
	def ipv6prefix(self, ipv6prefix) :
		ur"""Onlink prefixes for RA messages.
		"""
		try :
			self._ipv6prefix = ipv6prefix
		except Exception as e:
			raise e

	@property
	def onlinkprefix(self) :
		ur"""RA Prefix onlink flag.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._onlinkprefix
		except Exception as e:
			raise e

	@onlinkprefix.setter
	def onlinkprefix(self, onlinkprefix) :
		ur"""RA Prefix onlink flag.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._onlinkprefix = onlinkprefix
		except Exception as e:
			raise e

	@property
	def autonomusprefix(self) :
		ur"""RA Prefix Autonomus flag.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._autonomusprefix
		except Exception as e:
			raise e

	@autonomusprefix.setter
	def autonomusprefix(self, autonomusprefix) :
		ur"""RA Prefix Autonomus flag.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._autonomusprefix = autonomusprefix
		except Exception as e:
			raise e

	@property
	def depricateprefix(self) :
		ur"""Depricate the prefix.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._depricateprefix
		except Exception as e:
			raise e

	@depricateprefix.setter
	def depricateprefix(self, depricateprefix) :
		ur"""Depricate the prefix.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._depricateprefix = depricateprefix
		except Exception as e:
			raise e

	@property
	def decrementprefixlifetimes(self) :
		ur"""RA Prefix Autonomus flag.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._decrementprefixlifetimes
		except Exception as e:
			raise e

	@decrementprefixlifetimes.setter
	def decrementprefixlifetimes(self, decrementprefixlifetimes) :
		ur"""RA Prefix Autonomus flag.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._decrementprefixlifetimes = decrementprefixlifetimes
		except Exception as e:
			raise e

	@property
	def prefixvalidelifetime(self) :
		ur"""Valide life time of the prefix, in seconds.<br/>Default value: 2592000.
		"""
		try :
			return self._prefixvalidelifetime
		except Exception as e:
			raise e

	@prefixvalidelifetime.setter
	def prefixvalidelifetime(self, prefixvalidelifetime) :
		ur"""Valide life time of the prefix, in seconds.<br/>Default value: 2592000
		"""
		try :
			self._prefixvalidelifetime = prefixvalidelifetime
		except Exception as e:
			raise e

	@property
	def prefixpreferredlifetime(self) :
		ur"""Preferred life time of the prefix, in seconds.<br/>Default value: 604800.
		"""
		try :
			return self._prefixpreferredlifetime
		except Exception as e:
			raise e

	@prefixpreferredlifetime.setter
	def prefixpreferredlifetime(self, prefixpreferredlifetime) :
		ur"""Preferred life time of the prefix, in seconds.<br/>Default value: 604800
		"""
		try :
			self._prefixpreferredlifetime = prefixpreferredlifetime
		except Exception as e:
			raise e

	@property
	def prefixcurrvalidelft(self) :
		ur"""Prefix current valid life time.
		"""
		try :
			return self._prefixcurrvalidelft
		except Exception as e:
			raise e

	@property
	def prefixcurrpreferredlft(self) :
		ur"""Prefix current prefered life time.
		"""
		try :
			return self._prefixcurrpreferredlft
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(onlinkipv6prefix_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.onlinkipv6prefix
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ipv6prefix is not None :
				return str(self.ipv6prefix)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add onlinkipv6prefix.
		"""
		try :
			if type(resource) is not list :
				addresource = onlinkipv6prefix()
				addresource.ipv6prefix = resource.ipv6prefix
				addresource.onlinkprefix = resource.onlinkprefix
				addresource.autonomusprefix = resource.autonomusprefix
				addresource.depricateprefix = resource.depricateprefix
				addresource.decrementprefixlifetimes = resource.decrementprefixlifetimes
				addresource.prefixvalidelifetime = resource.prefixvalidelifetime
				addresource.prefixpreferredlifetime = resource.prefixpreferredlifetime
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ onlinkipv6prefix() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ipv6prefix = resource[i].ipv6prefix
						addresources[i].onlinkprefix = resource[i].onlinkprefix
						addresources[i].autonomusprefix = resource[i].autonomusprefix
						addresources[i].depricateprefix = resource[i].depricateprefix
						addresources[i].decrementprefixlifetimes = resource[i].decrementprefixlifetimes
						addresources[i].prefixvalidelifetime = resource[i].prefixvalidelifetime
						addresources[i].prefixpreferredlifetime = resource[i].prefixpreferredlifetime
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete onlinkipv6prefix.
		"""
		try :
			if type(resource) is not list :
				deleteresource = onlinkipv6prefix()
				if type(resource) !=  type(deleteresource):
					deleteresource.ipv6prefix = resource
				else :
					deleteresource.ipv6prefix = resource.ipv6prefix
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ onlinkipv6prefix() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipv6prefix = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ onlinkipv6prefix() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipv6prefix = resource[i].ipv6prefix
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update onlinkipv6prefix.
		"""
		try :
			if type(resource) is not list :
				updateresource = onlinkipv6prefix()
				updateresource.ipv6prefix = resource.ipv6prefix
				updateresource.onlinkprefix = resource.onlinkprefix
				updateresource.autonomusprefix = resource.autonomusprefix
				updateresource.depricateprefix = resource.depricateprefix
				updateresource.decrementprefixlifetimes = resource.decrementprefixlifetimes
				updateresource.prefixvalidelifetime = resource.prefixvalidelifetime
				updateresource.prefixpreferredlifetime = resource.prefixpreferredlifetime
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ onlinkipv6prefix() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].ipv6prefix = resource[i].ipv6prefix
						updateresources[i].onlinkprefix = resource[i].onlinkprefix
						updateresources[i].autonomusprefix = resource[i].autonomusprefix
						updateresources[i].depricateprefix = resource[i].depricateprefix
						updateresources[i].decrementprefixlifetimes = resource[i].decrementprefixlifetimes
						updateresources[i].prefixvalidelifetime = resource[i].prefixvalidelifetime
						updateresources[i].prefixpreferredlifetime = resource[i].prefixpreferredlifetime
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of onlinkipv6prefix resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = onlinkipv6prefix()
				if type(resource) !=  type(unsetresource):
					unsetresource.ipv6prefix = resource
				else :
					unsetresource.ipv6prefix = resource.ipv6prefix
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ onlinkipv6prefix() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ipv6prefix = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ onlinkipv6prefix() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ipv6prefix = resource[i].ipv6prefix
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the onlinkipv6prefix resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = onlinkipv6prefix()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = onlinkipv6prefix()
						obj.ipv6prefix = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [onlinkipv6prefix() for _ in range(len(name))]
							obj = [onlinkipv6prefix() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = onlinkipv6prefix()
								obj[i].ipv6prefix = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of onlinkipv6prefix resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = onlinkipv6prefix()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the onlinkipv6prefix resources configured on NetScaler.
		"""
		try :
			obj = onlinkipv6prefix()
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
		ur""" Use this API to count filtered the set of onlinkipv6prefix resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = onlinkipv6prefix()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Depricateprefix:
		YES = "YES"
		NO = "NO"

	class Decrementprefixlifetimes:
		YES = "YES"
		NO = "NO"

	class Onlinkprefix:
		YES = "YES"
		NO = "NO"

	class Autonomusprefix:
		YES = "YES"
		NO = "NO"

class onlinkipv6prefix_response(base_response) :
	def __init__(self, length=1) :
		self.onlinkipv6prefix = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.onlinkipv6prefix = [onlinkipv6prefix() for _ in range(length)]

