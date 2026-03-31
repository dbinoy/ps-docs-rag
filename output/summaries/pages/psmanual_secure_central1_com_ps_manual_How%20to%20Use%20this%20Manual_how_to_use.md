# Payment Solutions Manual - User Access & Navigation Architecture

**Page Purpose:** Documentation of the Payment Solutions Manual's structure, access model, navigation capabilities, and operational procedures for Client Centre users.

---

## Key Architectural Concepts

- **Hierarchical Content Structure:** Manual organized as Volumes → Parts → Chapters → Sections, enabling modular product/service documentation with cross-referenced forms (National vs. BC-Only variants)

- **Dual Access Control Model:** 
  - Base access: Automatic for most Client Centre users (no provisioning required)
  - Restricted access: Operations Manual Program content subscription-based for BC/Ontario credit unions only; returns HTTP error on unauthorized link traversal

- **Form State Management:** Two-tier form distribution strategy:
  - **Unlocked forms** (customer-facing): Customizable; client responsible for CPA compliance monitoring and version control
  - **Locked forms** (Central 1-facing): Immutable to preserve integrity; unlocked variants available only via ServiceNow request with compliance attestation and system output testing requirement

---

## Integration Dependencies

- **Client Centre (https://clients.central1.com):** Authentication gateway for email preference management, form requests, and ServiceNow access
- **ServiceNow Portal:** Service catalogue for unlocked form requests; generates ticket numbers and documents compliance agreements
- **Google Analytics:** Cookie-based user behavior tracking integrated into manual pages
- **Email Notification System (clientcentre@central1.com):** Sends preference update links and release notifications

---

## Critical Constraints for Architects

- **Form Compliance Responsibility:** Clients must validate unlocked form modifications against CPA Rule H1 (PAD agreements) and other applicable regulations; Central 1 rejects non-compliant submissions with no fallback process
- **Real-time Search Indexing:** Full-text search requires 4+ characters for real-time results; 1-3 character searches require explicit Enter keypress, affecting UX design for search features
- **Version Synchronization:** Clients must continuously monitor releases and immediately update internal systems; no automatic form distribution or push mechanism exists beyond email notifications
- **Multi-tab Navigation:** Right-click context menu handling required for concurrent section viewing; impacts web application design for seamless multi-window workflows