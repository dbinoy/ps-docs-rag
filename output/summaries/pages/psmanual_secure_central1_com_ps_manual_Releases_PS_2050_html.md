# Payment Solutions Release Summary: Version 20:50 (December 31, 2020)

- **Release scope**: FX Notes Plus application update restricting foreign currency draft purchases to USD only, effective January 1, 2020, per Exchange Bank of Canada directive.

- **Currency constraint**: Single-currency model implemented—USD is now the exclusive currency supported for draft purchasing through FX Notes Plus; multi-currency logic previously in Sections 7.2 must be refactored to reflect this constraint.

- **Affected functional areas**: Four manual sections updated (7.2, 7.6, 7.7, 7.8) covering currency availability, order cancellation workflows, draft selling, and pending draft review processes—suggests these workflows contain currency-dependent logic requiring validation layers.

- **External dependency**: Exchange Bank of Canada acts as the authoritative source for currency availability rules; architectural changes are policy-driven rather than feature-driven, indicating need for externalized configuration or policy service to handle future currency rule changes.

- **Documentation artifacts**: Training videos and manual sections revised concurrently, indicating tight coupling between application behavior and user-facing documentation—consider versioning strategy for content delivery.

- **Integration implications**: FX Notes Plus operates as a distinct subsystem with order management, cancellation, and review capabilities; any enhancement must account for downstream settlement systems and draft lifecycle management.

- **Support escalation**: Client Support Services owns change communication; architects should anticipate support load during transition period and confirm backward compatibility or deprecation messaging for clients with multi-currency workflows.