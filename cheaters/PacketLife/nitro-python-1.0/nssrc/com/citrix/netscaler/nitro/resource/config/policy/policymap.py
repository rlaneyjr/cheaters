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

class policymap(base_resource) :
	""" Configuration for map policy resource. """
	def __init__(self) :
		self._mappolicyname = ""
		self._sd = ""
		self._su = ""
		self._td = ""
		self._tu = ""
		self._targetname = ""
		self.___count = 0

	@property
	def mappolicyname(self) :
		ur"""Name for the map policy. Must begin with a letter, number, or the underscore (_) character and must consist only of letters, numbers, and the hash (#), period (.), colon (:), space ( ), at (@), equals (=), hyphen (-), and underscore (_) characters.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my map" or 'my map').<br/>Minimum length =  1.
		"""
		try :
			return self._mappolicyname
		except Exception as e:
			raise e

	@mappolicyname.setter
	def mappolicyname(self, mappolicyname) :
		ur"""Name for the map policy. Must begin with a letter, number, or the underscore (_) character and must consist only of letters, numbers, and the hash (#), period (.), colon (:), space ( ), at (@), equals (=), hyphen (-), and underscore (_) characters.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my map" or 'my map').<br/>Minimum length =  1
		"""
		try :
			self._mappolicyname = mappolicyname
		except Exception as e:
			raise e

	@property
	def sd(self) :
		ur"""Publicly known source domain name. This is the domain name with which a client request arrives at a reverse proxy virtual server for cache redirection. If you specify a source domain, you must specify a target domain.<br/>Minimum length =  1.
		"""
		try :
			return self._sd
		except Exception as e:
			raise e

	@sd.setter
	def sd(self, sd) :
		ur"""Publicly known source domain name. This is the domain name with which a client request arrives at a reverse proxy virtual server for cache redirection. If you specify a source domain, you must specify a target domain.<br/>Minimum length =  1
		"""
		try :
			self._sd = sd
		except Exception as e:
			raise e

	@property
	def su(self) :
		ur"""Source URL. Specify all or part of the source URL, in the following format: /[[prefix] [*]] [.suffix].<br/>Minimum length =  1.
		"""
		try :
			return self._su
		except Exception as e:
			raise e

	@su.setter
	def su(self, su) :
		ur"""Source URL. Specify all or part of the source URL, in the following format: /[[prefix] [*]] [.suffix].<br/>Minimum length =  1
		"""
		try :
			self._su = su
		except Exception as e:
			raise e

	@property
	def td(self) :
		ur"""Target domain name sent to the server. The source domain name is replaced with this domain name.<br/>Minimum length =  1.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		ur"""Target domain name sent to the server. The source domain name is replaced with this domain name.<br/>Minimum length =  1
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def tu(self) :
		ur"""Target URL. Specify the target URL in the following format: /[[prefix] [*]][.suffix].<br/>Minimum length =  1.
		"""
		try :
			return self._tu
		except Exception as e:
			raise e

	@tu.setter
	def tu(self, tu) :
		ur"""Target URL. Specify the target URL in the following format: /[[prefix] [*]][.suffix].<br/>Minimum length =  1
		"""
		try :
			self._tu = tu
		except Exception as e:
			raise e

	@property
	def targetname(self) :
		ur"""The expression string.
		"""
		try :
			return self._targetname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policymap_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policymap
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.mappolicyname is not None :
				return str(self.mappolicyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add policymap.
		"""
		try :
			if type(resource) is not list :
				addresource = policymap()
				addresource.mappolicyname = resource.mappolicyname
				addresource.sd = resource.sd
				addresource.su = resource.su
				addresource.td = resource.td
				addresource.tu = resource.tu
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ policymap() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].mappolicyname = resource[i].mappolicyname
						addresources[i].sd = resource[i].sd
						addresources[i].su = resource[i].su
						addresources[i].td = resource[i].td
						addresources[i].tu = resource[i].tu
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete policymap.
		"""
		try :
			if type(resource) is not list :
				deleteresource = policymap()
				if type(resource) !=  type(deleteresource):
					deleteresource.mappolicyname = resource
				else :
					deleteresource.mappolicyname = resource.mappolicyname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ policymap() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].mappolicyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ policymap() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].mappolicyname = resource[i].mappolicyname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the policymap resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = policymap()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = policymap()
						obj.mappolicyname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [policymap() for _ in range(len(name))]
							obj = [policymap() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = policymap()
								obj[i].mappolicyname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of policymap resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policymap()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the policymap resources configured on NetScaler.
		"""
		try :
			obj = policymap()
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
		ur""" Use this API to count filtered the set of policymap resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policymap()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class policymap_response(base_response) :
	def __init__(self, length=1) :
		self.policymap = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policymap = [policymap() for _ in range(length)]

