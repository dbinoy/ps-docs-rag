# Summary: PS 25:22 Release (September 23, 2025)

- **Release scope**: Updates to Country-Specific Guidelines and Instructions (Form 3597) with corresponding changes synced to the Wires application, reflecting regulatory and operational changes across multiple jurisdictions.

- **Sanctions/warning message management**: Added for Bolivia and British Virgin Islands; updated for Croatia; removed for 7 countries (Barbados, Djibouti, Gibraltar, Guyana, Jamaica, Saint Maartin, UAE). These messages are bidirectionally integrated between Form 3597 and the Wires application.

- **Payment instructions expansion**: New instructions added for French Polynesia and Oman; updated instructions for 6 countries (Kenya, Malaysia, Pakistan, Peru, Qatar, Vietnam), indicating Form 3597 now reflects real-time Wires application payment rule changes.

- **Data synchronization dependency**: The Wires application is a critical integration point—Form 3597 updates must be propagated to and maintained in sync with Wires application logic, suggesting either a shared data store or event-driven synchronization mechanism.

- **Regulatory compliance artifact**: Form 3597 serves as the authoritative country-specific compliance matrix (sanctions codes, payment instructions, purpose-of-payment codes like Kenya's "10013"), requiring versioning and audit trail for regulatory evidence.

- **Support handoff point**: Client Support Services (1-888-889-7878, support@central1.com) is the escalation path for questions regarding country-specific rules, indicating Form 3597 is client-facing and requires L1 support training on each release.