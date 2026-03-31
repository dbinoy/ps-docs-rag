# Data Hub User Management Summary

- **Purpose**: Defines the process for requesting, managing, and removing Data Hub access via ServiceNow; Central 1 (not local admins) is the sole provisioning authority for Data Hub user accounts.

- **Key Constraint**: Data Hub access cannot be assigned through CPS Admin or User Management applications—all provisioning flows through ServiceNow Service Catalogue, creating a hard dependency on Central 1's manual intervention and ticket-based workflow.

- **Prerequisite**: Users must have an existing Client Centre ID (as either a Client Centre User or User Management Security Officer) before Data Hub access can be requested; this creates a two-system identity dependency.

- **Access Request Data Flow**: ServiceNow captures User ID, Email Address, Department (dropdown), Job Role (free text), and Objectives (dropdown), then routes to Central 1 for approval and associates the access to the Client Centre user ID—architect should expect this form schema as a contract for provisioning integrations.

- **Access Revocation**: Uses a separate "Make a Request" form in ServiceNow requiring narrative description including user name and Client Centre username, indicating no standardized deletion workflow—risk of manual error and inconsistent removal.

- **Dormant User Auto-Removal**: 180-day inactivity triggers warning email; 240-day inactivity auto-removes access with notification—architect must account for this automatic lifecycle management when designing retention or audit features.

- **Integration Point**: ServiceNow acts as the single integration touchpoint for Data Hub user lifecycle; no API mentioned, suggesting manual Central 1 back-office processing and potential bottleneck for bulk operations.