# Payment Solutions 22:20 Release Summary (September 1, 2022)

- **Scope**: FX Notes Plus module update removing FedEx account number requirement from foreign cheque shipping workflows and foreign currency processing shipment procedures.

- **Key Process Change**: Eliminated mandatory EBC (Electronic Banking Company) FedEx account number collection during FedEx pickup ordering; now requires only verification of prepaid label status and receiver name validation (EBC).

- **Affected Sections**: 
  - Section 11.4 (Shipping Foreign Cheques) 
  - Section 13.2 (Processing Foreign Currency for Shipment)

- **Data Field Removal**: EBC FedEx account number field no longer required in FX Notes Plus Part—impacts data input validation and form schema for both foreign cheque and foreign currency shipment transactions.

- **Integration Point**: FedEx pickup integration simplified; system no longer passes account number to FedEx API calls, suggesting shift to account-agnostic prepaid label model.

- **Constraint/Assumption**: Assumes all outbound FedEx shipments use prepaid labels registered to EBC entity, centralizing billing and simplifying client-side configuration.

- **Support Contact**: Client Support Services (1-888-889-7878, Option 1) or Support@central1.com for implementation questions.