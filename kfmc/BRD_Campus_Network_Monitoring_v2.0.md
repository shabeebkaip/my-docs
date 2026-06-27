# Business Requirements Document
## Enterprise Campus Network Monitoring System — Vendor Procurement

---

| Field | Details |
|---|---|
| **Document Title** | Enterprise Campus Network Monitoring System — BRD |
| **Version** | 2.0 |
| **Status** | Final — For Vendor Distribution |
| **Client Organization** | King Faisal Medical City (KFMC) |
| **Prepared By** | CodeOx · shabeeb.k@code-ox.com · +966 535 716 437 |
| **Date** | June 2026 |
| **Classification** | Confidential — Vendor Use Only |

---

## Document Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | May 2026 | Business Analysis Team | Initial internal draft |
| 2.0 | June 2026 | CodeOx | Revised for vendor distribution — reframed as procurement BRD, added evaluation criteria, commercial requirements, and vendor response instructions |

---

## Table of Contents

1. Executive Summary
2. Organization & Current Environment
3. Business Problem Statement
4. Project Objectives & Success Metrics
5. Scope
6. Stakeholders
7. Functional Requirements
8. Non-Functional Requirements
9. Technical Environment
10. Compliance & Regulatory Requirements
11. Vendor Evaluation Criteria
12. Commercial & Licensing Requirements
13. Implementation & Support Requirements
14. Acceptance Criteria
15. Risks & Constraints
16. Vendor Response Instructions
17. Appendix A — Priority Key
18. Appendix B — Glossary

---

## 1. Executive Summary

King Faisal Medical City (KFMC) operates a large-scale enterprise campus network serving clinical, administrative, and research functions across multiple facilities. The organization's current network monitoring contract with SolarWinds is being discontinued, and KFMC is actively seeking a replacement platform of equivalent or superior capability.

This Business Requirements Document (BRD) defines the full scope of functional requirements, non-functional requirements, integration needs, compliance obligations, and commercial expectations for the procured solution. Vendors are invited to respond to this document with a formal proposal demonstrating how their product meets each stated requirement.

The selected solution must provide complete, real-time visibility into network infrastructure health, performance, and availability — supporting IT operations, the NOC, and executive reporting — all from a centralized, web-based management console deployed on-premises within KFMC's data center environment.

---

## 2. Organization & Current Environment

### 2.1 About the Organization

KFMC is a healthcare institution operating an enterprise-grade network infrastructure that spans campus buildings, data centers, and clinical zones. The network consists of multi-vendor hardware including Cisco, Juniper, HPE/Aruba, Fortinet, and Palo Alto devices.

### 2.2 Current Monitoring Environment

| Attribute | Current State |
|---|---|
| **Existing Platform** | SolarWinds (NPM + NTA modules) |
| **Contract Status** | Ending — active replacement search |
| **Approximate Scale** | Up to 3,000 monitored nodes; up to 80,000 monitored interfaces |
| **Deployment Model** | On-premises, Windows Server |
| **Active Integrations** | Active Directory (AD), Email notifications, SNMP traps |
| **Primary Users** | Network Operations Center (NOC) team, Network Engineering, IT Management |

### 2.3 Drivers for Change

- End of commercial agreement with SolarWinds
- Need for a solution with a lower total cost of ownership (TCO)
- Requirement for long-term vendor stability and active product roadmap
- Desire to eliminate single-vendor lock-in for network observability

---

## 3. Business Problem Statement

Without a unified, real-time network monitoring platform, KFMC's IT Operations team faces the following operational risks:

- **Reactive incident response:** Outages and degradations are detected by end-user complaints rather than proactive alerting, extending Mean Time to Resolution (MTTR)
- **Monitoring blind spots:** Distributed, multi-vendor infrastructure produces fragmented visibility with no single pane of glass
- **No root cause correlation:** Performance degradation cannot be systematically traced to its origin across Layer 2/3 without automated dependency mapping
- **Absent capacity planning:** Without trending data and forecasting, bandwidth saturation and hardware refresh decisions are reactive
- **Compliance reporting gaps:** Uptime SLA reports, audit trails, and availability metrics must be generated manually
- **Flow analysis limitations:** Inability to identify top bandwidth consumers, rogue applications, or abnormal traffic patterns in real time

The procured solution must close all of these gaps within the first six months of deployment.

