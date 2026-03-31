# Summary: Wires Settlement (Section 26)

- **Purpose**: Defines settlement account flows and timing for incoming and outgoing wire transactions across Central 1's payment network, with regional variations for BC/Ontario vs. other provinces.

- **Settlement Timing**: Near real-time processing for BC/Ontario institutions to Central 1 current accounts; minutes unless manual compliance review required. Subject to cut-off times defined in Section 14.7.

- **Account Routing Logic**: 
  - Outgoing wires (CAD or foreign) debit Canadian dollar account; US dollar outgoing wires debit US dollar account (if held with provincial central)
  - Incoming wires credit matching currency account; non-matching currencies converted to CAD
  - Regional split: BC/Ontario route to Central 1 current account; all other provinces route to provincial central account

- **Fraud/Sanctions Integration Dependencies**:
  - EFM (Enterprise Fraud Management) system flags potential fraud; wires remain "Pending" until resolution—settlement only occurs on "legitimate" confirmation, not on fraud detection
  - Sanctioned list matches held at Central 1 pending investigation; funds remain debited but not settled until cleared
  - Manual compliance review can delay settlement; no API connection between Wires application and client banking systems

- **Fee Structure**: All wires assessed processing fees at month-end; currency of fee posting matches transaction currency and account held (CAD or USD), not uniform billing model.

- **Critical Constraint for Architects**: Wires application has no direct banking system integration—institutions must manually reconcile fraud-flagged or legitimized wires through their own internal procedures; this creates a manual handoff gap requiring compensating controls.