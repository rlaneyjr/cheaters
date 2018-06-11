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

class protocoltcp_stats(base_resource) :
	ur""" Statistics for tcp protocol resource.
	"""
	def __init__(self) :
		self._clearstats = ""
		self._tcpactiveserverconn = 0
		self._tcpcurserverconnopening = 0
		self._tcpcurclientconnopening = 0
		self._tcpcurclientconnestablished = 0
		self._tcpcurserverconnestablished = 0
		self._tcptotrxpkts = 0
		self._tcprxpktsrate = 0
		self._tcptotrxbytes = 0
		self._tcprxbytesrate = 0
		self._tcptottxpkts = 0
		self._tcptxpktsrate = 0
		self._tcptottxbytes = 0
		self._tcptxbytesrate = 0
		self._tcpcurclientconn = 0
		self._tcpcurclientconnclosing = 0
		self._tcptotclientconnopened = 0
		self._tcpclientconnopenedrate = 0
		self._tcpcurserverconn = 0
		self._tcpcurserverconnclosing = 0
		self._tcptotserverconnopened = 0
		self._tcpserverconnopenedrate = 0
		self._tcpsurgequeuelen = 0
		self._tcpspareconn = 0
		self._tcptotzombiecltconnflushed = 0
		self._tcpzombiecltconnflushedrate = 0
		self._tcptotzombiehalfopencltconnflushed = 0
		self._tcpzombiehalfopencltconnflushedrate = 0
		self._tcptotzombieactivehalfclosecltconnflushed = 0
		self._tcpzombieactivehalfclosecltconnflushedrate = 0
		self._tcptotzombiepassivehalfclosecltconnflushed = 0
		self._tcpzombiepassivehalfclosecltconnflushedrate = 0
		self._tcptotzombiesvrconnflushed = 0
		self._tcpzombiesvrconnflushedrate = 0
		self._tcptotzombiehalfopensvrconnflushed = 0
		self._tcpzombiehalfopensvrconnflushedrate = 0
		self._tcptotzombieactivehalfclosesvrconnflushed = 0
		self._tcpzombieactivehalfclosesvrconnflushedrate = 0
		self._tcptotzombiepassivehalfclosesrvconnflushed = 0
		self._tcpzombiepassivehalfclosesrvconnflushedrate = 0
		self._pcbtotzombiecall = 0
		self._pcbzombiecallrate = 0
		self._tcptotsyn = 0
		self._tcpsynrate = 0
		self._tcptotsynprobe = 0
		self._tcpsynproberate = 0
		self._tcptotsvrfin = 0
		self._tcpsvrfinrate = 0
		self._tcptotcltfin = 0
		self._tcpcltfinrate = 0
		self._tcpwaittosyn = 0
		self._tcpwaittosynrate = 0
		self._tcpwaittodata = 0
		self._tcpwaittodatarate = 0
		self._tcptotsynheld = 0
		self._tcpsynheldrate = 0
		self._tcptotsynflush = 0
		self._tcpsynflushrate = 0
		self._tcptotfinwaitclosed = 0
		self._tcpfinwaitclosedrate = 0
		self._tcperrbadchecksum = 0
		self._tcperrbadchecksumrate = 0
		self._tcperrdataafterfin = 0
		self._tcperrdataafterfinrate = 0
		self._tcperrsyninsynrcvd = 0
		self._tcperrsyninsynrcvdrate = 0
		self._tcperrsyninest = 0
		self._tcperrsyninestrate = 0
		self._tcperrsynsentbadack = 0
		self._tcperrsynsentbadackrate = 0
		self._tcperrrst = 0
		self._tcperrrstrate = 0
		self._tcperrrstnonest = 0
		self._tcperrrstnonestrate = 0
		self._tcperrrstoutofwindow = 0
		self._tcperrrstoutofwindowrate = 0
		self._tcperrrstintimewait = 0
		self._tcperrrstintimewaitrate = 0
		self._tcperrsvroutoforder = 0
		self._tcperrsvroutoforderrate = 0
		self._tcperrcltoutoforder = 0
		self._tcperrcltoutoforderrate = 0
		self._tcperrclthole = 0
		self._tcperrcltholerate = 0
		self._tcperrsvrhole = 0
		self._tcperrsvrholerate = 0
		self._tcperrcookiepktseqreject = 0
		self._tcperrcookiepktseqrejectrate = 0
		self._tcperrcookiepktsigreject = 0
		self._tcperrcookiepktsigrejectrate = 0
		self._tcperrcookiepktseqdrop = 0
		self._tcperrcookiepktseqdroprate = 0
		self._tcperrcookiepktmssreject = 0
		self._tcperrcookiepktmssrejectrate = 0
		self._tcperranyportfail = 0
		self._tcperranyportfailrate = 0
		self._tcperripportfail = 0
		self._tcperripportfailrate = 0
		self._tcperrstraypkt = 0
		self._tcperrstraypktrate = 0
		self._tcperrsentrst = 0
		self._tcperrsentrstrate = 0
		self._tcperrbadstateconn = 0
		self._tcperrbadstateconnrate = 0
		self._tcperrrstthreshold = 0
		self._tcperrrstthresholdrate = 0
		self._tcperroutofwindowpkts = 0
		self._tcperroutofwindowpktsrate = 0
		self._tcperrsyndroppedcongestion = 0
		self._tcperrsyndroppedcongestionrate = 0
		self._tcperrcltretrasmit = 0
		self._tcperrcltretrasmitrate = 0
		self._tcperrfullretrasmit = 0
		self._tcperrfullretrasmitrate = 0
		self._tcperrsynretry = 0
		self._tcperrsynretryrate = 0
		self._tcperrsyngiveup = 0
		self._tcperrsyngiveuprate = 0
		self._tcperrretransmit = 0
		self._tcperrretransmitrate = 0
		self._tcperrfirstretransmissions = 0
		self._tcperrfirstretransmissionsrate = 0
		self._tcperrthirdretransmissions = 0
		self._tcperrthirdretransmissionsrate = 0
		self._tcperrfifthretransmissions = 0
		self._tcperrfifthretransmissionsrate = 0
		self._tcperrseventhretransmissions = 0
		self._tcperrseventhretransmissionsrate = 0
		self._tcperrfastretransmissions = 0
		self._tcperrfastretransmissionsrate = 0
		self._tcperrsvrretrasmit = 0
		self._tcperrsvrretrasmitrate = 0
		self._tcperrpartialretrasmit = 0
		self._tcperrpartialretrasmitrate = 0
		self._tcperrfinretry = 0
		self._tcperrfinretryrate = 0
		self._tcperrfingiveup = 0
		self._tcperrfingiveuprate = 0
		self._tcperrsecondretransmissions = 0
		self._tcperrsecondretransmissionsrate = 0
		self._tcperrforthretransmissions = 0
		self._tcperrforthretransmissionsrate = 0
		self._tcperrsixthretransmissions = 0
		self._tcperrsixthretransmissionsrate = 0
		self._tcperrretransmitgiveup = 0
		self._tcperrretransmitgiveuprate = 0
		self._tcperrcipalloc = 0
		self._tcperrcipallocrate = 0

	@property
	def clearstats(self) :
		ur"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		ur"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def tcperrfingiveuprate(self) :
		ur"""Rate (/s) counter for tcperrfingiveup.
		"""
		try :
			return self._tcperrfingiveuprate
		except Exception as e:
			raise e

	@property
	def tcperrretransmit(self) :
		ur"""TCP packets retransmitted. The NetScaler attempts to retransmit the packet up to seven times, after which it resets the other half of the TCP connection.
		"""
		try :
			return self._tcperrretransmit
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktmssreject(self) :
		ur"""SYN cookie packets rejected because the maximum segment size (MSS) specified in the packets is incorrect.
		"""
		try :
			return self._tcperrcookiepktmssreject
		except Exception as e:
			raise e

	@property
	def tcptotzombiehalfopencltconnflushed(self) :
		ur"""Half-opened client connections that are flushed because the three-way handshakes are not complete.
		"""
		try :
			return self._tcptotzombiehalfopencltconnflushed
		except Exception as e:
			raise e

	@property
	def tcperrsentrstrate(self) :
		ur"""Rate (/s) counter for tcperrsentrst.
		"""
		try :
			return self._tcperrsentrstrate
		except Exception as e:
			raise e

	@property
	def tcperrcltoutoforder(self) :
		ur"""Out of order TCP packets received from a client.
		"""
		try :
			return self._tcperrcltoutoforder
		except Exception as e:
			raise e

	@property
	def tcpsurgequeuelen(self) :
		ur"""Connections in the surge queue. When the NetScaler cannot open a connection to the server, for example when maximum connections have been reached, the NetScaler queues these requests.
		"""
		try :
			return self._tcpsurgequeuelen
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktseqrejectrate(self) :
		ur"""Rate (/s) counter for tcperrcookiepktseqreject.
		"""
		try :
			return self._tcperrcookiepktseqrejectrate
		except Exception as e:
			raise e

	@property
	def tcperrrstoutofwindowrate(self) :
		ur"""Rate (/s) counter for tcperrrstoutofwindow.
		"""
		try :
			return self._tcperrrstoutofwindowrate
		except Exception as e:
			raise e

	@property
	def tcptotrxpkts(self) :
		ur"""TCP packets received.
		"""
		try :
			return self._tcptotrxpkts
		except Exception as e:
			raise e

	@property
	def tcpcurclientconnopening(self) :
		ur"""Client connections in the Opening state, which indicates that the handshakes are not yet complete.
		"""
		try :
			return self._tcpcurclientconnopening
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktseqreject(self) :
		ur"""SYN cookie packets rejected because they contain an incorrect sequence number.
		"""
		try :
			return self._tcperrcookiepktseqreject
		except Exception as e:
			raise e

	@property
	def tcperrforthretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrforthretransmissions.
		"""
		try :
			return self._tcperrforthretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcperrrst(self) :
		ur"""Reset packets received from a client or a server.
		"""
		try :
			return self._tcperrrst
		except Exception as e:
			raise e

	@property
	def tcpsvrfinrate(self) :
		ur"""Rate (/s) counter for tcptotsvrfin.
		"""
		try :
			return self._tcpsvrfinrate
		except Exception as e:
			raise e

	@property
	def tcptxbytesrate(self) :
		ur"""Rate (/s) counter for tcptottxbytes.
		"""
		try :
			return self._tcptxbytesrate
		except Exception as e:
			raise e

	@property
	def tcptotsyn(self) :
		ur"""SYN packets received.
		"""
		try :
			return self._tcptotsyn
		except Exception as e:
			raise e

	@property
	def tcpserverconnopenedrate(self) :
		ur"""Rate (/s) counter for tcptotserverconnopened.
		"""
		try :
			return self._tcpserverconnopenedrate
		except Exception as e:
			raise e

	@property
	def tcperrsyninsynrcvdrate(self) :
		ur"""Rate (/s) counter for tcperrsyninsynrcvd.
		"""
		try :
			return self._tcperrsyninsynrcvdrate
		except Exception as e:
			raise e

	@property
	def tcperrpartialretrasmitrate(self) :
		ur"""Rate (/s) counter for tcperrpartialretrasmit.
		"""
		try :
			return self._tcperrpartialretrasmitrate
		except Exception as e:
			raise e

	@property
	def tcpzombieactivehalfclosecltconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombieactivehalfclosecltconnflushed.
		"""
		try :
			return self._tcpzombieactivehalfclosecltconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcperrfinretry(self) :
		ur"""FIN packets resent to a server or a client.
		"""
		try :
			return self._tcperrfinretry
		except Exception as e:
			raise e

	@property
	def tcperrsvroutoforderrate(self) :
		ur"""Rate (/s) counter for tcperrsvroutoforder.
		"""
		try :
			return self._tcperrsvroutoforderrate
		except Exception as e:
			raise e

	@property
	def pcbzombiecallrate(self) :
		ur"""Rate (/s) counter for pcbtotzombiecall.
		"""
		try :
			return self._pcbzombiecallrate
		except Exception as e:
			raise e

	@property
	def tcperrfirstretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrfirstretransmissions.
		"""
		try :
			return self._tcperrfirstretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcperrstraypkt(self) :
		ur"""Number of stray or misrouted packets.
		"""
		try :
			return self._tcperrstraypkt
		except Exception as e:
			raise e

	@property
	def tcperrsyninsynrcvd(self) :
		ur"""SYN packets received on a connection that is in the SYN_RCVD state. A connection goes into the SYN_RCVD state after receiving a SYN packet.
		"""
		try :
			return self._tcperrsyninsynrcvd
		except Exception as e:
			raise e

	@property
	def tcprxbytesrate(self) :
		ur"""Rate (/s) counter for tcptotrxbytes.
		"""
		try :
			return self._tcprxbytesrate
		except Exception as e:
			raise e

	@property
	def tcpcurserverconnestablished(self) :
		ur"""Current server connections in the Established state, which indicates that data transfer can occur between the NetScaler and the server.
		"""
		try :
			return self._tcpcurserverconnestablished
		except Exception as e:
			raise e

	@property
	def tcperroutofwindowpktsrate(self) :
		ur"""Rate (/s) counter for tcperroutofwindowpkts.
		"""
		try :
			return self._tcperroutofwindowpktsrate
		except Exception as e:
			raise e

	@property
	def tcperranyportfailrate(self) :
		ur"""Rate (/s) counter for tcperranyportfail.
		"""
		try :
			return self._tcperranyportfailrate
		except Exception as e:
			raise e

	@property
	def tcpsynproberate(self) :
		ur"""Rate (/s) counter for tcptotsynprobe.
		"""
		try :
			return self._tcpsynproberate
		except Exception as e:
			raise e

	@property
	def tcpzombiesvrconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombiesvrconnflushed.
		"""
		try :
			return self._tcpzombiesvrconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcpcurclientconn(self) :
		ur"""Client connections, including connections in the Opening, Established, and Closing state.
		"""
		try :
			return self._tcpcurclientconn
		except Exception as e:
			raise e

	@property
	def tcperrsyninestrate(self) :
		ur"""Rate (/s) counter for tcperrsyninest.
		"""
		try :
			return self._tcperrsyninestrate
		except Exception as e:
			raise e

	@property
	def tcpcurserverconn(self) :
		ur"""Server connections, including connections in the Opening, Established, and Closing state.
		"""
		try :
			return self._tcpcurserverconn
		except Exception as e:
			raise e

	@property
	def tcperripportfailrate(self) :
		ur"""Rate (/s) counter for tcperripportfail.
		"""
		try :
			return self._tcperripportfailrate
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktsigrejectrate(self) :
		ur"""Rate (/s) counter for tcperrcookiepktsigreject.
		"""
		try :
			return self._tcperrcookiepktsigrejectrate
		except Exception as e:
			raise e

	@property
	def tcperrforthretransmissions(self) :
		ur"""Packets retransmitted four times by the NetScaler.
		"""
		try :
			return self._tcperrforthretransmissions
		except Exception as e:
			raise e

	@property
	def tcpzombiehalfopensvrconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombiehalfopensvrconnflushed.
		"""
		try :
			return self._tcpzombiehalfopensvrconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcperrsixthretransmissions(self) :
		ur"""Packets retransmitted six times by the NetScaler.
		"""
		try :
			return self._tcperrsixthretransmissions
		except Exception as e:
			raise e

	@property
	def tcpfinwaitclosedrate(self) :
		ur"""Rate (/s) counter for tcptotfinwaitclosed.
		"""
		try :
			return self._tcpfinwaitclosedrate
		except Exception as e:
			raise e

	@property
	def tcperrbadchecksum(self) :
		ur"""Packets received with a TCP checksum error.
		"""
		try :
			return self._tcperrbadchecksum
		except Exception as e:
			raise e

	@property
	def tcpsynflushrate(self) :
		ur"""Rate (/s) counter for tcptotsynflush.
		"""
		try :
			return self._tcpsynflushrate
		except Exception as e:
			raise e

	@property
	def tcperrcipallocrate(self) :
		ur"""Rate (/s) counter for tcperrcipalloc.
		"""
		try :
			return self._tcperrcipallocrate
		except Exception as e:
			raise e

	@property
	def tcperrrstthreshold(self) :
		ur"""Reset packets dropped because the default threshold of 100 resets per 10 milliseconds has been exceeded. This is a configurable value using the set rateControl command.
		"""
		try :
			return self._tcperrrstthreshold
		except Exception as e:
			raise e

	@property
	def tcptotzombieactivehalfclosecltconnflushed(self) :
		ur"""Active half-closed client connections that are flushed because the client has closed the connection and there has been no activity on the connection.
		"""
		try :
			return self._tcptotzombieactivehalfclosecltconnflushed
		except Exception as e:
			raise e

	@property
	def tcperrsynsentbadackrate(self) :
		ur"""Rate (/s) counter for tcperrsynsentbadack.
		"""
		try :
			return self._tcperrsynsentbadackrate
		except Exception as e:
			raise e

	@property
	def tcpwaittodatarate(self) :
		ur"""Rate (/s) counter for tcpwaittodata.
		"""
		try :
			return self._tcpwaittodatarate
		except Exception as e:
			raise e

	@property
	def tcperrseventhretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrseventhretransmissions.
		"""
		try :
			return self._tcperrseventhretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcperrretransmitrate(self) :
		ur"""Rate (/s) counter for tcperrretransmit.
		"""
		try :
			return self._tcperrretransmitrate
		except Exception as e:
			raise e

	@property
	def tcperrfullretrasmitrate(self) :
		ur"""Rate (/s) counter for tcperrfullretrasmit.
		"""
		try :
			return self._tcperrfullretrasmitrate
		except Exception as e:
			raise e

	@property
	def tcptotsynflush(self) :
		ur"""SYN packets flushed on the NetScaler because of no response from the server for three or more seconds.
		"""
		try :
			return self._tcptotsynflush
		except Exception as e:
			raise e

	@property
	def tcperrsixthretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrsixthretransmissions.
		"""
		try :
			return self._tcperrsixthretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcperrfastretransmissions(self) :
		ur"""TCP packets on which the NetScaler performs a fast retransmission in response to three duplicate acknowledgements or a partial acknowledgement.  The NetScaler assumes that the packet is lost and retransmits the packet before its time-out.
		"""
		try :
			return self._tcperrfastretransmissions
		except Exception as e:
			raise e

	@property
	def tcperrsecondretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrsecondretransmissions.
		"""
		try :
			return self._tcperrsecondretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcpzombiepassivehalfclosecltconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombiepassivehalfclosecltconnflushed.
		"""
		try :
			return self._tcpzombiepassivehalfclosecltconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcpcltfinrate(self) :
		ur"""Rate (/s) counter for tcptotcltfin.
		"""
		try :
			return self._tcpcltfinrate
		except Exception as e:
			raise e

	@property
	def tcpsynheldrate(self) :
		ur"""Rate (/s) counter for tcptotsynheld.
		"""
		try :
			return self._tcpsynheldrate
		except Exception as e:
			raise e

	@property
	def tcperrrstnonestrate(self) :
		ur"""Rate (/s) counter for tcperrrstnonest.
		"""
		try :
			return self._tcperrrstnonestrate
		except Exception as e:
			raise e

	@property
	def tcperrcltretrasmit(self) :
		ur"""Packets retransmitted by a client. This usually occurs because the acknowledgement from the NetScaler has not reached the client.
		"""
		try :
			return self._tcperrcltretrasmit
		except Exception as e:
			raise e

	@property
	def tcptotsynprobe(self) :
		ur"""Probes from the NetScaler to a server. The NetScaler sends a SYN packet to the server to check its availability and expects a SYN_ACK packet from the server before a specified response timeout.
		"""
		try :
			return self._tcptotsynprobe
		except Exception as e:
			raise e

	@property
	def tcptotfinwaitclosed(self) :
		ur"""Connections closed on the NetScaler because the number of connections in the TIME_WAIT state has exceeded the default value of 7000.
		"""
		try :
			return self._tcptotfinwaitclosed
		except Exception as e:
			raise e

	@property
	def tcpzombiepassivehalfclosesrvconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombiepassivehalfclosesrvconnflushed.
		"""
		try :
			return self._tcpzombiepassivehalfclosesrvconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcperrsynsentbadack(self) :
		ur"""Incorrect ACK packets received on a connection that is in the SYN_SENT state. An incorrect ACK packet is the third packet in the three-way handshake that has an incorrect sequence number.
		"""
		try :
			return self._tcperrsynsentbadack
		except Exception as e:
			raise e

	@property
	def tcptotsynheld(self) :
		ur"""SYN packets held on the NetScaler that are waiting for a server connection.
		"""
		try :
			return self._tcptotsynheld
		except Exception as e:
			raise e

	@property
	def tcperrrstintimewaitrate(self) :
		ur"""Rate (/s) counter for tcperrrstintimewait.
		"""
		try :
			return self._tcperrrstintimewaitrate
		except Exception as e:
			raise e

	@property
	def tcperrrstintimewait(self) :
		ur"""Reset packets received on a connection that is in the TIME_WAIT state. Packets cannot be transferred on a connection in the TIME_WAIT state.
		"""
		try :
			return self._tcperrrstintimewait
		except Exception as e:
			raise e

	@property
	def tcperrthirdretransmissions(self) :
		ur"""Packets retransmitted three times by the NetScaler.
		"""
		try :
			return self._tcperrthirdretransmissions
		except Exception as e:
			raise e

	@property
	def tcptotrxbytes(self) :
		ur"""Bytes of TCP data received.
		"""
		try :
			return self._tcptotrxbytes
		except Exception as e:
			raise e

	@property
	def tcperrsvrretrasmit(self) :
		ur"""Packets retransmitted by a server. This usually occurs because the acknowledgement from the NetScaler has not reached the server.
		"""
		try :
			return self._tcperrsvrretrasmit
		except Exception as e:
			raise e

	@property
	def tcperrfastretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrfastretransmissions.
		"""
		try :
			return self._tcperrfastretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcptotzombiepassivehalfclosecltconnflushed(self) :
		ur"""Passive half-closed client connections that are flushed because the NetScaler has closed the connection and there has been no activity on the connection.
		"""
		try :
			return self._tcptotzombiepassivehalfclosecltconnflushed
		except Exception as e:
			raise e

	@property
	def tcperrcltholerate(self) :
		ur"""Rate (/s) counter for tcperrclthole.
		"""
		try :
			return self._tcperrcltholerate
		except Exception as e:
			raise e

	@property
	def tcperrsvroutoforder(self) :
		ur"""Out of order TCP packets received from a server. .
		"""
		try :
			return self._tcperrsvroutoforder
		except Exception as e:
			raise e

	@property
	def tcprxpktsrate(self) :
		ur"""Rate (/s) counter for tcptotrxpkts.
		"""
		try :
			return self._tcprxpktsrate
		except Exception as e:
			raise e

	@property
	def tcptotclientconnopened(self) :
		ur"""Client connections opened by the NetScaler since startup (after three-way handshake). This counter is reset when the NetScaler is restarted.
		"""
		try :
			return self._tcptotclientconnopened
		except Exception as e:
			raise e

	@property
	def tcperrstraypktrate(self) :
		ur"""Rate (/s) counter for tcperrstraypkt.
		"""
		try :
			return self._tcperrstraypktrate
		except Exception as e:
			raise e

	@property
	def tcperrfinretryrate(self) :
		ur"""Rate (/s) counter for tcperrfinretry.
		"""
		try :
			return self._tcperrfinretryrate
		except Exception as e:
			raise e

	@property
	def tcptotserverconnopened(self) :
		ur"""Server connections initiated by the NetScaler since startup. This counter is reset when the NetScaler is restarted.
		"""
		try :
			return self._tcptotserverconnopened
		except Exception as e:
			raise e

	@property
	def tcperrretransmitgiveup(self) :
		ur"""Number of times NetScaler terminates a connection after retransmitting the packet seven times on that connection.Retrasnmission happens when recieving end doesn't acknowledges the packet.
		"""
		try :
			return self._tcperrretransmitgiveup
		except Exception as e:
			raise e

	@property
	def tcperrthirdretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrthirdretransmissions.
		"""
		try :
			return self._tcperrthirdretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcpwaittosyn(self) :
		ur"""SYN packets (packets used to initiate a TCP connection) received on connections that are in the TIME_WAIT state. Packets cannot be transferred on a connection in this state.
		"""
		try :
			return self._tcpwaittosyn
		except Exception as e:
			raise e

	@property
	def tcperrsyndroppedcongestion(self) :
		ur"""SYN packets dropped because of network congestion.
		"""
		try :
			return self._tcperrsyndroppedcongestion
		except Exception as e:
			raise e

	@property
	def tcperrfingiveup(self) :
		ur"""Connections that were timed out by the NetScaler because of not receiving the ACK packet after retransmitting the FIN packet four times.
		"""
		try :
			return self._tcperrfingiveup
		except Exception as e:
			raise e

	@property
	def tcptotsvrfin(self) :
		ur"""FIN packets received from the server.
		"""
		try :
			return self._tcptotsvrfin
		except Exception as e:
			raise e

	@property
	def tcperrcltretrasmitrate(self) :
		ur"""Rate (/s) counter for tcperrcltretrasmit.
		"""
		try :
			return self._tcperrcltretrasmitrate
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktmssrejectrate(self) :
		ur"""Rate (/s) counter for tcperrcookiepktmssreject.
		"""
		try :
			return self._tcperrcookiepktmssrejectrate
		except Exception as e:
			raise e

	@property
	def tcperrsvrretrasmitrate(self) :
		ur"""Rate (/s) counter for tcperrsvrretrasmit.
		"""
		try :
			return self._tcperrsvrretrasmitrate
		except Exception as e:
			raise e

	@property
	def tcpcurserverconnclosing(self) :
		ur"""Server connections in the Closing state, which indicates that the connection termination process has initiated but is not complete.
		"""
		try :
			return self._tcpcurserverconnclosing
		except Exception as e:
			raise e

	@property
	def tcperrrstrate(self) :
		ur"""Rate (/s) counter for tcperrrst.
		"""
		try :
			return self._tcperrrstrate
		except Exception as e:
			raise e

	@property
	def tcperrfifthretransmissionsrate(self) :
		ur"""Rate (/s) counter for tcperrfifthretransmissions.
		"""
		try :
			return self._tcperrfifthretransmissionsrate
		except Exception as e:
			raise e

	@property
	def tcperrdataafterfin(self) :
		ur"""Packets received following a connection termination request. This error is usually caused by a reordering of packets during transmission.
		"""
		try :
			return self._tcperrdataafterfin
		except Exception as e:
			raise e

	@property
	def tcperrsvrhole(self) :
		ur"""TCP holes created on a server connection. When out of order packets are received from a server, a hole is created on the NetScaler for each group of missing packets.
		"""
		try :
			return self._tcperrsvrhole
		except Exception as e:
			raise e

	@property
	def tcperrsyngiveup(self) :
		ur"""Attempts to establish a connection on the NetScaler that timed out.
		"""
		try :
			return self._tcperrsyngiveup
		except Exception as e:
			raise e

	@property
	def tcperrfirstretransmissions(self) :
		ur"""Packets retransmitted once by the NetScaler.
		"""
		try :
			return self._tcperrfirstretransmissions
		except Exception as e:
			raise e

	@property
	def tcptotzombiesvrconnflushed(self) :
		ur"""Server connections that are flushed because there have been no client requests in the queue for some time.
		"""
		try :
			return self._tcptotzombiesvrconnflushed
		except Exception as e:
			raise e

	@property
	def tcperrsynretryrate(self) :
		ur"""Rate (/s) counter for tcperrsynretry.
		"""
		try :
			return self._tcperrsynretryrate
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktsigreject(self) :
		ur"""SYN cookie packets rejected because they contain an incorrect signature.
		"""
		try :
			return self._tcperrcookiepktsigreject
		except Exception as e:
			raise e

	@property
	def tcperroutofwindowpkts(self) :
		ur"""Packets received that are out of the current advertised window.
		"""
		try :
			return self._tcperroutofwindowpkts
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktseqdrop(self) :
		ur"""SYN cookie packets dropped because the sequence number specified in the packets is outside the current window.
		"""
		try :
			return self._tcperrcookiepktseqdrop
		except Exception as e:
			raise e

	@property
	def tcperrbadstateconnrate(self) :
		ur"""Rate (/s) counter for tcperrbadstateconn.
		"""
		try :
			return self._tcperrbadstateconnrate
		except Exception as e:
			raise e

	@property
	def tcperrsyndroppedcongestionrate(self) :
		ur"""Rate (/s) counter for tcperrsyndroppedcongestion.
		"""
		try :
			return self._tcperrsyndroppedcongestionrate
		except Exception as e:
			raise e

	@property
	def tcperrsvrholerate(self) :
		ur"""Rate (/s) counter for tcperrsvrhole.
		"""
		try :
			return self._tcperrsvrholerate
		except Exception as e:
			raise e

	@property
	def tcperrdataafterfinrate(self) :
		ur"""Rate (/s) counter for tcperrdataafterfin.
		"""
		try :
			return self._tcperrdataafterfinrate
		except Exception as e:
			raise e

	@property
	def tcperrcltoutoforderrate(self) :
		ur"""Rate (/s) counter for tcperrcltoutoforder.
		"""
		try :
			return self._tcperrcltoutoforderrate
		except Exception as e:
			raise e

	@property
	def tcptotzombiepassivehalfclosesrvconnflushed(self) :
		ur"""Passive half-closed server connections that are flushed because the NetScaler has closed the connection and there has been no activity on the connection.
		"""
		try :
			return self._tcptotzombiepassivehalfclosesrvconnflushed
		except Exception as e:
			raise e

	@property
	def tcperrsyninest(self) :
		ur"""SYN packets received on a connection that is in the ESTABLISHED state. A SYN packet is not expected on an ESTABLISHED connection.
		"""
		try :
			return self._tcperrsyninest
		except Exception as e:
			raise e

	@property
	def tcperrsecondretransmissions(self) :
		ur"""Packets retransmitted twice by the NetScaler.
		"""
		try :
			return self._tcperrsecondretransmissions
		except Exception as e:
			raise e

	@property
	def tcperrbadstateconn(self) :
		ur"""Connections that are not in a valid TCP state.
		"""
		try :
			return self._tcperrbadstateconn
		except Exception as e:
			raise e

	@property
	def tcpspareconn(self) :
		ur"""Spare connections available. To save time and resources in establishing another connection for a new client, the connection on the server is not closed after completing the request from the first client and is available for serving future requests.
		"""
		try :
			return self._tcpspareconn
		except Exception as e:
			raise e

	@property
	def tcperrretransmitgiveuprate(self) :
		ur"""Rate (/s) counter for tcperrretransmitgiveup.
		"""
		try :
			return self._tcperrretransmitgiveuprate
		except Exception as e:
			raise e

	@property
	def tcptottxpkts(self) :
		ur"""TCP packets transmitted.
		"""
		try :
			return self._tcptottxpkts
		except Exception as e:
			raise e

	@property
	def tcptotcltfin(self) :
		ur"""FIN packets received from the clients.
		"""
		try :
			return self._tcptotcltfin
		except Exception as e:
			raise e

	@property
	def tcpsynrate(self) :
		ur"""Rate (/s) counter for tcptotsyn.
		"""
		try :
			return self._tcpsynrate
		except Exception as e:
			raise e

	@property
	def tcpclientconnopenedrate(self) :
		ur"""Rate (/s) counter for tcptotclientconnopened.
		"""
		try :
			return self._tcpclientconnopenedrate
		except Exception as e:
			raise e

	@property
	def tcperranyportfail(self) :
		ur"""Port allocations that have failed on a mapped IP address because the maximum limit of 65536 has been exceeded.
		"""
		try :
			return self._tcperranyportfail
		except Exception as e:
			raise e

	@property
	def tcpwaittosynrate(self) :
		ur"""Rate (/s) counter for tcpwaittosyn.
		"""
		try :
			return self._tcpwaittosynrate
		except Exception as e:
			raise e

	@property
	def tcperrrstnonest(self) :
		ur"""Reset packets received on a connection that is not in the ESTABLISHED state.
		"""
		try :
			return self._tcperrrstnonest
		except Exception as e:
			raise e

	@property
	def tcperripportfail(self) :
		ur"""Port allocations that have failed on a subnet IP address or vserver IP address because the maximum limit of 65536 has been exceeded.
		"""
		try :
			return self._tcperripportfail
		except Exception as e:
			raise e

	@property
	def tcperrpartialretrasmit(self) :
		ur"""Partial packet retransmits by a client or server due to congestion on the connection. This usually occurs because the window advertised by the NetScaler is not big enough to hold the full packet.
		"""
		try :
			return self._tcperrpartialretrasmit
		except Exception as e:
			raise e

	@property
	def tcpzombieactivehalfclosesvrconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombieactivehalfclosesvrconnflushed.
		"""
		try :
			return self._tcpzombieactivehalfclosesvrconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcperrclthole(self) :
		ur"""TCP holes created on a client connection. When out of order packets are received from a client, a hole is created on the NetScaler for each group of missing packets.
		"""
		try :
			return self._tcperrclthole
		except Exception as e:
			raise e

	@property
	def tcpcurclientconnestablished(self) :
		ur"""Current client connections in the Established state, which indicates that data transfer can occur between the NetScaler and the client.
		"""
		try :
			return self._tcpcurclientconnestablished
		except Exception as e:
			raise e

	@property
	def tcpwaittodata(self) :
		ur"""Bytes of data received on connections that are in the TIME_WAIT state. Data cannot be transferred on a connection that is in this state.
		"""
		try :
			return self._tcpwaittodata
		except Exception as e:
			raise e

	@property
	def tcperrsentrst(self) :
		ur"""Reset packets sent to a client or a server.
		"""
		try :
			return self._tcperrsentrst
		except Exception as e:
			raise e

	@property
	def tcperrsyngiveuprate(self) :
		ur"""Rate (/s) counter for tcperrsyngiveup.
		"""
		try :
			return self._tcperrsyngiveuprate
		except Exception as e:
			raise e

	@property
	def tcperrbadchecksumrate(self) :
		ur"""Rate (/s) counter for tcperrbadchecksum.
		"""
		try :
			return self._tcperrbadchecksumrate
		except Exception as e:
			raise e

	@property
	def tcperrcookiepktseqdroprate(self) :
		ur"""Rate (/s) counter for tcperrcookiepktseqdrop.
		"""
		try :
			return self._tcperrcookiepktseqdroprate
		except Exception as e:
			raise e

	@property
	def tcperrseventhretransmissions(self) :
		ur"""Packets retransmitted seven times by the NetScaler. If this fails, the NetScaler terminates the connection.
		"""
		try :
			return self._tcperrseventhretransmissions
		except Exception as e:
			raise e

	@property
	def tcperrrstoutofwindow(self) :
		ur"""Reset packets received on a connection that is out of the current TCP window.
		"""
		try :
			return self._tcperrrstoutofwindow
		except Exception as e:
			raise e

	@property
	def tcpcurserverconnopening(self) :
		ur"""Server connections in the Opening state, which indicates that the handshakes are not yet complete.
		"""
		try :
			return self._tcpcurserverconnopening
		except Exception as e:
			raise e

	@property
	def tcptotzombieactivehalfclosesvrconnflushed(self) :
		ur"""Active half-closed server connections that are flushed because the server has closed the connection and there has been no activity on the connection.
		"""
		try :
			return self._tcptotzombieactivehalfclosesvrconnflushed
		except Exception as e:
			raise e

	@property
	def tcperrfullretrasmit(self) :
		ur"""Full packets retransmitted by the client or the server.
		"""
		try :
			return self._tcperrfullretrasmit
		except Exception as e:
			raise e

	@property
	def tcperrcipalloc(self) :
		ur"""Number of times TCP level client header insertion failure.
		"""
		try :
			return self._tcperrcipalloc
		except Exception as e:
			raise e

	@property
	def tcptotzombiecltconnflushed(self) :
		ur"""Client connections that are flushed because the client has been idle for some time.
		"""
		try :
			return self._tcptotzombiecltconnflushed
		except Exception as e:
			raise e

	@property
	def tcptotzombiehalfopensvrconnflushed(self) :
		ur"""Half-opened server connections that are flushed because the three-way handshakes are not complete.
		"""
		try :
			return self._tcptotzombiehalfopensvrconnflushed
		except Exception as e:
			raise e

	@property
	def pcbtotzombiecall(self) :
		ur"""Times the Zombie cleanup function is called. Every time a connection is flushed, it is marked for cleanup. The Zombie cleanup function clears all these connections at predefined intervals.
		"""
		try :
			return self._pcbtotzombiecall
		except Exception as e:
			raise e

	@property
	def tcpactiveserverconn(self) :
		ur"""Connections to a server currently responding to requests.
		"""
		try :
			return self._tcpactiveserverconn
		except Exception as e:
			raise e

	@property
	def tcperrsynretry(self) :
		ur"""SYN packets resent to a server.
		"""
		try :
			return self._tcperrsynretry
		except Exception as e:
			raise e

	@property
	def tcptottxbytes(self) :
		ur"""Bytes of TCP data transmitted.
		"""
		try :
			return self._tcptottxbytes
		except Exception as e:
			raise e

	@property
	def tcpcurclientconnclosing(self) :
		ur"""Client connections in the Closing state, which indicates that the connection termination process has initiated but is not complete.
		"""
		try :
			return self._tcpcurclientconnclosing
		except Exception as e:
			raise e

	@property
	def tcperrrstthresholdrate(self) :
		ur"""Rate (/s) counter for tcperrrstthreshold.
		"""
		try :
			return self._tcperrrstthresholdrate
		except Exception as e:
			raise e

	@property
	def tcperrfifthretransmissions(self) :
		ur"""Packets retransmitted five times by the NetScaler.
		"""
		try :
			return self._tcperrfifthretransmissions
		except Exception as e:
			raise e

	@property
	def tcpzombiehalfopencltconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombiehalfopencltconnflushed.
		"""
		try :
			return self._tcpzombiehalfopencltconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcpzombiecltconnflushedrate(self) :
		ur"""Rate (/s) counter for tcptotzombiecltconnflushed.
		"""
		try :
			return self._tcpzombiecltconnflushedrate
		except Exception as e:
			raise e

	@property
	def tcptxpktsrate(self) :
		ur"""Rate (/s) counter for tcptottxpkts.
		"""
		try :
			return self._tcptxpktsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		ur""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocoltcp_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocoltcp
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
	def  get(cls, service, name="", option_="") :
		ur""" Use this API to fetch the statistics of all protocoltcp_stats resources that are configured on netscaler.
		"""
		try :
			obj = protocoltcp_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocoltcp_response(base_response) :
	def __init__(self, length=1) :
		self.protocoltcp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocoltcp = [protocoltcp_stats() for _ in range(length)]

