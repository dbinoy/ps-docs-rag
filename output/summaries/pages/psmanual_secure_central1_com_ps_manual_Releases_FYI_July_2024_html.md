# FYI – July 2024 Summary for Solutions Architect

- **Purpose**: Documentation updates to Payment Solutions Manual and Document Library released in July 2024; includes new report examples and revised error code definitions.

- **AFT Volume Update**: Section 3.23 now includes example of ICDR/UCDR (Interac e-Transfer / Universal Credit/Debit Return) batch return report, clarifying data delivery structure for AFT transactions.

- **Bill Payments Volume Update**: Section 12.3 added TXMC (Tax Payments Monthly Billing) report example for CRA business tax payments, establishing billing reconciliation reference documentation.

- **ISO 8583 Integration Error Handling**: Error code 997 added to Response Codes documentation (9346) to indicate transaction timeout when user fails to complete transaction within 5-minute window; applies to ISO 8583-based integrations.

- **ISO 20022 Integration Error Handling**: Identical error code 997 added to Response Codes documentation (9347) for ISO 20022-based integrations with same timeout constraint and semantics.

- **Critical Constraint**: 5-minute user session timeout is enforced across both legacy (ISO 8583) and modern (ISO 20022) integration paths; error handling must distinguish timeout failures from other failure modes.

- **Documentation Dependencies**: Architects should reference updated report examples in Sections 3.23 and 12.3, plus revised response code tables (9346, 9347) when designing reconciliation, monitoring, or error recovery logic.