---

## 4. Project Objectives & Success Metrics

### 4.1 Strategic Objectives

| # | Objective |
|---|---|
| O-01 | Achieve 100% visibility across all monitored campus network infrastructure within 60 days of go-live |
| O-02 | Reduce MTTR by at least 35% within 90 days of go-live through proactive alerting and automated root cause correlation |
| O-03 | Eliminate dependency on SolarWinds with no monitoring gap during transition |
| O-04 | Establish automated SLA and compliance reporting to replace current manual processes |
| O-05 | Enable scalable growth in monitored device count without platform re-procurement |

### 4.2 Key Performance Indicators

| KPI | Target |
|---|---|
| Device discovery coverage | ≥ 98% of all managed devices discovered within 48 hours of deployment |
| Alert-to-notification latency | ≤ 60 seconds from threshold breach to notification delivery |
| Dashboard availability | 99.9% uptime for the monitoring console |
| NOC adoption | 100% of NOC operators trained and actively using the platform within 30 days |
| MTTR reduction | ≥ 35% reduction vs. baseline within 90 days |

---

## 5. Scope

### 5.1 In Scope

- Network device discovery, inventory, and classification (routers, switches, firewalls, access points, servers)
- Real-time SNMP-based polling of device status, CPU, memory, and interface-level metrics
- NetFlow / sFlow / IPFIX traffic collection and analysis
- Automated Layer 2 and Layer 3 topology discovery and map generation
- Threshold-based and anomaly-based alerting with escalation and suppression policies
- Web-based dashboard designer and pre-built NOC/executive dashboards
- Scheduled and on-demand report generation (PDF, Excel, HTML)
- Role-based access control (RBAC) with Active Directory / LDAP integration
- REST API for programmatic access and third-party ITSM integration
- High-availability (HA) deployment architecture
- Multi-vendor device support

### 5.2 Out of Scope

- Application Performance Monitoring (APM) — separate procurement
- Log aggregation and SIEM/SOAR functionality
- Configuration backup and change management (NCM)
- Endpoint or agent-based security monitoring
- SD-WAN or SASE-specific monitoring (future phase)
- Mobile native applications

### 5.3 Assumptions

- KFMC will provide access to a representative test network segment during the Proof of Concept (POC) phase
- Third-party MIB files for non-standard devices will be sourced by KFMC's network engineering team with vendor support
- Integration with existing ITSM (e.g., ServiceNow) is via standard webhook or REST API — no deep custom connector development is in scope
- The vendor is responsible for providing a full bill of materials (BOM) for hardware and software licensing

### 5.4 Constraints

| Constraint | Details |
|---|---|
| Deployment model | On-premises only; no mandatory cloud dependency |
| Data residency | All monitoring data must remain within KFMC's on-premises environment |
| Browser support | Chrome, Firefox, Edge (Chromium), and Safari (latest 2 major versions) |
| Regulatory compliance | Must comply with Saudi Arabia NCA ECC 2018 controls applicable to network monitoring tools |
| Transition timeline | No monitoring gap tolerated; parallel run with SolarWinds during cutover |

---

## 6. Stakeholders

| Stakeholder | Role | Responsibility | Engagement Level |
|---|---|---|---|
| IT Operations Director | Primary Sponsor | Approve requirements and budget; final sign-off | High |
| Network Engineering Team | Subject Matter Expert | Validate monitoring requirements and device coverage | High |
| NOC Manager | End User Representative | Define alerting workflows, dashboard needs, and NOC workflows | High |
| IT Security Team | Reviewer | Validate access control, data security, and compliance requirements | Medium |
| CodeOx | Procurement Facilitator | Coordinate vendor evaluation, requirement alignment, and selection | High |
| Executive Leadership | Executive Sponsor | Final investment decision | Low |

---

## 7. Functional Requirements

Requirements are classified by priority: **Must Have (M)**, **Should Have (S)**, **Could Have (C)**.

