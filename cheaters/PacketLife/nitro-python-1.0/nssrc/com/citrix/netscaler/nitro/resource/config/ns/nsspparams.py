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

class nsspparams(base_resource) :
	""" Configuration for Surge Protection parameter resource. """
	def __init__(self) :
		self._basethreshold = 0
		self._throttle = ""
		self._table0 = []

	@property
	def basethreshold(self) :
		ur"""Maximum number of server connections that can be opened before surge protection is activated.<br/>Default value: 200<br/>Maximum length =  0x7FFF.
		"""
		try :
			return self._basethreshold
		except Exception as e:
			raise e

	@basethreshold.setter
	def basethreshold(self, basethreshold) :
		ur"""Maximum number of server connections that can be opened before surge protection is activated.<br/>Default value: 200<br/>Maximum length =  0x7FFF
		"""
		try :
			self._basethreshold = basethreshold
		except Exception as e:
			raise e

	@property
	def throttle(self) :
		ur"""Rate at which the system opens connections to the server.<br/>Default value: Normal<br/>Possible values = Aggressive, Normal, Relaxed.
		"""
		try :
			return self._throttle
		except Exception as e:
			raise e

	@throttle.setter
	def throttle(self, throttle) :
		ur"""Rate at which the system opens connections to the server.<br/>Default value: Normal<br/>Possible values = Aggressive, Normal, Relaxed
		"""
		try :
			self._throttle = throttle
		except Exception as e:
			raise e

	@property
	def table0(self) :
		ur"""Table.
		"""
		try :
			return self._table0
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsspparams_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsspparams
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
	def update(cls, client, resource) :
		ur""" Use this API to update nsspparams.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsspparams()
				updateresource.basethreshold = resource.basethreshold
				updateresource.throttle = resource.throttle
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nsspparams resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsspparams()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsspparams resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsspparams()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Throttle:
		Aggressive = "Aggressive"
		Normal = "Normal"
		Relaxed = "Relaxed"

class nsspparams_response(base_response) :
	def __init__(self, length=1) :
		self.nsspparams = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsspparams = [nsspparams() for _ in range(length)]

