# FYI – December 2023 Summary

- **Purpose**: Release notes documenting updates to Payment Solutions Manual procedures and documentation as of December 2023.

- **Currency Volume Process Changes**: Penny bag supply chain updated—penny bags are now sourced exclusively through financial institutions' armoured car companies rather than direct institutional ordering. Affects Sections 11.1 (Ordering Supplies for Returning Currency) and 11.4 (Returning Canadian Coin).

- **Interac e-Transfer® Limit Groups**: Limit Group 14 has been deprecated and is no longer available for selection. Architects must ensure any existing implementations or customizations referencing Limit Group 14 are refactored; no custom limit group creation is now supported.

- **Data Structure Impact**: Limit group configuration is a controlled enumeration; any APIs or UI components presenting limit group options must be updated to exclude Group 14 and prevent custom group instantiation.

- **Integration Dependency**: Armoured car company systems are now a critical integration point for currency supply ordering workflows—architects should verify SLA alignment and error handling between Payment Solutions and third-party logistics providers.

- **Support & Escalation**: Technical questions route through Central 1 Client Support Services (1-888-889-7878, Option 1, or support@central1.com).