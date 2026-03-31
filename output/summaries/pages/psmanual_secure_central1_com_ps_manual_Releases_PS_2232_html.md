# Release Summary: PS 22:32 (December 15, 2022)

- **Purpose**: Documentation update to International Transfers module reflecting operational changes to FX spread revenue settlement timing and statement delivery mechanism.

- **Critical Business Rule Change**: FX spread revenue credit and statement generation date shifted from 1st business day of following month to the 15th—impacts revenue recognition cycles and reconciliation schedules for international transfer operations.

- **System Integration Dependency**: International Transfers FX spread revenue statements now delivered exclusively through Treasury Reports module (not standalone delivery)—requires clients to have Treasury Reports access configured and users trained on Form 6158 retrieval workflow.

- **Documentation Artifact**: Form 6158 (Treasury Reports User Guide) added to International Transfers document library—establishes this as the authoritative reference for FX spread revenue statement extraction and format.

- **Terminology Addition**: "Treasury Reports" formally defined in Section 2—indicates Treasury Reports is a distinct system component with documented API/interface contract for financial statement delivery.

- **Training Resources**: International Transfers training video page linked in Section 1.5—suggests video documentation exists covering the revised statement date and Treasury Reports integration; relevant for user onboarding and support processes.

- **Architect Consideration**: Any enhancement to international transfer settlement logic, FX revenue calculations, or reporting pipelines must account for the 15th-of-month statement date constraint and Treasury Reports as the sole distribution channel.