# Payment Solutions Release 23:01 (January 5, 2023) Summary

- **Release scope**: Consolidated current accounts documentation into a new dedicated Part; updated reporting interfaces and deprecated legacy account types (Ontario Banking Services, US Dollar and Pound Sterling accounts, standalone Account Reconciliation).

- **Key structural change**: Created "Central 1 Current Accounts" Part consolidating procedures for account management, inter-branch transfers, corporate client transfers, settlement processes, and reconciliation workflows previously scattered across multiple volumes.

- **Reporting and reconciliation updates**: 
  - Daily settlement reports renamed in Access and Administration Volume (Section 2.1)
  - OREC introduced as a new reconciliation file format requiring integration with existing settlement processes
  - Report presentation examples updated in CBS Online (Chapter 9)

- **Data flow consolidation**: Inter-branch and Central 1 corporate client transfer workflows moved from Electronic Transactions Volume (Wires, Chapter 27) to Central 1 Current Accounts Part; Form 1579 (Central 1 Current Account Transfer) relocated and referenced in new location.

- **Integration point changes**: Two request methods for inter-branch/corporate transfers documented—ServiceNow-based (automated) and manual processes—now centralized in single Part for easier maintenance and discovery.

- **Deprecated integrations**: Removal of legacy account types signals downstream system changes; architects should verify no active implementations depend on Ontario Banking Services, US Dollar, or Pound Sterling account structures.

- **Support handoff**: Client Support Services (1-888-889-7878, Option 1) owns implementation questions; indicates potential breaking changes requiring customer communication.