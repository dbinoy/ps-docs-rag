# FYI – March 2023 Summary for Solutions Architect

- **Purpose**: Documentation of March 2023 updates to the Payment Solutions Manual, including deprecation notices and document revisions.

- **Service Discontinuation**: Western Union Money Transfers via Interac e-Transfer (Online International Remittances/OIR) has been decommissioned; all related settlement, tracing, and reporting documentation removed from the manual.

- **Integration Impact**: Any downstream systems, reconciliation processes, or reporting workflows dependent on Western Union/OIR money transfer settlement logic and trace files should be assessed for removal or refactoring.

- **Document Update**: Payors' PAD (Pre-Authorized Debit) Agreement documentation (Status ID 1696) revised to remove redundant page references in Terms and Conditions (Sections 4, 7a), affecting the normative agreement structure clients reference.

- **Data Flow Consideration**: Electronic Transactions Volume section no longer includes Western Union settlement data flows; audit trails and transaction classification rules may need updates to exclude OIR transaction codes.

- **Compliance**: Changes to PAD Agreement terms require version control awareness—architects should confirm client systems have updated to the latest agreement version to avoid contract-system misalignment.

- **Support Contact**: Central 1 Client Support Services (1-888-889-7878 Option 1, support@central1.com) maintains authority on interpretation of manual changes and their implementation scope.