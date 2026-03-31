# Wire Templates Management - Technical Summary

- **Purpose**: Enables creation, management, and reuse of wire transaction templates (Regular and Bank-to-Bank types) to streamline recurring wire transmission workflows within the Wires application.

- **Permission Model**: Template access is gated by:
  - User role permissions (wire creation capability required to create templates; edit/delete require access to associated sending transit number)
  - Authorized user subset can restore/permanently delete templates
  - Permissions defined in MTS (Management System) Section 8.6 user profiles

- **Template Lifecycle States**: Templates transition through statuses—Active → Pending Deletion → (restorable or permanently deleted)—with audit trail tracking the last editing user; Pending Deletion templates remain queryable but unavailable for wire creation.

- **Data Model**: Templates require mandatory field completion (mirrors wire creation schemas per Chapters 16-17); recommended to store external reference spreadsheet mapping template name/ID, ordering customer, and beneficiary for operational tracking.

- **Validation Constraint**: Only Active-status templates can be applied to generate outgoing wires; Inactive templates (failed validation) must be edited and corrected before use, creating a validation-repair workflow.

- **Integration Dependencies**: 
  - Dependency on Chapter 10 (Wires authentication/login)
  - Dependency on Chapters 16-17 (wire creation field specifications and regulatory compliance requirements)
  - MTS system interaction for user permission administration

- **Irreversible Operation**: Permanent deletion is one-way; once executed, no restore mechanism exists—requires explicit reason entry and confirmation to prevent accidental data loss.