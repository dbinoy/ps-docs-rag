# Summary: Payment Solutions Release 24:05 (January 25, 2024)

- **Scope**: Update to Form 3597 (Country-Specific Guidelines and Instructions) affecting wire payment workflows across Payment Solutions and integrated Wires application

- **Sanctions/Compliance Rules Changed**: Removed sanctions warnings for 8 countries (Albania, Cambodia, Costa Rica, Jordan, Morocco, Sint Maarten, British Virgin Islands, Marshall Islands) and added warnings for 5 countries (Antigua and Barbuda, Belize, Bulgaria, Seychelles, Tunisia)—requires validation layer updates in payment processing pipelines to reflect current compliance posture

- **Payment Instructions Enhanced**: Added new instructions for 4 countries (Bahrain, Kenya, Kuwait, Switzerland) and revised existing instructions for 3 countries (Malaysia, Mexico, Vietnam)—impacts country-specific routing rules, beneficiary bank requirements, and instruction formatting

- **System Synchronization**: Changes deployed simultaneously to Form 3597 documentation and the Wires application—indicates shared data model or dual-write requirement; architects must verify consistency between Payment Solutions core and Wires application

- **Integration Constraint**: Form 3597 serves as source-of-truth for country-level compliance and routing metadata; any enhancement accessing country-specific rules must validate against this document's current state

- **Configuration Management**: Updates are classified as "Revised" status in Document Library, suggesting versioning mechanism exists; architects need to understand release cadence and how clients consume updated country rules

- **Support/Governance**: Changes governed through Client Support Services (1-888-889-7878)—escalation point for clients requiring clarification on country-specific rules or exceptions