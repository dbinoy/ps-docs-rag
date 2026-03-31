# Payment Solutions Release 21:29 Summary

- **Purpose**: August 5, 2021 release announcement documenting deprecation and removal of seven obsolete payment processing forms from the Payment Solutions Manual and secure document library.

- **Form Lifecycle States**: Two distinct statuses exist—"Obsolete" (no longer needed, safe to destroy) vs. "Unavailable" (removed but occasionally required for internal Central 1 operations), indicating different retention and access policies.

- **Affected Processing Workflows**: Forms covered deposit processing (foreign funds, multi-currency accounts in GBP/CAD/USD/EUR) and returns processing (returned item envelopes, debit re-payment), suggesting these workflows have been migrated to digital/alternative channels.

- **Data Structures Deprecated**: Seven form codes (1107, 1179, 1312, 1346, 1558, 1703, 1705, 2405) should be removed from any downstream systems, document management integrations, or form library references to prevent obsolete data flows.

- **Availability Model Split**: Forms 1107, 1346, 1703, and 1705 remain internally available to Central 1 operations despite public removal, indicating asymmetric access control between client-facing and internal document repositories.

- **Integration Constraint**: Any legacy client integrations or APIs that reference these form codes or deposit slip workflows require migration planning; no backwards compatibility path is documented.

- **Support Dependencies**: Client inquiries regarding form availability or migration path should route to Client Support Services (1-888-889-7878 Option 1) rather than technical support.