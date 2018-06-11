/* Sample C script to demonstrate Netscaler API
 * Command-line parameters (all optional):  <NS IP> <username> <password>
 */

/* $ ./setConfig 10.102.4.107
 * login: Done
 * add service s1: Done
 * add service s2: Done
 * set service s1: Done
 * bind monitor to s1: Done
 * bind monitor to s2: Done
 * add lb vserver vip_1: Done
 * bind s1 to vip_1: Done
 * bind s2 to vip_1: Done
 * save config: Done
 * log out: EOF
 * $
 */

#include <stdio.h>

#include "soapH.h"
#include "soapStub.h"
#include "NSConfigBinding.nsmap"

#define URLBUF	256
#define NSACT	"urn:NSConfigAction"

struct _result {
	unsigned int rc;			/* api return code */
	char *message;
};
static void _check_result(struct soap*, int, struct _result *, char* tag);


int main(int argc, char* argv[])
{
	char* nshost = (argc>=2 ? argv[1]:"localhost");
	char* uname = (argc>=3 ? argv[2]:"nsroot");
	char* passwd = (argc>=4 ? argv[3]:"nsroot");
	char nsurl[URLBUF];
	int	rc;				/* soap return code */

	struct soap* psoap;
	struct ns1__loginResponse rlogin;
	struct ns1__addservice svc;
	struct ns1__addlbvserver vs;
	struct ns1__addlbvserverResponse rvs;
	struct ns1__bindlbmonitor_USCOREservice bindmon;
	struct ns1__bindlbmonitor_USCOREserviceResponse rbindmon;
	struct ns1__addserviceResponse rsvc;
	struct ns1__logoutResponse rlogout;
	struct ns1__bindlbvserver_USCOREservice bindvsr;
	struct ns1__bindlbvserver_USCOREserviceResponse rbindvsr;

	sprintf(nsurl, "%s/soap", nshost);


	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");

	/* add service s1 */
	memset(&svc, 0, sizeof(svc));
	svc.name = "s1";
	svc.ip = "10.1.1.11";
	svc.servicetype = ns1__servicetypeEnum__HTTP;
	svc.port = 80;
	svc.cleartextport = -1;

	rc = soap_call_ns1__addservice(psoap, nsurl, NSACT,
				   svc.name, svc.servername, svc.ip,
				   svc.servicetype, svc.port,
				   svc.cleartextport,
				   svc.cachetype,
				   svc.state,
				   &rsvc);
	_check_result(psoap, rc, (struct _result*)rsvc.return_,
		  "add service s1");

	/* add service s2 */

	memset(&svc, 0, sizeof(svc));
	svc.name = "s2";
	svc.ip = "10.1.1.12";
	svc.servicetype = ns1__servicetypeEnum__HTTP;
	svc.port = 80;
	svc.cleartextport = -1;

	rc = soap_call_ns1__addservice(psoap, nsurl, NSACT,
				   svc.name, svc.servername, svc.ip,
				   svc.servicetype, svc.port,
				   svc.cleartextport,
				   svc.cachetype,
				   svc.state,
				   &rsvc);
	_check_result(psoap, rc, (struct _result*)rsvc.return_,
		  "add service s2");

	/* bind monitor s1 */
	memset(&bindmon, 0, sizeof(bindmon));
	bindmon.monitorname = "http";
	bindmon.servicename = "s1";
	bindmon.state = ns1__enabledisabledEnum__ENABLED;
	bindmon.weight = 10;
	rc = soap_call_ns1__bindlbmonitor_USCOREservice(psoap, nsurl, NSACT,
						  bindmon.monitorname,
						  bindmon.servicename,
						  bindmon.state,
						  bindmon.weight,
						  &rbindmon);
	_check_result(psoap, rc, (struct _result*)rbindmon.return_,
		  "bind monitor s1");


	/* bind monitor s2 */
	memset(&bindmon, 0, sizeof(bindmon));
	bindmon.monitorname = "http";
	bindmon.servicename = "s2";
	bindmon.state = ns1__enabledisabledEnum__ENABLED;
	bindmon.weight = 10;
	rc = soap_call_ns1__bindlbmonitor_USCOREservice(psoap, nsurl, NSACT,
						  bindmon.monitorname,
						  bindmon.servicename,
						  bindmon.state,
						  bindmon.weight,
						  &rbindmon);
	_check_result(psoap, rc, (struct _result*)rbindmon.return_,
		  "bind monitor s1");

	/* add lb vserver */
	memset(&vs, 0, sizeof(vs));
	vs.name = "vip_1";
	vs.ipaddress = "10.1.1.100";
	vs.servicetype = ns1__servicetypeEnum__HTTP;
	vs.port = 80;
	vs.range = 1;
	vs.state = ns1__enabledisabledEnum__ENABLED;

	rc = soap_call_ns1__addlbvserver(psoap, nsurl, NSACT,
					 vs.name,
					 vs.servicetype,
					 vs.ipaddress,
					 vs.port,
					 vs.range,
					 vs.state,
					 vs.vipheader,
					 &rvs);
	_check_result(psoap, rc, (struct _result*)rvs.return_,
		  "add lb vserver vip_1");

	/* bind lb vserver */
	memset(&bindvsr, 0, sizeof(bindvsr));
	bindvsr.name = "vip_1";
	bindvsr.servicename = "s1";
	bindvsr.weight = 10;

	rc = soap_call_ns1__bindlbvserver_USCOREservice(psoap, nsurl, NSACT,
							bindvsr.name,
							bindvsr.servicename,
							bindvsr.weight,
							&rbindvsr);
	_check_result(psoap, rc, (struct _result*)rbindvsr.return_,
		  "bind lb vserver s1");

	/* bind lb vserver */
	memset(&bindvsr, 0, sizeof(bindvsr));
	bindvsr.name = "vip_1";
	bindvsr.servicename = "s2";
	bindvsr.weight = 10;

	rc = soap_call_ns1__bindlbvserver_USCOREservice(psoap, nsurl, NSACT,
							bindvsr.name,
							bindvsr.servicename,
							bindvsr.weight,
							&rbindvsr);
	_check_result(psoap, rc, (struct _result*)rbindvsr.return_,
		  "bind lb vserver s2");

	/* log out */
	rc = soap_call_ns1__logout(psoap, nsurl, NSACT,
				   &rlogout);
	_check_result(psoap, rc, (struct _result*)rlogout.return_,
		  "log out");

	return 0;
}


static void _check_result(struct soap* psoap, int rc, struct _result* pres,
			  char* tag)
{
	if (rc != 0) {
	soap_print_fault(psoap, stderr);
	exit(1);
		}
	if (pres->rc == 0) {
	printf("%s: %s\n", tag, pres->message);
		} else {
	fprintf(stderr, "%s: %s\n", tag, pres->message);
	exit(1);
		}
}
