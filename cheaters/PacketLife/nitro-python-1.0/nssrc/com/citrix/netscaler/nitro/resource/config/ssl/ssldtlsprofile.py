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

class ssldtlsprofile(base_resource) :
	""" Configuration for DTLS profile resource. """
	def __init__(self) :
		self._name = ""
		self._pmtudiscovery = ""
		self._maxrecordsize = 0
		self._maxretrytime = 0
		self._helloverifyrequest = ""
		self._terminatesession = ""
		self._maxpacketsize = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for the DTLS profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for the DTLS profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def pmtudiscovery(self) :
		ur"""Source for the maximum record size value. If ENABLED, the value is taken from the PMTU table. If DISABLED, the value is taken from the profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._pmtudiscovery
		except Exception as e:
			raise e

	@pmtudiscovery.setter
	def pmtudiscovery(self, pmtudiscovery) :
		ur"""Source for the maximum record size value. If ENABLED, the value is taken from the PMTU table. If DISABLED, the value is taken from the profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._pmtudiscovery = pmtudiscovery
		except Exception as e:
			raise e

	@property
	def maxrecordsize(self) :
		ur"""Maximum size of records that can be sent if PMTU is disabled.<br/>Default value: 1459<br/>Minimum length =  250<br/>Maximum length =  1459.
		"""
		try :
			return self._maxrecordsize
		except Exception as e:
			raise e

	@maxrecordsize.setter
	def maxrecordsize(self, maxrecordsize) :
		ur"""Maximum size of records that can be sent if PMTU is disabled.<br/>Default value: 1459<br/>Minimum length =  250<br/>Maximum length =  1459
		"""
		try :
			self._maxrecordsize = maxrecordsize
		except Exception as e:
			raise e

	@property
	def maxretrytime(self) :
		ur"""Wait for the specified time, in seconds, before resending the request.<br/>Default value: 3.
		"""
		try :
			return self._maxretrytime
		except Exception as e:
			raise e

	@maxretrytime.setter
	def maxretrytime(self, maxretrytime) :
		ur"""Wait for the specified time, in seconds, before resending the request.<br/>Default value: 3
		"""
		try :
			self._maxretrytime = maxretrytime
		except Exception as e:
			raise e

	@property
	def helloverifyrequest(self) :
		ur"""Send a Hello Verify request to validate the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._helloverifyrequest
		except Exception as e:
			raise e

	@helloverifyrequest.setter
	def helloverifyrequest(self, helloverifyrequest) :
		ur"""Send a Hello Verify request to validate the client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._helloverifyrequest = helloverifyrequest
		except Exception as e:
			raise e

	@property
	def terminatesession(self) :
		ur"""Terminate the session if the message authentication code (MAC) of the client and server do not match.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._terminatesession
		except Exception as e:
			raise e

	@terminatesession.setter
	def terminatesession(self, terminatesession) :
		ur"""Terminate the session if the message authentication code (MAC) of the client and server do not match.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._terminatesession = terminatesession
		except Exception as e:
			raise e

	@property
	def maxpacketsize(self) :
		ur"""Maximum number of packets to reassemble. This value helps protect against a fragmented packet attack.<br/>Default value: 120<br/>Maximum length =  86400.
		"""
		try :
			return self._maxpacketsize
		except Exception as e:
			raise e

	@maxpacketsize.setter
	def maxpacketsize(self, maxpacketsize) :
		ur"""Maximum number of packets to reassemble. This value helps protect against a fragmented packet attack.<br/>Default value: 120<br/>Maximum length =  86400
		"""
		try :
			self._maxpacketsize = maxpacketsize
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ssldtlsprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssldtlsprofile
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
		ur""" Use this API to add ssldtlsprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = ssldtlsprofile()
				addresource.name = resource.name
				addresource.pmtudiscovery = resource.pmtudiscovery
				addresource.maxrecordsize = resource.maxrecordsize
				addresource.maxretrytime = resource.maxretrytime
				addresource.helloverifyrequest = resource.helloverifyrequest
				addresource.terminatesession = resource.terminatesession
				addresource.maxpacketsize = resource.maxpacketsize
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ ssldtlsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].pmtudiscovery = resource[i].pmtudiscovery
						addresources[i].maxrecordsize = resource[i].maxrecordsize
						addresources[i].maxretrytime = resource[i].maxretrytime
						addresources[i].helloverifyrequest = resource[i].helloverifyrequest
						addresources[i].terminatesession = resource[i].terminatesession
						addresources[i].maxpacketsize = resource[i].maxpacketsize
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete ssldtlsprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ssldtlsprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ ssldtlsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ ssldtlsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update ssldtlsprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = ssldtlsprofile()
				updateresource.name = resource.name
				updateresource.pmtudiscovery = resource.pmtudiscovery
				updateresource.maxrecordsize = resource.maxrecordsize
				updateresource.maxretrytime = resource.maxretrytime
				updateresource.helloverifyrequest = resource.helloverifyrequest
				updateresource.terminatesession = resource.terminatesession
				updateresource.maxpacketsize = resource.maxpacketsize
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ ssldtlsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].pmtudiscovery = resource[i].pmtudiscovery
						updateresources[i].maxrecordsize = resource[i].maxrecordsize
						updateresources[i].maxretrytime = resource[i].maxretrytime
						updateresources[i].helloverifyrequest = resource[i].helloverifyrequest
						updateresources[i].terminatesession = resource[i].terminatesession
						updateresources[i].maxpacketsize = resource[i].maxpacketsize
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of ssldtlsprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ssldtlsprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ ssldtlsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ ssldtlsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the ssldtlsprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ssldtlsprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = ssldtlsprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [ssldtlsprofile() for _ in range(len(name))]
							obj = [ssldtlsprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = ssldtlsprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of ssldtlsprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssldtlsprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the ssldtlsprofile resources configured on NetScaler.
		"""
		try :
			obj = ssldtlsprofile()
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
		ur""" Use this API to count filtered the set of ssldtlsprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssldtlsprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Terminatesession:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pmtudiscovery:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Helloverifyrequest:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class ssldtlsprofile_response(base_response) :
	def __init__(self, length=1) :
		self.ssldtlsprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ssldtlsprofile = [ssldtlsprofile() for _ in range(length)]

