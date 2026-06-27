# Vendor Research Report
## SolarWinds Replacement — Enterprise Campus Network Monitoring

---

| Field | Details |
|---|---|
| **Prepared For** | KFMC Internal Evaluation |
| **Prepared By** | CodeOx · shabeeb.k@code-ox.com · +966 535 716 437 |
| **Date** | June 2026 |
| **Classification** | Internal — Not for Vendor Distribution |

---

## 1. Research Scope

This report evaluates commercially available enterprise network monitoring platforms that can replace SolarWinds NPM + NTA functionality for a campus environment with the following profile:

- **Scale:** 3,000–5,000 managed nodes, up to 100,000 interfaces
- **Deployment:** On-premises only (no cloud dependency)
- **Infrastructure:** Multi-vendor (Cisco, Juniper, HPE/Aruba, Fortinet, Palo Alto)
- **Protocols:** SNMP v2c/v3, NetFlow v9, sFlow, CDP, LLDP
- **Compliance:** Saudi Arabia NCA ECC 2018
- **Integrations:** Active Directory, ServiceNow, SMTP, SMS

---

## 2. Shortlist Overview

| Vendor | Product | Origin | Deployment | Pricing Model | Tier |
|---|---|---|---|---|---|
| Paessler AG | **PRTG Network Monitor** | Germany | On-prem / Cloud | Per-sensor perpetual or subscription | ⭐ Tier 1 |
| Zoho (ManageEngine) | **OpManager** | India / USA | On-prem | Per-device perpetual or subscription | ⭐ Tier 1 |
| Progress Software | **WhatsUp Gold** | USA | On-prem | Per-device subscription | ⭐ Tier 1 |
| Zabbix LLC | **Zabbix Enterprise** | Latvia | On-prem | Open source + paid support | ✅ Tier 2 |
| Centreon SAS | **Centreon IT Monitoring** | France | On-prem / Cloud | Subscription | ✅ Tier 2 |
| Cisco | **Catalyst Center (DNA Center)** | USA | On-prem appliance | Cisco licensing | ⚠️ Conditional |

---

## 3. Detailed Vendor Profiles

---

### 3.1 PRTG Network Monitor — Paessler AG

**Overview**

PRTG is one of the most widely deployed SolarWinds NPM alternatives in the enterprise market. Founded in 1997, Paessler has over 500,000 installations globally. The product is used extensively in healthcare, government, and large enterprise campuses.

**Product website:** paessler.com/prtg

**Feature Coverage Against BRD Requirements**

| Requirement Area | Coverage |
|---|---|
| Device discovery (SNMP, ICMP, CDP/LLDP) | ✅ Full — auto-discovery with network scanning |
| SNMP v1/v2c/v3 polling | ✅ Full |
| NetFlow / sFlow / IPFIX collection | ✅ Full — dedicated flow sensor |
| Layer 2/3 topology maps | ✅ Full — auto-generated and manual maps |
| Threshold-based alerting | ✅ Full |
| Alert escalation & maintenance windows | ✅ Full |
| Drag-and-drop dashboards | ✅ Full — Maps and dashboards |
| Scheduled PDF/Excel reports | ✅ Full |
| SLA availability reporting | ✅ Full |
| Active Directory / LDAP integration | ✅ Full |
| RBAC with custom roles | ✅ Full |
| REST API | ✅ Full — documented API |
| ServiceNow integration | ⚠️ Via webhook/REST — not native connector |
| SAML 2.0 SSO | ✅ Supported |
| HA / failover | ✅ Failover cluster (Enterprise license) |
| On-premises deployment | ✅ Windows Server primary; Linux via hosted probe |
| NCA ECC 2018 compliance tools | ⚠️ Not certified specifically; TLS, AES-256, audit logs present |

**Architecture Notes**

- Core server on Windows Server; probes (distributed polling engines) run on Windows or Linux
- Data stored in an embedded database (up to ~2,500 sensors) or Microsoft SQL Server for large deployments
- HA requires Windows failover cluster or probe redundancy setup

**Licensing Model**

- **Perpetual:** License by sensor count (each monitored metric = 1 sensor). Common starting points: 500, 1,000, 2,500, 5,000, XL (unlimited) sensors
- **Subscription (PRTG Hosted Monitor):** Cloud-hosted option — not suitable per on-prem constraint
- **Typical enterprise cost (5,000 sensors, perpetual):** ~USD 15,000–25,000 one-time + 25% annual maintenance
- Unlimited sensor license (PRTG XL) available for large deployments

