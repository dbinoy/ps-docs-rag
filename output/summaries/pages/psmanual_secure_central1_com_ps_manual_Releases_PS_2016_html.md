# Payment Solutions Release Summary: Version 20:16 (May 21, 2020)

- **Scope**: Updated sanctions compliance data in Form 3597 (Country-Specific Guidelines and Instructions) to reflect revised Canadian regulatory restrictions on wire transfers and money movement.

- **Affected Systems**: Changes synchronized across three integrated systems—primary documentation (Form 3597), Wires application, and Money Transfer System (MTS)—indicating these components share or reference common sanctions country lists.

- **Key Data Element**: Country-list validation rules in Form 3597 require architectural consideration for how sanctions checks are implemented; updates suggest this is a critical compliance gate for transaction processing.

- **Integration Dependency**: MTS and Wires application both consume the same sanctions reference data from Form 3597, implying a centralized or synchronized data source that must maintain consistency across systems. Any architectural changes should account for this multi-system dependency.

- **Regulatory Constraint**: Canadian-specific sanctions regulations drive periodic updates; architects should design systems with versioned compliance ruleset management to support future regulatory changes without breaking deployed systems.

- **Support Contact**: Client Support Services (1-888-889-7878, Option 1 or support@central1.com) is the escalation path for sanctions-related questions—relevant for SLAs and change management workflows.

- **Revision Status**: Document marked "Revised" indicates form updates are tracked; architects should implement audit trails for compliance document versions linked to transaction processing.