# Release 25:04 Summary (February 6, 2025)

- **Release scope**: Documentation update expanding Currency Ordering Part to include precious metals operations for Class A financial institutions in BC and ON regions.

- **New capability**: Precious metals purchase and sell-back functionality enabling customer investment diversification—requires understanding regional compliance constraints (BC/ON Class A institutions only) and potential tier-based access controls in the system.

- **Key operational processes defined**: Policies, purchasing workflows, sell-back sales, shipment verification, shipment packaging, and settlement procedures—architect should identify where these workflows integrate with existing currency ordering systems and settlement engines.

- **Documentation structure change**: "Currency Ordering Part" renamed to "Currency Ordering and Precious Metals Part" with new Chapter 14 dedicated to precious metals—impacts navigation, API documentation references, and any system modules using hardcoded section identifiers.

- **Data flow consideration**: Precious metals transactions likely require parallel handling to currency transactions in ordering, inventory, and settlement systems—architect must determine if existing ledger/settlement architecture supports dual asset types or requires schema extensions.

- **Institutional eligibility gating**: Class A institution classification tied to provincial location (BC/ON)—requires validation logic during customer onboarding and product eligibility checks; may need new institution attribute in customer/institution data model.

- **Support channel**: Client Support available via 1-888-889-7878 (Option 1) or support@central1.com—indicates downstream support dependencies for troubleshooting integration issues.