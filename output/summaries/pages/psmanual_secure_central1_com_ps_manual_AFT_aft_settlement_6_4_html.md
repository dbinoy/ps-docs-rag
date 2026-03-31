# Summary: Posting Outgoing AFT Files

- **Scope**: Defines settlement posting rules for outgoing AFT (Automated Funds Transfer) files submitted by financial institutions and business member originators to Central 1, covering both CAD and USD transactions with distinct posting timing based on lead time and business day availability.

- **Net Settlement Model**: AFT transactions are netted against offsetting transactions; only non-zero net balances generate postings (coded as AO) to the financial institution's Central 1 account. Zero-balanced nets result in no posting activity.

- **Posting Timing Rules (CAD)**:
  - Sufficient lead time + business day due date → post on due date
  - Sufficient lead time + non-business day due date → post next business day
  - Insufficient lead time → post on receipt date or next business day
  - Timing directly impacts liquidity and settlement finality

- **Offsetting Transaction Handling**: CAD files either include offsetting transactions automatically (posted to originator account on due date) or require manual posting by financial institutions if the net balance is unbalanced; USD files require manual posting by the financial institution (no automatic originator posting).

- **Critical Validation/Integration Point**: Settlement Register Report (ICSR/UCSR) is the authoritative source to determine if offsetting transactions were automatically included—absence of entries in both "Due To" and "Due From" sections indicates manual posting obligation.

- **Account-Level Segregation**: USD and CAD transactions post to separate Central 1 account types (USD vs. default), requiring parallel ledger management and currency-specific settlement logic.

- **Dependency on External Reporting**: Architects must integrate or reference ICSR/UCSR, ICPS/UCPS, and AIBC/AIBU (or AIOC/AIOU) reports to determine posting requirements and verify settlement state; these reports are gating factors for financial institution operational decisions.