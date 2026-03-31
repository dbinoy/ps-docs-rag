# Terminology Summary: Payment Solutions Documentation

**Overview:**
This section defines core terminology for the Business Taxes and Client Centre ecosystem within the PaymentStream® Direct platform.

**Key Concepts & Definitions:**

- **Business Taxes Application**: Runs on PaymentStream® Direct; enables authorized users to submit CRA files and business tax payments to Central 1—primary use case for this documentation module.

- **Client Centre**: Central authentication and access portal providing secured single sign-on to multiple Payment Solutions applications and administrative tools; acts as the identity and access control gateway.

- **Three User Role Types with Distinct Permissions**:
  - *Client Centre Users*: Read-only/application access; cannot manage security roles or other users
  - *CPS Admin Security Officers*: Full user lifecycle management (add/edit/delete) via CPS Admin or User Management; can modify peer CPS Admin roles with restrictions
  - *CPS Admin Tool*: Legacy administrative interface for user management; being phased out by User Management application

- **User Management Application**: Strategic system replacing CPS Admin; manages both Client Centre Users and CPS Admin Security Officers; also handles 2-step security token lifecycle—indicates evolving security posture and planned deprecation path.

- **Integration Dependencies**: PaymentStream® Direct depends on Client Centre for authentication and MemberDirect® system support; all administrative functions flow through Client Centre SSO.

- **Architectural Note**: Role hierarchy and permission model requires careful RBAC implementation; User Management migration strategy should inform design decisions for access control enhancements.