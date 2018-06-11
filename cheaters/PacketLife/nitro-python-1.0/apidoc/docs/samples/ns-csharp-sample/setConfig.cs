/* Sample c# program to demonstrate netscaler api
 
	 Date : 01 Nov 2004 
 Engineer : Ajay Kumar Nema

# Sample C# : To demonstrate NetScaler api

# usage : > setConfig.exe <NS IP> username password
 
# Output:

# login: Done
# add service s1: Done
# add service s2: Done
# set service s1 : Done
# bind monitor s1: Done
# bind monitor s2: Done
# add lb vserver vip_1: Done
# bind lb vserver s1: Done
# bind lb vserver s2: Done
# save ns config: Done
# logout: Done
# >
*/

using System;
using System.Runtime.Remoting;
using System.Xml.Serialization;
using System.Web.Services;

//using Samples.Runtime.Remoting.Configuration.Network;




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
	
	class setConfig
	{
		
		ClientService client=null;
		// The main entry point for the application.
		[STAThread]
		static void Main(string[] args)
		{
			//
			// TODO: Add code to start application here
			//
			if ( args.Length < 3)
			{
				// usage
				Console.WriteLine("Usage: setConfig <NS IP> username password");
				return;
			} 
			string server_ip = args[0];
			string username = args[1];
			string password = args[2];

			setConfig obj = new setConfig();
			// run the script
			obj.run_commands(server_ip,username,password);
			
		}
	
		// API to run the script.
		void run_commands(string servername,string username,string password)
		{
			
			simpleResult result;
			service	 svc = new service();
	
			// Initialized the soap client
			Console.WriteLine("\nConnecting to server "+servername+" ............\n"); 
			client = new ClientService(servername);
			client.CookieContainer = new System.Net.CookieContainer();
			// Login request
			result = client.login(username,password) ;

			Console.WriteLine("login : "+result.message);  
			if (result.rc.ToString() == "0")
			{
				//add service s1
				result = client.addservice("s1","10.101.0.1",null,servicetypeEnum.HTTP,80, 0xFFFFFFFF, cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);
				Console.WriteLine("add service s1 : " + result.message);  

				// add service s2
				result = client.addservice("s2","10.101.0.2",null,servicetypeEnum.HTTP,80, 0xFFFFFFFF, cachtypeEnum.VALNOTSET,enabledisabledEnum.VALNOTSET);

				Console.WriteLine("add service s2 : " + result.message);  
				
				// Modify service s1
				result = client.setservice_maxreq("s1",50);
				Console.WriteLine("set service maxReq : " + result.message);

				result = client.setservice_cip("s1",enabledisabledEnum.ENABLED,"abc");
				Console.WriteLine("set service cip : " + result.message);

				// bind monitor s1
				result = client.bindlbmonitor_service("http","s1",enabledisabledEnum.ENABLED,80); 
				Console.WriteLine("bind monitor s1 : "+ result.message);  
			
				
				// bind monitor s2
				result = client.bindlbmonitor_service("http","s2",enabledisabledEnum.ENABLED,80); 
				Console.WriteLine("bind monitor s1 : "+ result.message);  
			
				
				// add lb vserver
				result = client.addlbvserver("vip_1", vservicetypeEnum.HTTP, "10.100.0.100",80,0xFFFFFFFF,enabledisabledEnum.ENABLED,null);
				Console.WriteLine("add lb vserver newv1 : " + result.message);

				Console.WriteLine("add lb vserver vip_1 : " + result.message);
				
				// bind lb vserver s1
						
				result = client.bindlbvserver_service("vip_1","s1",10);
				Console.WriteLine("bind lb vserver s1 : "+ result.message);  

				// bind lb vserver s2

				result = client.bindlbvserver_service("vip_1","s2",10);
				Console.WriteLine("bind lb vserver s2 : "+ result.message);  

								
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
