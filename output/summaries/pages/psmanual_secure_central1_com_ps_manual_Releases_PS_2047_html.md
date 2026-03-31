# Summary: Bill Payment Remittance Processing (BPRP) Updates — November 17, 2020

- **Overview**: Release notes documenting structural reorganization and modernization of BPRP application forms (2482, 2665, 2667) and removal of legacy paper processing pathways.

- **Key Form Restructuring (Form 2482)**: Consolidated biller data into dedicated sections with new fields (Biller's French Trade Name), separated contact information with purpose indicators (enrollment/tracing/both), and relocated validation rules to standalone section—increasing required sample account numbers from 6 to 10 digits.

- **Financial Institution Integration Points**: Removed fax as contact method; email field now primary for FI communication in Financial Institution Information section.

- **Multi-Central Architecture Constraint**: Form includes conditional sections for "other provincial centrals" requiring Lead Central designation, Provincial Central Letter of Direction (Form 9215), and Credit Union Central Authorization—indicating hierarchical central registry dependencies.

- **Account Validation Rule Change**: Tightened validation requirements by mandating 10-digit sample account numbers (previously 6), affecting downstream validation logic and biller onboarding workflows.

- **Legacy System Removal**: Paper processing references eliminated from both flat file (2665) and EDI file specifications (2667)—constrains architectural decisions to electronic-only data flow paths.

- **Data Structure Impact**: Flat file and EDI specifications modified in parallel, suggesting dual-format support requirement with synchronized schema updates across both transmission protocols.