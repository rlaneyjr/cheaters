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
	struct ns1__addrewriteaction act;
	struct ns1__addrewriteactionResponse ract;
	struct ns1__addrewritepolicy pol;
	struct ns1__addrewritepolicyResponse rpol;

	sprintf(nsurl, "%s/soap", nshost);

	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");


	memset(&act, 0, sizeof(act));
	act.name = "rewrite_act1";
	act.type = ns1__actionrewritetypeEnum__DELETE;
	act.target = "HTTP.RES.HEADER(\"Server\").VALUE(0)";
	act.stringbuilderexpr = NULL;
	act.bypasssafetycheck = ns1__yesnoEnum__VALNOTSET;
	rc = soap_call_ns1__addrewriteaction(psoap, nsurl, NSACT,
						 act.name,
						 act.type,
						 act.target,
						 act.stringbuilderexpr,
						 act.bypasssafetycheck,
						 &ract);
	_check_result(psoap, rc, (struct _result*)ract.return_,
				  "add rewriteaction rewrite_act1");


	memset(&pol, 0, sizeof(pol));
	pol.name = "rewrite_pol1";
	pol.rule = "HTTP.RES.HEADER(\"Server\").CONTAINS(\"IIS\")";
	pol.actioN = "rewrite_act1";
	pol.undefaction = NULL;
	rc = soap_call_ns1__addrewritepolicy(psoap, nsurl, NSACT,
						 pol.name,
						 pol.rule,
						 pol.actioN,
						 pol.undefaction,
						 &rpol);
	_check_result(psoap, rc, (struct _result*)rpol.return_,
				  "add rewritepolicy rewrite_pol1");


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

