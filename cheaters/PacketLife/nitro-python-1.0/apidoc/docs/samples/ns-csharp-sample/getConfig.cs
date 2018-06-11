/* Sample c# program to demonstrate netscaler api
 
	 Date : 01 Nov 2004 
 Engineer : Ajay Kumar Nema

# Sample C# :  To demonstrate netscaler api "get" methods
# usage : getConfig <NS IP> username password.
## Output:
# > getConfig.exe <NS IP> nsroot nsroot
# login: Done
# getlbvserver: Done
# vip_1:	100.1.1.1:80(HTTP)	DOWN
# getlbvserver  vip_1: Done
# Services bound to vip_1:
# 	s1: 10.1.1.11:80(HTTP)	DOWN
# 	s2:	10.1.1.12:80(HTTP)	DOWN
# getlbvserver(nonesuch): No such resource
# No such resource
# logout: EOF
# >
*/



using System;


namespace NSConfig
{
	/*  ClientService is created from NSConfigService class to handle the cookies */

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

	// Summary description for NSAPITest.
	
	class getConfig
	{
		
		ClientService client=null;
		// The main entry point for the application.
		[STAThread]
		static void Main(string[] args)
		{
			if ( args.Length < 3)
			{
				// usage
				Console.WriteLine("Usage: getConfig <NS IP> username password");
				return;
			} 
			string server_ip = args[0];
			string username = args[1];
			string password = args[2];

			getConfig obj = new getConfig();
			// run the script
			obj.run_commands(server_ip,username,password);
			
		}
	
		// API to run the script.
		void run_commands(string servername,string username,string password)
		{
			
			simpleResult result;
			getlbvserverResult getlbvserverresult;
			getserviceResult	getserviceresult;

			// Initialized the soap client

			Console.WriteLine("\nConnecting to server "+servername+" ............\n"); 
			client = new ClientService(servername);
			client.CookieContainer = new System.Net.CookieContainer();

			// Login request

			result = client.login(username,password) ;
			Console.WriteLine("login : "+result.message);  

			// Get lb vserver 
				
			getlbvserverresult = client.getlbvserver("");
			Console.WriteLine("getlbvserver : "+ getlbvserverresult.message); 
			if (getlbvserverresult.rc.ToString() == "0") 
			{
				for(int i =0 ; i < getlbvserverresult.List.Length;i++)
				{
					lbvserver  obj;
					obj = (lbvserver)getlbvserverresult.List[i];
					Console.WriteLine(obj.name+" :\t"+obj.ipaddress+":"+obj.port +"("+obj.servicetype+")"+ "\t" + obj.state); 
				}
			}
			// Get lb vserver vip_1
			getlbvserverresult = client.getlbvserver("vip_1");
			Console.WriteLine("getlbvserver  vip_1 : "+ getlbvserverresult.message); 
			if (getlbvserverresult.rc.ToString() == "0") 
			{
					lbvserver  obj;
					obj = (lbvserver)getlbvserverresult.List[0];
					Console.WriteLine("Services bound to vip_1 :"); 
					for(int i =0 ; i < obj.servicename.Length;i++)
					{
						// get the bind service in formation.	
						getserviceresult = client.getservice(obj.servicename[i],true,true);
						if (getserviceresult.rc.ToString() == "0") 
						{
							service objsvc = (service)getserviceresult.List[0];
							Console.WriteLine("\t"+objsvc.name+" :\t "+objsvc.ipaddress+":"+objsvc.port+"("+objsvc.servicetype+")" + "\t" + objsvc.svrstate); 
						}
					}
			}
			

			getlbvserverresult = client.getlbvserver("nonesuch");
			Console.WriteLine("getlbvserver(nonesuch) : "+ getlbvserverresult.message);
			result = client.logout();
			Console.WriteLine("logout : " + result.message);
		}
				
	}
}
