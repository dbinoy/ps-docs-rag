# Summary: 3 Legal Considerations (AFT Settlement)

- **Purpose**: Provides a reference summary of statutes and regulations governing Automated Funds Transfer (AFT) processing and settlement between Canadian financial institutions; explicitly not a substitute for actual regulatory text.

- **Primary Regulatory Body**: Canadian Payment Association (CPA) establishes clearing and settlement rules for member financial institutions; architects must reference official CPA documentation for authoritative requirements.

- **Core AFT Processing Rules** (CPA Rule F1): Defines mandatory procedures for AFT transaction processing and exchange between direct clearers; applies universally to all AFT transactions conforming to CPA Standard 005.

- **Pre-Authorized Debit (PAD) Framework** (CPA Rule H1): Establishes separate procedures for four distinct PAD categories (Business, Cash Management, Funds Transfer, Personal); each category requires compliant clearing and settlement workflows.

- **Data Exchange Standards** (CPA Standard 005): Specifies standardized formats and protocols for financial data transmission on AFT files; this is a critical integration constraint for file structure design.

- **Transaction and Return Code Registry** (CPA Standard 007): Defines enumerated sets of valid AFT transaction codes and return reason codes; architects must maintain a mapping table of these codes for validation logic and error handling.

- **Key Constraint for Design**: Online statute versions carry no accuracy guarantee; the architecture must support versioning and changeability of regulatory rules without requiring code recompilation, and integration points must reference the official CPA ruleset, not this documentation.