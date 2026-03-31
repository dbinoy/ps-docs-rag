# PS 20:12 Release Summary (April 30, 2020)

- **Scope**: Documentation updates to International Transfers product functionality, including new implementation forms and optional FX spread capability.

- **Key Workflow Changes**: Section 1.2 updated International Transfers workflow description; Section 1.3 revised transaction limit constraints—architects should review these constraints before designing transaction processing logic.

- **New FX Capability**: Section 1.4 introduces optional Foreign Exchange (FX) spread configuration allowing financial institutions to apply variable spreads to International Transfers transactions—requires integration point at transaction calculation layer.

- **Form-Driven Configuration**: Two critical forms drive implementation:
  - Form 9080 (International Transfers Implementation Requirements) — mandatory configuration for product setup
  - Form 9111 (International Transfers FX Spread) — optional configuration for FX spread rules
  - These forms represent data input interfaces that must map to backend configuration storage

- **Document Library Restructuring**: Form 8944 (International Transfers Customization) marked obsolete—architects must ensure legacy customization code paths are deprecated and replaced with Form 9080-based configuration model.

- **Data Flow Consideration**: FX spread application implies a new transaction enrichment step in the International Transfers processing pipeline; architects should identify where spread calculations occur relative to authorization/settlement workflows.

- **Support/Operations Contact**: Client Support Services (1-888-889-7878 Option 2 or digitalbanking_Support@central1.com) owns implementation guidance—establish escalation path for design clarifications during architecture reviews.