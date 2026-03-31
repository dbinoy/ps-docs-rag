# PS 23:27 Release Summary – Wires Processing Updates

- **Overview**: November 1, 2023 release documenting updates to Wires processing functionality, MemberDirect® Business Services (MDB), and Forge Commercial Wires, aligned with Payment Stream Direct (PSD) UI changes announced August 25, 2023.

- **Key Process Changes**: 
  - Added support for priority regular wires and future-dated regular wires (Sections 16.5-16.6)
  - Added support for priority bank-to-bank wires and future-dated bank-to-bank wires (Sections 17.5-17.6)
  - Enhanced wire cancellation procedures, including approved future-dated wires via ServiceNow integration
  - Wire return functionality now supports both return reason codes and narrative return reasons

- **Critical Authorization & Limits Rules**:
  - Users approving wires in MDB or Forge Commercial must have sufficient transfer and daily limits to approve wires for all associated business customers (Section 8.8)
  - Level 1 Authorization field values in MTS differ based on wire source: applies to MDB/Forge Commercial transits but NOT to in-branch wire transits (Section 9.5)

- **Data Structures & Fields**:
  - Transfer and Daily Limit fields (user-level approval capacity)
  - Level 1 Authorization field (transit-specific, context-dependent application)
  - Wire Priority Section (new)
  - Future Dated Wire Section (new)
  - Return Reason Section with dual input methods (code or narrative)

- **Integration Dependencies**: ServiceNow integration point for future-dated wire cancellation requests; Payments Canada Lynx (high-value system) reference added; MTS (core configuration system) for user and branch settings.

- **Geographic/Scope Constraint**: Removed generalized statement about provincial wire participant restrictions—participants can now operate in any province; deadlines for non-participating Canadian institutions updated to reflect current landscape.