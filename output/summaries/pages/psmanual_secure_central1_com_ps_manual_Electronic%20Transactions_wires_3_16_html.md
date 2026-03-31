# Summary: Creating a Regular Wire (Page 16)

- **Purpose**: Procedural documentation for creating outgoing wires in the Wires application, covering branch selection, beneficiary institution lookup, amount/currency configuration, intermediary routing, and priority/scheduling options.

- **Key Data Flow**: Sending Branch → Beneficiary FI (via SWIFT/transit/ABA routing) → Wire Amount/Currency → Intermediary (conditional) → Sender Details → Priority/Schedule → Confirmation, with Central 1 debiting the selected branch and calculating final FX rates at transaction completion.

- **Critical Field Dependencies**:
  - Wire Priority and Future Date sections only render if beneficiary FI is in Canada AND currency is CAD
  - Intermediary Financial Institution field is conditional: required for non-domestic currency pairs (e.g., GBP→France) or when beneficiary FI mandates it; optional for domestic currency routing
  - Currency dropdown availability is constrained by beneficiary FI country
  - Sender address must be physical (PO Boxes rejected)

- **Compliance & Risk Gates**:
  - Country-based screening triggers warnings for tax haven/high-risk/sanctioned destinations (best-effort basis)
  - Prohibited country destinations block wire progression with error after "Next" action
  - FINTRAC reportability logic conditionally prompts for additional sender details; behavior customizable per institution
  - Fee validation rule: customer-facing fee must ≥ Central 1 processing fee to recover costs

- **Integration Dependencies**:
  - Central 1 correspondent/intermediary banks deduct fees downstream (outside Wires control); FX rates determined post-submission
  - High-priority wires route through Payments Canada Lynx system for participating institutions only; requires authorized user approval pre-processing
  - Future-dated wires require pre-scheduled approval; cancellation requests must reach Central 1 by 2:15 PM PT/11:15 AM ET prior business day (trace request workflow in Chapter 25)
  - Multi-branch access gated by linked transit numbers and permission model

- **Architect Must Know**: Fee structure is split-layer (customer fee input → Central 1 debit to FI account month-end); wire recall/amendment/trace operations are post-release and best-effort dependent on receiving bank cooperation; Future Date has 14-day maximum horizon; foreign currency wires include configurable FX spreads per Chapter 12.