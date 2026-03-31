# Payment Solutions Release 22:10 Summary

- **Release Overview**: March 23, 2022 update to Bill Payment Remittance Processing (BPRP) forms 2482 and 2661, removing CCIN cancellation functionality and clarifying biller/member requirements.

- **Form 2482 (BPRP Application) Change**: Removed "Cancellation of a CCIN" option from the Electronic Bill Payment Remittance Processing Information section; CCIN cancellations now require separate Letter of Direction Form 9310, creating a new process dependency and form routing requirement.

- **Form 2661 (BPRP Checklist) Clarifications**: 
  - Business members must issue and display customer account numbers on invoices (data structure requirement for billing/reconciliation)
  - Third-party financial institutions mandate fax number fields for tracing/audit purposes

- **Integration Dependencies**: The removal of inline CCIN cancellation from Form 2482 creates a dependency on Form 9310 workflow; systems must route cancellation requests to appropriate handler and potentially track multi-form submission states.

- **Data Model Constraints**: Customer account numbers are now a mandatory data element with display requirements on invoices; fax number becomes a required field for inter-institution communication, affecting member profile data structures.

- **Architectural Consideration**: Forms 2482, 2661, and 9310 now form an interdependent workflow; any future BPRP system redesign must account for this separation of concerns and ensure proper routing logic between application, assessment, and cancellation processes.