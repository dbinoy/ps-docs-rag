# Release 21:15 (May 26, 2021) - Summary for Solutions Architect

- **Purpose**: Administrative update to FX Notes Plus documentation reflecting contact information and nomenclature changes from Treasury Services and Solutions to Central 1 Support.

- **Contact Integration Point**: All customer-facing contact references now route to `support@central1.com` and phone `1-888-889-7878 (Option 1)`; this centralization may impact support ticket routing and SLA configurations.

- **Nomenclature Change - Critical for Data Models**: Field "Name for CPS" renamed to "Name for User Management" in FX Notes Plus Enrollment forms (document 5898); any systems consuming enrollment data or validating field names against legacy CPS references require mapping updates.

- **Documentation Scope Affected**: Changes span three sections of FX Notes Plus Part (Overview 1.1, Contacts 1.4, Agreements 3.4) and two enrollment/customization documents (5898, 5899); verify all dependent integrations reference updated documentation versions.

- **No Functional Changes**: This is a contact/labeling update only—no API changes, data schema modifications, or business logic alterations; existing FX Notes Plus workflows remain unchanged.

- **Constraint for Architects**: The shift from CPS to User Management terminology suggests potential system architecture change in identity/access management layer; confirm whether backend systems still use CPS identifiers internally or if full nomenclature migration occurred.