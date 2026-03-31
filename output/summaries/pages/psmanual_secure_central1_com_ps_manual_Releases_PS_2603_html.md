# Release 26:03 (January 21, 2026) Summary

- **Overview**: Documentation update addressing FX Notes product rebranding and new User Management procedures for FX Notes user provisioning and administration.

- **Key Concept - FX Notes Rebranding**: Product formerly called "FX Notes Plus" renamed to "FX Notes" across all documentation; all references updated in the Currency Volume. Implies backend product naming conventions may have changed—verify if this affects API endpoints, service identifiers, or licensing modules.

- **New Terminology**: "Unlisted Transit" defined in User Management terminology (Section 2.1). Architects should clarify business logic implications for currency routing or transaction classification if this term represents a new data flow or processing path.

- **Integration Point - User Management Application**: New Section 8.1 establishes FX Notes user management capability within the User Management system. This suggests a cross-module dependency requiring role-based access control (RBAC) integration and likely database schema updates to support FX Notes-specific user attributes or permissions.

- **Documentation Structure Change**: Section renumbering in Access and Administration Volume indicates structural reorganization. Architects should verify that internal cross-references, API documentation, and integration guides reflect updated section numbering to avoid broken dependencies.

- **Affected Subsystem - Currency Ordering**: Section 12 updates in "Currency Ordering and Precious Metals" document indicate FX Notes integration with order placement workflows. Potential data flow implications for order initiation, validation, and fulfillment processes.

- **No New Data Structures Mentioned**: This release does not introduce new fields, codes, or data models—it is primarily a nomenclature and documentation update. Verify backend schema alignment with rebranding in production systems.