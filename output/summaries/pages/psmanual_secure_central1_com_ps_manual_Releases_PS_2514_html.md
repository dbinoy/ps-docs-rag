# Release 25:14 Summary for Solutions Architects

- **Overview**: June 24, 2025 release focused on extending Enterprise Fraud Management (EFM) documentation to cover mobile deposit transactions, including monitoring mode capabilities and fund recovery workflows.

- **Key Concept - Mobile Deposit Monitoring Mode**: EFM now supports active monitoring of mobile deposit transactions with live monitoring mode functionality; architects should understand this introduces a new transaction classification pathway distinct from traditional electronic transactions.

- **Risk Classification Enhancement**: Section 8.2 introduces newly-defined risk reasons specific to mobile deposits; architects need clarification on whether these risk codes are additive to or replace existing risk reason enumerations in the fraud detection data model.

- **Notification Integration Point**: Email notification system extended to mobile transaction workflows (Section 8.9); verify SMTP/notification service dependencies and confirm whether mobile deposit alerts follow existing alert routing rules or require separate configuration channels.

- **Transaction Marking State Machine**: Section 8.9 documents new mark-as-Risk/No-risk operational workflows post-monitoring-mode; architects should map these state transitions to understand impact on transaction status enumerations and audit logging requirements.

- **Fund Recovery Scope Expansion**: Section 8.11 now includes mobile deposit transactions in recovery workflows; verify whether recovery processing rules, timelines, and reconciliation logic differ from traditional ACH/wire fund recovery procedures.

- **Data Flow Constraint**: Monitoring mode appears to precede live transaction processing; confirm whether mobile deposits bypass standard fraud checks initially or run parallel validation paths during monitoring phase.