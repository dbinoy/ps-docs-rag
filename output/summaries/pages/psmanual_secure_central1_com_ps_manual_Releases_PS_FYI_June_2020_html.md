# FYI – June 2020 Summary for Solutions Architect

- **Purpose**: Release notes documenting corrections and clarifications to the Payment Solutions Manual (Document Library Status 9031) for June 2020.

- **Cash Services Process Change**: Standing Orders in Cash Services module are deletion-only; edit functionality is not supported. This is a constraint for any UI/API enhancements involving order management workflows.

- **Cash Order Creation Logic**: Cut-off day rules are location-dependent (e.g., Location D uses "Previous Monday"). The creation process requires validation against location-specific cut-off parameters—relevant for cash order initiation APIs.

- **Deposit Slip Reordering Dependency**: Deposit slips are reordered through D+H system integration. If the reorder form is unavailable, manual intervention via RBC support is required—indicates a potential single point of failure in the reorder workflow.

- **Document Reference**: Changes span multiple sections (3.1, 3.2, 4.2, Chapter 7), suggesting Cash Services functionality is distributed across the manual; architects should review these sections holistically for interdependencies.

- **Support Integration Point**: Client Support Services (1-888-889-7878, Option 1 / support@central1.com) handles escalations—relevant for error handling and customer-facing failure scenarios in enhanced systems.