# Payment Solutions Release Summary: PS 23:30

- **Overview**: Fee schedule update for Digital & Payment Services Class A (Form 2725) effective January 1, 2024, with changes previously announced in the September 28, 2023 pricing notice.

- **Scope & Eligibility**: Form 2725 applies exclusively to BC and Ontario Class A credit unions; architecture must enforce regional/institutional-type constraints on fee schedule application.

- **Document Artifact**: Form 2725 is the authoritative fee schedule document—likely a critical configuration reference that should be versioned and linked in fee calculation services; status changed to "Revised" as of this release.

- **Temporal Constraint**: Fee changes are effective January 1, 2024; any fee calculation logic, billing systems, or reporting tools must reference the correct schedule based on transaction date or billing period to avoid billing errors.

- **Reference Dependencies**: This release references the "2024 Indicative Pricing for Digital and Payment Solutions" notice (September 28, 2023)—suggests fee schedules are announced in advance; architects should model a lead-time dependency between pricing announcements and effective implementation.

- **Support & Governance**: Client Support Services (1-888-889-7878, Option 1; support@central1.com) owns fee-related questions; indicates fee changes may require customer communication workflows or support ticket routing.

- **Documentation Gap**: The phrase "additional changes are described here" references external details not shown—architects should obtain the complete Form 2725 change log and any detailed specifications to understand specific fee structure modifications (new fees, rate changes, product inclusions).