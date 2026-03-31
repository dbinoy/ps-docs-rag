# Summary: Customizing Wires Elements

- **Overview**: Chapter 4 documents customizable configuration elements within the Wires application for electronic fund transfers, including regulatory compliance fields, fee structures, and user-facing messaging—requires completion of Form 6493 to request changes.

- **Customizable FINTRAC Details**: Sender/beneficiary information collection can be configured as "Always Show" or "Let Logic Decide" (display triggered on EFT Report detection); field set differs for business/entity vs. individual senders, indicating conditional schema logic.

- **Representative/Conductor Details**: Optional section for capturing third-party wire initiator data when sender type = Business/Entity; disabled by default; this is a toggle configuration with no cascading business logic documented.

- **PEP/HIO Determination Questions**: Required regulatory control for wires ≥$100,000 CAD equivalent; can be enabled (mandatory completion, displays in Regulatory section) or disabled (requires offline manual recording); represents compliance workflow state management.

- **Fee Configuration System**: Supports two modes—manual entry or pre-populated; pre-populated fees use tiered lookup logic based on three criteria (Maximum Wire Amount in tiers up to $50K, Wire Currency [CAD/USD/ANY], Destination Country [CA/US/ANY]) with separate Fee Currency output (CAD/USD); add-on fees apply to future-dated/priority wires; manual override capability exists in both modes; **constraint**: requires US dollar Central 1 account for USD fee currency.

- **Message Box Customization**: Four configurable message locations (Create Wire, Confirmation, Receipt pages, and FINTRAC Fields) with unlimited character length but page layout impact; note that printable confirmation/receipt terms & conditions are **non-customizable**, suggesting separate rendering logic for PDF exports.

- **Data Extract Service Integration**: Optional XML/report file export to Central 1 File and Report Exchange for FINTRAC reporting; financial institutions own AML analysis responsibility; cross-border field may display "Verify Manually" when status cannot be determined, creating manual reconciliation dependency.

- **System Dependencies & Constraints**: Central 1 charges monthly processing fees per wire (separate from customer-charged fees); Wires Data Extract Service requires pre-configured access to File and Report Exchange; all customization requests route through centralized change control (Form 6493), indicating no self-service configuration UI documented.