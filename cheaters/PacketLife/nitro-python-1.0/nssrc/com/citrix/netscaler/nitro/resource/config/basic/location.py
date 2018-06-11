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

class location(base_resource) :
	""" Configuration for location resource. """
	def __init__(self) :
		self._ipfrom = ""
		self._ipto = ""
		self._preferredlocation = ""
		self._longitude = 0
		self._latitude = 0
		self._q1label = ""
		self._q2label = ""
		self._q3label = ""
		self._q4label = ""
		self._q5label = ""
		self._q6label = ""
		self.___count = 0

	@property
	def ipfrom(self) :
		ur"""First IP address in the range, in dotted decimal notation.<br/>Minimum length =  1.
		"""
		try :
			return self._ipfrom
		except Exception as e:
			raise e

	@ipfrom.setter
	def ipfrom(self, ipfrom) :
		ur"""First IP address in the range, in dotted decimal notation.<br/>Minimum length =  1
		"""
		try :
			self._ipfrom = ipfrom
		except Exception as e:
			raise e

	@property
	def ipto(self) :
		ur"""Last IP address in the range, in dotted decimal notation.<br/>Minimum length =  1.
		"""
		try :
			return self._ipto
		except Exception as e:
			raise e

	@ipto.setter
	def ipto(self, ipto) :
		ur"""Last IP address in the range, in dotted decimal notation.<br/>Minimum length =  1
		"""
		try :
			self._ipto = ipto
		except Exception as e:
			raise e

	@property
	def preferredlocation(self) :
		ur"""String of qualifiers, in dotted notation, describing the geographical location of the IP address range. Each qualifier is more specific than the one that precedes it, as in continent.country.region.city.isp.organization. For example, "NA.US.CA.San Jose.ATT.citrix". 
		Note: A qualifier that includes a dot (.) or space ( ) must be enclosed in double quotation marks.<br/>Minimum length =  1.
		"""
		try :
			return self._preferredlocation
		except Exception as e:
			raise e

	@preferredlocation.setter
	def preferredlocation(self, preferredlocation) :
		ur"""String of qualifiers, in dotted notation, describing the geographical location of the IP address range. Each qualifier is more specific than the one that precedes it, as in continent.country.region.city.isp.organization. For example, "NA.US.CA.San Jose.ATT.citrix". 
		Note: A qualifier that includes a dot (.) or space ( ) must be enclosed in double quotation marks.<br/>Minimum length =  1
		"""
		try :
			self._preferredlocation = preferredlocation
		except Exception as e:
			raise e

	@property
	def longitude(self) :
		ur"""Numerical value, in degrees, specifying the longitude of the geographical location of the IP address-range. 
		Note: Longitude and latitude parameters are used for selecting a service with the static proximity GSLB method. If they are not specified, selection is based on the qualifiers specified for the location.<br/>Minimum length =  -180<br/>Maximum length =  180.
		"""
		try :
			return self._longitude
		except Exception as e:
			raise e

	@longitude.setter
	def longitude(self, longitude) :
		ur"""Numerical value, in degrees, specifying the longitude of the geographical location of the IP address-range. 
		Note: Longitude and latitude parameters are used for selecting a service with the static proximity GSLB method. If they are not specified, selection is based on the qualifiers specified for the location.<br/>Minimum length =  -180<br/>Maximum length =  180
		"""
		try :
			self._longitude = longitude
		except Exception as e:
			raise e

	@property
	def latitude(self) :
		ur"""Numerical value, in degrees, specifying the latitude of the geographical location of the IP address-range. 
		Note: Longitude and latitude parameters are used for selecting a service with the static proximity GSLB method. If they are not specified, selection is based on the qualifiers specified for the location.<br/>Minimum length =  -90<br/>Maximum length =  90.
		"""
		try :
			return self._latitude
		except Exception as e:
			raise e

	@latitude.setter
	def latitude(self, latitude) :
		ur"""Numerical value, in degrees, specifying the latitude of the geographical location of the IP address-range. 
		Note: Longitude and latitude parameters are used for selecting a service with the static proximity GSLB method. If they are not specified, selection is based on the qualifiers specified for the location.<br/>Minimum length =  -90<br/>Maximum length =  90
		"""
		try :
			self._latitude = latitude
		except Exception as e:
			raise e

	@property
	def q1label(self) :
		ur"""Least specific location qualifier.
		"""
		try :
			return self._q1label
		except Exception as e:
			raise e

	@property
	def q2label(self) :
		ur"""Location qualifier 2.
		"""
		try :
			return self._q2label
		except Exception as e:
			raise e

	@property
	def q3label(self) :
		ur"""Location qualifier 3.
		"""
		try :
			return self._q3label
		except Exception as e:
			raise e

	@property
	def q4label(self) :
		ur"""Location qualifier 4.
		"""
		try :
			return self._q4label
		except Exception as e:
			raise e

	@property
	def q5label(self) :
		ur"""Location qualifier 5.
		"""
		try :
			return self._q5label
		except Exception as e:
			raise e

	@property
	def q6label(self) :
		ur"""Most specific location qualifier.
		"""
		try :
			return self._q6label
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(location_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.location
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.ipfrom is not None :
				return str(self.ipfrom)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add location.
		"""
		try :
			if type(resource) is not list :
				addresource = location()
				addresource.ipfrom = resource.ipfrom
				addresource.ipto = resource.ipto
				addresource.preferredlocation = resource.preferredlocation
				addresource.longitude = resource.longitude
				addresource.latitude = resource.latitude
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ location() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].ipfrom = resource[i].ipfrom
						addresources[i].ipto = resource[i].ipto
						addresources[i].preferredlocation = resource[i].preferredlocation
						addresources[i].longitude = resource[i].longitude
						addresources[i].latitude = resource[i].latitude
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete location.
		"""
		try :
			if type(resource) is not list :
				deleteresource = location()
				if type(resource) !=  type(deleteresource):
					deleteresource.ipfrom = resource
				else :
					deleteresource.ipfrom = resource.ipfrom
					deleteresource.ipto = resource.ipto
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ location() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipfrom = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ location() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].ipfrom = resource[i].ipfrom
							deleteresources[i].ipto = resource[i].ipto
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the location resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = location()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = location()
						obj.ipfrom = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [location() for _ in range(len(name))]
							obj = [location() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = location()
								obj[i].ipfrom = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of location resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = location()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the location resources configured on NetScaler.
		"""
		try :
			obj = location()
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
		ur""" Use this API to count filtered the set of location resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = location()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class location_response(base_response) :
	def __init__(self, length=1) :
		self.location = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.location = [location() for _ in range(length)]

