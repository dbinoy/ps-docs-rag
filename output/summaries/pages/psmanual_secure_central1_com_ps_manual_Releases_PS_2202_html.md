# Release 22:02 Summary — January 12, 2022

- **Scope**: Correction to Digital & Payment Services Class A Fee Schedule (Form 2725) addressing erroneous pricing data published December 30, 2021.

- **Data correction**: Deposit Anywhere pricing was corrected across multiple sections of Form 2725; the December 30 publication inadvertently reflected a price increase when no actual fee change occurred for 2021 baseline rates.

- **Key artifact**: Form 2725 is the authoritative fee schedule document for Digital & Payment Services Class A offerings—architects must treat this as a master reference for pricing configurations and ensure downstream systems (billing, quote generation, customer portals) reflect corrected values.

- **Affected service**: Deposit Anywhere is explicitly called out; verify this service's pricing logic in downstream systems and confirm no billing cycles were processed using the erroneous December 30 rates.

- **No structural changes**: This is a data correction only—no schema, API contract, or process flow changes are indicated; however, any caching layers or pricing lookup systems may require invalidation.

- **Constraint**: Architects should implement versioning or audit trails for fee schedules to prevent similar silent updates from propagating undetected to dependent systems.

- **Support escalation**: Client Support Services (1-888-889-7878, Option 1, or support@central1.com) is the contact for questions—flag customer impact assessments through this channel.