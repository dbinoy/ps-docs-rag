# Summary: Payment Solutions Terminology & FAQ (Data Hub Section)

This page defines core user management entities, application roles, and data visualization capabilities within the Central 1 Payment Solutions ecosystem.

## Key Concepts & Definitions

- **Client Centre** is the primary secured portal providing single-point access to Central 1 applications, products, and services information
- **Three-tier user hierarchy exists**: Client Centre Users (read-only portal access) → User Management Security Officers (full CRUD on users/officers) → System administrators
- **Security Officer dual naming**: "User Management Security Officers" and "CPS Admin Security Officers" are identical roles—terminology reflects application context (User Management vs. legacy CPS Admin)

## Application Stack & Integration Points

- **CPS Admin**: Legacy application for user/security officer management; likely requires deprecation planning or documented transition path
- **User Management**: Current application for user lifecycle management, security officer administration, and 2-step token management
- **ServiceNow**: External ticketing system for issue escalation and change requests (dependency for operational support workflows)

## Data Structures & Constraints

- **Visuals**: Dual-format data representation (chart default, table alternate) in Data Hub; suggests templated rendering engine with configurable display modes
- **Security Officer modification permissions**: Only User Management Security Officers can modify peer officers within User Management; CPS Admin lacks this self-management capability (architectural constraint)

## Architect Must Know

- User Management and CPS Admin coexist as parallel systems—clarify consolidation roadmap before designing new capabilities
- No mention of API-based access or programmatic user management; all administration appears portal-centric