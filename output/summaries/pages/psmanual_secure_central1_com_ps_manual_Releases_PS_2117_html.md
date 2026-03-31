# Payment Solutions 21:17 Release Summary

- **Release Focus**: Updates to Interac e-Transfer settlement reports (ECCX, EMCU) and response codes for ISO 8583 and ISO 20022 integrations, effective June 15, 2021, with transaction limit changes coming July 8.

- **Key Data Flow Change**: Payees can now receive e-Transfers based on account number (in addition to previous routing methods), affecting settlement logic in Section 1.1 of the manual.

- **Report Schema Updates**: 
  - EMCU (e-Transfer Settlement Summary Report) now includes a defined element table for parsing
  - ECCX (e-Transfer Failed Transactions Report) modified to reflect changes in Interac reference number format; report examples updated

- **Integration Point Expansion**: Two new response code document formats introduced—separate mapping tables for ISO 8583 (document 9346) and ISO 20022 (document 9347) integrations, indicating support for dual protocol pathways with distinct code vocabularies.

- **ServiceNow Dependency**: Interac e-Transfer Trace Request form procedures updated in ServiceNow; architects must account for potential UI/workflow changes affecting tracing operations in Section 6.2.

- **Constraint**: Transaction limit changes effective July 8 will be documented separately; current release does not include those specifications—design reviews should flag this as a pending dependency.

- **Support Escalation**: Client Support Services (1-888-889-7878, Option 1) available for clarification on implementation details; critical for cross-team validation during design phase.