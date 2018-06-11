/* Sample JAVA : To demonstrate NetScaler API

	 Date : 15 Dec 2004

Note - Please use following piece of code to disable the href support in 
Axis java client.
((org.apache.axis.client.Stub)client)._setProperty
(org.apache.axis.AxisEngine.PROP_DOMULTIREFS, Boolean.FALSE);

# Output:

# login: Done
# add service s1: Done
# add service s2: Done
# set service s1 : Done
# bind monitor s1: Done
# bind monitor s2: Done
# add lb vserver vip_1: Done
# bind lb vserver s1: Done
# bind lb vserbver s2: Done
# save ns config: Done
# logout: Done
# >
*/

package NSConfig;

import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;


public class setConfig  {

	public static void main(String[] args) {

		String  soap_server;
		String username;
		String password ;
		NSConfigBindingStub client ;
		SimpleResult  result;
		NSConfig.Service svr;
		UnsignedInt NULL_UINT=null;

		if (args.length < 3) {
			System.out.println("Usage : java setConfig.class http://<NP> <username> <password>");
			return;
		}
		soap_server = args[0];
		username    = args[1];
		password    = args[2];

		try {
				// Initialized the client stub
				soap_server = "http://"+soap_server+"/soap";
				System.out.println("Connecting to  "+soap_server + " ........");


				client  = new NSConfigBindingStub(new URL(soap_server),null);
				client.setMaintainSession(true);
				((org.apache.axis.client.Stub)client)._setProperty(org.apache.axis.AxisEngine.PROP_DOMULTIREFS, Boolean.FALSE);

				//Login

				result = client.login(username, password);
				System.out.println("Login : "+result.getMessage());

				// add service s1

				result = client.addservice("s1",null,"10.101.0.1",(ServicetypeEnum) ServicetypeEnum.HTTP,new UnsignedInt(80), null, (CachtypeEnum)CachtypeEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);

				System.out.println("add service s1 : " + result.getMessage());
				
				result = client.addservice("s2",null,"10.101.0.2",(ServicetypeEnum) ServicetypeEnum.HTTP,new UnsignedInt(80), null, (CachtypeEnum)CachtypeEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);

				System.out.println("add service s2 : " + result.getMessage());
				
				//set service
				result = client.setservice_maxreq("s1",new UnsignedInt(50));
				System.out.println("set service maxReq : " + result.getMessage());

				result = client.setservice_cip("s1",(EnabledisabledEnum)EnabledisabledEnum.ENABLED,"abc");
				System.out.println("set service cip : " + result.getMessage());

				// bind monitor s1

				result = client.bindlbmonitor_service("http","s1",(EnabledisabledEnum)EnabledisabledEnum.ENABLED,new UnsignedInt(10));
				System.out.println("bind monitor  s1 : "+ result.getMessage());

				// bind monitor s2

				result = client.bindlbmonitor_service("http","s2",(EnabledisabledEnum)EnabledisabledEnum.ENABLED,new UnsignedInt(10));
				System.out.println("bind monitor  s2 : "+ result.getMessage());


				// add lb vserver

				result = client.addlbvserver("vip_1", (VservicetypeEnum)VservicetypeEnum.HTTP, "10.100.0.100",new UnsignedInt(80),null,(EnabledisabledEnum)EnabledisabledEnum.ENABLED,null);
				
				System.out.println("add lb vserver vip_1 : "  + result.getMessage());

				// bind lb vserver s1

				result = client.bindlbvserver_service("vip_1","s1",new UnsignedInt(10));
				System.out.println("bind lb vserver s1 : "+ result.getMessage());

				// bind lb vserver s2

				result = client.bindlbvserver_service("vip_1","s2",new UnsignedInt(10));
				System.out.println("bind lb vserver s2 : "+ result.getMessage());

				// Save config

				result = client.savensconfig();
				System.out.println("save config : " + result.getMessage());

				// Logout

				result = client.logout();
				System.out.println("logout : " + result.getMessage());

		}
		catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}
