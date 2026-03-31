# FX Drafts Login Process - Architecture Summary

- **Purpose**: Defines user authentication and access control procedures for the FX Drafts application, a foreign exchange draft management system integrated with the Client Centre portal.

- **Dual-System Permission Model**: Users require setup in both Client Centre (as Security Officer with FX Drafts application access) and FX Drafts (with role-based admin or order creator permissions), establishing a two-tier access control requirement that must be synchronized during onboarding.

- **Integration Point - Client Centre**: FX Drafts is accessed as a discrete application within the https://clients.central1.com portal, accessed via Applications menu with category-based grouping and favorites functionality, indicating federated identity/SSO architecture.

- **Branch Segregation Field**: "Act on Behalf of" branch name field enforces organizational compartmentalization at login time, suggesting FX Drafts supports multi-branch operations with isolated data contexts per branch session.

- **Role-Based Admin Functions**: Admin users manage other users' permissions within FX Drafts via Form 9182 guide, implying internal permission matrix management separate from Client Centre provisioning—potential data consistency risk between systems.

- **Session Security Constraint**: Mandatory logout requirement when stepping away suggests session state sensitivity; architecture should consider auto-logout timeouts and session invalidation mechanisms.

- **Documentation Dependency**: Procedures for admin and order creator workflows documented in separate user guides (Forms 9182, 9183), distributed via Payment Solutions Manual—indicates functional complexity warranting clear API documentation if designing programmatic access.