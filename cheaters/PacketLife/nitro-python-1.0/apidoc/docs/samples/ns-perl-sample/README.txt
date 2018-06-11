README for NetScaler API Perl example
-------------------------------------

The example code that accompanies this file uses Perl to communicate
with Netscaler, using XML/SOAP.


SOFTWARE REQUIREMENTS
.....................

* Perl

* SOAP::Lite Perl module  (available at http://www.soaplite.com/)

Note: The NetScaler API uses cookies for client authentication purposes, but
SOAP::Lite does not support cookies on its own.  Please see the work-around
in the samples.


INSTALLATION INSTRUCTIONS
.........................

1. Install all of the required modules:

	perl -MCPAN -c "install 'SOAP::Lite'"


RUNNING THE EXAMPLES
....................

The parameters to all of the examples are :
	<NS IP> <username> <password>

setConfig uses the Netscaler API to:
	* log in to Netscaler
	* add a service
	* bind a monitor
	* add a vserver
	* bind a service to a vserver
	* save configuration
	* log out

getConfig fetches information about all configured lb vservers,
and prints selected information about each one.

rmConfig removes all of the configuration that was created by setConfig.c.

Additional documentation is available as inline comments in the sample sources.

