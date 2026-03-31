# Release 24:09 Summary (February 28, 2024)

- **Purpose**: Documentation update to the Enterprise Fraud Management (EFM) Part reflecting new reporting capabilities and role-based access controls in the Electronic Transactions Volume.

- **New Role Introduced**: Tenant Report role added to Section 4.2 (EFM User Roles), expanding RBAC model for reporting access—architects must account for role provisioning in identity/authorization systems.

- **Reporting Infrastructure Added**: New Section 10 (Enterprise Fraud Management Reports) indicates a reporting subsystem was introduced; Reports link added to navigation (Section 6.1), suggesting new UI/API endpoints for report generation and delivery.

- **Alert and Incident Management Updates**: 
  - Section 8.1 modified email notification logic for manually created alerts by Fraud Analysis Services (FAS)
  - Section 8.4 updated Auto Risk transaction identification processes
  - Data flow changes between FAS system and notification service require integration point review

- **Recovery of Funds Process Clarified** (Section 8.8): Process logic refined but specifics not detailed here—architects should review full documentation for fund reversal workflows and state machine transitions.

- **UI/UX Enhancements**: Sidebar expand/collapse and "Select None" functionality added to Incidents Page (Section 7.2)—minor but indicates frontend state management changes.

- **Contact/Support**: Questions directed to efm@central1.com (EFM team)—escalation point for architectural clarifications.