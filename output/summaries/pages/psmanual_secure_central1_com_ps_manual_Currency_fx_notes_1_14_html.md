# FX Notes Reports Summary

- **Purpose**: Documents user workflows for FX Notes Managers and Auditors to access, filter, and export foreign exchange transaction and profitability data through two distinct report types.

- **Data Retention Policy**: Report data is retained for 25 months—critical constraint for historical queries and compliance requirements; archived data beyond this window is not accessible.

- **Authentication Dependency**: Report access requires prior authentication via FX Notes login process (Section 6.2), indicating role-based access control with at least two permission levels (Manager and Auditor).

- **Report Types & Export Formats**:
  - **Orders Report**: Supports CSV and XLSX downloads; no PDF option mentioned
  - **Profitability Report**: Supports CSV and PDF downloads (conditional availability); filtering requires explicit "Generate Report" action before export

- **Multi-Tenant Filter Architecture**: Both reports implement hierarchical filtering (date range, branches, currency, order type, order status) with branch-level access control, indicating branch isolation is a core data governance model.

- **Profitability Report Additional Fields**: Includes rate type and amount filters beyond Orders report—suggests distinct data schemas and calculation logic separate from transactional Orders data.

- **Browser-Dependent Print Function**: Print functionality relies on native browser capabilities rather than server-side PDF generation for Orders reports, creating potential rendering inconsistencies across browsers.

- **Missing Integration Details**: No mention of API endpoints, scheduled report delivery, alerting mechanisms, or downstream system integrations (accounting, reconciliation platforms).