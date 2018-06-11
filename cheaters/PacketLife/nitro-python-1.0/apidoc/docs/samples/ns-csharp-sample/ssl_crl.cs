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
	
	class ssl_crl
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
       
				result = client.addsslcertkey("ca_cert","/nsconfig/ssl/certs/ca_cert.pem",null,false,null,informatsEnum.VALNOTSET,enabledisabledEnum.VALNOTSET,0xFFFFFFFF);
				Console.WriteLine("addsslcertkey	ca_cert : " + result.message);

				result = client.addsslcertkey("root_cert","/nsconfig/ssl/certs/root_cert.pem",null,false,null,informatsEnum.VALNOTSET,enabledisabledEnum.VALNOTSET,0xFFFFFFFF);
				Console.WriteLine("addsslcertkey	root_cert : " + result.message);

				result = client.addsslcrl("crl1","/var/netscaler/ssl/crl.pem",informatsEnum.VALNOTSET);
				Console.WriteLine("addsslcrl	crl1 : " + result.message);

				result = client.setsslcrl_cacert("crl1","ca_cert");
				Console.WriteLine("setsslcrl_cacert	crl1 : " + result.message);

				result = client.addsslcrl("crl1","/var/netscaler/ssl/crl.pem",informatsEnum.VALNOTSET);
				Console.WriteLine("addsslcrl	crl1 : " + result.message);

				result = client.setsslcrl_refresh("crl1",enabledisabledEnum.ENABLED);
				Console.WriteLine("setsslcrl_refresh	crl1 : " + result.message);

				result = client.setsslcrl_cacert("crl1","ca_cert");
				Console.WriteLine("setsslcrl_cacert	crl1 : " + result.message);

				result = client.setsslcrl_server("crl1","10.102.3.120");
				Console.WriteLine("setsslcrl_server	crl1 : " + result.message);

				result = client.setsslcrl_method("crl1",refreshmethodEnum.HTTP,null);
				Console.WriteLine("setsslcrl_method	crl1 : " + result.message);

				result = client.setsslcrl_port("crl1",80);
				Console.WriteLine("setsslcrl_port	crl1 : " + result.message);

				result = client.setsslcrl_interval("crl1",refreshintervlEnum.WEEKLY);
				Console.WriteLine("setsslcrl_interval	crl1 : " + result.message);

				result = client.addsslcrl("crl1","/var/netscaler/ssl/crl.pem",informatsEnum.VALNOTSET);
				Console.WriteLine("addsslcrl	crl1 : " + result.message);

				result = client.setsslcrl_refresh("crl1",enabledisabledEnum.ENABLED);
				Console.WriteLine("setsslcrl_refresh	crl1 : " + result.message);

				result = client.setsslcrl_cacert("crl1","ca_cert");
				Console.WriteLine("setsslcrl_cacert	crl1 : " + result.message);

				result = client.setsslcrl_server("crl1","10.102.3.120");
				Console.WriteLine("setsslcrl_server	crl1 : " + result.message);

				result = client.setsslcrl_method("crl1",refreshmethodEnum.LDAP,null);
				Console.WriteLine("setsslcrl_method	crl1 : " + result.message);

				result = client.setsslcrl_port("crl1",389);
				Console.WriteLine("setsslcrl_port	crl1 : " + result.message);

				result = client.setsslcrl_basedn("crl1","cn=Manager,dc=my-domain,dc=com");
				Console.WriteLine("setsslcrl_basedn	crl1 : " + result.message);

				result = client.setsslcrl_interval("crl1",refreshintervlEnum.WEEKLY);
				Console.WriteLine("setsslcrl_interval	crl1 : " + result.message);

				result = client.logout();
				Console.WriteLine("logout : " + result.message); 
			}
			catch (Exception ex) {
			      Console.WriteLine( "Exception: "+ex.ToString());
			}
		}

	}
	}
