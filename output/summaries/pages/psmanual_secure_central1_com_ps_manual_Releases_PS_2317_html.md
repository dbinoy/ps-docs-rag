# Release 23:17 Summary for Solutions Architects

- **Purpose**: Release notes documenting the consolidation of Enterprise Fraud Management (EFM) documentation into a new dedicated Part within the Payment Solutions Manual (effective July 18, 2023)

- **Primary Use Case**: EFM currently monitors Interac e-Transfer® transactions with architecture designed to support extensibility to additional payment types (wires noted as example); roadmap for additional payment types pending confirmation

- **Documentation Structure**: New EFM Part encompasses legal/policy frameworks, FAQs, user management, incident management workflows, transaction alerts management, risk/no-risk reporting procedures, and training video resources

- **Key Process Flows**: Includes transaction alert lifecycle management and incident response workflows with structured risk assessment reporting back to Central 1 (specific report format documented in Email Template artifact 9696)

- **Integration Dependencies**: Settlement data flows for Interac e-Transfers reference external documentation in "Interac e-Transfer® Limits, Settlement, Tracing, and Reports Part"—architects should treat this as a dependent system for end-to-end transaction visibility

- **User Management Model**: EFM includes dedicated user access control mechanisms (specifics documented in new Part); relevant for designing role-based access patterns for fraud monitoring operations

- **Obsolescence Note**: Document 9387 (Fraud Alert Services guide) superseded by new Part—ensure legacy references are redirected and migration paths are clear for existing implementations

- **Support/Escalation**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) owns implementation questions; architects should coordinate with support for deployment requirements