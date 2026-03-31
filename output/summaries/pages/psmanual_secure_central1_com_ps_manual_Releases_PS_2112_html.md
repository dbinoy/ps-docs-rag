# Payment Solutions 21:12 Release Summary (April 30, 2021)

- **Purpose**: Documentation update to Currency Ordering Part reflecting new authorization requirements for cash location management operations

- **Key Process Change**: Adding or editing a cash location now requires **second-level authorization** (dual authorization control); this is a critical compliance/control enhancement

- **Affected Operations**:
  - Creating cash order locations (Section 4.3)
  - Updating cash order locations or limits (Section 4.4)

- **New Procedural Element**: Authorized signatory workflows introduced for both new location requests and revised location requests; architects must account for signatory assignment and approval state machines

- **Data Structure Implications**: Cash location entities now require fields for tracking primary authorizer and secondary authorizer; approval workflow states must be managed through the ordering system

- **Integration Consideration**: Currency Volume ordering system depends on authorization service or role-based access control (RBAC) layer to enforce second-sign-off requirement

- **Constraint for Enhancement Design**: Any modifications to cash location management APIs must enforce dual-authorization gates; cannot bypass this control in downstream integrations

- **Support/Escalation**: Client Support (1-888-889-7878 Opt 1, support@central1.com) owns operational questions; coordinate for UAT validation of new authorization flows