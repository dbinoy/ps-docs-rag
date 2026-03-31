# Summary: 12 Branches on FX Notes

- **Purpose**: Documents branch location management and viewing procedures for FX Notes, Central 1's multi-branch foreign exchange notes system.

- **Primary Data Asset**: Form 5898 (FX Notes Branch Locations) is the master configuration document; must be resubmitted to Central 1 whenever branch information changes, triggering system reconfiguration.

- **Critical Data Field**: "Financial Institution Name for User Management" (max 50 characters) must exactly match the name used in the User Management system when granting FX Notes access—any mismatch breaks user provisioning (dependency on Section 6.2).

- **Transit Number Format**: 9-digit identifier consisting of leading zero + 3-digit institution number + 5-digit branch number (e.g., 080912010); this is the canonical branch identifier in FX Notes.

- **User Roles**: FX Notes Managers and Auditors have branch management and viewing permissions; role-based access is enforced at the Administration > Branch Management interface level.

- **Integration Points**: Direct dependency on User Management system for access control; Form 5898 is the single point of truth for branch-to-system mapping that Central 1 must process and implement.

- **Constraint**: Branch updates are not self-service; all changes require manual form submission to Central 1 and require their implementation—no real-time branch provisioning capability.