### 7.1 Device Discovery & Inventory

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Perform automated ICMP ping sweep across user-defined IP ranges or CIDR subnets to discover all live hosts | M |
| FR-02 | Poll and manage devices via SNMP v1, v2c, and v3 with support for configurable community strings and v3 credentials (auth + priv) | M |
| FR-03 | Use CDP (Cisco Discovery Protocol) and LLDP to discover adjacent network devices and build neighbor tables automatically | M |
| FR-04 | Import and parse custom MIB files to extend monitoring to proprietary or niche device types | S |
| FR-05 | Auto-classify discovered devices by type: router, switch, firewall, server, wireless access point, printer, UPS | M |
| FR-06 | Schedule recurring discovery scans (hourly, daily, weekly) with delta reporting showing newly added and removed devices | M |
| FR-07 | Provide a live device inventory view with filterable columns: device name, IP, type, vendor, OS version, status, last polled | M |
| FR-08 | Support bulk import of devices via CSV for large-scale on-boarding | S |

### 7.2 Real-Time Performance Monitoring

| ID | Requirement | Priority |
|---|---|---|
| FR-10 | Poll device CPU and memory utilization via SNMP at configurable intervals (default: 60 seconds; minimum: 30 seconds) | M |
| FR-11 | Monitor interface-level metrics per port: bandwidth utilization (in/out), error rate, discard rate, packet loss | M |
| FR-12 | Display real-time up/down status with color-coded indicators: green (up), red (down), yellow (warning), grey (unknown) | M |
| FR-13 | Calculate and display device response time (latency) via ICMP round-trip time per device | M |
| FR-14 | Retain raw performance data for a minimum of 90 days; aggregated hourly/daily data for at least 2 years | M |
| FR-15 | Support WMI polling for Windows servers to retrieve OS-level metrics: disk I/O, service status, process CPU | S |
| FR-16 | Support SNMP trap reception and correlation with polled device state | M |
| FR-17 | Display interface utilization heat maps or trend sparklines within device detail views | S |

### 7.3 Network Traffic Analysis (Flow)

| ID | Requirement | Priority |
|---|---|---|
| FR-20 | Receive and parse NetFlow v5/v9, sFlow v5, and IPFIX flow records from network devices (UDP listener, configurable port, default 2055) | M |
| FR-21 | Classify traffic by application using NBAR or deep packet inspection (DPI) signatures and display top-N applications by bandwidth | M |
| FR-22 | Display top talkers by source IP, destination IP, protocol, and port number with conversation-level drill-down | M |
| FR-23 | Provide historical flow analysis with selectable time ranges: last 1h, 6h, 24h, 7d, 30d, and custom range | M |
| FR-24 | Alert on bandwidth utilization thresholds per interface or aggregate circuit capacity | M |
| FR-25 | Support per-VLAN and per-subnet traffic breakdown | S |
| FR-26 | Identify and flag anomalous traffic patterns (e.g., port scans, bandwidth spikes) | S |

### 7.4 Topology Discovery & Mapping

| ID | Requirement | Priority |
|---|---|---|
| FR-30 | Auto-generate Layer 2 topology maps using CDP/LLDP neighbor discovery data without manual input | M |
| FR-31 | Generate Layer 3 routing topology maps using OSPF/BGP routing tables retrieved via SNMP | S |
| FR-32 | Overlay live device health status on topology maps using color-coded status indicators | M |
| FR-33 | Allow administrators to create custom network maps with drag-and-drop device placement and optional background floor plan images | M |
| FR-34 | Export topology maps as PNG, PDF, or SVG | S |
| FR-35 | Display link utilization levels on topology map edges with color graduation (green/amber/red) | M |
| FR-36 | Enable topology map drill-down — clicking a device opens its detail/performance view | M |

### 7.5 Alerting & Notification Engine

| ID | Requirement | Priority |
|---|---|---|
| FR-40 | Define threshold-based alerts on any monitored metric: CPU %, memory %, interface utilization %, packet loss, device up/down | M |
| FR-41 | Support multi-condition alert rules using AND/OR boolean logic across multiple metrics and device groups | M |
| FR-42 | Deliver alert notifications via: email (SMTP), SMS (via HTTP gateway), webhook (outbound JSON POST), and SNMP trap forwarding | M |
| FR-43 | Support alert escalation policies — if unacknowledged within a configurable time window, automatically escalate to the next responsible tier | S |
| FR-44 | Provide maintenance windows (one-time and recurring schedules) that automatically suppress alerts for planned downtime | M |
| FR-45 | Correlate dependent alerts — suppress child device alerts when an upstream parent device is confirmed down (root cause suppression) | M |
| FR-46 | Allow alert acknowledgement, annotation, and assignment to operators from within the console | M |
| FR-47 | Provide an alert history log with search, filter, and export capability | M |
| FR-48 | Support alert deduplication to prevent notification flooding for flapping devices | M |

