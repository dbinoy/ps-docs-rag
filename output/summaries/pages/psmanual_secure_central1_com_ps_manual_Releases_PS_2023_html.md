# Payment Solutions Release Summary: CEBA 3.0 ServiceNow Workflow Update

- **Purpose**: Documents July 21, 2020 release of revised ServiceNow workflows for CEBA 3.0 Loan Application form, based on expanded EDC (Export Development Canada) program requirements

- **Critical Constraint**: CEBA 2.0 forms have been decommissioned upon Wave 1 go-live for Group 3 clients; all existing CEBA 2.0 instances must be migrated to CEBA 3.0 per EDC mandate—this is a hard cutover, not a parallel run scenario

- **Data Model Changes**: CEBA Loan Application form schema updated with new fields to support CEBA 3.0 specifications; a new searchable category ("CEBA Application – Searchable") introduced and exposed via ServiceNow My Company module

- **Integration Points**: 
  - Central 1 ServiceNow instance (workflow engine for form processing)
  - EDC system (downstream approval authority; financial institutions can only approve/decline, EDC retains exclusive reject authority)
  - MemberDirect and Forge platforms (alternative delivery channels with synchronized CEBA Application form)

- **Process Separation**: Clear role boundary—financial institutions (FIs) limited to approve/decline operations; rejection authority exclusively with EDC, requiring architectural consideration for state machine validation and external approval workflows

- **Affected Documentation**: Quick Reference Guide (sections 2.1, 2.2, Chapter 3) updated with new form images and search procedures; architects should reference these for field mapping and UI requirements

- **Support/Escalation**: Client Support Services (1-888-889-7878 Option 2) owns documentation questions; escalate implementation gaps to digitalbanking_support@central1.com