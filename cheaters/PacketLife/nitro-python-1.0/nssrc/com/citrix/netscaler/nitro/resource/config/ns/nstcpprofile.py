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

class nstcpprofile(base_resource) :
	""" Configuration for TCP profile resource. """
	def __init__(self) :
		self._name = ""
		self._ws = ""
		self._sack = ""
		self._wsval = 0
		self._nagle = ""
		self._ackonpush = ""
		self._mss = 0
		self._maxburst = 0
		self._initialcwnd = 0
		self._delayedack = 0
		self._oooqsize = 0
		self._maxpktpermss = 0
		self._pktperretx = 0
		self._minrto = 0
		self._slowstartincr = 0
		self._buffersize = 0
		self._syncookie = ""
		self._kaprobeupdatelastactivity = ""
		self._flavor = ""
		self._dynamicreceivebuffering = ""
		self._ka = ""
		self._kaconnidletime = 0
		self._kamaxprobes = 0
		self._kaprobeinterval = 0
		self._sendbuffsize = 0
		self._mptcp = ""
		self._establishclientconn = ""
		self._tcpsegoffload = ""
		self._rstwindowattenuate = ""
		self._rstmaxack = ""
		self._spoofsyndrop = ""
		self._ecn = ""
		self._mptcpdropdataonpreestsf = ""
		self._mptcpfastopen = ""
		self._mptcpsessiontimeout = 0
		self._timestamp = ""
		self._dsack = ""
		self._ackaggregation = ""
		self._frto = ""
		self._refcnt = 0
		self.___count = 0

	@property
	def name(self) :
		ur"""Name for a TCP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), and equal \(=\) characters. The name of a TCP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my tcp profile" or 'my tcp profile'\).<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		ur"""Name for a TCP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), and equal \(=\) characters. The name of a TCP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my tcp profile" or 'my tcp profile'\).<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ws(self) :
		ur"""Enable or disable window scaling.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ws
		except Exception as e:
			raise e

	@ws.setter
	def ws(self, ws) :
		ur"""Enable or disable window scaling.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ws = ws
		except Exception as e:
			raise e

	@property
	def sack(self) :
		ur"""Enable or disable Selective ACKnowledgement (SACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sack
		except Exception as e:
			raise e

	@sack.setter
	def sack(self, sack) :
		ur"""Enable or disable Selective ACKnowledgement (SACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sack = sack
		except Exception as e:
			raise e

	@property
	def wsval(self) :
		ur"""Factor used to calculate the new window size.
		This argument is needed only when window scaling is enabled.<br/>Default value: 4<br/>Maximum length =  14.
		"""
		try :
			return self._wsval
		except Exception as e:
			raise e

	@wsval.setter
	def wsval(self, wsval) :
		ur"""Factor used to calculate the new window size.
		This argument is needed only when window scaling is enabled.<br/>Default value: 4<br/>Maximum length =  14
		"""
		try :
			self._wsval = wsval
		except Exception as e:
			raise e

	@property
	def nagle(self) :
		ur"""Enable or disable the Nagle algorithm on TCP connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nagle
		except Exception as e:
			raise e

	@nagle.setter
	def nagle(self, nagle) :
		ur"""Enable or disable the Nagle algorithm on TCP connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nagle = nagle
		except Exception as e:
			raise e

	@property
	def ackonpush(self) :
		ur"""Send immediate positive acknowledgement (ACK) on receipt of TCP packets when doing Web 2.0 PUSH.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ackonpush
		except Exception as e:
			raise e

	@ackonpush.setter
	def ackonpush(self, ackonpush) :
		ur"""Send immediate positive acknowledgement (ACK) on receipt of TCP packets when doing Web 2.0 PUSH.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ackonpush = ackonpush
		except Exception as e:
			raise e

	@property
	def mss(self) :
		ur"""Maximum number of octets to allow in a TCP data segment.<br/>Maximum length =  9176.
		"""
		try :
			return self._mss
		except Exception as e:
			raise e

	@mss.setter
	def mss(self, mss) :
		ur"""Maximum number of octets to allow in a TCP data segment.<br/>Maximum length =  9176
		"""
		try :
			self._mss = mss
		except Exception as e:
			raise e

	@property
	def maxburst(self) :
		ur"""Maximum number of TCP segments allowed in a burst.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._maxburst
		except Exception as e:
			raise e

	@maxburst.setter
	def maxburst(self, maxburst) :
		ur"""Maximum number of TCP segments allowed in a burst.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._maxburst = maxburst
		except Exception as e:
			raise e

	@property
	def initialcwnd(self) :
		ur"""Initial maximum upper limit on the number of TCP packets that can be outstanding on the TCP link to the server.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  44.
		"""
		try :
			return self._initialcwnd
		except Exception as e:
			raise e

	@initialcwnd.setter
	def initialcwnd(self, initialcwnd) :
		ur"""Initial maximum upper limit on the number of TCP packets that can be outstanding on the TCP link to the server.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  44
		"""
		try :
			self._initialcwnd = initialcwnd
		except Exception as e:
			raise e

	@property
	def delayedack(self) :
		ur"""Timeout for TCP delayed ACK, in milliseconds.<br/>Default value: 100<br/>Minimum length =  10<br/>Maximum length =  300.
		"""
		try :
			return self._delayedack
		except Exception as e:
			raise e

	@delayedack.setter
	def delayedack(self, delayedack) :
		ur"""Timeout for TCP delayed ACK, in milliseconds.<br/>Default value: 100<br/>Minimum length =  10<br/>Maximum length =  300
		"""
		try :
			self._delayedack = delayedack
		except Exception as e:
			raise e

	@property
	def oooqsize(self) :
		ur"""Maximum size of out-of-order packets queue. A value of 0 means no limit.<br/>Default value: 64<br/>Maximum length =  65535.
		"""
		try :
			return self._oooqsize
		except Exception as e:
			raise e

	@oooqsize.setter
	def oooqsize(self, oooqsize) :
		ur"""Maximum size of out-of-order packets queue. A value of 0 means no limit.<br/>Default value: 64<br/>Maximum length =  65535
		"""
		try :
			self._oooqsize = oooqsize
		except Exception as e:
			raise e

	@property
	def maxpktpermss(self) :
		ur"""Maximum number of TCP packets allowed per maximum segment size (MSS).<br/>Maximum length =  1460.
		"""
		try :
			return self._maxpktpermss
		except Exception as e:
			raise e

	@maxpktpermss.setter
	def maxpktpermss(self, maxpktpermss) :
		ur"""Maximum number of TCP packets allowed per maximum segment size (MSS).<br/>Maximum length =  1460
		"""
		try :
			self._maxpktpermss = maxpktpermss
		except Exception as e:
			raise e

	@property
	def pktperretx(self) :
		ur"""Maximum limit on the number of packets that should be retransmitted on receiving a partial ACK.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  512.
		"""
		try :
			return self._pktperretx
		except Exception as e:
			raise e

	@pktperretx.setter
	def pktperretx(self, pktperretx) :
		ur"""Maximum limit on the number of packets that should be retransmitted on receiving a partial ACK.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  512
		"""
		try :
			self._pktperretx = pktperretx
		except Exception as e:
			raise e

	@property
	def minrto(self) :
		ur"""Minimum retransmission timeout, in milliseconds.<br/>Default value: 1000<br/>Minimum length =  10<br/>Maximum length =  64000.
		"""
		try :
			return self._minrto
		except Exception as e:
			raise e

	@minrto.setter
	def minrto(self, minrto) :
		ur"""Minimum retransmission timeout, in milliseconds.<br/>Default value: 1000<br/>Minimum length =  10<br/>Maximum length =  64000
		"""
		try :
			self._minrto = minrto
		except Exception as e:
			raise e

	@property
	def slowstartincr(self) :
		ur"""Multiplier that determines the rate at which slow start increases the size of the TCP transmission window after each acknowledgement of successful transmission.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._slowstartincr
		except Exception as e:
			raise e

	@slowstartincr.setter
	def slowstartincr(self, slowstartincr) :
		ur"""Multiplier that determines the rate at which slow start increases the size of the TCP transmission window after each acknowledgement of successful transmission.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._slowstartincr = slowstartincr
		except Exception as e:
			raise e

	@property
	def buffersize(self) :
		ur"""TCP buffering size, in bytes.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  4194304.
		"""
		try :
			return self._buffersize
		except Exception as e:
			raise e

	@buffersize.setter
	def buffersize(self, buffersize) :
		ur"""TCP buffering size, in bytes.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  4194304
		"""
		try :
			self._buffersize = buffersize
		except Exception as e:
			raise e

	@property
	def syncookie(self) :
		ur"""Enable or disable the SYNCOOKIE mechanism for TCP handshake with clients. Disabling SYNCOOKIE prevents SYN attack protection on the NetScaler appliance.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._syncookie
		except Exception as e:
			raise e

	@syncookie.setter
	def syncookie(self, syncookie) :
		ur"""Enable or disable the SYNCOOKIE mechanism for TCP handshake with clients. Disabling SYNCOOKIE prevents SYN attack protection on the NetScaler appliance.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._syncookie = syncookie
		except Exception as e:
			raise e

	@property
	def kaprobeupdatelastactivity(self) :
		ur"""Update last activity for the connection after receiving keep-alive (KA) probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._kaprobeupdatelastactivity
		except Exception as e:
			raise e

	@kaprobeupdatelastactivity.setter
	def kaprobeupdatelastactivity(self, kaprobeupdatelastactivity) :
		ur"""Update last activity for the connection after receiving keep-alive (KA) probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._kaprobeupdatelastactivity = kaprobeupdatelastactivity
		except Exception as e:
			raise e

	@property
	def flavor(self) :
		ur"""Set TCP congestion control algorithm.<br/>Default value: Default<br/>Possible values = Default, Westwood, BIC, CUBIC.
		"""
		try :
			return self._flavor
		except Exception as e:
			raise e

	@flavor.setter
	def flavor(self, flavor) :
		ur"""Set TCP congestion control algorithm.<br/>Default value: Default<br/>Possible values = Default, Westwood, BIC, CUBIC
		"""
		try :
			self._flavor = flavor
		except Exception as e:
			raise e

	@property
	def dynamicreceivebuffering(self) :
		ur"""Enable or disable dynamic receive buffering. When enabled, allows the receive buffer to be adjusted dynamically based on memory and network conditions.
		Note: The buffer size argument must be set for dynamic adjustments to take place.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dynamicreceivebuffering
		except Exception as e:
			raise e

	@dynamicreceivebuffering.setter
	def dynamicreceivebuffering(self, dynamicreceivebuffering) :
		ur"""Enable or disable dynamic receive buffering. When enabled, allows the receive buffer to be adjusted dynamically based on memory and network conditions.
		Note: The buffer size argument must be set for dynamic adjustments to take place.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dynamicreceivebuffering = dynamicreceivebuffering
		except Exception as e:
			raise e

	@property
	def ka(self) :
		ur"""Send periodic TCP keep-alive (KA) probes to check if peer is still up.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ka
		except Exception as e:
			raise e

	@ka.setter
	def ka(self, ka) :
		ur"""Send periodic TCP keep-alive (KA) probes to check if peer is still up.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ka = ka
		except Exception as e:
			raise e

	@property
	def kaconnidletime(self) :
		ur"""Duration, in seconds, for the connection to be idle, before sending a keep-alive (KA) probe.<br/>Minimum length =  1<br/>Maximum length =  4095.
		"""
		try :
			return self._kaconnidletime
		except Exception as e:
			raise e

	@kaconnidletime.setter
	def kaconnidletime(self, kaconnidletime) :
		ur"""Duration, in seconds, for the connection to be idle, before sending a keep-alive (KA) probe.<br/>Minimum length =  1<br/>Maximum length =  4095
		"""
		try :
			self._kaconnidletime = kaconnidletime
		except Exception as e:
			raise e

	@property
	def kamaxprobes(self) :
		ur"""Number of keep-alive (KA) probes to be sent when not acknowledged, before assuming the peer to be down.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._kamaxprobes
		except Exception as e:
			raise e

	@kamaxprobes.setter
	def kamaxprobes(self, kamaxprobes) :
		ur"""Number of keep-alive (KA) probes to be sent when not acknowledged, before assuming the peer to be down.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._kamaxprobes = kamaxprobes
		except Exception as e:
			raise e

	@property
	def kaprobeinterval(self) :
		ur"""Time interval, in seconds, before the next keep-alive (KA) probe, if the peer does not respond.<br/>Minimum length =  1<br/>Maximum length =  4095.
		"""
		try :
			return self._kaprobeinterval
		except Exception as e:
			raise e

	@kaprobeinterval.setter
	def kaprobeinterval(self, kaprobeinterval) :
		ur"""Time interval, in seconds, before the next keep-alive (KA) probe, if the peer does not respond.<br/>Minimum length =  1<br/>Maximum length =  4095
		"""
		try :
			self._kaprobeinterval = kaprobeinterval
		except Exception as e:
			raise e

	@property
	def sendbuffsize(self) :
		ur"""TCP Send Buffer Size.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  4194304.
		"""
		try :
			return self._sendbuffsize
		except Exception as e:
			raise e

	@sendbuffsize.setter
	def sendbuffsize(self, sendbuffsize) :
		ur"""TCP Send Buffer Size.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  4194304
		"""
		try :
			self._sendbuffsize = sendbuffsize
		except Exception as e:
			raise e

	@property
	def mptcp(self) :
		ur"""Enable or disable Multipath TCP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mptcp
		except Exception as e:
			raise e

	@mptcp.setter
	def mptcp(self, mptcp) :
		ur"""Enable or disable Multipath TCP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mptcp = mptcp
		except Exception as e:
			raise e

	@property
	def establishclientconn(self) :
		ur"""Establishing Client Client connection on First data/ Final-ACK / Automatic.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, CONN_ESTABLISHED, ON_FIRST_DATA.
		"""
		try :
			return self._establishclientconn
		except Exception as e:
			raise e

	@establishclientconn.setter
	def establishclientconn(self, establishclientconn) :
		ur"""Establishing Client Client connection on First data/ Final-ACK / Automatic.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, CONN_ESTABLISHED, ON_FIRST_DATA
		"""
		try :
			self._establishclientconn = establishclientconn
		except Exception as e:
			raise e

	@property
	def tcpsegoffload(self) :
		ur"""Offload TCP segmentation to the NIC. If set to AUTOMATIC, TCP segmentation will be offloaded to the NIC, if the NIC supports it.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, DISABLED.
		"""
		try :
			return self._tcpsegoffload
		except Exception as e:
			raise e

	@tcpsegoffload.setter
	def tcpsegoffload(self, tcpsegoffload) :
		ur"""Offload TCP segmentation to the NIC. If set to AUTOMATIC, TCP segmentation will be offloaded to the NIC, if the NIC supports it.<br/>Default value: AUTOMATIC<br/>Possible values = AUTOMATIC, DISABLED
		"""
		try :
			self._tcpsegoffload = tcpsegoffload
		except Exception as e:
			raise e

	@property
	def rstwindowattenuate(self) :
		ur"""Enable or disable RST window attenuation to protect against spoofing. When enabled, will reply with corrective ACK when a sequence number is invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rstwindowattenuate
		except Exception as e:
			raise e

	@rstwindowattenuate.setter
	def rstwindowattenuate(self, rstwindowattenuate) :
		ur"""Enable or disable RST window attenuation to protect against spoofing. When enabled, will reply with corrective ACK when a sequence number is invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rstwindowattenuate = rstwindowattenuate
		except Exception as e:
			raise e

	@property
	def rstmaxack(self) :
		ur"""Enable or disable acceptance of RST that is out of window yet echoes highest ACK sequence number. Useful only in proxy mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rstmaxack
		except Exception as e:
			raise e

	@rstmaxack.setter
	def rstmaxack(self, rstmaxack) :
		ur"""Enable or disable acceptance of RST that is out of window yet echoes highest ACK sequence number. Useful only in proxy mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rstmaxack = rstmaxack
		except Exception as e:
			raise e

	@property
	def spoofsyndrop(self) :
		ur"""Enable or disable drop of invalid SYN packets to protect against spoofing. When disabled, established connections will be reset when a SYN packet is received.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._spoofsyndrop
		except Exception as e:
			raise e

	@spoofsyndrop.setter
	def spoofsyndrop(self, spoofsyndrop) :
		ur"""Enable or disable drop of invalid SYN packets to protect against spoofing. When disabled, established connections will be reset when a SYN packet is received.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._spoofsyndrop = spoofsyndrop
		except Exception as e:
			raise e

	@property
	def ecn(self) :
		ur"""Enable or disable TCP Explicit Congestion Notification.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ecn
		except Exception as e:
			raise e

	@ecn.setter
	def ecn(self, ecn) :
		ur"""Enable or disable TCP Explicit Congestion Notification.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ecn = ecn
		except Exception as e:
			raise e

	@property
	def mptcpdropdataonpreestsf(self) :
		ur"""Enable or disable silently dropping the data on Pre-Established subflow. When enabled, DSS data packets are dropped silently instead of dropping the connection when data is received on pre established subflow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mptcpdropdataonpreestsf
		except Exception as e:
			raise e

	@mptcpdropdataonpreestsf.setter
	def mptcpdropdataonpreestsf(self, mptcpdropdataonpreestsf) :
		ur"""Enable or disable silently dropping the data on Pre-Established subflow. When enabled, DSS data packets are dropped silently instead of dropping the connection when data is received on pre established subflow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mptcpdropdataonpreestsf = mptcpdropdataonpreestsf
		except Exception as e:
			raise e

	@property
	def mptcpfastopen(self) :
		ur"""Enable or disable Multipath TCP fastopen. When enabled, DSS data packets are accepted before receiving the third ack of SYN handshake.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mptcpfastopen
		except Exception as e:
			raise e

	@mptcpfastopen.setter
	def mptcpfastopen(self, mptcpfastopen) :
		ur"""Enable or disable Multipath TCP fastopen. When enabled, DSS data packets are accepted before receiving the third ack of SYN handshake.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mptcpfastopen = mptcpfastopen
		except Exception as e:
			raise e

	@property
	def mptcpsessiontimeout(self) :
		ur"""MPTCP session timeout in seconds. If this value is not set, idle MPTCP sessions are flushed after vserver's client idle timeout.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._mptcpsessiontimeout
		except Exception as e:
			raise e

	@mptcpsessiontimeout.setter
	def mptcpsessiontimeout(self, mptcpsessiontimeout) :
		ur"""MPTCP session timeout in seconds. If this value is not set, idle MPTCP sessions are flushed after vserver's client idle timeout.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._mptcpsessiontimeout = mptcpsessiontimeout
		except Exception as e:
			raise e

	@property
	def timestamp(self) :
		ur"""Enable or Disable TCP Timestamp option (RFC 1323).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._timestamp
		except Exception as e:
			raise e

	@timestamp.setter
	def timestamp(self, timestamp) :
		ur"""Enable or Disable TCP Timestamp option (RFC 1323).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._timestamp = timestamp
		except Exception as e:
			raise e

	@property
	def dsack(self) :
		ur"""Enable or disable DSACK.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dsack
		except Exception as e:
			raise e

	@dsack.setter
	def dsack(self, dsack) :
		ur"""Enable or disable DSACK.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dsack = dsack
		except Exception as e:
			raise e

	@property
	def ackaggregation(self) :
		ur"""Enable or disable ACK Aggregation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ackaggregation
		except Exception as e:
			raise e

	@ackaggregation.setter
	def ackaggregation(self, ackaggregation) :
		ur"""Enable or disable ACK Aggregation.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ackaggregation = ackaggregation
		except Exception as e:
			raise e

	@property
	def frto(self) :
		ur"""Enable or disable FRTO (Forward RTO-Recovery).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._frto
		except Exception as e:
			raise e

	@frto.setter
	def frto(self, frto) :
		ur"""Enable or disable FRTO (Forward RTO-Recovery).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._frto = frto
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		ur"""Number of entities using this profile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nstcpprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nstcpprofile
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
		ur""" Use this API to add nstcpprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = nstcpprofile()
				addresource.name = resource.name
				addresource.ws = resource.ws
				addresource.sack = resource.sack
				addresource.wsval = resource.wsval
				addresource.nagle = resource.nagle
				addresource.ackonpush = resource.ackonpush
				addresource.mss = resource.mss
				addresource.maxburst = resource.maxburst
				addresource.initialcwnd = resource.initialcwnd
				addresource.delayedack = resource.delayedack
				addresource.oooqsize = resource.oooqsize
				addresource.maxpktpermss = resource.maxpktpermss
				addresource.pktperretx = resource.pktperretx
				addresource.minrto = resource.minrto
				addresource.slowstartincr = resource.slowstartincr
				addresource.buffersize = resource.buffersize
				addresource.syncookie = resource.syncookie
				addresource.kaprobeupdatelastactivity = resource.kaprobeupdatelastactivity
				addresource.flavor = resource.flavor
				addresource.dynamicreceivebuffering = resource.dynamicreceivebuffering
				addresource.ka = resource.ka
				addresource.kaconnidletime = resource.kaconnidletime
				addresource.kamaxprobes = resource.kamaxprobes
				addresource.kaprobeinterval = resource.kaprobeinterval
				addresource.sendbuffsize = resource.sendbuffsize
				addresource.mptcp = resource.mptcp
				addresource.establishclientconn = resource.establishclientconn
				addresource.tcpsegoffload = resource.tcpsegoffload
				addresource.rstwindowattenuate = resource.rstwindowattenuate
				addresource.rstmaxack = resource.rstmaxack
				addresource.spoofsyndrop = resource.spoofsyndrop
				addresource.ecn = resource.ecn
				addresource.mptcpdropdataonpreestsf = resource.mptcpdropdataonpreestsf
				addresource.mptcpfastopen = resource.mptcpfastopen
				addresource.mptcpsessiontimeout = resource.mptcpsessiontimeout
				addresource.timestamp = resource.timestamp
				addresource.dsack = resource.dsack
				addresource.ackaggregation = resource.ackaggregation
				addresource.frto = resource.frto
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nstcpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].ws = resource[i].ws
						addresources[i].sack = resource[i].sack
						addresources[i].wsval = resource[i].wsval
						addresources[i].nagle = resource[i].nagle
						addresources[i].ackonpush = resource[i].ackonpush
						addresources[i].mss = resource[i].mss
						addresources[i].maxburst = resource[i].maxburst
						addresources[i].initialcwnd = resource[i].initialcwnd
						addresources[i].delayedack = resource[i].delayedack
						addresources[i].oooqsize = resource[i].oooqsize
						addresources[i].maxpktpermss = resource[i].maxpktpermss
						addresources[i].pktperretx = resource[i].pktperretx
						addresources[i].minrto = resource[i].minrto
						addresources[i].slowstartincr = resource[i].slowstartincr
						addresources[i].buffersize = resource[i].buffersize
						addresources[i].syncookie = resource[i].syncookie
						addresources[i].kaprobeupdatelastactivity = resource[i].kaprobeupdatelastactivity
						addresources[i].flavor = resource[i].flavor
						addresources[i].dynamicreceivebuffering = resource[i].dynamicreceivebuffering
						addresources[i].ka = resource[i].ka
						addresources[i].kaconnidletime = resource[i].kaconnidletime
						addresources[i].kamaxprobes = resource[i].kamaxprobes
						addresources[i].kaprobeinterval = resource[i].kaprobeinterval
						addresources[i].sendbuffsize = resource[i].sendbuffsize
						addresources[i].mptcp = resource[i].mptcp
						addresources[i].establishclientconn = resource[i].establishclientconn
						addresources[i].tcpsegoffload = resource[i].tcpsegoffload
						addresources[i].rstwindowattenuate = resource[i].rstwindowattenuate
						addresources[i].rstmaxack = resource[i].rstmaxack
						addresources[i].spoofsyndrop = resource[i].spoofsyndrop
						addresources[i].ecn = resource[i].ecn
						addresources[i].mptcpdropdataonpreestsf = resource[i].mptcpdropdataonpreestsf
						addresources[i].mptcpfastopen = resource[i].mptcpfastopen
						addresources[i].mptcpsessiontimeout = resource[i].mptcpsessiontimeout
						addresources[i].timestamp = resource[i].timestamp
						addresources[i].dsack = resource[i].dsack
						addresources[i].ackaggregation = resource[i].ackaggregation
						addresources[i].frto = resource[i].frto
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		ur""" Use this API to delete nstcpprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nstcpprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		ur""" Use this API to update nstcpprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = nstcpprofile()
				updateresource.name = resource.name
				updateresource.ws = resource.ws
				updateresource.sack = resource.sack
				updateresource.wsval = resource.wsval
				updateresource.nagle = resource.nagle
				updateresource.ackonpush = resource.ackonpush
				updateresource.mss = resource.mss
				updateresource.maxburst = resource.maxburst
				updateresource.initialcwnd = resource.initialcwnd
				updateresource.delayedack = resource.delayedack
				updateresource.oooqsize = resource.oooqsize
				updateresource.maxpktpermss = resource.maxpktpermss
				updateresource.pktperretx = resource.pktperretx
				updateresource.minrto = resource.minrto
				updateresource.slowstartincr = resource.slowstartincr
				updateresource.buffersize = resource.buffersize
				updateresource.syncookie = resource.syncookie
				updateresource.kaprobeupdatelastactivity = resource.kaprobeupdatelastactivity
				updateresource.flavor = resource.flavor
				updateresource.dynamicreceivebuffering = resource.dynamicreceivebuffering
				updateresource.ka = resource.ka
				updateresource.kaconnidletime = resource.kaconnidletime
				updateresource.kamaxprobes = resource.kamaxprobes
				updateresource.kaprobeinterval = resource.kaprobeinterval
				updateresource.sendbuffsize = resource.sendbuffsize
				updateresource.mptcp = resource.mptcp
				updateresource.establishclientconn = resource.establishclientconn
				updateresource.tcpsegoffload = resource.tcpsegoffload
				updateresource.rstwindowattenuate = resource.rstwindowattenuate
				updateresource.rstmaxack = resource.rstmaxack
				updateresource.spoofsyndrop = resource.spoofsyndrop
				updateresource.ecn = resource.ecn
				updateresource.mptcpdropdataonpreestsf = resource.mptcpdropdataonpreestsf
				updateresource.mptcpfastopen = resource.mptcpfastopen
				updateresource.mptcpsessiontimeout = resource.mptcpsessiontimeout
				updateresource.timestamp = resource.timestamp
				updateresource.dsack = resource.dsack
				updateresource.ackaggregation = resource.ackaggregation
				updateresource.frto = resource.frto
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nstcpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ws = resource[i].ws
						updateresources[i].sack = resource[i].sack
						updateresources[i].wsval = resource[i].wsval
						updateresources[i].nagle = resource[i].nagle
						updateresources[i].ackonpush = resource[i].ackonpush
						updateresources[i].mss = resource[i].mss
						updateresources[i].maxburst = resource[i].maxburst
						updateresources[i].initialcwnd = resource[i].initialcwnd
						updateresources[i].delayedack = resource[i].delayedack
						updateresources[i].oooqsize = resource[i].oooqsize
						updateresources[i].maxpktpermss = resource[i].maxpktpermss
						updateresources[i].pktperretx = resource[i].pktperretx
						updateresources[i].minrto = resource[i].minrto
						updateresources[i].slowstartincr = resource[i].slowstartincr
						updateresources[i].buffersize = resource[i].buffersize
						updateresources[i].syncookie = resource[i].syncookie
						updateresources[i].kaprobeupdatelastactivity = resource[i].kaprobeupdatelastactivity
						updateresources[i].flavor = resource[i].flavor
						updateresources[i].dynamicreceivebuffering = resource[i].dynamicreceivebuffering
						updateresources[i].ka = resource[i].ka
						updateresources[i].kaconnidletime = resource[i].kaconnidletime
						updateresources[i].kamaxprobes = resource[i].kamaxprobes
						updateresources[i].kaprobeinterval = resource[i].kaprobeinterval
						updateresources[i].sendbuffsize = resource[i].sendbuffsize
						updateresources[i].mptcp = resource[i].mptcp
						updateresources[i].establishclientconn = resource[i].establishclientconn
						updateresources[i].tcpsegoffload = resource[i].tcpsegoffload
						updateresources[i].rstwindowattenuate = resource[i].rstwindowattenuate
						updateresources[i].rstmaxack = resource[i].rstmaxack
						updateresources[i].spoofsyndrop = resource[i].spoofsyndrop
						updateresources[i].ecn = resource[i].ecn
						updateresources[i].mptcpdropdataonpreestsf = resource[i].mptcpdropdataonpreestsf
						updateresources[i].mptcpfastopen = resource[i].mptcpfastopen
						updateresources[i].mptcpsessiontimeout = resource[i].mptcpsessiontimeout
						updateresources[i].timestamp = resource[i].timestamp
						updateresources[i].dsack = resource[i].dsack
						updateresources[i].ackaggregation = resource[i].ackaggregation
						updateresources[i].frto = resource[i].frto
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		ur""" Use this API to unset the properties of nstcpprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nstcpprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nstcpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		ur""" Use this API to fetch all the nstcpprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nstcpprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = nstcpprofile()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [nstcpprofile() for _ in range(len(name))]
							obj = [nstcpprofile() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = nstcpprofile()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		ur""" Use this API to fetch filtered set of nstcpprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstcpprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		ur""" Use this API to count the nstcpprofile resources configured on NetScaler.
		"""
		try :
			obj = nstcpprofile()
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
		ur""" Use this API to count filtered the set of nstcpprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nstcpprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Kaprobeupdatelastactivity:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mptcpdropdataonpreestsf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ecn:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Spoofsyndrop:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dsack:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mptcp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Frto:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Establishclientconn:
		AUTOMATIC = "AUTOMATIC"
		CONN_ESTABLISHED = "CONN_ESTABLISHED"
		ON_FIRST_DATA = "ON_FIRST_DATA"

	class Flavor:
		Default = "Default"
		Westwood = "Westwood"
		BIC = "BIC"
		CUBIC = "CUBIC"

	class Mptcpfastopen:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dynamicreceivebuffering:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tcpsegoffload:
		AUTOMATIC = "AUTOMATIC"
		DISABLED = "DISABLED"

	class Sack:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ws:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Syncookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ackonpush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Timestamp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ka:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rstmaxack:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rstwindowattenuate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ackaggregation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nagle:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nstcpprofile_response(base_response) :
	def __init__(self, length=1) :
		self.nstcpprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nstcpprofile = [nstcpprofile() for _ in range(length)]

