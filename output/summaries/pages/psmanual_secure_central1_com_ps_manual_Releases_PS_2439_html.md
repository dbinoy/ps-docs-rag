# Payment Solutions Release 24:39 Summary

- **Scope**: October 16, 2024 update to Interac e-Transfer Online Administration System (OAS) introducing the OAS Fraud Analyst role as a new user type with fraud management capabilities

- **New User Role**: OAS Fraud Analyst can enable/disable profiles and manage suspicious Interac e-Transfer transactions; replaces previous FAS (Central 1 Fraud Analyst System) team involvement for fraud-related actions

- **Key Data Model Changes**: 
  - *Blocked List* now accepts email/phone numbers with transfers still processing but under Interac scrutiny (not hard-blocked)
  - *Contact* definition expanded to include banking account numbers for Account Number Routing workflows
  - New entities: *Funds Recovery Request*, *Handle*, *OAS Fraud Analyst*

- **Transaction Processing Rules**:
  - Only outgoing transfers subject to limit violation failures
  - Request and fulfilling transfer cross-referenced in transaction details
  - Interrupted transfers identified as failure root cause

- **Integration Dependencies**: Central 1 FAS team contact information updated; OAS Fraud Analyst role requires integration with Central 1 fraud systems for suspicious transaction flagging

- **System Access Layer**: Distinct landing page and account management section (3.8) for OAS Fraud Analyst users; authentication/authorization likely separates this role from standard administrators

- **Constraint for Architects**: Must support dual-path fraud workflows—OAS Fraud Analyst actions + Client Centre access—with transaction state consistency