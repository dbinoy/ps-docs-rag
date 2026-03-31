# Summary: Wires Processing Models Selection & Setup

- **Purpose**: Documents three configurable wires processing architectures (Centralized, Partially Centralized, Decentralized) for multi-branch and single-branch financial institutions, with setup procedures for users, administrators, and branches in MTS.

- **Key Architectural Models**:
  - *Centralized*: Single designated branch (head office) sends/receives all wires for organization; all users operate under one home transit number with "Use Linked Transits" permission
  - *Partially Centralized*: Designated branch handles specific functions (e.g., incoming only) while other branches manage remaining functions (e.g., outgoing); mixed permission assignments by user role and branch
  - *Decentralized*: Each branch independently manages its own wires; no branch linking, no "Use Linked Transits" permission required

- **User & Administrator Requirements**: 
  - Minimum 3 wires users per branch/model (except 1 for incoming-only roles); minimum 2 MTS administrators
  - Permission matrix varies by model: Inbox, Outbox (View/Create/Authorize), Template Management, FX Spreads/Fees management
  - All outgoing wires require 2-Step security token and at least one authorized approver (Chapter 22 dependency)

- **Critical Setup Dependencies**:
  - Authorization limits (Level 1 & Level 2) must be configured *before* first outgoing wire creation per branch
  - Home transit number assignment determines user/admin access scope and branch linking capability
  - "Use Linked Transits" permission is mandatory in centralized/partially centralized models but prohibited in decentralized model

- **MTS Integration Points**: 
  - Wires branch administration, user permissions, and authorization limits managed entirely in MTS
  - Branch linking configuration in MTS Section 9.5 controls outgoing wire behavior across models
  - Template deletion/restoration and FX spread/fee management reference separate administrative chapters

- **Governance Constraint**: Best practice recommendation to designate compliance group for high-value wire review/approval (no enforcement mechanism specified in this section).