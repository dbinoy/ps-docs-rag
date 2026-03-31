# Summary: Payment Solutions Terminology (Currency Section)

- **Purpose**: Defines foundational terminology for the FX Notes foreign currency trading system and associated Client Centre portal infrastructure

- **User Role Hierarchy**: Four distinct permission tiers—FX Notes Standard User (process orders, view branch-specific data), FX Notes Manager (process orders + manage spreads), FX Notes Auditor (view-only across all branches), and User Management Security Officer (administer users/security)—requiring role-based access control implementation

- **Transit Number Structure**: Critical 9-digit identifier combining leading zero + 3-digit institution number (CPA-assigned, e.g., 809 for BC credit unions) + 5-digit branch number; must be validated in any currency ordering or transaction lookup workflow

- **Transaction Identification**: Reference numbers uniquely identify FX Notes transactions; architects should ensure these persist in audit logs and reconciliation systems for PCMLTFA compliance

- **Business Day Definition**: Weekday operations excluding statutory holidays (including Quebec-specific observances); affects settlement timing, cutoff windows, and SLA calculations—requires jurisdiction-aware holiday calendar configuration

- **Currency Classification**: System distinguishes Major vs. Minor currencies; likely affects pricing, spreads, order processing logic, and availability constraints that should be parameterized for future currency additions

- **Portal Dependencies**: Client Centre is the single access point for all FX Notes operations and user management; CPS Admin and User Management are separate but interconnected subsystems for identity governance—consider authentication federation and session management requirements