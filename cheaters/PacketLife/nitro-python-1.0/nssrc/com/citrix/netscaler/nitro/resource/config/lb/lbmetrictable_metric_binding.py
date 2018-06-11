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

class lbmetrictable_metric_binding(base_resource) :
	""" Binding class showing the metric that can be bound to lbmetrictable.
	"""
	def __init__(self) :
		self._metric = ""
		self._Snmpoid = ""
		self._metrictype = ""
		self._metrictable = ""
		self.___count = 0

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
	def metrictable(self) :
		ur"""Name of the metric table.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._metrictable
		except Exception as e:
			raise e

	@metrictable.setter
	def metrictable(self, metrictable) :
		ur"""Name of the metric table.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._metrictable = metrictable
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
			result = service.payload_formatter.string_to_resource(lbmetrictable_metric_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmetrictable_metric_binding
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
		try :
			if resource and type(resource) is not list :
				updateresource = lbmetrictable_metric_binding()
				updateresource.metrictable = resource.metrictable
				updateresource.metric = resource.metric
				updateresource.Snmpoid = resource.Snmpoid
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lbmetrictable_metric_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].metrictable = resource[i].metrictable
						updateresources[i].metric = resource[i].metric
						updateresources[i].Snmpoid = resource[i].Snmpoid
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = lbmetrictable_metric_binding()
				deleteresource.metrictable = resource.metrictable
				deleteresource.metric = resource.metric
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lbmetrictable_metric_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i].metrictable = resource[i].metrictable
						deleteresources[i].metric = resource[i].metric
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, metrictable) :
		ur""" Use this API to fetch lbmetrictable_metric_binding resources.
		"""
		try :
			obj = lbmetrictable_metric_binding()
			obj.metrictable = metrictable
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, metrictable, filter_) :
		ur""" Use this API to fetch filtered set of lbmetrictable_metric_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmetrictable_metric_binding()
			obj.metrictable = metrictable
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, metrictable) :
		ur""" Use this API to count lbmetrictable_metric_binding resources configued on NetScaler.
		"""
		try :
			obj = lbmetrictable_metric_binding()
			obj.metrictable = metrictable
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, metrictable, filter_) :
		ur""" Use this API to count the filtered set of lbmetrictable_metric_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmetrictable_metric_binding()
			obj.metrictable = metrictable
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Metrictype:
		INTERNAL = "INTERNAL"
		CONFIGURED = "CONFIGURED"

class lbmetrictable_metric_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbmetrictable_metric_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmetrictable_metric_binding = [lbmetrictable_metric_binding() for _ in range(length)]

