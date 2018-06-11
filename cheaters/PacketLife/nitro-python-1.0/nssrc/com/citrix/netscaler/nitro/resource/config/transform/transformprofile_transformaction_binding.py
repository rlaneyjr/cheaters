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

class transformprofile_transformaction_binding(base_resource) :
	""" Binding class showing the transformaction that can be bound to transformprofile.
	"""
	def __init__(self) :
		self._actionname = ""
		self._priority = 0
		self._state = ""
		self._profilename = ""
		self._requrlfrom = ""
		self._requrlinto = ""
		self._resurlfrom = ""
		self._resurlinto = ""
		self._cookiedomainfrom = ""
		self._cookiedomaininto = ""
		self._actioncomment = ""
		self._name = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""Name of the profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the profile.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def actionname(self) :
		ur"""URL Transformation action name.
		"""
		try :
			return self._actionname
		except Exception as e:
			raise e

	@actionname.setter
	def actionname(self, actionname) :
		ur"""URL Transformation action name.
		"""
		try :
			self._actionname = actionname
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Priority of the Action within the Profile.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def resurlfrom(self) :
		ur"""Pattern of original response URLs. It corresponds to the way external users view the server, and acts as a source for response transformations.
		"""
		try :
			return self._resurlfrom
		except Exception as e:
			raise e

	@property
	def profilename(self) :
		ur"""URL Transformation profile name.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""Enabled flag.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def actioncomment(self) :
		ur"""Comments.
		"""
		try :
			return self._actioncomment
		except Exception as e:
			raise e

	@property
	def requrlinto(self) :
		ur"""Pattern of transformed request URLs. It corresponds to internal addresses and indicates how they are created.
		"""
		try :
			return self._requrlinto
		except Exception as e:
			raise e

	@property
	def cookiedomainfrom(self) :
		ur"""Pattern of the original domain in Set-Cookie headers.
		"""
		try :
			return self._cookiedomainfrom
		except Exception as e:
			raise e

	@property
	def cookiedomaininto(self) :
		ur"""Pattern of the transformed domain in Set-Cookie headers.
		"""
		try :
			return self._cookiedomaininto
		except Exception as e:
			raise e

	@property
	def resurlinto(self) :
		ur"""Pattern of transformed response URLs. It corresponds to internal addresses and indicates how they are created.
		"""
		try :
			return self._resurlinto
		except Exception as e:
			raise e

	@property
	def requrlfrom(self) :
		ur"""Pattern of original request URLs. It corresponds to the way external users view the server, and acts as a source for request transformations.
		"""
		try :
			return self._requrlfrom
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(transformprofile_transformaction_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.transformprofile_transformaction_binding
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
	def get(cls, service, name) :
		ur""" Use this API to fetch transformprofile_transformaction_binding resources.
		"""
		try :
			obj = transformprofile_transformaction_binding()
			obj.name = name
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		ur""" Use this API to fetch filtered set of transformprofile_transformaction_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformprofile_transformaction_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		ur""" Use this API to count transformprofile_transformaction_binding resources configued on NetScaler.
		"""
		try :
			obj = transformprofile_transformaction_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		ur""" Use this API to count the filtered set of transformprofile_transformaction_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = transformprofile_transformaction_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class transformprofile_transformaction_binding_response(base_response) :
	def __init__(self, length=1) :
		self.transformprofile_transformaction_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.transformprofile_transformaction_binding = [transformprofile_transformaction_binding() for _ in range(length)]

