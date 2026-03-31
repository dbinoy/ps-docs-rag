# PS 2119 Release Summary (June 16, 2021)

- **Purpose**: Release notes documenting updates to incoming wire routing instructions across multiple currency corridors and introduction of NZD routing documentation.

- **New Currency Support**: Added routing instructions form for NZD (New Zealand Dollar) incoming wires—represents expansion of supported currency pairs for inbound wire transfers.

- **Correspondent & Beneficiary Bank Updates**: Seven existing currency forms (USD, EUR, AUD, CHF, GBP, JPY, MXN, PLN) underwent revision of correspondent bank and beneficiary bank routing information—critical for wire settlement path integrity; suggests either banking relationship changes or routing optimization.

- **Nomenclature Standardization**: Terminology changed from "wire transfer/transfer" to "wire(s)" across all routing instruction forms—indicates potential downstream impact on API contracts, data models, and documentation consistency.

- **Architecture Transition in Progress**: Wires Part is replacing Funds Transfer Part; upcoming revision will consolidate form naming conventions and routing instruction content—signals deprecation risk for any integrations still coupled to legacy Funds Transfer nomenclature.

- **Document Library as Source of Truth**: All routing instruction forms tracked by Document Library ID (9352, 2606, 3710, etc.); architects should treat these IDs as versioned configuration references and design retrieval mechanisms accordingly.

- **Support Contact**: Client Support Services (1-888-889-7878) and support@central1.com for implementation questions—escalation path for ambiguous routing scenarios.