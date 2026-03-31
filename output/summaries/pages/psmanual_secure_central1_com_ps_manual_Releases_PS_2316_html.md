# Summary: PS 23:16 Release Notes - FX Drafts Documentation Updates

- **Release scope**: July 7, 2023 update removing obsolete FX Drafts documentation and transitioning draft stock reorder and stop payment workflows from manual processes to the FX Drafts application

- **Deprecated processes**: Manual draft stock reordering (form 9189) and manual stop payment requests (form 9190) are now obsolete; these functions must be performed through the FX Drafts application instead

- **System dependency**: FX Drafts application is the authoritative system for draft stock management and stop payment operations; manual fallback procedures have been eliminated, creating a critical dependency on FX Drafts availability

- **Fallback procedure**: When FX Drafts application is unavailable, clients must contact Convera support (1-888-889-7878 Option 1 or support@central1.com) rather than using manual processes—no documented workaround exists

- **Documentation consolidation**: Related contact information and support resources centralized in Section 1.3; Section 8 procedures for manual processes were completely removed, indicating a deliberate shift from dual-track to application-only operations

- **Integration constraint**: Any system enhancement or integration affecting draft stock or stop payment functionality must route through the FX Drafts application; direct database or alternative processing paths are no longer documented as valid

- **Arch consideration**: The removal of manual processes creates a single point of failure; architects should evaluate whether FX Drafts availability requirements (SLA, failover, disaster recovery) meet operational needs for this critical payment function