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

class gslbconfig(base_resource) :
	""" Configuration for gslb config resource. """
	def __init__(self) :
		self._preview = False
		self._debug = False
		self._forcesync = ""
		self._nowarn = False
		self._saveconfig = False
		self._command = ""

	@property
	def preview(self) :
		ur"""Do not synchronize the GSLB sites, but display the commands that would be applied on the slave node upon synchronization. Mutually exclusive with the Save Configuration option.
		"""
		try :
			return self._preview
		except Exception as e:
			raise e

	@preview.setter
	def preview(self, preview) :
		ur"""Do not synchronize the GSLB sites, but display the commands that would be applied on the slave node upon synchronization. Mutually exclusive with the Save Configuration option.
		"""
		try :
			self._preview = preview
		except Exception as e:
			raise e

	@property
	def debug(self) :
		ur"""Generate verbose output when synchronizing the GSLB sites. The Debug option generates more verbose output than the sync gslb config command in which the option is not used, and is useful for analyzing synchronization issues.
		"""
		try :
			return self._debug
		except Exception as e:
			raise e

	@debug.setter
	def debug(self, debug) :
		ur"""Generate verbose output when synchronizing the GSLB sites. The Debug option generates more verbose output than the sync gslb config command in which the option is not used, and is useful for analyzing synchronization issues.
		"""
		try :
			self._debug = debug
		except Exception as e:
			raise e

	@property
	def forcesync(self) :
		ur"""Force synchronization of the specified site even if a dependent configuration on the remote site is preventing synchronization or if one or more GSLB entities on the remote site have the same name but are of a different type. You can specify either the name of the remote site that you want to synchronize with the local site, or you can specify All Sites in the configuration utility (the string all-sites in the CLI). If you specify All Sites, all the sites in the GSLB setup are synchronized with the site on the master node. 
		Note: If you select the Force Sync option, the synchronization starts without displaying the commands that are going to be executed.
		"""
		try :
			return self._forcesync
		except Exception as e:
			raise e

	@forcesync.setter
	def forcesync(self, forcesync) :
		ur"""Force synchronization of the specified site even if a dependent configuration on the remote site is preventing synchronization or if one or more GSLB entities on the remote site have the same name but are of a different type. You can specify either the name of the remote site that you want to synchronize with the local site, or you can specify All Sites in the configuration utility (the string all-sites in the CLI). If you specify All Sites, all the sites in the GSLB setup are synchronized with the site on the master node. 
		Note: If you select the Force Sync option, the synchronization starts without displaying the commands that are going to be executed.
		"""
		try :
			self._forcesync = forcesync
		except Exception as e:
			raise e

	@property
	def nowarn(self) :
		ur"""Suppress the warning and the confirmation prompt that are displayed before site synchronization begins. This option can be used in automation scripts that must not be interrupted by a prompt.
		"""
		try :
			return self._nowarn
		except Exception as e:
			raise e

	@nowarn.setter
	def nowarn(self, nowarn) :
		ur"""Suppress the warning and the confirmation prompt that are displayed before site synchronization begins. This option can be used in automation scripts that must not be interrupted by a prompt.
		"""
		try :
			self._nowarn = nowarn
		except Exception as e:
			raise e

	@property
	def saveconfig(self) :
		ur"""Save the configuration on all the nodes participating in the synchronization process, automatically. The master saves its configuration immediately before synchronization begins. Slave nodes save their configurations after the process of synchronization is complete. A slave node saves its configuration only if the configuration difference was successfully applied to it. Mutually exclusive with the Preview option.
		"""
		try :
			return self._saveconfig
		except Exception as e:
			raise e

	@saveconfig.setter
	def saveconfig(self, saveconfig) :
		ur"""Save the configuration on all the nodes participating in the synchronization process, automatically. The master saves its configuration immediately before synchronization begins. Slave nodes save their configurations after the process of synchronization is complete. A slave node saves its configuration only if the configuration difference was successfully applied to it. Mutually exclusive with the Preview option.
		"""
		try :
			self._saveconfig = saveconfig
		except Exception as e:
			raise e

	@property
	def command(self) :
		ur"""Run the specified command on the master node and then on all the slave nodes. You cannot use this option with the force sync and preview options.
		"""
		try :
			return self._command
		except Exception as e:
			raise e

	@command.setter
	def command(self, command) :
		ur"""Run the specified command on the master node and then on all the slave nodes. You cannot use this option with the force sync and preview options.
		"""
		try :
			self._command = command
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbconfig_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbconfig
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
	def sync(cls, client, resource) :
		ur""" Use this API to sync gslbconfig.
		"""
		try :
			if type(resource) is not list :
				syncresource = gslbconfig()
				syncresource.preview = resource.preview
				syncresource.debug = resource.debug
				syncresource.forcesync = resource.forcesync
				syncresource.nowarn = resource.nowarn
				syncresource.saveconfig = resource.saveconfig
				syncresource.command = resource.command
				return syncresource.perform_operation(client,"sync")
		except Exception as e :
			raise e

class gslbconfig_response(base_response) :
	def __init__(self, length=1) :
		self.gslbconfig = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbconfig = [gslbconfig() for _ in range(length)]

