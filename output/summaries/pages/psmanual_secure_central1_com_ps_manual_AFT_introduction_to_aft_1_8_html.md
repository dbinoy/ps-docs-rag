# Page Summary: AFT Dormant Period Requests and Service Cancellation

- **Purpose**: Documents procedures for placing AFT transactions into dormant status and completely cancelling AFT originator services through multiple channels (PaymentStream UI and FTP).

- **Dormant Period Process**: Payor/Payee initiates via Form 2044 → Originator specifies notification requirement days → Originator enters dormant period into PaymentStream AFT system → request retained for audit trail.

- **PaymentStream AFT Cancellation**: Requires Form 5329 with dual authorized officer signatures; Originator must supply 10-digit Originator ID (OID), Legal Company Name, and Originator Long Name; Central 1 performs final cancellation upon receipt.

- **FTP-based Cancellation**: Regional constraint—Form 1378 limited to BC and Atlantic regions only; parallel process to PaymentStream but requires OID selection as "Delete OID" flag rather than form-based entry.

- **Governance Dependencies**: All cancellation flows are bounded by three master agreements (Forms 1904, 2007, 2043) that define underlying service terms; these are prerequisite controls, not enforced within cancellation workflows.

- **Key Data Elements**: Originator ID (10-digit identifier), Legal Company Name, Originator Long Name, notification requirement days, and Delete OID flag are critical fields across all forms; no validation rules or format specifications documented.

- **Integration Point**: PaymentStream AFT system is the primary state-management system for dormant period entry; FTP channel operates independently, suggesting dual-path processing that may require reconciliation logic or state synchronization.

- **Architect Consideration**: No error handling, rollback procedures, or SLA for Central 1 cancellation confirmation documented; dormant vs. cancelled states and transition rules need clarification for system design.