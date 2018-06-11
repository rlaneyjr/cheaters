# 
# Makefile for NetScaler gSOAP example client: Unix version.
# See README.txt.
#
# Modify the following as necessary in you environment (or set them on the
# gmake command line)
CC?=gcc
NS?=10.102.31.7
METHODS?=addservice setservice* addnsacl  addcspolicy addcsvserver bindcsvserver* addcmppolicy bindcmpglobal* addpolicyexpression showservice bindlbmonitor* addlbvserver rmlbvserver bindlbvserver* showlbvserver rmservice rmvserver bindsystemuser* addsystemuser addrewriteaction addrewritepolicy bindrewriteglobal* addsslcertkey addsslcrl savensconfig

#-----------------------------------------------------------------------

all: setConfig getConfig rmConfig getStat acl csw cmp lb rba rewrite ssl ssl_crl

CFLAGS += -DWITH_COOKIES -DHAVE_CONFIG_H

GSOAPCONFIGOBJS = stdsoap2.o soapC.o soapClient.o statC.o statClient.o
GSOAPCONFIGLIB = gsoapconfiglib.a

GSOAPSTATOBJS = stdsoap2.o statC.o statClient.o
GSOAPSTATLIB = gsoapstatlib.a

setConfig: NSConfig.h $(GSOAPCONFIGLIB) setConfig.o
	$(CC) setConfig.o $(GSOAPCONFIGLIB) -o $@
getConfig: NSConfig.h $(GSOAPCONFIGLIB) getConfig.o
	$(CC) getConfig.o $(GSOAPCONFIGLIB) -o $@
getStat: NSStat.h $(GSOAPSTATLIB) getStat.o
	$(CC) getStat.o $(GSOAPSTATLIB) -o $@
rmConfig: NSConfig.h $(GSOAPCONFIGLIB) rmConfig.o
	$(CC) rmConfig.o $(GSOAPCONFIGLIB) -o $@
acl: NSConfig.h $(GSOAPCONFIGLIB) acl.o
	$(CC) acl.o $(GSOAPCONFIGLIB) -o $@
csw: NSConfig.h $(GSOAPCONFIGLIB) csw.o
	$(CC) csw.o $(GSOAPCONFIGLIB) -o $@
cmp: NSConfig.h $(GSOAPCONFIGLIB) cmp.o
	$(CC) cmp.o $(GSOAPCONFIGLIB) -o $@
lb: NSConfig.h $(GSOAPCONFIGLIB) lb.o
	$(CC) lb.o $(GSOAPCONFIGLIB) -o $@
rba: NSConfig.h $(GSOAPCONFIGLIB) rba.o
	$(CC) rba.o $(GSOAPCONFIGLIB) -o $@
rewrite: NSConfig.h $(GSOAPCONFIGLIB) rewrite.o
	$(CC) rewrite.o $(GSOAPCONFIGLIB) -o $@
ssl: NSConfig.h $(GSOAPCONFIGLIB) ssl.o
	$(CC) ssl.o $(GSOAPCONFIGLIB) -o $@
ssl_crl: NSConfig.h $(GSOAPCONFIGLIB) ssl_crl.o
	$(CC) ssl_crl.o $(GSOAPCONFIGLIB) -o $@


NSConfig.h: NSConfig.wsdl
	./wsdl2h -c -o NSConfig.h NSConfig.wsdl

NSStat.h: NSStat.wsdl
	./wsdl2h -c -o NSStat.h NSStat.wsdl
$(GSOAPCONFIGLIB): $(GSOAPCONFIGOBJS)
	ar rcsuv $@ $(GSOAPCONFIGOBJS)

NSConfig.wsdl : NSConfig.fullwsdl
	./filterwsdl NSConfig.fullwsdl $(METHODS) > NSConfig.wsdl
NSConfig.fullwsdl :
	scp nsroot@$(NS):/netscaler/api/NSConfig.wsdl $@
NSStat.wsdl :
	scp nsroot@$(NS):/netscaler/api/$@ .

$(GSOAPSTATLIB): $(GSOAPSTATOBJS)
	ar rcsuv $@ $(GSOAPSTATOBJS)
soapC.o: soapC.c
statC.o: statC.c
soapClient.o: soapClient.c
statClient.o: statClient.c

soapC.c: xml.h NSConfig.h 
	./soapcpp2 -c NSConfig.h 

soapClient.c: xml.h NSConfig.h
	./soapcpp2 -c NSConfig.h

soapClientS.c: xml.h NSStat.h
	./soapcpp2 -c NSStat.h

statC.c: xml.h NSStat.h
	./soapcpp2 -c -p stat NSStat.h 

# A file that was left out of the gSOAP 2.4.1 distribution ...
xml.h :
	@echo typedef char *XML\; > $@

.PHONY: clean
clean:
	rm -fr getStat getConfig setConfig rmConfig acl csw cmp lb rba rewrite ssl ssl_crl *.o *.xml *.nsmap *.log \
	soapNSConfig* soapServer* soapClient* soapC* NSConfig.h* soapH.h \
	soapStub.h $(GSOAPCONFIGLIB) $(GSOAPSTATLIB)
