# Release 21:38 Summary (October 28, 2021)

- **Overview**: Documentation updates for Fraud Alert Services access provisioning within Enterprise Fraud Management (EFM), targeting CPS Admin and User Management roles.

- **Key Process**: Access provisioning to Fraud Alert Services in EFM now requires documented procedures across two administrative functions—CPS Admin Applications and User Management—indicating role-based access control implementation.

- **Documentation Updates**:
  - New Section 9.8 added to Access and Administration Volume (User Management Part)
  - Section 1.15 added to CPS Admin Applications User Setup Quick Reference Guide
  - Fraud Alert Services document (ID: 9387) revised with clarifying procedural details from live training feedback

- **Integration Point**: Fraud Alert Services operates as a discrete module within the broader EFM system, requiring documented handoff between CPS Admin setup and User Management provisioning workflows.

- **Operational Constraint**: Procedures are now formalized post-training, suggesting previous ambiguity in EFM access workflows; architects should assume downstream systems depend on correct access tier assignments.

- **Support Dependencies**: Client Support Services (1-888-889-7878, Option 1) serves as escalation path; indicates potential configuration complexity warranting support contact during implementation.

- **Architect Consideration**: The revision pattern (new + revised docs) suggests EFM access control evolved after production use; evaluate existing access grant states for consistency with updated procedures before designing enhancements.