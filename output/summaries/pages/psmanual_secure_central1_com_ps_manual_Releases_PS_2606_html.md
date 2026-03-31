# Summary: Payment Services Class A Fee Schedule Update (26:06 - March 03, 2026)

- **Scope**: Maintenance release updating Form 2725 (Payment Services Class A Fee Schedule) applicable exclusively to BC and Ontario Class A credit unions; primarily fee schedule reorganization with minor corrections and one new fee category.

- **Key Fee Schedule Changes**:
  - Section 1.3: Remote Deposit Capture fees reorganized (Corporate Capture subsection) with no rate modifications
  - Section 2.5: New fee category "Electronic Bill Payments – Billers with Non-Standard Pricing" introduced; pricing matrix references Form 10183 (Billers with Non-Standard Pricing)
  - Section 5.1: Minimum fee corrected for USD note returns
  - Section 9.1: Deposit Anywhere API fees aligned to match Section 1.3 Remote Deposit Capture rates (fee parity requirement)
  - Chapter 7: Origination Solutions Fees section removed entirely

- **Critical Dependencies**: Electronic Bill Payment processing now depends on Form 10183 for identifying billers with non-standard pricing; this creates a dynamic reference requirement between fee schedules.

- **API/System Integration Point**: Deposit Anywhere API fee calculation must maintain real-time parity with Mobile Remote Deposit Capture fees (Section 1.3), requiring either unified fee lookup or synchronization mechanism between fee modules.

- **Jurisdictional Constraint**: Form 2725 restricted to BC and Ontario Class A credit unions only; system must enforce geographic/institution-type filtering for applicable fee schedules.

- **Architect Consideration**: Removal of Chapter 7 (Origination Solutions) suggests either deprecation of product line or restructuring; verify downstream dependencies in pricing engines and product configuration before implementing.