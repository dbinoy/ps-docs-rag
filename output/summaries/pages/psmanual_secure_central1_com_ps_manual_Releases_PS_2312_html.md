# Payment Solutions Release Summary: 23:12 (June 16, 2023)

- **Release scope**: Updated ISO 20022 return code definitions in Form 9610 with newly added codes to align with international payment standards

- **Key artifact modified**: Form 9610 (ISO 20022 Return Code Definitions) — a structured document governing payment return/reject code mappings used across transaction processing workflows

- **Data structure impact**: New ISO 20022 return codes introduced; architects must verify these codes are supported throughout the payment processing pipeline (authorization, settlement, reconciliation services) and mapped correctly in downstream systems

- **Integration point**: Return codes likely feed into:
  - Transaction status reporting to clients
  - Automated reconciliation and exception handling workflows
  - Regulatory compliance reporting (ISO 20022 compliance requirement)

- **Critical constraint**: Any system consuming Form 9610 data must be updated to recognize and properly handle the newly added codes to prevent silent failures or incorrect transaction classification

- **Documentation status**: Marked as "Revised" — existing implementations using older code sets require validation and potential migration planning

- **Support contact**: Client Support Services (1-888-889-7878, Option 1) for clarification on code mapping and implementation impact