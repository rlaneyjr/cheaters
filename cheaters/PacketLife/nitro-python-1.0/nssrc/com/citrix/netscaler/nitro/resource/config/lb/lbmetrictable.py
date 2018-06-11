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

class lbmetrictable(base_resource) :
	""" Configuration for metric table resource. """
	def __init__(self) :
		self._metrictable = ""
		self._metric = ""
		self._Snmpoid = ""
		self._metrictype = ""
		self.___count = 0

	@property
	def metrictable(self) :
		ur"""Name for the metric table. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. 
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my metrictable" or 'my metrictable').<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._metrictable
		except Exception as e:
			raise e

	@metrictable.setter
	def metrictable(self, metrictable) :
		ur"""Name for the metric table. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. 
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my metrictable" or 'my metrictable').<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._metrictable = metrictable
		except Exception as e:
			raise e

	@property
	def metric(self) :
		ur"""Name of the metric for which to change the SNMP OID.<br/>Minimum length =  1.
		"""
		try :
			return self._metric
		except Exception as e:
			raise e

	@metric.setter
	def metric(self, metric) :
		ur"""Name of the metric for which to change the SNMP OID.<br/>Minimum length =  1
		"""
		try :
			self._metric = metric
		except Exception as e:
			raise e

	@property
	def Snmpoid(self) :
		ur"""New SNMP OID of the metric.<br/>Minimum length =  1.
		"""
		try :
			return self._Snmpoid
		except Exception as e:
			raise e

	@Snmpoid.setter
	def Snmpoid(self, Snmpoid) :
		ur"""New SNMP OID of the metric.<br/>Minimum length =  1
		"""
		try :
			self._Snmpoid = Snmpoid
		except Exception as e:
			raise e

	@property
	def metrictype(self) :
		ur"""Indication if it is a configured or internal.<br/>Possible values = INTERNAL, CONFIGURED.
		"""
		try :
			return self._metrictype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmetrictable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmetrictable
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.metrictable is not None :
				return str(self.metrictable)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add lbmetrictable.
		"""
		try :
			if type(resource) is not list :
				addresource = lbmetrictable()
				addresource.metrictable = resource.metrictable
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbmetrictable() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].metrictable = resource[i].metrictable
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete lbmetrictable.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbmetrictable()
				if type(resource) !=  type(deleteresource):
					deleteresource.metrictable = resource
				else :
					deleteresource.metrictable = resource.metrictable
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbmetrictable() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].metrictable = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbmetrictable() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].metrictable = resource[i].metrictable
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update lbmetrictable.
		"""
		try :
			if type(resource) is not list :
				updateresource = lbmetrictable()
				updateresource.metrictable = resource.metrictable
				updateresource.metric = resource.metric
				updateresource.Snmpoid = resource.Snmpoid
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lbmetrictable() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].metrictable = resource[i].metrictable
						updateresources[i].metric = resource[i].metric
						updateresources[i].Snmpoid = resource[i].Snmpoid
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the lbmetrictable resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbmetrictable()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = lbmetrictable()
						obj.metrictable = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [lbmetrictable() for _ in range(len(name))]
							obj = [lbmetrictable() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = lbmetrictable()
								obj[i].metrictable = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of lbmetrictable resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmetrictable()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the lbmetrictable resources configured on NetScaler.
		"""
		try :
			obj = lbmetrictable()
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
		ur""" Use this API to count filtered the set of lbmetrictable resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmetrictable()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Metrictype:
		INTERNAL = "INTERNAL"
		CONFIGURED = "CONFIGURED"

class lbmetrictable_response(base_response) :
	def __init__(self, length=1) :
		self.lbmetrictable = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmetrictable = [lbmetrictable() for _ in range(length)]

