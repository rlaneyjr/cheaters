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
	

 $result = $soap->enablensfeature(name('feature'=> 'LB' ))	->result;
print "enablensfeature LB:" . $result->{'message'}."\n";

 $result = $soap->enablensfeature(name('feature'=> 'CS' ))	->result;
print "enablensfeature CS:" . $result->{'message'}."\n";

 $result = $soap->addserver(name('name'=> 's1' ),name('ipaddress'=> '10.102.3.91' ),name('domain'=> '' ),name('state'=> 'VALNOTSET' ))	->result;
print "addserver s1:" . $result->{'message'}."\n";

 $result = $soap->addserver(name('name'=> 's2' ),name('ipaddress'=> '10.102.3.92' ),name('domain'=> '' ),name('state'=> 'VALNOTSET' ))	->result;
print "addserver s2:" . $result->{'message'}."\n";

 $result = $soap->addserver(name('name'=> 's3' ),name('ipaddress'=> '10.102.3.93' ),name('domain'=> '' ),name('state'=> 'VALNOTSET' ))	->result;
print "addserver s3:" . $result->{'message'}."\n";

 $result = $soap->addservice(name('name'=> 'srv1' ),name('ip'=> '' ),name('servername'=> 's1' ),name('servicetype'=> 'HTTP' ),name('port'=> '80' ),name('cleartextport'=> '0xFFFFFFFF' ),name('cachetype'=> 'VALNOTSET' ),name('state'=> 'VALNOTSET' ))	->result;
print "addservice srv1:" . $result->{'message'}."\n";

 $result = $soap->addservice(name('name'=> 'srv2' ),name('ip'=> '' ),name('servername'=> 's2' ),name('servicetype'=> 'HTTP' ),name('port'=> '80' ),name('cleartextport'=> '0xFFFFFFFF' ),name('cachetype'=> 'VALNOTSET' ),name('state'=> 'VALNOTSET' ))	->result;
print "addservice srv2:" . $result->{'message'}."\n";

 $result = $soap->addservice(name('name'=> 'srv3' ),name('ip'=> '' ),name('servername'=> 's3' ),name('servicetype'=> 'HTTP' ),name('port'=> '80' ),name('cleartextport'=> '0xFFFFFFFF' ),name('cachetype'=> 'VALNOTSET' ),name('state'=> 'VALNOTSET' ))	->result;
print "addservice srv3:" . $result->{'message'}."\n";

 $result = $soap->addlbvserver(name('name'=> 'lbvip1' ),name('servicetype'=> 'HTTP' ),name('ipaddress'=> '' ),name('port'=> '0xFFFFFFFF' ),name('range'=> '0xFFFFFFFF' ),name('state'=> 'VALNOTSET' ),name('vipheader'=> '' ))	->result;
print "addlbvserver lbvip1:" . $result->{'message'}."\n";

 $result = $soap->addlbvserver(name('name'=> 'lbvip2' ),name('servicetype'=> 'HTTP' ),name('ipaddress'=> '' ),name('port'=> '0xFFFFFFFF' ),name('range'=> '0xFFFFFFFF' ),name('state'=> 'VALNOTSET' ),name('vipheader'=> '' ))	->result;
print "addlbvserver lbvip2:" . $result->{'message'}."\n";

 $result = $soap->addlbvserver(name('name'=> 'lbvip3' ),name('servicetype'=> 'HTTP' ),name('ipaddress'=> '' ),name('port'=> '0xFFFFFFFF' ),name('range'=> '0xFFFFFFFF' ),name('state'=> 'VALNOTSET' ),name('vipheader'=> '' ))	->result;
print "addlbvserver lbvip3:" . $result->{'message'}."\n";

 $result = $soap->bindlbvserver_service(name('name'=> 'lbvip1' ),name('servicename'=> 'srv1' ),name('weight'=> '0xFFFFFFFF' ))	->result;
print "bindlbvserver_service lbvip1:" . $result->{'message'}."\n";

 $result = $soap->bindlbvserver_service(name('name'=> 'lbvip2' ),name('servicename'=> 'srv2' ),name('weight'=> '0xFFFFFFFF' ))	->result;
print "bindlbvserver_service lbvip2:" . $result->{'message'}."\n";

 $result = $soap->bindlbvserver_service(name('name'=> 'lbvip3' ),name('servicename'=> 'srv3' ),name('weight'=> '0xFFFFFFFF' ))	->result;
print "bindlbvserver_service lbvip3:" . $result->{'message'}."\n";

 $result = $soap->addcspolicy(name('policyname'=> 'contains_html' ),name('url'=> '' ),name('rule'=> 'REQ.HTTP.URL CONTAINS html' ),name('domain'=> '' ))	->result;
print "addcspolicy contains_html:" . $result->{'message'}."\n";

 $result = $soap->addcspolicy(name('policyname'=> 'contains_txt' ),name('url'=> '' ),name('rule'=> 'REQ.HTTP.URL CONTAINS gif' ),name('domain'=> '' ))	->result;
print "addcspolicy contains_txt:" . $result->{'message'}."\n";

 $result = $soap->addcspolicy(name('policyname'=> 'contains_gif' ),name('url'=> '' ),name('rule'=> 'REQ.HTTP.URL CONTAINS asp' ),name('domain'=> '' ))	->result;
print "addcspolicy contains_gif:" . $result->{'message'}."\n";

 $result = $soap->addcsvserver(name('name'=> 'csvip' ),name('servicetype'=> 'HTTP' ),name('ipaddress'=> '10.102.3.54' ),name('range'=> '0xFFFFFFFF' ),name('port'=> '80' ),name('state'=> 'VALNOTSET' ),name('vipheader'=> '' ))	->result;
print "addcsvserver csvip:" . $result->{'message'}."\n";

 $result = $soap->bindcsvserver_targetvserver(name('name'=> 'csvip' ),name('targetvserver'=> 'lbvip1' ),name('policyname'=> 'contains_html' ),name('priority'=> '5' ),name('gotopriorityexpression'=> '' ),name('type'=> 'VALNOTSET' ),name('invoke'=> 'false' ),name('labeltype'=> 'VALNOTSET' ),name('labelname'=> '' ))	->result;
print "bindcsvserver_targetvserver csvip:" . $result->{'message'}."\n";

 $result = $soap->bindcsvserver_targetvserver(name('name'=> 'csvip' ),name('targetvserver'=> 'lbvip2' ),name('policyname'=> 'contains_txt' ),name('priority'=> '5' ),name('gotopriorityexpression'=> '' ),name('type'=> 'VALNOTSET' ),name('invoke'=> 'false' ),name('labeltype'=> 'VALNOTSET' ),name('labelname'=> '' ))	->result;
print "bindcsvserver_targetvserver csvip:" . $result->{'message'}."\n";

 $result = $soap->bindcsvserver_targetvserver(name('name'=> 'csvip' ),name('targetvserver'=> 'lbvip3' ),name('policyname'=> 'contains_gif' ),name('priority'=> '5' ),name('gotopriorityexpression'=> '' ),name('type'=> 'VALNOTSET' ),name('invoke'=> 'false' ),name('labeltype'=> 'VALNOTSET' ),name('labelname'=> '' ))	->result;
print "bindcsvserver_targetvserver csvip:" . $result->{'message'}."\n";
# Logout
print "logout: ";
$result = $soap->logout()->result;
print $result->{'message'} . "\n";

exit;
