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

class locationfile(base_resource) :
	""" Configuration for location file resource. """
	def __init__(self) :
		self._Locationfile = ""
		self._format = ""

	@property
	def Locationfile(self) :
		ur"""Name of the location file, with or without absolute path. If the path is not included, the default path (/var/netscaler/locdb) is assumed. In a high availability setup, the static database must be stored in the same location on both NetScaler appliances.<br/>Minimum length =  1.
		"""
		try :
			return self._Locationfile
		except Exception as e:
			raise e

	@Locationfile.setter
	def Locationfile(self, Locationfile) :
		ur"""Name of the location file, with or without absolute path. If the path is not included, the default path (/var/netscaler/locdb) is assumed. In a high availability setup, the static database must be stored in the same location on both NetScaler appliances.<br/>Minimum length =  1
		"""
		try :
			self._Locationfile = Locationfile
		except Exception as e:
			raise e

	@property
	def format(self) :
		ur"""Format of the location file. Required for the NetScaler appliance to identify how to read the location file.<br/>Default value: netscaler<br/>Possible values = netscaler, ip-country, ip-country-isp, ip-country-region-city, ip-country-region-city-isp, geoip-country, geoip-region, geoip-city, geoip-country-org, geoip-country-isp, geoip-city-isp-org.
		"""
		try :
			return self._format
		except Exception as e:
			raise e

	@format.setter
	def format(self, format) :
		ur"""Format of the location file. Required for the NetScaler appliance to identify how to read the location file.<br/>Default value: netscaler<br/>Possible values = netscaler, ip-country, ip-country-isp, ip-country-region-city, ip-country-region-city-isp, geoip-country, geoip-region, geoip-city, geoip-country-org, geoip-country-isp, geoip-city-isp-org
		"""
		try :
			self._format = format
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(locationfile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.locationfile
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
	def add(cls, client, resource) :
		ur""" Use this API to add locationfile.
		"""
		try :
			if type(resource) is not list :
				addresource = locationfile()
				addresource.Locationfile = resource.Locationfile
				addresource.format = resource.format
				return addresource.add_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource="") :
		ur""" Use this API to delete locationfile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = locationfile()
				return deleteresource.delete_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the locationfile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = locationfile()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Format:
		netscaler = "netscaler"
		ip_country = "ip-country"
		ip_country_isp = "ip-country-isp"
		ip_country_region_city = "ip-country-region-city"
		ip_country_region_city_isp = "ip-country-region-city-isp"
		geoip_country = "geoip-country"
		geoip_region = "geoip-region"
		geoip_city = "geoip-city"
		geoip_country_org = "geoip-country-org"
		geoip_country_isp = "geoip-country-isp"
		geoip_city_isp_org = "geoip-city-isp-org"

class locationfile_response(base_response) :
	def __init__(self, length=1) :
		self.locationfile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.locationfile = [locationfile() for _ in range(length)]

