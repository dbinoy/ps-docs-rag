# Payment Solutions Release 23:29 Summary (December 21, 2023)

- **Overview**: Documentation audit and update for File Exchange and Report Distribution functionality, including deprecated Ontario-specific user management procedures and SFTP access clarifications.

- **File Exchange Architecture**: System supports both web-based (Client Centre) and direct connection (SFTP) access patterns; SFTP connections require port 22 configuration and are used by financial institution business members.

- **User Access Control Model**: CPS Admin Security Officers can manage user provisioning when at least two existing officers with administrative access exist; access types include personal and administrative roles with granular permissions to File and Report Exchange resources.

- **Folder Structure Update**: File and Report Exchange implements a hierarchical folder organization containing reports, files, statements, and summaries with standardized naming conventions—this change impacts integration points and file discovery logic for consuming systems.

- **Deprecated Components**: Ontario Financial Institution (ON Only) specific procedures removed—Online User Registration System (OURS) modules (codes 3034, 3035, 3039) are obsolete and should not be referenced in new integrations or architecture decisions; Central 1 Reports (BC) Part is marked obsolete.

- **Integration Dependencies**: Financial institutions depend on File and Report Exchange as a central document distribution hub; removal of User Management Summary table indicates consolidation of administrative interfaces—ensure downstream systems don't rely on this deprecated summary data structure.

- **Support Contact**: Client Support Services available at 1-888-889-7878 (Option 1) or support@central1.com for implementation questions.