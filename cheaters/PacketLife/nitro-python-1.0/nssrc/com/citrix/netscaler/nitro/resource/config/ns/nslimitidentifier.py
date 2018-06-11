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

class nslimitidentifier(base_resource) :
	""" Configuration for limit Indetifier resource. """
	def __init__(self) :
		self._limitidentifier = ""
		self._threshold = 0
		self._timeslice = 0
		self._mode = ""
		self._limittype = ""
		self._selectorname = ""
		self._maxbandwidth = 0
		self._trapsintimeslice = 0
		self._ngname = ""
		self._hits = 0
		self._drop = 0
		self._rule = []
		self._time = 0
		self._total = 0
		self._trapscomputedintimeslice = 0
		self._computedtraptimeslice = 0
		self._referencecount = 0
		self.___count = 0

	@property
	def limitidentifier(self) :
		ur"""Name for a rate limit identifier. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Reserved words must not be used.
		"""
		try :
			return self._limitidentifier
		except Exception as e:
			raise e

	@limitidentifier.setter
	def limitidentifier(self, limitidentifier) :
		ur"""Name for a rate limit identifier. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Reserved words must not be used.
		"""
		try :
			self._limitidentifier = limitidentifier
		except Exception as e:
			raise e

	@property
	def threshold(self) :
		ur"""Maximum number of requests that are allowed in the given timeslice when requests (mode is set as REQUEST_RATE) are tracked per timeslice.
		When connections (mode is set as CONNECTION) are tracked, it is the total number of connections that would be let through.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._threshold
		except Exception as e:
			raise e

	@threshold.setter
	def threshold(self, threshold) :
		ur"""Maximum number of requests that are allowed in the given timeslice when requests (mode is set as REQUEST_RATE) are tracked per timeslice.
		When connections (mode is set as CONNECTION) are tracked, it is the total number of connections that would be let through.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._threshold = threshold
		except Exception as e:
			raise e

	@property
	def timeslice(self) :
		ur"""Time interval, in milliseconds, specified in multiples of 10, during which requests are tracked to check if they cross the threshold. This argument is needed only when the mode is set to REQUEST_RATE.<br/>Default value: 1000<br/>Minimum length =  10.
		"""
		try :
			return self._timeslice
		except Exception as e:
			raise e

	@timeslice.setter
	def timeslice(self, timeslice) :
		ur"""Time interval, in milliseconds, specified in multiples of 10, during which requests are tracked to check if they cross the threshold. This argument is needed only when the mode is set to REQUEST_RATE.<br/>Default value: 1000<br/>Minimum length =  10
		"""
		try :
			self._timeslice = timeslice
		except Exception as e:
			raise e

	@property
	def mode(self) :
		ur"""Defines the type of traffic to be tracked.
		* REQUEST_RATE - Tracks requests/timeslice.
		* CONNECTION - Tracks active transactions.
		Examples
		1. To permit 20 requests in 10 ms and 2 traps in 10 ms:
		add limitidentifier limit_req -mode request_rate -limitType smooth -timeslice 1000 -Threshold 2000 -trapsInTimeSlice 200
		2. To permit 50 requests in 10 ms:
		set  limitidentifier limit_req -mode request_rate -timeslice 1000 -Threshold 5000 -limitType smooth
		3. To permit 1 request in 40 ms:
		set limitidentifier limit_req -mode request_rate -timeslice 2000 -Threshold 50 -limitType smooth
		4. To permit 1 request in 200 ms and 1 trap in 130 ms:
		set limitidentifier limit_req -mode request_rate -timeslice 1000 -Threshold 5 -limitType smooth -trapsInTimeSlice 8
		5. To permit 5000 requests in 1000 ms and 200 traps in 1000 ms:
		set limitidentifier limit_req  -mode request_rate -timeslice 1000 -Threshold 5000 -limitType BURSTY.<br/>Default value: REQUEST_RATE<br/>Possible values = CONNECTION, REQUEST_RATE, NONE.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		ur"""Defines the type of traffic to be tracked.
		* REQUEST_RATE - Tracks requests/timeslice.
		* CONNECTION - Tracks active transactions.
		Examples
		1. To permit 20 requests in 10 ms and 2 traps in 10 ms:
		add limitidentifier limit_req -mode request_rate -limitType smooth -timeslice 1000 -Threshold 2000 -trapsInTimeSlice 200
		2. To permit 50 requests in 10 ms:
		set  limitidentifier limit_req -mode request_rate -timeslice 1000 -Threshold 5000 -limitType smooth
		3. To permit 1 request in 40 ms:
		set limitidentifier limit_req -mode request_rate -timeslice 2000 -Threshold 50 -limitType smooth
		4. To permit 1 request in 200 ms and 1 trap in 130 ms:
		set limitidentifier limit_req -mode request_rate -timeslice 1000 -Threshold 5 -limitType smooth -trapsInTimeSlice 8
		5. To permit 5000 requests in 1000 ms and 200 traps in 1000 ms:
		set limitidentifier limit_req  -mode request_rate -timeslice 1000 -Threshold 5000 -limitType BURSTY.<br/>Default value: REQUEST_RATE<br/>Possible values = CONNECTION, REQUEST_RATE, NONE
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	@property
	def limittype(self) :
		ur"""Smooth or bursty request type.
		* SMOOTH - When you want the permitted number of requests in a given interval of time to be spread evenly across the timeslice
		* BURSTY - When you want the permitted number of requests to exhaust the quota anytime within the timeslice.
		This argument is needed only when the mode is set to REQUEST_RATE.<br/>Default value: BURSTY<br/>Possible values = BURSTY, SMOOTH.
		"""
		try :
			return self._limittype
		except Exception as e:
			raise e

	@limittype.setter
	def limittype(self, limittype) :
		ur"""Smooth or bursty request type.
		* SMOOTH - When you want the permitted number of requests in a given interval of time to be spread evenly across the timeslice
		* BURSTY - When you want the permitted number of requests to exhaust the quota anytime within the timeslice.
		This argument is needed only when the mode is set to REQUEST_RATE.<br/>Default value: BURSTY<br/>Possible values = BURSTY, SMOOTH
		"""
		try :
			self._limittype = limittype
		except Exception as e:
			raise e

	@property
	def selectorname(self) :
		ur"""Name of the rate limit selector. If this argument is NULL, rate limiting will be applied on all traffic received by the virtual server or the NetScaler (depending on whether the limit identifier is bound to a virtual server or globally) without any filtering.<br/>Minimum length =  1.
		"""
		try :
			return self._selectorname
		except Exception as e:
			raise e

	@selectorname.setter
	def selectorname(self, selectorname) :
		ur"""Name of the rate limit selector. If this argument is NULL, rate limiting will be applied on all traffic received by the virtual server or the NetScaler (depending on whether the limit identifier is bound to a virtual server or globally) without any filtering.<br/>Minimum length =  1
		"""
		try :
			self._selectorname = selectorname
		except Exception as e:
			raise e

	@property
	def maxbandwidth(self) :
		ur"""Maximum bandwidth permitted, in kbps.<br/>Maximum length =  4294967287.
		"""
		try :
			return self._maxbandwidth
		except Exception as e:
			raise e

	@maxbandwidth.setter
	def maxbandwidth(self, maxbandwidth) :
		ur"""Maximum bandwidth permitted, in kbps.<br/>Maximum length =  4294967287
		"""
		try :
			self._maxbandwidth = maxbandwidth
		except Exception as e:
			raise e

	@property
	def trapsintimeslice(self) :
		ur"""Number of traps to be sent in the timeslice configured. A value of 0 indicates that traps are disabled.<br/>Maximum length =  65535.
		"""
		try :
			return self._trapsintimeslice
		except Exception as e:
			raise e

	@trapsintimeslice.setter
	def trapsintimeslice(self, trapsintimeslice) :
		ur"""Number of traps to be sent in the timeslice configured. A value of 0 indicates that traps are disabled.<br/>Maximum length =  65535
		"""
		try :
			self._trapsintimeslice = trapsintimeslice
		except Exception as e:
			raise e

	@property
	def ngname(self) :
		ur"""Nodegroup name to which this identifier belongs to.
		"""
		try :
			return self._ngname
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""The number of times this identifier was evaluated.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def drop(self) :
		ur"""The number of times action was taken.
		"""
		try :
			return self._drop
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Rule.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@property
	def time(self) :
		ur"""Time interval considered for rate limiting.
		"""
		try :
			return self._time
		except Exception as e:
			raise e

	@property
	def total(self) :
		ur"""Maximum number of requests permitted in the computed timeslice.
		"""
		try :
			return self._total
		except Exception as e:
			raise e

	@property
	def trapscomputedintimeslice(self) :
		ur"""The number of traps that would be sent in the timeslice configured. .
		"""
		try :
			return self._trapscomputedintimeslice
		except Exception as e:
			raise e

	@property
	def computedtraptimeslice(self) :
		ur"""The time interval computed for sending traps.
		"""
		try :
			return self._computedtraptimeslice
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		ur"""Total number of transactions pointing to this entry.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslimitidentifier_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslimitidentifier
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.limitidentifier is not None :
				return str(self.limitidentifier)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add nslimitidentifier.
		"""
		try :
			if type(resource) is not list :
				addresource = nslimitidentifier()
				addresource.limitidentifier = resource.limitidentifier
				addresource.threshold = resource.threshold
				addresource.timeslice = resource.timeslice
				addresource.mode = resource.mode
				addresource.limittype = resource.limittype
				addresource.selectorname = resource.selectorname
				addresource.maxbandwidth = resource.maxbandwidth
				addresource.trapsintimeslice = resource.trapsintimeslice
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nslimitidentifier() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].limitidentifier = resource[i].limitidentifier
						addresources[i].threshold = resource[i].threshold
						addresources[i].timeslice = resource[i].timeslice
						addresources[i].mode = resource[i].mode
						addresources[i].limittype = resource[i].limittype
						addresources[i].selectorname = resource[i].selectorname
						addresources[i].maxbandwidth = resource[i].maxbandwidth
						addresources[i].trapsintimeslice = resource[i].trapsintimeslice
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nslimitidentifier.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nslimitidentifier()
				if type(resource) !=  type(deleteresource):
					deleteresource.limitidentifier = resource
				else :
					deleteresource.limitidentifier = resource.limitidentifier
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslimitidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].limitidentifier = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslimitidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].limitidentifier = resource[i].limitidentifier
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nslimitidentifier.
		"""
		try :
			if type(resource) is not list :
				updateresource = nslimitidentifier()
				updateresource.limitidentifier = resource.limitidentifier
				updateresource.threshold = resource.threshold
				updateresource.timeslice = resource.timeslice
				updateresource.mode = resource.mode
				updateresource.limittype = resource.limittype
				updateresource.selectorname = resource.selectorname
				updateresource.maxbandwidth = resource.maxbandwidth
				updateresource.trapsintimeslice = resource.trapsintimeslice
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nslimitidentifier() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].limitidentifier = resource[i].limitidentifier
						updateresources[i].threshold = resource[i].threshold
						updateresources[i].timeslice = resource[i].timeslice
						updateresources[i].mode = resource[i].mode
						updateresources[i].limittype = resource[i].limittype
						updateresources[i].selectorname = resource[i].selectorname
						updateresources[i].maxbandwidth = resource[i].maxbandwidth
						updateresources[i].trapsintimeslice = resource[i].trapsintimeslice
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nslimitidentifier resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nslimitidentifier()
				if type(resource) !=  type(unsetresource):
					unsetresource.limitidentifier = resource
				else :
					unsetresource.limitidentifier = resource.limitidentifier
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nslimitidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].limitidentifier = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nslimitidentifier() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].limitidentifier = resource[i].limitidentifier
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nslimitidentifier resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nslimitidentifier()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nslimitidentifier()
						obj.limitidentifier = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nslimitidentifier() for _ in range(len(name))]
							obj = [nslimitidentifier() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nslimitidentifier()
								obj[i].limitidentifier = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nslimitidentifier resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslimitidentifier()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nslimitidentifier resources configured on NetScaler.
		"""
		try :
			obj = nslimitidentifier()
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
		ur""" Use this API to count filtered the set of nslimitidentifier resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslimitidentifier()
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
		CONNECTION = "CONNECTION"
		REQUEST_RATE = "REQUEST_RATE"
		NONE = "NONE"

	class Limittype:
		BURSTY = "BURSTY"
		SMOOTH = "SMOOTH"

class nslimitidentifier_response(base_response) :
	def __init__(self, length=1) :
		self.nslimitidentifier = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslimitidentifier = [nslimitidentifier() for _ in range(length)]

