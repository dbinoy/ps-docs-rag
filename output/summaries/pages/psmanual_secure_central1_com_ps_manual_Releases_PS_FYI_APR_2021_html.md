# Payment Solutions April 2021 Release Summary

- **Purpose**: Documentation updates to Payment Solutions Manual addressing AFT (Automated File Transfer) processing and document management procedures

- **AFT Access Clarification**: Defined differential access patterns for PaymentStream AFT between financial institutions and business members—architects should understand role-based access controls apply to AFT origination workflows

- **Image File Delivery Integration Point**: Application form (status code 1916) governs enrollment for image file delivery services; now requires FTP home folder name as a mandatory data field for integration setup

- **Form Modernization**: Removed internal-only metadata ("Central 1 Use Only" section) from Application for Image File Delivery—indicates shift toward customer-facing documentation; architects should ensure external form versions don't expose internal operational details

- **PaymentStream Dependency**: AFT originates through PaymentStream subsystem; architects designing AFT enhancements must account for institutional vs. business member access model differences

- **FTP Configuration Requirement**: New FTP home folder name field suggests file delivery systems require explicit directory path specification during client onboarding—this is a new constraint for integration automation

- **Support Contact**: Central 1 Client Support Services (1-888-889-7878 Option 1) owns escalations; architects should reference support@central1.com for clarification on AFT access policies or form requirements