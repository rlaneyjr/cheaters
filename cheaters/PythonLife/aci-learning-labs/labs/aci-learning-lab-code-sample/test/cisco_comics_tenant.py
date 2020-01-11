# import libraries
from credentials import *
from acitoolkit.acitoolkit import *

# create session with apic
session = Session(URL, LOGIN, PASSWORD)
session.login()

#create tenant and vrf
tenant = Tenant("Cisco_Comics")
vrf = Context("Network_Universe", tenant)

# create bridge domain with vrf relationship
bridge_domain = BridgeDomain("ACI_Way", tenant)
bridge_domain.add_context(vrf)

# create public subnet and assign gateway
subnet = Subnet("Network1", bridge_domain)
subnet.set_addr("10.10.10.1/24")
subnet.set_scope("public")

# create http filter and filter entry
filter_http = Filter("http", tenant)
filter_entry_tcp80 = FilterEntry("tcp-80", filter_http, etherT="ip", prot="tcp", dFromPort="http", dToPort="http")

# create sql filter and filter entry
filter_sql = Filter("sql", tenant)
filter_entry_tcp1433 = FilterEntry("tcp-1433", filter_sql, etherT="ip", prot="tcp", dFromPort="1433", dToPort="1433")

# create web contract and associate to http filter
contract_web = Contract("web", tenant)
contract_subject_http = ContractSubject("http", contract_web)
contract_subject_http.add_filter(filter_http)

# create database contract and associate to sql filter
contract_database = Contract("database", tenant)
contract_subject_sql = ContractSubject("sql", contract_database)
contract_subject_sql.add_filter(filter_sql)

# create application profile
app_profile = AppProfile("App_Deployer", tenant)

# create web epg and associate bridge domain and contracts
epg_web = EPG("Web", app_profile)
epg_web.add_bd(bridge_domain)
epg_web.provide(contract_web)
epg_web.consume(contract_database)

# create db epg and associate bridge domain and contract
epg_db = EPG("Database", app_profile)
epg_db.add_bd(bridge_domain)
epg_db.provide(contract_database)

# print url and configuration data
print("\n{}\n\n{}".format(tenant.get_url(), tenant.get_json()))

# push configuration to apic
resp = session.push_to_apic(tenant.get_url(), tenant.get_json())

# test configuration request
if resp.ok:
    print("\n{}: {}\n\n{} is ready for action".format(resp.status_code, resp.reason, app_profile.name))
else:
    print("\n{}: {}\n\n{} was not created!\n\n Error: {}".format(resp.status_code, resp.reason, subnet.name, resp.content))

# exit
exit()