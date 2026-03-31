# Payment Solutions Release Summary: CEBA Settlement & Reconciliation Updates

- **Release scope**: May 29, 2020 update to CEBA (Canada Emergency Business Account) Settlement and Reconciliation procedures within Payment Solutions Manual, specifically addressing EDC (Export Development Canada) fund return workflows.

- **New return procedures**: Documented processes for returning EDC-funded disbursements due to duplicate payments or borrower cancellations—critical for financial institutions managing CEBA loan reversals.

- **Reporting code requirement**: All debit transactions in CEBA settlement must be reported with code **DM** on AIBC reports (BC) and AIOC reports (Ontario)—architects must ensure transaction classification logic supports this dual-jurisdiction reporting requirement.

- **Sectional additions**: Three documentation sections added—Section 3.1 (debit transaction reporting), Section 3.4 (EDC fund return procedures), and Section 3.5 (settlement of returned funds)—indicating multi-step settlement flow that architects need to model in system design.

- **Data flow implication**: System must track EDC funding source at transaction level, enable fund return initiation, and reconcile returned amounts separately from standard CEBA settlement—requires transaction tagging and return request workflow integration.

- **Jurisdiction-specific reporting**: Architecture must support conditional AIBC/AIOC report generation based on financial institution geography, suggesting environment-aware or rule-engine driven report generation.

- **EDC funding dependency**: Integration with Export Development Canada funding tracking is implicit; architects should clarify EDC data source feeds and settlement account mappings before designing return workflows.