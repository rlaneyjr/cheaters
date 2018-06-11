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
	

 $result = $soap->addsystemuser(name('username'=> 'user1' ),name('password'=> 'passwd1' ))	->result;
print "addsystemuser user1:" . $result->{'message'}."\n";

 $result = $soap->addsystemuser(name('username'=> 'user2' ),name('password'=> 'passwd2' ))	->result;
print "addsystemuser user2:" . $result->{'message'}."\n";

 $result = $soap->bindsystemuser_policy(name('username'=> 'user1' ),name('policyname'=> 'read-only' ),name('priority'=> '1' ))	->result;
print "bindsystemuser_policy user1:" . $result->{'message'}."\n";

 $result = $soap->bindsystemuser_policy(name('username'=> 'user1' ),name('policyname'=> 'operator' ),name('priority'=> '2' ))	->result;
print "bindsystemuser_policy user1:" . $result->{'message'}."\n";

 $result = $soap->addsystemgroup(name('groupname'=> 'group1' ))	->result;
print "addsystemgroup group1:" . $result->{'message'}."\n";

 $result = $soap->bindsystemgroup_user(name('groupname'=> 'group1' ),name('username'=> 'user2' ))	->result;
print "bindsystemgroup_user group1:" . $result->{'message'}."\n";

 $result = $soap->bindsystemgroup_policy(name('groupname'=> 'group1' ),name('policyname'=> 'read-only' ),name('priority'=> '1' ))	->result;
print "bindsystemgroup_policy group1:" . $result->{'message'}."\n";

 $result = $soap->addsystemcmdpolicy(name('policyname'=> 'add_pol1' ),name('actioN'=> 'ALLOW' ),name('cmdspec'=> '^add.*' ))	->result;
print "addsystemcmdpolicy add_pol1:" . $result->{'message'}."\n";

 $result = $soap->bindsystemuser_policy(name('username'=> 'user1' ),name('policyname'=> 'add_pol1' ),name('priority'=> '3' ))	->result;
print "bindsystemuser_policy user1:" . $result->{'message'}."\n";

 $result = $soap->getsystemuser(name('username'=> '' ))	->result;
print "getsystemuser null:" . $result->{'message'}."\n";

if ($result->{rc}==0) {
foreach $obj (@{$result->{List}} ) {
print "username::$obj->{username}\tgroupname::$obj->{groupname}\tpolicyname::$obj->{policyname}\tpriority::$obj->{priority}\n";
}
}

 $result = $soap->getsystemgroup(name('groupname'=> '' ))	->result;
print "getsystemgroup null:" . $result->{'message'}."\n";

if ($result->{rc}==0) {
foreach $obj (@{$result->{List}} ) {
print "groupname::$obj->{groupname}\tusername::$obj->{username}\tpolicyname::$obj->{policyname}\tpriority::$obj->{priority}\n";
}
}
# Logout
print "logout: ";
$result = $soap->logout()->result;
print $result->{'message'} . "\n";

exit;