### 7.6 Dashboards & Reporting

| ID | Requirement | Priority |
|---|---|---|
| FR-50 | Provide a drag-and-drop dashboard builder with pre-built widget types: gauge, line chart, bar chart, data table, topology map tile, and status summary | M |
| FR-51 | Deliver out-of-the-box dashboards: Executive Summary, NOC Real-Time Overview, Interface Detail, Top-10 Bandwidth Users, Device Health Summary | M |
| FR-52 | Generate scheduled reports delivered via email in PDF, Excel, and HTML formats | M |
| FR-53 | Provide SLA availability reporting per device or device group over configurable date ranges, showing: uptime %, MTTR, MTBF, downtime events | M |
| FR-54 | Support capacity planning reports that trend current utilization and project when thresholds will be exceeded (at minimum, linear trend) | S |
| FR-55 | Allow report templates to be saved and shared across user accounts | S |
| FR-56 | Support dashboard sharing via a read-only public URL or embedded iFrame (NOC wall display use case) | S |

### 7.7 Access Control & User Management

| ID | Requirement | Priority |
|---|---|---|
| FR-60 | Implement RBAC with built-in roles: Administrator, Operator, Read-Only; plus support for custom role creation with granular permission assignment | M |
| FR-61 | Integrate with Microsoft Active Directory and LDAP for user authentication and group-to-role mapping | M |
| FR-62 | Support SAML 2.0 for single sign-on (SSO) integration | S |
| FR-63 | Enforce organizational unit-based device visibility scoping — users only see devices within their assigned scope | M |
| FR-64 | Record all user actions in a tamper-evident audit log: login/logout, configuration changes, alert acknowledgements, report generation | M |
| FR-65 | Support account lockout policy after configurable number of failed login attempts | M |

### 7.8 API & External Integration

| ID | Requirement | Priority |
|---|---|---|
| FR-70 | Expose a documented REST API (JSON) for programmatic read/write access to devices, alerts, metrics, and configuration | M |
| FR-71 | Support outbound webhook triggers on alert state changes (open, acknowledged, resolved) | M |
| FR-72 | Provide a native or documented integration with ServiceNow for automatic incident creation on critical alerts | S |
| FR-73 | Receive syslog messages from network devices and correlate with polled device state | S |
| FR-74 | Support SNMP trap reception from managed devices | M |

---

## 8. Non-Functional Requirements

### 8.1 Performance

| ID | Requirement | Target |
|---|---|---|
| NFR-01 | Dashboard load time for standard views with up to 500 devices | < 3 seconds |
| NFR-02 | Full polling cycle duration for 10,000 monitored interfaces | < 60 seconds |
| NFR-03 | NetFlow/sFlow/IPFIX record ingestion and processing throughput | ≥ 100,000 flows/second |
| NFR-04 | Alert trigger latency from threshold breach to notification delivery | < 60 seconds |
| NFR-05 | Search or filter response time across full device inventory | < 2 seconds |

### 8.2 Scalability

| ID | Requirement |
|---|---|
| NFR-10 | Must support at least 5,000 monitored nodes and 100,000 monitored interfaces in a single deployment instance |
| NFR-11 | Distributed polling architecture must support horizontal scaling by adding additional polling engines with no platform re-installation |
| NFR-12 | Database architecture must maintain query performance as historical data grows beyond 1 TB |
| NFR-13 | Must support at least 50 concurrent authenticated web console users without performance degradation |

### 8.3 Availability & Reliability

| ID | Requirement |
|---|---|
| NFR-20 | Platform shall maintain 99.9% uptime for the monitoring console (< 8.76 hours unplanned downtime per year) |
| NFR-21 | High-availability (hot-standby) configuration must achieve failover within 60 seconds with no data loss |
| NFR-22 | All configuration and historical data must be backed up daily with a minimum 30-day backup retention |
| NFR-23 | Distributed polling engines must continue collecting data independently if the central server is temporarily unreachable |

### 8.4 Security

