# Payment Solutions Release 24:23 Summary (May 16, 2024)

- **Scope**: Updated wire request forms (1171 Outgoing Wire Request, 1799 Contingency Outgoing Wire Request) and Wires Part documentation to enhance sender agreement requirements and clarify error messaging for country-based restrictions.

- **Sender Agreement Changes**: Forms 1171 and 1799 now require explicit sender confirmation of (1) beneficiary permission to include personal information when required by destination country regulations, and (2) absence of deceptive/malicious URLs or harmful content in wire payload—changes propagated to printable receipts in Wires Application.

- **Prohibited Country Validation Logic**: Error messages for country-based restrictions now display *post-submission* (after "Next" button selection) rather than real-time, affecting three validation points: Beneficiary's Financial Institution country (Section 16.3), Sender/Third Party residence country (Section 16.7), and Beneficiary residence country (Section 16.8).

- **Privacy Compliance Integration**: Wire requests must now handle country-specific payment instruction requirements that include personal information—requires upstream consent verification flow and data mapping between beneficiary jurisdiction and payment instruction templates.

- **Enterprise Fraud Management (EFM) System Dependency**: Wires Part now documents that all wire transactions are monitored through Central 1's EFM system; architects must understand EFM integration points for compliance and risk screening workflows.

- **Data Flow Constraint**: Personal information disclosure in wire details requires documented consent chain (sender → beneficiary → confirmation field) before transaction confirmation, creating a new validation gate in the payment processing pipeline.

- **Documentation Updates**: Six sections of Wires Part and two form templates updated; printable receipt templates must reflect new sender agreement fields for audit and compliance records.