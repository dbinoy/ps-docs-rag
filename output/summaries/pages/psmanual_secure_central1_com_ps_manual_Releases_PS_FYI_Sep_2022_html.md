# Payment Solutions September 2022 Release Summary

- **Purpose**: Documentation updates to Payment Solutions Manual released September 2022, affecting FTP connectivity and flat file specifications for bill payment processing.

- **Direct Connection (SFTP) Constraint**: IP addresses used for SFTP direct connections must be static—a critical requirement for establishing stable, whitelisted connections in production environments.

- **Flat File Format Change**: Data Element 3 in Bill Payment Remittance Processing flat file specifications revised from "C1CU plus 5 spaces" to "C1CU plus 6 spaces" in Table 1—impacts parser logic and field alignment for all remittance file consumers.

- **Integration Point**: FTP/SFTP transport layer is a primary integration mechanism for remittance data ingestion; architects must ensure downstream systems account for the static IP requirement and validate connectivity patterns.

- **Data Flow Dependency**: Bill payment remittance processing depends on correctly formatted flat files; the field spacing change affects file validation, record parsing, and data mapping in downstream systems.

- **Backward Compatibility Note**: The spacing adjustment (5→6 spaces) may create compatibility issues with existing parsers; migration strategy needed for systems processing historical vs. current file formats.

- **Support & Documentation Reference**: Contact Central 1 Client Support (1-888-889-7878, Option 1 or support@central1.com) for clarification on implementation impact before designing systems consuming these data files.