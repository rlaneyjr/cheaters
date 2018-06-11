use SOAP::Lite;		# troubleshoot: append: +trace=>"debug";
import SOAP::Data 'name';		# to set data values (q.v.)
use HTTP::Cookies;		# server uses client cookie for auth

# Command-line parameters:  <NS IP> <username> <password>
my $NS = shift @ARGV;
$NS = "localhost" if (!$NS);
my $username = shift @ARGV;
$username = "nsroot" if (!$username);
my $password = shift @ARGV;
$password = "nsroot" if (!$password);
	  
# Cookie object.  Server sends cookie for client authentication.
my $cookies = HTTP::Cookies->new(ignore_discard => 1, hide_cookie2 => 1);

# Create the soap object
my $soap = SOAP::Lite
# service URI and cookie object
-> proxy("http://$NS/soap", cookie_jar=>$cookies)
;
	 
# Log on
print "login: ";
	my $result = $soap->login( name('username'=>$username), 
name('password'=>$password) )
->result;
print $result->{'message'} ."\n";
	

 $result = $soap->addsslcertkey(name('certkeyname'=> 'ca_cert' ),name('cert'=> '/nsconfig/ssl/certs/ca_cert.pem' ),name('key'=> '' ),name('password'=> 'false' ),name('fipskey'=> '' ),name('inform'=> 'VALNOTSET' ),name('expirymonitor'=> 'VALNOTSET' ),name('notificationperiod'=> '0xFFFFFFFF' ))	->result;
print "addsslcertkey ca_cert:" . $result->{'message'}."\n";

 $result = $soap->addsslcertkey(name('certkeyname'=> 'root_cert' ),name('cert'=> '/nsconfig/ssl/certs/root_cert.pem' ),name('key'=> '' ),name('password'=> 'false' ),name('fipskey'=> '' ),name('inform'=> 'VALNOTSET' ),name('expirymonitor'=> 'VALNOTSET' ),name('notificationperiod'=> '0xFFFFFFFF' ))	->result;
print "addsslcertkey root_cert:" . $result->{'message'}."\n";

 $result = $soap->addsslcrl(name('crlname'=> 'crl1' ),name('crlpath'=> '/var/netscaler/ssl/crl.pem' ),name('inform'=> 'VALNOTSET' ))	->result;
print "addsslcrl crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_cacert(name('crlname'=> 'crl1' ),name('cacert'=> 'ca_cert' ))	->result;
print "setsslcrl_cacert crl1:" . $result->{'message'}."\n";

 $result = $soap->addsslcrl(name('crlname'=> 'crl1' ),name('crlpath'=> '/var/netscaler/ssl/crl.pem' ),name('inform'=> 'VALNOTSET' ))	->result;
print "addsslcrl crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_refresh(name('crlname'=> 'crl1' ),name('refresh'=> 'ENABLED' ))	->result;
print "setsslcrl_refresh crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_cacert(name('crlname'=> 'crl1' ),name('cacert'=> 'ca_cert' ))	->result;
print "setsslcrl_cacert crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_server(name('crlname'=> 'crl1' ),name('server'=> '10.102.3.120' ))	->result;
print "setsslcrl_server crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_method(name('crlname'=> 'crl1' ),name('method'=> 'HTTP' ),name('url'=> '' ))	->result;
print "setsslcrl_method crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_port(name('crlname'=> 'crl1' ),name('port'=> '80' ))	->result;
print "setsslcrl_port crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_interval(name('crlname'=> 'crl1' ),name('interval'=> 'WEEKLY' ))	->result;
print "setsslcrl_interval crl1:" . $result->{'message'}."\n";

 $result = $soap->addsslcrl(name('crlname'=> 'crl1' ),name('crlpath'=> '/var/netscaler/ssl/crl.pem' ),name('inform'=> 'VALNOTSET' ))	->result;
print "addsslcrl crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_refresh(name('crlname'=> 'crl1' ),name('refresh'=> 'ENABLED' ))	->result;
print "setsslcrl_refresh crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_cacert(name('crlname'=> 'crl1' ),name('cacert'=> 'ca_cert' ))	->result;
print "setsslcrl_cacert crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_server(name('crlname'=> 'crl1' ),name('server'=> '10.102.3.120' ))	->result;
print "setsslcrl_server crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_method(name('crlname'=> 'crl1' ),name('method'=> 'LDAP' ),name('url'=> '' ))	->result;
print "setsslcrl_method crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_port(name('crlname'=> 'crl1' ),name('port'=> '389' ))	->result;
print "setsslcrl_port crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_basedn(name('crlname'=> 'crl1' ),name('basedn'=> 'cn=Manager,dc=my-domain,dc=com' ))	->result;
print "setsslcrl_basedn crl1:" . $result->{'message'}."\n";

 $result = $soap->setsslcrl_interval(name('crlname'=> 'crl1' ),name('interval'=> 'WEEKLY' ))	->result;
print "setsslcrl_interval crl1:" . $result->{'message'}."\n";
# Logout
print "logout: ";
$result = $soap->logout()->result;
print $result->{'message'} . "\n";

exit;
