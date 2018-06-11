/* Sample JAVA :  program to demonstrate NetScaler API

	 Date : 15 Dec 2004

# Sample JAVA :  To demonstrate NetScaler API "get" methods

Note - Please use following piece of code to disable the href support in 
Axis java client.
((org.apache.axis.client.Stub)client)._setProperty
(org.apache.axis.AxisEngine.PROP_DOMULTIREFS, Boolean.FALSE);

# Output:

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


package NSConfig;

import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;


public class getConfig  {

	public static void main(String[] args) {

		String  soap_server;
		String username;
		String password;
		NSConfigBindingStub client ;
		SimpleResult result;
		GetlbvserverResult getlbvserverresult;
		GetserviceResult getserviceresult;
		UnsignedInt NULL_UINT=null;

		if (args.length < 3) {
			System.out.println("Usage : java getConfig.class http://<NP> <username> <password>");
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

				result = client.login(username,password);
				System.out.println("login : "+result.getMessage());

				// Get lb vserver

				getlbvserverresult = client.getlbvserver("");
				System.out.println("getlbvserver : "+ getlbvserverresult.getMessage());
				for(int i =0 ; i < getlbvserverresult.getList().length;i++)
				{
						Lbvserver  obj;
						obj = (Lbvserver)getlbvserverresult.getList()[i];
						System.out.println("\t"+obj.getName()+" :\t"+obj.getIpaddress()+":"+obj.getPort() + "\t" + obj.getState());
				}

				getlbvserverresult = client.getlbvserver("vip_1");
				System.out.println("getlbvserver vip_1: "+ getlbvserverresult.getMessage());
				System.out.println("Services bound to vip_1:");
				Lbvserver  obj;
				obj = (Lbvserver)getlbvserverresult.getList()[0];
				for(int i =0 ; i < obj.getServicename().length;i++)
				{
					// Get the bind service details
					getserviceresult = client.getservice(obj.getServicename()[i],true,false);
					Service  objsvc;
					objsvc = (Service)getserviceresult.getList()[0];
					System.out.println("\t"+objsvc.getName()+" :\t"+objsvc.getIpaddress()+":"+objsvc.getPort() + "\t" + objsvc.getSvrstate());
				}

				// Get invalid  lb vserver

				getlbvserverresult = client.getlbvserver("nonesuch");
				System.out.println("getlbvserver (nonesuch) : "+ getlbvserverresult.getMessage());

				// Logout

				result = client.logout();
				System.out.println("logout : " + result.getMessage());

		}
		catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}
