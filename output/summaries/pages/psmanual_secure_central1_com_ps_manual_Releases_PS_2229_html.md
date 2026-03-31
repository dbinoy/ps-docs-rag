# Payment Solutions Release Summary: Version 22:29

**Overview:** This release (November 29, 2022) updates sanctions compliance requirements and payment instruction guidelines in Form 3597, with synchronized changes propagated to the Wires application.

**Key Updates:**
- **Haiti sanctions requirement added** to Form 3597 with dual-path notification logic: transaction submission triggers rejection notification to responsible financial institution, with mandatory compliance officer consultation and potential escalation to Global Affairs Canada
- **Pakistan payment instruction revision** introduces new "Purpose of Payment" field requirement, indicating enhanced transaction metadata capture for compliance or audit purposes
- **Form 3597 as compliance instrument** serves as the authoritative Country-Specific Guidelines document; updates reflect evolving regulatory obligations by jurisdiction

**Data Flow & Integration Points:**
- Wires application maintains synchronized state with Form 3597 updates, indicating bidirectional or event-driven integration between document repository and transaction processing system
- Rejection notifications flow from Wires application to responsible financial institutions, requiring notification delivery mechanism for compliance workflows
- Document Library status tracking confirms versioning control for regulatory artifacts

**Architectural Constraints & Considerations:**
- Country-specific rules are configurable per jurisdiction (Haiti, Pakistan examples), requiring rule engine or configuration table supporting dynamic regulatory changes without code deployment
- Compliance validation must occur pre-submission with user-facing warnings; rejection handling post-submission suggests dual-stage validation architecture
- Global Affairs Canada escalation path implies external regulatory body integration or documentation audit trail requirement