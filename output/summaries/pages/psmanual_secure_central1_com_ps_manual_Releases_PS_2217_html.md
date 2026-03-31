# Release 22:17 Summary for Solutions Architect

- **Purpose**: Documentation updates clarifying biller enrollment requirements and processes for Central 1's Electronic Bill Payments (EBP) System as of June 24, 2022.

- **Key Enrollment Constraint**: Billers must be pre-registered with a financial institution before being added to the EBP System; this is a mandatory due diligence and security requirement, not optional.

- **Multi-Institution Enrollment Flow**: Billers registered with institutions other than the enrolling FI must initiate enrollment through their own FI, which then sends enrollment data to Central 1 to facilitate cross-institution setup—this creates an asynchronous, multi-party data exchange dependency.

- **Form 1320 (Biller Enrollment Request)** includes "Account Validation Rules" field with clarified information requirements; this is a critical data structure for biller configuration and must be properly validated during enrollment.

- **Regional Data Model Variation**: Ontario FIs use 9-digit vendor numbers with separate viewing/lookup mechanisms (Bill Payment Vendor Information vs. EBP Billers Listing), indicating schema or vendor identification differences that require location-aware logic.

- **Integration Point**: Biller enrollment information flows between external FIs and Central 1's system; architects must design for receiving and processing enrollment data from peer institutions, not just internal requests.

- **Vendor Reference Update**: Bill Payment Reversal Request document (Form 1793) references vendor/biller data; biller name changes indicate master data synchronization requirements across documents and potentially across linked systems.