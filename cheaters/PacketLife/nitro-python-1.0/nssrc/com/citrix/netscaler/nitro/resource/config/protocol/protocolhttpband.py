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

class protocolhttpband(base_resource) :
	""" Configuration for HTTP request/response band resource. """
	def __init__(self) :
		self._reqbandsize = 0
		self._respbandsize = 0
		self._type = ""
		self._bandrange = 0
		self._numberofbands = 0
		self._totalbandsize = []
		self._avgbandsize = []
		self._avgbandsizenew = []
		self._banddata = []
		self._banddatanew = []
		self._accesscount = []
		self._accessratio = []
		self._accessrationew = []
		self._totals = []

	@property
	def reqbandsize(self) :
		ur"""Band size, in bytes, for HTTP request band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 100<br/>Minimum length =  50.
		"""
		try :
			return self._reqbandsize
		except Exception as e:
			raise e

	@reqbandsize.setter
	def reqbandsize(self, reqbandsize) :
		ur"""Band size, in bytes, for HTTP request band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 100<br/>Minimum length =  50
		"""
		try :
			self._reqbandsize = reqbandsize
		except Exception as e:
			raise e

	@property
	def respbandsize(self) :
		ur"""Band size, in bytes, for HTTP response band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 1024<br/>Minimum length =  50.
		"""
		try :
			return self._respbandsize
		except Exception as e:
			raise e

	@respbandsize.setter
	def respbandsize(self, respbandsize) :
		ur"""Band size, in bytes, for HTTP response band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 1024<br/>Minimum length =  50
		"""
		try :
			self._respbandsize = respbandsize
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""Type of statistics to display.<br/>Possible values = REQUEST, RESPONSE.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""Type of statistics to display.<br/>Possible values = REQUEST, RESPONSE
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def bandrange(self) :
		ur"""The range of the HTTP request/response size, in bytes.
		"""
		try :
			return self._bandrange
		except Exception as e:
			raise e

	@property
	def numberofbands(self) :
		ur"""The total number of http bands.
		"""
		try :
			return self._numberofbands
		except Exception as e:
			raise e

	@property
	def totalbandsize(self) :
		ur"""The total size of all HTTP requests/responses in this size range.
		"""
		try :
			return self._totalbandsize
		except Exception as e:
			raise e

	@property
	def avgbandsize(self) :
		ur"""The average size of all HTTP requests/responses in this size range.
		"""
		try :
			return self._avgbandsize
		except Exception as e:
			raise e

	@property
	def avgbandsizenew(self) :
		ur"""The average size of all HTTP requests/responses in this size range.
		"""
		try :
			return self._avgbandsizenew
		except Exception as e:
			raise e

	@property
	def banddata(self) :
		ur"""The total size of all HTTP requests/responses in this size range, expressed as a percentage of the total size of all HTTP requests/responses.
		"""
		try :
			return self._banddata
		except Exception as e:
			raise e

	@property
	def banddatanew(self) :
		ur"""The total size of all HTTP requests/responses in this size range, expressed as a percentage of the total size of all HTTP requests/responses.
		"""
		try :
			return self._banddatanew
		except Exception as e:
			raise e

	@property
	def accesscount(self) :
		ur"""The number of HTTP requests/responses in this size range.
		"""
		try :
			return self._accesscount
		except Exception as e:
			raise e

	@property
	def accessratio(self) :
		ur"""The number of HTTP requests/responses in this size range, expressed as a percentage of the total number of HTTP requests/responses.
		"""
		try :
			return self._accessratio
		except Exception as e:
			raise e

	@property
	def accessrationew(self) :
		ur"""The number of HTTP requests/responses in this size range, expressed as a percentage of the total number of HTTP requests/responses.
		"""
		try :
			return self._accessrationew
		except Exception as e:
			raise e

	@property
	def totals(self) :
		ur"""The total of totalBandSize, avgBandSize, BandData, accessCount, accessRatio respectively.
		"""
		try :
			return self._totals
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolhttpband_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolhttpband
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
		ur""" Use this API to update protocolhttpband.
		"""
		try :
			if type(resource) is not list :
				updateresource = protocolhttpband()
				updateresource.reqbandsize = resource.reqbandsize
				updateresource.respbandsize = resource.respbandsize
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of protocolhttpband resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = protocolhttpband()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the protocolhttpband resources that are configured on netscaler.
		"""
		try :
			if type(name) == cls :
				if type(name) is not list :
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the protocolhttpband resources that are configured on netscaler.
	# This uses protocolhttpband_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = protocolhttpband()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Type:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"

class protocolhttpband_response(base_response) :
	def __init__(self, length=1) :
		self.protocolhttpband = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolhttpband = [protocolhttpband() for _ in range(length)]

