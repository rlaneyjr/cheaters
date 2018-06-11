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
	
	class acl 
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
       
				result = client.addnsacl("allow_sip",extaclactionEnum.ALLOW,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	allow_sip : " + result.message);

				result = client.setnsacl_srcip("allow_sip",true,xacloperatorEnum.VALNOTSET,"10.102.3.84");
				Console.WriteLine("setnsacl_srcip	allow_sip : " + result.message);

				result = client.addnsacl("allow_sip_range",extaclactionEnum.ALLOW,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	allow_sip_range : " + result.message);

				result = client.setnsacl_srcip("allow_sip_range",true,xacloperatorEnum.VALNOTSET,"10.102.3.1-10.102.3.255");
				Console.WriteLine("setnsacl_srcip	allow_sip_range : " + result.message);


				result = client.addnsacl("Deny_sipr",extaclactionEnum.DENY,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	Deny_sipr : " + result.message);

				result = client.setnsacl_srcip("Deny_sipr",true,xacloperatorEnum.VALNOTSET,"10.10.0.1-10.102.7.152");
				Console.WriteLine("setnsacl_srcip	Deny_sipr : " + result.message);


				result = client.addnsacl("allow_dip",extaclactionEnum.ALLOW,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	allow_dip : " + result.message);

				result = client.setnsacl_destip("allow_dip",true,xacloperatorEnum.VALNOTSET,"192.168.17.11");
				Console.WriteLine("setnsacl_destip	allow_dip : " + result.message);

				result = client.addnsacl("allow_dip_rng",extaclactionEnum.ALLOW,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	allow_dip_rng : " + result.message);

				result = client.setnsacl_destip("allow_dip_rng",true,xacloperatorEnum.VALNOTSET,"192.168.17.1-192.168.17.250");
				Console.WriteLine("setnsacl_destip	allow_dip_rng : " + result.message);


				result = client.addnsacl("deny_src_mac",extaclactionEnum.DENY,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	deny_src_mac : " + result.message);

				result = client.setnsacl_srcmac("deny_src_mac","00:0d:9d:54:64:6a");
				Console.WriteLine("setnsacl_srcmac	deny_src_mac : " + result.message);

				result = client.addnsacl("acl_user_priority",extaclactionEnum.ALLOW,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	acl_user_priority : " + result.message);

				result = client.setnsacl_priority("acl_user_priority",1);
				Console.WriteLine("setnsacl_priority	acl_user_priority : " + result.message);


				result = client.addnsacl("Deny_dip_intf",extaclactionEnum.DENY,0xFFFFFFFF,extaclprotoenumEnum.VALNOTSET,false,0xFFFFFFFF,0xFFFFFFFF);
				Console.WriteLine("addnsacl	Deny_dip_intf : " + result.message);

                		result = client.disablensacl("allow_sip");
                		Console.WriteLine("disablensacl	allow_sip : " + result.message);

                		result = client.rmnsacl("allow_sip");	  
                		Console.WriteLine("rmnsacl	allow_sip : " + result.message);

				result = client.clearnsacls();
				Console.WriteLine("clearnsacls	Deny_sip_dip_dport : " + result.message);

				result = client.logout();
				Console.WriteLine("logout : " + result.message); 
			}
			catch (Exception ex) {
			      Console.WriteLine( "Exception: "+ex.ToString());
			}
		}

	}
	}
