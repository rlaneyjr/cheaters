package NSConfig;
import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;

public class csw  {
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

				result = client.enablensfeature((FeatureEnum)FeatureEnum.LB);
				System.out.println("Enablensfeature	LB : " + result.getMessage());

				result = client.enablensfeature((FeatureEnum)FeatureEnum.CS);
				System.out.println("Enablensfeature	CS : " + result.getMessage());

				result = client.addserver("s1","10.102.3.91",null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addserver	s1 : " + result.getMessage());

				result = client.addserver("s2","10.102.3.92",null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addserver	s2 : " + result.getMessage());

				result = client.addserver("s3","10.102.3.93",null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addserver	s3 : " + result.getMessage());

				result = client.addservice("srv1",null,"s1",(ServicetypeEnum)ServicetypeEnum.HTTP,new UnsignedInt(80),null,(CachtypeEnum)CachtypeEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addservice	srv1 : " + result.getMessage());

				result = client.addservice("srv2",null,"s2",(ServicetypeEnum)ServicetypeEnum.HTTP,new UnsignedInt(80),null,(CachtypeEnum)CachtypeEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addservice	srv2 : " + result.getMessage());

				result = client.addservice("srv3",null,"s3",(ServicetypeEnum)ServicetypeEnum.HTTP,new UnsignedInt(80),null,(CachtypeEnum)CachtypeEnum.VALNOTSET,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Addservice	srv3 : " + result.getMessage());

				result = client.addlbvserver("lbvip1",(VservicetypeEnum)VservicetypeEnum.HTTP,null,null,null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addlbvserver	lbvip1 : " + result.getMessage());

				result = client.addlbvserver("lbvip2",(VservicetypeEnum)VservicetypeEnum.HTTP,null,null,null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addlbvserver	lbvip2 : " + result.getMessage());

				result = client.addlbvserver("lbvip3",(VservicetypeEnum)VservicetypeEnum.HTTP,null,null,null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addlbvserver	lbvip3 : " + result.getMessage());

				result = client.bindlbvserver_service("lbvip1","srv1",null);
				System.out.println("Bindlbvserver_service	lbvip1 : " + result.getMessage());

				result = client.bindlbvserver_service("lbvip2","srv2",null);
				System.out.println("Bindlbvserver_service	lbvip2 : " + result.getMessage());

				result = client.bindlbvserver_service("lbvip3","srv3",null);
				System.out.println("Bindlbvserver_service	lbvip3 : " + result.getMessage());

				result = client.addcspolicy("contains_html",null,"REQ.HTTP.URL CONTAINS html",null);
				System.out.println("Addcspolicy	contains_html : " + result.getMessage());

				result = client.addcspolicy("contains_txt",null,"REQ.HTTP.URL CONTAINS gif",null);
				System.out.println("Addcspolicy	contains_txt : " + result.getMessage());

				result = client.addcspolicy("contains_gif",null,"REQ.HTTP.URL CONTAINS asp",null);
				System.out.println("Addcspolicy	contains_gif : " + result.getMessage());

				result = client.addcsvserver("csvip",(CsvservicetypeEnum)CsvservicetypeEnum.HTTP,"10.102.3.54",null,new UnsignedInt(80),(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET,null);
				System.out.println("Addcsvserver	csvip : " + result.getMessage());

				result = client.bindcsvserver_targetvserver("csvip","lbvip1","contains_html",new UnsignedInt(5),null,(VserverbindpointEnum)VserverbindpointEnum.VALNOTSET,false,(PolicylabelinvoketypeEnum)PolicylabelinvoketypeEnum.VALNOTSET,null);
				System.out.println("Bindcsvserver_targetvserver	csvip : " + result.getMessage());

				result = client.bindcsvserver_targetvserver("csvip","lbvip2","contains_txt",new UnsignedInt(5),null,(VserverbindpointEnum)VserverbindpointEnum.VALNOTSET,false,(PolicylabelinvoketypeEnum)PolicylabelinvoketypeEnum.VALNOTSET,null);
				System.out.println("Bindcsvserver_targetvserver	csvip : " + result.getMessage());

				result = client.bindcsvserver_targetvserver("csvip","lbvip3","contains_gif",new UnsignedInt(5),null,(VserverbindpointEnum)VserverbindpointEnum.VALNOTSET,false,(PolicylabelinvoketypeEnum)PolicylabelinvoketypeEnum.VALNOTSET,null);
				System.out.println("Bindcsvserver_targetvserver	csvip : " + result.getMessage());

				result = client.logout();
				System.out.println("logout : " + result.getMessage());
	   }
	   catch (Exception ex) {
	       ex.printStackTrace();
	   }
	}

}
