# Summary: 5 Posting Incoming AFT Files

- **Overview**: Defines how incoming Automated Funds Transfer (AFT) transactions are posted to financial institutions' Central 1 accounts and member accounts, with different processing rules for Canadian and US dollar transactions across BC and Ontario regions.

- **Serviceability Code Framework**: Three-tier compliance model (Codes 0, 1, 2) governed by CPA Rule F1 Section 8 determines funds availability windows—Code 0 requires 2-hour posting of direct deposits from clearing file receipt; Codes 1/2 require posting by start of business on due date. Enrollment requires Form 3571 with dual officer signatures.

- **Regional Multi-Run Processing**: BC processes up to 4 CAD AFT runs daily (CR01-CR04) plus 1 USD run (UC01); Ontario processes up to 4 CAD runs (ON01-ON04 + ONRT) plus 2 USD runs (UN01 + UNRT). US dollar settlement follows US business day calendar, not Canadian.

- **Net Settlement Posting Logic**: Transactions post to Central 1 account by run/branch/currency as net consolidated entries coded "AS" (AFT Settlement). Zero-balance nets generate no posting; postings appear on Account Activity and Balances Reports (AIBC/AIOC for CAD; AIBU/AIOU for USD) and CAS Online with clearing file references.

- **Dual Posting Paths**: Transaction data flows simultaneously to Central 1 account settlement AND to banking system for member account posting; automatic posting via banking system is standard, but manual posting via CCD/UCD reports required if in-house/third-party systems lack automation capability or fail—manual posting responsibility includes CPA Rule compliance verification.

- **Critical Integration Dependencies**: File Exchange timing guarantees (CAD: 4 delivery windows per day 8:59 PM to 8:00 PM PT; USD: 9:00 AM PT daily), report distribution (CRF* for CAD, MERG for USD), and banking system download frequencies are key integration touchpoints requiring synchronization between Central 1, banking platforms, and financial institution systems.

- **Record Type Classification**: Eight transaction record types (C/D/E/F/I/J/K/L) define posting direction and reversal/return semantics; architects must ensure accurate mapping in transaction processing logic, particularly for reversals (E/F) and returns (I/J) which impact member account balances differently than originals.