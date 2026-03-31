# Payment Solutions 24:40 Release Summary

- **Purpose**: Release notes documenting updates to Wires application template management and source of funds question handling, effective October 17, 2024

- **Template Lifecycle Enhancement**: Templates deleted from availability now enter "Pending Deletion" status rather than immediate removal, allowing authorized users to restore or permanently delete—requires new "Permanently Delete Templates" Outbox permission assigned by MTS Administrators

- **Permission Management**: New "Permanently Delete Templates" permission must be explicitly assigned in MTS user profiles; notably excluded from MDB/Forge Commercial Business profiles, indicating distinct permission models for different account types

- **Source of Funds Question**: Significant change across Wires forms and documentation affecting Wire Funds section completion; impacts Outgoing Wire Request (Form 1171), Contingency Outgoing Wire Request (Form 1799), and Wires Customization Request (Form 6493)

- **Configuration Scope**: Changes apply across all three Wires environment architectures (Centralized, Partially Centralized, Decentralized) with identical permission documentation, suggesting consistent business rules regardless of deployment model

- **Form and Documentation Dependencies**: Updates span 12+ documentation sections including MTS user profile procedures (Sections 8.8-8.11), wire request completion workflows (Sections 15.4, 27.3), and template management chapter restructure (Chapter 18)

- **Architect Consideration**: Template restoration capability requires audit trail/versioning support for deleted templates; source of funds data flow changes may affect downstream reporting, compliance, or settlement systems