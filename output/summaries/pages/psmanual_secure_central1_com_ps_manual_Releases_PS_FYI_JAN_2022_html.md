# Summary: FYI – January 2022 Release Notes

- **Purpose**: Documentation of manual updates and clarifications released in January 2022 for Payment Solutions system, covering CEBA loan administration and AFT clearing file specifications.

- **CEBA Loan Policy Change**: Due date extended from December 31, 2022 to December 31, 2023; impacts loan repayment workflows, settlement logic, and reconciliation processes that depend on maturity date validation.

- **AFT Clearing File Specification Corrections**: File extension corrected to `.DAT` format across four specification documents (CAD/USD variants for both clearing and return files); architects must ensure file handling logic and validation rules reference correct extension to prevent file rejection or routing failures.

- **Ontario-only Scope**: AFT clearing and return file specifications apply exclusively to Ontario operations; system configurations must support regional file format variations and prevent cross-region file processing errors.

- **Document Versioning**: Four specification documents updated (IDs: 9083, 9084, 9085, 9086) with "Revised" status; integration points consuming these specifications require version control and rollout coordination to avoid format mismatches.

- **No API or Data Structure Changes**: This release involves administrative/operational updates rather than system interface changes; no new endpoints, data models, or integration protocols introduced.

- **Support Dependencies**: Central 1 Client Support Services (1-888-889-7878, Option 1) is the escalation point for specification interpretation or implementation issues.