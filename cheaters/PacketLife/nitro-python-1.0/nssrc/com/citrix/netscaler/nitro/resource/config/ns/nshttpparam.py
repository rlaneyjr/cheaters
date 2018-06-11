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

class nshttpparam(base_resource) :
	""" Configuration for HTTP parameter resource. """
	def __init__(self) :
		self._dropinvalreqs = ""
		self._markhttp09inval = ""
		self._markconnreqinval = ""
		self._insnssrvrhdr = ""
		self._nssrvrhdr = ""
		self._logerrresp = ""
		self._conmultiplex = ""
		self._maxreusepool = 0

	@property
	def dropinvalreqs(self) :
		ur"""Drop invalid HTTP requests or responses.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._dropinvalreqs
		except Exception as e:
			raise e

	@dropinvalreqs.setter
	def dropinvalreqs(self, dropinvalreqs) :
		ur"""Drop invalid HTTP requests or responses.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._dropinvalreqs = dropinvalreqs
		except Exception as e:
			raise e

	@property
	def markhttp09inval(self) :
		ur"""Mark HTTP/0.9 requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._markhttp09inval
		except Exception as e:
			raise e

	@markhttp09inval.setter
	def markhttp09inval(self, markhttp09inval) :
		ur"""Mark HTTP/0.9 requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._markhttp09inval = markhttp09inval
		except Exception as e:
			raise e

	@property
	def markconnreqinval(self) :
		ur"""Mark CONNECT requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._markconnreqinval
		except Exception as e:
			raise e

	@markconnreqinval.setter
	def markconnreqinval(self, markconnreqinval) :
		ur"""Mark CONNECT requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._markconnreqinval = markconnreqinval
		except Exception as e:
			raise e

	@property
	def insnssrvrhdr(self) :
		ur"""Enable or disable NetScaler server header insertion for NetScaler generated HTTP responses.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._insnssrvrhdr
		except Exception as e:
			raise e

	@insnssrvrhdr.setter
	def insnssrvrhdr(self, insnssrvrhdr) :
		ur"""Enable or disable NetScaler server header insertion for NetScaler generated HTTP responses.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._insnssrvrhdr = insnssrvrhdr
		except Exception as e:
			raise e

	@property
	def nssrvrhdr(self) :
		ur"""The server header value to be inserted. If no explicit header is specified then NSBUILD.RELEASE is used as default server header.<br/>Minimum length =  1.
		"""
		try :
			return self._nssrvrhdr
		except Exception as e:
			raise e

	@nssrvrhdr.setter
	def nssrvrhdr(self, nssrvrhdr) :
		ur"""The server header value to be inserted. If no explicit header is specified then NSBUILD.RELEASE is used as default server header.<br/>Minimum length =  1
		"""
		try :
			self._nssrvrhdr = nssrvrhdr
		except Exception as e:
			raise e

	@property
	def logerrresp(self) :
		ur"""Server header value to be inserted.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._logerrresp
		except Exception as e:
			raise e

	@logerrresp.setter
	def logerrresp(self, logerrresp) :
		ur"""Server header value to be inserted.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._logerrresp = logerrresp
		except Exception as e:
			raise e

	@property
	def conmultiplex(self) :
		ur"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._conmultiplex
		except Exception as e:
			raise e

	@conmultiplex.setter
	def conmultiplex(self, conmultiplex) :
		ur"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._conmultiplex = conmultiplex
		except Exception as e:
			raise e

	@property
	def maxreusepool(self) :
		ur"""Maximum limit on the number of connections, from the NetScaler to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time.<br/>Maximum length =  360000.
		"""
		try :
			return self._maxreusepool
		except Exception as e:
			raise e

	@maxreusepool.setter
	def maxreusepool(self, maxreusepool) :
		ur"""Maximum limit on the number of connections, from the NetScaler to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time.<br/>Maximum length =  360000
		"""
		try :
			self._maxreusepool = maxreusepool
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nshttpparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nshttpparam
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
		ur""" Use this API to update nshttpparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = nshttpparam()
				updateresource.dropinvalreqs = resource.dropinvalreqs
				updateresource.markhttp09inval = resource.markhttp09inval
				updateresource.markconnreqinval = resource.markconnreqinval
				updateresource.insnssrvrhdr = resource.insnssrvrhdr
				updateresource.nssrvrhdr = resource.nssrvrhdr
				updateresource.logerrresp = resource.logerrresp
				updateresource.conmultiplex = resource.conmultiplex
				updateresource.maxreusepool = resource.maxreusepool
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nshttpparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nshttpparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nshttpparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nshttpparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Conmultiplex:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Markhttp09inval:
		ON = "ON"
		OFF = "OFF"

	class Insnssrvrhdr:
		ON = "ON"
		OFF = "OFF"

	class Markconnreqinval:
		ON = "ON"
		OFF = "OFF"

	class Logerrresp:
		ON = "ON"
		OFF = "OFF"

	class Dropinvalreqs:
		ON = "ON"
		OFF = "OFF"

class nshttpparam_response(base_response) :
	def __init__(self, length=1) :
		self.nshttpparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nshttpparam = [nshttpparam() for _ in range(length)]

