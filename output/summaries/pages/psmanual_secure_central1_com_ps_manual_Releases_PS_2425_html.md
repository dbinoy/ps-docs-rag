# Release 24:25 Summary for Solutions Architects

- **Overview**: July 15, 2024 release introducing Enterprise Fraud Management (EFM) system integration for outgoing wire monitoring in "decision mode," with updates across wire processing workflows.

- **Key Integration Point**: Outgoing wires now flow through EFM in decision mode for fraud detection; authorized users manage identified potential fraud cases within EFM system before settlement.

- **New Functional Areas**: 
  - Section 3.3 establishes policies/procedures for EFM-monitored outgoing wires
  - Section 14.5 defines operational handling of EFM-monitored wires (new section)

- **Wire Status States Extended**: Wires application now tracks distinct status values for wires identified as "potential fraud" or "fraud" in EFM; cancellation workflows (Section 23.1) account for these statuses.

- **Settlement Process Changes**: Section 26.2 updates define settlement behavior for wires under investigation for sanction list matches AND wires flagged as potential/confirmed fraud in EFM—likely introducing holds or conditional settlement logic.

- **Incoming Wire Constraint**: Incoming wires missing identifiers will be returned to originating institution (Section 24.2)—impacts data validation requirements and return workflow design.

- **Definition Added**: Enterprise Fraud Management formally defined in Section 2.1 as a system dependency architects must model for authentication, authorization, and decision state management.