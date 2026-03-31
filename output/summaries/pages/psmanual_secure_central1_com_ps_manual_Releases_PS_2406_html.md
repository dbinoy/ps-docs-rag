# Release 24:06 (February 7, 2024) Summary

- **Purpose**: Documentation update to Digital & Payment Services Class A Fee Schedule (Form 2725) reflecting service discontinuation and product nomenclature corrections for BC and Ontario Class A credit unions only.

- **Scope Constraint**: Form 2725 applies exclusively to Class A credit unions in BC and Ontario; this release does not affect other member categories or provinces.

- **Removed Capability**: FX Notes Plus priority delivery service and associated fee line item (Section 5.1, Currency Fees) have been discontinued—any downstream integrations or billing systems referencing this fee tier must remove or archive the pricing model.

- **Product Naming Corrections**: 
  - "Self-Serve PAC Reset" renamed to "Self-Serve Reset PAC" (Chapter 16, Cyber Security and Authentication Features)
  - Suggests taxonomy/product catalog updates may be required in downstream API documentation and system configurations

- **Tiered User Calculation Error Fix**: Forge Small Business tier 3 "Active Users" threshold corrected from 20,000 to 10,000 (Section 6.2)—impacts billing logic and user segmentation for small business product tiers.

- **Support Dependency**: Central1 Client Support Services (1-888-889-7878, Option 1; support@central1.com) is the escalation point for implementation questions; no self-service or automated update mechanism indicated.

- **No API/Schema Changes Documented**: Release appears administrative/fee-based rather than technical infrastructure change, but maintain awareness for any downstream billing system mappings tied to Form 2725 structure.