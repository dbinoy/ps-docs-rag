# FX Notes Documentation Summary

- **Purpose**: FX Notes enables authorized financial institution users to transact foreign currency bank notes (excluding coins and CAD notes) via Central 1's Client Centre, partnered with Globex 2000 as the fulfillment provider.

- **Key Operational Constraints**: Service operates 7:30 AM–9 PM ET daily with live exchange rates; orders placed after 3 PM ET (12 PM PT) process the next business day; Globex 2000 support unavailable on Quebec provincial holidays, creating potential SLA gaps.

- **Exchange Rate Management**: Users can download daily rate pages, but rates are locked at order time; organizations must manage FX risk internally via configured spreads—this implies a retail rate modifier system (referenced in Section 7.1) that requires architectural support for rate distribution and modification workflows.

- **Integration Dependencies**: System integrates with Current Account Services (CAS) Online, CPS Admin Application, File Exchange and Report Distribution, and User Management modules; depends on external Globex 2000 systems for delivery logistics, settlement processing, and technical support; FINTRAC integration required for compliance reporting (Large Cash Transaction Reports, Suspicious Transaction Reports).

- **Access Control & Enrollment**: Role-based authorization required; enrollment managed by Central 1 Client Support Services; architecture must support CPS Admin Appointment Certificate (form 1918) for role assignment and CPS Admin Modification/Deletion Request (form 2035) for lifecycle management.

- **Regulatory & Compliance Touch Points**: PCMLTFA compliance requirements differ by province (BC/ON); Operations Manual Program subscription model affects documentation visibility and creates potential architecture friction for form/template management across subscriber/non-subscriber tiers.

- **Multi-Tenant Considerations**: Separate procedures for BC/Ontario credit unions vs. non-member institutions; Fee Schedule (form 2725) available only to Class A credit unions, indicating tiered product offerings that require segmentation logic in data models and access controls.