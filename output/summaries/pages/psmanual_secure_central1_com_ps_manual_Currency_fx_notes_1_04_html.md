# Summary: Establishing Policies for FX Notes

**Purpose:** Defines mandatory and recommended security, access control, and operational policies that financial institutions must implement when deploying FX Notes for foreign currency transaction management.

---

## Key Points for Architects

- **Access Control Model:** FX Notes uses role-based user provisioning with segregated duties; institutions designate users and must restrict administrative access based on job responsibilities and authorization levels. User types are defined in Section 5.2.

- **Authentication & Identity Management:** FX Notes integrates with Client Centre for password-based authentication; one-time passwords must be delivered securely for new users or password resets. See User Management Part for detailed specifications.

- **User Lifecycle Management:** System must support user profile creation, review cycles, and deletion workflows; deletion triggers include one-year inactivity, role changes, or employment termination. No user ID sharing is permitted (unique IDs required).

- **Audit & Monitoring Requirements:** Institutions must implement logging and monitoring controls for FX Notes access activity; external/internal auditors require audit trail visibility. No specific logging schema defined on this page.

- **Inventory Control Integration:** FX Notes interacts with physical foreign currency operations; system must support joint custody workflows, vault register reconciliation, and branch-level distribution logs. Daily reconciliation of orders to shipments/deliveries is required.

- **Regulatory Compliance Dependencies:** System must accommodate Globex 2000 transaction screening rules and flag patterns (e.g., same-day, same-beneficiary payments split under $10K CAD) for FINTRAC Suspicious Transaction Report compliance.

- **No Technical Architecture Defined:** This page prescribes policy requirements, not system design; architects should expect separate technical specifications documents for API contracts, data schemas, and audit logging structures.