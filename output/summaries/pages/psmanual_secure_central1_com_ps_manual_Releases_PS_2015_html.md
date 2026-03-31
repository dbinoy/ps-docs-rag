# Payment Solutions Release Summary: Cash Services ServiceNow Integration

- **Release scope**: May 19, 2020 update introducing ServiceNow workflow procedures for Cash Services system, targeting financial institutions migrating from legacy Currency and Coin Order form-based processes.

- **Dual-system architecture**: System operates in parallel modes—migrated institutions use new Cash Services workflows in ServiceNow; non-migrated institutions continue using legacy Currency and Coin Order form until migration completion, requiring conditional routing logic in implementation.

- **Core order management workflows**: ServiceNow integration handles four distinct order types—Standing Orders, Late Orders, Contingency Orders, and cash order location/limits management—with separate workflow definitions per order type.

- **Standing Order state model constraint**: Editing or deleting Standing Orders in Cash Services UI only affects individual occurrences; permanent changes require ServiceNow workflow execution, indicating transaction-level vs. master-record separation in the data model.

- **User and order management data scope**: Cash Services procedures (Form 9031) govern user provisioning, cash order creation, and location/limit management as primary data operations within the system.

- **Documentation and knowledge management**: Form 9031 (Cash Services Procedures Quick Reference) is designated as temporary pending full institutional migration and eventual consolidation into Payment Solutions Manual; training videos provide supplementary procedural guidance.

- **Support integration**: Client Support Services (1-888-889-7878, Option 1; support@central1.com) provides first-line support, indicating external dependency for resolving workflow or system issues.