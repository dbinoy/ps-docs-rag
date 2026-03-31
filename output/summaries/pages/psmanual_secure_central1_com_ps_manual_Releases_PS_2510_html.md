# Payment Solutions Release 25:10 Summary (April 30, 2025)

- **Release scope**: FX Notes Plus module update clarifying business rules for foreign currency note denomination entry and transaction submission workflows.

- **Key rule change**: Denomination fields are now mandatory and must contain actual currency note denominations when purchasing foreign currency; blank denomination fields with Mixed Notes totals are no longer permitted (removed as valid alternative workflow).

- **Data validation constraint**: The system must enforce that at least one denomination field contains a value before accepting transactions with a Mixed Notes total—validation logic likely resides in the currency volume calculation or transaction submission layer.

- **Affected module/section**: FX Notes Plus Part (Section 10.2, Buying Foreign Currency workflow)—suggests this is part of a larger foreign exchange or treasury management subsystem with denomination-based pricing or risk controls.

- **Documentation update**: Legacy guidance permitting blank denomination fields was removed; architects should verify existing integrations don't rely on that behavior and confirm client applications enforce the new mandatory-field requirement upstream.

- **Escalation path**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) for questions—indicates this change may impact downstream clients; consider monitoring support tickets for integration issues.

- **Architectural consideration**: If denomination fields drive downstream processes (e.g., inventory management, rate calculations, compliance reporting), the mandatory-field change could affect data flow logic and validation rules across connected systems.