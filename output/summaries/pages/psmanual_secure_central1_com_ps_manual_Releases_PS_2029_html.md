# Payment Solutions Release Summary: Version 20:29 (August 28, 2020)

- **Scope**: Fee schedule update to Digital & Payment Services Form 2725, effective August 28, 2020; restricted distribution to BC and Ontario Class A credit unions only.

- **Key artifact**: Form 2725 (Digital & Payment Services Fee Schedule) — this is the primary configuration document; architectural systems must reference and enforce version control for this form.

- **Regulatory/compliance constraint**: Access control requirement — Form 2725 is jurisdiction-gated (BC/Ontario) and member-class-gated (Class A credit unions only); authentication/authorization logic must validate both dimensions before granting access.

- **Data governance**: Details of fee structure changes are documented in a separate secure site news item (linked but not embedded); this creates a dependency on external documentation systems for change traceability.

- **Integration point**: Document Library system manages versioning and status tracking (marked "Revised"); architects should understand how this library integrates with fee calculation engines and billing systems.

- **No technical specifications provided**: This release note lacks schema changes, API modifications, or database field details; architects will need to consult the actual Form 2725 and news item for implementation details.

- **Support escalation path**: Changes flow through Client Support Services (1-888-889-7878, Option 1 or support@central1.com); consider whether release deployment requires coordinated communication with support teams.