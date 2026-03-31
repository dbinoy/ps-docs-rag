# Payment Solutions Release Summary: Version 23:25

- **Release scope**: Updated Transaction and Charge Codes reference document (Form 3667) effective October 12, 2023, consolidating two prior wire-related billing code advisories issued June 23 and October 6, 2023.

- **Key process changes**: Two distinct billing code modifications affecting wire transactions:
  - Monthly billing code structure changes (June 23 advisory)
  - New transaction billing code introduced specifically for future-dated wire transfers (October 6 advisory)

- **Critical data structure**: Form 3667 serves as the authoritative reference for Transaction and Charge Codes; architects must reference this revised version for any wire transfer billing logic or code mapping implementations.

- **Temporal constraint**: Future-dated wire functionality introduces time-based transaction classification—billing code assignment depends on wire execution timing relative to submission date, requiring state management in wire processing pipelines.

- **Integration dependency**: Wire transaction processing systems must align charge code assignment logic with the October 2023 Form 3667 updates; any existing code mappings or billing rule engines require validation against the revised document.

- **Support/escalation path**: Form 3667 is now the living document for billing code definitions; changes to transaction classification require Client Support Services coordination (1-888-889-7878, Option 1 or support@central1.com) before implementation.