# PS 2033 Release Summary (September 8, 2020)

- **Overview**: Documentation update for CEBA (Canada Emergency Business Account) procedures, including application processing workflows and ServiceNow repayment form integration.

- **Key Process Addition**: Section 2.3 clarifies EDC (Export Development Canada) approval/decline workflows within the "My Company" application review module—architects must understand EDC integration as a gating step in the application pipeline.

- **ServiceNow Integration Point**: Chapter 3 updates signal field validation requirements in the CEBA Repayment Form module within ServiceNow; architects should review information field schemas and validation rules to ensure downstream loan administration accuracy.

- **New Loan Admin Taxonomy**: Section 4.3 introduces Loan Administration Fee Categories structure—architects need to understand the fee categorization model, its impact on repayment calculations, and how it maps to the ServiceNow data model.

- **FAQ Categorization**: Chapter 7 reorganization suggests business rule clarifications around common failure points; review updated FAQs to identify undocumented constraints affecting application flow or data validation.

- **No Breaking Changes Indicated**: Updates appear to be clarifications and structural additions rather than API/schema modifications, but architects should verify ServiceNow field requirements against current implementations.

- **Support/Escalation**: Client Support Services (1-888-889-7878, Option 2) is the escalation path for CEBA procedure clarifications.