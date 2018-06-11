package NSConfig;
import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;

public class acl  {
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

				result = client.addnsacl("allow_sip",(ExtaclactionEnum)ExtaclactionEnum.ALLOW,null,(ExtaclprotoenumEnum)ExtaclprotoenumEnum.VALNOTSET,false,null,null);
				System.out.println("Addnsacl	allow_sip : " + result.getMessage());

				result = client.setnsacl_srcip("allow_sip",true,(XacloperatorEnum)XacloperatorEnum.VALNOTSET,"10.102.3.84");
				System.out.println("Setnsacl_srcip	allow_sip : " + result.getMessage());

				result = client.addnsacl("allow_sip_range",(ExtaclactionEnum)ExtaclactionEnum.ALLOW,null,(ExtaclprotoenumEnum)ExtaclprotoenumEnum.VALNOTSET,false,null,null);
				System.out.println("Addnsacl	allow_sip_range : " + result.getMessage());

				result = client.setnsacl_srcip("allow_sip_range",true,(XacloperatorEnum)XacloperatorEnum.VALNOTSET,"10.102.3.1-10.102.3.255");
				System.out.println("Setnsacl_srcip	allow_sip_range : " + result.getMessage());

				result = client.addnsacl("Deny_sipr",(ExtaclactionEnum)ExtaclactionEnum.DENY,null,(ExtaclprotoenumEnum)ExtaclprotoenumEnum.VALNOTSET,false,null,null);
				System.out.println("Addnsacl	Deny_sipr : " + result.getMessage());

				result = client.setnsacl_srcip("Deny_sipr",true,(XacloperatorEnum)XacloperatorEnum.VALNOTSET,"10.10.0.1-10.102.7.152");
				System.out.println("Setnsacl_srcip	Deny_sipr : " + result.getMessage());

				result = client.addnsacl("allow_dip",(ExtaclactionEnum)ExtaclactionEnum.ALLOW,null,(ExtaclprotoenumEnum)ExtaclprotoenumEnum.VALNOTSET,false,null,null);
				System.out.println("Addnsacl	allow_dip : " + result.getMessage());

				result = client.setnsacl_destip("allow_dip",true,(XacloperatorEnum)XacloperatorEnum.VALNOTSET,"192.168.17.11");
				System.out.println("Setnsacl_destip	allow_dip : " + result.getMessage());

				result = client.addnsacl("allow_dip_rng",(ExtaclactionEnum)ExtaclactionEnum.ALLOW,null,(ExtaclprotoenumEnum)ExtaclprotoenumEnum.VALNOTSET,false,null,null);
				System.out.println("Addnsacl	allow_dip_rng : " + result.getMessage());

				result = client.setnsacl_destip("allow_dip_rng",true,(XacloperatorEnum)XacloperatorEnum.VALNOTSET,"192.168.17.1-192.168.17.250");
				System.out.println("Setnsacl_destip	allow_dip_rng : " + result.getMessage());

				result = client.addnsacl("deny_src_mac",(ExtaclactionEnum)ExtaclactionEnum.DENY,null,(ExtaclprotoenumEnum)ExtaclprotoenumEnum.VALNOTSET,false,null,null);
				System.out.println("Addnsacl	deny_src_mac : " + result.getMessage());

				result = client.setnsacl_srcmac("deny_src_mac","00:0d:9d:54:64:6a");
				System.out.println("Setnsacl_srcmac	deny_src_mac : " + result.getMessage());

				result = client.addnsacl("acl_user_priority",(ExtaclactionEnum)ExtaclactionEnum.ALLOW,null,(ExtaclprotoenumEnum)ExtaclprotoenumEnum.VALNOTSET,false,null,null);
				System.out.println("Addnsacl	acl_user_priority : " + result.getMessage());

				result = client.setnsacl_priority("acl_user_priority",new UnsignedInt(1));
				System.out.println("Setnsacl_priority	acl_user_priority : " + result.getMessage());

				result = client.disablensacl("allow_sip");
				System.out.println("Disablensacl	Deny_sample : " + result.getMessage());

				result = client.rmnsacl("allow_sip");
				System.out.println("Rmnsacl	Deny_sip_dip_dport : " + result.getMessage());

				result = client.clearnsacls();
				System.out.println("Clearnsacls	Deny_sip_dip_dport : " + result.getMessage());

				result = client.logout();
				System.out.println("logout : " + result.getMessage());
	   }
	   catch (Exception ex) {
	       ex.printStackTrace();
	   }
	}

}
