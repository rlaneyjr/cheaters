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

class rewritepolicylabel(base_resource) :
	""" Configuration for rewrite policy label resource. """
	def __init__(self) :
		self._labelname = ""
		self._transform = ""
		self._comment = ""
		self._newname = ""
		self._numpol = 0
		self._hits = 0
		self._priority = 0
		self._gotopriorityexpression = ""
		self._labeltype = ""
		self._invoke_labelname = ""
		self._flowtype = 0
		self._description = ""
		self._isdefault = False
		self._builtin = []
		self.___count = 0

	@property
	def labelname(self) :
		ur"""Name for the rewrite policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the rewrite policy label is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rewrite policy label" or 'my rewrite policy label').
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		ur"""Name for the rewrite policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the rewrite policy label is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my rewrite policy label" or 'my rewrite policy label').
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def transform(self) :
		ur"""Types of transformations allowed by the policies bound to the label. For Rewrite, the following types are supported:
		* http_req - HTTP requests
		* http_res - HTTP responses
		* othertcp_req - Non-HTTP TCP requests
		* othertcp_res - Non-HTTP TCP responses
		* url - URLs
		* text - Text strings
		* clientless_vpn_req - NetScaler clientless VPN requests
		* clientless_vpn_res - NetScaler clientless VPN responses
		* sipudp_req - SIP requests
		* sipudp_res - SIP responses
		* diameter_req - DIAMETER requests
		* diameter_res - DIAMETER responses.<br/>Possible values = http_req, http_res, othertcp_req, othertcp_res, url, text, clientless_vpn_req, clientless_vpn_res, sipudp_req, sipudp_res, diameter_req, diameter_res.
		"""
		try :
			return self._transform
		except Exception as e:
			raise e

	@transform.setter
	def transform(self, transform) :
		ur"""Types of transformations allowed by the policies bound to the label. For Rewrite, the following types are supported:
		* http_req - HTTP requests
		* http_res - HTTP responses
		* othertcp_req - Non-HTTP TCP requests
		* othertcp_res - Non-HTTP TCP responses
		* url - URLs
		* text - Text strings
		* clientless_vpn_req - NetScaler clientless VPN requests
		* clientless_vpn_res - NetScaler clientless VPN responses
		* sipudp_req - SIP requests
		* sipudp_res - SIP responses
		* diameter_req - DIAMETER requests
		* diameter_res - DIAMETER responses.<br/>Possible values = http_req, http_res, othertcp_req, othertcp_res, url, text, clientless_vpn_req, clientless_vpn_res, sipudp_req, sipudp_res, diameter_req, diameter_res
		"""
		try :
			self._transform = transform
		except Exception as e:
			raise e

	@property
	def comment(self) :
		ur"""Any comments to preserve information about this rewrite policy label.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		ur"""Any comments to preserve information about this rewrite policy label.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def newname(self) :
		ur"""New name for the rewrite policy label. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy label" or 'my policy label').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		ur"""New name for the rewrite policy label. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my policy label" or 'my policy label').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def numpol(self) :
		ur"""Number of polices bound to label.
		"""
		try :
			return self._numpol
		except Exception as e:
			raise e

	@property
	def hits(self) :
		ur"""Number of times policy label was invoked.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def priority(self) :
		ur"""Specifies the priority of the policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		ur"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		ur"""Type of invocation. Available settings function as follows:
		* reqvserver - Forward the request to the specified request virtual server.
		* resvserver - Forward the response to the specified response virtual server.
		* policylabel - Invoke the specified policy label.<br/>Possible values = reqvserver, resvserver, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def invoke_labelname(self) :
		ur"""* If labelType is policylabel, name of the policy label to invoke. 
		* If labelType is reqvserver or resvserver, name of the virtual server to which to forward the request or response.
		"""
		try :
			return self._invoke_labelname
		except Exception as e:
			raise e

	@property
	def flowtype(self) :
		ur"""Flowtype of the bound rewrite policy.
		"""
		try :
			return self._flowtype
		except Exception as e:
			raise e

	@property
	def description(self) :
		ur"""Description of the policylabel.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	@property
	def isdefault(self) :
		ur"""A value of true is returned if it is a default rewritepolicylabel.
		"""
		try :
			return self._isdefault
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		ur"""Flag to determine if rewrite policy label is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rewritepolicylabel_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rewritepolicylabel
		except Exception as e :
			raise e

	def _get_object_name(self) :
		ur""" Returns the value of object identifier argument
		"""
		try :
			if self.labelname is not None :
				return str(self.labelname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		ur""" Use this API to add rewritepolicylabel.
		"""
		try :
			if type(resource) is not list :
				addresource = rewritepolicylabel()
				addresource.labelname = resource.labelname
				addresource.transform = resource.transform
				addresource.comment = resource.comment
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ rewritepolicylabel() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].labelname = resource[i].labelname
						addresources[i].transform = resource[i].transform
						addresources[i].comment = resource[i].comment
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete rewritepolicylabel.
		"""
		try :
			if type(resource) is not list :
				deleteresource = rewritepolicylabel()
				if type(resource) !=  type(deleteresource):
					deleteresource.labelname = resource
				else :
					deleteresource.labelname = resource.labelname
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ rewritepolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ rewritepolicylabel() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].labelname = resource[i].labelname
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_labelname) :
		ur""" Use this API to rename a rewritepolicylabel resource.
		"""
		try :
			renameresource = rewritepolicylabel()
			if type(resource) == cls :
				renameresource.labelname = resource.labelname
			else :
				renameresource.labelname = resource
			return renameresource.rename_resource(client,new_labelname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the rewritepolicylabel resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = rewritepolicylabel()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = rewritepolicylabel()
						obj.labelname = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [rewritepolicylabel() for _ in range(len(name))]
							obj = [rewritepolicylabel() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = rewritepolicylabel()
								obj[i].labelname = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of rewritepolicylabel resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rewritepolicylabel()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the rewritepolicylabel resources configured on NetScaler.
		"""
		try :
			obj = rewritepolicylabel()
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
		ur""" Use this API to count filtered the set of rewritepolicylabel resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = rewritepolicylabel()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

	class Transform:
		http_req = "http_req"
		http_res = "http_res"
		othertcp_req = "othertcp_req"
		othertcp_res = "othertcp_res"
		url = "url"
		text = "text"
		clientless_vpn_req = "clientless_vpn_req"
		clientless_vpn_res = "clientless_vpn_res"
		sipudp_req = "sipudp_req"
		sipudp_res = "sipudp_res"
		diameter_req = "diameter_req"
		diameter_res = "diameter_res"

class rewritepolicylabel_response(base_response) :
	def __init__(self, length=1) :
		self.rewritepolicylabel = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rewritepolicylabel = [rewritepolicylabel() for _ in range(length)]

