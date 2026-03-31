# FYI – May 2024 Release Summary

- **Purpose**: Documentation of manual updates to Payment Solutions across Clearing/Deposits and Currency processing volumes for May 2024.

- **Key Process Changes – Clearing & Deposits Volume**:
  - Foreign currency deposit items now processable through FX Notes Plus (currency-dependent acceptance rules apply)
  - Updates span deposit eligibility criteria (Sections 5.2–5.3), non-US foreign item processing (Section 6.1), and cheque collection acceptance (Section 15.1)

- **Key Process Changes – Currency Volume**:
  - Removed Australian Dollar (AUD) support from cash letter and cheque collection workflows in FX Notes Plus processing pipeline
  - Indicates regional/currency support matrix requires maintenance during integration design

- **Integration Point**: FX Notes Plus system is a critical dependency for multi-currency deposit processing; architects must verify currency whitelist logic and validation rules when designing deposit intake or reconciliation workflows.

- **Data Structure Consideration**: Deposit item acceptance rules are segmented by capture type (Branch vs. Corporate) and item origin (domestic vs. non-US foreign); filtering logic must respect these categorical boundaries.

- **Administrative Note**: BPRP application document (2482) underwent revision with HSBC reference removal—suggest verifying vendor dependencies and client-specific configurations in related workflows.

- **Support Dependencies**: Central 1 Client Support (1-888-889-7878, support@central1.com) is the escalation point for clarifications on updated processing rules.