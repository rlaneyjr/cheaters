README for NetScaler API C# example
-----------------------------------

The example code that accompanies this file uses C# to communicate
with Netscaler, using XML/SOAP.


SOFTWARE REQUIREMENTS
.....................

* .Net Framework, 1.0 or later

Note: The NetScaler API uses cookies for client authentication purposes, but
the .Net Framework does not support cookies on its own.  Please see the
work-around in the samples.


INSTALLATION INSTRUCTIONS
.........................

1. Extract files from the archive.  It contains, among other files:
	* WSDL filter (filterwsdl)
	* the sample sources

2. Customize makesamp.bat, setting the variables at the top to match your
   environment.

3. 	In the directory where you extracted these files, type:

		makesamp [ENTER]

	makesamp.bat does the following:

	* Obtain NSConfig.wsdl and NSStat.wsdl from the NetScaler.

	  The wsdl file for the API is located on the Netscaler device,
	  at //Netscaler/api/NSConfig.wsdl.

	* Create a subset of NSConfig.wsdl.

	  The full NSConfig.wsdl file is very large - it can take up to five minutes
	  or more to process it.  This can be avoided by creating a custom subset
	  of the WSDL, containing just the needed methods.  makesamp.bat does this
	  by downloading the full WSDL as NSConfig.fullwsdl and then filtering:

		filterwsdl NSConfig.fullwsdl "addservice" "setservice" "showservice" "bindlbmonitor" "addlbvserver" "bindlbvserver" "showlbvserver" "rmservice" "rmlbvserver" "savensconfig" > NSConfig.wsdl

	* Generate stubs from the WSDL files.

	  Stubs are generated using wsdl.exe, from Visual Studio .NET.
	  In C#, the stubs are all methods in a single class, NSConfigService (or
	  NSStatService).

	* Compile the sample and stub sources into setConfig, getConfig, and
	  rmConfig executables.


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

