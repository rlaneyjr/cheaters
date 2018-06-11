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

class clusternodegroup_binding(base_resource):
	""" Binding class showing the resources that can be bound to clusternodegroup_binding. 
	"""
	def __init__(self) :
		self._name = ""
		self.clusternodegroup_csvserver_binding = []
		self.clusternodegroup_gslbsite_binding = []
		self.clusternodegroup_nslimitidentifier_binding = []
		self.clusternodegroup_clusternode_binding = []
		self.clusternodegroup_lbvserver_binding = []
		self.clusternodegroup_vpnvserver_binding = []
		self.clusternodegroup_service_binding = []
		self.clusternodegroup_streamidentifier_binding = []
		self.clusternodegroup_gslbvserver_binding = []
		self.clusternodegroup_authenticationvserver_binding = []
		self.clusternodegroup_crvserver_binding = []

	@property
	def name(self) :
		ur"""Name of the nodegroup to be displayed. If a name is not provided, information about all nodegroups is displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name of the nodegroup to be displayed. If a name is not provided, information about all nodegroups is displayed.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clusternodegroup_csvserver_bindings(self) :
		ur"""csvserver that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_csvserver_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_vpnvserver_bindings(self) :
		ur"""vpnvserver that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_vpnvserver_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_crvserver_bindings(self) :
		ur"""crvserver that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_crvserver_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_nslimitidentifier_bindings(self) :
		ur"""nslimitidentifier that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_nslimitidentifier_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_gslbsite_bindings(self) :
		ur"""gslbsite that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_gslbsite_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_clusternode_bindings(self) :
		ur"""clusternode that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_clusternode_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_authenticationvserver_bindings(self) :
		ur"""authenticationvserver that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_authenticationvserver_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_lbvserver_bindings(self) :
		ur"""lbvserver that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_lbvserver_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_gslbvserver_bindings(self) :
		ur"""gslbvserver that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_gslbvserver_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_streamidentifier_bindings(self) :
		ur"""streamidentifier that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_streamidentifier_binding
		except Exception as e:
			raise e

	@property
	def clusternodegroup_service_bindings(self) :
		ur"""service that can be bound to clusternodegroup.
		"""
		try :
			return self._clusternodegroup_service_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusternodegroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusternodegroup_binding
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
	def get(self, service, name) :
		ur""" Use this API to fetch clusternodegroup_binding resource.
		"""
		try :
			if type(name) is not list :
				obj = clusternodegroup_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [clusternodegroup_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class clusternodegroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.clusternodegroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusternodegroup_binding = [clusternodegroup_binding() for _ in range(length)]

