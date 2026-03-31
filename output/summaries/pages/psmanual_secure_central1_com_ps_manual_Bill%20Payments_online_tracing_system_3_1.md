# Settlement of Trace Request Adjustments and Service Charges - Summary

- **Overview**: Documents the settlement workflow for electronic bill payment trace request adjustments and service charges, including dual settlement pathways to both financial institutions and members.

- **Settlement Trigger & Timing**: Settlement posts automatically when trace request status transitions to "Closed - Settled" state; timing is date-dependent on status change event.

- **Financial Institution Settlement**: Posted to the FI's central credit union account at the branch level, using either the branch associated with the trace request or a FI-specified transit number as the routing identifier.

- **Transit Number as Key Routing Field**: Transit number is the primary routing mechanism for settlement posting; FI-specific transit numbers can be configured via Central 1 Client Support Services—suggests configurable routing rules that must be maintained separately.

- **OLT Reports System Integration**: Daily "Closed - Settled" reports (generated via OLT Reports function in Chapter 10) are the operational source of truth; reports must surface adjustment amount, service charge amount, and transit number for reconciliation and posting.

- **Member Settlement Conditional Logic**: Requires manual review of each "Closed - Settled" trace request against Additional Comments field to determine if member-level posting is required; settlement amount (adjustment and/or service charge) then posted to member account—introduces human decision point in automated workflow.

- **CAS Online Reconciliation Dependency**: Settlement posting must reconcile to Current Account Services (CAS) Online postings; suggests downstream accounting system integration and potential reconciliation gaps if posting fails.