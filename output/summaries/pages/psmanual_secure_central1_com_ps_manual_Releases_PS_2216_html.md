# Release 22:16 Summary – May 19, 2022

- **Overview**: Documentation update reflecting Western Union Business Solutions' corporate rebranding to Convera, with corresponding updates to FX Drafts and Clearing/Deposits functionality documentation.

- **Scope of Changes**: Business references, contact information, and regulatory/operational forms updated across FX Drafts Part documentation; no functional logic changes indicated, primarily nomenclature and contact data updates.

- **Document Versioning**: Four core documents affected with mixed publication status—two rebranded documents already published (9182, 9183, 9515), two pending rebranded versions (9189, 9190)—requiring tracking of document IDs for version control and client distribution.

- **Key Integration Point**: Convera partnership/integration within FX (Foreign Exchange) Drafts workflow; architects must account for potential downstream changes in Convera's APIs, forms, or service agreements that could impact draft processing, clearing, or deposit reconciliation flows.

- **Contact/Support Changes**: Section 1.3 updated with new Convera contact information (phone: 1-888-889-7878 Option 1; email: support@central1.com); support escalation procedures may differ post-rebranding.

- **Constraint**: Remote Draft Print Testing Guidelines (9515) and Desktop Draft Stock Order (9189) document updates have staggered delivery; architects should confirm document availability before designing client-facing features dependent on these materials.

- **Data Structure Consideration**: FX Drafts Part references suggest structured form data and MICR (Magnetic Ink Character Recognition) processing—validate that rebranded forms maintain backward compatibility with existing MICR parsing and draft transmission pipelines.