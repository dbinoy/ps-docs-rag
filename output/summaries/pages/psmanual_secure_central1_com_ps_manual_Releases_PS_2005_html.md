# Release 20:05 (March 4, 2020) Summary: Ontario AFT Clearing File Specifications

- **Release scope**: Publication of AFT clearing file specifications for Ontario region with no functional changes; documentation update for consistency with Central 1's regional specification standards.

- **Core data flow**: Central 1 generates and distributes AFT clearing files to financial institution members for posting transactions to member accounts, including direct deposits and pre-authorized debits originated by the institution or received from other institutions.

- **File types and optionality**: Four specification documents define clearing file formats:
  - CAD and USD variants for standard clearing (mandatory)
  - CAD and USD variants for returns (ONRT/UNRT - optional files)

- **Transaction scope**: Clearing files handle direct deposit transactions, pre-authorized debit (PAD) transactions, and return transactions; origination source can be the receiving institution or a peer institution.

- **Documentation integration points**: Specifications documented in Payment Solutions Manual under Access & Administration Volume, with references in both Section 1.4 (File Specifications Document Library) and Section 5.2 (AFT Clearing File Specifications).

- **Artifact identifiers**: Four specification documents assigned document IDs (9083–9086) for version control and retrieval from the Secure Site repository.

- **Regional constraint**: Ontario-specific file specifications; architects should anticipate similar specification documents may exist or be required for other regions (implied by "all regions" standard).