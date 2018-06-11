#include <stdio.h>

#include "soapH.h"
#include "soapStub.h"
#include "NSConfigBinding.nsmap"

#define URLBUF	256
#define NSACT	"urn:NSConfigAction"
#define FALSE 0

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
	struct ns1__logoutResponse rlogout;
	struct ns1__addlbvserver vs;
	struct ns1__addlbvserverResponse rvs;
	struct ns1__addcspolicy cspol;
	struct ns1__addcspolicyResponse rcspol;
	struct ns1__addcsvserver cs;
	struct ns1__addcsvserverResponse rcs;
	struct ns1__bindcsvserver_USCOREtargetvserver bindvs;
	struct ns1__bindcsvserver_USCOREtargetvserverResponse  rbindvs;

	sprintf(nsurl, "%s/soap", nshost);

	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");


	/* add lb vserver */
	memset(&vs, 0, sizeof(vs));
	vs.name = "lbvip1";
	vs.servicetype = ns1__servicetypeEnum__HTTP;
	vs.ipaddress = NULL;
	vs.port = -1;
	vs.range = -1;
	vs.state = ns1__enabledisabledEnum__VALNOTSET;
	vs.vipheader = NULL;

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
				  "add lb vserver lbvip1");

		/*addcspolicy */
	memset(&cspol, 0, sizeof(cspol));
	cspol.policyname = "contains_html";
	cspol.url = NULL;
	cspol.rule = "REQ.HTTP.URL CONTAINS html";
	cspol.domain = NULL;

	rc = soap_call_ns1__addcspolicy(psoap, nsurl, NSACT,
					cspol.policyname, cspol.url, cspol.rule, cspol.domain,
					&rcspol);
	_check_result(psoap, rc, (struct _result*)rcspol.return_,
				  "add cs policy contains_html");


	/* add cs vserver */
	memset(&cs, 0, sizeof(cs));
	cs.name = "csvip";
	cs.servicetype = ns1__servicetypeEnum__HTTP;
	cs.ipaddress = "1.1.2.1";
	cs.port = 80;
	cs.range = -1;
	cs.state = ns1__enabledisabledEnum__VALNOTSET;
	cs.vipheader = NULL;

	rc = soap_call_ns1__addcsvserver(psoap, nsurl, NSACT,
					 cs.name,
					 cs.servicetype,
					 cs.ipaddress,
					 cs.range,
					 cs.port,
					 cs.state,
					 cs.vipheader,
					 &rcs);
	_check_result(psoap, rc, (struct _result*)rcs.return_,
				  "add cs vserver csvip");


	memset(&bindvs, 0, sizeof(bindvs));
	bindvs.name = "csvip";
	bindvs.targetvserver = "lbvip1";
	bindvs.policyname = "contains_html";
	bindvs.priority = 5;
	bindvs.gotopriorityexpression = NULL;
	bindvs.type = ns1__vserverbindpointEnum__VALNOTSET;
	bindvs.invoke = FALSE;
	bindvs.labeltype = ns1__policylabelinvoketypeEnum__VALNOTSET;
	bindvs.labelname = NULL;

	rc = soap_call_ns1__bindcsvserver_USCOREtargetvserver(psoap, nsurl, NSACT,
						  bindvs.name,
						  bindvs.targetvserver,
						  bindvs.policyname,
						  bindvs.priority,
						  bindvs.gotopriorityexpression,
						  bindvs.type,
						  bindvs.invoke,
						  bindvs.labeltype,
						  bindvs.labelname,
						  &rbindvs);
	_check_result(psoap, rc, (struct _result*)rbindvs.return_,
		  "bind csvserver_targetvserver csvip");

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