| ID | Requirement |
|---|---|
| NFR-30 | All web console traffic must be served over HTTPS (TLS 1.2 minimum; TLS 1.3 preferred) |
| NFR-31 | SNMP v3 credentials must be stored encrypted at rest (AES-256 minimum) |
| NFR-32 | User passwords must be stored using a strong one-way hashing algorithm (bcrypt or Argon2) |
| NFR-33 | Session timeout after 30 minutes of inactivity (administrator-configurable) |
| NFR-34 | The platform must have undergone a third-party OWASP Top 10 vulnerability assessment within the past 24 months; report to be provided on request |
| NFR-35 | No monitoring data, device credentials, or telemetry shall be transmitted to any external cloud service |

### 8.5 Usability

| ID | Requirement |
|---|---|
| NFR-40 | Web console must be fully functional on Chrome, Firefox, Edge (Chromium), and Safari (latest 2 major versions) |
| NFR-41 | UI must be responsive and functional at 1280×800 minimum screen resolution |
| NFR-42 | A new administrator must be able to complete initial device discovery and begin receiving alerts within 4 hours of installation |
| NFR-43 | The vendor must provide in-product contextual help or a searchable knowledge base accessible from within the console |

---

## 9. Technical Environment

### 9.1 Current Network Infrastructure

| Category | Details |
|---|---|
| **Network Vendors** | Cisco (primary), Juniper, HPE/Aruba, Fortinet, Palo Alto |
| **Protocols in use** | SNMP v2c/v3, OSPF, BGP, CDP, LLDP |
| **Flow Export** | NetFlow v9 (Cisco), sFlow (HPE/Aruba) |
| **Authentication** | Microsoft Active Directory |
| **ITSM Platform** | ServiceNow |
| **Operating Systems (servers)** | Windows Server 2019/2022, RHEL 8/9, Ubuntu 22.04 LTS |

### 9.2 Deployment Requirements

- **Deployment model:** On-premises only; cloud-connected SaaS models are not acceptable
- **Supported server OS:** Windows Server 2019/2022 and/or Linux (RHEL 8/9 or Ubuntu 22.04 LTS)
- **Virtualization:** VMware vSphere; vendor must confirm VM deployment support and provide resource specifications (vCPU, RAM, storage)
- **High availability:** Active-passive HA is required; vendor must describe the HA architecture in their response
- **Database:** Vendor must describe the embedded or external database engine and provide storage sizing guidance

### 9.3 Integration Points

| System | Integration Type | Requirement |
|---|---|---|
| Microsoft Active Directory | LDAP/LDAPS | User authentication and role mapping |
| ServiceNow | REST webhook outbound | Auto-create incidents from critical alerts |
| Email Server | SMTP with TLS | Alert notifications and scheduled report delivery |
| SMS Gateway | HTTP API | Critical alert SMS via third-party gateway |
| Syslog | UDP/TCP | Receive device syslog events |
| External APIs | REST (JSON) | Programmatic read access for third-party tooling |

---

## 10. Compliance & Regulatory Requirements

All aspects of the solution — including data storage, access control, encryption, and audit logging — must comply with the following:

| Regulation / Standard | Relevance |
|---|---|
| **Saudi Arabia NCA ECC 2018** | National Cybersecurity Authority Essential Cybersecurity Controls — governs monitoring tool data handling, access management, and encryption |
| **HIPAA (where applicable)** | KFMC handles patient data; network monitoring systems must not inadvertently capture or expose PHI |
| **ISO/IEC 27001** | Vendor must confirm that their development and delivery processes are ISO 27001 certified or in progress |
| **GDPR (informational)** | Applicable to any data processed on behalf of non-KSA entities; vendor must clarify scope |

Vendors must explicitly state compliance posture against each item above in their proposal response.

---

## 11. Vendor Evaluation Criteria

Proposals will be evaluated against the following weighted criteria:

| # | Criterion | Weight |
|---|---|---|
| 1 | **Functional coverage** — percentage of Must Have requirements met out of the box (no customization) | 30% |
| 2 | **Scalability & performance** — proven ability to support 5,000+ nodes and 100,000+ interfaces | 15% |
| 3 | **Security & compliance posture** — encryption, RBAC, audit logging, NCA ECC alignment | 15% |
| 4 | **Total Cost of Ownership (3-year)** — license, maintenance, support, and infrastructure costs | 15% |
| 5 | **Vendor stability & roadmap** — years in market, customer base, active development commitment | 10% |
| 6 | **Ease of migration from SolarWinds** — discovery import, configuration migration tooling | 8% |
| 7 | **Support quality** — SLA tiers available, KSA or MENA region support presence | 7% |

