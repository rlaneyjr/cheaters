/* Sample c# program to demonstrate netscaler api
 
	 Date : 01 Nov 2004 
 Engineer : Ajay Kumar Nema

# Sample C# :  To demonstrate netscaler api "get stat" methods
# usage : getStat <NS IP> username password.
## Output:
# > getStat.exe 10.10.10.10 nsroot nsroot
# login : Done
# stat lb vserver  vip_1 : Done
#         Name : vip_1 (10.100.0.100:80)
#         State : DOWN Total Request : 0 Total Response0)
# logout: EOF
# >
*/



using System;

namespace NSConfig
{
	/*  ClientService is created from NSConfigService class to handle the cookies */

	public class ClientService : NSStatService
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
	
	class getStat
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

			getStat obj = new getStat();
			// run the script
			obj.run_commands(server_ip,username,password);
			
		}
	
		// API to run the script.
		void run_commands(string servername,string username,string password)
		{
			
			simpleResult result;
			statlbvserverResult statlbvserverresult; 		
	
			Console.WriteLine("\nConnecting to server "+servername+" ............\n"); 
			client = new ClientService(servername);
			client.CookieContainer = new System.Net.CookieContainer();

			// Login request
			result = client.login(username,password) ;
			Console.WriteLine("login : "+result.message);  
			// Stat lb vserver. 
			statlbvserverresult = client.statlbvserver("vip_1");
			Console.WriteLine("stat lb vserver  vip_1 : "+ statlbvserverresult.message); 
			if (statlbvserverresult.rc.ToString() == "0") 
			{
				lbvserverstats  obj;
				obj = (lbvserverstats) statlbvserverresult.List[0];
				Console.WriteLine("\t Name : "+ obj.name+" ("+obj.primaryipaddress+":"+obj.primaryport+")");
				Console.WriteLine("\t State : "+ obj.state+" Total Request : "+obj.totalrequests+" Total Response"+obj.totalresponses+")");
			}
			// log out
			result = client.logout();
			Console.WriteLine("logout : " + result.message);
		}
				
	}
}
