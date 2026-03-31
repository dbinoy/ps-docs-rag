# FX Drafts Settlement Summary

- **Purpose**: Documents the settlement flow for foreign exchange drafts between Central 1, member financial institutions, and their customers, including posting mechanics and revenue retention.

- **Settlement Architecture**: Convera generates daily settlement files to Central 1, which debits the FI's CAD/USD account; currency selection (CAD or USD) is configurable per institution at enrollment, not per-draft.

- **Posting Code & Reporting**: Settlements are tagged with code `TD` and appear on institution-specific reports (AIBC/AIBU for BC, AIOC/AIOU for Ontario) accessible via Central 1's File and Report Exchange and CAS Online system.

- **Fee Structure**: Per-item fees are included in settlement amounts; if USD settlement is selected, core platform fees are assessed monthly via AFT to a designated account. Class A credit unions reference Form 2725 for fee schedules.

- **Revenue Model**: Financial institutions retain spread revenue (daily) and fee revenue (daily); no wholesale FX markup deducted at settlement level.

- **Posting Location**: Debits post to either a designated branch (head office) or the originating draft branch based on FI configuration during enrollment.

- **Compliance Dependency**: Member account debits must occur *before* draft issuance; AML/PCMLTFA requirements apply, particularly for foreign fund or cash payments—requires coordination with AML Compliance Officer/FINTRAC.

- **System Dependencies**: Integration with Central 1 Banking System (CAS), File and Report Exchange, and Convera's daily settlement file generation; no mention of real-time settlement or intra-day processing.