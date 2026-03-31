# PS 25:28 Release Summary – December 1, 2025

- **Scope**: Documentation update to the Wires Part of the Electronic Transactions Volume, reflecting structural changes to wire processing workflows and form handling in ServiceNow.

- **Key Structural Change**: Sender FI to Receiver FI Information section reduced from six fields to two fields for both regular wires (Section 16.14) and bank-to-bank wires (Section 17.9), simplifying wire metadata exchange between financial institutions.

- **ServiceNow Integration**: Wires Trace, Recall, and Amendment Request form (Document 1917) updated with new request type options—Compliance Request and Fraud Recall Request—indicating expanded functionality in the ServiceNow ticketing/workflow system.

- **Critical Operational Constraint**: Wire recalls, amendments, and trace requests operate on best-efforts basis with no guarantee; receiving bank voluntary cooperation required post-release. This constraint affects SLA design and client expectations for remediation workflows.

- **Process Impact**: Section 25.2 reflects minor changes to trace/recall/amendment request workflows, suggesting potential UX or field validation updates in ServiceNow that architects must account for in downstream integrations or audit trails.

- **Nomenclature Change**: "Relationship manager" replaced with "senior account executive" across documentation—verify if this affects API role mappings, permission models, or account hierarchy structures in related systems.

- **Support Dependency**: Client Support Services (1-888-889-7878, support@central1.com) is the escalation point for wire processing issues, indicating this is customer-facing with potential SLA implications for system availability.