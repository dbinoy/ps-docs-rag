# Payment Solutions Release 21:31 Summary

- **Release Focus**: Resolution of e-signature rendering defect affecting OneSpan and DocuSign integrations when using Chrome or Edge browsers, caused by non-embedded Courier font in fillable PDF form fields.

- **Root Cause & Technical Detail**: Courier font (the legacy standard field font) does not embed in PDF documents, causing field content to disappear during e-signature workflows in specific browsers. Font embedding is required for cross-browser e-signature provider compatibility.

- **Breaking Change**: All fillable PDF forms in the document library migrated from Courier to Arial font. Forms page timestamps auto-updated, but individual form revision dates remain unchanged—architects should account for version control implications when querying form metadata.

- **Custom Form Constraint**: Organizations with custom fillable PDF forms using non-embedded fonts must independently remediate using Adobe Acrobat Action Wizard or manual font conversion; Payment Solutions does not automatically update customer-owned documents.

- **Integration Dependencies**: Direct dependency on OneSpan and DocuSign platform support for non-embedded font rendering (both providers working on concurrent fixes), and Adobe PDF specification constraints around font embedding behavior.

- **Operational Consideration**: Recommended backup procedure before font conversion suggests document mutation risks; architects should consider idempotency and rollback strategies if building automated form management features.

- **Support Path**: Product Compliance & Design (PCD) owns form specifications and tooling; integration questions route through phone (604-737-5984 ext. 5984) or email (manuals@central1.com).