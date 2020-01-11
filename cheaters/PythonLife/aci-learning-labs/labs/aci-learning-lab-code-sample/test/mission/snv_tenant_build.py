import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.ip
import cobra.model.vz
import cobra.model.pol
import cobra.model.vpc
import cobra.model.fvns
import cobra.model.lacp
import cobra.model.phys
import cobra.model.infra
import cobra.model.l3ext
import cobra.model.fabric
from cobra.internal.codec.xmlcodec import toXMLStr


# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://apic', 'admin', 'password')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')
infraInfra = cobra.model.infra.Infra(polUni)

# build the vlan pools
snv_pool = cobra.model.fvns.VlanInstP(infraInfra, name=u'SnV_general_pool', allocMode=u'static')
snv_range = cobra.model.fvns.EncapBlk(snv_pool, to=u'vlan-199', from_=u'vlan-100')

# build the phys domain
snv_phys_domain = cobra.model.phys.DomP(polUni, name=u'SnV_phys')
infraRsVlanNs = cobra.model.infra.RsVlanNs(snv_phys_domain, tDn=u'uni/infra/vlanns-[SnV_general_pool]-static')

# build the l3ext domain
snv_l3ext_domain = cobra.model.l3ext.DomP(polUni, name=u'SnV_external_corporate')

# build phys aaep
snv_aaep_phys = cobra.model.infra.AttEntityP(infraInfra, name=u'SnV_phys')
snv_aaep_phys_domain = cobra.model.infra.RsDomP(snv_aaep_phys, tDn=u'uni/phys-SnV_phys')
snv_aaep_phys_infra = cobra.model.infra.FuncP(infraInfra)

# build l3ext aaep
snv_aaep_l3ext = cobra.model.infra.AttEntityP(infraInfra, name=u'SnV_corporate_external')
snv_aaep_l3ext_domain = cobra.model.infra.RsDomP(snv_aaep_l3ext, tDn=u'uni/l3dom-SnV_external_corporate')
snv_aaep_l3ext_infra = cobra.model.infra.FuncP(infraInfra)

# build the lacp active policy
lacpLagPol = cobra.model.lacp.LagPol(infraInfra, name=u'lacp_active', ctrl=u'fast-sel-hot-stdby,graceful-conv,susp-individual', mode=u'active')

# build the interface policy groups
infraFuncP = cobra.model.infra.FuncP(infraInfra)

snv_standard_pg = cobra.model.infra.AccPortGrp(infraFuncP, name=u'SnV_standard_access')
snv_standard_aaep = cobra.model.infra.RsAttEntP(snv_standard_pg, tDn=u'uni/infra/attentp-SnV_phys')

snv_corp_ext_pg = cobra.model.infra.AccPortGrp(infraFuncP, name=u'SnV_corporate_external')
snv_corp_ext_aaep = cobra.model.infra.RsAttEntP(snv_corp_ext_pg, tDn=u'uni/infra/attentp-SnV_corporate_external')

fi1a_bundle = cobra.model.infra.AccBndlGrp(infraFuncP, lagT=u'node', name=u'SnV_FI-1A')
fi1a_aaep = cobra.model.infra.RsAttEntP(fi1a_bundle, tDn=u'uni/infra/attentp-SnV_phys')
fi1a_lacp = cobra.model.infra.RsLacpPol(fi1a_bundle, tnLacpLagPolName=u'lacp_active')

fi1b_bundle = cobra.model.infra.AccBndlGrp(infraFuncP, lagT=u'node', name=u'SnV_FI-1B')
fi1b_aaep = cobra.model.infra.RsAttEntP(fi1b_bundle, tDn=u'uni/infra/attentp-SnV_phys')
fi1b_lacp = cobra.model.infra.RsLacpPol(fi1b_bundle, tnLacpLagPolName=u'lacp_active')

# build the interface profiles
snv_corp_ext_acc = cobra.model.infra.AccPortP(infraInfra, name=u'SnV_corporate_external')
snv_corp_ext_phys_port = cobra.model.infra.HPortS(snv_corp_ext_acc, name=u'ethernet1_48', type='range')
snv_corp_ext_port_range = cobra.model.infra.PortBlk(snv_corp_ext_phys_port, name=u'block2', fromPort=u'48', toPort=u'48')
snv_corp_ext_config = cobra.model.infra.RsAccBaseGrp(snv_corp_ext_phys_port, tDn=u'uni/infra/funcprof/accportgrp-SnV_corporate_external')

