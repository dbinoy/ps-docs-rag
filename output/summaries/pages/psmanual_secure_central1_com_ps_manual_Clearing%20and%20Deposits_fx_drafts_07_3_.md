# FX Drafts Legal Considerations Summary

- **Scope**: Documents legal and compliance requirements for FX Draft offerings, with emphasis on AML/CFT obligations under Canadian federal legislation and OFAC compliance.

- **Key Regulatory Framework**: PCMLTFA (Proceeds of Crime (Money Laundering) and Terrorist Financing Act) and PCMLTF Regulations apply to financial institutions and their agents; supplementary provincial legislation (BC, ON) and other federal/provincial laws (privacy, human rights) also apply—architects must design systems to support compliance monitoring.

- **Third-Party Dependencies**: Convera is the external payment processor; agreements mandate Convera's compliance with PCMLTFA, OFAC, and Canadian AML/anti-terrorism/sanctions regulations—integration points must enforce these compliance attestations and enable information sharing.

- **Suspicious Activity Notification Requirement**: Financial institutions must immediately notify Convera of suspicious activity; system design must include alerting/logging mechanisms and real-time notification pathways to external party, not just internal compliance workflows.

- **Information Sharing Obligation**: Institutions must share data with Convera to meet regulatory obligations and respond to correspondent bank requests—data governance and API contracts must support controlled disclosure without violating privacy requirements.

- **Compliance Verification**: Convera must demonstrate OFAC (US Treasury) and Canadian regulatory compliance; architecture should include periodic compliance certification validation and audit trails for regulatory review.

- **Architect Implications**: Before designing FX Draft enhancements, coordinate with compliance/legal teams; implement audit logging for all AML-triggering events; design APIs for regulated information exchange with Convera; do not proceed without understanding institution-specific PCMLTFA implementation (refer to Operations Manual Program subscribers).