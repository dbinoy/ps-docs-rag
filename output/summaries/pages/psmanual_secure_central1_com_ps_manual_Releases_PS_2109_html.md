# Payment Solutions 21:09 Release Summary (March 23, 2021)

- **Purpose**: Documentation updates to the Currency Ordering Part covering cash order management workflows and user account controls within the Payment Solutions system.

- **Key Process Changes**:
  - Cash order location inactivation now requires explicit AFT Desk contact rather than self-service
  - Carrier Check & Released state represents an immutable boundary—orders cannot be edited or deleted post-release, implying state-driven access controls

- **Data Structure Addition**: New optional `Carrier Location` field added to Order Entry form (Section 7.2) to support delivery metadata and routing instructions (e.g., "for ATM 123"), indicating flexible order metadata requirements.

- **User Account State Clarification**: "Inactive" status refined to distinguish locked-out accounts from other inactive states, requiring updated business logic for account unlock procedures (Section 6.7).

- **Integration Dependency**: AFT Desk acts as an external system dependency for cash order location lifecycle management; self-service UI likely lacks this capability.

- **Constraint to Model**: Order state transitions include at least three distinct states (pre-release, Carrier Check & Released, post-release), with enforcement rules preventing mutations after Carrier Check & Released transition.

- **Contact/Support Integration**: Client Support Services (1-888-889-7878, Option 1 / support@central1.com) handles escalations, suggesting support ticketing system dependency.