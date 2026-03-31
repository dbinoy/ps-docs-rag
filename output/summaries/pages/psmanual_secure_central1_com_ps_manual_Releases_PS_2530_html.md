# Summary: Payment Services Class A Fee Schedule Update (25:30)

- **Purpose**: Documents fee schedule updates to Payment Services Class A Form 2725, effective January 1, 2025, following vendor price increases in fraud advisory services and standardized wire transfer pricing.

- **Affected Services & Scope**: 
  - Updates to Section 6.2 (Fraud Advisory Services - optional services only)
  - Section 2.8 wire transfer fees now align pricing: "Outgoing Wires Other Currencies" equals "Outgoing Wires to Canada (CAD)"
  - Form 2725 applies exclusively to BC and Ontario Class A credit unions

- **Key Data Structure**: Payment Services Class A Fee Schedule (Form 2725) maintains hierarchical fee organization by service category (sections 2.8, 6.2, etc.), indicating modular fee tables that may require version control or conditional pricing logic.

- **Upstream Dependencies**: Fee schedule updates were announced in the "2026 Indicative Pricing for Payment Services" notice (September 22, 2025), suggesting a formal pricing announcement cycle that precedes implementation.

- **Vendor Integration Point**: Third-party fraud advisory services vendor pricing changes cascade directly into Form 2725, requiring contract management integration and change notification workflows.

- **Architectural Constraint**: Optional service fees (Section 6.2) and fixed fees (wire transfers) must be independently configurable to handle selective adoption by credit unions; pricing rules cannot assume universal service availability.

- **Support & Governance**: Changes managed through Client Support Services (1-888-889-7878), indicating centralized fee schedule administration rather than distributed updates.