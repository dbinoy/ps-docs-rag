# FYI – March 2025 Summary

- **Purpose**: Release notes documenting updates to the Payment Solutions Manual regarding currency support for Notes and Drafts instruments.

- **Currency Expansion**: Major Currencies list expanded to include New Taiwan Dollar (TWD) and Thai Baht (THB) in Section 8.2, indicating broadened FX capabilities for international payment instruments.

- **Data Structure Impact**: The "Types of Currency Available" enumeration for Notes and Drafts products likely requires updates to currency code tables/reference data—architects should verify this impacts downstream validation logic and settlement systems.

- **Documentation Reference**: Section 8.2 is the authoritative source for supported currencies; any system handling currency selection, validation, or routing for Notes/Drafts must align with this reference.

- **No Breaking Changes Noted**: Update appears additive (list expansion) rather than deprecative, suggesting backward compatibility for existing instruments in previously supported currencies.

- **Integration Consideration**: FX processing, reporting, and compliance modules that reference the Major Currencies list should be reviewed for compatibility with TWD/THB addition.

- **Support Contact**: Central 1 Client Support (1-888-889-7878 Option 1, support@central1.com) is the escalation path for implementation questions or edge cases.