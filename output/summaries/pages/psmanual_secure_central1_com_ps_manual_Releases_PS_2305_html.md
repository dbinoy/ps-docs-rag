# Release 23:05 Summary for Solutions Architect

- **Release scope**: Regulatory update to Country-Specific Guidelines and Instructions (Form 3597) effective March 31, 2023, with synchronized changes deployed to the Wires application

- **Sanctions messaging governance**: Three-tier classification system—removals (Pakistan, Paraguay, Tunisia), additions (15 countries including high-risk jurisdictions like Chad, Marshall Islands, Russia), and updates (4 countries with revised requirements/language), indicating dynamic compliance rule management tied to regulatory/OFAC changes

- **Payment instruction versioning**: Selective country coverage with new instructions for 3 jurisdictions (Namibia, Sri Lanka, The Gambia) and updated instructions for 5 others (Costa Rica, Guyana, Jordan, Pakistan, UAE), suggesting Form 3597 contains variable, country-specific payment routing or processing rules

- **System integration dependency**: Changes "also made in the Wires application" indicates bi-directional or synchronized data model between the primary Payment Solutions system and Wires subsystem—architect must understand data consistency mechanisms and whether Form 3597 serves as single source of truth or requires reconciliation logic

- **Configuration-driven compliance**: Form 3597 structure supports dynamic rule injection (sanctions messages, payment instructions) without apparent code changes, suggesting template-based or rule-engine architecture for country-specific processing

- **Support/change management**: Client-facing updates require downstream communication through documented support channels, implying formal change request and notification workflows that affect SLA/integration schedules

- **Architectural constraint**: No versioning metadata visible (previous Form 3597 state undefined)—architect must clarify whether historical snapshots are maintained for audit/rollback and how downstream systems handle form version dependencies