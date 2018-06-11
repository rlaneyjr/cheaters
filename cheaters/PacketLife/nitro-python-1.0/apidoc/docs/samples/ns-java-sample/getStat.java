/* Sample JAVA :  program to demonstrate NetScaler API

	 Date : 15 Dec 2004

# Sample JAVA :  To demonstrate NetScaler API "Stat" methods

Note - Please use following piece of code to disable the href support in 
Axis java client.
((org.apache.axis.client.Stub)client)._setProperty
(org.apache.axis.AxisEngine.PROP_DOMULTIREFS, Boolean.FALSE);

# Output:
# login : Done
# stat lb vserver  vip_1 : Done
#         Name : vip_1 (10.100.0.100:80)
#         State : DOWN Total Request : 0 Total Response0)
# logout: EOF


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


public class getStat  {

	public static void main(String[] args) {

		String  soap_server;
		String username;
		String password;
		NSStatBindingStub client ;
		SimpleResult result;
		
		
		if (args.length < 3) {
			System.out.println("Usage : java getStat.class <NP> <username> <password>");
			return;
		}
		soap_server = args[0];
		username    = args[1];
		password    = args[2];

		try {
				// Initialized the client stub
				soap_server = "http://"+soap_server+"/soap";
				System.out.println("Connecting to  "+soap_server + " ........");

				client  = new NSStatBindingStub(new URL(soap_server),null);
				client.setMaintainSession(true);

				//Login

				result = client.login(username,password);
				System.out.println("login : "+result.getMessage());
				
				StatlbvserverResult statlbvserverresult = client.statlbvserver("vip_1");
				System.out.println("\n\nstat lb vserver : " + statlbvserverresult.getMessage());
				for (int i=0; i < statlbvserverresult.getList().length; i++) 
				{
					Lbvserverstats obj = statlbvserverresult.getList()[i];
					System.out.println("Name : "+obj.getName()+"("+obj.getPrimaryipaddress()+":"+obj.getPrimaryport()+")");
					System.out.println("State : "+obj.getState()+". Total Request : "+obj.getTotalrequests());
				}
				// Logout
				result = client.logout();
				System.out.println("logout : " + result.getMessage());

		}
		catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}
