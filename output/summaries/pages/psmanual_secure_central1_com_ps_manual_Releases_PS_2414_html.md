# Payment Solutions Release 24:14 Summary

- **Overview**: Release 24:14 (March 13, 2024) introduces three new transaction and charge code combinations to Form 3667, the standardized code reference document for Payment Solutions transaction classification.

- **New Code Additions**:
  - **PC** (Primary Cheques Clearing) – for cheque settlement processing
  - **CQ** (Charge Back Qualified Clearing) – for disputed/qualified chargeback transactions
  - **E3** (e-Transfer Request Money Debit) – for e-Transfer payment initiation debits
  - These codes integrate into Form 3667, the master reference for transaction-to-charge code mappings

- **Data Structure Impact**: Form 3667 is the authoritative lookup table for transaction routing and classification; systems consuming this form must update their code validation logic and transaction routing rules to recognize and properly handle PC, CQ, and E3 codes.

- **Integration Constraints**: Any downstream systems, clearing house interfaces, or reporting engines that perform transaction type validation or categorization depend on Form 3667 currency; stale code references will cause routing failures or data reconciliation issues.

- **Backward Compatibility Consideration**: Existing transaction workflows must account for the three new code paths; legacy systems may require migration logic to classify historical transactions or reject unknown codes.

- **Governance**: Form 3667 revisions are documented through Central1 news/updates advisories (published March 7, 2024); architects should subscribe to the advisory feed for regulatory or operational changes affecting transaction handling.

- **Support Dependencies**: Client Support Services (1-888-889-7878 Option 1) owns Form 3667 clarifications and code interpretation questions; escalation path for integration ambiguities.