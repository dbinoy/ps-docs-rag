# Release 24:36 Summary – Enterprise Fraud Management Update

- **Scope**: Process change to Auto Risk wire transaction handling in Enterprise Fraud Management (EFM) Part, effective September 23, 2024

- **Auto Risk Scope Narrowed**: Auto Risk flags are now **limited to Interac e-Transfer® transactions only**; all Auto Risk wire references have been removed from EFM documentation and functionality

- **Wire Alert State Machine Change**: Alerted wires transition to "Pending" status (not auto-cancelled) and remain held until fraud analyst adjudication as "Risk" or "No-Risk"; subsequently sent wires after an alerted wire are also flagged and held pending the initial wire's adjudication

- **Process Dependency**: Wire cancellation and settlement workflows must follow institution-specific internal procedures; no automatic settlement occurs on EFM adjudication decisions

- **Documentation Updates**: 
  - Section 8.4: Auto Risk applicability clarified for e-Transfer only
  - Section 8.7: Removed legacy Auto Risk wire logic, added "Subsequently Alerted Wire" scenario definition

- **Integration Point**: Wires application must support Pending status field and coordinate with fraud analyst workflow; settlement system depends on manual cancellation/release decisions rather than automated EFM outputs

- **Support**: Questions directed to EFM@central1.com (no technical integration or API details provided in this release note)