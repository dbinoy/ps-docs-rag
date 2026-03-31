# PS Release 22:04 (January 31, 2022) - Summary

- **Purpose**: Documentation updates to clarify procedures for currency ordering, cash services user management, and cash parcel/counterfeit note handling workflows

- **Key Process Changes**:
  - User profile searches now require explicit "All" status filter selection to retrieve locked profiles; default filtering excludes locked users
  - Discrepancy reporting logic depends on bundle-level granularity: whole bundle discrepancies require parcel tag submission; sub-bundle discrepancies require bundle strap submission

- **Data Dependencies**: Cash parcel discrepancies must map back to originating financial institution via either parcel tag or bundle strap identifiers—RBC integration point for discrepancy resolution

- **External System Dependencies**: 
  - RBC (Royal Bank of Canada) receives parcel tag/bundle strap metadata for financial institution attribution and discrepancy investigation
  - Regional law enforcement (local police department or RCMP) integration for counterfeit note handling procedures; no centralized validation—responses vary by geographic region

- **Constraint**: Counterfeit note procedures are not standardized across regions; implementations must support variable workflows based on local law enforcement directives rather than fixed business logic

- **Data Structures Affected**: User profiles (status field), cash parcels (tag identifiers), bundle handling (strap identifiers), counterfeit note tracking (jurisdiction mapping)

- **Support Contact**: Client Support Services for clarifications (1-888-889-7878 Option 1 or support@central1.com)