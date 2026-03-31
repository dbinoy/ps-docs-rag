# Summary: PS Release 24:29 – August 15, 2024

- **Scope**: Documentation update establishing maximum face value constraints ($3,000) for specific BC Employment and Assistance cheque types processed through Payment Solutions.

- **Affected Cheque Types**: Imprest cheques issued by Ministry of Social Development and Poverty Reduction (MSDPR) or Ministry of Children and Family Development (MCFD) offices—validation rule applies at point of deposit and during dishonour/reimbursement workflows.

- **Key Process Impact**: Constraint applies across two distinct operational flows:
  - **Deposit Processing** (Section 5.6): Cheque intake and clearing validation
  - **Dishonour & Return** (Section 7.1): Fraud/non-fraud reimbursement requests for rejected cheques

- **Data Validation Requirement**: Cheque processing engine must validate `face_value ≤ $3,000` for cheques with issuing ministry origin codes (MSDPR/MCFD) before acceptance; rejection handling needed for non-compliant submissions.

- **No New Data Structures**: Update applies to existing cheque metadata validation rules; no new fields or codes introduced—constraint is applied at business logic layer.

- **Integration Dependencies**: Assumes upstream systems provide accurate cheque issuing ministry classification; clearing house and reimbursement modules must enforce same constraint consistently.

- **Operational Consideration**: Changes affect both normal-path deposits and exception-path (dishonour) processing—architects should verify constraint enforcement is synchronized across both code paths to prevent inconsistent behavior.