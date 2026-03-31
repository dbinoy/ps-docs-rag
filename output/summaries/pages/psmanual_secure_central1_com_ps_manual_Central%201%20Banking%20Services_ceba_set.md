# CEBA Settlement and Reconciliation Summary

- **Overview**: Documents the end-to-end settlement workflow for Canada Emergency Business Account (CEBA) loan funds, including initial funding, reconciliation, repayments, and administration fee distribution between EDC, Central 1, and member financial institutions.

- **Primary Data Flow**: EDC → Central 1 (lump sum posting, same-day) → Member FI current account → Customer accounts. Settlement visibility via CAS Online (Reference ID: "CEBA") and account activity reports (AIBC for BC, AIOC for Ontario) with transaction codes FT (credit) and DM (debit).

- **Funding Request Timeline**: 3-4 business day lag from application submission in ServiceNow to funds deposited in FI's Central 1 account; reconciliation key is matching Credit/Debit Memo Slip funding note date to ServiceNow Funding Request Date.

- **Critical Integration Points**: ServiceNow (funding request tracking), CAS Online (settlement visibility), CHQ4/ADVC memo slips (settlement notifications for BC/Ontario FIs), and EDC direct wire transfers for returned funds and repayment submissions.

- **Repayment Settlement Constraints**: Bi-monthly reporting cycle with hard cutoff dates (15th/22nd and month-end/7th); Central 1 debits FI accounts on fixed dates (8th and 23rd) regardless of actual customer payment timing, creating a 6-23 day settlement float window.

- **Administration Fee Distribution**: Quarterly (March, June, September, December); EDC remits to Central 1 on the 15th; Central 1 retains 12.5% fee and credits FI 87.5% of reported amounts—requires upstream FI fee calculation and reporting per Chapter 5.

- **Discrepancy Handling**: No automated reconciliation described; manual Client Support Services contact required if funding amounts mismatch—indicates no real-time reconciliation API or exception handling automation currently in place.