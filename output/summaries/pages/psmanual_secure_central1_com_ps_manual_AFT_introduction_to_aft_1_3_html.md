# Legal Considerations for AFT Transactions - Summary

- **Page Purpose**: Outlines mandatory compliance frameworks and operational rules governing Automated Funds Transfer (AFT) transactions within the Canadian payment ecosystem.

- **CPA Rules Architecture**: Three primary rule sets govern AFT implementation:
  - **CPA Rule F1**: Core AFT exchange, clearing, settlement, and exception handling procedures between Direct Clearers
  - **CPA Rule H1**: Pre-authorized Debit (PAD) variants—Business PAD, Cash Management PAD, Funds Transfer PAD, personal PAD
  - **CPA Standards 005 & 007**: Data transmission standards and transaction/return reason code catalogs (must reference these for valid code sets in file generation)

- **Regulatory Compliance Dependencies**: PCMLTFA and PCMLTF Regulations apply to financial institutions and agents; AML compliance officer engagement and FINTRAC reporting integration are mandatory prerequisites for AFT service operation.

- **Enhanced Due Diligence Requirement**: New Business Originator applications require financial institution validation of Restricted Entities; Central 1 retains investigative rights and service-denial authority, creating a secondary approval gate in onboarding workflows.

- **Data Exchange Constraints**: AFT file transmission must conform to CPA Standard 005 formats; transaction and return codes must be validated against CPA Standard 007 enumerated values—critical for clearing and settlement validation logic.

- **Scope Boundary**: This section addresses AFT-specific legal considerations only; architects must reference PCMLTFA Compliance Part documentation for comprehensive AML policies, officer appointment procedures, and risk assessment frameworks beyond AFT scope.