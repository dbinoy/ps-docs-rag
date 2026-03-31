# FYI – August 2025 Release Summary

- **Purpose**: Documentation of August 2025 updates to Payment Solutions Manual across three primary volumes (Bill Payments, Clearing & Deposits, Electronic Transactions)

- **CRA Business Tax Processing**: Added references to Bank Truncation Guide (Form 10138) for CRA Remittance Vouchers in sections covering document library and electronic filing workflows—critical for tax remittance integrations

- **Payments Canada Migration**: Removed all CPA references across Online Return System (ORS) Part; architect must account for legacy CPA integrations requiring replacement with Payments Canada equivalents

- **Multi-Currency Settlement Logic**: AFT (Automated Fund Transfer) returns for both CAD and USD are debited/credited to appropriate Central 1 accounts—settlement reconciliation logic must handle dual-currency transaction flows correctly

- **Wire Transfer Compliance Changes**: Sections 15.6, 16.10, 16.11 corrected representative/beneficiary recording and international outgoing wire reporting to align with FINTRAC EFT reporting requirements—validate data model captures all required beneficiary/representative fields

- **Transaction Code Refactoring**: Transaction and Charge Codes (3667) removed two defunct M2M-related codes and added description column—update any lookup tables, validation logic, or reporting schemas dependent on M2M transaction types

- **OAS Data Access**: Updated screenshots in Interac e-Transfer transaction tracing via Online Administration System—UI/UX changes in data search/retrieval; verify API or direct database query patterns remain unaffected