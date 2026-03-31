# Payment Solutions Release 23:21 Summary

- **Purpose**: September 2023 release updating indemnifiable amount thresholds and terminology across cheque processing procedures, reflecting regulatory/organizational changes.

- **Key Indemnifiable Amount Changes**:
  - Receiver General Warrants: **$1,750** (new threshold for non-customer cashing requirements)
  - BC Employment and Assistance + Imprest Cheques: **$4,500** (increased threshold for reimbursement eligibility)
  - These limits establish hard constraints in fraud/dishonour reimbursement workflows and must be enforced at validation/processing layers.

- **Critical Process Rules Updated**:
  - Financial institutions are **mandated to cash** Receiver General Warrants for non-members up to $1,750 threshold (CPA Rule G8)
  - Photo ID requirements for non-member payees revised; Ministry-provided Photo ID Letter now required for BC cheques without acceptable ID
  - Validation workflow for BC cheques includes phone escalation (778-405-4306 / 1-877-377-7702) for legitimacy concerns.

- **Terminology Mapping** (system/UI updates required):
  - "Government of Canada Warrants" → **Receiver General Warrants**
  - "Secure site" → **Client Centre** (with updated login procedures)
  - "Ministry of Housing and Social Development" → **Ministry of Social Development and Poverty Reduction**
  - These nomenclature changes likely affect configuration, labels, and integration with ministry systems.

- **System Integration Dependencies**:
  - Ministry of Social Development and Poverty Reduction (BC cheque validation, Photo ID Letter issuance)
  - Client Centre authentication/access control (replaces previous secure site login)
  - Reimbursement request workflows tied to document 2303 (Request for Reimbursement form)

- **Architecture Constraints**:
  - Indemnifiable amounts are configuration parameters requiring version control and audit trails for compliance
  - Cheque validation logic must differentiate customer vs. non-customer processing paths and apply threshold gates
  - Dishonour/fraud claim workflows depend on cheque type (Receiver General vs. BC Employment) to determine applicable limits and reimbursement eligibility.