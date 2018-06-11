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
	
	class ssl
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
       
				result = client.addserver("s1","10.102.3.84",null,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addserver	s1 : " + result.message);

				result = client.addserver("s2","10.102.3.83",null,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addserver	s2 : " + result.message);

				result = client.addservice("src1",null,"s1",servicetypeEnum.HTTP,80,0xFFFFFFFF,cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addservice	src1 : " + result.message);

				result = client.addservice("src2",null,"s2",servicetypeEnum.HTTP,80,0xFFFFFFFF,cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addservice	src2 : " + result.message);

				result = client.addlbvserver("sslbase",vservicetypeEnum.SSL,"10.102.3.100",443,0xFFFFFFFF,enabledisabledEnum.VALNOTSET,null);
				Console.WriteLine("addlbvserver	sslbase : " + result.message);

				result = client.bindlbvserver_service("sslbase","src1",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	sslbase : " + result.message);

				result = client.bindlbvserver_service("sslbase","src2",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	sslbase : " + result.message);

				result = client.addsslcertkey("server_cert","/nsconfig/ssl/certs/cert1.pem","/nsconfig/ssl/certs/cert1ky.pem",false,null,informatsEnum.VALNOTSET,enabledisabledEnum.VALNOTSET,0xFFFFFFFF);
				Console.WriteLine("addsslcertkey	server_cert : " + result.message);

				result = client.bindsslcertkey_vserver("server_cert","sslbase",false);
				Console.WriteLine("bindsslcertkey_vserver	server_cert : " + result.message);

				result = client.logout();
				Console.WriteLine("logout : " + result.message); 
			}
			catch (Exception ex) {
			      Console.WriteLine( "Exception: "+ex.ToString());
			}
		}

	}
	}
