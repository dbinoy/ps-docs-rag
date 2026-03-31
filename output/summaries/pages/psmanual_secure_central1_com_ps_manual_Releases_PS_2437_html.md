# Release 24:37 Summary for Solutions Architect

- **Scope**: Updates to Wires Part documentation reflecting Enterprise Fraud Management (EFM) process changes and Wires Customization Request (Form 6493) enhancements, effective September 23, 2024.

- **Critical Process Change**: Removal of "Auto Risk" alert classification in EFM; all EFM-alerted wires now transition to "Pending" status in Wires application until actioned in EFM—Wires application does not expose alert reasons or investigation details to standard users.

- **EFM Integration Dependency**: Outgoing wires are monitored against EFM, compliance lists, and fraud detection rules; authorized EFM users have separate access to investigation details—implies role-based access control and data segregation between Wires and EFM systems.

- **Cut-off Time Constraint**: Wire settlement with Central 1 (same business day) requires approval before cut-off times specified in Section 14.7; wires held for fraud investigation or compliance scanning may miss cut-off windows.

- **Customization Field Addition**: Collect Funding Method now includes conditional "funds collected by another party" question with required entity detail capture (Section 4.2, Form 6493)—impacts data validation logic and downstream compliance workflows.

- **Post-Approval Limitation**: Approved outgoing wires cannot be cancelled via Wires application; only trace, recall, or amendment requests (best-effort basis) available to financial institutions—architectural implication for state management and workflow irreversibility.

- **Data Transparency Gap**: Wires application intentionally does not surface cancellation reasons or pending status reasons; only EFM-authorized users access investigation context—design implications for audit logging and user support workflows.