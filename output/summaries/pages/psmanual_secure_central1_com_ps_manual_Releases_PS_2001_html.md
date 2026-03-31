# PaymentStream® Direct CRA Account Management – Release 20:01

- **Purpose**: Release notes documenting addition of CRA account management capabilities (add/delete) for five specific Canadian tax forms within PaymentStream® Direct, effective January 10, 2020.

- **Scope Limitation**: Functionality applies only when credit unions operate in **member serving state** to process CRA payments/filings directly—does not apply to institutions using the separate **Business Taxes application** for CRA tax processing. This creates a critical architectural constraint: two parallel processing paths exist for CRA transactions.

- **Supported CRA Transaction Types** (five forms):
  - GST/HST 34 Filing and Remittances
  - GST/HST Amount Owing Remittances (Form RC159)
  - GST/HST Interim Payments Remittances (Form RC160)
  - CRA Corporation Taxes (RC159/RC160)
  - Payroll and Source Deductions (Current Year)

- **Documentation Integration Points**: New procedures documented in Chapter 8 of PaymentStream® Direct Part manual (Sections 8.8–8.15), covering account management, individual filing/payment flows, and history viewing—suggests multi-step workflows with state management requirements.

- **Key Architectural Consideration**: CRA account lifecycle (add/delete operations) must be managed at the member level within the member serving state context, implying account-member associations that affect authorization, data validation, and audit trails.

- **No System Integration Dependencies Mentioned**: Page does not reference external CRA systems, file format specifications, or transmission protocols—additional documentation likely required for end-to-end data flow design.