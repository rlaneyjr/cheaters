package NSConfig;
import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;
    
public class ssl  {
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
          
				result = client.addserver("s1","10.102.3.84",null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addserver	s1 : " + result.getMessage());

				result = client.addserver("s2","10.102.3.83",null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addserver	s2 : " + result.getMessage());

				result = client.addservice("src1",null,"s1",(ServicetypeEnum)ServicetypeEnum.HTTP,new UnsignedInt(80),null,(CachtypeEnum)CachtypeEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addservice	src1 : " + result.getMessage());

				result = client.addservice("src2",null,"s2",(ServicetypeEnum)ServicetypeEnum.HTTP,new UnsignedInt(80),null,(CachtypeEnum)CachtypeEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addservice	src2 : " + result.getMessage());

				result = client.addlbvserver("sslbase",(VservicetypeEnum)VservicetypeEnum.SSL,"10.102.3.100",new UnsignedInt(443),null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addlbvserver	sslbase : " + result.getMessage());

				result = client.bindlbvserver_service("sslbase","src1",null);
				System.out.println("Bindlbvserver_service	sslbase : " + result.getMessage());

				result = client.bindlbvserver_service("sslbase","src2",null);
				System.out.println("Bindlbvserver_service	sslbase : " + result.getMessage());

				result = client.addsslcertkey("server_cert","/nsconfig/ssl/certs/cert1.pem","/nsconfig/ssl/certs/cert1ky.pem",false,null,(InformatsEnum)InformatsEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addsslcertkey	server_cert : " + result.getMessage());

				result = client.bindsslcertkey_vserver("server_cert","sslbase",false);
				System.out.println("Bindsslcertkey_vserver	server_cert : " + result.getMessage());

				result = client.logout();
				System.out.println("logout : " + result.getMessage());
	   }
	   catch (Exception ex) {
	       ex.printStackTrace();
	   }
	}

}