**Strengths**
- Most intuitive UI in the category — fastest time-to-value from SolarWinds migration
- Extremely comprehensive out-of-the-box sensor library (200+ sensor types)
- Strong community and documentation
- Flexible sensor model means almost any metric can be monitored
- Active product development with frequent releases

**Weaknesses**
- Sensor-based licensing can become expensive at scale when all interfaces are monitored
- Windows Server primary deployment (Linux support is partial via remote probes)
- No native ServiceNow connector — requires webhook configuration
- Flow analysis (NetFlow/sFlow) is included but less feature-rich than dedicated tools like ManageEngine NFA

**Recommendation for KFMC**

PRTG is the **strongest candidate for ease of migration from SolarWinds** and will have the lowest learning curve for the NOC team. For a 3,000-node campus with ~80,000 interfaces, the sensor count will be significant — Paessler's XL (unlimited) or Enterprise license is recommended to avoid per-sensor cost management.

---

### 3.2 ManageEngine OpManager — Zoho Corporation

**Overview**

OpManager is ManageEngine's flagship network monitoring product. It has the most direct feature parity with SolarWinds NPM + NTA of any commercial alternative. ManageEngine has a strong presence in the Middle East and GCC region with local resellers and support. Part of the Zoho ecosystem (38 years old, 100M+ users globally).

**Product website:** manageengine.com/network-monitoring/

**Feature Coverage Against BRD Requirements**

| Requirement Area | Coverage |
|---|---|
| Device discovery (SNMP, ICMP, CDP/LLDP) | ✅ Full |
| SNMP v1/v2c/v3 polling | ✅ Full |
| NetFlow / sFlow / IPFIX collection | ✅ Full — NetFlow Analyzer (bundled in Enterprise) |
| Layer 2/3 topology maps | ✅ Full — Layer 2 maps, 3D floor view |
| Threshold-based alerting | ✅ Full |
| Alert escalation & maintenance windows | ✅ Full |
| Drag-and-drop dashboards | ✅ Full |
| Scheduled PDF/Excel reports | ✅ Full — 100+ out-of-box reports |
| SLA availability reporting | ✅ Full |
| Active Directory / LDAP integration | ✅ Full |
| RBAC with custom roles | ✅ Full |
| REST API | ✅ Full |
| ServiceNow integration | ✅ Native certified connector available |
| SAML 2.0 SSO | ✅ Supported |
| HA / failover | ✅ High Availability edition available |
| On-premises deployment | ✅ Windows Server + Linux (RHEL/Ubuntu) |
| NCA ECC 2018 compliance | ⚠️ Not formally certified; encryption and audit logging controls present; review required |

**Architecture Notes**

- Deployable on Windows Server or Linux (RHEL/Ubuntu)
- Supports distributed polling probes for large environments
- Ships with PostgreSQL; supports MS SQL for enterprise deployments
- Separate add-on: **NetFlow Analyzer** (for flow analysis) — often bundled in Enterprise edition
- **OpManager Plus** bundles: OpManager + NetFlow Analyzer + IP Address Manager + Switch Port Mapper — directly mirrors SolarWinds Orion suite approach

**Licensing Model**

- **Per-device perpetual or annual subscription**
- OpManager Standard, Professional, and Enterprise editions
- OpManager Enterprise (for 1,000+ devices): ~USD 10,000–35,000 depending on device count
- NetFlow Analyzer: separate license if not on OpManager Plus
- High Availability add-on: additional cost
- **Free evaluation:** Full feature trial up to 30 devices

**Strengths**
- Most complete feature parity with SolarWinds NPM + NTA — least configuration effort post-migration
- Native ServiceNow integration (certified connector)
- Linux server deployment fully supported — no Windows Server dependency
- Strong GCC/KSA regional presence — local resellers and Arabic-speaking support
- OpManager Plus mirrors the Orion bundle concept — familiar procurement model for organizations coming off SolarWinds
- Competitively priced vs. SolarWinds and PRTG at scale

**Weaknesses**
- UI is more complex than PRTG — steeper initial learning curve
- Large feature set can make initial configuration feel overwhelming
- Some advanced features require add-ons that increase TCO
- NetFlow Analyzer is technically a separate product bundled at Enterprise tier

**Recommendation for KFMC**

ManageEngine OpManager is CodeOx's **primary recommendation** for KFMC. It has the highest functional coverage against the BRD requirements, the strongest SolarWinds feature parity, the best regional support in GCC, and the native ServiceNow connector eliminates a key integration risk. **OpManager Plus** should be evaluated as the procurement bundle.

