# FYI – May 2022 Summary for Solutions Architect

- **Purpose**: Documentation updates across Payment Solutions Manual covering Access/Administration, Bill Payments, Central 1 Banking Services, and Electronic Transactions volumes released in May 2022.

- **Wires Data Extract Service Expansion**: Service availability expanded from BC/Manitoba/Ontario credit unions to **all Central 1 clients**—removes a geographic/customer-tier constraint that may affect system capacity planning and subscription management.

- **Data Structure Changes**: 
  - Form 9327 (Wires Data Extract Service File Specifications) reorganized with new chapters for file naming conventions and service availability
  - Subscription model changed from transit number-level to **organizational-level subscriptions** in Form 2592—impacts client setup configuration and billing architecture

- **Bill Payment Remittance Processing (BPRP)**: Clarified Corporate Creditor Agreement (Form 9215) usage rules and payment date reporting logic in CEBA Loan Repayments—affects transaction routing and reconciliation workflows.

- **Integration Dependencies**: Wires Data Extract Service file specifications (Form 9327) now foundational reference for Forms 1171 (Outgoing Wire Request) and 2592 (Service Request)—document these dependencies in architecture diagram.

- **Constraint Change**: Removal of regional availability restrictions on Wires Data Extract Service may require backend infrastructure scaling for non-traditional credit union clients; assess current subscription management system capacity.

- **Documentation Architecture**: Forms 9215, 9327, 1171, and 2592 are interdependent control documents; maintain version control across these related specifications.