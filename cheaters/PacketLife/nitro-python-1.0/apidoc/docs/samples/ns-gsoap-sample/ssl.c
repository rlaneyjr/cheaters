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
	struct ns1__addsslcertkey cert;
	struct ns1__addsslcertkeyResponse rcert;

	sprintf(nsurl, "%s/soap", nshost);

	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");

	memset(&cert, 0, sizeof(cert));
	cert.certkeyname = "server_cert";
	cert.cert = "/nsconfig/ssl/certs/cert1.pem";
	cert.key = "/nsconfig/ssl/certs/cert1ky.pem";
	cert.password = FALSE;
	cert.fipskey = NULL;
	cert.inform = ns1__informatsEnum__VALNOTSET;
	cert.expirymonitor = ns1__enabledisabledEnum__VALNOTSET;
	cert.notificationperiod = -1;
	rc = soap_call_ns1__addsslcertkey(psoap, nsurl, NSACT,
						cert.certkeyname,
						cert.cert,
						cert.key,
						cert.password,
						cert.fipskey,
						cert.inform,
						cert.expirymonitor,
						cert.notificationperiod,
						&rcert);
	_check_result(psoap, rc, (struct _result*)rcert.return_,
				  "add sslcertkey");


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

