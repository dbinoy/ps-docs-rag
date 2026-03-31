# Summary: Payment Solutions Terminology and FAQ

- **Purpose**: Defines 130+ technical terms and concepts for the Electronic Transactions domain, specifically wire transfer operations and regulatory compliance within Central 1's payment infrastructure.

- **Core Wire Transfer Concepts**: Distinguishes between outgoing wires (institution-initiated, beneficiary external) and incoming wires (external-initiated, crediting local institution/account holder), with special categorization for large international wires (≥$10,000 CAD equivalent).

- **Authorization Framework**: Implements two-tier approval model via MTS (Money Transfer System) using Level 1 and Level 2 authorization limits set at branch level; in-branch wires bypass Level 1 threshold and require minimum one approval, while Level 2 requires two approvals regardless of amount.

- **FX Data Structures**: Live rates (not static) used in wire creation with optional spread markup; supports exotic, major, and minor currency classifications; pegged currency handling indicates derivative rate dependencies on external benchmarks.

- **Messaging Standards & Compliance**: Wires application is SWIFT-compliant and Lynx-compatible (Canada's real-time ISO 20022 system); supports IBAN validation via check digits for cross-border payments; rich remittance data capability enables invoice/PO travel with transactions.

- **Regulatory Integration Points**: Multiple AML/CFT touchpoints—FINTRAC reporting, PCMLTFA/Regulations enforcement, PEP screening (domestic/foreign/HIO), large cash transaction thresholds ($10,000 CAD), and jurisdiction-specific regulators (BCFSA, FSRA, DGCM); Enterprise Fraud Management (EFM) system provides ML-based fraud detection requiring manual investigation workflow.

- **User/Access Control Dependencies**: MTS manages wire users and administrators; User Management application handles 2-step security token provisioning; Client Centre serves as digital portal; role separation between Client Centre Users and User Management Security Officers affects operational segregation of duties.

- **System Dependencies**: Relies on ServiceNow for ticketing; transit number format (0 + 3-digit institution + 5-digit branch) is hardcoded identifier; branch settings in MTS control authorization logic, indicating tight coupling between branch master data and wire approval rules.