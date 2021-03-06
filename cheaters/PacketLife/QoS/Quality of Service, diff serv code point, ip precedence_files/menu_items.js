/*
  --- menu items --- 
  note that this structure has changed its format since previous version.
  additional third parameter is added for item scope settings.
  Now this structure is compatible with Tigra Menu GOLD.
  Format description can be found in product documentation.
*/
var MENU_ITEMS = [
	['Physical Layer', null, null,
		['Structured Cabling', 'scs.htm'],
		['Intelligent Bldg Cabling', 'cab_ibs.htm'],
		['Cabling Terminology', 'cabstand.htm'],
		['Optical Budgets', 'optical.htm'],
		['Power Separation', 'pwrsep.htm'],
		['Data Encoding', 'encoding.htm'],
		['Transmission', 'transm.htm'],
		['Voice & Telephony', 'voice.htm'],
		['Modem Setup', 'modem.htm'],
		['Console Pinouts', 'pinouts.htm'],
	],
	['Data Link Layer', null, null,
		['Ethernet', null, null,
			['Ethernet', 'ethernet.htm'],
			['Intro to Ethernet', 'eth_intr.htm'],
			['Ethernet Terminology', 'eth_err.htm'],
			['Ethernet Bridging', 'eth_brid.htm'],
			['Ethernet Switching', 'eth_swit.htm'],
			['VLANs', 'eth_vlan.htm'],
			['Power over Ethernet', 'eth_poe.htm'],
		],
		['Wireless', null, null,
			['Wi-Fi', 'wireless.htm'],
			['LWAPP', 'lwapp.htm'],
			['Wi-Fi Security', 'wifisec.htm'],
			['Wi-Fi Survey', 'survey.htm'],
		],
		['Token Ring', 'tokenr.htm'],
		['FDDI', 'fddi.htm'],
		['Serial Comms', 'serial.htm'],
		['Building Controls', 'controls.htm'],
		['X.25', 'x25.htm'],
		['DSL', 'dsl.htm'],
		['ISDN', 'isdn.htm'],
		['PPP', 'ppp.htm'],
		['Frame Relay', 'frame.htm'],
		['ATM', 'atm.htm'],
		['SDH', 'sdh.htm'],
		['LLC, HDLC, SDLC', 'hdlc.htm'],
		['SMDS', 'smds.htm'],
		['SS7', 'ss7.htm'],
		['CDP', 'cdp.htm'],

	],
	['Network Layer', null, null,
		['IPv4', null, null,
			['IP Introduction', 'ipintro.htm'],
			['IP Datagram', 'ipdgram.htm'],
			['IP Addressing', 'ipadd.htm'],
			['CIDR', 'cidr.htm'],
			['TCP', 'tcp.htm'],
			['UDP', 'udp.htm'],
			['ARP/RARP', 'arp.htm'],
			['ICMP', 'icmp.htm'],
			['Bootp and DHCP', 'dhcp.htm'],
			['DNS', 'dns.htm'],
			['WINS', 'wins.htm'],
			['Multicast', 'multicas.htm'],
			['RIP', 'iprip.htm'],
			['IGRP', 'igrp.htm'],
			['EIGRP', 'eigrp.htm'],
			['OSPF', 'ospf.htm'],
			['BGP', 'bgp.htm'],
			['ISIS', 'isis.htm'],
			['DLSw', 'dlsw.htm'],
			['Telnet', 'telnet.htm'],
			['FTP', 'ftp.htm'],
			['Finger', 'finger.htm'],
			['RWhois', 'rwhois.htm'],
			['IP Small Services', 'ip_small.htm'],
			['HTTP', 'http.htm'],
			['NAT', 'nat.htm'],
			['VPN', 'vpn.htm'],
			['SSL', 'ssl.htm'],
		],
		['IPv6', 'ipv6.htm'],
		['IPX', 'ipx.htm'],
		['NetBIOS', 'netbios.htm'],
		['DECnet', 'decnet.htm'],
		['AppleTalk', 'apple.htm'],
		['Banyan Vines', 'banyan.htm'],
		['SNA', 'sna.htm'],
	],
	['Upper Layers', null, null,
		['Security', null, null,
			['Encryption', 'encrypt.htm'],
			['IPsec', 'ipsec.htm'],
			['802.1X', '8021x.htm'],
			['SecureID', 'secureid.htm'],
			['SSH', 'ssh.htm'],
		],
		['Unix Overview', 'unix.htm'],
		['RPC', 'rpc.htm'],
		['NFS', 'nfs.htm'],
		['NIS', 'nis.htm'],
		['Content Networking', 'content.htm'],
		['Quality of Service', 'qos.htm'],
	],
	['Miscellaneous', null, null,
		['OSI', 'osi.htm'],
		['HTML', 'writeweb.htm'],
		['Windows NT 4', null, null,
			['Contents', 'nt4.htm'],
			['Introduction', 'nt_int.htm'],
			['Architecture', 'nt_arch.htm'],
			['Installation', 'nt_inst.htm'],
			['Environment', 'nt_env.htm'],
			['System Policies', 'nt_pol.htm'],
			['File Systems', 'nt_file.htm'],
			['Partitions', 'nt_part.htm'],
			['Applications', 'nt_app.htm'],
			['Protocols', 'nt_prot.htm'],
			['RAS', 'nt_ras.htm'],
			['IIS and PWS', 'nt_iis.htm'],
			['Novell Netware', 'nt_nov.htm'],
			['Logging on', 'nt_log.htm'],
			['User Accounts', 'nt_user.htm'],
			['Group Accounts', 'nt_grp.htm'],
			['Administration', 'nt_admin.htm'],
			['Shared Folders', 'nt_flder.htm'],
			['NTFS Permissions', 'nt_ntfs.htm'],
			['Printers', 'nt_print.htm'],
			['Auditing', 'nt_audit.htm'],
			['Monitoring', 'nt_rsnet.htm'],
			['Backup', 'nt_bkup.htm'],
			['Directory Services', 'nt_dir.htm'],
			['Optimisation', 'nt_opt.htm'],
			['Analysis', 'nt_ntopt.htm'],
			['Troubleshooting', 'nt_troub.htm'],
		],
		['Win98 ICS', 'win98ics.htm'],
		['DOS Sniffer', 'snif_dos.htm'],
		['Windows Sniffer', 'snif_win.htm'],
		['Building a PC', 'pcbuild.htm'],
		['Intelligent Bldgs', null, null,
			['IB Contents', 'ibs.htm'],
			['Concepts', 'assign1.htm'],
			['Building Systems', 'assign2.htm'],
			['Integrated Building', 'assign4.htm'],
			['Financial Analysis', 'assign5.htm'],
			['Information Technology', 'assign3.htm'],
			['Facilities Management', 'assign6.htm'],
			['Sustainable Design', 'assign7.htm'],
			['Design Management', 'assign8.htm'],
		],
		['Intelligent Bldgs Links', 'ibslinks.htm'],
		['Spelling Codes', 'ispell.htm'],
		['Data Links', 'links.htm'],
		['CV', 'cv.htm'],
		['Future Topics', 'future.htm'],
		['Disclaimer', 'disclaim.htm'],
	],
];