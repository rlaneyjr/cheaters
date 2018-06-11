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
	

 $result = $soap->addserver(name('name'=> 's1' ),name('ipaddress'=> '10.102.3.84' ),name('domain'=> '' ),name('state'=> 'VALNOTSET' ))	->result;
print "addserver s1:" . $result->{'message'}."\n";

 $result = $soap->addserver(name('name'=> 's2' ),name('ipaddress'=> '10.102.3.83' ),name('domain'=> '' ),name('state'=> 'VALNOTSET' ))	->result;
print "addserver s2:" . $result->{'message'}."\n";

 $result = $soap->addservice(name('name'=> 'src1' ),name('ip'=> '' ),name('servername'=> 's1' ),name('servicetype'=> 'HTTP' ),name('port'=> '80' ),name('cleartextport'=> '0xFFFFFFFF' ),name('cachetype'=> 'VALNOTSET' ),name('state'=> 'VALNOTSET' ))	->result;
print "addservice src1:" . $result->{'message'}."\n";

 $result = $soap->addservice(name('name'=> 'src2' ),name('ip'=> '' ),name('servername'=> 's2' ),name('servicetype'=> 'HTTP' ),name('port'=> '80' ),name('cleartextport'=> '0xFFFFFFFF' ),name('cachetype'=> 'VALNOTSET' ),name('state'=> 'VALNOTSET' ))	->result;
print "addservice src2:" . $result->{'message'}."\n";

 $result = $soap->addlbvserver(name('name'=> 'sslbase' ),name('servicetype'=> 'SSL' ),name('ipaddress'=> '10.102.3.100' ),name('port'=> '443' ),name('range'=> '0xFFFFFFFF' ),name('state'=> 'VALNOTSET' ),name('vipheader'=> '' ))	->result;
print "addlbvserver sslbase:" . $result->{'message'}."\n";

 $result = $soap->bindlbvserver_service(name('name'=> 'sslbase' ),name('servicename'=> 'src1' ),name('weight'=> '0xFFFFFFFF' ))	->result;
print "bindlbvserver_service sslbase:" . $result->{'message'}."\n";

 $result = $soap->bindlbvserver_service(name('name'=> 'sslbase' ),name('servicename'=> 'src2' ),name('weight'=> '0xFFFFFFFF' ))	->result;
print "bindlbvserver_service sslbase:" . $result->{'message'}."\n";

 $result = $soap->addsslcertkey(name('certkeyname'=> 'server_cert' ),name('cert'=> '/nsconfig/ssl/certs/cert1.pem' ),name('key'=> '/nsconfig/ssl/certs/cert1ky.pem' ),name('password'=> 'false' ),name('fipskey'=> '' ),name('inform'=> 'VALNOTSET' ),name('expirymonitor'=> 'VALNOTSET' ),name('notificationperiod'=> '0xFFFFFFFF' ))	->result;
print "addsslcertkey server_cert:" . $result->{'message'}."\n";

 $result = $soap->bindsslcertkey_vserver(name('certkeyname'=> 'server_cert' ),name('vservername'=> 'sslbase' ),name('vserver'=> 'false' ))	->result;
print "bindsslcertkey_vserver server_cert:" . $result->{'message'}."\n";
# Logout
print "logout: ";
$result = $soap->logout()->result;
print $result->{'message'} . "\n";

exit;
