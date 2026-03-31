# Release 24:28 Summary for Solutions Architects

- **Release scope**: August 13, 2024 update to Wires Part documentation reflecting EFTR (Electronic Funds Transfer Regulation) data extract changes and associated form revisions across outgoing wire workflows.

- **Key process changes**: Enhanced third-party relationship tracking now mandatory in both Sender and Beneficiary sections; regulatory compliance workflow expanded to capture fund collection source (new "Were funds collected by another person or entity?" field requiring conditional detail entry).

- **Data structure expansion**: Forms 1171 (standard) and 1799 (contingency) now capture 10+ new fields including future date capability, wire priority designation, customer type classification, source of funds, face-to-face transaction flag, and FINTRAC additional information fields for enhanced AML/KYC data collection.

- **System integration dependency**: Outgoing wires now flow through Central 1's Enterprise Fraud Management (EFM) system for monitoring; wires flagged as potential fraud are managed within EFM, creating a downstream dependency that architects must account for in wire creation and approval workflows (Sections 29.1, 29.10).

- **Behavioral constraint correction**: Prohibited country residence validation changed from hard error block to warning-only; system no longer prevents wire progression, requiring client-side logic to handle user override scenarios.

- **IBAN validation requirement**: New validation rule added for IBAN check digit validation, indicating enhanced international wire routing validation that may impact beneficiary section processing logic.

- **Critical field dependencies**: Source System field introduced in approval workflows (22.2) to track origination system (MDB/Forge Commercial vs. core Wires application), essential for audit trails and multi-system wire reconciliation.