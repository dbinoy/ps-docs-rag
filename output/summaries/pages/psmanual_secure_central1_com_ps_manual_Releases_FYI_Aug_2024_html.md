# FYI – August 2024 Summary

- **Purpose**: Documentation of August 2024 updates to Payment Solutions Manual and Document Library affecting currency support and bill payment processing workflows.

- **Currency Constraint**: Swedish Krona (SEK) removed from FX Notes Plus product offering—architects must update any currency enumeration lists, validation rules, or FX conversion logic to exclude SEK from this feature path.

- **BPRP Application (Document ID 2482)**: Bill Payment Remittance Processing application requirements expanded to capture group email addresses in addition to individual contacts—integration points or form schemas tied to applicant onboarding must accommodate multi-recipient email distribution.

- **Data Files & Reporting**: BPRP workflow generates detailed report(s) automatically for processed data files, with optional on-demand report generation—architects should design report generation as either event-driven (automatic) or request-driven (manual trigger) with persistent storage.

- **No Breaking Changes to Core Systems**: Updates are documentation and application requirement changes rather than API/schema modifications, but dependent systems consuming BPRP outputs (e.g., remittance processing engines, settlement systems) should be aware of expanded email distribution capability.

- **Support & Governance**: Changes managed through Client Support Services (1-888-889-7878 Option 1, support@central1.com)—escalation path for clarification on implementation details.