### 11.1 Shortlisting Process

1. **RFI response review** — vendors evaluated against requirements table (Sections 7–9)
2. **Reference check** — minimum 2 enterprise references (≥ 1,000 nodes) in GCC or healthcare sector preferred
3. **Proof of Concept (POC)** — shortlisted vendors (maximum 3) will conduct a 30-day on-site or remote POC against a defined test plan
4. **Commercial proposal** — final pricing submitted after POC conclusion

---

## 12. Commercial & Licensing Requirements

Vendors must address all of the following in their proposal:

| Requirement | Details |
|---|---|
| **Licensing model** | State clearly: perpetual vs. subscription; per-node, per-interface, per-user, or unlimited |
| **3-year TCO** | Provide full 3-year cost breakdown: license fees, annual maintenance/support, implementation services, training |
| **POC pricing** | Confirm whether a fully-featured POC license can be provided at no cost |
| **Upgrade pricing** | Clarify pricing for scaling from current node count to 5,000+ nodes |
| **Module pricing** | If traffic analysis (flow), topology, or reporting are separate modules, itemize separately |
| **Support tiers** | Describe available support tiers (business hours, 24×7, dedicated TAM) and associated costs |
| **Payment terms** | State preferred payment terms (annual, multi-year upfront discount) |
| **Local reseller/partner** | Confirm whether a KSA-based authorized reseller or partner is available |

---

## 13. Implementation & Support Requirements

### 13.1 Implementation

| Requirement |
|---|
| Vendor must provide a formal implementation project plan within 10 business days of contract award |
| Parallel running period of minimum 30 days alongside the existing SolarWinds environment during cutover |
| Vendor must provide initial device discovery and onboarding support for the first 500 devices |
| All implementation documentation (installation guide, admin guide, user guide) must be provided in English |

### 13.2 Training

| Requirement |
|---|
| Administrator training: minimum 2 days of in-person or live virtual instructor-led training |
| End-user (NOC operator) training: minimum 1 day of practical training |
| Training materials (slides, videos, or e-learning) to be provided for self-paced refresher use |

### 13.3 Ongoing Support

| Requirement |
|---|
| 24×7 technical support with a maximum 4-hour initial response SLA for critical (P1) incidents |
| Dedicated support channel (ticketing portal, email, phone) |
| Patch and security update delivery within 30 days of release for critical vulnerabilities |
| Named KSA or MENA region technical account contact preferred |

---

## 14. Acceptance Criteria

The solution will be considered accepted for production when all of the following criteria are verified through User Acceptance Testing (UAT):

| ID | Acceptance Criterion | Test Method |
|---|---|---|
| AC-01 | Automated discovery scan completes across a /24 subnet and returns all live devices within 5 minutes | Live test |
| AC-02 | SNMP polling accurately reflects actual CPU and interface state within 2 polling cycles of a real change | Lab test |
| AC-03 | Alert fires and email notification is received within 60 seconds of a threshold breach | Live test |
| AC-04 | Topology map correctly displays all discovered CDP/LLDP neighbors and links for a 50-device test network | UAT review |
| AC-05 | NetFlow data from a Cisco router correctly populates top-talker and top-application views | Lab test |
| AC-06 | A Read-Only user cannot access configuration or alert management screens | Role test |
| AC-07 | A scheduled PDF report is generated and delivered to the configured email recipient | End-to-end test |
| AC-08 | Platform sustains polling of 10,000 interfaces for 24 hours without memory leak or performance degradation | Load test |
| AC-09 | HA failover completes within 60 seconds with no data loss on the secondary node | Failover test |
| AC-10 | RBAC user scoped to a device group cannot view devices outside that group | Role test |
| AC-11 | Alert suppression correctly silences child-device alerts when the upstream parent is confirmed down | Integration test |
| AC-12 | Audit log captures login, configuration change, and alert acknowledgement events with user and timestamp | Audit test |

---

