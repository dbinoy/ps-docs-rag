# Payment Solutions Release Summary: PS 25:05

- **Purpose**: February 21, 2025 release documenting updates to Digital & Payment Services Class A Fee Schedule (Form 2725), applicable exclusively to BC and Ontario Class A credit unions.

- **Fee Schedule Updates**: Two sections modified in Form 2725:
  - Section 2.3 (ATM and POS Fees): Updated "Traces on Transactions" description
  - Section 5.1 (Currency Fees): Implemented Bank of Canada fee increase for new Canadian dollar notes effective January 1, 2025

- **Regulatory Dependency**: Form 2725 is subject to Bank of Canada fee structure changes; architects must implement configuration mechanisms to accommodate external regulatory fee updates without full releases.

- **Geographic Constraints**: Fee schedule applies only to Class A credit unions in British Columbia and Ontario; multi-region deployments require institution-type and jurisdiction validation logic.

- **Document Control**: Form 2725 status changed to "Revised" in Document Library; suggests versioning/audit trail requirements for regulatory compliance tracking.

- **Support Integration**: Client Support Services (1-888-889-7878 Option 1 / support@central1.com) manages inquiries; escalation workflows may be needed for fee-related customer disputes.

- **Architecture Consideration**: Fee table updates appear manual/administrative; evaluate whether to implement dynamic fee configuration endpoints or maintain static scheduled deployments based on regulatory notice cycles.