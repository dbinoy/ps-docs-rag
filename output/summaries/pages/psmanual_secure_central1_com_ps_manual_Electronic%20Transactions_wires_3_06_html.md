# Summary: MTS Administrator Login and Access Control

- **Purpose**: Documents the authentication and access flow for MTS (Money Transfer System) administrators to manage Wires User permissions, MTS Administrators, and branch information.

- **Authentication Requirements**: Two-factor authentication is mandatory—users must possess a registered 2-step security token and enter the generated code during login; token codes are time-sensitive and validated at the Client Centre layer.

- **Access Control Dependencies**: Three prerequisites must be satisfied before MTS login succeeds:
  1. User must be provisioned as a "User Management Security Officer" or "Client Centre User" role in a separate User Management system
  2. Access to the MTS application must be explicitly assigned (application-level permission)
  3. A corresponding MTS Administrator account must exist in the MTS application (separate identity in MTS)

- **Integration Points**: 
  - Client Centre (https://clients.central1.com) acts as the SSO/authentication gateway
  - User Management system manages role assignment and application access permissions
  - MTS application maintains its own administrator account registry (Section 7.5 reference)
  - Applications are grouped by category and support "favorites" caching

- **Session Management Constraints**: Users must manually log off and close browsers; no automatic session timeout is documented, presenting a potential security consideration for architect review.

- **Data Flow**: Username/Password → Client Centre Authentication → 2-Step Token Validation → Applications List → MTS Selection → MTS Main Menu (only on successful token verification).