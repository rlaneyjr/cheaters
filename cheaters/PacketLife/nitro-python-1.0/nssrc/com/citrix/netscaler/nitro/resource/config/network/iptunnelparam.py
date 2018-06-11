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

class iptunnelparam(base_resource) :
	""" Configuration for ip tunnel parameter resource. """
	def __init__(self) :
		self._srcip = ""
		self._dropfrag = ""
		self._dropfragcputhreshold = 0
		self._srciproundrobin = ""
		self._enablestrictrx = ""
		self._enablestricttx = ""

	@property
	def srcip(self) :
		ur"""Common source-IP address for all tunnels. For a specific tunnel, this global setting is overridden if you have specified another source IP address. Must be a MIP or SNIP address.<br/>Minimum length =  1.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		ur"""Common source-IP address for all tunnels. For a specific tunnel, this global setting is overridden if you have specified another source IP address. Must be a MIP or SNIP address.<br/>Minimum length =  1
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def dropfrag(self) :
		ur"""Drop any IP packet that requires fragmentation before it is sent through the tunnel.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._dropfrag
		except Exception as e:
			raise e

	@dropfrag.setter
	def dropfrag(self, dropfrag) :
		ur"""Drop any IP packet that requires fragmentation before it is sent through the tunnel.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._dropfrag = dropfrag
		except Exception as e:
			raise e

	@property
	def dropfragcputhreshold(self) :
		ur"""Threshold value, as a percentage of CPU usage, at which to drop packets that require fragmentation to use the IP tunnel. Applies only if dropFragparameter is set to NO. The default value, 0, specifies that this parameter is not set.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._dropfragcputhreshold
		except Exception as e:
			raise e

	@dropfragcputhreshold.setter
	def dropfragcputhreshold(self, dropfragcputhreshold) :
		ur"""Threshold value, as a percentage of CPU usage, at which to drop packets that require fragmentation to use the IP tunnel. Applies only if dropFragparameter is set to NO. The default value, 0, specifies that this parameter is not set.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._dropfragcputhreshold = dropfragcputhreshold
		except Exception as e:
			raise e

	@property
	def srciproundrobin(self) :
		ur"""Use a different source IP address for each new session through a particular IP tunnel, as determined by round robin selection of one of the SNIP addresses. This setting is ignored if a common global source IP address has been specified for all the IP tunnels. This setting does not apply to a tunnel for which a source IP address has been specified.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._srciproundrobin
		except Exception as e:
			raise e

	@srciproundrobin.setter
	def srciproundrobin(self, srciproundrobin) :
		ur"""Use a different source IP address for each new session through a particular IP tunnel, as determined by round robin selection of one of the SNIP addresses. This setting is ignored if a common global source IP address has been specified for all the IP tunnels. This setting does not apply to a tunnel for which a source IP address has been specified.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._srciproundrobin = srciproundrobin
		except Exception as e:
			raise e

	@property
	def enablestrictrx(self) :
		ur"""Strict PBR check for IPSec packets received through tunnel.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._enablestrictrx
		except Exception as e:
			raise e

	@enablestrictrx.setter
	def enablestrictrx(self, enablestrictrx) :
		ur"""Strict PBR check for IPSec packets received through tunnel.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._enablestrictrx = enablestrictrx
		except Exception as e:
			raise e

	@property
	def enablestricttx(self) :
		ur"""Strict PBR check for packets to be sent IPSec protected.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._enablestricttx
		except Exception as e:
			raise e

	@enablestricttx.setter
	def enablestricttx(self, enablestricttx) :
		ur"""Strict PBR check for packets to be sent IPSec protected.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._enablestricttx = enablestricttx
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(iptunnelparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.iptunnelparam
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
		ur""" Use this API to update iptunnelparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = iptunnelparam()
				updateresource.srcip = resource.srcip
				updateresource.dropfrag = resource.dropfrag
				updateresource.dropfragcputhreshold = resource.dropfragcputhreshold
				updateresource.srciproundrobin = resource.srciproundrobin
				updateresource.enablestrictrx = resource.enablestrictrx
				updateresource.enablestricttx = resource.enablestricttx
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of iptunnelparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = iptunnelparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the iptunnelparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = iptunnelparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Enablestrictrx:
		YES = "YES"
		NO = "NO"

	class Enablestricttx:
		YES = "YES"
		NO = "NO"

	class Dropfrag:
		YES = "YES"
		NO = "NO"

	class Srciproundrobin:
		YES = "YES"
		NO = "NO"

class iptunnelparam_response(base_response) :
	def __init__(self, length=1) :
		self.iptunnelparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.iptunnelparam = [iptunnelparam() for _ in range(length)]

