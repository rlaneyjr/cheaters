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
	
	class csw 
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

				result = client.enablensfeature(featureEnum.CS);
				Console.WriteLine("enablensfeature	CS : " + result.message);

				result = client.addserver("s1","10.102.3.91",null,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addserver	s1 : " + result.message);

				result = client.addserver("s2","10.102.3.92",null,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addserver	s2 : " + result.message);

				result = client.addserver("s3","10.102.3.93",null,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addserver	s3 : " + result.message);

				result = client.addservice("srv1",null,"s1",servicetypeEnum.HTTP,80,0xFFFFFFFF,cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addservice	srv1 : " + result.message);

				result = client.addservice("srv2",null,"s2",servicetypeEnum.HTTP,80,0xFFFFFFFF,cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addservice	srv2 : " + result.message);

				result = client.addservice("srv3",null,"s3",servicetypeEnum.HTTP,80,0xFFFFFFFF,cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("addservice	srv3 : " + result.message);

				result = client.addlbvserver("lbvip1",vservicetypeEnum.HTTP,null,0xFFFFFFFF,0xFFFFFFFF,enabledisabledEnum.VALNOTSET,null);
				Console.WriteLine("addlbvserver	lbvip1 : " + result.message);

				result = client.addlbvserver("lbvip2",vservicetypeEnum.HTTP,null,0xFFFFFFFF,0xFFFFFFFF,enabledisabledEnum.VALNOTSET,null);
				Console.WriteLine("addlbvserver	lbvip2 : " + result.message);

				result = client.addlbvserver("lbvip3",vservicetypeEnum.HTTP,null,0xFFFFFFFF,0xFFFFFFFF,enabledisabledEnum.VALNOTSET,null);
				Console.WriteLine("addlbvserver	lbvip3 : " + result.message);

				result = client.bindlbvserver_service("lbvip1","srv1",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	lbvip1 : " + result.message);

				result = client.bindlbvserver_service("lbvip2","srv2",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	lbvip2 : " + result.message);

				result = client.bindlbvserver_service("lbvip3","srv3",0xFFFFFFFF);
				Console.WriteLine("bindlbvserver_service	lbvip3 : " + result.message);

				result = client.addcspolicy("contains_html",null,"REQ.HTTP.URL CONTAINS html",null);
				Console.WriteLine("addcspolicy	contains_html : " + result.message);

				result = client.addcspolicy("contains_txt",null,"REQ.HTTP.URL CONTAINS gif",null);
				Console.WriteLine("addcspolicy	contains_txt : " + result.message);

				result = client.addcspolicy("contains_gif",null,"REQ.HTTP.URL CONTAINS asp",null);
				Console.WriteLine("addcspolicy	contains_gif : " + result.message);

				result = client.addcsvserver("csvip",csvservicetypeEnum.HTTP,"10.102.3.54",0xFFFFFFFF,80,enabledisabledEnum.VALNOTSET,null);
				Console.WriteLine("addcsvserver	csvip : " + result.message);

				result = client.bindcsvserver_targetvserver("csvip","lbvip1","contains_html",5,null,vserverbindpointEnum.VALNOTSET,false,policylabelinvoketypeEnum.VALNOTSET,null);
				Console.WriteLine("bindcsvserver_targetvserver	csvip : " + result.message);

				result = client.bindcsvserver_targetvserver("csvip","lbvip2","contains_txt",5,null,vserverbindpointEnum.VALNOTSET,false,policylabelinvoketypeEnum.VALNOTSET,null);
				Console.WriteLine("bindcsvserver_targetvserver	csvip : " + result.message);

				result = client.bindcsvserver_targetvserver("csvip","lbvip3","contains_gif",5,null,vserverbindpointEnum.VALNOTSET,false,policylabelinvoketypeEnum.VALNOTSET,null);
				Console.WriteLine("bindcsvserver_targetvserver	csvip : " + result.message);

				result = client.logout();
				Console.WriteLine("logout : " + result.message); 
			}
			catch (Exception ex) {
			      Console.WriteLine( "Exception: "+ex.ToString());
			}
		}

	}
	}
