# Service Charges Documentation Summary

- **Purpose**: Documents the fee structure and billing mechanics for Central 1's Payment Services offerings to Class A credit unions in BC and Ontario, governed by Form 2725.

- **Billing Model**: Monthly fee collection with currency-specific posting—CAD charges post to CAD current accounts; USD charges post to USD current accounts at month-end, or convert to CAD if no USD account exists.

- **Geographic & Membership Constraints**: Form 2725 and associated fees apply exclusively to Class A credit unions in British Columbia and Ontario; other jurisdictions or membership classes are out of scope.

- **Dual Support Channels**: Separate escalation paths exist for Payment Services fees (Option 1: support@central1.com) and digital banking fees (Option 2: digitalbanking_support@central1.com)—architects should route billing inquiries accordingly.

- **Document Registry**: Form 2725 (PDF format) is the single source of truth for product/service pricing; any system enhancement must reference this form and maintain version alignment.

- **Currency Conversion Dependency**: USD-to-CAD conversion logic is triggered when a member institution lacks a USD current account—architects must validate this fallback path in billing engines and reconciliation processes.

- **Account Posting Integration**: Billing system must interface with Central 1's current account ledger system to post monthly charges; assumes standardized account coding and month-end cutoff procedures.