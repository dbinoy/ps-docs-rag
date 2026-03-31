# Wires Page Summary

- **Overview**: Introduces the Wires application on PaymentStream Direct™ platform for creating/receiving domestic and international wire transfers with advanced SWIFT lookup, 2-Step Security token support, templating, and FX management capabilities.

- **Critical Integration Constraint**: Wires application is **not connected to banking systems**—settlement of incoming/outgoing wires must occur outside the application, creating a manual reconciliation dependency that architects must account for in system design.

- **Fraud Monitoring Integration**: Outgoing wires are monitored by Central 1's Enterprise Fraud Management (EFM) system; potential fraud alerts are managed in EFM, requiring bidirectional data flow between Wires and EFM systems.

- **Regulatory & Compliance Dependencies**: System integrates with multiple external compliance frameworks (PCMLTFA, FINTRAC, OFAC, CSIS, RCMP) and regional regulators (BCFSA, FSRA, DGCM, etc.); architects must understand reporting obligations and data requirements for each jurisdiction.

- **Fee Processing Rules**: Incoming and outgoing wires incur multiple deduction points (receiving institution, intermediary institutions, trace/recall/amendment requests); architects must support fee calculation logic where final beneficiary amount may differ from sent amount, plus optional future-dated/priority wire surcharges.

- **Cut-off Times & Availability Constraint**: Wire processing subject to cut-off times (details in Section 14.7) with incoming wires limited to business days (Mon-Fri, excluding statutory holidays); system must enforce these temporal constraints.

- **Security & Access Requirements**: 2-Step security token mandatory for sensitive operations (approve outgoing wires, accept incoming wires); requires token integration architecture, and Microsoft Edge browser incompatibility noted.

- **Data Extraction & Reporting**: Wires Data Extract Service (Form 2592) and ISO 20022 Return Code Definitions (Form 9610) indicate system generates structured extract files; architects should plan for standardized data export mechanisms supporting compliance reporting and integrations.