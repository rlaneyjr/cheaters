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

class feoparameter(base_resource) :
	""" Configuration for FEO parameter resource. """
	def __init__(self) :
		self._cachemaxage = 0
		self._jpegqualitypercent = 0
		self._cssinlinethressize = 0
		self._jsinlinethressize = 0
		self._imginlinethressize = 0

	@property
	def cachemaxage(self) :
		ur"""Maximum period (in days), for cache extension.<br/>Default value: 30<br/>Maximum length =  360.
		"""
		try :
			return self._cachemaxage
		except Exception as e:
			raise e

	@cachemaxage.setter
	def cachemaxage(self, cachemaxage) :
		ur"""Maximum period (in days), for cache extension.<br/>Default value: 30<br/>Maximum length =  360
		"""
		try :
			self._cachemaxage = cachemaxage
		except Exception as e:
			raise e

	@property
	def jpegqualitypercent(self) :
		ur"""The percentage value of a JPEG image quality to be reduced. Range: 0 - 100.<br/>Default value: 75<br/>Maximum length =  100.
		"""
		try :
			return self._jpegqualitypercent
		except Exception as e:
			raise e

	@jpegqualitypercent.setter
	def jpegqualitypercent(self, jpegqualitypercent) :
		ur"""The percentage value of a JPEG image quality to be reduced. Range: 0 - 100.<br/>Default value: 75<br/>Maximum length =  100
		"""
		try :
			self._jpegqualitypercent = jpegqualitypercent
		except Exception as e:
			raise e

	@property
	def cssinlinethressize(self) :
		ur"""Threshold value of the file size (in bytes) for converting external CSS files to inline CSS files.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  2048.
		"""
		try :
			return self._cssinlinethressize
		except Exception as e:
			raise e

	@cssinlinethressize.setter
	def cssinlinethressize(self, cssinlinethressize) :
		ur"""Threshold value of the file size (in bytes) for converting external CSS files to inline CSS files.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  2048
		"""
		try :
			self._cssinlinethressize = cssinlinethressize
		except Exception as e:
			raise e

	@property
	def jsinlinethressize(self) :
		ur"""Threshold value of the file size (in bytes), for converting external JavaScript files to inline JavaScript files.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  2048.
		"""
		try :
			return self._jsinlinethressize
		except Exception as e:
			raise e

	@jsinlinethressize.setter
	def jsinlinethressize(self, jsinlinethressize) :
		ur"""Threshold value of the file size (in bytes), for converting external JavaScript files to inline JavaScript files.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  2048
		"""
		try :
			self._jsinlinethressize = jsinlinethressize
		except Exception as e:
			raise e

	@property
	def imginlinethressize(self) :
		ur"""Maximum file size of an image (in bytes), for coverting linked images to inline images.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  2048.
		"""
		try :
			return self._imginlinethressize
		except Exception as e:
			raise e

	@imginlinethressize.setter
	def imginlinethressize(self, imginlinethressize) :
		ur"""Maximum file size of an image (in bytes), for coverting linked images to inline images.<br/>Default value: 1024<br/>Minimum length =  1<br/>Maximum length =  2048
		"""
		try :
			self._imginlinethressize = imginlinethressize
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(feoparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.feoparameter
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
		ur""" Use this API to update feoparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = feoparameter()
				updateresource.cachemaxage = resource.cachemaxage
				updateresource.jpegqualitypercent = resource.jpegqualitypercent
				updateresource.cssinlinethressize = resource.cssinlinethressize
				updateresource.jsinlinethressize = resource.jsinlinethressize
				updateresource.imginlinethressize = resource.imginlinethressize
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of feoparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = feoparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the feoparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = feoparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class feoparameter_response(base_response) :
	def __init__(self, length=1) :
		self.feoparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.feoparameter = [feoparameter() for _ in range(length)]

