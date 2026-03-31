# Summary: Legal Considerations and Policies for Incoming and Outgoing Wires

- **Overview**: Documents regulatory compliance requirements and mandatory internal control policies for wire transfer operations (incoming/outgoing) under Canadian financial services law.

- **Regulatory Compliance Framework**: Financial institutions must adhere to PCMLTFA/PCMLTF Regulations, Criminal Code, PIPEDA/PIPA, Freezing Assets of Corrupt Foreign Officials Act, Human Rights Code, and Economic Sanctions—with FINTRAC as primary enforcement/guidance body.

- **Mandatory Policy Domains**: Staff must be trained on identity verification, suspicious transaction reporting, record-keeping/FINTRAC reporting, terrorist property reporting, split transaction monitoring, PEP/HIO determinations, foreign currency exchange processing, and non-account holder transactions.

- **Enterprise Fraud Management (EFM) Integration**: Outgoing wires are monitored asynchronously in EFM; wire status in the Wires application updates to "Pending" (investigation) or "Cancelled" (fraud identified) with no user-visible reason codes—only authorized EFM users see investigation details. **Critical constraint**: Wires application is not connected to the banking system; settlement must be reconciled via internal procedures.

- **Wire Status Semantics**: Understand status transitions—"Pending" indicates EFM fraud investigation in progress; "Cancelled" indicates EFM fraud determination—but no status reason field is exposed to Wires application users.

- **Access Control Requirements**: Implement role-based access restrictions, one-time secure password distribution, inactive user deactivation, transaction/daily limits per user, two-approval authorization thresholds for high-value outgoing wires (institution-defined), and audit trails for compliance review.

- **Data Isolation Risk**: Wires application operates as isolated system from core banking; architects must design reconciliation/settlement workflows to close the gap between fraud decisions in EFM and actual transaction reversal/customer communication.