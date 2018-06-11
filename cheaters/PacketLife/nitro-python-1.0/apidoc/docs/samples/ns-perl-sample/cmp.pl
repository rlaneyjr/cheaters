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
	

 $result = $soap->enablensfeature(name('feature'=> 'CMP' ))	->result;
print "enablensfeature CMP:" . $result->{'message'}."\n";

 $result = $soap->setservice_cmp(name('name'=> 'svc1' ),name('cmp'=> 'YES' ))	->result;
print "setservice_cmp svc1:" . $result->{'message'}."\n";

 $result = $soap->setservice_cmp(name('name'=> 'svc2' ),name('cmp'=> 'NO' ))	->result;
print "setservice_cmp svc2:" . $result->{'message'}."\n";

 $result = $soap->addcmppolicy(name('name'=> 'cmp1' ),name('rule'=> 'url == /testsite/file5.html' ),name('resaction'=> 'nocompress' ))	->result;
print "addcmppolicy cmp1:" . $result->{'message'}."\n";

 $result = $soap->bindcmpglobal_policy(name('policyname'=> 'cmp1' ),name('priority'=> '0xFFFFFFFF' ),name('state'=> 'VALNOTSET' ))	->result;
print "bindcmpglobal_policy cmp1:" . $result->{'message'}."\n";

 $result = $soap->addpolicyexpression(name('name'=> 'ex1' ),name('value'=> 'RES.HTTP.HEADER Content-Type CONTAINS application/msword' ))	->result;
print "addpolicyexpression ex1:" . $result->{'message'}."\n";

 $result = $soap->addcmppolicy(name('name'=> 'cmp2' ),name('rule'=> 'ex1' ),name('resaction'=> 'deflate' ))	->result;
print "addcmppolicy cmp2:" . $result->{'message'}."\n";

 $result = $soap->bindcmpglobal_policy(name('policyname'=> 'cmp2' ),name('priority'=> '0xFFFFFFFF' ),name('state'=> 'VALNOTSET' ))	->result;
print "bindcmpglobal_policy cmp2:" . $result->{'message'}."\n";

 $result = $soap->addcmppolicy(name('name'=> 'cmp3' ),name('rule'=> 'url contains file50 || RES.HTTP.HEADER Content-Type CONTAINS text/css' ),name('resaction'=> 'deflate' ))	->result;
print "addcmppolicy cmp3:" . $result->{'message'}."\n";

 $result = $soap->bindlbvserver_policy(name('name'=> 'lbvip1' ),name('policyname'=> 'cmp3' ),name('priority'=> '0xFFFFFFFF' ),name('gotopriorityexpression'=> '' ),name('type'=> 'VALNOTSET' ),name('invoke'=> 'false' ),name('labeltype'=> 'VALNOTSET' ),name('labelname'=> '' ))	->result;
print "bindlbvserver_policy lbvip1:" . $result->{'message'}."\n";

 $result = $soap->addpolicyexpression(name('name'=> 'ex2' ),name('value'=> 'HEADER User-Agent CONTAINS MSIE' ))	->result;
print "addpolicyexpression ex2:" . $result->{'message'}."\n";

 $result = $soap->addpolicyexpression(name('name'=> 'ex3' ),name('value'=> 'RES.HTTP.HEADER Content-Type CONTAINS application/vnd.ms-excel' ))	->result;
print "addpolicyexpression ex3:" . $result->{'message'}."\n";

 $result = $soap->addcmppolicy(name('name'=> 'cmp4' ),name('rule'=> 'ex2&&ex3' ),name('resaction'=> 'gzip' ))	->result;
print "addcmppolicy cmp4:" . $result->{'message'}."\n";

 $result = $soap->bindlbvserver_policy(name('name'=> 'lbvip2' ),name('policyname'=> 'cmp4' ),name('priority'=> '0xFFFFFFFF' ),name('gotopriorityexpression'=> '' ),name('type'=> 'VALNOTSET' ),name('invoke'=> 'false' ),name('labeltype'=> 'VALNOTSET' ),name('labelname'=> '' ))	->result;
print "bindlbvserver_policy lbvip2:" . $result->{'message'}."\n";
# Logout
print "logout: ";
$result = $soap->logout()->result;
print $result->{'message'} . "\n";

exit;
