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


 $result = $soap->addnsacl(name('aclname'=> 'allow_sip' ),name('aclaction'=> 'ALLOW' ),name('ttl'=> '0xFFFFFFFF' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl allow_sip:" . $result->{'message'}."\n";

 $result = $soap->setnsacl_srcip(name('aclname'=> 'allow_sip' ),name('srcip'=> 'true' ),name('operatoR'=> 'VALNOTSET' ),name('srcipval'=> '10.102.3.84' ))	->result;
print "setnsacl_srcip allow_sip:" . $result->{'message'}."\n";

 $result = $soap->addnsacl(name('aclname'=> 'allow_sip_range' ),name('aclaction'=> 'ALLOW' ),name('ttl'=> '0xFFFFFFFF' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl allow_sip_range:" . $result->{'message'}."\n";

 $result = $soap->setnsacl_srcip(name('aclname'=> 'allow_sip_range' ),name('srcip'=> 'true' ),name('operatoR'=> 'VALNOTSET' ),name('srcipval'=> '10.102.3.1-10.102.3.255' ))	->result;
print "setnsacl_srcip allow_sip_range:" . $result->{'message'}."\n";

 $result = $soap->addnsacl(name('aclname'=> 'Deny_sipr' ),name('aclaction'=> 'DENY' ),name('ttl'=> '0xFFFFFFFF' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl Deny_sipr:" . $result->{'message'}."\n";

 $result = $soap->setnsacl_srcip(name('aclname'=> 'Deny_sipr' ),name('srcip'=> 'true' ),name('operatoR'=> 'VALNOTSET' ),name('srcipval'=> '10.10.0.1-10.102.7.152' ))	->result;
print "setnsacl_srcip Deny_sipr:" . $result->{'message'}."\n";

 $result = $soap->addnsacl(name('aclname'=> 'allow_dip' ),name('aclaction'=> 'ALLOW' ),name('ttl'=> '0xFFFFFFFF' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl allow_dip:" . $result->{'message'}."\n";

 $result = $soap->setnsacl_destip(name('aclname'=> 'allow_dip' ),name('destip'=> 'true' ),name('operatoR'=> 'VALNOTSET' ),name('destipval'=> '192.168.17.11' ))	->result;
print "setnsacl_destip allow_dip:" . $result->{'message'}."\n";

 $result = $soap->addnsacl(name('aclname'=> 'allow_dip_rng' ),name('aclaction'=> 'ALLOW' ),name('ttl'=> '0xFFFFFFFF' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl allow_dip_rng:" . $result->{'message'}."\n";

 $result = $soap->setnsacl_destip(name('aclname'=> 'allow_dip_rng' ),name('destip'=> 'true' ),name('operatoR'=> 'VALNOTSET' ),name('destipval'=> '192.168.17.1-192.168.17.250' ))	->result;
print "setnsacl_destip allow_dip_rng:" . $result->{'message'}."\n";

 $result = $soap->addnsacl(name('aclname'=> 'deny_src_mac' ),name('aclaction'=> 'DENY' ),name('ttl'=> '0xFFFFFFFF' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl deny_src_mac:" . $result->{'message'}."\n";

 $result = $soap->setnsacl_srcmac(name('aclname'=> 'deny_src_mac' ),name('srcmac'=> '00:0d:9d:54:64:6a' ))	->result;
print "setnsacl_srcmac deny_src_mac:" . $result->{'message'}."\n";

 $result = $soap->addnsacl(name('aclname'=> 'acl_user_priority' ),name('aclaction'=> 'ALLOW' ),name('ttl'=> '0xFFFFFFFF' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl acl_user_priority:" . $result->{'message'}."\n";

 $result = $soap->setnsacl_priority(name('aclname'=> 'acl_user_priority' ),name('priority'=> '1' ))	->result;
print "setnsacl_priority acl_user_priority:" . $result->{'message'}."\n";


 $result = $soap->disablensacl(name('aclname'=> 'allow_sip' ))	->result;
print "disablensacl allow_sip:" . $result->{'message'}."\n";

 $result = $soap->rmnsacl(name('aclname'=> 'allow_sip' ))	->result;
print "rmnsacl allow_sip:" . $result->{'message'}."\n";

 $result = $soap->clearnsacls()	->result;
print "clearnsacls Deny_sip_dip_dport:" . $result->{'message'}."\n";

 $result = $soap->addnsacl(name('aclname'=> 'acl_ttl' ),name('aclaction'=> 'ALLOW' ),name('ttl'=> '10' ),name('protocol'=> 'VALNOTSET' ),name('established'=> 'false' ),name('icmptype'=> '0xFFFFFFFF' ),name('icmpcode'=> '0xFFFFFFFF' ))	->result;
print "addnsacl acl_ttl:" . $result->{'message'}."\n";


# Logout
print "logout: ";
$result = $soap->logout()->result;
print $result->{'message'} . "\n";

exit;