## 15. Risks & Constraints

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Monitoring gap during SolarWinds cutover | Medium | High | Mandatory parallel-run period; vendor to confirm migration tooling |
| Third-party MIB compatibility issues with niche medical devices | Medium | Medium | Vendor must provide MIB browser and OID testing tool; support escalation path for custom MIBs |
| Flow data volume exceeding platform processing capacity | Low | High | Vendor to provide capacity sizing guidance; confirm flow sampling support |
| Database storage growth exceeding projections | Medium | High | Vendor must provide configurable data retention policies and auto-archive capability |
| Integration with ServiceNow requiring custom development | Low | Medium | Confirm native or documented REST API integration before contract award |
| Vendor financial stability or product discontinuation | Low | Very High | Require 3-year product roadmap; evaluate market standing and customer base size |

---

## 16. Vendor Response Instructions

Vendors are requested to submit a written proposal structured as follows:

### 16.1 Required Sections in Vendor Response

1. **Company overview** — years in operation, global and MENA customer base, relevant certifications (ISO 27001, etc.)
2. **Product overview** — current product version, release cadence, 3-year roadmap summary
3. **Requirements compliance matrix** — complete table mapping each FR and NFR in this document to: ✅ Natively supported / ⚠️ Supported via configuration / 🔧 Supported via customization / ❌ Not supported
4. **Architecture overview** — deployment architecture diagram, HA design, supported OS and virtualization platforms
5. **Security & compliance statement** — explicitly address NCA ECC 2018, encryption at rest/in-transit, audit logging, and data residency
6. **Migration approach** — how the vendor proposes to transition from SolarWinds with no monitoring gap
7. **POC plan** — proposed 30-day POC scope, success criteria, and resource requirements
8. **Customer references** — minimum 2 enterprise references; GCC or healthcare sector preferred
9. **Commercial proposal** — itemized 3-year TCO, licensing model, support tiers, and payment options
10. **Support model** — SLA commitments, escalation process, KSA/MENA region support availability

### 16.2 Submission Details

| Field | Details |
|---|---|
| **Submission deadline** | To be confirmed |
| **Submission format** | PDF or Word document; email submission |
| **Point of contact** | Shabeeb Kaip · CodeOx · shabeeb.k@code-ox.com · +966 535 716 437 |
| **Questions deadline** | Clarification questions accepted up to 5 business days before submission deadline |

---

## Appendix A — Priority Key

| Priority | Definition |
|---|---|
| **Must Have (M)** | Critical requirement — solution must support this natively or with minor configuration; failure to meet disqualifies the proposal |
| **Should Have (S)** | Important but not blocking — lack of this feature will be scored against the vendor; compensating capability acceptable |
| **Could Have (C)** | Nice to have — low weight in scoring; not expected in baseline proposal |

---

## Appendix B — Glossary

| Term | Definition |
|---|---|
| SNMP | Simple Network Management Protocol — used to poll and manage network devices |
| NetFlow | Cisco protocol for exporting IP traffic metadata from routers and switches |
| sFlow | Vendor-neutral flow sampling protocol supported by HPE/Aruba and others |
| IPFIX | IETF-standardized flow export protocol (successor to NetFlow v9) |
| CDP | Cisco Discovery Protocol — Layer 2 protocol for discovering adjacent Cisco devices |
| LLDP | Link Layer Discovery Protocol — vendor-neutral equivalent of CDP |
| MIB | Management Information Base — database of SNMP OIDs for a given device |
| MTTR | Mean Time to Repair — average time to restore a failed service or device |
| MTBF | Mean Time Between Failures — average time between successive failures |
| RBAC | Role-Based Access Control — permission model tying user roles to resource access |
| NCA ECC | Saudi Arabia National Cybersecurity Authority Essential Cybersecurity Controls (2018) |
| NOC | Network Operations Center — team responsible for real-time network monitoring |
| HA | High Availability — system design eliminating single points of failure |
| TCO | Total Cost of Ownership — all costs over a defined ownership period |
| POC | Proof of Concept — time-limited evaluation of a vendor solution in a real or simulated environment |
| ITSM | IT Service Management platform (e.g., ServiceNow) |
| TLS | Transport Layer Security — protocol for encrypted data transmission |
| SAML | Security Assertion Markup Language — standard for SSO federation |

---

*Document prepared by CodeOx on behalf of KFMC · June 2026*
*![CodeOx](https://code-ox.com/codeoxlogo.svg) · shabeeb.k@code-ox.com · +966 535 716 437*
