# Summary: Wires User Management (Section 8)

- **Purpose**: Defines procedures for MTS Administrators to create, modify, and delete Wires Users with granular permission management and transaction approval limits.

- **Dual-system requirement**: Wires access requires both (1) Client Centre User ID with Wires application access AND (2) MTS user ID with role-based permissions; MTS user ID must match Client Centre ID exactly (≤20 characters).

- **Permission model**: Seven discrete permissions control user capabilities—View/Update Incoming Transfers, View/Create/Authorize Outgoing Transfers, Permanently Delete Templates, and Spreads/Fees management—assigned independently at user creation/modification.

- **Approval limit constraints**: Two-tier limit structure (Transfer Limit + Daily Limit) applies only to users with "Authorize Outgoing Transfers" permission; limits denominated in CAD with automatic FX conversion at live rates for foreign currency wires (or last-available rate if live unavailable); separate limits required for MemberDirect® Business Services (MDB) and Forge Commercial approvers.

- **Processing model dependency**: User's home transit number and branch-access permissions determined by selected Wires processing model (centralized/partially centralized/decentralized); supports linked branch hierarchies with conditional access.

- **Change authorization workflow**: All user profile additions, modifications, and deletions require dual-administrator approval via Change List queue before activation; pending changes block user modifications until authorized or cancelled.

- **Security requirement**: 2-Step Security token required on Client Centre profile to access Pending Incoming/Outgoing queue options (separate User Management system configuration).

- **Integration dependencies**: Relies on external User Management system (for Client Centre ID provisioning and 2-Step token assignment) and MTS application as primary administrative interface; Wires Users themselves have no MTS access.