# Release 22:27 – October 21, 2022 Summary

- **Purpose**: Documents updates to CEBA (Canada Emergency Business Account) repayment notification workflows and reporting clarifications, effective October 21, 2022.

- **Key Process Change**: CEBA eligibility validations are now final (completed in partnership with CRA); repayment assignments are deterministic based on ineligibility reasons. No exceptions or escalations are permitted—constraints must be enforced in assignment logic.

- **Data Structure Addition**: New ServiceNow category **"CEBA Application Repayment Plan"** tracks two discrete repayment plan states per business member: `Early Repayment Required` or `Standard Repayment Terms`. This is a required reporting artifact under `My Company` in ServiceNow.

- **Temporal Constraint**: Fiscal quarterly calculation periods do not align to fixed calendar dates; exact dates are specified in the **Calculation Period List** artifact (delivered with CEBA Loan Administration Fee Report in ServiceNow). Any calculation, reporting, or validation logic must reference this external source of truth, not hardcoded quarters.

- **Integration Dependencies**: 
  - CRA data partnership for validation (periodic revalidation since April 2020)
  - EDC manages message templates and Intralinks (secure, one-way document repository for external clients)
  - ServiceNow is the authoritative system for repayment plan visibility and reporting
  - EDC Call Centre is the support boundary (no programmatic dispute/escalation handling)

- **Data Flow Note**: Architects must design notification workflows to push repayment plan assignments to business members via EDC-provided templates; ServiceNow is the source system but does not auto-notify.

- **Support Constraint**: CEBA Call Centre (1-888-324-4201) provides information only; system design must not allow end-users to challenge or modify finalized eligibility decisions through any channel.