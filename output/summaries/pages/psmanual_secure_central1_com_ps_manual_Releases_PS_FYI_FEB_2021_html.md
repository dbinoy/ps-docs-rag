# FYI – February 2021 Summary

- **Purpose**: Release notes documenting February 2021 updates to Payment Solutions Manual across three product volumes (Bill Payments, Clearing and Deposits, Currency).

- **Bill Payments Volume**: Financial Institution Transaction Limit Modification Request (Form 2424) now captures transit number for debit designation during transaction limit changes; limits are institution-wide and do not cascade to individual biller limits (max 10 billers, real-time clients only).

- **Clearing and Deposits Volume**: FX Notes Plus system logic clarified—cash letters can be processed as either cash letters or cheque collections at financial institution discretion, while cheque collections have mandatory collection-only routing.

- **Currency Volume**: CIBC transit number for dishonoured item returns corrected to 00090-010 in Provincial Concentrator Account Deposits configuration.

- **Data Structure Change**: Form 2424 now includes a transit number field as a required data point for transaction limit modification workflows.

- **Integration Dependencies**: Constraint exists between institution-level bill payment transaction limits and biller-specific limits (10-biller maximum); changes to one tier do not propagate to the other, requiring separate configuration management.

- **System Boundary**: FX Notes Plus integrates with financial institution backend to determine item classification (cash letter vs. cheque collection) and enforce routing rules accordingly.