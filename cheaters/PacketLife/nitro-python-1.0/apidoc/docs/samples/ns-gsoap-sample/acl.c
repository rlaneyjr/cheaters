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
	struct ns1__addnsacl acl;
	struct ns1__addnsaclResponse racl;

	sprintf(nsurl, "%s/soap", nshost);

	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");


	/* add ns acl allow_sip ALLOW */
	memset(&acl, 0, sizeof(acl));
	acl.aclname = "allow_sip";
	acl.aclaction = ns1__extaclactionEnum__ALLOW;
	acl.ttl = -1,
	acl.protocol = ns1__extaclprotoenumEnum__VALNOTSET;
	acl.established = FALSE;
	acl.icmptype = -1;
	acl.icmpcode = -1;

	rc = soap_call_ns1__addnsacl(psoap, nsurl, NSACT,
				   acl.aclname,acl.aclaction, acl.ttl,
				   acl.protocol, acl.established,
				   acl.icmptype, acl.icmpcode,
				   &racl);
	_check_result(psoap, rc, (struct _result*)racl.return_,
				  "add ns acl allow_sip");

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
