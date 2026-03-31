# Release Summary: Payment Solutions 25:12 (May 20, 2025)

- **Release scope**: Updates to United Kingdom payment instruction documentation, affecting wire transfer processing and country-specific payment code requirements as of May 20, 2025.

- **Modified documentation**: Form 3597 (Country-Specific Guidelines and Instructions) revised for UK payment instructions; updates integrated into Section 14.4 of the Electronic Transactions Volume and Section 1.6 Wires Document Library.

- **New data structure**: Form 10117 introduced as a new reference document for "United Kingdom – Purpose of Payment" codes, indicating a new or restructured payment purpose classification system specific to UK wire transactions.

- **Integration dependency**: Wire transfer processing logic must reference the updated Section 1.6 Wires Document Library and validate against the new Form 10117 purpose-of-payment codes before routing UK-destined transactions.

- **Geographic constraint**: These updates apply specifically to United Kingdom payment corridors; architects should implement region-specific validation logic that enforces Form 10117 compliance for UK wire instructions.

- **Documentation governance**: Two separate forms manage this domain—Form 3597 (instructions/guidelines) and Form 10117 (code reference)—suggesting a split between procedural documentation and lookup/validation data; consider data synchronization between these sources.

- **Support escalation path**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) is the contact for implementation questions and issue resolution.