---

### 3.3 WhatsUp Gold — Progress Software

**Overview**

WhatsUp Gold is a long-established (30+ years) direct competitor to SolarWinds NPM. Progress Software acquired WhatsUp Gold in 2010. It has a strong install base in US/UK enterprise environments and is gaining traction in the Middle East.

**Product website:** whatsupgold.com

**Feature Coverage Against BRD Requirements**

| Requirement Area | Coverage |
|---|---|
| Device discovery (SNMP, ICMP, CDP/LLDP) | ✅ Full |
| SNMP v1/v2c/v3 polling | ✅ Full |
| NetFlow / sFlow / IPFIX collection | ✅ Full — built-in flow monitoring |
| Layer 2/3 topology maps | ✅ Full — automated network maps |
| Threshold-based alerting | ✅ Full |
| Alert escalation & maintenance windows | ✅ Full |
| Drag-and-drop dashboards | ✅ Full |
| Scheduled reports | ✅ Full |
| SLA availability reporting | ✅ Full |
| Active Directory / LDAP integration | ✅ Full |
| RBAC with custom roles | ✅ Full |
| REST API | ✅ Full |
| ServiceNow integration | ⚠️ Via REST webhook |
| SAML 2.0 SSO | ✅ Supported |
| HA / failover | ✅ Available |
| On-premises deployment | ✅ Windows Server |
| NCA ECC 2018 | ⚠️ Not certified; controls present |

**Architecture Notes**

- **Windows Server only** — no native Linux server deployment
- Microsoft SQL Server required for production deployments (not bundled)
- Distributed polling via WhatsUp Gold Remote Site

**Licensing Model**

- Annual subscription per device
- WhatsUp Gold Total Plus (all modules bundled): ~USD 8,000–20,000/year depending on device count
- Free 14-day trial

**Strengths**
- Clean, modern UI with strong dashboard capabilities
- Long track record as SolarWinds NPM direct competitor
- Good flow analysis built into base product
- Strong alerting engine with dependency-aware suppression

**Weaknesses**
- **Windows Server only** — significant constraint if KFMC prefers Linux deployment
- Smaller ecosystem and community compared to PRTG or ManageEngine
- Limited GCC regional presence — support may be EMEA-routed
- Less commonly used in healthcare or large-scale MENA enterprise environments

**Recommendation for KFMC**

WhatsUp Gold is a solid platform but the Windows-only deployment and limited regional support presence are concerns for KFMC. Recommended as a **Tier 3 evaluation candidate** if PRTG and OpManager do not meet commercial requirements.

---

### 3.4 Zabbix Enterprise — Zabbix LLC

**Overview**

Zabbix is an open-source enterprise monitoring platform founded in 2001. The core product is free under the GPL license; Zabbix LLC sells commercial support, professional services, and certified training. It is massively scalable and widely deployed in large enterprise environments globally.

**Product website:** zabbix.com

**Feature Coverage Against BRD Requirements**

| Requirement Area | Coverage |
|---|---|
| Device discovery (SNMP, ICMP, CDP/LLDP) | ✅ Full — network discovery rules |
| SNMP v1/v2c/v3 polling | ✅ Full |
| NetFlow / sFlow / IPFIX collection | ⚠️ Not native — requires external collector (ntopng, pmacct) integration |
| Layer 2/3 topology maps | ✅ Improved in Zabbix 7.x — network maps with live status |
| Threshold-based alerting | ✅ Full — trigger-based alert engine |
| Alert escalation & maintenance windows | ✅ Full |
| Drag-and-drop dashboards | ✅ Full — widget-based dashboards |
| Scheduled reports | ✅ Supported in 6.x+ (PDF scheduled reports) |
| SLA availability reporting | ✅ Full — SLA module built in |
| Active Directory / LDAP integration | ✅ Full |
| RBAC with custom roles | ✅ Full |
| REST API | ✅ Full — mature JSON-RPC API |
| ServiceNow integration | ⚠️ Via media type / webhook; community templates exist |
| SAML 2.0 SSO | ✅ Supported |
| HA / failover | ✅ Native HA since Zabbix 6.0 |
| On-premises deployment | ✅ Linux (primary), Windows (proxy only) |
| NCA ECC 2018 | ⚠️ Not certified; encryption, audit, and RBAC controls present |

**Architecture Notes**

