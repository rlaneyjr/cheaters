package NSConfig;
import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;
    
public class rba  {
	public static void main(String[] args) {
	   String  soap_server;
	   String username;
	   String password ;
    
	   NSConfigBindingStub client ;
	   SimpleResult  result;
	   UnsignedInt NULL_UINT=null;
	   if (args.length < 3) {
	      System.out.println("Usage : java setConfig.class <NP> <username> <password>");
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
          
				result = client.addsystemuser("user1","passwd1");
				System.out.println("Addsystemuser	user1 : " + result.getMessage());

				result = client.addsystemuser("user2","passwd2");
				System.out.println("Addsystemuser	user2 : " + result.getMessage());

				result = client.bindsystemuser_policy("user1","read-only",new UnsignedInt(1));
				System.out.println("Bindsystemuser_policy	user1 : " + result.getMessage());

				result = client.bindsystemuser_policy("user1","operator",new UnsignedInt(2));
				System.out.println("Bindsystemuser_policy	user1 : " + result.getMessage());

				result = client.addsystemgroup("group1");
				System.out.println("Addsystemgroup	group1 : " + result.getMessage());

				result = client.bindsystemgroup_user("group1","user2");
				System.out.println("Bindsystemgroup_user	group1 : " + result.getMessage());

				result = client.bindsystemgroup_policy("group1","read-only",new UnsignedInt(1));
				System.out.println("Bindsystemgroup_policy	group1 : " + result.getMessage());

				result = client.addsystemcmdpolicy("add_pol1",(AllowdenyEnum)AllowdenyEnum.ALLOW,"^add.*");
				System.out.println("Addsystemcmdpolicy	add_pol1 : " + result.getMessage());

				result = client.bindsystemuser_policy("user1","add_pol1",new UnsignedInt(3));
				System.out.println("Bindsystemuser_policy	user1 : " + result.getMessage());

				GetsystemuserResult  Getsystemuserresult1 = client.getsystemuser(null);
				System.out.println("Getsystemuser	null : " + Getsystemuserresult1.getMessage());

				if ( (Getsystemuserresult1.getList() != null) && (Getsystemuserresult1.getList().length > 0)) {
					for(int i =0 ; i < Getsystemuserresult1.getList().length;i++) { 
						Systemuser obj;
						obj = (Systemuser) Getsystemuserresult1.getList()[i];
						System.out.println("\tusername\t\t =  "+obj.getUsername()+"\n"+"\tgroupname\t\t =  "+obj.getGroupname()+"\n"+"\tpolicyname\t\t =  "+obj.getPolicyname()+"\n"+"\tpriority\t\t =  "+obj.getPriority()+"\n");
					}
				}

				GetsystemgroupResult  Getsystemgroupresult2 = client.getsystemgroup(null);
				System.out.println("Getsystemgroup	null : " + Getsystemgroupresult2.getMessage());

				if ( (Getsystemgroupresult2.getList() != null) && (Getsystemgroupresult2.getList().length > 0)) {
					for(int i =0 ; i < Getsystemgroupresult2.getList().length;i++) { 
						Systemgroup obj;
						obj = (Systemgroup) Getsystemgroupresult2.getList()[i];
						System.out.println("\tgroupname\t\t =  "+obj.getGroupname()+"\n"+"\tusername\t\t =  "+obj.getUsername()+"\n"+"\tpolicyname\t\t =  "+obj.getPolicyname()+"\n"+"\tpriority\t\t =  "+obj.getPriority()+"\n");
					}
				}

				result = client.logout();
				System.out.println("logout : " + result.getMessage());
	   }
	   catch (Exception ex) {
	       ex.printStackTrace();
	   }
	}

}
