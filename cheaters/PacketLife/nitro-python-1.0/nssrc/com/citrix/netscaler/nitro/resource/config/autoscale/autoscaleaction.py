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

class autoscaleaction(base_resource) :
	""" Configuration for autoscale action resource. """
	def __init__(self) :
		self._name = ""
		self._type = ""
		self._profilename = ""
		self._parameters = ""
		self._vmdestroygraceperiod = 0
		self._quiettime = 0
		self._vserver = ""
		self.___count = 0

	@property
	def name(self) :
		ur"""ActionScale action name.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""ActionScale action name.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		ur"""The type of action.<br/>Possible values = SCALE_UP, SCALE_DOWN.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		ur"""The type of action.<br/>Possible values = SCALE_UP, SCALE_DOWN
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def profilename(self) :
		ur"""AutoScale profile name.<br/>Minimum length =  1.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@profilename.setter
	def profilename(self, profilename) :
		ur"""AutoScale profile name.<br/>Minimum length =  1
		"""
		try :
			self._profilename = profilename
		except Exception as e:
			raise e

	@property
	def parameters(self) :
		ur"""Parameters to use in the action.<br/>Minimum length =  1.
		"""
		try :
			return self._parameters
		except Exception as e:
			raise e

	@parameters.setter
	def parameters(self, parameters) :
		ur"""Parameters to use in the action.<br/>Minimum length =  1
		"""
		try :
			self._parameters = parameters
		except Exception as e:
			raise e

	@property
	def vmdestroygraceperiod(self) :
		ur"""Time in minutes a VM is kept in inactive state before destroying.<br/>Default value: 10.
		"""
		try :
			return self._vmdestroygraceperiod
		except Exception as e:
			raise e

	@vmdestroygraceperiod.setter
	def vmdestroygraceperiod(self, vmdestroygraceperiod) :
		ur"""Time in minutes a VM is kept in inactive state before destroying.<br/>Default value: 10
		"""
		try :
			self._vmdestroygraceperiod = vmdestroygraceperiod
		except Exception as e:
			raise e

	@property
	def quiettime(self) :
		ur"""Time in seconds no other policy is evaluated or action is taken.<br/>Default value: 300.
		"""
		try :
			return self._quiettime
		except Exception as e:
			raise e

	@quiettime.setter
	def quiettime(self, quiettime) :
		ur"""Time in seconds no other policy is evaluated or action is taken.<br/>Default value: 300
		"""
		try :
			self._quiettime = quiettime
		except Exception as e:
			raise e

	@property
	def vserver(self) :
		ur"""Name of the vserver on which autoscale action has to be taken.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		ur"""Name of the vserver on which autoscale action has to be taken.
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(autoscaleaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscaleaction
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
	def add(cls, client, resource) :
		ur""" Use this API to add autoscaleaction.
		"""
		try :
			if type(resource) is not list :
				addresource = autoscaleaction()
				addresource.name = resource.name
				addresource.type = resource.type
				addresource.profilename = resource.profilename
				addresource.parameters = resource.parameters
				addresource.vmdestroygraceperiod = resource.vmdestroygraceperiod
				addresource.quiettime = resource.quiettime
				addresource.vserver = resource.vserver
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ autoscaleaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].type = resource[i].type
						addresources[i].profilename = resource[i].profilename
						addresources[i].parameters = resource[i].parameters
						addresources[i].vmdestroygraceperiod = resource[i].vmdestroygraceperiod
						addresources[i].quiettime = resource[i].quiettime
						addresources[i].vserver = resource[i].vserver
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete autoscaleaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = autoscaleaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update autoscaleaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = autoscaleaction()
				updateresource.name = resource.name
				updateresource.profilename = resource.profilename
				updateresource.parameters = resource.parameters
				updateresource.vmdestroygraceperiod = resource.vmdestroygraceperiod
				updateresource.quiettime = resource.quiettime
				updateresource.vserver = resource.vserver
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ autoscaleaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].profilename = resource[i].profilename
						updateresources[i].parameters = resource[i].parameters
						updateresources[i].vmdestroygraceperiod = resource[i].vmdestroygraceperiod
						updateresources[i].quiettime = resource[i].quiettime
						updateresources[i].vserver = resource[i].vserver
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of autoscaleaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = autoscaleaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the autoscaleaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = autoscaleaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = autoscaleaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [autoscaleaction() for _ in range(len(name))]
							obj = [autoscaleaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = autoscaleaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of autoscaleaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = autoscaleaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the autoscaleaction resources configured on NetScaler.
		"""
		try :
			obj = autoscaleaction()
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
		ur""" Use this API to count filtered the set of autoscaleaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = autoscaleaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		SCALE_UP = "SCALE_UP"
		SCALE_DOWN = "SCALE_DOWN"

class autoscaleaction_response(base_response) :
	def __init__(self, length=1) :
		self.autoscaleaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.autoscaleaction = [autoscaleaction() for _ in range(length)]