snv_server1_acc = cobra.model.infra.AccPortP(infraInfra, name=u'SnV_server1')
snv_server1_phys_port = cobra.model.infra.HPortS(snv_server1_acc, name=u'ethernet1_1', type='range')
snv_server1_port_range = cobra.model.infra.PortBlk(snv_server1_phys_port, name=u'block2', fromPort=u'1', toPort=u'1')
snv_server1_config = cobra.model.infra.RsAccBaseGrp(snv_server1_phys_port, tDn=u'uni/infra/funcprof/accportgrp-SnV_standard_access')

snv_server2_acc = cobra.model.infra.AccPortP(infraInfra, name=u'SnV_server2')
snv_server2_phys_port = cobra.model.infra.HPortS(snv_server2_acc, name=u'ethernet1_1', type='range')
snv_server2_port_range = cobra.model.infra.PortBlk(snv_server2_phys_port, name=u'block2', fromPort=u'1', toPort=u'1')
snv_server2_config = cobra.model.infra.RsAccBaseGrp(snv_server2_phys_port, tDn=u'uni/infra/funcprof/accportgrp-SnV_standard_access')

snv_act_pass_acc = cobra.model.infra.AccPortP(infraInfra, name=u'SnV_phys_act_pass')
snv_act_pass_phys_ports = cobra.model.infra.HPortS(snv_act_pass_acc, name=u'ethernet1_2-4', type='range')
snv_act_pass_port_range = cobra.model.infra.PortBlk(snv_act_pass_phys_ports, name=u'block2', fromPort=u'2', toPort=u'4')
snv_act_pass_config = cobra.model.infra.RsAccBaseGrp(snv_act_pass_phys_ports, tDn=u'uni/infra/funcprof/accportgrp-SnV_standard_access')

fi1a_acc = cobra.model.infra.AccPortP(infraInfra, name=u'SnV_FI-1A')
fi1a_phys_ports = cobra.model.infra.HPortS(fi1a_acc, name=u'ethernet1_5-8', type='range')
fi1a_port_range = cobra.model.infra.PortBlk(fi1a_phys_ports, name=u'block2', fromPort=u'5', toPort=u'8')
fi1a_config = cobra.model.infra.RsAccBaseGrp(fi1a_phys_ports, tDn=u'uni/infra/funcprof/accbundle-SnV_FI-1A')

fi1b_acc = cobra.model.infra.AccPortP(infraInfra, name=u'SnV_FI-1B')
fi1b_phys_ports = cobra.model.infra.HPortS(fi1b_acc, name=u'ethernet1_9-12', type='range')
fi1b_port_range = cobra.model.infra.PortBlk(fi1b_phys_ports, name=u'block2', fromPort=u'9', toPort=u'12')
fi1b_confige = cobra.model.infra.RsAccBaseGrp(fi1b_phys_ports, tDn=u'uni/infra/funcprof/accbundle-SnV_FI-1B')

# build the switch profiles and attach interfaces
leaf1 = cobra.model.infra.NodeP(infraInfra, name=u'leaf_1')
leaf1_name = cobra.model.infra.LeafS(leaf1, type=u'range', name=u'leaf_1')
leaf1_range = cobra.model.infra.NodeBlk(leaf1_name, to_=u'101', from_=u'101', name=u'b235d75799f7d020')
leaf1_intfc1 = cobra.model.infra.RsAccPortP(leaf1, tDn=u'uni/infra/accportprof-SnV_server1')

leaf2 = cobra.model.infra.NodeP(infraInfra, name=u'leaf_2')
leaf2_name = cobra.model.infra.LeafS(leaf2, type=u'range', name=u'leaf_2')
leaf2_range = cobra.model.infra.NodeBlk(leaf2_name, to_=u'102', from_=u'102', name=u'9ebfdd3979c07bcf')
leaf2_intfc1 = cobra.model.infra.RsAccPortP(leaf2, tDn=u'uni/infra/accportprof-SnV_server2')

leafs12 = cobra.model.infra.NodeP(infraInfra, name=u'leafs_1-2')
leafs12_name = cobra.model.infra.LeafS(leafs12, type=u'range', name=u'leafs_1-2')
leafs12_range = cobra.model.infra.NodeBlk(leafs12_name, to_=u'102', from_=u'101', name=u'50b60d7cf265710f')
leafs12_intfc1 = cobra.model.infra.RsAccPortP(leafs12, tDn=u'uni/infra/accportprof-SnV_FI-1A')
leafs12_intfc2 = cobra.model.infra.RsAccPortP(leafs12, tDn=u'uni/infra/accportprof-SnV_FI-1B')
leafs12_intfc3 = cobra.model.infra.RsAccPortP(leafs12, tDn=u'uni/infra/accportprof-SnV_corporate_external')
leafs12_intfc4 = cobra.model.infra.RsAccPortP(leafs12, tDn=u'uni/infra/accportprof-SnV_phys_act_pass')

