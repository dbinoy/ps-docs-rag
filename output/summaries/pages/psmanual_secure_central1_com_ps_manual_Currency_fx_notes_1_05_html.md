# Summary: FX Notes User Management

- **Purpose**: Documents user access control and role assignment procedures for FX Notes application within the Payment Solutions platform, spanning Client Centre User setup through CPS Admin Security Officer authorization.

- **Three-tier Role Model**: Users assigned to exactly one role per institution level—Standard User (transaction processing), Manager (spread/fee management, reporting), or Auditor (read-only reconciliation access). Role constraint is critical; multiple roles cause access failures.

- **Dual System Architecture**: Client Centre Users exist in parallel systems (CPS Admin and User Management); FX Notes access can be assigned in either system, but User Management is recommended as the authoritative system to enforce single-role constraint and reduce configuration errors.

- **Branch-Level Access Control**: Standard Users require explicit transit number assignment (comma-separated format, e.g., "080912010,080912011") to restrict access; blank field grants all-branch access. Managers and Auditors have institution-wide visibility.

- **Authentication & Authorization Dependencies**: Requires Client Centre User ID with 2-step security token; assignments require CPS Admin Security Officer role with administrative access rights; new Security Officers require Central 1 intervention via Form 1918.

- **Multi-Step Approval Workflow**: Task submissions require secondary authorization by another CPS Admin Security Officer; changes to existing Security Officers routed through central credit union to Central 1 via Form 2035 unless two existing administrative officers exist locally.

- **Integration Points**: Links to User Management Part, CPS Admin Application Part, and 2-Step Security procedures; dependent on Forms 1918, 2035, and 5898 for administrative workflows and branch location definitions.