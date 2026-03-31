# Payment Solutions Release 21:24 Summary

- **Overview**: July 8, 2021 release implementing Interac's mandatory $25,000 per-transaction incoming limit across all e-Transfer service participants, eliminating rolling limits and probationary features.

- **Key Regulatory Change**: All financial institutions must support a per-transaction incoming limit of $25,000 (no cumulative restrictions) for security-question transfers, Autodeposit, and future account-to-account transactions; applies to Send Money, Request Money, and Interac e-Transfer for Business (Instant) transaction types.

- **Limit Group Architecture**: New Limit Group 16 introduced with maximum $25,000 Send Money outgoing limits; existing Limit Groups 1-15 updated to support $25,000 incoming per-transaction while maintaining current outgoing limits unchanged; probationary limit feature deprecated and removed.

- **Data Model Changes**: 
  - Removed all incoming rolling limit fields/logic
  - Added "No Delay Transfer" terminology (effective July 18, 2021) replacing "Instant Transfer"
  - Updated "Rolling Time Period" definition to apply only to Send transactions

- **Documentation Restructuring**: Chapter 4 created for "Interac e-Transfer Limits and Central 1 Limit Groups"; Section 1.3 content migrated; new Section 4.3 for limit group listing with Sections 4.1-4.2 defining limits and group details.

- **Integration Dependencies**: Changes affect all downstream transaction processing, settlement, and fraud management systems; FI participation in Limit Group 16 requires Central 1 Relationship Manager coordination for risk/fraud management policies.

- **Support Contact**: Client Support Services (1-888-889-7878, Option 1 or support@central1.com) for implementation questions.