package NSConfig;
import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;

public class rewrite  {
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

				result = client.enablensfeature((FeatureEnum)FeatureEnum.REWRITE);
				System.out.println("Enablensfeature	REWRITE : " + result.getMessage());

				result = client.addrewriteaction("rewrite_act1",(ActionrewritetypeEnum)ActionrewritetypeEnum.DELETE,"HTTP.RES.HEADER(\"Server\").VALUE(0)",null,(YesnoEnum)YesnoEnum.VALNOTSET);
				System.out.println("Addrewriteaction	rewrite_act1 : " + result.getMessage());

				result = client.addrewritepolicy("rewrite_pol1","HTTP.RES.HEADER(\"Server\").CONTAINS(\"IIS\")","rewrite_act1",null);
				System.out.println("Addrewritepolicy	rewrite_pol1 : " + result.getMessage());

				result = client.bindrewriteglobal_policy("rewrite_pol1",new UnsignedInt(1),"END",(RwglobalbindpointEnum)RwglobalbindpointEnum.VALNOTSET,false,(PolicylabelinvoketypeEnum)PolicylabelinvoketypeEnum.VALNOTSET,null);
				System.out.println("Bindrewriteglobal_policy	rewrite_pol1 : " + result.getMessage());

				result = client.logout();
				System.out.println("logout : " + result.getMessage());
	   }
	   catch (Exception ex) {
	       ex.printStackTrace();
	   }
	}

}
