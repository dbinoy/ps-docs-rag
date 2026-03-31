# Summary: Release 20:32 – CPS Admin User Management Forms Update

- **Purpose**: Documents updates to CPS Admin user management forms (1918, 2035) to reflect decommissioning of biometric authentication devices for step-up authentication.

- **Key Process Changes**: Two primary workflows updated:
  - Form 1918 (CPS Admin Appointment Certificate): Used to request new CPS Admin Security Officers with access to both CPS Admin and User Management Application
  - Form 2035 (CPS Admin Modification/Deletion Request): Used to modify or delete CPS Admin Security Officer access; most changes can now be completed directly in User Management Application by another CPS Admin Security Officer

- **Critical Authorization Constraints**: CPS Admin Security Officers cannot independently:
  - Reset passwords of other CPS Admin Security Officers
  - Assign administrative application rights (which enables delegation of those applications to others)
  - These operations require form submission to Central 1

- **Authentication Architecture Change**: 2-step security tokens are supplied by the client's financial institution, not by Central 1—architects must assume external token management dependency

- **System Integration Points**: 
  - CPS Admin system integrates with User Management Application for both new provisioning and modification/deletion workflows
  - Central 1 remains the authoritative backend for sensitive operations (password resets, admin rights assignment)

- **Design Consideration**: Biometric device references removed from documentation; architects should not design new biometric authentication into CPS Admin workflows and should plan for legacy biometric removal from existing integrations