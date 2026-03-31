# PS 2025 Release Summary – CEBA Repayment & Settlement Updates

- **Release scope**: August 7, 2020 update adding ServiceNow-based CEBA repayment procedures and clarifying EDC fund return processing timelines within Central 1's banking services platform

- **Key process addition**: New repayment workflow in ServiceNow with associated form completion procedures (Form 9140, Chapter 3), requiring integration between CEBA application lifecycle and ServiceNow ticketing/form submission interface

- **Critical constraint**: Same-day processing of returned EDC funds requires ticket submission to Central 1 before 12:00 pm PT / 3:00 pm ET—hard cutoff dependency for settlement operations affecting reconciliation timing

- **Documentation structure impact**: CEBA Application and Repayment Categories (Chapter 4, Form 9140) underwent restructuring; architects should verify category mappings don't break downstream reconciliation logic or reporting against prior version data

- **Integration dependency**: ServiceNow acts as transactional entry point for repayment forms; requires tight coupling with Central 1's CEBA settlement and reconciliation subsystem (Volume reference: Section 3.4) for EDC fund tracking and audit trails

- **Data flow concern**: Repayment form completion → ServiceNow ticket → Central 1 processing queue (with PT/ET timezone enforcement) → settlement reconciliation; architects must ensure idempotency and error handling around missed cutoff submissions

- **Support contact**: Client Support Services (1-888-889-7878 Opt. 2 or digitalbanking_support@central1.com) owns operational questions; confirm escalation path for ServiceNow integration issues