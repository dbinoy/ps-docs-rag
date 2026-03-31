# Summary: Files Outgoing from Central 1

**Overview:** This page documents all file types that Central 1 generates and posts to financial institutions' File and Report Exchange folders for downstream processing (reconciliation, posting, settlement).

## Key Points:

- **AFT Clearing Files** (Forms 6269, 6270, 9083, 9084, 9085, 9086): Post direct deposit and pre-authorized debit transactions to member accounts; region-specific (BC/Atlantic vs. other regions) and currency-specific (CAD/USD) variants required.

- **Qualified Debit Clearing Items** (DREC, QREC, XDREC, XQREC, DCPA/QCPA forms): Process cheques through automated clearing; geographic variants (BC-only vs. all regions) and currency variants (CAD/USD) create four distinct file types with overlapping coverage.

- **Reconciliation Files** (PREC Form 3750, OREC Form 8951): Support automated account-to-account matching; OREC is the successor standard (includes Reference ID, Description, Processing Date, Opening/Closing balances); financial institutions build their own match programs. **Migration constraint:** PREC subscribers automatically receive both files; new subscriptions receive OREC only.

- **Bill Payment & Settlement Files** (HREC Form 6118, Bill Payment Remittance Forms 2665/2667): HREC enables daily bill payment reconciliation; Flat File and EDI variants provide alternative structural formats for remittance data.

- **Interac e-Transfer Reconciliation** (EMTC/EMFC Form 6195): EMTC is mandatory (pending, canceled, completed transactions); EMFC is optional but requires banking system changes to process failed transaction details—key integration decision point.

- **Deposit Processing Files** (Mobile Remote Deposit Form 3604, Corporate Capture XML Form 9349): RTE/XML-based real-time engine integration alternative to legacy mobile capture; dual-path supports both automated posting and manual processes.

- **FINTRAC Compliance File** (Wires Data Extract Form 9327): XML format for AML/FINTRAC reporting; scope filtering (all wires vs. cross-border only) configurable per institution—requires downstream AML system integration.