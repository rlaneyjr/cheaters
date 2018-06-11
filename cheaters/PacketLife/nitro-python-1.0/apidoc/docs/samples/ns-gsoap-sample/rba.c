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
	struct ns1__addsystemuser sysuser;
	struct ns1__addsystemuserResponse rsysuser;
	struct ns1__bindsystemuser_USCOREpolicy binduser;
	struct ns1__bindsystemuser_USCOREpolicyResponse rbinduser;

	sprintf(nsurl, "%s/soap", nshost);

	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");


		/* add system user */
	memset(&sysuser, 0, sizeof(sysuser));
	sysuser.username = "swetha";
	sysuser.password = "swetha";

	rc = soap_call_ns1__addsystemuser(psoap, nsurl, NSACT,
						  sysuser.username,
						  sysuser.password,
						  &rsysuser);
	_check_result(psoap, rc, (struct _result*)rsysuser.return_,
				  "add sys user swetha");


		/* bind sys user*/
	memset(&binduser, 0, sizeof(binduser));
	binduser.username = "swetha";
	binduser.policyname = "read-only";
	binduser.priority = 1;

	rc = soap_call_ns1__bindsystemuser_USCOREpolicy(psoap, nsurl, NSACT,
						binduser.username,
						binduser.policyname,
						binduser.priority,
						&rbinduser);
	_check_result(psoap, rc, (struct _result*)rbinduser.return_,
				  "bind sys user_policy");


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

