# Release 20:39 Summary (October 13, 2020)

- **Overview**: Documentation updates reflecting biometric device decommissioning and enhanced integration between CPS Admin Application and User Management application for Secure Site user and security officer management.

- **Biometric Sunset**: Forms 1919 (Biometric Device Order) and 5972 (SecuGen Device Driver Troubleshooting Guide) marked obsolete; 2-step security tokens now referenced throughout CPS Admin documentation as replacement authentication mechanism.

- **Dual User Management Systems**: CPS Admin and User Management applications run in parallel with asymmetric capabilities—token management exclusive to CPS Admin; realm management exclusive to User Management; Secure Site Users synchronized across both systems with limited exceptions.

- **Account Lifecycle & Recovery**: Disabled accounts (after 13+ months inactivity) enter 90-day grace period before deletion; deleted accounts recoverable for additional 90 days—architects must implement retention logic supporting this three-phase deactivation model.

- **CPS Admin Security Officer Management**: New CPS Admin officer provisioning requires Central 1 processing (no self-service via User Management); modifications/deletions can occur via User Management directly *or* manual Central 1 request—architects must define role-based authorization boundaries between systems.

- **Forms Updated**: CPS Admin Appointment Certificate (Form 1918) and Modification/Deletion Request (Form 2035) refreshed in September 2020; both forms require procedure alignment with dual-system management workflow.

- **Integration Dependency**: User Management application provides upgraded UX for managing CPS Admin Security Officers; architects should plan migration path treating User Management as primary system for officer lifecycle operations.