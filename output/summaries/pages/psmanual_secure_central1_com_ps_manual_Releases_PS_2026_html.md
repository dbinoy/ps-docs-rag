# Release 20:26 (August 18, 2020) – Summary for Solutions Architect

- **Overview**: Documentation update for FX Notes Plus component reflecting courier service migration from UPS to FedEx and removal of AMEX traveler cheques processing capability due to EBC policy change.

- **Key Process Changes**: 
  - Shipping carrier changed to FedEx with temporary operational constraint: foreign cash services restricted to two-day delivery (vs. historical overnight)
  - AMEX traveler cheques workflow completely removed from system; no longer processable effective immediately
  - Collection items processing clarified: items paid only after complete clearing confirmation; no dishonored/returned status possible

- **Critical Data Element**: FedEx account number **310492418** hardcoded in system—verify this is stored as configuration parameter rather than hardcoded literal to enable account migration scenarios.

- **Affected Modules/Sections**:
  - Chapter 7: Foreign currency/draft selling (shipping methods & timelines)
  - Section 11.4: Foreign cheque shipping procedures
  - Section 11.5: Dishonoured/returned cheque handling logic
  - Chapter 13: Foreign currency shipping (AMEX references removed)

- **Integration Dependencies**: External dependency on FedEx service availability and two-day delivery SLA; no documented fallback carrier if FedEx service degrades.

- **Backward Compatibility Risk**: Removal of AMEX traveler cheques processing may impact legacy integrations or stored procedures that reference this workflow—audit for orphaned code paths.

- **Support Contact**: Client Support Services (1-888-889-7878, Option 1 or support@central1.com) owns operational questions.