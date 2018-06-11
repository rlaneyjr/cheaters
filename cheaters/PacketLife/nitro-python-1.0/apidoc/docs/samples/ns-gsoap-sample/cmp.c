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
	struct ns1__addcmppolicy cmppol;
	struct ns1__addcmppolicyResponse rcmppol;
	struct ns1__bindcmpglobal_USCOREpolicy bindcmp;
	struct ns1__bindcmpglobal_USCOREpolicyResponse rbindcmp;
	struct ns1__addpolicyexpression polexp;
	struct ns1__addpolicyexpressionResponse rpolexp;

	sprintf(nsurl, "%s/soap", nshost);

	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");


	/* add cmp pol cmp1*/
	memset(&cmppol, 0, sizeof(cmppol));
	cmppol.name = "cmp1";
	cmppol.rule = "url == /testsite/file5.html";
	cmppol.resaction = "nocompress";

	rc = soap_call_ns1__addcmppolicy(psoap, nsurl, NSACT,
						 cmppol.name,
						 cmppol.rule,
						 cmppol.resaction,
						 &rcmppol);
	_check_result(psoap, rc, (struct _result*)rcmppol.return_,
				  "add cmppol cmp1");


	memset(&bindcmp, 0, sizeof(bindcmp));
	bindcmp.policyname = "cmp1";
	bindcmp.priority = -1;
	bindcmp.state = ns1__enabledisabledEnum__VALNOTSET;

	rc = soap_call_ns1__bindcmpglobal_USCOREpolicy(psoap, nsurl, NSACT,
						bindcmp.policyname,
						bindcmp.priority,
						bindcmp.state,
						&rbindcmp);
	_check_result(psoap, rc, (struct _result*)rbindcmp.return_,
				  "bind cmpglobal_policy cmp1");


	memset(&polexp, 0, sizeof(polexp));
	polexp.name = "ex1";
	polexp.value = "RES.HTTP.HEADER Content-Type CONTAINS application/msword";
	rc = soap_call_ns1__addpolicyexpression(psoap, nsurl, NSACT,
						polexp.name,
						polexp.value,
						&rpolexp);
	_check_result(psoap, rc, (struct _result*)rpolexp.return_,
				  "addpolicyexp ex1");

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
