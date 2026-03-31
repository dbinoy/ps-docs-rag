# PS 2027 Release Summary (August 21, 2020)

- **Release scope**: Introduced new Currency Ordering Part consolidating cash services procedures for BC and Ontario regions with ServiceNow integration for request management.

- **Key process redesign**: Migrated from legacy Cash Parcel Online Ordering System (Ontario) and Currency Ordering System (BC) to unified Currency Ordering Part, indicating architectural consolidation across regional implementations.

- **System integration point**: New Cash Services system integrates with ServiceNow for process workflow management; architects must account for bidirectional data synchronization and request state management between ordering and ticketing systems.

- **Regional data handling**: Dual-region support (BC/Ontario) requires partitioned configurations or feature flags; BC credit unions have elevated permissions (Extended Supervisor Request 6134 now obsolete), suggesting role-based access control changes.

- **Reference documentation structure**: User Management Part (Section 9.4) now contains Cash Services procedures; architects should verify documentation dependencies and ensure API contract stability for downstream integrations.

- **Document deprecation cascade**: Four legacy documents marked obsolete (1782, 6134, 9031, 1390 revised); migration path required for existing integrations referencing old ordering system IDs and request codes.

- **Support model**: Single support contact (1-888-889-7878, support@central1.com) suggests potential for unified ticketing; architects should clarify escalation procedures and SLA definitions for cash services requests.