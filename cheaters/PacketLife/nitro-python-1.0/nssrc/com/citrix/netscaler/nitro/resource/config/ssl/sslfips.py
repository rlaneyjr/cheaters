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

class sslfips(base_resource) :
	""" Configuration for fips resource. """
	def __init__(self) :
		self._inithsm = ""
		self._sopassword = ""
		self._oldsopassword = ""
		self._userpassword = ""
		self._hsmlabel = ""
		self._fipsfw = ""
		self._erasedata = ""
		self._serial = 0
		self._majorversion = 0
		self._minorversion = 0
		self._fipshwmajorversion = 0
		self._fipshwminorversion = 0
		self._fipshwversionstring = ""
		self._flashmemorytotal = 0
		self._flashmemoryfree = 0
		self._sramtotal = 0
		self._sramfree = 0
		self._status = 0
		self._flag = 0
		self._serialno = ""
		self._model = ""
		self._state = 0
		self._firmwarereleasedate = ""
		self._coresmax = 0
		self._coresenabled = 0

	@property
	def inithsm(self) :
		ur"""FIPS initialization level. The appliance currently supports Level-2 (FIPS 140-2).<br/>Possible values = Level-2.
		"""
		try :
			return self._inithsm
		except Exception as e:
			raise e

	@inithsm.setter
	def inithsm(self, inithsm) :
		ur"""FIPS initialization level. The appliance currently supports Level-2 (FIPS 140-2).<br/>Possible values = Level-2
		"""
		try :
			self._inithsm = inithsm
		except Exception as e:
			raise e

	@property
	def sopassword(self) :
		ur"""Security officer password that will be in effect after you have configured the HSM.<br/>Minimum length =  1.
		"""
		try :
			return self._sopassword
		except Exception as e:
			raise e

	@sopassword.setter
	def sopassword(self, sopassword) :
		ur"""Security officer password that will be in effect after you have configured the HSM.<br/>Minimum length =  1
		"""
		try :
			self._sopassword = sopassword
		except Exception as e:
			raise e

	@property
	def oldsopassword(self) :
		ur"""Old password for the security officer.<br/>Minimum length =  1.
		"""
		try :
			return self._oldsopassword
		except Exception as e:
			raise e

	@oldsopassword.setter
	def oldsopassword(self, oldsopassword) :
		ur"""Old password for the security officer.<br/>Minimum length =  1
		"""
		try :
			self._oldsopassword = oldsopassword
		except Exception as e:
			raise e

	@property
	def userpassword(self) :
		ur"""The Hardware Security Module's (HSM) User password.<br/>Minimum length =  1.
		"""
		try :
			return self._userpassword
		except Exception as e:
			raise e

	@userpassword.setter
	def userpassword(self, userpassword) :
		ur"""The Hardware Security Module's (HSM) User password.<br/>Minimum length =  1
		"""
		try :
			self._userpassword = userpassword
		except Exception as e:
			raise e

	@property
	def hsmlabel(self) :
		ur"""Label to identify the Hardware Security Module (HSM).<br/>Minimum length =  1.
		"""
		try :
			return self._hsmlabel
		except Exception as e:
			raise e

	@hsmlabel.setter
	def hsmlabel(self, hsmlabel) :
		ur"""Label to identify the Hardware Security Module (HSM).<br/>Minimum length =  1
		"""
		try :
			self._hsmlabel = hsmlabel
		except Exception as e:
			raise e

	@property
	def fipsfw(self) :
		ur"""FIPS firmware update.<br/>Possible values = 4.6.1.
		"""
		try :
			return self._fipsfw
		except Exception as e:
			raise e

	@fipsfw.setter
	def fipsfw(self, fipsfw) :
		ur"""FIPS firmware update.<br/>Possible values = 4.6.1
		"""
		try :
			self._fipsfw = fipsfw
		except Exception as e:
			raise e

	@property
	def erasedata(self) :
		ur"""Erase data.<br/>Default value: FIPS_ERASE<br/>Minimum length =  1.
		"""
		try :
			return self._erasedata
		except Exception as e:
			raise e

	@property
	def serial(self) :
		ur"""FIPS card serial number.
		"""
		try :
			return self._serial
		except Exception as e:
			raise e

	@property
	def majorversion(self) :
		ur"""Firmware major version.
		"""
		try :
			return self._majorversion
		except Exception as e:
			raise e

	@property
	def minorversion(self) :
		ur"""Firmware minor version.
		"""
		try :
			return self._minorversion
		except Exception as e:
			raise e

	@property
	def fipshwmajorversion(self) :
		ur"""FIPS card hardware major version.
		"""
		try :
			return self._fipshwmajorversion
		except Exception as e:
			raise e

	@property
	def fipshwminorversion(self) :
		ur"""FIPS card hardware minor version.
		"""
		try :
			return self._fipshwminorversion
		except Exception as e:
			raise e

	@property
	def fipshwversionstring(self) :
		ur"""FIPS card hardware extended version string.
		"""
		try :
			return self._fipshwversionstring
		except Exception as e:
			raise e

	@property
	def flashmemorytotal(self) :
		ur"""Total size of the flash memory on card.
		"""
		try :
			return self._flashmemorytotal
		except Exception as e:
			raise e

	@property
	def flashmemoryfree(self) :
		ur"""Total size of free flash memory.
		"""
		try :
			return self._flashmemoryfree
		except Exception as e:
			raise e

	@property
	def sramtotal(self) :
		ur"""Total size of the SRAM memory on card.
		"""
		try :
			return self._sramtotal
		except Exception as e:
			raise e

	@property
	def sramfree(self) :
		ur"""Total size of free SRAM memory.
		"""
		try :
			return self._sramfree
		except Exception as e:
			raise e

	@property
	def status(self) :
		ur"""Status.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def flag(self) :
		ur"""Internal Flags.
		"""
		try :
			return self._flag
		except Exception as e:
			raise e

	@property
	def serialno(self) :
		ur"""FIPS card serial number.
		"""
		try :
			return self._serialno
		except Exception as e:
			raise e

	@property
	def model(self) :
		ur"""FIPS card model info.
		"""
		try :
			return self._model
		except Exception as e:
			raise e

	@property
	def state(self) :
		ur"""FIPS card state.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def firmwarereleasedate(self) :
		ur"""FIPS card firmware revision date.
		"""
		try :
			return self._firmwarereleasedate
		except Exception as e:
			raise e

	@property
	def coresmax(self) :
		ur"""Maximum number of crypto cores present in the FIPS card.
		"""
		try :
			return self._coresmax
		except Exception as e:
			raise e

	@property
	def coresenabled(self) :
		ur"""Number of crypto cores enabled in the FIPS card.
		"""
		try :
			return self._coresenabled
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslfips_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslfips
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
		ur""" Use this API to update sslfips.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslfips()
				updateresource.inithsm = resource.inithsm
				updateresource.sopassword = resource.sopassword
				updateresource.oldsopassword = resource.oldsopassword
				updateresource.userpassword = resource.userpassword
				updateresource.hsmlabel = resource.hsmlabel
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of sslfips resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslfips()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def reset(cls, client, resource) :
		ur""" Use this API to reset sslfips.
		"""
		try :
			if type(resource) is not list :
				resetresource = sslfips()
				return resetresource.perform_operation(client,"reset")
		except Exception as e :
			raise e

	@classmethod
	def change(cls, client, resource) :
		ur""" Use this API to change sslfips.
		"""
		try :
			if type(resource) is not list :
				changeresource = sslfips()
				changeresource.fipsfw = resource.fipsfw
				return changeresource.perform_operation(client,"update")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the sslfips resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslfips()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Inithsm:
		Level_2 = "Level-2"

	class Fipsfw:
		_4_6_1 = "4.6.1"

class sslfips_response(base_response) :
	def __init__(self, length=1) :
		self.sslfips = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslfips = [sslfips() for _ in range(length)]

