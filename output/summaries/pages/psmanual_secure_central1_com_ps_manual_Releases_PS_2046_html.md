# Payment Solutions Release Summary: Version 20:46

- **Purpose**: Documents a scheduled update to the Digital & Payment Services Fee Schedule (Form 2725) effective November 12, 2020, with full details available in a secure site news attachment.

- **Regulatory Scope**: Form 2725 applies exclusively to BC and Ontario Class A credit unions—this is a critical access control constraint for any system consuming or distributing this fee schedule data.

- **Document Status**: The fee schedule document is marked as "Revised," indicating a versioned artifact that likely requires version tracking and change management in downstream systems.

- **Documentation Model**: Details are stored externally in a news item attachment rather than inline on this release page, creating a dependency on a separate content management system for the authoritative fee structure data.

- **Support & Change Communication**: Client Support Services (1-888-889-7878, Option 1 or support@central1.com) is the single point of contact, suggesting support ticketing or escalation workflows may feed back into release/documentation processes.

- **No Technical Integration Details**: The page lacks API specifications, data format descriptions, or system dependencies, indicating fee schedule updates are likely distributed through manual document publication rather than automated data pipelines.

- **Architectural Implication**: Any system handling digital/payment services pricing must implement conditional logic to validate that fee schedules are only served to BC/Ontario Class A credit union clients; consider federation or role-based access patterns for multi-jurisdiction deployments.