/* Sample C script to demonstrate Netscaler API
 * Command-line parameters (all optional):  <NS IP> <username> <password>
 */

/* $ ./getStats 10.102.4.107
 * login: Done
 * statlbvserver: Done
 *  vip_1	   SSL	 10.102.6.229	0 DOWN
 * log out: EOF
 */

#include <stdio.h>

#include "statH.h"
#include "statStub.h"
#include "NSStatBinding.nsmap"

#define FALSE	0
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
	struct ns1__statlbvserverResponse rvserver;
	struct lbvserverstatsList* pvl;

	sprintf(nsurl, "http://%s/soap", nshost);


	psoap = soap_new();
	soap_omode(psoap, SOAP_XML_TREE);	/* non-href mode */
	/* we use cookies */
	psoap->cookie_domain = "";
	psoap->cookie_path = "/soap";

	/* log in */
	rc = soap_call_ns1__login(psoap, nsurl, NSACT, uname, passwd, &rlogin);
	_check_result(psoap, rc, (struct _result*)rlogin.return_, "login");
	/* stat vserver detail */
	rc = soap_call_ns1__statlbvserver(psoap, nsurl, NSACT, "vip_1", &rvserver);
	_check_result(psoap, rc, (struct _result*)rvserver.return_,
		  "stat vserver");
	pvl = rvserver.return_->List;
	if (pvl == NULL) {
	"(no vservers)\n";
		} else if (rvserver.return_->rc == 0) {
	for (i=0; i<pvl->__size; i++) {
		printf("%s:\t%s:%u(%s)\t%s\n",
		   pvl->__ptr[i]->name,
		   pvl->__ptr[i]->primaryipaddress,
		   pvl->__ptr[i]->primaryport,
		   pvl->__ptr[i]->state,
		   pvl->__ptr[i]->totalresponses);
	}
		}
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
