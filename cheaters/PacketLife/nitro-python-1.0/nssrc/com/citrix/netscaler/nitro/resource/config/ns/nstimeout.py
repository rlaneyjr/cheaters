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

class nstimeout(base_resource) :
	""" Configuration for timeout resource. """
	def __init__(self) :
		self._zombie = 0
		self._client = 0
		self._server = 0
		self._httpclient = 0
		self._httpserver = 0
		self._tcpclient = 0
		self._tcpserver = 0
		self._anyclient = 0
		self._anyserver = 0
		self._halfclose = 0
		self._nontcpzombie = 0
		self._reducedfintimeout = 0
		self._reducedrsttimeout = 0
		self._newconnidletimeout = 0

	@property
	def zombie(self) :
		ur"""Interval, in seconds, at which the NetScaler zombie cleanup process must run. This process cleans up inactive TCP connections.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  600.
		"""
		try :
			return self._zombie
		except Exception as e:
			raise e

	@zombie.setter
	def zombie(self, zombie) :
		ur"""Interval, in seconds, at which the NetScaler zombie cleanup process must run. This process cleans up inactive TCP connections.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  600
		"""
		try :
			self._zombie = zombie
		except Exception as e:
			raise e

	@property
	def client(self) :
		ur"""Client idle timeout (in seconds).  If zero, the service-type default value is taken when service is created.<br/>Maximum length =  18000.
		"""
		try :
			return self._client
		except Exception as e:
			raise e

	@client.setter
	def client(self, client) :
		ur"""Client idle timeout (in seconds).  If zero, the service-type default value is taken when service is created.<br/>Maximum length =  18000
		"""
		try :
			self._client = client
		except Exception as e:
			raise e

	@property
	def server(self) :
		ur"""Server idle timeout (in seconds).  If zero, the service-type default is taken when service is created.<br/>Maximum length =  18000.
		"""
		try :
			return self._server
		except Exception as e:
			raise e

	@server.setter
	def server(self, server) :
		ur"""Server idle timeout (in seconds).  If zero, the service-type default is taken when service is created.<br/>Maximum length =  18000
		"""
		try :
			self._server = server
		except Exception as e:
			raise e

	@property
	def httpclient(self) :
		ur"""Global idle timeout, in seconds, for client connections of HTTP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Maximum length =  18000.
		"""
		try :
			return self._httpclient
		except Exception as e:
			raise e

	@httpclient.setter
	def httpclient(self, httpclient) :
		ur"""Global idle timeout, in seconds, for client connections of HTTP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Maximum length =  18000
		"""
		try :
			self._httpclient = httpclient
		except Exception as e:
			raise e

	@property
	def httpserver(self) :
		ur"""Global idle timeout, in seconds, for server connections of HTTP service type. This value is over ridden by the server timeout that is configured on individual entities.<br/>Maximum length =  18000.
		"""
		try :
			return self._httpserver
		except Exception as e:
			raise e

	@httpserver.setter
	def httpserver(self, httpserver) :
		ur"""Global idle timeout, in seconds, for server connections of HTTP service type. This value is over ridden by the server timeout that is configured on individual entities.<br/>Maximum length =  18000
		"""
		try :
			self._httpserver = httpserver
		except Exception as e:
			raise e

	@property
	def tcpclient(self) :
		ur"""Global idle timeout, in seconds, for non-HTTP client connections of TCP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Maximum length =  18000.
		"""
		try :
			return self._tcpclient
		except Exception as e:
			raise e

	@tcpclient.setter
	def tcpclient(self, tcpclient) :
		ur"""Global idle timeout, in seconds, for non-HTTP client connections of TCP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Maximum length =  18000
		"""
		try :
			self._tcpclient = tcpclient
		except Exception as e:
			raise e

	@property
	def tcpserver(self) :
		ur"""Global idle timeout, in seconds, for non-HTTP server connections of TCP service type. This value is over ridden by the server timeout that is configured on entities.<br/>Maximum length =  18000.
		"""
		try :
			return self._tcpserver
		except Exception as e:
			raise e

	@tcpserver.setter
	def tcpserver(self, tcpserver) :
		ur"""Global idle timeout, in seconds, for non-HTTP server connections of TCP service type. This value is over ridden by the server timeout that is configured on entities.<br/>Maximum length =  18000
		"""
		try :
			self._tcpserver = tcpserver
		except Exception as e:
			raise e

	@property
	def anyclient(self) :
		ur"""Global idle timeout, in seconds, for non-TCP client connections. This value is over ridden by the client timeout that is configured on individual entities.<br/>Maximum length =  31536000.
		"""
		try :
			return self._anyclient
		except Exception as e:
			raise e

	@anyclient.setter
	def anyclient(self, anyclient) :
		ur"""Global idle timeout, in seconds, for non-TCP client connections. This value is over ridden by the client timeout that is configured on individual entities.<br/>Maximum length =  31536000
		"""
		try :
			self._anyclient = anyclient
		except Exception as e:
			raise e

	@property
	def anyserver(self) :
		ur"""Global idle timeout, in seconds, for non TCP server connections. This value is over ridden by the server timeout that is configured on individual entities.<br/>Maximum length =  31536000.
		"""
		try :
			return self._anyserver
		except Exception as e:
			raise e

	@anyserver.setter
	def anyserver(self, anyserver) :
		ur"""Global idle timeout, in seconds, for non TCP server connections. This value is over ridden by the server timeout that is configured on individual entities.<br/>Maximum length =  31536000
		"""
		try :
			self._anyserver = anyserver
		except Exception as e:
			raise e

	@property
	def halfclose(self) :
		ur"""Idle timeout, in seconds, for connections that are in TCP half-closed state.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  600.
		"""
		try :
			return self._halfclose
		except Exception as e:
			raise e

	@halfclose.setter
	def halfclose(self, halfclose) :
		ur"""Idle timeout, in seconds, for connections that are in TCP half-closed state.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  600
		"""
		try :
			self._halfclose = halfclose
		except Exception as e:
			raise e

	@property
	def nontcpzombie(self) :
		ur"""Interval at which the zombie clean-up process for non-TCP connections should run. Inactive IP NAT connections will be cleaned up.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  600.
		"""
		try :
			return self._nontcpzombie
		except Exception as e:
			raise e

	@nontcpzombie.setter
	def nontcpzombie(self, nontcpzombie) :
		ur"""Interval at which the zombie clean-up process for non-TCP connections should run. Inactive IP NAT connections will be cleaned up.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  600
		"""
		try :
			self._nontcpzombie = nontcpzombie
		except Exception as e:
			raise e

	@property
	def reducedfintimeout(self) :
		ur"""Alternative idle timeout for new TCP NATPCB connections.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  300.
		"""
		try :
			return self._reducedfintimeout
		except Exception as e:
			raise e

	@reducedfintimeout.setter
	def reducedfintimeout(self, reducedfintimeout) :
		ur"""Alternative idle timeout for new TCP NATPCB connections.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  300
		"""
		try :
			self._reducedfintimeout = reducedfintimeout
		except Exception as e:
			raise e

	@property
	def reducedrsttimeout(self) :
		ur"""Timer interval(in seconds) for NATPCB for tcp flow.<br/>Default value: 0<br/>Maximum length =  300.
		"""
		try :
			return self._reducedrsttimeout
		except Exception as e:
			raise e

	@reducedrsttimeout.setter
	def reducedrsttimeout(self, reducedrsttimeout) :
		ur"""Timer interval(in seconds) for NATPCB for tcp flow.<br/>Default value: 0<br/>Maximum length =  300
		"""
		try :
			self._reducedrsttimeout = reducedrsttimeout
		except Exception as e:
			raise e

	@property
	def newconnidletimeout(self) :
		ur"""Timer interval(in seconds) for new NATPCB for tcp connections.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  120.
		"""
		try :
			return self._newconnidletimeout
		except Exception as e:
			raise e

	@newconnidletimeout.setter
	def newconnidletimeout(self, newconnidletimeout) :
		ur"""Timer interval(in seconds) for new NATPCB for tcp connections.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  120
		"""
		try :
			self._newconnidletimeout = newconnidletimeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstimeout_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstimeout
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
		ur""" Use this API to update nstimeout.
		"""
		try :
			if type(resource) is not list :
				updateresource = nstimeout()
				updateresource.zombie = resource.zombie
				updateresource.client = resource.client
				updateresource.server = resource.server
				updateresource.httpclient = resource.httpclient
				updateresource.httpserver = resource.httpserver
				updateresource.tcpclient = resource.tcpclient
				updateresource.tcpserver = resource.tcpserver
				updateresource.anyclient = resource.anyclient
				updateresource.anyserver = resource.anyserver
				updateresource.halfclose = resource.halfclose
				updateresource.nontcpzombie = resource.nontcpzombie
				updateresource.reducedfintimeout = resource.reducedfintimeout
				updateresource.reducedrsttimeout = resource.reducedrsttimeout
				updateresource.newconnidletimeout = resource.newconnidletimeout
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nstimeout resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nstimeout()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nstimeout resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nstimeout()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nstimeout_response(base_response) :
	def __init__(self, length=1) :
		self.nstimeout = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstimeout = [nstimeout() for _ in range(length)]

