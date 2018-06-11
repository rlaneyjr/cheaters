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

class appfwsignatures(base_resource) :
	""" Configuration for application firewall signatures XML configuration resource. """
	def __init__(self) :
		self._name = ""
		self._src = ""
		self._xslt = ""
		self._comment = ""
		self._overwrite = False
		self._merge = False
		self._sha1 = ""
		self._mergedefault = False
		self._response = ""

	@property
	def name(self) :
		ur"""Name of the signature object.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the signature object.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def src(self) :
		ur"""URL (protocol, host, path, and file name) for the location at which to store the imported signatures object.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._src
		except Exception as e:
			raise e

	@src.setter
	def src(self, src) :
		ur"""URL (protocol, host, path, and file name) for the location at which to store the imported signatures object.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._src = src
		except Exception as e:
			raise e

	@property
	def xslt(self) :
		ur"""XSLT file source.<br/>Maximum length =  2047.
		"""
		try :
			return self._xslt
		except Exception as e:
			raise e

	@xslt.setter
	def xslt(self, xslt) :
		ur"""XSLT file source.<br/>Maximum length =  2047
		"""
		try :
			self._xslt = xslt
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments to preserve information about the signatures object.<br/>Maximum length =  128.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments to preserve information about the signatures object.<br/>Maximum length =  128
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def overwrite(self) :
		ur"""Overwrite any existing signatures object of the same name.
		"""
		try :
			return self._overwrite
		except Exception as e:
			raise e

	@overwrite.setter
	def overwrite(self, overwrite) :
		ur"""Overwrite any existing signatures object of the same name.
		"""
		try :
			self._overwrite = overwrite
		except Exception as e:
			raise e

	@property
	def merge(self) :
		ur"""Merges the existing Signature with new signature rules.
		"""
		try :
			return self._merge
		except Exception as e:
			raise e

	@merge.setter
	def merge(self, merge) :
		ur"""Merges the existing Signature with new signature rules.
		"""
		try :
			self._merge = merge
		except Exception as e:
			raise e

	@property
	def sha1(self) :
		ur"""File path for sha1 file to validate signature file.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._sha1
		except Exception as e:
			raise e

	@sha1.setter
	def sha1(self, sha1) :
		ur"""File path for sha1 file to validate signature file.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._sha1 = sha1
		except Exception as e:
			raise e

	@property
	def mergedefault(self) :
		ur"""Merges signature file with default signature file.
		"""
		try :
			return self._mergedefault
		except Exception as e:
			raise e

	@mergedefault.setter
	def mergedefault(self, mergedefault) :
		ur"""Merges signature file with default signature file.
		"""
		try :
			self._mergedefault = mergedefault
		except Exception as e:
			raise e

	@property
	def response(self) :
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwsignatures_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwsignatures
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
	def delete(cls, client, resource) :
		ur""" Use this API to delete appfwsignatures.
		"""
		try :
			if type(resource) is not list :
				deleteresource = appfwsignatures()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		ur""" Use this API to Import appfwsignatures.
		"""
		try :
			if type(resource) is not list :
				Importresource = appfwsignatures()
				Importresource.src = resource.src
				Importresource.name = resource.name
				Importresource.xslt = resource.xslt
				Importresource.comment = resource.comment
				Importresource.overwrite = resource.overwrite
				Importresource.merge = resource.merge
				Importresource.sha1 = resource.sha1
				return Importresource.perform_operation(client,"Import")
		except Exception as e :
			raise e

	@classmethod
	def change(cls, client, resource) :
		ur""" Use this API to change appfwsignatures.
		"""
		try :
			if type(resource) is not list :
				changeresource = appfwsignatures()
				changeresource.name = resource.name
				changeresource.mergedefault = resource.mergedefault
				return changeresource.perform_operation(client,"update")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the appfwsignatures resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwsignatures()
				response = obj.get_resources(client, option_)
				if type(name) != cls :
					if type(name) is not list :
						obj = appfwsignatures()
						obj.name = name
						response = obj.get_resource(client, option_)
			return response
		except Exception as e :
			raise e


class appfwsignatures_response(base_response) :
	def __init__(self, length=1) :
		self.appfwsignatures = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwsignatures = [appfwsignatures() for _ in range(length)]

