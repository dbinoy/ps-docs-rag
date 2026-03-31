# Payment Solutions 21.14 Release Summary

- **Release Focus**: Documentation clarification on Currency Ordering cash delivery location constraints (May 11, 2021)

- **Key Business Rule**: Cash order locations are restricted to branch or ATM addresses only; alternative delivery locations (e.g., customer sites) require manual post-delivery arrangements outside the Payment Solutions system

- **Affected Documentation Sections**: 
  - Currency Ordering Part, Section 4.3 (Creating a Cash Order Location)
  - Currency Ordering Part, Section 4.4 (Updating a Cash Order Location or Limit)

- **Data Constraint**: The cash order location entity must validate against a predefined set of location types (branch, ATM) at both creation and update operations; no free-form address fields permitted for order fulfillment

- **Integration Implication**: RBC delivers cash only to validated branch/ATM addresses; downstream out-of-system workflows required for non-standard delivery scenarios, creating a manual handoff dependency

- **No System Changes Indicated**: This is a documentation-only release; no data model, API, or application logic modifications mentioned—existing system behavior remains unchanged

- **Contact/Support**: Client Support Services available for clarifications (1-888-889-7878 Option 1, support@central1.com)