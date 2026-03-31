# PS 24:42 Release Summary (November 28, 2024)

- **Purpose**: Release notes documenting updates to FX Notes Plus functionality, including exchange rate mechanics, user management workflows, and branch location configuration procedures.

- **Exchange Rate Update Mechanism**: Daily automated updates at 4:15 am PT / 7:15 am ET; intra-day updates triggered when any exchange rate fluctuates ≥1%, creating potential real-time data refresh dependency.

- **Critical Data Alignment Rule**: CU name field in FX Notes Plus user creation must match the Financial Institution Name previously recorded in Form 5898 (FX Notes Plus Branch Locations)—enforce this validation at user provisioning layer to prevent lookup failures or permission mismatches.

- **Form 5898 Dependency**: Branch locations data captured in Form 5898 serves as source-of-truth for institution names and is prerequisite input for downstream user management; architect must ensure form submission workflow is complete before user creation workflows are initiated.

- **Floating Privileges Logic**: Section 6.2 now addresses floating privileges in FX Notes Plus user creation—clarify with Product team whether this enables privilege escalation across multiple branches or conditional access, as it impacts authorization model design.

- **Documentation Governance**: Instructions for user creation and branch location submission were centralized in manual (Chapter 5 added); consider whether these procedural constraints should be encoded as enforced business rules in the application vs. remaining documentation-only.

- **Support Escalation Point**: Client Support Services (1-888-889-7878 Opt 1 / support@central1.com) is primary contact for FX Notes Plus issues—integrate into incident routing and SLA tracking if designing operational dashboards.