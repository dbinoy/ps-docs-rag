# Payment Solutions Release Summary: 21:07 (March 18, 2021)

- **Release scope**: Documentation update to Bill Payment Remittance Processing (BPRP) extending support beyond BC/ON to credit unions in other provinces, with geographic applicability clearly marked throughout.

- **New concept introduced**: "Restricted Entity" classification added to Section 2.1 (Definitions) and Section 3.3, affecting financial institution enrollment policies (Section 4.1); architects should account for entity-type validation in enrollment workflows.

- **Corporate creditor structure**: BPRP now supports flexible agreement models—one corporate creditor agreement per remittance OR single agreement across multiple remittance types, each requiring unique Corporate Creditor Identification Number (CCIN); impacts data model for agreement-to-remittance cardinality.

- **New form artifact**: Letter of Direction – Bill Payment Remittance Processing Cancellation (Form 9310) added to document library; represents new cancellation workflow requiring integration with existing arrangement management (Section 8.2).

- **Tiered service availability**: Chapters 5, 9, 10, 11 (Agreements, Settlement/Tracing, Reports, Data Files) apply only to Central 1 clients in BC/ON; non-Central 1 institutions must route requests/data through provincial centrals—creates architectural dependency on provincial central APIs/intermediaries.

- **Key integration dependency**: File and Report Exchange system (Sections 4.2, 6.7) limited to BC/ON; architects must design conditional logic for report/data file delivery paths based on institution geography and Central 1 affiliation.

- **Process change**: BPRP service requests from non-Central 1 clients now route through provincial centrals (Section 7.1) rather than direct to Central 1; affects request handling, validation, and SLA tracking in downstream systems.