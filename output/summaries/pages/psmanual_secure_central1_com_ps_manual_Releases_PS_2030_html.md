# Payment Solutions Release 20:30 Summary (August 31, 2020)

- **Overview**: Documentation update for Wires and Funds Transfers functionality, primarily addressing near real-time settlement for BC/Ontario institutions, high-risk/sanctioned country controls, and service naming conventions.

- **Settlement Architecture Change**: Near real-time settlement implemented for outgoing and incoming wires across BC and Ontario financial institutions in both Wires Part (Sections 14.1, 18.1) and Funds Transfers Part (Sections 10.15, 13.16)—impacts transaction timing SLAs and reconciliation workflows.

- **Compliance Data Flow**: Three-tier country-of-residence/institution validation added to wire processing (beneficiary financial institution, sender/third-party, beneficiary country) with application-level blocking for high-risk/tax haven/sanctioned/prohibited countries—integrates with FINTRAC primary identification requirements (updated in both parts' Section 2.1).

- **Service Naming Migration**: "MTS Data Extract Service" renamed to "Wires Data Extract Service" across 7+ sections and Form 2592; legacy reference cleanup required in dependent systems (BC, Manitoba, Ontario Credit Unions) to prevent integration breaks.

- **Wire Audit Trail Enhancement**: Edit tracking now captures timestamp and user ID in Transaction Information Section (Section 11.2)—critical for compliance and operational troubleshooting; removed previous statement that edit history was invisible to other users.

- **Regulatory Data Addition**: New "Is this transaction face-to-face?" field added to Regulatory Section (Section 8.8)—requires schema extension and potential downstream reporting impact.

- **Wire Lifecycle Rules Clarification**: Distinction clarified between cancellation (application-based, Wires app) vs. recall requests (best-effort, ServiceNow)—impacts operational procedures and state machine design (Section 13.1).

- **Form Management**: Form 2592 formally renamed and revised—update required in document management system and any automated form reference logic.