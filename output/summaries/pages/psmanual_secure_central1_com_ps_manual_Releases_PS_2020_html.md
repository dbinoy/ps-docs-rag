# Release Notes Summary: Payment Solutions 20:20 (June 15, 2020)

- **Purpose**: Documentation updates to International Transfers product regarding FX spread revenue settlement/reporting and branding compliance requirements

- **Key Technical Updates**:
  - Section 1.4 now cross-references Section 4.1 for FX spread revenue handling in International Transfers
  - Section 4.1 expanded with settlement mechanics and reporting procedures for FX spread revenue (critical for revenue recognition and reconciliation)

- **Implementation Constraint**: Form 9080 (International Transfers Implementation Requirements) updated with clarified branding requirements—architects must ensure form validation and branding rules are enforced during integration workflows

- **Data Flow Impact**: FX spread revenue now requires explicit settlement and reporting processes; architects should verify downstream systems (settlement engines, reporting platforms) can handle this distinct revenue stream separately from primary transfer flows

- **Integration Dependencies**: Changes affect at least three documentation sections (1.4, 3.1, 3.2, 4.1), suggesting coupled business logic across implementation, product setup, and settlement modules—design for loose coupling to isolate future updates

- **Compliance Note**: Branding requirements clarification suggests regulatory or contractual constraints on International Transfers product presentation; architects must incorporate these as non-functional requirements in UI/API design

- **Support Reference**: Client Support (1-888-889-7878, support@central1.com) owns questions—this is a documentation-only release with no system changes indicated