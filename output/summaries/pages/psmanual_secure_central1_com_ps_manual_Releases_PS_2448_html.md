# Summary: PS 24:48 Release — Digital & Payment Services Class A Fee Schedule Update

- **Purpose**: Documentation of fee schedule updates for Digital & Payment Services Class A offerings (Form 2725), effective January 1, 2025, aligned with 2025 Indicative Pricing announcement from September 27, 2024.

- **Scope constraint**: Form 2725 applies exclusively to **BC and Ontario Class A credit unions**—architecture must enforce geographic and institutional classification filters to prevent unauthorized access or application to other regions/tiers.

- **Document artifact**: Form 2725 is the authoritative fee schedule document; any pricing engine or billing system must reference the revised version and track document status (marked "Revised" in library).

- **Effective date dependency**: January 1, 2025 is a hard cutoff—billing systems must implement date-based logic to apply legacy fees pre-2025 and new fees post-2025; retroactive application is not indicated.

- **Change rationale linkage**: Detailed rationale is provided in "2025 Indicative Pricing for Payment and Digital Services" notice (September 27, 2024)—architects should review that notice to understand fee structure changes and model potential billing impact.

- **Support integration point**: Client Support Services (1-888-889-7878, Option 1; support@central1.com) is the escalation channel—consider support ticketing system integration for fee-related inquiries and ensure billing team has access to Form 2725 and change documentation.

- **No API/technical integration details provided**: This is a policy/document release; architects must separately identify which billing, pricing, or quote systems consume Form 2725 data and design update propagation mechanisms.