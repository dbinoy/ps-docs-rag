# Release Summary: PS 21:34 (September 17, 2021)

- **Purpose**: Documentation correction for Interac e-Transfer® Limit Group 14 transaction thresholds and definitions in the Payment Solutions manual.

- **Updated Limit Group 14 Parameters**:
  - Daily outgoing transfer limit: $3,000 CAD
  - No-delay transfer 24-hour rolling limit: $500 CAD
  - These constraints apply to transaction authorization and risk management logic

- **Document Artifact**: Limit Groups taxonomy (Document ID: 9369) revised—architects should reference this document when designing transaction validation rules or building compliance checks for Interac e-Transfer flows.

- **System Integration Point**: Limit Group 14 is a configuration parameter that likely feeds into transaction authorization engines, fraud detection rules, and real-time balance validation systems; any enhancement affecting outgoing transfer logic must validate against these thresholds.

- **Architectural Constraint**: No-delay transfer window operates on a 24-hour rolling calculation (not calendar day)—systems processing time-sensitive transfers must implement proper timestamp windowing and state tracking for this duration model.

- **Change Type**: Documentation/configuration correction only—no API changes indicated, but systems already deployed using Limit Group 14 may need validation that they're enforcing the corrected limits.

- **Support Reference**: Client Support Services owns clarifications; escalate questions about limit group behavior impact to 1-888-889-7878 (Option 1) or support@central1.com.