# Release Summary: PS 26:05 (February 6, 2026)

- **Overview**: Maintenance release updating Form 3597 (Country-Specific Guidelines and Instructions) with sanctions/warning messages, payment instructions, and data corrections across 40+ countries.

- **Key Concept - Form 3597**: The system maintains country-indexed compliance metadata that governs payment processing rules; this form serves as the authoritative reference for country-level payment constraints and regulatory warnings.

- **Sanctions/Warning Message Logic**: New conditional flags added for 39 countries (Argentina through Uzbekistan); these likely trigger compliance checks at payment initiation or settlement stages and may require user acknowledgment or transaction blocking.

- **Payment Instructions Data Structure**: Country-keyed payment method specifications that were corrected for Democratic Republic of the Congo (removed) and Republic of the Congo (added)—indicates instructions are country-specific and may be linked to banking corridors, settlement accounts, or routing rules.

- **Data Integrity Issue Identified**: Instructions were initially misattributed between Congo entities; architects should verify reconciliation logic for multi-country payment flows and consider validation gates to prevent similar cross-country mapping errors.

- **Integration Dependencies**: Form 3597 updates likely propagate to payment processing engines, compliance screening modules, and client-facing instruction sets; verify change management procedures for downstream system impacts.

- **Support Contact**: Client Support Services owns implementation questions (1-888-889-7878, support@central1.com); escalation path for production issues should be established pre-deployment.