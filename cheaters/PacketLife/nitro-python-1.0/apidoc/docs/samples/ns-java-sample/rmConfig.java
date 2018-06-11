/* Sample JAVA : To removes configuration that was added by setConfig.java


	 Date : 15 Dec 2004

# Output:

Note - Please use following piece of code to disable the href support in 
Axis java client.
((org.apache.axis.client.Stub)client)._setProperty
(org.apache.axis.AxisEngine.PROP_DOMULTIREFS, Boolean.FALSE);

# login: Done
# rm vserver vip_1: Done
# rm service s1: Done
# rm service s2: Done
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


public class rmConfig  {

	public static void main(String[] args) {

		String  soap_server;
		String username ;
		String password ;
		NSConfigBindingStub client ;
		SimpleResult result;
		UnsignedInt NULL_UINT=null;

		if (args.length < 3) {
			System.out.println("Usage : java rmConfig.class <NP> <username> <password>");
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

				//Login

				result = client.login("nsroot", "nsroot");
				System.out.println("Login : "+result.getMessage());

				// Remove vserver vip_1

				result = client.rmlbvserver("vip_1");
				System.out.println("rm lb vserver vip_1 : " + result.getMessage());

				// Remove service s1
				result = client.rmservice("s1");
				System.out.println("rm service s1 : " + result.getMessage());

				// Remove service s2
				result = client.rmservice("s2");
				System.out.println("rm service s2 : " + result.getMessage());

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
