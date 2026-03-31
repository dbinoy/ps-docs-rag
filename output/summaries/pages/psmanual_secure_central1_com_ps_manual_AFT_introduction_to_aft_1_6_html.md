# Summary: Processing PADs (Section 6, AFT Manual)

- **Purpose**: Defines Pre-authorized Debit (PAD) types, notification requirements, and authorization workflows governed by CPA Rule H1

- **Four PAD Types**: Business PAD, Cash Management PAD, Funds Transfer PAD (same payor/payee), and Personal PAD—each with distinct use cases and regulatory treatment; system must classify and track PAD type as a required data attribute

- **Notification Logic**: Fixed-amount PADs require 10-calendar-day advance notice before first debit, annual top-ups, and any amount/date changes; variable-amount PADs require 10-day notice per transaction—unless waived in the PAD Agreement; system must enforce notification timing rules and track waiver status per agreement

- **Authorization & Record Retention**: All PADs require documented authorization (written or recorded); records must be retained minimum 12 months post-termination; sporadic PADs require per-transaction authorization with password/code validation; architect should plan for audit trail storage and long-term record archival

- **Sporadic PAD Handling**: One-time or non-scheduled PADs need explicit per-transaction authorization; PAD Agreement must flag transactions as "sporadic" type; consider separate authorization workflow and telephone recording capability for this classification

- **Integration Dependencies**: Depends on CPA Rule H1 compliance framework; PAD Agreement data model must support waiver flags, amount/date change tracking, and sporadic designation; notification system must be event-driven and calendar-aware

- **Key Data Constraints**: Authorization records and PAD Agreement terms are legal artifacts with statutory retention periods; document retention requirements may extend beyond 12 months per other regulations—architect should implement flexible retention policies and compliance reporting