- Linux server (RHEL, Ubuntu, Debian) — Windows server NOT supported
- Database: MySQL, PostgreSQL, TimescaleDB (recommended for large scale), Oracle
- TimescaleDB extension dramatically improves performance at 100K+ metrics
- Distributed monitoring via Zabbix Proxy — no per-proxy licensing cost
- Native HA since version 6.0 (2022)

**Licensing Model**

- **Software: Free (GPL)** — no per-node or per-interface cost ever
- **Commercial support:** Annual subscription — Zabbix Enterprise Support; pricing based on nodes (typically USD 2,000–15,000/year for large deployments)
- **Professional services:** Quoted separately for implementation
- **Lowest 3-year TCO** of all vendors evaluated — primarily implementation and support costs only

**Strengths**
- **Zero software licensing cost** — dramatically lower TCO vs. all commercial alternatives
- Extremely scalable — proven deployments at 100K+ hosts
- Highly customizable monitoring — can monitor anything via custom items
- Strong community (templates, plugins) including healthcare-specific templates
- Native Linux deployment — aligns with KFMC server OS preferences
- Active development (Zabbix 7.x actively released)

**Weaknesses**
- **No native NetFlow/sFlow analysis** — requires external tool integration (ntopng, ElasticFlow, or Grafana-based stack) which adds deployment complexity
- Higher initial setup effort — not plug-and-play like PRTG or OpManager
- Web UI is functional but less polished than commercial alternatives
- Commercial support quality varies by region; MENA coverage should be verified
- Requires Linux server administration skills

**Recommendation for KFMC**

Zabbix is the **best long-term cost option** and strongest for scalability. The critical gap is **flow analysis** — this must be solved with an integration (ntopng is the most common companion). Recommended if KFMC has a strong Linux/infrastructure team and wants to minimize licensing costs. CodeOx recommends **Zabbix + ntopng** as a combined stack for the full SolarWinds NPM + NTA replacement at lowest TCO.

---

### 3.5 Centreon IT Monitoring — Centreon SAS

**Overview**

Centreon is a French monitoring platform with roots in the open-source Nagios ecosystem. The enterprise edition (Centreon IT Edition) is a commercial product targeting large enterprise and service provider environments. Growing presence in Europe and Middle East.

**Product website:** centreon.com

**Feature Coverage Against BRD Requirements**

| Requirement Area | Coverage |
|---|---|
| Device discovery (SNMP, ICMP) | ✅ Full |
| SNMP v1/v2c/v3 polling | ✅ Full |
| NetFlow / sFlow / IPFIX | ⚠️ Via Centreon MAP integration — not native |
| Topology maps | ✅ Centreon MAP module (paid add-on) |
| Threshold alerting | ✅ Full |
| Alert escalation | ✅ Full |
| Dashboards & reporting | ✅ Full |
| AD/LDAP + SAML | ✅ Full |
| RBAC | ✅ Full |
| REST API | ✅ Full |
| HA | ✅ Supported |
| On-premises | ✅ Linux |

**Recommendation for KFMC**

Centreon is a capable platform but flow analysis is not native and topology maps require an additional paid module. It lacks the GCC regional presence of ManageEngine or the simplicity of PRTG. **Recommended as fallback Tier 2** only if primary vendors cannot meet commercial requirements.

---

### 3.6 Cisco Catalyst Center (formerly DNA Center)

**Overview**

Cisco Catalyst Center is Cisco's network automation and assurance platform for campus and branch networks. It provides deep visibility specifically for Cisco infrastructure.

**Key Consideration**

Catalyst Center is purpose-built for Cisco environments and provides superior visibility for Cisco switches, routers, and wireless. However:

- Requires a physical or virtual Cisco appliance (significant hardware cost)
- Monitoring non-Cisco devices (Juniper, Fortinet, Palo Alto) is limited
- Designed as a **network management and automation** tool, not a pure monitoring platform
- Does not natively replace SolarWinds NTA (flow analysis module)

**Recommendation for KFMC**

**Conditional recommendation** — suitable only if KFMC's campus network is predominantly Cisco (>80% of devices). If the environment is genuinely multi-vendor, Catalyst Center will leave significant monitoring gaps. Could be deployed **alongside** a platform like OpManager (OpManager monitors Catalyst Center-managed Cisco devices via SNMP while Catalyst Center handles Cisco-specific automation).

---

## 4. Comparison Matrix

### 4.1 Feature Coverage

