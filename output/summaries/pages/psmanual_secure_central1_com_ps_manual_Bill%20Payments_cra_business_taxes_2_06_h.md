# Summary: Examining Remittance Vouchers

- **Purpose**: Describes how to identify CRA remittance voucher types and determine eligibility for electronic processing via Business Taxes; vouchers not supported must be processed manually or via mail/courier.

- **Electronic Processing Workflow**: Form number lookup in Business Taxes determines processing route—supported vouchers proceed to Section 8.2 (file/payment submission), unsupported vouchers follow manual processes (Chapter 9). Language codes (E/F suffix) must be stripped from form numbers during lookup queries.

- **Core Data Structure**: Each remittance voucher contains three required fields: tax program identifier, form number, and Business Number/Account Number (e.g., 123456782RT0001). Form numbers follow pattern `[CODE]-[LANGUAGE]` where language character must be filtered.

- **Tax Program Classification**: Business Number/Account Number uses 2-4 character alpha prefixes (NR, NW, RC, RD, RE, RG, RN, RP, RT, SL) as deterministic identifiers mapping to specific tax programs; NR92 forms require additional `02` or `08` tax program number suffix (formatted as TT02/TT08) rather than relying solely on alpha prefix.

- **Business Rules & Constraints**: System rejects vouchers with zero balance or refund claims; shared form numbers across programs require tax program validation via alpha character lookup table when not explicitly labeled on voucher.

- **Integration Dependencies**: Assumes upstream Business Taxes system maintains authoritative form number registry and electronic processing capability flags; downstream manual processing (Chapter 9) handles unsupported vouchers.

- **Data Validation Critical Path**: Form number normalization (language code removal) → Business Number alpha character mapping → tax program determination → availability check in Business Taxes → routing decision (electronic vs. manual).