# setup the vpc
fabricInst = cobra.model.fabric.Inst(polUni)
vpcInstPol = cobra.model.vpc.InstPol(fabricInst, name=u'leafs_1-2')

# build the vpc domain
fabricProtPol = cobra.model.fabric.ProtPol(fabricInst)
fabricExplicitGEp = cobra.model.fabric.ExplicitGEp(fabricProtPol, name=u'leafs_1-2', id=u'12')
fabricNodePEp = cobra.model.fabric.NodePEp(fabricExplicitGEp, id=u'101')
fabricNodePEp2 = cobra.model.fabric.NodePEp(fabricExplicitGEp, id=u'102')
fabricRsVpcInstPol = cobra.model.fabric.RsVpcInstPol(fabricExplicitGEp, tnVpcInstPolName=u'leafs_1-2')

# build snv tenant


# commit infraInfra
c = cobra.mit.request.ConfigRequest()
#c.addMo(polUni)
c.addMo(infraInfra)
md.commit(c)

# commit snv phys domain
c = cobra.mit.request.ConfigRequest()
c.addMo(snv_phys_domain)
md.commit(c)


# commit snv l3ext domain
c = cobra.mit.request.ConfigRequest()
c.addMo(snv_l3ext_domain)
md.commit(c)


# commit the vpc configs
c = cobra.mit.request.ConfigRequest()
c.addMo(fabricProtPol)
c.addMo(vpcInstPol)
md.commit(c)


