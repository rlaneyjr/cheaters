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


 $result = $soap->enablensfeature(name('feature'=> 'REWRITE' ))	->result;
print "enablensfeature REWRITE:" . $result->{'message'}."\n";

 $result = $soap->addrewriteaction(name('name'=> 'rewrite_act1' ),name('type'=> 'delete' ),name('target'=> 'HTTP.RES.HEADER("Server").VALUE(0)' ),name('stringbuilderexpr'=> '' ),name('bypasssafetycheck'=> 'VALNOTSET' ))	->result;
print "addrewriteaction rewrite_act1:" . $result->{'message'}."\n";

 $result = $soap->addrewritepolicy(name('name'=> 'rewrite_pol1' ),name('rule'=> 'HTTP.RES.HEADER("Server").CONTAINS("IIS")' ),name('actioN'=> 'rewrite_act1' ),name('undefaction'=> '' ))	->result;
print "addrewritepolicy rewrite_pol1:" . $result->{'message'}."\n";

 $result = $soap->bindrewriteglobal_policy(name('policyname'=> 'rewrite_pol1' ),name('priority'=> '1' ),name('gotopriorityexpression'=> 'END' ),name('type'=> 'VALNOTSET' ),name('invoke'=> 'false' ),name('labeltype'=> 'VALNOTSET' ),name('labelname'=> '' ))	->result;
print "bindrewriteglobal_policy rewrite_pol1:" . $result->{'message'}."\n";

# Logout
print "logout: ";
$result = $soap->logout()->result;
print $result->{'message'} . "\n";

exit;
