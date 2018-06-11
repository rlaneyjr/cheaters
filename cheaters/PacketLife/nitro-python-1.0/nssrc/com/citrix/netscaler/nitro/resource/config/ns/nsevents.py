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

class nsevents(base_resource) :
	""" Configuration for events resource. """
	def __init__(self) :
		self._eventno = 0
		self._time = 0
		self._eventcode = 0
		self._devid = 0
		self._devname = ""
		self._text = ""
		self._data0 = 0
		self._data1 = 0
		self._data2 = 0
		self._data3 = 0
		self.___count = 0

	@property
	def eventno(self) :
		ur"""Event number starting from which events must be shown.
		"""
		try :
			return self._eventno
		except Exception as e:
			raise e

	@eventno.setter
	def eventno(self, eventno) :
		ur"""Event number starting from which events must be shown.
		"""
		try :
			self._eventno = eventno
		except Exception as e:
			raise e

	@property
	def time(self) :
		ur"""Event no.
		"""
		try :
			return self._time
		except Exception as e:
			raise e

	@property
	def eventcode(self) :
		ur"""event Code.
		"""
		try :
			return self._eventcode
		except Exception as e:
			raise e

	@property
	def devid(self) :
		ur"""Device Name.
		"""
		try :
			return self._devid
		except Exception as e:
			raise e

	@property
	def devname(self) :
		ur"""Device Name.
		"""
		try :
			return self._devname
		except Exception as e:
			raise e

	@property
	def text(self) :
		ur"""Event no.
		"""
		try :
			return self._text
		except Exception as e:
			raise e

	@property
	def data0(self) :
		ur"""additional event information.
		"""
		try :
			return self._data0
		except Exception as e:
			raise e

	@property
	def data1(self) :
		ur"""additional event information.
		"""
		try :
			return self._data1
		except Exception as e:
			raise e

	@property
	def data2(self) :
		ur"""additional event information.
		"""
		try :
			return self._data2
		except Exception as e:
			raise e

	@property
	def data3(self) :
		ur"""additional event information.
		"""
		try :
			return self._data3
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsevents_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsevents
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
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nsevents resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsevents()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		ur""" Use this API to fetch all the nsevents resources that are configured on netscaler.
	# This uses nsevents_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nsevents()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nsevents resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsevents()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nsevents resources configured on NetScaler.
		"""
		try :
			obj = nsevents()
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
		ur""" Use this API to count filtered the set of nsevents resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsevents()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nsevents_response(base_response) :
	def __init__(self, length=1) :
		self.nsevents = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsevents = [nsevents() for _ in range(length)]

