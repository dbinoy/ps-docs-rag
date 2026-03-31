# Payment Solutions Release 22:26 Summary

- **Overview**: Documentation update (September 29, 2022) aligning Payment Solutions Manual and AFT agreements with CPA Rule H1 changes for Pre-authorized Debits (PADs).

- **Key Concept - Sporadic PAD Classification**: "One-time" explicitly added to Sporadic PAD definitions and examples; this distinction affects authorization and processing rules for single-occurrence debits versus recurring patterns.

- **Authorization & Record Retention Requirements**: Recorded authorizations now treated equivalently to written agreements with mandatory 12-month retention; system must support dual capture/retrieval methods (written and audio/recorded formats).

- **Agreement/Document Consolidation**: Paper vs. electronic agreement distinction eliminated; Section 5.7 merged into 5.6, reducing operational branching logic and simplifying enrollment flows for AFT Service PADs.

- **Updated Data Structures** (Document Library):
  - Payee/Payor Information sections now include additional contact fields
  - Payment Details frequency section distinguishes "one-time" payments
  - New "Payment Service Provider as Payee" section in Payee's PAD Agreement (1696)
  - Waiver of Pre-Notification section clarified to include "confirmation" concept

- **Reimbursement Claim Processing**: Requests can now accept either signed written claims or recorded equivalents; Request for Reimbursement Claim document (2425) updated to document dual-method capability; minimum 12-month retention applies to both formats.

- **Recourse & Dispute Handling Dependencies**: Rule H1 section number updates affect recourse deadline calculations and disputed PAD workflows; architects should version-gate these against Rule H1 amendment dates for backward compatibility.