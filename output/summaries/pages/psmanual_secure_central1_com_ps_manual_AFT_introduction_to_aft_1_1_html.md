# Introduction to AFT - Architecture Summary

- **Purpose**: Defines Central 1's Automated Funds Transfer (AFT) system for electronic credit/debit transactions, processing workflows, and the optional AFT Re-presentment service for Canadian/USD transactions.

- **Processing Pipeline**: AFT files flow through three validation layers—(1) Central 1 file verification (format, File Creation Number, File Limit, Originator ID), (2) Central 1 transaction verification (removes invalid items but accepts file), (3) receiving institution's data centre validation—with rejected items removed at each stage and reported on ICRR/UCRR reports.

- **Dual Origination Methods**: Originators create AFT files either directly on PaymentStream™ AFT (manual/automatic release) or via third-party software uploaded to File and Report Exchange or PaymentStream AFT; both require successful receipt confirmation before responsibility transfers to Central 1.

- **Re-Presentment Service**: Optional service automatically re-presents returned AFT debits (one-time only) for return codes 901 (NSF) or 908 (Funds Not Cleared); generates offsetting credit transactions to original or alternate account per configuration in ServiceNow; governed by CPA Rule F1.

- **Settlement Integration**: Central 1 forwards accepted AFT files to destination financial institution data centre and delivers offsetting entries to banking system; in some cases financial institutions must manually post offsetting entries—dependency requiring clear settlement account mapping (see AFT Settlement Part).

- **Reporting Architecture**: Separate reports for returns (ICRR/UCRR), re-presented debits (ICDN/UCDN, ICSR/UCSR), and detailed transactions (CCD/UCD); US dollar transactions segregated; re-presentment reports derived from back-end AFT system under separate Originator ID, not PaymentStream AFT directly.

- **CPA Compliance & Constraints**: Transaction codes (Payments Canada Standard 007) must match PAD type and affect reimbursement eligibility; AFT debits limited to single re-presentation per CPA rules; no new transaction code validation mentioned—assumes upstream responsibility.

- **Billing Model**: Per-transaction charges, file-level charges (per-file or monthly based on release mode), monthly incoming AFT charge to sponsoring institution, one-time setup fee—all require manual posting by financial institutions to member accounts, creating reconciliation dependency.