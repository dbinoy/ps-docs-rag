# Summary: PS 24:34 Release – Digital & Payment Services Class A Fee Schedule Update

- **Release scope**: Update to Form 2725 (Digital & Payment Services Class A Fee Schedule) released September 11, 2024; detailed change log available via linked documentation.

- **Regulatory/compliance constraint**: Form 2725 applies exclusively to BC and Ontario Class A credit unions—this is a jurisdictional and membership-tier gating requirement that must be enforced in fee schedule distribution logic.

- **Document status**: Form 2725 marked as "Revised" in Document Library—indicates versioning control is in place; architects should assume prior versions exist and may need version-aware retrieval/migration logic.

- **No explicit data model details provided**: The page references "changes" without detailing specific fee structure fields, calculation rules, or schema modifications—architects will need to review the attached news item and Form 2725 itself to identify data structure impacts.

- **Support/escalation path**: Client Support Services (1-888-889-7878 Option 1, support@central1.com) is the documentation owner—useful for clarification on change specifics during design, but indicates this release may affect downstream client-facing systems.

- **Integration consideration**: Form 2725 updates likely feed into fee calculation engines, billing systems, and client-facing fee disclosure systems—architects should map dependencies on this fee schedule in existing payment processing workflows.