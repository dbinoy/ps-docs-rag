# Release Summary: Payment Solutions 20:45 (November 12, 2020)

- **Purpose**: Documentation update reflecting enhancements to the Wires application, including new filtering capabilities and sender identification fields.

- **New Filtering Architecture**: Submitted Wires and Received Wires pages now support multi-dimensional filtering:
  - Submitted: Cross-Border, Amount Range (From/To), Currency
  - Received: Cross-Border, Amount Range (From/To), Currency, Original Amount (From/To), Original Currency
  - Enables cross-border transaction tracking and currency-aware reporting at the UI layer.

- **Data Structure Enhancement**: Member Number field added to Sender section on both Pending Outgoing Wires and Submitted Wires Personal Information pages—establishes sender identity correlation across wire lifecycle states.

- **New Reference Data/Codes**:
  - IBAN Country List Form (9252)—integration point for country-IBAN mapping validation
  - UAE Purpose of Payment Codes (9254)—regulatory compliance codes for UAE wire transactions; suggests regional/jurisdictional code dependencies.

- **Authentication/Security Change**: Removal of biometric references from Chapter 5 (Wires Access and Administration) indicates shift away from biometric authentication; clarify impact on existing authentication integrations.

- **FX Rate Handling**: Wire recall/return scenarios now have defined FX rate application logic—architects must understand rate recalculation dependencies when wires are reversed or recalled.

- **System Boundaries**: Wire submission, approval, and cancellation processes span multiple stateful pages (Pending, Submitted); ensure state management and audit trail integrity across transitions.