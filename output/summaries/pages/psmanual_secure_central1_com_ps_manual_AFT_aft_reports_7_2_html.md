# Payment Solutions AFT Terminology Summary

- **Purpose**: Defines 50+ standard terms and concepts for Automated Funds Transfer (AFT) operations, establishing a shared vocabulary for debit transactions (PADs), credit transactions (Direct Deposits), and related processing workflows across Canadian financial institutions.

- **Core Transaction Types**: AFT supports two primary transaction classes—debit transactions (PADs drawn on payor accounts) and credit transactions (direct deposits to payee accounts)—with special handling for Business PADs, AFT Re-presentments (return codes 901/908), and US dollar transactions between Canadian institutions.

- **Clearing and Settlement Architecture**: Central 1 acts as the originating direct clearer for BC/Ontario institutions, processing Canadian AFT up to 4 runs/day (BC) or 3 runs/day (Ontario) and USD AFT in single daily/business-day runs; settlement occurs via Bank of Canada accounts with sequential file creation numbers required for verification.

- **Error Handling and Reversals**: System supports Error Corrections (transaction-level fixes), File Error Corrections/Mass Reversals (file-level corrections generating offsetting entries), File Recalls (unprocessed file returns), and Transaction Recalls (individual credit recall before posting)—all critical for reconciliation and dispute resolution.

- **Routing and Identification**: Transit numbers (5-digit branch + 3-digit institution code), 10-digit Originator IDs, and Notice of Change (NOC) transactions maintain routing accuracy; receiving institutions can reject transactions that cannot be processed.

- **File Exchange Infrastructure**: Two integration points—SFTP direct connection or Client Centre portal—for File and Report Exchange; ORS (Online Return System) provides web-based AFT return and NOC transaction creation; PaymentStream AFT enables transaction creation and file uploads.

- **Architectural Constraints**: Files must arrive in sequential order (file creation number validation); offsetting transactions must equal sum of individual items; Business PADs, Member Payees, and Processing Direct Clearers require specialized handling in the origination chain.