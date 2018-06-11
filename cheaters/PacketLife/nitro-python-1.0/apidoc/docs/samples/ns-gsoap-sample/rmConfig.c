/* Sample C script to demonstrate Netscaler API
 * Command-line parameters (all optional):  <NS IP> <username> <password>
 */

/*
 * $ ./rmConfig.pl 10.102.4.107
 * login: Done
 * rm vserver vip_1: Done
 * rm service s1: Done
 * rm service s2: Done
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
	int i;

	struct soap* psoap;
	struct ns1__loginResponse rlogin;
	struct ns1__logoutResponse rlogout;
	struct ns1__rmserviceResponse rsvc;
	struct ns1__rmlbvserverResponse rvserver;

	sprintf(nsurl, "%s/soap", nshost);


	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");

	/* remove vserver */
	rc = soap_call_ns1__rmlbvserver(psoap, nsurl, NSACT, "vip_1", &rvserver);
	_check_result(psoap, rc, (struct _result*)rvserver.return_,
		  "rm vserver vip_1");

	/* remove services */
	rc = soap_call_ns1__rmservice(psoap, nsurl, NSACT,
				  "s1",
				  &rsvc);
	_check_result(psoap, rc, (struct _result*)rsvc.return_,
		  "rm service s1");
	rc = soap_call_ns1__rmservice(psoap, nsurl, NSACT,
				  "s2",
				  &rsvc);
	_check_result(psoap, rc, (struct _result*)rsvc.return_,
		  "rm service s2");

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
