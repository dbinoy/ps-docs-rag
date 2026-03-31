# FYI – March 2021 Summary for Solutions Architect

- **Purpose**: Minor documentation updates to Payment Solutions Manual across three functional volumes (Currency Volume, Electronic Transactions Volume, Document Library) released in March 2021.

- **User Role Clarification (FX Notes Plus)**: Standard user role classification now explicitly documented to encompass all three role types (standard user, cluser, ncluser), affecting access control logic and permission inheritance in FX operations.

- **ATM/POS Deposit Verification Logic**: Cheque verification workflow refined—adjustment requests must target individual non-compliant cheques rather than entire deposit amounts, implying granular transaction-level adjustment tracking rather than batch-level reversals.

- **Document Library Updates**: Two forms versioned (Letter of Direction v2533 with added signature line; CEBA Application Procedures v9140 with FAQ updates in Section 8.3 Reporting Requirements), suggesting external compliance dependencies or regulatory requirement changes.

- **Architectural Implication**: Role-type consolidation and deposit adjustment granularity suggest potential refactoring needs in permission matrices and transaction reversal/adjustment data structures to prevent batch-level processing constraints.

- **Support Dependencies**: Central 1 Client Support Services remains single point of contact (1-888-889-7878 Opt 1 / support@central1.com), indicating external system dependencies for compliance document management and CEBA processing.