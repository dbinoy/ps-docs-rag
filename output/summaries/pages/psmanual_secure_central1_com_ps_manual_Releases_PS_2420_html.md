# PS 24:20 Release Summary (May 7, 2024)

- **Release Scope**: Updated Online Return System (ORS) documentation for cheque return eligibility criteria and clearing/deposits processes

- **Key Process Updated**: Section 9.2 of ORS Part Chapter 9 governs cheque eligibility determination for return transactions—critical validation logic in the return workflow

- **Data Structure Change**: Figure 1 (Eligibility Colour Codes for Return Cycles) was replaced, indicating the visual/coded representation of cheque return states/statuses changed; architects must reference updated documentation for accurate colour-code mappings used in ORS eligibility checks

- **Clearing and Deposits Integration**: Changes affect the clearing and deposits volume workflow; cheque return eligibility directly impacts deposit reconciliation and clearing cycles—timing and state transitions matter for downstream settlement processes

- **Constraint**: Return eligibility is cycle-dependent (Return Cycles referenced in colour codes); architects must account for temporal/cyclical constraints when designing cheque return request logic or status queries

- **Documentation Dependency**: ORS Part Chapter 9 is the source of truth for return eligibility rules; any system interfacing with ORS (deposits, clearing, reconciliation) must align with updated eligibility criteria to avoid return rejections or processing failures

- **Support Contact**: Client Support Services (1-888-889-7878 Option 1, support@central1.com) owns ORS rules interpretation—engage before finalizing designs affecting return flows