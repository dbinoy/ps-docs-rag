# Payment Solutions Release Summary: 22:33

**Overview:** Fee schedule update for Digital & Payment Services Class A offerings effective January 1, 2023.

- **Affected Document:** Digital & Payment Services Class A Fee Schedule, Form 2725 (revised status in Document Library)
- **Regulatory Scope:** BC and Ontario Class A credit unions only—geo/institution-type constraint on applicability
- **Change Driver:** Previously announced in "2023 New Prices for Digital and Payment Solutions" notice (September 27, 2022)—fee changes tied to published pricing strategy with lead time
- **Effective Date:** January 1, 2023—requires systems/billing configurations to support date-based fee schedule switchover
- **Reference Architecture:** Form 2725 appears to be a master data artifact; architects should assume downstream billing systems consume this as a configuration source requiring versioning and effective-date handling
- **Support Dependency:** Client Support Services (1-888-889-7878, support@central1.com) owns change communication—integration points may exist for client inquiry/escalation workflows
- **Knowledge Gap:** Full details referenced as "described here" (broken/missing link)—architects need access to complete change specification before designing fee calculation logic or data model updates