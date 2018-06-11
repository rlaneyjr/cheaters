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

	

	class rewrite 

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

       

				result = client.enablensfeature(featureEnum.REWRITE);

				Console.WriteLine("enablensfeature	REWRITE : " + result.message);



				result = client.addrewriteaction("rewrite_act1",actionrewritetypeEnum.DELETE,"HTTP.RES.HEADER(\"Server\").VALUE(0)",null,yesnoEnum.VALNOTSET);

				Console.WriteLine("addrewriteaction	rewrite_act1 : " + result.message);



				result = client.addrewritepolicy("rewrite_pol1","HTTP.RES.HEADER(\"Server\").CONTAINS(\"IIS\")","rewrite_act1",null);

				Console.WriteLine("addrewritepolicy	rewrite_pol1 : " + result.message);



				result = client.bindrewriteglobal_policy("rewrite_pol1",1,"END",rwglobalbindpointEnum.VALNOTSET,false,policylabelinvoketypeEnum.VALNOTSET,null);

				Console.WriteLine("bindrewriteglobal_policy	rewrite_pol1 : " + result.message);



				result = client.logout();

				Console.WriteLine("logout : " + result.message); 

			}

			catch (Exception ex) {

			      Console.WriteLine( "Exception: "+ex.ToString());

			}

		}



	}

	}

