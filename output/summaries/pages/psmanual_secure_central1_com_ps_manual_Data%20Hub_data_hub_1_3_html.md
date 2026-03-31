# Summary: Legal Considerations and Policies for Data Hub

**Page Purpose:** Outlines contractual requirements and mandatory internal control policies that financial institutions must implement to participate in the Data Hub platform.

**Key Concepts & Rules:**
- **Prerequisite Agreement:** Participation requires a formal agreement between the financial institution and Central 1; initiate via Client Support Services or account executive (ref. Section 1.3)
- **Security Responsibility Model:** Financial institutions bear full responsibility for Data Hub security practices and internal controls—not a shared or Central 1-managed responsibility
- **User Identity Management:** Enforces strict 1:1 mapping between employees and Data Hub user IDs; multi-ID per employee is prohibited to ensure audit traceability

**Mandatory Policy Controls (Institution-Enforced):**
- Access provisioning limited to job-required functions (principle of least privilege)
- Identification and deactivation of inactive user accounts (lifecycle management requirement)
- No shared credentials across users (non-repudiation requirement)

**Integration Dependencies:**
- Links to Section 1.3 for contact/support resources and organizational contacts
- Implies dependency on upstream identity management systems for user provisioning workflows

**Architect Considerations:**
- Design user access controls to enforce non-sharable, unique credential bindings at the application layer
- Account for user lifecycle workflows (provisioning/deactivation) in integration design
- Legal/contractual requirements should inform authorization architecture and audit logging scope