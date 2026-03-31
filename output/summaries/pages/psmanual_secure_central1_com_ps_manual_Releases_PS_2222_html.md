# Release Summary: 22:22 – September 9, 2022

- **Purpose**: Documents a fee schedule update to Form 2725 (Digital & Payment Services Class A Fee Schedule) for BC and Ontario Class A credit unions only.

- **Regulatory Scope**: Form 2725 is a restricted-access document limited to Class A credit union members in two provinces—this introduces geographic and membership tier constraints on feature/pricing availability.

- **Update Mechanism**: Changes are published via secure site news items (external reference dependency); the release page itself contains no detailed change specifications, only a reference link—architects should verify the linked news item for actual fee structure modifications.

- **Document Versioning**: Form 2725 is tracked in a Document Library with status "Revised," indicating version control governance; no specific version number or change delta is provided on this page.

- **Support Integration Point**: Client Support (1-888-889-7878, Option 1 or support@central1.com) is the single point of contact for implementation questions—suggests support systems should be briefed on fee schedule changes before release.

- **No Technical Integration Details**: This release contains no API changes, data model updates, or system integration requirements—fee schedule changes likely impact billing/pricing tiers but implementation details are deferred to the referenced news item.

- **Critical Gap for Architects**: The actual technical impact (fee codes, tier mappings, system configuration changes) is external to this page; architects must access the secure news item to determine if billing engine, rate card, or authorization logic modifications are required.