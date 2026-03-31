# Payment Solutions Release Summary: Version 20:02 (January 17, 2020)

- **Release Overview:** Documentation updates for PaymentStream AFT (Automated Fund Transfer) platform, introducing FAQ resources and security enhancements for originating institutions.

- **Key Concept - PaymentStream AFT Originator Management:** New FAQ section (Access and Administration Volume, Section 2.2) addresses common operational queries related to Originator ID management, user provisioning, and business member administration—critical for financial institution operators.

- **Integration Point - Originating AFT via PaymentStream:** The system operates as a distinct AFT origination channel; architects should understand this is a separate product tier with specific administrative workflows distinct from other AFT processing methods.

- **Security Enhancement - 2-Step Authentication:** Document library now includes revised guidance on soft token replacement (Section 1.4) for business member access, indicating multi-factor authentication is a requirement for platform access control.

- **Data Structure Reference:** Originator IDs and business member entities are primary administrative objects requiring lifecycle management; the FAQ section suggests these require careful provisioning and maintenance procedures.

- **Support & Escalation:** Client Support (1-888-889-7878, Option 1 or support@central1.com) owns operational questions—architects should route integration issues through this channel for clarification on supported configurations.

- **Architect Consideration:** This release focuses on operational usability rather than functional expansion, suggesting the core AFT origination platform was stable; plan enhancements around administration tooling and security posture rather than transaction processing changes.