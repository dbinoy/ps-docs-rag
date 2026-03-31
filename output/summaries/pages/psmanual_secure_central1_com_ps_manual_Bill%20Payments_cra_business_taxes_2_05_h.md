# Business Taxes User Management Summary

- **Purpose**: Defines procedures for provisioning user access to the Business Taxes module within the Client Centre, including test and production environment segregation.

- **Dual User Management Systems**: Two parallel applications currently manage access—CPS Admin (legacy) and User Management (future replacement)—with CPS Admin Security Officers encouraged to migrate to User Management; this creates temporary technical debt in the architecture.

- **User Type Requirements**: Business Taxes access requires users to be provisioned as either Client Centre Users or CPS Admin Security Officers; CPS Admin changes require Form 1918 (new appointments) or Form 2035 (modifications/deletions).

- **Environment-Specific Access Control**: Four permission flags control environment access via CPS Admin:
  - `PSD-BusinessTaxes` (grants Business Taxes function access)
  - `PSD-Deny` (production blocking flag—must be unchecked to enable production)
  - `PSD-Prev-CompTest` (mirrors production test environment)
  - `PSD-SYS` (pre-production test environment with two-week deployment lead time)

- **Test/Production Segregation Logic**: Test access is optional and independent of production access; removing the `PSD-Deny` flag grants production access while preserving test environment permissions—no flag de-selection required for test-to-prod promotion.

- **External Integration Dependencies**: The module integrates with CRA (Canada Revenue Agency) for filing and payment submission; PaymentStream Direct documentation referenced but not detailed here, indicating dependency on separate user management documentation.

- **Data Flow Constraint**: Production environment submissions route through Central 1 infrastructure; test environments operate independently with PSD-SYS providing two-week visibility into pending production changes.