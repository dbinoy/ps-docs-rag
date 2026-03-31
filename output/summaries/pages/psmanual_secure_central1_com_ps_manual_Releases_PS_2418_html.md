# Payment Solutions 24:18 Release Summary

- **Release scope**: Documentation update (May 3, 2024) reflecting policy changes to same-day CRA (Canada Revenue Agency) bill payment reversal functionality across multiple system components.

- **Core policy change**: All corporate and personal CRA bill payment reversal requests are **no longer accepted**—this represents a constraint that cascades across three distinct subsystems (Electronic Bill Payments System, CRA Business Taxes, PaymentStream® Direct).

- **Affected data flows**:
  - Bill Payment Reversal Request form (Document ID 1793) now includes a link to CRA billers that cannot be reversed, indicating a whitelist/blacklist lookup mechanism
  - Reversal request workflows previously supported in Section 12.2 (Electronic Bill Payments) and Section 8.1 (Business Tax Payments) are now deprecated

- **Integration dependencies**: The reversal policy affects three interconnected volumes/parts—Electronic Bill Payments System, CRA Business Taxes Part, and PaymentStream® Direct—suggesting shared reversal processing logic or a common CRA biller registry that requires synchronized updates across modules.

- **Architectural constraint**: Designers must implement blocking logic or state validation to prevent reversal requests for CRA transactions; the form now routes to a CRA biller exception list, implying a lookup table dependency during transaction processing.

- **Documentation maintenance burden**: Multiple sections required updates (12.2, 8.1, 12.1) and screenshot replacements, indicating the reversal feature was embedded across different user workflows—new enhancements should centralize reversal eligibility rules to reduce future maintenance.