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

class riseprofile(base_resource) :
	""" Configuration for RISE profile resource. """
	def __init__(self) :
		self._profilename = ""
		self._servicename = ""
		self._deviceid = ""
		self._slotid = 0
		self._slotno = 0
		self._vdcid = 0
		self._vpcid = 0
		self._ipaddress = ""
		self._mode = ""
		self._status = ""
		self._vlan = 0
		self._vlangroupid = 0
		self._vlancfgstatus = ""
		self._ifnum = ""
		self._issu = ""
		self.___count = 0

	@property
	def profilename(self) :
		ur"""Name of the RISE profile.<br/>Minimum length =  1<br/>Maximum length =  83.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@profilename.setter
	def profilename(self, profilename) :
		ur"""Name of the RISE profile.<br/>Minimum length =  1<br/>Maximum length =  83
		"""
		try :
			self._profilename = profilename
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		ur"""RISE Service name.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def deviceid(self) :
		ur"""Device id.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._deviceid
		except Exception as e:
			raise e

	@property
	def slotid(self) :
		ur"""Slot number of the RISE profile.
		"""
		try :
			return self._slotid
		except Exception as e:
			raise e

	@property
	def slotno(self) :
		ur"""Slot number of the RISE profile.
		"""
		try :
			return self._slotno
		except Exception as e:
			raise e

	@property
	def vdcid(self) :
		ur"""RISE vdc id.
		"""
		try :
			return self._vdcid
		except Exception as e:
			raise e

	@property
	def vpcid(self) :
		ur"""RISE vpc id.
		"""
		try :
			return self._vpcid
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		ur"""RISE ip address.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@property
	def mode(self) :
		ur"""RISE attach mode.<br/>Possible values = Direct, Indirect, vPC-Direct.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""RISE status.<br/>Possible values = Active, Inactive.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		ur"""RISE Vlan id.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@property
	def vlangroupid(self) :
		ur"""RISE Vlan Group id.
		"""
		try :
			return self._vlangroupid
		except Exception as e:
			raise e

	@property
	def vlancfgstatus(self) :
		ur"""RISE config status.<br/>Possible values = Ok, Invalid.
		"""
		try :
			return self._vlancfgstatus
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		ur"""RISE Interface number.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@property
	def issu(self) :
		ur"""RISE issu status.<br/>Possible values = InProgress, None.
		"""
		try :
			return self._issu
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(riseprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.riseprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.profilename is not None :
				return str(self.profilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the riseprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = riseprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = riseprofile()
						obj.profilename = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [riseprofile() for _ in range(len(name))]
							obj = [riseprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = riseprofile()
								obj[i].profilename = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of riseprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = riseprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the riseprofile resources configured on NetScaler.
		"""
		try :
			obj = riseprofile()
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
		ur""" Use this API to count filtered the set of riseprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = riseprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Mode:
		Direct = "Direct"
		Indirect = "Indirect"
		vPC_Direct = "vPC-Direct"

	class Issu:
		InProgress = "InProgress"
		NONE = "None"

	class Status:
		Active = "Active"
		Inactive = "Inactive"

	class Vlancfgstatus:
		Ok = "Ok"
		Invalid = "Invalid"

class riseprofile_response(base_response) :
	def __init__(self, length=1) :
		self.riseprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.riseprofile = [riseprofile() for _ in range(length)]

