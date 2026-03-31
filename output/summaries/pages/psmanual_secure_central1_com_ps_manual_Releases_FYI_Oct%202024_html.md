# FYI – October 2024 Summary

- **Purpose**: October 2024 release notes documenting updates to the Payment Solutions Manual, specifically ISO 20022 integration and CAS Online User request handling.

- **ISO 20022 Error Code Additions**: Four new response codes added to Response Codes documentation (doc 9347):
  - **205**: Transaction already committed (idempotency constraint)
  - **375**: Transaction ID mismatch between payment initiation and subsequent request (validation dependency)
  - **397**: Duplicate participant transaction reference number (uniqueness constraint)
  - **446**: Transaction already reversed/rolled back (state management constraint)

- **Data Flow Implication**: Error code 375 indicates a critical validation point where submitted transaction IDs must match the original initiate payment request—architects must ensure this mapping is preserved across request sequences and system boundaries.

- **CAS Online User Access Management**: New request type added to CAS Online User Request form (doc 2513) for post-merger account access provisioning, indicating business process support for M&A scenarios requiring dynamic permission escalation.

- **Integration Point**: Changes affect ISO 20022 message handling and CAS (likely Central 1's internal access/authorization system), suggesting tight coupling between payment transaction lifecycle and user provisioning workflows.

- **Constraint to Note**: Error codes 205 and 446 imply idempotent transaction handling with state tracking; architects must implement stateful transaction management with clear terminal state definitions.