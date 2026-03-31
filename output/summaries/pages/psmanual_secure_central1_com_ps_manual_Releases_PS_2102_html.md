# Summary: PS 21:02 Release Notes - CEBA Forgivable Principal Processing

- **Release scope**: Documentation updates to CEBA (Canada Emergency Business Account) loan forgiveness procedures, effective January 11, 2021, focusing on forgivable principal processing workflows.

- **Core process rule**: Loans close when 75% (for $40K loans) or 66% (for $60K loans) of principal is repaid; remaining 25%/33% is reported as forgivable amount simultaneously via CEBA Repayment form in ServiceNow, triggering loan completion.

- **System of record constraint**: ServiceNow does not mark loans as closed/completed; the financial institution's banking host system is the authoritative book of record, requiring asynchronous reconciliation between systems.

- **Data flow**: Financial institutions submit payment data + forgivable amount date/amount through CEBA Repayment form in ServiceNow → EDC maintains customer-facing loan status via separate CEBA Call Centre backend.

- **Integration dependencies**: 
  - Upstream: Banking host systems (loan origination/disbursement)
  - Downstream: ServiceNow (repayment intake), EDC systems (customer inquiry backend)
  - Settlement/reconciliation processes documented in Central 1 Banking Services Volume, Chapter 1

- **Stakeholder separation**: CEBA Call Centre (1-888-324-4201) serves end customers only; financial institutions must use email (ceba-cuec@edc.ca) for EDC program questions—relevant for support escalation design.

- **Documentation references**: Form 9140 (Quick Reference Guide, Section 8.1) is the authoritative source for procedures; Client Support escalates to Central 1 (1-888-889-7878 Option 2 or digitalbanking_support@central1.com).