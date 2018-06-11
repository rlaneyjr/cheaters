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

class pqpolicy(base_resource) :
	""" Configuration for PQ policy resource. """
	def __init__(self) :
		self._policyname = ""
		self._rule = ""
		self._priority = 0
		self._weight = 0
		self._qdepth = 0
		self._polqdepth = 0
		self._hits = 0
		self.___count = 0

	@property
	def policyname(self) :
		ur"""Name for the priority queuing policy. Must begin with a letter, number, or the underscore symbol (_). Other characters allowed, after the first character, are the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), and colon (:) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		ur"""Name for the priority queuing policy. Must begin with a letter, number, or the underscore symbol (_). Other characters allowed, after the first character, are the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), and colon (:) characters.<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def rule(self) :
		ur"""Expression or name of a named expression, against which the request is evaluated. The priority queuing policy is applied if the rule evaluates to true.
		Note:
		* On the command line interface, if the expression includes blank spaces, the entire expression must be enclosed in double quotation marks.
		* If the expression itself includes double quotation marks, you must escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you will not have to escape the double quotation marks.
		* Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		ur"""Expression or name of a named expression, against which the request is evaluated. The priority queuing policy is applied if the rule evaluates to true.
		Note:
		* On the command line interface, if the expression includes blank spaces, the entire expression must be enclosed in double quotation marks.
		* If the expression itself includes double quotation marks, you must escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you will not have to escape the double quotation marks.
		* Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'.
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Priority for queuing the request. If server resources are not available for a request that matches the configured rule, this option specifies a priority for queuing the request until the server resources are available again. Enter the value of positive_integer as 1, 2 or 3. The highest priority level is 1 and the lowest priority value is 3.<br/>Minimum length =  1<br/>Maximum length =  3.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		ur"""Priority for queuing the request. If server resources are not available for a request that matches the configured rule, this option specifies a priority for queuing the request until the server resources are available again. Enter the value of positive_integer as 1, 2 or 3. The highest priority level is 1 and the lowest priority value is 3.<br/>Minimum length =  1<br/>Maximum length =  3
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def weight(self) :
		ur"""Weight of the priority. Each priority is assigned a weight according to which it is served when server resources are available. The weight for a higher priority request must be set higher than that of a lower priority request.
		To prevent delays for low-priority requests across multiple priority levels, you can configure weighted queuing for serving requests. The default weights for the priorities
		are:
		* Gold - Priority 1 - Weight 3
		* Silver - Priority 2 - Weight 2
		* Bronze - Priority 3 - Weight 1
		Specify the weights as 0 through 101. A weight of 0 indicates that the particular priority level should be served only when there are no requests in any of the priority queues.
		A weight of 101 specifies a weight of infinity. This means that this priority level is served irrespective of the number of clients waiting in other priority queues.<br/>Maximum length =  101.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		ur"""Weight of the priority. Each priority is assigned a weight according to which it is served when server resources are available. The weight for a higher priority request must be set higher than that of a lower priority request.
		To prevent delays for low-priority requests across multiple priority levels, you can configure weighted queuing for serving requests. The default weights for the priorities
		are:
		* Gold - Priority 1 - Weight 3
		* Silver - Priority 2 - Weight 2
		* Bronze - Priority 3 - Weight 1
		Specify the weights as 0 through 101. A weight of 0 indicates that the particular priority level should be served only when there are no requests in any of the priority queues.
		A weight of 101 specifies a weight of infinity. This means that this priority level is served irrespective of the number of clients waiting in other priority queues.<br/>Maximum length =  101
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def qdepth(self) :
		ur"""Queue depth threshold value. When the queue size (number of requests in the queue) on the virtual server to which this policy is bound, increases to the specified qDepth value, subsequent requests are dropped to the lowest priority level.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._qdepth
		except Exception as e:
			raise e

	@qdepth.setter
	def qdepth(self, qdepth) :
		ur"""Queue depth threshold value. When the queue size (number of requests in the queue) on the virtual server to which this policy is bound, increases to the specified qDepth value, subsequent requests are dropped to the lowest priority level.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._qdepth = qdepth
		except Exception as e:
			raise e

	@property
	def polqdepth(self) :
		ur"""Policy queue depth threshold value. When the policy queue size (number of requests in all the queues belonging to this policy) increases to the specified polqDepth value, subsequent requests are dropped to the lowest priority level.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._polqdepth
		except Exception as e:
			raise e

	@polqdepth.setter
	def polqdepth(self, polqdepth) :
		ur"""Policy queue depth threshold value. When the policy queue size (number of requests in all the queues belonging to this policy) increases to the specified polqDepth value, subsequent requests are dropped to the lowest priority level.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._polqdepth = polqdepth
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Total number of hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(pqpolicy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pqpolicy
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add pqpolicy.
		"""
		try :
			if type(resource) is not list :
				addresource = pqpolicy()
				addresource.policyname = resource.policyname
				addresource.rule = resource.rule
				addresource.priority = resource.priority
				addresource.weight = resource.weight
				addresource.qdepth = resource.qdepth
				addresource.polqdepth = resource.polqdepth
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ pqpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].policyname = resource[i].policyname
						addresources[i].rule = resource[i].rule
						addresources[i].priority = resource[i].priority
						addresources[i].weight = resource[i].weight
						addresources[i].qdepth = resource[i].qdepth
						addresources[i].polqdepth = resource[i].polqdepth
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete pqpolicy.
		"""
		try :
			if type(resource) is not list :
				deleteresource = pqpolicy()
				if type(resource) !=  type(deleteresource):
					deleteresource.policyname = resource
				else :
					deleteresource.policyname = resource.policyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ pqpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ pqpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].policyname = resource[i].policyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update pqpolicy.
		"""
		try :
			if type(resource) is not list :
				updateresource = pqpolicy()
				updateresource.policyname = resource.policyname
				updateresource.weight = resource.weight
				updateresource.qdepth = resource.qdepth
				updateresource.polqdepth = resource.polqdepth
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ pqpolicy() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].policyname = resource[i].policyname
						updateresources[i].weight = resource[i].weight
						updateresources[i].qdepth = resource[i].qdepth
						updateresources[i].polqdepth = resource[i].polqdepth
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of pqpolicy resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = pqpolicy()
				if type(resource) !=  type(unsetresource):
					unsetresource.policyname = resource
				else :
					unsetresource.policyname = resource.policyname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ pqpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].policyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ pqpolicy() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].policyname = resource[i].policyname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the pqpolicy resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = pqpolicy()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = pqpolicy()
						obj.policyname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [pqpolicy() for _ in range(len(name))]
							obj = [pqpolicy() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = pqpolicy()
								obj[i].policyname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of pqpolicy resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = pqpolicy()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the pqpolicy resources configured on NetScaler.
		"""
		try :
			obj = pqpolicy()
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
		ur""" Use this API to count filtered the set of pqpolicy resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = pqpolicy()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class pqpolicy_response(base_response) :
	def __init__(self, length=1) :
		self.pqpolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.pqpolicy = [pqpolicy() for _ in range(length)]

