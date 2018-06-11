package NSConfig;
import java.io.*;
import java.util.*;
import java.net.*;
import java.beans.*;
import java.net.*;
import NSConfig.*;
import org.apache.axis.types.*;

public class cmp  {
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

				result = client.enablensfeature((FeatureEnum)FeatureEnum.CMP);
				System.out.println("Enablensfeature	CMP : " + result.getMessage());

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

				result = client.setservice_cmp("svc1",(YesnoEnum)YesnoEnum.YES);
				System.out.println("Setservice_cmp	svc1 : " + result.getMessage());

				result = client.setservice_cmp("svc2",(YesnoEnum)YesnoEnum.NO);
				System.out.println("Setservice_cmp	svc2 : " + result.getMessage());

				result = client.addcmppolicy("cmp1","url == /testsite/file5.html","nocompress");
				System.out.println("Addcmppolicy	cmp1 : " + result.getMessage());

				result = client.bindcmpglobal_policy("cmp1",null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Bindcmpglobal_policy	cmp1 : " + result.getMessage());

				result = client.addpolicyexpression("ex1","RES.HTTP.HEADER Content-Type CONTAINS application/msword");
				System.out.println("Addpolicyexpression	ex1 : " + result.getMessage());

				result = client.addcmppolicy("cmp2","ex1","deflate");
				System.out.println("Addcmppolicy	cmp2 : " + result.getMessage());

				result = client.bindcmpglobal_policy("cmp2",null,(EnabledisabledEnum)EnabledisabledEnum.VALNOTSET);
				System.out.println("Bindcmpglobal_policy	cmp2 : " + result.getMessage());

				result = client.addcmppolicy("cmp3","url contains file50 || RES.HTTP.HEADER Content-Type CONTAINS text/css","compress");
				System.out.println("Addcmppolicy	cmp3 : " + result.getMessage());

				result = client.bindlbvserver_policy("lbvip1","cmp3",null,null,(VserverbindpointEnum)VserverbindpointEnum.VALNOTSET,false,(PolicylabelinvoketypeEnum)PolicylabelinvoketypeEnum.VALNOTSET,null);
				System.out.println("Bindlbvserver_policy	lbvip1 : " + result.getMessage());

				result = client.addpolicyexpression("ex2","HEADER User-Agent CONTAINS MSIE");
				System.out.println("Addpolicyexpression	ex2 : " + result.getMessage());

				result = client.addpolicyexpression("ex3","RES.HTTP.HEADER Content-Type CONTAINS application/vnd.ms-excel");
				System.out.println("Addpolicyexpression	ex3 : " + result.getMessage());

				result = client.addcmppolicy("cmp4","ex2&&ex3","gzip");
				System.out.println("Addcmppolicy	cmp4 : " + result.getMessage());

				result = client.bindlbvserver_policy("lbvip2","cmp4",null,null,(VserverbindpointEnum)VserverbindpointEnum.VALNOTSET,false,(PolicylabelinvoketypeEnum)PolicylabelinvoketypeEnum.VALNOTSET,null);
				System.out.println("Bindlbvserver_policy	lbvip2 : " + result.getMessage());

				result = client.logout();
				System.out.println("logout : " + result.getMessage());
	   }
	   catch (Exception ex) {
	       ex.printStackTrace();
	   }
	}

}
