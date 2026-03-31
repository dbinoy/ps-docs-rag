# Release 23:20 Summary for Solutions Architect

- **Overview**: August 28, 2023 release focused on UI/UX updates to Incoming Wires Routing Instruction forms and migration of all login procedures from legacy secure site to Client Centre authentication system.

- **Authentication Migration**: All login procedures updated across MTS, CPS Admin, and Wires modules now route through Client Centre. New "Client Centre" and "Client Centre User" definitions added to Section 2.1—verify integration with Client Centre IAM/RBAC if designing auth-dependent features.

- **Wires Data Extract Service**: Added requirement for manual AML review of cross-border wires flagged with "Verify Manually" status (Section 4.4). Clarified that extracts contain *all* wires—important for filtering logic and downstream compliance workflows.

- **Form Layout and Field Standardization**: Nine routing instruction forms (CAD domestic/international, USD, EUR, AUD, CHF, GBP, JPY, MXN, PLN, NZD) standardized with updated layout for beneficiary FI route/transit and account number fields. Forms now include mandatory completion reminders—consider validation rules and data quality gates to prevent delays/returns.

- **Settlement Scope Expansion**: BC and Ontario settlement procedures now explicitly include "Other Central 1 clients" (Sections 26 and 28.1)—clarify client classification logic and inter-branch transfer routing if designing settlement or inter-institution workflows.

- **Wire Amount Logic Refinement**: US dollar wires to other Wires-participating institutions no longer require US correspondent bank (Section 17.4)—impacts wire routing decision trees and correspondent bank selection logic.

- **Structural Reorganization**: Wires search/reporting functionality moved to new Section 20.4 with downstream chapter renumbering—verify all documentation references and API endpoints are updated if exposing search/reporting via services.

- **New ISO Standard**: ISO 20022 Return Code Definitions (Form 9610) added to Document Library—confirm alignment with outgoing wire return handling, recall/amendment workflows, and error reporting integrations.