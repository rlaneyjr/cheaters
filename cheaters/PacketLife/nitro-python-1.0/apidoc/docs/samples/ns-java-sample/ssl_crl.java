package NSConfig;
import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;
    
public class ssl_crl  {
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
          
				result = client.addsslcertkey("ca_cert","/nsconfig/ssl/certs/ca_cert.pem",null,false,null,(InformatsEnum)InformatsEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addsslcertkey	ca_cert : " + result.getMessage());

				result = client.addsslcertkey("root_cert","/nsconfig/ssl/certs/root_cert.pem",null,false,null,(InformatsEnum)InformatsEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addsslcertkey	root_cert : " + result.getMessage());

				result = client.addsslcrl("crl1","/var/netscaler/ssl/crl.pem",(InformatsEnum)InformatsEnum.VALNOTSET);
				System.out.println("Addsslcrl	crl1 : " + result.getMessage());

				result = client.setsslcrl_cacert("crl1","ca_cert");
				System.out.println("Setsslcrl_cacert	crl1 : " + result.getMessage());

				result = client.addsslcrl("crl1","/var/netscaler/ssl/crl.pem",(InformatsEnum)InformatsEnum.VALNOTSET);
				System.out.println("Addsslcrl	crl1 : " + result.getMessage());

				result = client.setsslcrl_refresh("crl1",(EnabledisabledEnum)EnabledisabledEnum.ENABLED);
				System.out.println("Setsslcrl_refresh	crl1 : " + result.getMessage());

				result = client.setsslcrl_cacert("crl1","ca_cert");
				System.out.println("Setsslcrl_cacert	crl1 : " + result.getMessage());

				result = client.setsslcrl_server("crl1","10.102.3.120");
				System.out.println("Setsslcrl_server	crl1 : " + result.getMessage());

				result = client.setsslcrl_method("crl1",(RefreshmethodEnum)RefreshmethodEnum.HTTP,null);
				System.out.println("Setsslcrl_method	crl1 : " + result.getMessage());

				result = client.setsslcrl_port("crl1",new UnsignedInt(80));
				System.out.println("Setsslcrl_port	crl1 : " + result.getMessage());

				result = client.setsslcrl_interval("crl1",(RefreshintervlEnum)RefreshintervlEnum.WEEKLY);
				System.out.println("Setsslcrl_interval	crl1 : " + result.getMessage());

				result = client.addsslcrl("crl1","/var/netscaler/ssl/crl.pem",(InformatsEnum)InformatsEnum.VALNOTSET);
				System.out.println("Addsslcrl	crl1 : " + result.getMessage());

				result = client.setsslcrl_refresh("crl1",(EnabledisabledEnum)EnabledisabledEnum.ENABLED);
				System.out.println("Setsslcrl_refresh	crl1 : " + result.getMessage());

				result = client.setsslcrl_cacert("crl1","ca_cert");
				System.out.println("Setsslcrl_cacert	crl1 : " + result.getMessage());

				result = client.setsslcrl_server("crl1","10.102.3.120");
				System.out.println("Setsslcrl_server	crl1 : " + result.getMessage());

				result = client.setsslcrl_method("crl1",(RefreshmethodEnum)RefreshmethodEnum.LDAP,null);
				System.out.println("Setsslcrl_method	crl1 : " + result.getMessage());

				result = client.setsslcrl_port("crl1",new UnsignedInt(389));
				System.out.println("Setsslcrl_port	crl1 : " + result.getMessage());

				result = client.setsslcrl_basedn("crl1","cn=Manager,dc=my-domain,dc=com");
				System.out.println("Setsslcrl_basedn	crl1 : " + result.getMessage());

				result = client.setsslcrl_interval("crl1",(RefreshintervlEnum)RefreshintervlEnum.WEEKLY);
				System.out.println("Setsslcrl_interval	crl1 : " + result.getMessage());

				result = client.logout();
				System.out.println("logout : " + result.getMessage());
	   }
	   catch (Exception ex) {
	       ex.printStackTrace();
	   }
	}

}
