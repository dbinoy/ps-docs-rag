# PS 2035 Release Summary (September 30, 2020)

- **Purpose**: Documentation update introducing the Excessive Interac e-Transfers Report, a subscription-based compliance tool for detecting suspicious recipient activity patterns in e-Transfer volumes.

- **Key Compliance Use Cases**: Identifies customers receiving abnormally high volumes of Interac e-Transfers; supports detection of illegal gambling activities and AML/KYC compliance workflows.

- **Report Availability Model**: Subscription-based access to the Excessive Interac e-Transfers Report—implies tiered licensing or entitlements management for different customer segments.

- **Documentation Structure Impact**: Two sections updated under "Electronic Transactions Volume" > "Interac e-Transfer Settlement, Tracing, and Reports Part":
  - Section 7.1 (Overview): Added reference paragraph
  - Section 7.5 (New): Dedicated section for report specifications, thresholds, and output schema

- **No explicit data structures or API endpoints mentioned**—review Section 7.5 directly for field definitions, threshold parameters, and output format (likely JSON/XML or scheduled report delivery mechanism).

- **Integration Dependencies**: Report generation likely depends on:
  - Interac e-Transfer transaction ledger
  - Customer recipient identification/matching logic
  - Threshold configuration or anomaly detection rules

- **Support & Escalation**: Client Support (1-888-889-7878, Opt. 2 or digitalbanking_support@central1.com) owns operational questions—escalate policy/threshold changes through this channel.

- **Architect Action Item**: Obtain Section 7.5 documentation to understand report triggering logic, volume thresholds, delivery SLAs, and any downstream compliance systems integration requirements.