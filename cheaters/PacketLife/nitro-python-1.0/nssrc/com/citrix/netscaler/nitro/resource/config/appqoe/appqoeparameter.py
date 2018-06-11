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

class appqoeparameter(base_resource) :
	""" Configuration for QOS parameter resource. """
	def __init__(self) :
		self._sessionlife = 0
		self._avgwaitingclient = 0
		self._maxaltrespbandwidth = 0
		self._dosattackthresh = 0

	@property
	def sessionlife(self) :
		ur"""Time, in seconds, between the first time and the next time the AppQoE alternative content window is displayed. The alternative content window is displayed only once during a session for the same browser accessing a configured URL, so this parameter determines the length of a session.<br/>Default value: 300<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._sessionlife
		except Exception as e:
			raise e

	@sessionlife.setter
	def sessionlife(self, sessionlife) :
		ur"""Time, in seconds, between the first time and the next time the AppQoE alternative content window is displayed. The alternative content window is displayed only once during a session for the same browser accessing a configured URL, so this parameter determines the length of a session.<br/>Default value: 300<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._sessionlife = sessionlife
		except Exception as e:
			raise e

	@property
	def avgwaitingclient(self) :
		ur"""average number of client connections, that can sit in service waiting queue.<br/>Default value: 1000000<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._avgwaitingclient
		except Exception as e:
			raise e

	@avgwaitingclient.setter
	def avgwaitingclient(self, avgwaitingclient) :
		ur"""average number of client connections, that can sit in service waiting queue.<br/>Default value: 1000000<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._avgwaitingclient = avgwaitingclient
		except Exception as e:
			raise e

	@property
	def maxaltrespbandwidth(self) :
		ur"""maximum bandwidth which will determine whether to send alternate content response.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._maxaltrespbandwidth
		except Exception as e:
			raise e

	@maxaltrespbandwidth.setter
	def maxaltrespbandwidth(self, maxaltrespbandwidth) :
		ur"""maximum bandwidth which will determine whether to send alternate content response.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._maxaltrespbandwidth = maxaltrespbandwidth
		except Exception as e:
			raise e

	@property
	def dosattackthresh(self) :
		ur"""average number of client connection that can queue up on vserver level without triggering DoS mitigation module.<br/>Default value: 2000<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._dosattackthresh
		except Exception as e:
			raise e

	@dosattackthresh.setter
	def dosattackthresh(self, dosattackthresh) :
		ur"""average number of client connection that can queue up on vserver level without triggering DoS mitigation module.<br/>Default value: 2000<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._dosattackthresh = dosattackthresh
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appqoeparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appqoeparameter
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
		ur""" Use this API to update appqoeparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = appqoeparameter()
				updateresource.sessionlife = resource.sessionlife
				updateresource.avgwaitingclient = resource.avgwaitingclient
				updateresource.maxaltrespbandwidth = resource.maxaltrespbandwidth
				updateresource.dosattackthresh = resource.dosattackthresh
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of appqoeparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appqoeparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the appqoeparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appqoeparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class appqoeparameter_response(base_response) :
	def __init__(self, length=1) :
		self.appqoeparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appqoeparameter = [appqoeparameter() for _ in range(length)]

