# Summary: PS 24:26 Release - July 30, 2024

- **Overview**: Documentation update to Digital & Payment Services Class A Fee Schedule (Form 2725) reflecting new fee structure for debit operations.

- **Scope & Constraints**: Form 2725 applies exclusively to BC and Ontario Class A credit unions; any architectural changes must enforce geographic and institution-type eligibility validation.

- **Key Change - Section 4.1**: Introduction of Co-Badge Card Fraud Monitoring Fee as a new line item in Debit Operations Fees; requires fee calculation and billing engine updates to support monthly recurring charge.

- **Data Structure Impact**: Fee Schedule document now requires new field/code to represent Co-Badge Card Fraud Monitoring Fee; likely requires version management in fee master data and corresponding GL coding for revenue recognition.

- **Integration Point**: Client Centre system is primary source-of-truth documentation; architects must establish data synchronization mechanism between Payment Solutions backend and Client Centre portal to maintain fee transparency.

- **Client Communication**: Fee changes documented in separate Client Centre notice ("Co-Badge Card: introducing monthly fraud monitoring fee"); architects should design notification/audit trail capability for fee schedule changes to ensure compliance visibility.

- **Support Dependency**: Client Support Services (1-888-889-7878, support@central1.com) owns customer communication; system should log fee inquiries and support escalations for Co-Badge-related billing questions.