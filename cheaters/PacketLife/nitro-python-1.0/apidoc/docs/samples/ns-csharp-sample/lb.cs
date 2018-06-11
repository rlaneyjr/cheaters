using System;
using System.Runtime.Remoting;
using System.Xml.Serialization;
using System.Web.Services;
    
	namespace NSConfig {
		public class ClientService : NSConfigService

                {
                        private string cookie = null;
                        /* override the getWebRequest to send cookie */
                        protected override System.Net.WebRequest  GetWebRequest(Uri uri)
                        {
                                System.Net.HttpWebRequest req = (System.Net.HttpWebRequest) base.GetWebRequest(uri);
                                if (cookie != null)
                                {
                                        req.Headers.Add("Set-Cookie", cookie);
                                }
                                return req;
                        }
                        /* override the getWebResponse to get the cookie */

                        protected override System.Net.WebResponse GetWebResponse(System.Net.WebRequest req)
                        {
                               System.Net.HttpWebResponse rep = (System.Net.HttpWebResponse) base.GetWebResponse(req);
                               if (rep.Headers["Set-Cookie"] != null)
                                {
                                       cookie = rep.Headers["Set-Cookie"];
                                }
                                return rep;
			}
                        public ClientService()
                        {
                                // Change the IP address pointing to netscaler.
                                this.Url = "http://10.102.4.111:18000";
                        }
                        public ClientService(string servername)
                        {
                                this.Url = "http://"+servername+"/soap";;
                        }
                }
	
	class lb 
	{
 		static ClientService client=null;
 
		[STAThread]
		static void Main(string[] args)
		{
			if ( args.Length < 3)
			{
				Console.WriteLine("Usage: getConfig <NS IP> username password");
				return;
			}
			string serverip = args[0];
			string username = args[1];
			string password = args[2];
			try {
          			Console.WriteLine("\nConnecting to server "+serverip+" ............\n");
				client = new ClientService(serverip);

				client.CookieContainer = new System.Net.CookieContainer();
				simpleResult result = client.login(username,password) ;
				Console.WriteLine("login : "+result.message);
       
				result = client.enablensfeature(featureEnum.LB);
				Console.WriteLine("enablensfeature	LB : " + result.message);

				result = client.addserver("s1","10.102.3.81",null,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addserver	s1 : " + result.message);

				result = client.addserver("s2","10.102.3.82",null,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addserver	s2 : " + result.message);

				result = client.addservice("svc1",null,"s1",servicetypeEnum.HTTP,80,0xFFFFFFFF,cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addservice	svc1 : " + result.message);

				result = client.addservice("svc2",null,"s2",servicetypeEnum.HTTP,80,0xFFFFFFFF,cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addservice	svc2 : " + result.message);

				getserverResult  getserverresult1 = client.getserver(null,false);
				Console.WriteLine("getserver	null : " + getserverresult1.message);

				if ( (getserverresult1.List != null) && (getserverresult1.List.Length > 0)) {
					for(int i =0 ; i < getserverresult1.List.Length;i++) { 
						server obj;
						obj = (server) getserverresult1.List[i];
						Console.WriteLine( obj.name + "\t" + obj.internaL + "\t" + obj.ipaddress + "\t" + obj.state + "\t" + obj.domain + "\t" + obj.domainresolveretry + "\t" + obj.servicename + "\t" + obj.servicegroupname + "\t" + obj.translationip + "\t" + obj.translationmask + "\t" );
					}
				}

				getserviceResult  getserviceresult2 = client.getservice(null,false,false);
				Console.WriteLine("getservice	null : " + getserviceresult2.message);

				if ( (getserviceresult2.List != null) && (getserviceresult2.List.Length > 0)) {
					for(int i =0 ; i < getserviceresult2.List.Length;i++) { 
						service obj;
						obj = (service) getserviceresult2.List[i];
						Console.WriteLine( obj.name + "\t" + obj.all + "\t" + obj.internaL + "\t" + obj.servername + "\t" + obj.servicetype + "\t" + obj.serviceconftype + "\t" + obj.port + "\t" + obj.value + "\t" + obj.cleartextport + "\t" + obj.gslb + "\t" + obj.cachetype + "\t" + obj.maxclient + "\t" + obj.maxreq + "\t" + obj.cacheable + "\t" + obj.cip + "\t" + obj.cipheader + "\t" + obj.usip + "\t" + obj.useproxyport + "\t" + obj.sc + "\t" + obj.weight + "\t" + obj.sp + "\t" + obj.rtspsessionidremap + "\t" + obj.failedprobes + "\t" + obj.clttimeout + "\t" + obj.totalprobes + "\t" + obj.svrtimeout + "\t" + obj.serverid + "\t" + obj.cka + "\t" + obj.tcpb + "\t" + obj.cmp + "\t" + obj.maxbandwidth + "\t" + obj.accessdown + "\t" + obj.svrstate + "\t" + obj.delay + "\t" + obj.ipaddress + "\t" + obj.monitorname + "\t" + obj.monthreshold + "\t" + obj.monstate + "\t" + obj.monstatcode + "\t" + obj.responsetime + "\t" + obj.downstateflush + "\t" + obj.statechangetimesec + "\t" + obj.statechangetimemsec + "\t" + obj.timesincelaststatechange + "\t" + obj.tickssincelaststatechange + "\t" + obj.stateupdatereason + "\t" + obj.runningmonstate + "\t" + obj.scpolicyname + "\t" + obj.dospolicyname + "\t" );
					}
				}

				result = client.addlbvserver("vlb1",vservicetypeEnum.HTTP,"10.102.3.101",80,0xFFFFFFFF,enabledisabledEnum.VALNOTSET,null);
				Console.WriteLine("addlbvserver	vlb1 : " + result.message);

				result = client.addlbvserver("vlb2",vservicetypeEnum.SSL,"10.102.3.102",443,0xFFFFFFFF,enabledisabledEnum.VALNOTSET,null);
				Console.WriteLine("addlbvserver	vlb2 : " + result.message);

				getlbvserverResult  getlbvserverresult3 = client.getlbvserver("vlb1");
				Console.WriteLine("getlbvserver	vlb1 : " + getlbvserverresult3.message);

				if ( (getlbvserverresult3.List != null) && (getlbvserverresult3.List.Length > 0)) {
					for(int i =0 ; i < getlbvserverresult3.List.Length;i++) { 
						lbvserver obj;
						obj = (lbvserver) getlbvserverresult3.List[i];
						Console.WriteLine( obj.name + "\t" + obj.insertvserveripport + "\t" + obj.vipheader + "\t" + obj.value + "\t" + obj.ipaddress + "\t" + obj.ipmapping + "\t" + obj.port + "\t" + obj.range + "\t" + obj.servicetype + "\t" + obj.type + "\t" + obj.state + "\t" + obj.effectivestate + "\t" + obj.status + "\t" + obj.lbrrreason + "\t" + obj.cachetype + "\t" + obj.redirect + "\t" + obj.precedence + "\t" + obj.redirecturl + "\t" + obj.authentication + "\t" + obj.homepage + "\t" + obj.dnsvservername + "\t" + obj.domain + "\t" + obj.policyname + "\t" + obj.servicename + "\t" + obj.weight + "\t" + obj.dynamicweight + "\t" + obj.cachevserver + "\t" + obj.backupvserver + "\t" + obj.priority + "\t" + obj.clttimeout + "\t" + obj.somethod + "\t" + obj.sopersistence + "\t" + obj.sopersistencetimeout + "\t" + obj.sothreshold + "\t" + obj.lbmethod + "\t" + obj.hashlength + "\t" + obj.dataoffset + "\t" + obj.health + "\t" + obj.datalength + "\t" + obj.netmask + "\t" + obj.rule + "\t" + obj.resrule + "\t" + obj.gotopriorityexpression + "\t" + obj.ruletype + "\t" + obj.groupname + "\t" + obj.m + "\t" + obj.persistencetype + "\t" + obj.timeout + "\t" + obj.cookiedomain + "\t" + obj.persistmask + "\t" + obj.persistencebackup + "\t" + obj.backuppersistencetimeout + "\t" + obj.cacheable + "\t" + obj.pq + "\t" + obj.sc + "\t" + obj.rtspnat + "\t" + obj.sessionless + "\t" + obj.map + "\t" + obj.connfailover + "\t" + obj.redirectportrewrite + "\t" + obj.downstateflush + "\t" + obj.disableprimaryondown + "\t" + obj.thresholdvalue + "\t" + obj.invoke + "\t" + obj.labeltype + "\t" + obj.labelname + "\t" + obj.cookieipport + "\t" + obj.vserverid + "\t" + obj.version + "\t" + obj.totalservices + "\t" + obj.activeservices + "\t" + obj.statechangetimesec + "\t" + obj.statechangetimemsec + "\t" + obj.tickssincelaststatechange + "\t" + obj.hits + "\t" + obj.svcipaddress + "\t" + obj.svcport + "\t" + obj.svctype + "\t" + obj.svcstate + "\t" + obj.servicegroupname + "\t" + obj.scpolicyname + "\t" + obj.scpolicypriority + "\t" + obj.dospolicyname + "\t" + obj.dospolicypriority + "\t" + obj.rwpolicyname + "\t" + obj.rwpolicypriority + "\t" + obj.rwpolicygotoprioexpression + "\t" + obj.rwpolicybindpoint + "\t" + obj.rwinvoke + "\t" + obj.rwpolicyinvokelabeltype + "\t" + obj.rwpolicyinvokelabelname + "\t" + obj.cachepolicyname + "\t" + obj.cachepolicypriority + "\t" + obj.cachepolicygotoprioexpression + "\t" + obj.cachepolicybindpoint + "\t" + obj.cacheinvoke + "\t" + obj.cachepolicyinvokelabeltype + "\t" + obj.cachepolicyinvokelabelname + "\t" + obj.rsppolicyname + "\t" + obj.rsppolicypriority + "\t" + obj.rsppolicygotoprioexpression + "\t" + obj.rspinvoke + "\t" + obj.rsppolicyinvokelabeltype + "\t" + obj.rsppolicyinvokelabelname + "\t" + obj.csvserver + "\t" + obj.cswpolicyname + "\t" + obj.priority + "\t" );
					}
				}

				getlbvserverResult  getlbvserverresult4 = client.getlbvserver("vlb2");
				Console.WriteLine("getlbvserver	vlb2 : " + getlbvserverresult4.message);

				if ( (getlbvserverresult4.List != null) && (getlbvserverresult4.List.Length > 0)) {
					for(int i =0 ; i < getlbvserverresult4.List.Length;i++) { 
						lbvserver obj;
						obj = (lbvserver) getlbvserverresult4.List[i];
						Console.WriteLine( obj.name + "\t" + obj.insertvserveripport + "\t" + obj.vipheader + "\t" + obj.value + "\t" + obj.ipaddress + "\t" + obj.ipmapping + "\t" + obj.port + "\t" + obj.range + "\t" + obj.servicetype + "\t" + obj.type + "\t" + obj.state + "\t" + obj.effectivestate + "\t" + obj.status + "\t" + obj.lbrrreason + "\t" + obj.cachetype + "\t" + obj.redirect + "\t" + obj.precedence + "\t" + obj.redirecturl + "\t" + obj.authentication + "\t" + obj.homepage + "\t" + obj.dnsvservername + "\t" + obj.domain + "\t" + obj.policyname + "\t" + obj.servicename + "\t" + obj.weight + "\t" + obj.dynamicweight + "\t" + obj.cachevserver + "\t" + obj.backupvserver + "\t" + obj.priority + "\t" + obj.clttimeout + "\t" + obj.somethod + "\t" + obj.sopersistence + "\t" + obj.sopersistencetimeout + "\t" + obj.sothreshold + "\t" + obj.lbmethod + "\t" + obj.hashlength + "\t" + obj.dataoffset + "\t" + obj.health + "\t" + obj.datalength + "\t" + obj.netmask + "\t" + obj.rule + "\t" + obj.resrule + "\t" + obj.gotopriorityexpression + "\t" + obj.ruletype + "\t" + obj.groupname + "\t" + obj.m + "\t" + obj.persistencetype + "\t" + obj.timeout + "\t" + obj.cookiedomain + "\t" + obj.persistmask + "\t" + obj.persistencebackup + "\t" + obj.backuppersistencetimeout + "\t" + obj.cacheable + "\t" + obj.pq + "\t" + obj.sc + "\t" + obj.rtspnat + "\t" + obj.sessionless + "\t" + obj.map + "\t" + obj.connfailover + "\t" + obj.redirectportrewrite + "\t" + obj.downstateflush + "\t" + obj.disableprimaryondown + "\t" + obj.thresholdvalue + "\t" + obj.invoke + "\t" + obj.labeltype + "\t" + obj.labelname + "\t" + obj.cookieipport + "\t" + obj.vserverid + "\t" + obj.version + "\t" + obj.totalservices + "\t" + obj.activeservices + "\t" + obj.statechangetimesec + "\t" + obj.statechangetimemsec + "\t" + obj.tickssincelaststatechange + "\t" + obj.hits + "\t" + obj.svcipaddress + "\t" + obj.svcport + "\t" + obj.svctype + "\t" + obj.svcstate + "\t" + obj.servicegroupname + "\t" + obj.scpolicyname + "\t" + obj.scpolicypriority + "\t" + obj.dospolicyname + "\t" + obj.dospolicypriority + "\t" + obj.rwpolicyname + "\t" + obj.rwpolicypriority + "\t" + obj.rwpolicygotoprioexpression + "\t" + obj.rwpolicybindpoint + "\t" + obj.rwinvoke + "\t" + obj.rwpolicyinvokelabeltype + "\t" + obj.rwpolicyinvokelabelname + "\t" + obj.cachepolicyname + "\t" + obj.cachepolicypriority + "\t" + obj.cachepolicygotoprioexpression + "\t" + obj.cachepolicybindpoint + "\t" + obj.cacheinvoke + "\t" + obj.cachepolicyinvokelabeltype + "\t" + obj.cachepolicyinvokelabelname + "\t" + obj.rsppolicyname + "\t" + obj.rsppolicypriority + "\t" + obj.rsppolicygotoprioexpression + "\t" + obj.rspinvoke + "\t" + obj.rsppolicyinvokelabeltype + "\t" + obj.rsppolicyinvokelabelname + "\t" + obj.csvserver + "\t" + obj.cswpolicyname + "\t" + obj.priority + "\t" );
					}
				}

				result = client.bindlbvserver_service("vlb1","svc1",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	vlb1 : " + result.message);

				result = client.bindlbvserver_service("vlb1","svc2",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	vlb1 : " + result.message);

				result = client.bindlbvserver_service("vlb2","svc1",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	vlb2 : " + result.message);

				result = client.bindlbvserver_service("vlb2","svc2",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	vlb2 : " + result.message);

				getvserverResult  getvserverresult5 = client.getvserver("vlb1");
				Console.WriteLine("getvserver	vlb1 : " + getvserverresult5.message);

				if ( (getvserverresult5.List != null) && (getvserverresult5.List.Length > 0)) {
					for(int i =0 ; i < getvserverresult5.List.Length;i++) { 
						vserver obj;
						obj = (vserver) getvserverresult5.List[i];
						Console.WriteLine( obj.name + "\t" + obj.insertvserveripport + "\t" + obj.vipheader + "\t" + obj.ipaddress + "\t" + obj.port + "\t" + obj.range + "\t" + obj.servicetype + "\t" + obj.value + "\t" + obj.type + "\t" + obj.state + "\t" + obj.effectivestate + "\t" + obj.status + "\t" + obj.cachetype + "\t" + obj.redirect + "\t" + obj.precedence + "\t" + obj.redirecturl + "\t" + obj.authentication + "\t" + obj.homepage + "\t" + obj.dnsvservername + "\t" + obj.domain + "\t" + obj.rule + "\t" + obj.policyname + "\t" + obj.hits + "\t" + obj.servicename + "\t" + obj.weight + "\t" + obj.cachevserver + "\t" + obj.backupvserver + "\t" + obj.priority + "\t" + obj.clttimeout + "\t" + obj.somethod + "\t" + obj.sopersistence + "\t" + obj.sothreshold + "\t" + obj.lbmethod + "\t" + obj.hashlength + "\t" + obj.dataoffset + "\t" + obj.datalength + "\t" + obj.netmask + "\t" + obj.groupname + "\t" + obj.m + "\t" + obj.persistencetype + "\t" + obj.cookiedomain + "\t" + obj.persistmask + "\t" + obj.persistencebackup + "\t" + obj.timeout + "\t" + obj.cacheable + "\t" + obj.pq + "\t" + obj.sc + "\t" + obj.sessionless + "\t" + obj.url + "\t" + obj.reuse + "\t" + obj.destinationvserver + "\t" + obj.via + "\t" + obj.flags + "\t" + obj.connfailover + "\t" + obj.casesensitive + "\t" + obj.redirectportrewrite + "\t" + obj.downstateflush + "\t" + obj.cookieipport + "\t" + obj.vserverid + "\t" + obj.version + "\t" + obj.totalservices + "\t" + obj.activeservices + "\t" );
					}
				}

				getvserverResult  getvserverresult6 = client.getvserver("vlb2");
				Console.WriteLine("getvserver	vlb2 : " + getvserverresult6.message);

				if ( (getvserverresult6.List != null) && (getvserverresult6.List.Length > 0)) {
					for(int i =0 ; i < getvserverresult6.List.Length;i++) { 
						vserver obj;
						obj = (vserver) getvserverresult6.List[i];
						Console.WriteLine( obj.name + "\t" + obj.insertvserveripport + "\t" + obj.vipheader + "\t" + obj.ipaddress + "\t" + obj.port + "\t" + obj.range + "\t" + obj.servicetype + "\t" + obj.value + "\t" + obj.type + "\t" + obj.state + "\t" + obj.effectivestate + "\t" + obj.status + "\t" + obj.cachetype + "\t" + obj.redirect + "\t" + obj.precedence + "\t" + obj.redirecturl + "\t" + obj.authentication + "\t" + obj.homepage + "\t" + obj.dnsvservername + "\t" + obj.domain + "\t" + obj.rule + "\t" + obj.policyname + "\t" + obj.hits + "\t" + obj.servicename + "\t" + obj.weight + "\t" + obj.cachevserver + "\t" + obj.backupvserver + "\t" + obj.priority + "\t" + obj.clttimeout + "\t" + obj.somethod + "\t" + obj.sopersistence + "\t" + obj.sothreshold + "\t" + obj.lbmethod + "\t" + obj.hashlength + "\t" + obj.dataoffset + "\t" + obj.datalength + "\t" + obj.netmask + "\t" + obj.groupname + "\t" + obj.m + "\t" + obj.persistencetype + "\t" + obj.cookiedomain + "\t" + obj.persistmask + "\t" + obj.persistencebackup + "\t" + obj.timeout + "\t" + obj.cacheable + "\t" + obj.pq + "\t" + obj.sc + "\t" + obj.sessionless + "\t" + obj.url + "\t" + obj.reuse + "\t" + obj.destinationvserver + "\t" + obj.via + "\t" + obj.flags + "\t" + obj.connfailover + "\t" + obj.casesensitive + "\t" + obj.redirectportrewrite + "\t" + obj.downstateflush + "\t" + obj.cookieipport + "\t" + obj.vserverid + "\t" + obj.version + "\t" + obj.totalservices + "\t" + obj.activeservices + "\t" );
					}
				}

				result = client.bindlbgroup_vserver("grp1","vlb1,vlb2");
				Console.WriteLine("bindlbgroup_vserver	grp1 : " + result.message);

				getlbgroupResult  getlbgroupresult7 = client.getlbgroup("grp1");
				Console.WriteLine("getlbgroup	grp1 : " + getlbgroupresult7.message);

				if ( (getlbgroupresult7.List != null) && (getlbgroupresult7.List.Length > 0)) {
					for(int i =0 ; i < getlbgroupresult7.List.Length;i++) { 
						lbgroup obj;
						obj = (lbgroup) getlbgroupresult7.List[i];
						Console.WriteLine( obj.name + "\t" + obj.vservername + "\t" + obj.persistencetype + "\t" + obj.persistencebackup + "\t" + obj.backuppersistencetimeout + "\t" + obj.persistmask + "\t" + obj.cookiedomain + "\t" + obj.timeout + "\t" );
					}
				}

				result = client.setlbgroup_persistencetype("grp1",grppersisttypeEnum.COOKIEINSERT);
				Console.WriteLine("setlbgroup_persistencetype	grp1 : " + result.message);

				result = client.setlbgroup_timeout("grp1",10);
				Console.WriteLine("setlbgroup_timeout	grp1 : " + result.message);

				getlbgroupResult  getlbgroupresult8 = client.getlbgroup("grp1");
				Console.WriteLine("getlbgroup	grp1 : " + getlbgroupresult8.message);

				if ( (getlbgroupresult8.List != null) && (getlbgroupresult8.List.Length > 0)) {
					for(int i =0 ; i < getlbgroupresult8.List.Length;i++) { 
						lbgroup obj;
						obj = (lbgroup) getlbgroupresult8.List[i];
						Console.WriteLine( obj.name + "\t" + obj.vservername + "\t" + obj.persistencetype + "\t" + obj.persistencebackup + "\t" + obj.backuppersistencetimeout + "\t" + obj.persistmask + "\t" + obj.cookiedomain + "\t" + obj.timeout + "\t" );
					}
				}

				getvserverResult  getvserverresult9 = client.getvserver(null);
				Console.WriteLine("getvserver	null : " + getvserverresult9.message);

				if ( (getvserverresult9.List != null) && (getvserverresult9.List.Length > 0)) {
					for(int i =0 ; i < getvserverresult9.List.Length;i++) { 
						vserver obj;
						obj = (vserver) getvserverresult9.List[i];
						Console.WriteLine( obj.name + "\t" + obj.insertvserveripport + "\t" + obj.vipheader + "\t" + obj.ipaddress + "\t" + obj.port + "\t" + obj.range + "\t" + obj.servicetype + "\t" + obj.value + "\t" + obj.type + "\t" + obj.state + "\t" + obj.effectivestate + "\t" + obj.status + "\t" + obj.cachetype + "\t" + obj.redirect + "\t" + obj.precedence + "\t" + obj.redirecturl + "\t" + obj.authentication + "\t" + obj.homepage + "\t" + obj.dnsvservername + "\t" + obj.domain + "\t" + obj.rule + "\t" + obj.policyname + "\t" + obj.hits + "\t" + obj.servicename + "\t" + obj.weight + "\t" + obj.cachevserver + "\t" + obj.backupvserver + "\t" + obj.priority + "\t" + obj.clttimeout + "\t" + obj.somethod + "\t" + obj.sopersistence + "\t" + obj.sothreshold + "\t" + obj.lbmethod + "\t" + obj.hashlength + "\t" + obj.dataoffset + "\t" + obj.datalength + "\t" + obj.netmask + "\t" + obj.groupname + "\t" + obj.m + "\t" + obj.persistencetype + "\t" + obj.cookiedomain + "\t" + obj.persistmask + "\t" + obj.persistencebackup + "\t" + obj.timeout + "\t" + obj.cacheable + "\t" + obj.pq + "\t" + obj.sc + "\t" + obj.sessionless + "\t" + obj.url + "\t" + obj.reuse + "\t" + obj.destinationvserver + "\t" + obj.via + "\t" + obj.flags + "\t" + obj.connfailover + "\t" + obj.casesensitive + "\t" + obj.redirectportrewrite + "\t" + obj.downstateflush + "\t" + obj.cookieipport + "\t" + obj.vserverid + "\t" + obj.version + "\t" + obj.totalservices + "\t" + obj.activeservices + "\t" );
					}
				}

				result = client.addsslcertkey("test_cert","/nsconfig/ssl/1024cert.pem","/nsconfig/ssl/1024key.pem",false,null,informatsEnum.VALNOTSET,enabledisabledEnum.VALNOTSET,0xFFFFFFFF);
				Console.WriteLine("addsslcertkey	test_cert : " + result.message);

				result = client.bindsslcertkey_vserver("test_cert","vlb2",false);
				Console.WriteLine("bindsslcertkey_vserver	test_cert : " + result.message);

				result = client.logout();
				Console.WriteLine("logout : " + result.message); 
			}
			catch (Exception ex) {
			      Console.WriteLine( "Exception: "+ex.ToString());
			}
		}

	}
	}
