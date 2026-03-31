# Payment Solutions Release Summary: Form 1770 Updates (v21:39)

- **Scope**: Updated transmission methods and form structure for the Authorized Signing Officer Signature Update (Form 1770), effective November 2, 2021

- **Transmission Channel Changes**: Form 1770 now accepts submission via ServiceNow ticket attachment or email only; deprecated registered mail and courier delivery methods, simplifying intake workflows

- **Signature Validation Constraint**: "Physical Signature" field requirement explicitly prohibits electronic signatures, necessitating wet-signature collection and storage workflows; impacts document scanning/archival procedures

- **New Optional Data Structure**: Added optional "Signing Officer Restrictions" section to capture financial institution-specific approval authority rules at the form level, eliminating need for out-of-band communication to Central 1

- **Removed Requirement**: Corporate seal section eliminated; reduces form complexity and data entry burden, though architects should verify no downstream compliance or audit processes depend on seal presence

- **Integration Point**: ServiceNow ticketing system is now primary structured intake channel; requires integration with existing ticket routing, tracking, and document attachment workflows

- **Support Dependency**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) owns Form 1770 inquiries; no indication of self-service or automated validation capabilities