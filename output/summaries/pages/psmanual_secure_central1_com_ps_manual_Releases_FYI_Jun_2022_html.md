# FYI – June 2022 Summary

- **Purpose**: Release notes documenting updates to the Payment Solutions Manual for June 2022, specifically addressing the Central 1 Account Request process (Document ID: 3571).

- **Key Process Change**: Central 1 Account Request workflow now integrates with ServiceNow ticketing system as the primary submission mechanism, with account request forms submitted as attachments to ServiceNow tickets rather than standalone submissions.

- **Contact Information Update**: Updated Central 1 Client Support Services contact details provided (phone: 1-888-889-7878 Option 1, email: support@central1.com), indicating potential backend contact system changes.

- **Constraint Change**: Notice period for account requests reduced from 30 days to 10 days—critical for downstream systems that depend on provisioning timelines and SLA calculations.

- **Integration Point**: Hard dependency on ServiceNow platform for account request submission workflow; architects must ensure Payment Solutions systems can interface with or consume ServiceNow ticket data for tracking and status updates.

- **Documentation Artifact**: Document ID 3571 is the authoritative reference; any system enhancement affecting account request flows should validate alignment with this document version and subsequent updates.

- **Support Channel Dependency**: Support escalations route through Central 1 Client Support Services; consider integrating ticket status notifications or escalation workflows if Payment Solutions systems provision accounts based on ticket lifecycle.