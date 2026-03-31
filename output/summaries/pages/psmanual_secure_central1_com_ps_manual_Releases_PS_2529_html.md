# Release Summary: PS 25:29 (December 16, 2025)

- **Overview**: Substantive documentation update to the 2-Step Security Part within the Access and Administration Volume covering authentication mechanisms, token management, and user administration procedures.

- **Key Concept - Token Management**: Two distinct token types are supported—hard tokens and soft tokens—with separate lifecycle procedures (ordering/registration/replacement); soft token replacement is newly documented in Section 4.3, indicating potential process or feature maturation.

- **User Role Definition Update**: "Client Centre Users" and "User Management Security Officers" are now formally defined in Section 2.1; architects should verify these role definitions align with existing identity/authorization frameworks and RBAC implementations.

- **Operational Procedures Revised**: Login procedures (Section 3.1) and soft token registration procedures (Section 4.2) underwent documentation updates with ServiceNow image/UI references, suggesting potential integration with ServiceNow for token lifecycle management.

- **Integration Point - Hypersecu**: New contact information added for Hypersecu in Section 1.2; this indicates a third-party dependency or vendor integration for 2-step security services that should be mapped in the architecture topology.

- **No Data Structure Changes Indicated**: Release focuses on procedural and contact information updates rather than schema, API, or field-level changes; however, architects should confirm whether the new soft token replacement process (Section 4.3) requires backend schema modifications.

- **Constraint for Architects**: All 2-step security enhancements must maintain backward compatibility with existing hard token workflows while supporting expanded soft token capabilities.