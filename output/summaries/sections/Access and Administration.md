# Access and Administration — Section Overview

## Purpose

This 40-page section documents Central 1's administrative framework for managing user lifecycle, authentication, permissions, and data exchange. It provides operational procedures for security officers, administrators, and Solutions Architects to establish governance policies, configure access controls, and manage secure file/report distribution across the payment solutions ecosystem.

## Key Concepts

1. **Role-Based Access Control (RBAC)** — Security Officers manage user permissions and application access through the CPS Admin and User Management applications. Policies establish what actions users can perform within Client Centre and connected systems.

2. **Two-Step Security (2SS)** — Multi-factor authentication via hard tokens (physical devices) or soft tokens (mobile apps). Critical for protecting sensitive operations; includes token lifecycle management (ordering, registration, troubleshooting).

3. **Client Centre** — Central portal for end-users to access applications, exchange files, and manage credentials. Administrators control user registration templates, login workflows, and permission inheritance.

4. **File Exchange and Report Distribution** — Dual-mode architecture supporting both programmatic (SFTP direct connection) and web-based (Client Centre UI) file operations with standardized folder structures and file specifications.

5. **Security Officer Hierarchy** — Delegated administration model where Security Officers manage subsets of users/permissions, enabling decentralized governance while maintaining security boundaries.

## How It Works

Users are onboarded through a registration process that captures credentials, assigns application permissions, and optionally enrolls 2-Step Security tokens. Administrators define policies in CPS Admin, then use User Management to implement role assignments and access controls. File exchange occurs either through SFTP (machine-to-machine) using registered credentials, or through Client Centre (human-interactive) with role-based folder visibility. Token lifecycle—including ordering, registration, and emergency recovery—is managed to maintain continuous authentication availability.

## Integration Points

- **CPS Admin Application** — Separate administrative console for Client Centre policy configuration and security officer management
- **File Specifications** — Technical contracts for incoming/outgoing file formats; integration trigger for downstream processing
- **Business Continuity Program** — Disaster recovery and operational resilience considerations for access infrastructure
- **Service Charges** — Billing implications of user counts and feature consumption

## Architect Notes

- **Token dependency risk**: Hard token shortages create onboarding bottlenecks; soft token rollout requires mobile device management strategy
- **Policy configuration complexity**: Cascading permission models (templates → users → applications) require careful inheritance testing
- **File format rigidity**: Central 1 file specifications are tightly coupled to clearing operations; validation failures break downstream workflows
- **Multi-tenancy isolation**: Security Officer scoping must prevent lateral access across distinct client organizations
- **Audit trail requirements**: Access/permission changes should be logged for compliance; verify reporting capabilities before deployment