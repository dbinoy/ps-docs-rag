# Settlement and Reports - Technical Summary

- **Overview**: Describes settlement mechanics for returned cheques and two primary reporting mechanisms (ORPI/ORUI and AIBC/AIOU/AIOC/AIOU) that track return processing and current account activity across CAD/USD currencies and regional jurisdictions (BC/Ontario).

- **Settlement Logic**: Return items are credited to currency-specific current accounts (CAD or USD); government reimbursements follow separate timing (upon receipt from provincial/federal sources), introducing asynchronous settlement flows that require reconciliation handling.

- **ORPI/ORUI Report Structure** (Daily):
  - Three-tiered layout: individual cheque returns (including reinstated/image-excluded variants), aggregated totals by item type, settlement posting summary
  - Distributed via MERG files in root directory; PDFs organized by currency subfolder (CAD/USD)
  - Critical for daily verification; discrepancies require immediate Central 1 notification—indicates SLA enforcement on downstream processing

- **AIBC/AIOU/AIOC/AIOU Report Structure** (Business Days only):
  - Four report variants by region/currency; multi-charter branching support (separate pages per charter)
  - Returns identified by Transaction Code "RI"; tracks opening/closing balances, net activity, debit/credit postings by branch
  - Serves as reconciliation tool; also mirrored in CAS Online system—indicates dual-channel data availability

- **Integration Dependencies**: Reports extracted from MERG files (File and Report Exchange) and CAS Online; Ontario data requires ONDL file extraction; tight coupling to current account posting mechanisms and currency routing logic.

- **Architectural Constraints**: Currency-aware settlement (CAD/USD routes), jurisdiction-specific reporting (BC/Ontario variants), multi-charter branch aggregation, and asynchronous government reimbursement settlement requiring eventual consistency handling.