# Payment Solutions Release Summary: PS 23:06

- **Release scope**: Updated Digital & Payment Services Class A Fee Schedule (Form 2725) effective April 18, 2023; architectural implications limited to fee configuration management

- **Geographic and institutional constraints**: Form 2725 applies exclusively to BC and Ontario Class A credit unions—any fee calculation or member-facing logic must enforce this membership class and provincial eligibility check

- **Document artifact**: Form 2725 serves as the authoritative fee schedule; changes are tracked in document library with "Revised" status indicator—consider versioning and audit trail requirements for fee data governance

- **No explicit data structures or APIs mentioned**: This release notification does not specify technical integration points, database schema changes, or API modifications; review the referenced "news item attachment" and full Form 2725 document for detailed fee codes and rate structures

- **Support and escalation path**: Client Support (1-888-889-7878, Option 1 or support@central1.com) is the single point of contact for implementation questions—integration team should establish clear communication protocol if fee changes require system adjustments

- **Knowledge gap for architects**: The actual fee schedule changes and any corresponding system modifications are not detailed on this page; confirm with documentation library or release notes whether fee processing logic, fee tables, or rate engine configurations require code/config changes