| Feature | PRTG | OpManager | WhatsUp Gold | Zabbix | Centreon |
|---|---|---|---|---|---|
| SNMP v3 | ✅ | ✅ | ✅ | ✅ | ✅ |
| NetFlow native | ✅ | ✅ | ✅ | ❌ | ❌ |
| Auto topology maps | ✅ | ✅ | ✅ | ✅ | ⚠️ Add-on |
| Drag-and-drop dashboards | ✅ | ✅ | ✅ | ✅ | ✅ |
| SLA reporting | ✅ | ✅ | ✅ | ✅ | ✅ |
| AD/LDAP SSO | ✅ | ✅ | ✅ | ✅ | ✅ |
| SAML 2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| ServiceNow native | ❌ | ✅ | ❌ | ❌ | ❌ |
| REST API | ✅ | ✅ | ✅ | ✅ | ✅ |
| Linux server deployment | ⚠️ Partial | ✅ | ❌ | ✅ | ✅ |
| HA / failover | ✅ | ✅ | ✅ | ✅ | ✅ |
| Alert dependency suppression | ✅ | ✅ | ✅ | ✅ | ✅ |
| Custom MIB import | ✅ | ✅ | ✅ | ✅ | ✅ |

### 4.2 Commercial & Strategic

| Attribute | PRTG | OpManager | WhatsUp Gold | Zabbix | Centreon |
|---|---|---|---|---|---|
| GCC/KSA regional support | ⚠️ EMEA routed | ✅ Local resellers | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited |
| Software license cost | Medium | Medium | Medium | **Free** | Medium |
| Estimated 3yr TCO (3K nodes) | ~USD 60K | ~USD 45K | ~USD 55K | ~USD 20K | ~USD 50K |
| Ease of SolarWinds migration | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Time-to-value (deployment) | Fast | Medium | Medium | Slower | Medium |
| Market maturity | High | High | High | Very High | Medium |
| Healthcare sector references | Medium | High | Low | High | Medium |

*TCO estimates are indicative; vendor quotes required for accurate figures.*

---

## 5. CodeOx Recommendations

### Primary Recommendation: ManageEngine OpManager Plus

**Why:** Highest functional parity with SolarWinds, includes NetFlow analysis in a single bundle, native ServiceNow integration, proven GCC/KSA presence with local resellers, supports Linux deployment. Most straightforward migration from SolarWinds for KFMC's NOC team.

**Action:** Request a full demo from ManageEngine ME/GCC reseller and issue the BRD for formal proposal.

---

### Alternative #1: PRTG Network Monitor (Paessler)

**Why:** Best user experience and fastest time-to-value. If KFMC prioritizes NOC operator adoption speed and has a tight transition timeline, PRTG will have the lowest friction from SolarWinds migration. Unlimited sensor license (PRTG XL or Enterprise) is the right SKU for this scale.

**Action:** Request PRTG XL/Enterprise pricing for 100,000 sensor capacity and 30-day POC license.

---

### Alternative #2: Zabbix + ntopng (Lowest TCO)

**Why:** If KFMC has budget pressure and a capable Linux/infrastructure team, this stack eliminates all software licensing costs. Zabbix handles SNMP polling, alerting, dashboards, and topology; ntopng provides the flow analysis layer. Combined 3-year TCO primarily covers implementation services and support.

**Action:** Only recommend to KFMC if budget is a primary constraint and team has Linux operations capability.

---

### Recommended Shortlist for POC

1. ManageEngine OpManager Plus
2. PRTG Network Monitor (Enterprise/XL)
3. Zabbix + ntopng (if budget-driven)

---

## 6. Next Steps

| # | Action | Owner | Timeline |
|---|---|---|---|
| 1 | Share BRD with shortlisted vendors (ManageEngine, PRTG, WhatsUp Gold) | CodeOx | Week 1 |
| 2 | Collect vendor proposal responses per BRD Section 16 | Vendors | Weeks 2–3 |
| 3 | Score proposals against evaluation criteria (BRD Section 11) | CodeOx + KFMC IT | Week 4 |
| 4 | Schedule live demos with top 2 vendors | CodeOx | Week 5 |
| 5 | Issue POC plan and initiate 30-day POC with selected vendor | All parties | Weeks 6–10 |
| 6 | UAT sign-off and commercial negotiation | KFMC + CodeOx | Week 11–12 |
| 7 | Contract award and kickoff | KFMC | Week 13 |

---

*Prepared by CodeOx · June 2026*
*![CodeOx](https://code-ox.com/codeoxlogo.svg) · shabeeb.k@code-ox.com · +966 535 716 437*