# build the snv tenant
fvTenant = cobra.model.fv.Tenant(polUni, name=u'SnV')
fvCtx = cobra.model.fv.Ctx(fvTenant, name=u'Superverse')
fvBD = cobra.model.fv.BD(fvTenant, name=u'antigravity')
fvRsCtx = cobra.model.fv.RsCtx(fvBD, tnFvCtxName=u'Superverse')
fvSubnet = cobra.model.fv.Subnet(fvBD, ip=u'10.2.10.1/23', name=u'Subnet')
vzFilter = cobra.model.vz.Filter(fvTenant, name=u'http')
vzEntry = cobra.model.vz.Entry(vzFilter, etherT=u'ip', prot=u'tcp', dFromPort=u'http', name=u'tcp-80', dToPort=u'http')
vzFilter2 = cobra.model.vz.Filter(fvTenant, name=u'https')
vzEntry2 = cobra.model.vz.Entry(vzFilter2, etherT=u'ip', prot=u'tcp', dFromPort=u'https', name=u'tcp-443', dToPort=u'https')
vzFilter3 = cobra.model.vz.Filter(fvTenant, name=u'syslog')
vzEntry3 = cobra.model.vz.Entry(vzFilter3, etherT=u'ip', prot=u'udp', dFromPort=u'514', name=u'udp-514', dToPort=u'514')
vzFilter4 = cobra.model.vz.Filter(fvTenant, name=u'sql-server')
vzEntry4 = cobra.model.vz.Entry(vzFilter4, etherT=u'ip', prot=u'tcp', dFromPort=u'1433', name=u'tcp-1433', dToPort=u'1433')
vzFilter5 = cobra.model.vz.Filter(fvTenant, name=u'mqtt')
vzEntry5 = cobra.model.vz.Entry(vzFilter5, etherT=u'ip', prot=u'tcp', dFromPort=u'1883', name=u'tcp-1883', dToPort=u'1883')
vzFilter6 = cobra.model.vz.Filter(fvTenant, name=u'sql-browser')
vzEntry6 = cobra.model.vz.Entry(vzFilter6, etherT=u'ip', prot=u'udp', dFromPort=u'1434', name=u'udp-1434', dToPort=u'1434')
vzBrCP = cobra.model.vz.BrCP(fvTenant, name=u'web-ui')
vzSubj = cobra.model.vz.Subj(vzBrCP, name=u'http')
vzRsSubjFiltAtt = cobra.model.vz.RsSubjFiltAtt(vzSubj, tnVzFilterName=u'http')
vzSubj2 = cobra.model.vz.Subj(vzBrCP, name=u'https')
vzRsSubjFiltAtt2 = cobra.model.vz.RsSubjFiltAtt(vzSubj2, tnVzFilterName=u'https')
vzBrCP2 = cobra.model.vz.BrCP(fvTenant, name=u'object-store')
vzSubj3 = cobra.model.vz.Subj(vzBrCP2, name=u'http')
vzRsSubjFiltAtt3 = cobra.model.vz.RsSubjFiltAtt(vzSubj3, tnVzFilterName=u'http')
vzSubj4 = cobra.model.vz.Subj(vzBrCP2, name=u'https')
vzRsSubjFiltAtt4 = cobra.model.vz.RsSubjFiltAtt(vzSubj4, tnVzFilterName=u'https')
vzBrCP3 = cobra.model.vz.BrCP(fvTenant, name=u'api-gateway')
vzSubj5 = cobra.model.vz.Subj(vzBrCP3, name=u'http')
vzRsSubjFiltAtt5 = cobra.model.vz.RsSubjFiltAtt(vzSubj5, tnVzFilterName=u'http')
vzSubj6 = cobra.model.vz.Subj(vzBrCP3, name=u'https')
vzRsSubjFiltAtt6 = cobra.model.vz.RsSubjFiltAtt(vzSubj6, tnVzFilterName=u'https')
vzSubj7 = cobra.model.vz.Subj(vzBrCP3, name=u'mqtt')
vzRsSubjFiltAtt7 = cobra.model.vz.RsSubjFiltAtt(vzSubj7, tnVzFilterName=u'mqtt')
vzBrCP4 = cobra.model.vz.BrCP(fvTenant, name=u'logging')
vzSubj8 = cobra.model.vz.Subj(vzBrCP4, name=u'syslog')
vzRsSubjFiltAtt8 = cobra.model.vz.RsSubjFiltAtt(vzSubj8, tnVzFilterName=u'syslog')
vzBrCP5 = cobra.model.vz.BrCP(fvTenant, name=u'message-broker')
vzSubj9 = cobra.model.vz.Subj(vzBrCP5, name=u'mqtt')
vzRsSubjFiltAtt9 = cobra.model.vz.RsSubjFiltAtt(vzSubj9, tnVzFilterName=u'mqtt')
vzBrCP6 = cobra.model.vz.BrCP(fvTenant, name=u'user-data')
vzSubj10 = cobra.model.vz.Subj(vzBrCP6, name=u'sql-server')
vzRsSubjFiltAtt10 = cobra.model.vz.RsSubjFiltAtt(vzSubj10, tnVzFilterName=u'sql-server')
vzSubj11 = cobra.model.vz.Subj(vzBrCP6, name=u'sql-browser')
vzRsSubjFiltAtt11 = cobra.model.vz.RsSubjFiltAtt(vzSubj11, tnVzFilterName=u'sql-browser')
vzSubj12 = cobra.model.vz.Subj(vzBrCP6, name=u'mqtt')
vzRsSubjFiltAtt12 = cobra.model.vz.RsSubjFiltAtt(vzSubj12, tnVzFilterName=u'mqtt')
vzBrCP7 = cobra.model.vz.BrCP(fvTenant, name=u'analytics')
vzSubj13 = cobra.model.vz.Subj(vzBrCP7, name=u'mqtt')
vzRsSubjFiltAtt13 = cobra.model.vz.RsSubjFiltAtt(vzSubj13, tnVzFilterName=u'mqtt')
fvAp = cobra.model.fv.Ap(fvTenant, name=u'Evolution_X')
fvAEPg = cobra.model.fv.AEPg(fvAp, name=u'Web-UI')
fvRsCons = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=u'api-gateway')
fvRsCons2 = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=u'object-store')
fvRsCons3 = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=u'logging')
fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]', encap=u'vlan-110')
fvRsPathAtt2 = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]', encap=u'vlan-110')
fvRsPathAtt3 = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/paths-101/pathep-[eth1/4]', encap =u'vlan-10')
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, tDn=u'uni/phys-SnV_phys')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=u'antigravity')
fvRsProv = cobra.model.fv.RsProv(fvAEPg, tnVzBrCPName=u'web-ui')
fvAEPg2 = cobra.model.fv.AEPg(fvAp, name=u'Object-Store')
fvRsCons4 = cobra.model.fv.RsCons(fvAEPg2, tnVzBrCPName=u'logging')
fvRsPathAtt3 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]', encap=u'vlan-111')
fvRsPathAtt4 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]', encap=u'vlan-111')
fvRsDomAtt2 = cobra.model.fv.RsDomAtt(fvAEPg2, tDn=u'uni/phys-SnV_phys')
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName=u'antigravity')
fvRsProv2 = cobra.model.fv.RsProv(fvAEPg2, tnVzBrCPName=u'object-store')
fvAEPg3 = cobra.model.fv.AEPg(fvAp, name=u'API-Gateway')
fvRsCons5 = cobra.model.fv.RsCons(fvAEPg3, tnVzBrCPName=u'message-broker')
fvRsCons6 = cobra.model.fv.RsCons(fvAEPg3, tnVzBrCPName=u'logging')
fvRsPathAtt5 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]', encap=u'vlan-112')
fvRsPathAtt6 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]', encap=u'vlan-112')
fvRsDomAtt3 = cobra.model.fv.RsDomAtt(fvAEPg3, tDn=u'uni/phys-SnV_phys')
fvRsBd3 = cobra.model.fv.RsBd(fvAEPg3, tnFvBDName=u'antigravity')
fvRsProv3 = cobra.model.fv.RsProv(fvAEPg3, tnVzBrCPName=u'api-gateway')
fvAEPg4 = cobra.model.fv.AEPg(fvAp, name=u'Logging')
fvRsPathAtt7 = cobra.model.fv.RsPathAtt(fvAEPg4, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]', encap=u'vlan-113')
fvRsPathAtt8 = cobra.model.fv.RsPathAtt(fvAEPg4, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]', encap=u'vlan-113')
fvRsDomAtt4 = cobra.model.fv.RsDomAtt(fvAEPg4, tDn=u'uni/phys-SnV_phys')
fvRsBd4 = cobra.model.fv.RsBd(fvAEPg4, tnFvBDName=u'antigravity')
fvRsProv4 = cobra.model.fv.RsProv(fvAEPg4, tnVzBrCPName=u'logging')
fvAEPg5 = cobra.model.fv.AEPg(fvAp, name=u'Message-Broker')
fvRsCons7 = cobra.model.fv.RsCons(fvAEPg5, tnVzBrCPName=u'api-gateway')
fvRsCons8 = cobra.model.fv.RsCons(fvAEPg5, tnVzBrCPName=u'user-data')
fvRsCons9 = cobra.model.fv.RsCons(fvAEPg5, tnVzBrCPName=u'analytics')
fvRsCons10 = cobra.model.fv.RsCons(fvAEPg5, tnVzBrCPName=u'logging')
fvRsPathAtt9 = cobra.model.fv.RsPathAtt(fvAEPg5, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]', encap=u'vlan-114')
fvRsPathAtt10 = cobra.model.fv.RsPathAtt(fvAEPg5, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]', encap=u'vlan-114')
fvRsDomAtt5 = cobra.model.fv.RsDomAtt(fvAEPg5, tDn=u'uni/phys-SnV_phys')
fvRsBd5 = cobra.model.fv.RsBd(fvAEPg5, tnFvBDName=u'antigravity')
fvRsProv5 = cobra.model.fv.RsProv(fvAEPg5, tnVzBrCPName=u'message-broker')
fvAEPg6 = cobra.model.fv.AEPg(fvAp, name=u'User-Data')
fvRsCons11 = cobra.model.fv.RsCons(fvAEPg6, tnVzBrCPName=u'message-broker')
fvRsCons12 = cobra.model.fv.RsCons(fvAEPg6, tnVzBrCPName=u'logging')
fvRsPathAtt11 = cobra.model.fv.RsPathAtt(fvAEPg6, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]', encap=u'vlan-115')
fvRsPathAtt12 = cobra.model.fv.RsPathAtt(fvAEPg6, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]', encap=u'vlan-115')
fvRsDomAtt6 = cobra.model.fv.RsDomAtt(fvAEPg6, tDn=u'uni/phys-SnV_phys')
fvRsBd6 = cobra.model.fv.RsBd(fvAEPg6, tnFvBDName=u'antigravity')
fvRsProv6 = cobra.model.fv.RsProv(fvAEPg6, tnVzBrCPName=u'user-data')
fvAEPg7 = cobra.model.fv.AEPg(fvAp, name=u'Analytics')
fvRsCons13 = cobra.model.fv.RsCons(fvAEPg7, tnVzBrCPName=u'message-broker')
fvRsCons14 = cobra.model.fv.RsCons(fvAEPg7, tnVzBrCPName=u'logging')
fvRsPathAtt13 = cobra.model.fv.RsPathAtt(fvAEPg7, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]', encap=u'vlan-116')
fvRsPathAtt14 = cobra.model.fv.RsPathAtt(fvAEPg7, tDn=u'topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]', encap=u'vlan-116')
fvRsDomAtt7 = cobra.model.fv.RsDomAtt(fvAEPg7, tDn=u'uni/phys-SnV_phys')
fvRsBd7 = cobra.model.fv.RsBd(fvAEPg7, tnFvBDName=u'antigravity')
fvRsProv7 = cobra.model.fv.RsProv(fvAEPg7, tnVzBrCPName=u'analytics')


c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)
