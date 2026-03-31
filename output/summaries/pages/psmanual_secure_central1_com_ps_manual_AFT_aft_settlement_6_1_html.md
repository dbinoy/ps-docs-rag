# AFT Settlement Documentation Summary

- **Overview**: Defines settlement mechanics for Automated Funds Transfer (AFT) transactions in Central 1's clearing system, covering posting rules, transaction types (Original, Error Correction, Returned, Offsetting Entry), and settlement timelines for both outgoing and incoming AFT flows.

- **Transaction Type Coding System**: Four primary record types with directional variants—C/D records for original transactions (credits/debits), E/F records for error corrections (debit/credit reversals), I/J records for returns (credits/debits). Offsetting entries automatically post to originator accounts for Canadian dollar files; US dollar files require manual posting if banking systems cannot generate them.

- **Settlement Timeline & Constraint**: Transactions post on the due date; however, transactions received *after* the due date post on receipt date. This creates variable settlement windows that must be accounted for in reconciliation and reporting logic.

- **Error Correction Window**: Members can refuse error corrections (E/F records) within 90 days post via transaction types 915/922 (CPA Standards 005/007). Refusals after 90 days fall outside the clearing system, creating operational handoff points requiring external process handling.

- **Dual Account Posting**: All AFT transactions post to both the originator's/sender's Central 1 account AND the recipient's account, creating double-entry accounting requirements. Offsetting entries specifically reverse file totals on originator accounts to balance.

- **Integration Dependencies**: Direct dependencies on Online Return System (ORS), Current Account Services (CAS) Online, File Exchange and Report Distribution, and Automated Transfer System Detailed Listing (CCD/UCD) reporting. Compliance tied to CPA Rule F1 and Payments Canada standards.

- **No State Machine Defined**: Documentation does not specify transaction state transitions, idempotency handling, or reconciliation workflows—architects should clarify these before designing settlement processing or audit systems.