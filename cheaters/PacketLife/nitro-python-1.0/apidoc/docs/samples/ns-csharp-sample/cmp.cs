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
	
	class cmp 
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
       
				result = client.enablensfeature(featureEnum.CMP);
				Console.WriteLine("enablensfeature	CMP : " + result.message);

                		result = client.addserver("s1", "10.102.3.91", null, enabledisabledEnum.VALNOTSET);
                		Console.WriteLine("addserver	s1 : " + result.message);
				
                		result = client.addserver("s2", "10.102.3.92", null, enabledisabledEnum.VALNOTSET);
                		Console.WriteLine("addserver	s2 : " + result.message);

                		result = client.addservice("srv1", null, "s1", servicetypeEnum.HTTP, 80, 0xFFFFFFFF, cachtypeEnum.VALNOTSET, enabledisabledEnum.VALNOTSET);
                		Console.WriteLine("addservice	srv1 : " + result.message);

                		result = client.addservice("srv2", null, "s2", servicetypeEnum.HTTP, 80, 0xFFFFFFFF, cachtypeEnum.VALNOTSET, enabledisabledEnum.VALNOTSET);
                		Console.WriteLine("addservice	srv2 : " + result.message);


                		result = client.addlbvserver("lbvip1", vservicetypeEnum.HTTP, null, 0xFFFFFFFF, 0xFFFFFFFF, enabledisabledEnum.VALNOTSET, null);
                		Console.WriteLine("addlbvserver	lbvip1 : " + result.message);

                		result = client.addlbvserver("lbvip2", vservicetypeEnum.HTTP, null, 0xFFFFFFFF, 0xFFFFFFFF, enabledisabledEnum.VALNOTSET, null);
                		Console.WriteLine("addlbvserver	lbvip2 : " + result.message);


                		result = client.bindlbvserver_service("lbvip1", "srv1", 0xFFFFFFFF);
                		Console.WriteLine("bindlbvserver_service	lbvip1 : " + result.message);

                		result = client.bindlbvserver_service("lbvip2", "srv2", 0xFFFFFFFF);
                		Console.WriteLine("bindlbvserver_service	lbvip2 : " + result.message);


				result = client.setservice_cmp("srv1",yesnoEnum.YES);
				Console.WriteLine("setservice_cmp	srv1 : " + result.message);

				result = client.setservice_cmp("srv2",yesnoEnum.NO);
				Console.WriteLine("setservice_cmp	srv2 : " + result.message);

				result = client.addcmppolicy("cmp1","url == /testsite/file5.html","nocompress");
				Console.WriteLine("addcmppolicy	cmp1 : " + result.message);

				result = client.bindcmpglobal_policy("cmp1",0xFFFFFFFF,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("bindcmpglobal_policy	cmp1 : " + result.message);

				result = client.addpolicyexpression("ex1","RES.HTTP.HEADER Content-Type CONTAINS application/msword");
				Console.WriteLine("addpolicyexpression	ex1 : " + result.message);

				result = client.addcmppolicy("cmp2","ex1","deflate");
				Console.WriteLine("addcmppolicy	cmp2 : " + result.message);

				result = client.bindcmpglobal_policy("cmp2",0xFFFFFFFF,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("bindcmpglobal_policy	cmp2 : " + result.message);

				result = client.addcmppolicy("cmp3","url contains file50 || RES.HTTP.HEADER Content-Type CONTAINS text/css","deflate");
				Console.WriteLine("addcmppolicy	cmp3 : " + result.message);

				result = client.addpolicyexpression("ex2","HEADER User-Agent CONTAINS MSIE");
				Console.WriteLine("addpolicyexpression	ex2 : " + result.message);

				result = client.addpolicyexpression("ex3","RES.HTTP.HEADER Content-Type CONTAINS application/vnd.ms-excel");
				Console.WriteLine("addpolicyexpression	ex3 : " + result.message);

				result = client.addcmppolicy("cmp4","ex2&&ex3","gzip");
				Console.WriteLine("addcmppolicy	cmp4 : " + result.message);

				result = client.logout();
				Console.WriteLine("logout : " + result.message); 
			}
			catch (Exception ex) {
			      Console.WriteLine( "Exception: "+ex.ToString());
			}
		}

	}
	}
