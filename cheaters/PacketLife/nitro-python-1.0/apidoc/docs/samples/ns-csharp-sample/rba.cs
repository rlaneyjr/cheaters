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
	
	class rba 
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
       
				result = client.addsystemuser("user1","passwd1");
				Console.WriteLine("addsystemuser	user1 : " + result.message);

				result = client.addsystemuser("user2","passwd2");
				Console.WriteLine("addsystemuser	user2 : " + result.message);

				result = client.bindsystemuser_policy("user1","read-only",1);
				Console.WriteLine("bindsystemuser_policy	user1 : " + result.message);

				result = client.bindsystemuser_policy("user1","operator",2);
				Console.WriteLine("bindsystemuser_policy	user1 : " + result.message);

				result = client.addsystemgroup("group1");
				Console.WriteLine("addsystemgroup	group1 : " + result.message);

				result = client.bindsystemgroup_user("group1","user2");
				Console.WriteLine("bindsystemgroup_user	group1 : " + result.message);

				result = client.bindsystemgroup_policy("group1","read-only",1);
				Console.WriteLine("bindsystemgroup_policy	group1 : " + result.message);

				result = client.addsystemcmdpolicy("add_pol1",allowdenyEnum.ALLOW,"^add.*");
				Console.WriteLine("addsystemcmdpolicy	add_pol1 : " + result.message);

				result = client.bindsystemuser_policy("user1","add_pol1",3);
				Console.WriteLine("bindsystemuser_policy	user1 : " + result.message);

				getsystemuserResult  getsystemuserresult1 = client.getsystemuser(null);
				Console.WriteLine("getsystemuser	null : " + getsystemuserresult1.message);

				if ( (getsystemuserresult1.List != null) && (getsystemuserresult1.List.Length > 0)) {
					for(int i =0 ; i < getsystemuserresult1.List.Length;i++) { 
						systemuser obj;
						obj = (systemuser) getsystemuserresult1.List[i];
						Console.WriteLine( obj.username + "\t" + obj.groupname + "\t" + obj.policyname + "\t" + obj.priority + "\t" );
					}
				}

				getsystemgroupResult  getsystemgroupresult2 = client.getsystemgroup(null);
				Console.WriteLine("getsystemgroup	null : " + getsystemgroupresult2.message);

				if ( (getsystemgroupresult2.List != null) && (getsystemgroupresult2.List.Length > 0)) {
					for(int i =0 ; i < getsystemgroupresult2.List.Length;i++) { 
						systemgroup obj;
						obj = (systemgroup) getsystemgroupresult2.List[i];
						Console.WriteLine( obj.groupname + "\t" + obj.username + "\t" + obj.policyname + "\t" + obj.priority + "\t" );
					}
				}

				result = client.logout();
				Console.WriteLine("logout : " + result.message); 
			}
			catch (Exception ex) {
			      Console.WriteLine( "Exception: "+ex.ToString());
			}
		}

	}
	}
