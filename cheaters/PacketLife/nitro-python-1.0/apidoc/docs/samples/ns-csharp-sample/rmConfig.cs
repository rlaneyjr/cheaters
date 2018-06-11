/* Sample c# program to demonstrate netscaler api
 
	 Date : 01 Nov 2004 
 Engineer : Ajay Kumar Nema

 Output:

# Sample C# : To removes configuration that was added by set.exe

# usage :  rmConfig <NS IP> username password.

# Output:

# login: Done
# rm vserver vip_1: Done
# rm service s1: Done
# rm service s2: Done
# save ns config: Done
# logout: Done
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
	
	class rmConfig
	{
		
		ClientService client=null;
		// The main entry point for the application.
		[STAThread]
		static void Main(string[] args)
		{
			if ( args.Length < 3)
			{
				// usage
				Console.WriteLine("Usage: rmConfig <NS IP> username password");
				return;
			} 
			string server_ip = args[0];
			string username = args[1];
			string password = args[2];

			rmConfig obj = new rmConfig();
			// run the script
			obj.run_commands(server_ip,username,password);
			
		}
	
		// API to run the script.
		void run_commands(string servername,string username,string password)
		{
			
			simpleResult result;
			

			// Initialized the soap client
			Console.WriteLine("\nConnecting to server "+servername+" ............\n"); 
			client = new ClientService(servername);
			client.CookieContainer = new System.Net.CookieContainer();
			// Login request
			result = client.login(username,password) ;
			Console.WriteLine("login : "+result.message);  
			if (result.rc.ToString() == "0")
			{
				// Remove vserver

				result = client.rmlbvserver("vip_1");
				Console.WriteLine("rm lb vserver vip_1 : " + result.message);
				
				// Remove service s1

				result = client.rmservice("s1");
				Console.WriteLine("rm service s1 : " + result.message);

				// Remove service s2

				result = client.rmservice("s2");
				Console.WriteLine("rm service s2 : " + result.message);
			
				// Save config

				result = client.savensconfig();
				Console.WriteLine("save config : " + result.message);

				// Logout
				result = client.logout();
				Console.WriteLine("logout : " + result.message);
				
			}
		}
				
	}
}
