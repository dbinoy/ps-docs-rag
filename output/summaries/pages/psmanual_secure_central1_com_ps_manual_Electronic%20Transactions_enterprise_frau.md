# Settlement Procedures - Technical Summary

- **Scope**: Documents settlement workflows and fraud reporting procedures for three transaction types (Interac e-Transfer, Wire transfers, and EFM-flagged transactions) within the Payment Solutions platform.

- **Interac e-Transfer Settlement**: Delegated to separate documentation (Interac e-Transfer Limits, Settlement, Tracing, and Reports Part); settlement logic not detailed here—reference required for full integration understanding.

- **Wire Transfer Settlement Constraint**: Wire transactions operate outside banking system integration; cancelled wires require manual intervention and custom internal procedures for customer account crediting—no automatic reversal mechanism exists. This is a critical architectural gap for wire processing workflows.

- **EFM Fraud Report Data Structure**: Two-page Excel report containing (1) Aggregated Overview with Operations/Analytics/Losses KPIs for the month, and (2) Alerted Transaction Report with transaction-level details, risk classifications, and institution decisioning on legitimacy. Sorted by transaction date with year-to-date totals.

- **Report Distribution Integration**: Report generated and distributed via Central 1's File and Report Exchange on the 15th of each month (or next business day); available in institution root folder. Architects must integrate file polling or webhook mechanisms to consume this data.

- **Key Architectural Dependency**: EFM fraud detection system feeds alerted transactions to the reporting pipeline—assumes upstream fraud rules engine and transaction classification logic already in place.

- **Multi-tenancy Consideration**: Report distributed to all participating financial institutions; design must support institution-specific folder isolation and access controls on File and Report Exchange.