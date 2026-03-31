# PS Release 21:36 Summary – September 27, 2021

- **Release scope**: Updated Country-Specific Guidelines and Instructions (Form 3597) to reflect changes in sanction requirements and payment instruction fields; changes synchronized across Payment Solutions and Wires applications.

- **Sanction requirement changes**: 
  - Removed sanctions for 41 countries (e.g., Switzerland, Mauritius, Malaysia)
  - Added sanctions for 20 countries (e.g., China, Brazil, Nigeria)
  - Updated sanction language/requirements for 40 countries (e.g., Russia, Iran, North Korea, Venezuela)

- **Payment instruction schema modification**: "Beneficiary Address" field added to Uganda payment instructions, indicating Form 3597 is a data structure with country-specific, conditional field requirements.

- **Multi-system synchronization requirement**: Changes implemented in both Payment Solutions and Wires application, indicating Form 3597 is a shared reference document requiring coordinated deployment across at least two systems.

- **Compliance-driven architecture**: Sanction requirements are country-based controls that likely enforce validation rules, transaction screening, or conditional field capture during payment processing workflows.

- **Form 3597 as configuration artifact**: Acts as a controlled reference document (versioned, released) rather than runtime-generated, suggesting it may be embedded in application configuration, a database lookup table, or externally referenced during payment validation.

- **Support contacts**: Client Support Services (1-888-889-7878, Option 1) and support@central1.com for questions regarding implementation or interpretation of country-specific rules.